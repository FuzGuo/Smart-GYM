import sys
from datetime import datetime

import PySide6
import mysql.connector
from PySide6.QtCore import QDate


class RecordManageDatabaseFactory():
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
        # 组织你的数据进一个元组，每个 %s 将由这些值替换
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
            print("No posts.")
            return None



    def query_user_by_id(self, userid):
        """查询数据库中名字为指定id的用户"""
        query = f"SELECT * FROM users WHERE userid = '{userid}';"
        results = self.execute_query(query)
        if results:
            return results[0]
        else:
            print("No users found or an error occurred.")
            return None

    def query_comment_by_comment_id(self, commentid):
        """查询数据库中评论为指定id的评论"""
        query = f"SELECT comments.commentid, comments.postid, comments.authorid, comments.content, comments.publishtime, comments.media, users.avatar, users.userid FROM comments join users on comments.authorid = users.userid WHERE commentid = '{commentid}';"
        results = self.execute_query(query)
        if results:
            return results[0]
        else:
            print("No users found or an error occurred.")
            return None

    def query_comment_by_post_id(self, postid):
        """查询数据库中指定帖子id的评论"""
        query = f"SELECT comments.commentid, comments.postid, comments.authorid, comments.content, comments.publishtime, comments.media, users.avatar, users.name FROM comments join users on comments.authorid = users.userid WHERE postid = '{postid}';"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_plan_by_user_id(self, userid):
        """查询数据库中指定用户id的plan"""
        query = f"SELECT * FROM plans WHERE userid = '{userid}';"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_tasks_by_user_id(self, userid):
        """查询数据库中指定用户id的task"""
        query = f"SELECT * FROM tasks join exercise_types on tasks.exercise_id = exercise_types.exercise_id WHERE userid = '{userid}';"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_tasks_by_user_id_and_date(self, userid, date):
        query = f"SELECT * FROM tasks join exercise_types on tasks.exercise_id = exercise_types.exercise_id WHERE userid = '{userid}' and task_date = '{date}';"

        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_record_by_user_id_and_date(self, userid, date):
        query = f"SELECT * FROM records join exercise_types on records.exercise_type = exercise_types.exercise_id WHERE userid = '{userid}' and record_date = '{date}';"

        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_record_by_user_id_and_month(self, userid, month):
        query = f"SELECT * FROM records WHERE userid = '{userid}' AND DATE_FORMAT(record_date, '%Y-%m') = '{month}' ORDER BY record_datetime DESC;"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def query_month_record_by_user(self, userid):
        """按月查询，第一列月份，第二列秒数，第三列消耗卡路里数，第四列次数"""
        query = f"SELECT DATE_FORMAT(record_date, '%Y-%m') AS month, SUM(total_seconds) AS total_seconds, SUM(calories_burned) AS total_calories_burned ,count(*)  AS count FROM records WHERE userid = '{userid}' GROUP BY DATE_FORMAT(record_date, '%Y-%m') ORDER BY month DESC ;"

        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def total_record(self, userid):
        """总结日报生成"""
        query = f"SELECT SUM(calories_burned) AS total_calories_burned, SUM(total_seconds) AS total_exercise_seconds FROM records WHERE userid = '{userid}';"

        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def add_record(self, userid, exercise_type, action_count, calories_burned, total_seconds):
        """添加新的记录"""
        current_datetime = datetime.now()
        record_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        record_date = current_datetime.strftime("%Y-%m-%d")
        feedback = None  # Feedback is not required, so we set it to None

        query = """
        INSERT INTO records (userid, exercise_type, record_datetime, action_count, calories_burned, feedback, total_seconds, record_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        params = (userid, exercise_type, record_datetime, action_count, calories_burned, feedback, total_seconds, record_date)

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



# pm = RecordManageDatabaseFactory()
# print(pm.query_record_by_user_id_and_date(11,QDate.currentDate().toString(format=PySide6.QtCore.Qt.DateFormat.ISODate)))
# print(pm.query_month_record_by_user(11))
# print(pm.query_record_by_user_id_and_month(11, a[1][0]))

# pm = RecordManageDatabaseFactory()
# print(pm.total_record(11))
