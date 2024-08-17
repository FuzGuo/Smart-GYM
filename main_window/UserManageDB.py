import sys
import mysql.connector


class UserManageDatabaseFactory():
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
            return None

    def check_password(self, name, password):
        """检查用户密码"""
        query = f"SELECT * FROM users WHERE name = '{name}' and password = '{password}';"
        results = self.execute_query(query)
        if results:
            return results[0][0]
        else:
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

    def edit_user_info(self, name, password, email, user_id):
        """用户界面-更新用户信息"""
        query = "update users set name = %s , password = %s, email = %s where userid = %s"
        params = (name, password, email, user_id)
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

    def query_user_by_id(self, userid):
        """查询数据库中名字为指定id的用户"""
        query = f"SELECT * FROM users WHERE userid = '{userid}';"
        results = self.execute_query(query)
        if results:
            return results[0]
        else:
            return None

    def query_all(self):
        """查询数据库中的所有用户"""
        query = f"SELECT * FROM users;"
        results = self.execute_query(query)
        if results:
            return results
        else:
            return None

    def delete_user_by_id(self, userid):
        """按照id删除用户"""
        # 使用参数化查询
        query = "DELETE FROM users WHERE userid = %s;"

        # 组织你的数据进一个元组，每个 %s 将由这些值替换
        params = (userid,)

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

    def add_user(self, name, password, email):
        """添加用户"""
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


