import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',
                                   auth_plugin='mysql_native_password',
                                   user='root',password='prince@191',
                                   database='pythontest')
        query='Create table if not exists user(userId int primary key,userName varchar(200), phone varchar(12))'     
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")                     

    #Insert
    def insert_user(self,userid,username,phone):
        query="Insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        # print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to database")
        

    #Fetch All
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        
        for row in cur:
            print("UserId : ",row[0])
            print("UserName : ",row[1])
            print("Phone : ",row[2])
            print()
              
    #Delete User
    def delete_user(self,userId):
        query="delete from user where userId={}".format(userId)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")
    
    #Update USer
    def update_user(self,userId,newName,newPhone):
        query="update user set userName='{}',phone='{}'where userId={}".format(newName,newPhone,userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
            
        