# دیکشنری همه دیتا ها
all_data_dict = {}
# دیکشنری پشتیبانی 
support = {}
# تابع ساختار برنامه
program_structure = "soon"


# تابع رمزگذاری (انگلیسی)
def Password_English_Full_Access() :
    print()
    key_about_Full_Access = input("Enter ""Full Access"" key :  ")
    # "شرط بررسی رمز عبور بخش "دسترسی کامل
    if key_about_Full_Access == "elman 1390" :
        print()
        print("True ✅")
        print()

    else :
        print()
        print("False ⛔")
        try_key_about_Full_Access = input("please try again :  ")
        # "شرط شانس دوباره امتحان رمز عبور بخش "دسنرسی کامل
        if try_key_about_Full_Access == "elman 1390" :
            print("Now True ✅")
            print()
        else :
            print()
            print("False again ⛔ ")
            print()
# تادبع رمزگذاری (انگلیسی)
def Password_English_PS_UI() :               # مخفف  Program structure و  User information
    # تابع درستی سنجی رمز عبور 1 و 2 
    def check_key1_2() :
        # شرط درستی سنجی رمز عبور2 برای بخش "دسترسی کامل - PS_UI"
        key_2_PS_UI_Full_access = input ("Enter key 2 :  ")
        if key_2_PS_UI_Full_access == "elman 1390" :
            print()
            print("True ✅")
            print()
            print(connector)

        else :
            print()
            print("False ⛔")
            try_key_2_PS_UI_Full_access = input("please try again :  ")
                # شرط درستی سنجی رمز عبور2 برای بخش "دسترسی کامل - PS_UI"
            if try_key_2_PS_UI_Full_access == "elman 1390" :
                print("Now True ✅")
                print()
                print(connector)
                print()
            else :
                print()
                print("False again ⛔ ")
                print()

    key_1_PS_UI_Full_access = input("Enter key 1 :  ")
    if key_1_PS_UI_Full_access == "fire 201.40.78" :
        print()
        print("True ✅")
        print()
        print()
        check_key1_2()



    else :
        print("False ⛔")
        key_1_PS_UI_Full_access = input("please try again :  ")
        if key_1_PS_UI_Full_access == "fire 201.40.78" :
            print()
            print("Now True ✅")
            print()
            print()
            check_key1_2()



# تابع رمزگذاری (فارسی)
def Password_Persian_Full_Access() :
    print()
    print()
    key_about_Full_Access = input("رمز عبور بخش ""دسترسی کامل"" را وارد کنید :  ")
    # "شرط بررسی رمز عبور بخش "دسترسی کامل
    if key_about_Full_Access == "elman 1390" :
        print()
        print("صحیح می باشد ✅")
        print()

    else :
        print()
        print("اشتباه می باشد ⛔")
        try_key_about_Full_Access = input("لطفا یک بار دیگر تلاش کنید :  ")
        # "شرط شانس دوباره امتحان رمز عبور بخش "دسنرسی کامل
        if try_key_about_Full_Access == "elman 1390" :
            print("الان درست شد ✅")
            print()
        else :
            print()
            print("دوباره اشتباه می باشد ⛔ ")
            print()
# تابع رمزگذاری (فارسی)
def Password_Persian_PS_UI() :               # مخفف  Program structure و  User information
    # تابع درستی سنجی رمز عبور 1 و 2 
    def check_key1_2() :
        # شرط درستی سنجی رمز عبور2 برای بخش "دسترسی کامل - PS_UI"
        key_2_PS_UI_Full_access = input ("رمز عبور شماره 2 را وارد کنید :  ")
        if key_2_PS_UI_Full_access == "elman 1390" :
            print()
            print("درست می باشد ✅")
            print()
            print(connector)

        else :
            print()
            print("اشتباه می باشد ⛔")
            try_key_2_PS_UI_Full_access = input("لطفا دوباره امتحان کنید :  ")
                # شرط درستی سنجی رمز عبور2 برای بخش "دسترسی کامل - PS_UI"
            if try_key_2_PS_UI_Full_access == "elman 1390" :
                print("الان درست شد ✅")
                print()
                print(connector)
                print()
            else :
                print()
                print("دوباره اشتباه می باشد ⛔ ")
                print()

    key_1_PS_UI_Full_access = input("رمزعبور شماره 1 را وارد کنید :  ")
    if key_1_PS_UI_Full_access == "fire 201.40.78" :
        print()
        print("درست می باشد ✅")
        print()
        print()
        check_key1_2()



    else :
        print("اشتباه می باشد ⛔")
        key_1_PS_UI_Full_access = input("رمزعبور شماره 1 را وارد کنید :  ")
        if key_1_PS_UI_Full_access == "fire 201.40.78" :
            print()
            print(" الان درست شد ✅")
            print()
            print()
            check_key1_2()


# بخش اتخاب زبان
print()
print("1. English \n2. فارسی")
print()
language = input("Enter language :   ")
# شرط اتخاب زبان (انگلیسی)
if language == "1" :


    while True :
        #(ورود) شرط مربوط به صفحه ورود/خروج
        print("1. continue \n   2. exit \n       3. about \n            4. support  ")
        login = input("chosse :  ")
        if login == "1" :                
            while True :
                print("-------------- Hello Welcome to Data App -------------")

                print()
                print()
                print()

                # بخش انتخاب خدمات
                print("app aptions :")
                print()
                print("1. add data   \n    2. remove data   \n        3. see data   \n           e. exit" )
                print()
                data_aption_chosse = input("your chosse aption :  ")
                print()
                print()

                # شرط اول ( مربوط به بخش انتخاب عملیات _ آپشن 1 )
                if data_aption_chosse == "1" :
                    data_name = input("Enter data name :  ")
                    data_key = input("Enter your data key :  ")
                    data = input("Enter your data : ")

                    # اضافه کردن به دیکشنری اصلی
                    all_data_dict[data_name] = {"data key " : data_key, "data " :data }
                    print("append ✅")
                    print()
                    print()
                

                # (شرط دوم (مربوط به بخش عملیات _ آپشن 2
                elif data_aption_chosse == "2" :
                    remove_data_name = input("Enter data name :  ")
                    print()
                    # شرط مربوط به آپشن 2 از بخش عملیات برای حدف دیتا
                        # شرط تشخیص درست بودن رمز عبور دیتا برای حذف دیتا کاربر
                    if remove_data_name in all_data_dict :
                        remove_data_key = input("Enter data key :  ")
                        if remove_data_key == all_data_dict[data_name(data_key)] :
                            sure_remove_data = input("Are you sure to clear this data ? (y/n) ")
                            if sure_remove_data == "y" :
                                print()
                                del all_data_dict[(data_name)]
                                print()
                                print("data cleared ❎")
                        
                            elif sure_remove_data == "n" :
                                print("Ok. data don't deleted ✅")
                                print()
                        else:
                            print("key false !")
                    else :
                        print("data name not found !")



                #( مربوط به مشاهده دیتا توسط کاربر برای کاربر ) شرط سوم 
                elif data_aption_chosse == "3" :
                    see_data_key = input("Enter data key :  ")
                    print()
                    # شرط مربوط به آپشن 3 از بخش عملیات برای نمایش دیتا به کاربر
                    if see_data_key == data_key :
                        print("True ✅")
                        data_name = input("Enter data name :  ")
                        print(all_data_dict.get(data_name, "Not found ⛔"))
                    else :
                        print()
                        print("key false ⛔ !")


                elif data_aption_chosse == "e" :
                    break


                else :
                    print("type Error !")



        #(خروج) شرط مربوط به صفحه ورود/خروج
        if login == "2" :
            print()
            print("exited")
            break





        #(درباره برنامه) شرط مربوط به صفحه ورود/خروج
        if login == "3" :
            while True :
                print()
                print()
                print("Access this section :")
                print()
                print("A password is required, But you can also view limited infomation without signing in .")
                print()
                print("1. sign in with password \n2. continue without password. (partial infomation) ")
                print()
                about_chosse_aption = input("Chosse an aption :  ")
                print()

                # شرط مشخص کننده نوع ارایه اطلاعات برنامه
                # با رمز عبور
                if about_chosse_aption == "1" :
                    print()
                    print()
                    Password_English_Full_Access()

                    # شرطی که وقتی رمز عبور بخش "دسترسی کامل" صحیح باشد بقیه کدها را اجرا میکند
                    print("Full Access ")
                    print()
                    print("Hello, you are now in the main section whit full control of the app.")
                    print()
                    print("you have full access to all the code of this app,")
                    print("as well as the most sensitive and secure area, protected whit strong two-step encryption.")
                    print()
                    print("1. Program structure (soon) \n2. User information (soon)")
                    print()

                    # "شرط انتخاب آپشن های بخش "دسترسی کامل
                    # (1)"شرط انتخاب آپشن های بخش "دسترسی کامل
                    choosse_aption_Full_access = input("Chosse an aption :  ")
                    if choosse_aption_Full_access == "1" :
                        # وصل کردن ساختار برنامه
                        connector = program_structure
                        print()
                        Password_English_PS_UI()



                    # (2)"شرط انتخاب آپشن های بخش "دسترسی کامل
                    elif choosse_aption_Full_access == "2" :
                        # وصل کردن به اطلاعات کاربران
                        connector = all_data_dict
                        print()
                        Password_English_PS_UI()


                elif about_chosse_aption == "e" :
                    break
                

                else :
                    print("type error ! ")
                        


                   








            # بدون رمز عبور(به صورت جزیی)
            if about_chosse_aption == "2" :
                print()
                print("Pratial infomation ")
                print()
                print("This app was created by Elman Gholi zade in 2025/3/20 .")
                print("It is an app where you can save any text, number, Email \nor other information whit a name and password that you chosse.")
                print()
                print()
        




        # ( بخش پشتیبانی ) شرط مربوط به صفحه ورود/خروج
        if login == "4" :
            while True:
                # انتخاب آپشن بخش پشتیبانی
                print()
                print("1. Share your thoughts \n 2. Edit your comment(coming soon) \n  3. See other's thoughts (will completely)")
                print()
                #(شرط یخش پشتیبانی - آپشن 1 (ارسال نظر  
                send_thoughts = input("Chosse :  ")
                print()
                if send_thoughts == "1" :
                    print()
                    print("Support Section ")
                    print()
                    print("You thoughts is very valuable To us.")
                    print("Please share your thoughts about this app : ")
                    print()
                    comment = input("  your comment →→ ")
                    print()
                    name = input("Enter your name : ")
                    print()
                    date = input("Enter date : ")
                    print()
                    print("Send ✅ \nThanks for you thoughts ")
                    print()
                    # ارسال نظر به دیکشنری نظرات
                    support[comment] = {"name " : name , "date " : date}




                # شرط بخش پشتیبانی - آپشن 2 ( ویرایش کامنت خود )
                elif send_thoughts == "2" :
                    print()
                    print("Edit Comment")
                    print()
                    comment = input("Enter comment :  ")
                    print(support.get(comment, "No this comment from this name yet. 🚫"))
                    print()
                    comment = input("New comment :  ")
                    name = input("New name :  ")
                    date = input("Enter date :  ")
                    support[comment] = {"name " : name , "date " : date}
                    


                #(شرط بخش پشتیبانی - آپشن 3 ( دیدن نظرات دیگران  
                elif send_thoughts == "3" :
                    print()
                    print("Comments")
                    print()
                    for show_comment in support :
                        print(show_comment)
                    print("This feature will  be gooded in future update. 🚀") 
                    print()



                elif send_thoughts == "e" :
                    break


                else :
                    print("type error")












# شرط اتخاب زبان (فارسی)
if language == "2" :
    print()
    print()
    while True :
        #(ورود) شرط مربوط به صفحه ورود/خروج
        print("1. ادامه \n   2. خارج شدن \n       3. درباره \n            4. پشتیبانی  ")
        login = input("chosse :  ")
        if login == "1" :
            while True :    
                print("-------------- سلام به برنامه Data app خوش آمید -------------")

                print()
                print()
                print()

                # بخش انتخاب خدمات
                print("آپشن های برنامه :")
                print()
                print("1. اضافه کردن دیتا :  \n    2. حذف دیتا :  \n        3. دیدن دیتا :  " )
                print()
                aption_chosse = input("آپشن مورد نظر شما:  ")
                print()
                print()
                # شرط اول ( مربوط به بخش انتخاب عملیات _ آپشن 1 )
                if aption_chosse == "1" :
                    data_name = input("نام دیتا خود را وارد کنید :  ")
                    data_key = input("رمز عبور دیتا خود را وارد کنید :  ")
                    data = input("دیتا خود را وارد کنید : ")

                    # اضافه کردن به دیکشنری اصلی
                    all_data_dict[data_name] = {"رمز عبور  " : data_key, "دیتا " :data }
                    print("اضافه شد ✅")
                    print()
                    print()
                

                # (شرط دوم (مربوط به بخش عملیات _ آپشن 2
                elif aption_chosse == "2" :
                    remove_data_name = input("نام دیتا را وارد کنید :  ")
                    remove_data_key = input("رمز عبور را وارد کنید :  ")
                    print()
                    sure_remove_data = input("آیا از حذف این دیتا مطمین هستید ? (y/n) ")
                    # شرط مربوط به آپشن 2 از بخش عملیات برای حدف دیتا
                    if sure_remove_data == "y" :
                        print()
                        # شرط تشخیص درست بودن رمز عبور دیتا برای حذف دیتا کاربر
                        if remove_data_key == data_key :
                            del all_data_dict[(data_name)]
                            print()
                            print("دیتا حذف شد ❎")
                    
                    elif sure_remove_data == "n" :
                        print("باشه. دیتا حذف نشد ✅")
                        print()




                #( مربوط به مشاهده دیتا توسط کاربر برای کاربر ) شرط سوم 
                elif aption_chosse == "3" :
                    data_name = input("نام دیتا را وارد کنید :  ")
                    data_key = ("رمز عبور را وارد کنید :  ")
                    print()
                    # شرط مربوط به آپشن 3 از بخش عملیات برای نمایش دیتا به کاربر
                    if data_key == data_key :
                        print()
                        print(all_data_dict.get(data_name, "دیتا یافت نشد ⛔"))
            

                elif aption_chosse == "e" :
                    break


                else :
                    print("خطای تایپ !")


        #(خروج) شرط مربوط به صفحه ورود/خروج
        if login == "2" :
            print()
            print("exited")
            break






        #(درباره برنامه) شرط مربوط به صفحه ورود/خروج
        if login == "3" :
            while True :
                print()
                print()
                print("دسترسی به این بخش :")
                print()
                print("برای ورود به این بخش رمز عبور لازم استو اما میتوانید بدون رمز عبور اطلاعات جزیی را ببینید .")
                print()
                print("1. ورود با رمز عبور \n2. ورود بدون رمز عبور. (اطلاعات جزیی) ")
                print()
                about_chosse_aption = input("یک گزینه را انتخاب کنید :  ")
                print()

                # شرطی که وقتی رمز عبور بخش "دسترسی کامل" صحیح باشد بقیه کدها را اجرا میکند
                # شرط مشخص کننده نوع ارایه اطلاعات برنامه
                # با رمز عبور
                if about_chosse_aption == "1" :
                    print()
                    Password_Persian_Full_Access()
                    print("دسترسی کامل ")
                    print()
                    print("سلام, شما الان در بخش اصلی با کنترل کامل برنامه هستید.")
                    print()
                    print("شما به تمام کدهای این برنامه دسترسی کامل دارید")
                    print("و همچنین حساس ترین وامن ترین بخش, محافظت شده با رمزگذاری دو مرحله ای قوی.")
                    print()
                    print("1. ساختار برنامه (بزودی) \n2. اطلاعات کاربران (بزودی)")
                    print()

                    # "شرط انتخاب آپشن های بخش "دسترسی کامل
                    # (1)"شرط انتخاب آپشن های بخش "دسترسی کامل
                    choosse_aption_Full_access = input("یک گزینه را انتخاب کنید :  ")
                    if choosse_aption_Full_access == "1" :                    
                        # وصل کردن ساختار برنامه
                        connector = program_structure
                        print()
                        Password_Persian_PS_UI()
                    # (2)"شرط انتخاب آپشن های بخش "دسترسی کامل
                    elif choosse_aption_Full_access == "2" :
                        # وصل کردن به اطلاعات کاربران
                        connector = all_data_dict
                        print()
                        Password_Persian_PS_UI()

                    else :
                        print("خطای تایپ !")




                

                # بدون رمز عبور(به صورت جزیی)
                elif about_chosse_aption == "2" :
                    print()
                    print("اطلاعات جزیی ")
                    print()
                    print("این برنامه توسط ' ایلمان گلی زاده ' در تاریخ 1404/6/20 استارت خورده شد.")
                    print("این برنامه ای است که میتوانید درآن متن, شماره, ایمیل یا اطلاعات دیگری با نام و رمز عبوری که خودتان تعیین میکنید, ذخیره کنید.")
                    print()
                    print()
            

                elif about_chosse_aption == "e" : 
                    break

                else :
                    print("خطای تایپ !")



        # ( بخش پشتیبانی ) شرط مربوط به صفحه ورود/خروج
        if login == "4" :
            while True :
                # انتخاب آپشن بخش پشتیبانی
                print()
                print("1.ارسال نظر خود \n 2. (بزودی)ویرایش نطر خود\n  مشاهده نظرات دیگران (کامل خواهد شد)")
                print()
                #(شرط یخش پشتیبانی - آپشن 1 (ارسال نظر  
                send_thoughts = input("انتخاب کنید :  ")
                print()
                if send_thoughts == "1" :
                    print()
                    print("بخش پشتیبانی ")
                    print()
                    print("نظر شما برای ما بسیار مهم است.")
                    comment = input("لطفا نظر خود را درباره این برنامه بنویسید : \n   →→")
                    print()
                    name = input("نام خود را وارد کنید : ")
                    print()
                    date = input("تاریخ را وارد کنید : ")
                    print()
                    print("ارسال شد ✅ \nاز نظر دادن شما ممنون هستیم ")
                    print()
                    # ارسال نظر به دیکشنری نظرات
                    support[comment] = {"نام " : name , "تاریخ " : date}




                # شرط بخش پشتیبانی - آپشن 2 ( ویرایش کامنت خود )
                elif send_thoughts == "2" :
                    print()
                    print("ویرایش نظر")
                    print()
                    comment = input("نظر خود را وارد کنید :  ")
                    print(support.get(comment, "هنوز نظری از این اسم وجود ندارد. 🚫"))
                    print()
                    name = input("اسم جدید را وارد کنید :  ")
                    comment = input("نظر جدید را وارد کنید :  ")
                    date = input("تاریخ را وارد کنید :  ")
                    support[name] = {"نام " : name , "تاریخ " : date}
                    


                #(شرط بخش پشتیبانی - آپشن 3 ( دیدن نظرات دیگران  
                elif send_thoughts == "3" :
                    print()
                    print("نظرات")
                    print()
                    for show_comment in support :
                        print(show_comment)
                    print("این ویژگی در آپدیت های جدید بهتر خواهد شد. 🚀") 
                    print()


                elif about_chosse_aption == "e" : 
                    break


                else :
                    print("خطای تایپ !")