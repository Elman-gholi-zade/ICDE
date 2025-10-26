# تابع بخش مخفی
def hide() :
    print()
    print("Hello   !!!")



print( )
print( )
print( )

print("____________________________________________________________________________ Hello Welccome ______________________________________________________________________")

print( )
print( )
print( )
print( )
while True :
    # بخش ورود و خروج
    print("1. Continue ")
    print("2. Exit ")
    print( )

    login = input("Choose : ")
    print( )
    if login=="1":
        # بخش انتخاب عملیات
        operations = input("operation :  ")
        print( )
        # بخش عملیات جمع
        if operations == "+" :
            num_1 = float(input("Enter number one : "))
            print( )
            num_2 = float(input("Enter number two :  "))
            print( )
            addition = num_1 + num_2
            print("-------------------------")
            print(f"{num_1} + {num_2} = {addition} ")
            print("-------------------------")
            print()
            print()


        # بخش عملیات تفریق
        elif operations == "-" :
            num_1 = float(input("Enter number one : "))
            print( )
            num_2 = float(input("Enter number two :  "))
            print( )
            subtraction = num_1 - num_2
            print("-------------------------")
            print(f"{num_1} - {num_2} = {subtraction} ")
            print("-------------------------")
            print(" ")
            print(" ")

        
        # بخش عملیات ضرب
        elif operations == "*" :
            num_1 = float(input("Enter number one : "))
            print( )
            num_2 = float(input("Enter number two :  "))
            print( )
            multiplication = num_1 * num_2
            print("-------------------------")
            print(f"{num_1} * {num_2} = {multiplication} ")
            print("-------------------------")
            print(" ")
            print(" ")

        # بخش عملیات تقسیم
        elif operations == "/" :
            num_1 = float(input("Enter number one : "))
            print( )
            num_2 = float(input("Enter number two :  "))
            print( )
            division = num_1 / num_2
            print("-------------------------")
            print(f"{num_1} / {num_2} = {division} ")
            print("-------------------------")
            print(" ")
            print(" ")


       # بخش مخفی
        elif operations == "0914" :
            hide()


        # پیغام داشتن مشکل
        else :
            print()
            print("Warring ! ")
            print()


# لاگین 2 (برای خروج)
    if login == "2" :
        print("exit 😊")
        break
    