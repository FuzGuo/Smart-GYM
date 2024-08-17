from datetime import datetime
import sys
import mysql.connector


class PostManageDatabaseFactory():
    def __init__(self):
        super().__init__()
        # 尝试连接数据库
        self.db = self.connect_database()

    def connect_database(self):
        """尝试连接到数据库，并返回连接对象"""
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="root",
                database="exercise"
            )
            return connection
        except mysql.connector.Error as err:
            print(err)
            print(f"Failed to connect to database: {str(err)}")
            return None

    def execute_query(self, query):
        """执行SQL查询并返回结果"""
        try:
            cursor = self.db.cursor()
            cursor.execute(query)
            return cursor.fetchall()  # 返回查询结果
        except mysql.connector.Error as err:
            print("Error:", err)
            return None

    def query_user_by_name(self, name):
        """查询数据库中名字为指定字符的用户"""
        query = f"SELECT * FROM users WHERE name = '{name}';"
        results = self.execute_query(query)
        if results:
            return results[0]
        else:
            print("No users found or an error occurred.")
            return None

    def check_password(self, name, password):
        """检查用户密码"""
        query = f"SELECT * FROM users WHERE name = '{name}' and password = '{password}';"
        results = self.execute_query(query)
        if results:
            return results[0][0]
        else:
            print("Password Error.")
            return None

    def reset_password(self, name, password):
        """重置密码"""
        query = "update users set password = %s where name = %s"
        params = (password, name)
        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.lastrowid  # 可用于INSERT操作，返回插入行的ID
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def user_register(self, name, password, email):
        """用户注册"""
        # 使用参数化查询
        query = "INSERT INTO users(name, password, email) VALUES (%s, %s, %s);"
        params = (name, password, email)
        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.lastrowid  # 可用于INSERT操作，返回插入行的ID
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def upload_avatar(self, avatar_path, user_id):
        """上传头像"""
        query = "update users set avatar = %s where userid = %s"
        params = (avatar_path, user_id)
        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.lastrowid  # 返回插入行的ID
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def save_user_info(self, name, gender, age, email, user_id):
        """用户界面-更新用户信息"""
        query = "update users set name = %s , gender = %s,age = %s,email = %s where userid = %s"
        params = (name, gender, age, email, user_id)
        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.lastrowid  # 返回插入行的ID
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def query_post_by_id(self, userid):
        """查询数据库中指定id的帖子"""
        query = f"SELECT * FROM posts WHERE authorid = '{userid}';"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_post_by_post_id(self, post_id):
        """查询数据库中指定id的帖子"""
        query = f"SELECT * FROM posts WHERE postid = '{post_id}';"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_comment_by_comment_id(self, comment_id):
        """查询数据库中指定id的帖子"""
        query = f"SELECT * FROM comments WHERE commentid = '{comment_id}';"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None



    def query_user_by_id(self, userid):
        """查询数据库中名字为指定id的用户"""
        query = f"SELECT * FROM users WHERE userid = '{userid}';"
        results = self.execute_query(query)
        if results:
            return results[0]
        else:
            return None

    def query_comment_by_comment_id(self, commentid):
        """查询数据库中评论为指定id的评论"""
        query = f"SELECT comments.commentid, comments.postid, comments.authorid, comments.content, comments.publishtime, comments.media, users.avatar, users.userid FROM comments join users on comments.authorid = users.userid WHERE commentid = '{commentid}';"
        results = self.execute_query(query)
        if results:
            return results[0]
        else:
            return None

    def query_comment_by_post_id(self, postid):
        """查询数据库中指定帖子id的评论"""
        query = f"SELECT comments.commentid, comments.postid, comments.authorid, comments.content, comments.publishtime, comments.media, users.avatar, users.name FROM comments join users on comments.authorid = users.userid WHERE postid = '{postid}';"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_all_posts(self):
        """返回所有的帖子"""
        query = f"SELECT * FROM posts"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_all_comments(self):
        """返回所有的评论"""
        query = f"SELECT * FROM comments"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def delete_post(self, post_id):
        """按照id删除帖子"""
        self.delete_comment_by_post_id(post_id)
        # 使用参数化查询
        query = "DELETE FROM posts WHERE postid = %s;"

        # 组织你的数据进一个元组，每个 %s 将由这些值替换
        params = (post_id,)

        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.rowcount  # 返回受影响的行数
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def delete_comment_by_post_id(self, post_id):
        """按照帖子id删除评论"""
        # 使用参数化查询
        query = "DELETE FROM comments WHERE postid = %s;"

        # 组织你的数据进一个元组，每个 %s 将由这些值替换
        params = (post_id,)

        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.rowcount  # 返回受影响的行数
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def add_new_post(self, userid, title, content):
        """添加帖子"""
        # 使用参数化查询
        query = "INSERT INTO posts(authorid, title, content, publishtime) VALUES (%s, %s, %s, %s);"
        publishtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间并格式化
        params = (userid, title, content, publishtime)  # 传递正确的参数

        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.lastrowid  # 可用于INSERT操作，返回插入行的ID
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def add_new_comment(self, post_id, userid, content):
        """添加评论"""
        # 使用参数化查询
        query = "INSERT INTO comments(postid, authorid, content, publishtime) VALUES (%s, %s, %s, %s);"
        publishtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间并格式化
        params = (post_id, userid, content, publishtime)  # 传递正确的参数

        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.lastrowid  # 可用于INSERT操作，返回插入行的ID
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def edit_post(self, title, content, post_id):
        """修改帖子"""
        query = "update posts set title = %s , content = %s where postid = %s"
        params = (title, content, post_id)
        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            return cursor.lastrowid  # 返回插入行的ID
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            return None

    def add_comment(self, content, userid, post_id):
        """添加评论"""
        # 使用参数化查询
        query = "INSERT INTO comments(authorid, content, publishtime, postid) VALUES (%s, %s, %s, %s);"
        publishtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间并格式化
        params = (userid, content, publishtime, post_id)  # 传递正确的参数

        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务

        query = "update posts set comments_count = comments_count + 1 where postid = %s;"

        # 组织你的数据进一个元组，每个 %s 将由这些值替换
        params = (post_id,)

        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            # return cursor.rowcount  # 返回受影响的行数
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            # return None

    def delete_comment(self, comment_id, post_id):
        """删除某个评论"""
        # 使用参数化查询
        query = "DELETE FROM comments WHERE commentid = %s;"

        # 组织你的数据进一个元组，每个 %s 将由这些值替换
        params = (comment_id,)

        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            # return cursor.rowcount  # 返回受影响的行数
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            # return None

        query = "update posts set comments_count = comments_count - 1 where postid = %s;"

        # 组织你的数据进一个元组，每个 %s 将由这些值替换
        params = (post_id,)

        # 执行查询并传入参数
        try:
            cursor = self.db.cursor()
            cursor.execute(query, params)  # 传入参数
            self.db.commit()  # 确保提交事务
            # return cursor.rowcount  # 返回受影响的行数
        except mysql.connector.Error as err:
            print("Error:", err)
            self.db.rollback()  # 出错时回滚事务
            # return None



