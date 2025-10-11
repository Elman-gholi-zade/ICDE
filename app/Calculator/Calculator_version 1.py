



print( )
print( )
print( )

print("____________________________________________________________________________ Hello Welccome ______________________________________________________________________")

print( )
print( )
print( )
print( )

# بخش ورود و خروج
print("1. Continue ")
print("2. Exit ")
print( )

login = input("Choose : ")
print( )
if login=="1":
    # بخش انتخاب عملیات
    a = input("1. +  \n2. - \n3. * \n4. / \n\nChoose :  ")
    print( )
    # بخش عملیات جمع
    if a =="1":
        num_1 = int(input("Enter number one : "))
        print( )
        num_2 = int(input("Enter number two :  "))
        print( )
        aa = num_1 + num_2
        print(f"{num_1} + {num_2} = {aa} ")
        print(" ")
        print(" ")
        print(" ")


    a = input("1. +  \n2. - \n3. * \n4. / \n\nChoose :  ")
    print( )
    # بخش عملیات تفریق
    if a =="2":
        num_1 = int(input("Enter number one : "))
        print( )
        num_2 = int(input("Enter number two :  "))
        print( )
        aa = num_1 - num_2
        print(f"{num_1} - {num_2} = {aa} ")
        print(" ")
        print(" ")
        print(" ")

    a = input("1. +  \n2. - \n3. * \n4. / \n\nChoose :  ")
    print( )
    # بخش عملیات ضرب
    if a =="3":
        num_1 = int(input("Enter number one : "))
        print( )
        num_2 = int(input("Enter number two :  "))
        print( )
        aa = num_1 * num_2
        print(f"{num_1} * {num_2} = {aa} ")
        print(" ")
        print(" ")
        print(" ")

    a = input("1. +  \n2. - \n3. * \n4. / \n\nChoose :  ")
    print( )
    # بخش عملیات تقسیم
    if a =="4":
        num_1 = int(input("Enter number one : "))
        print( )
        num_2 = int(input("Enter number two :  "))
        print( )
        aa = num_1 / num_2
        print(f"{num_1} / {num_2} = {aa} ")
        print(" ")
        print(" ")
        print(" ")


