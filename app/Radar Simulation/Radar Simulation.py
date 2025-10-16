import turtle

def draw_radar_shape() :
    # آمادی سازی صفحه
    window = turtle.Screen()
    window.title("RADAR SIMULATION")
    window.bgcolor("black")
    window.setup(700, 700)

    # افزودن turtle
    radar_shape = turtle.Turtle()
    radar_shape.hideturtle()
    radar_shape.shape("turtle")
    radar_shape.color("green")
    radar_shape.speed(10)

    # رسم دایره رادار (حلقه بیرونی)
    radar_shape.penup()
    radar_shape.goto(0, -200)

    radar_shape.pendown()
    radar_shape.circle(200)

    # رسم دیره رادار(حلقه هاب داخلی)
    for r in range(150, 50, -50) :      # از 150 به 50 کم میشود
        radar_shape.penup()
        radar_shape.goto(0, -r)      # مرکز دایره
        radar_shape.pendown()
        radar_shape.circle(r)       # رسم دایره با شعاع r


    # رسم خطوط داخلی رادار
    for radar_shape_angle in range(0, 360, 30) :
        radar_shape.penup()
        radar_shape.goto(0, 0)      
        radar_shape.setheading(radar_shape_angle)
        radar_shape.pendown()
        radar_shape.forward(200)

    # متن صفحه رادار
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.color("gold")
    text.goto(0, 300)
    text.write("RADAR SIMULATION", align="center", font=("Courier", 21, "bold" ))


    window.exitonclick()

def mine_meno() :
    while True :
        print("--- radar meno ---     \n\n")
        print(" 1. Start scaning \n 2. Exit \n")
        mine_meno__choice = input("your choice :  ")
        
        # شرط استارت اسکن 
        if mine_meno__choice == "1" :
            draw_radar_shape()
            scan_area()

        # شرط خروج
        elif mine_meno__choice == "2" :
            print("Exiting 👋  \n")
            break
        
        else :
            print("Warning ⚠  \n")


def scan_area() :
    print("--- scan start  📻 --- ")
    
    # درجه
    angle = 0
    while angle <= 180 :
        print(f"Angle : {angle} degrees  \n")

        # پرسش فاصله جسم
        distance = int(input("space : "))

        
        # شرط موانع مسیر
        if distance <10 :
            print(" Warning ⚠ \n Obstacle is too cloes ⛔  \n")
        
        else :
            print("Path is clear. ✅   \n")

        # چرخش رادار به درجه بعدی
        angle += 30








mine_meno()