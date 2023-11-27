import mysql.connector

class My_DB:
    def __init__(self):
        # Connect to the MySQL server
        self.conn = mysql.connector.connect(host='localhost', user='root', password='password')
        self.cursor = self.conn.cursor()

        # Create a new database (if not exists)
        create_database_query = "CREATE DATABASE IF NOT EXISTS vaticai_db"
        self.cursor.execute(create_database_query)

        # Use the database
        use_database_query = "USE vaticai_db"
        self.cursor.execute(use_database_query)

        # Create a user
        create_user_query = "CREATE USER IF NOT EXISTS 'vaticai_user'@'localhost' IDENTIFIED BY 'vaticai_password'"
        self.cursor.execute(create_user_query)

        # Grant necessary privileges to the user
        grant_privileges_query = "GRANT ALL PRIVILEGES ON vaticai_db.* TO 'vaticai_user'@'localhost'"
        self.cursor.execute(grant_privileges_query)

        # Flush privileges to apply changes
        flush_privileges_query = "FLUSH PRIVILEGES"
        self.cursor.execute(flush_privileges_query)

        # Commit the changes
        self.conn.commit()

        # Close the connection
        self.conn.close()

    def validate_user(self, userName, userPassword):
        if userName != 'vaticai_user':
            return "Invalid User"
        if userPassword != 'vaticai_password':
            return "Invalid Password for user vaticai_user"
        
        self.conn = mysql.connector.connect(host='localhost', user=userName, password=userPassword)
        self.cursor = self.conn.cursor()

        # Use the database
        use_database_query = "USE vaticai_db"
        self.cursor.execute(use_database_query)

        # Create a new Table for users Data (if not exists)
        create_table_query = "CREATE TABLE IF NOT EXISTS vaticai_users(username varchar(50), password varchar(50))"
        self.cursor.execute(create_table_query)
        self.conn.commit()

        return "Success"
    
    def add_user(self, username, password):
        new_user_query = "INSERT INTO vaticai_users VALUES(%s, %s)"
        user_data = (username, password)
        self.cursor.execute(new_user_query, user_data)
        self.conn.commit()

    def getAllUsers(self):
        get_user_query = "SELECT * FROM vaticai_users"
        self.cursor.execute(get_user_query)
        users = self.cursor.fetchall()
        return users

    def closeDB(self):
        pass
 