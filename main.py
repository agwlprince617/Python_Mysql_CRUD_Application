from dbhelper import DBHelper


def main():
    db=DBHelper()
    while True:
        print("*********WELCOME*********")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display all users")
        print("Press 3 to delete existing user")
        print("Press 4 to update existing user")
        print("Press 5 to exit the program")
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid=int(input("Enter user id: "))
                username=input("Enter user name :")
                userphone=input("Enter user phone: ")
                db.insert_user(uid, username, userphone)
                pass
            elif choice==2:
                #display
                db.fetch_all()
                pass
            elif choice==3:
                #delete
                uid=int(input("Enter user id you want to delete"))
                db.delete_user(uid)
                pass
            elif choice==4:
                #update
                uid=int(input("Enter user id for which the details need to be updated: "))
                username=input("Enter new user name :")
                userphone=input("Enter user new phone: ")
                db.update_user(uid, username, userphone)
                pass
            elif choice==5:
                #exit
                break
            else:
                print("Invalid input try once again")
                
        except Exception as e:
            print(e)
            print("Invalid details!! Try Again")
  
if __name__ == '__main__':
    main()            