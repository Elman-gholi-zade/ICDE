
# دیکشنری مدیریت ژتون  
Token_dict = {}
# دیکشنری مدیریت فالور
Follower_dict = {}

print('...........Welcome................... HELLO .................Welcome............')

print()
print()
# انتخاب بخش 
while True :
    section = input("1. Token \n2. Fllower  \n3. exit \nchosse :  ")
    print()
    # شرط انتخاب بخش

    # بخش 1 : ژتون
    if section == "1" :
        print()
        # انتخاب آپشن بخش ژتون
        print("option :")
        print()
        print(" 1. append \n    2. see \n       3. see one \n          4. update \n             5. remove")
        print()
        choose_aption_Token = input("Choose :  ")
        print()

        #  ( اضافه کردن ژتون) شرط اول
        if choose_aption_Token == "1" :
            Follower_name = input("Enter Follower name :  ")
            Follower_Token = input("Enter Token count :  ")
            Token_date = input("Enter date :  ")
            print()
            
            # ساخت دیکشنری کوچک و اضافه کردن آن به فالور ها  
            Token_dict[Follower_name] = {"Token count " : Follower_Token, "Token date " : Token_date}
            print("append ✅")
            print()
            print()
        # شرط دوم (دیدن تعداد ژتون های فالور)
        if choose_aption_Token == "2" :
            for Follower_name in Token_dict :    
                print(Follower_name , ":" , Follower_Token)



        # شرط سوم (دیدن تعداد ژتون یک نفر خاص)
        if choose_aption_Token == "3" :
            print()
            print()
            Follower_name = input("Enter Folower name :  ")
            print(Token_dict.get(Follower_name, "This task doesn't exist ! "))



        # شرط چهارم (بروزرسانی اطلاعات)
        if choose_aption_Token == "4" :
            print()
            Token_dict[Follower_name] = {"Token count " : Follower_Token, "date " : Token_date} 
            print()   
            Follower_name = input("Enter new follower name :  ")
            Follower_Token = input("Enter new token count :  ")
            Token_date = input("Enter new Token date :  ")
            # آپدیت اطلاعات کاربر
            print()
            Token_dict[Follower_name] = {"Token count " : Follower_Token, "Token date " : Token_date}
            print()

        # شرط پنجم (حذف فالور)
        if choose_aption_Token == "5" :
            print()
            Follower_name = input("Enter fllower name :  ")
            delete_Follower = input("Are you sure to delete this follower ?  (y/n)")
            # شرط اطمینان از حذف فالور
            if delete_Follower == "n":
                print()
                print("Ok ✅")
                print()
            else :
                print()
                



    # بخش 2 : فالور
    if section == "2" :
        pass










    # بخش 2 : خروج
    if section == "3" :
        print()
        print()    
        print()
        print()
        print("exit  🔚")
        break