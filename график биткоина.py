import requests as req
import turtle as t
import time

r=t.Turtle()
r2=t.Turtle()
w=t.Screen()
t.pensize(2)
t.speed(0)
t.hideturtle()
r2.hideturtle()
r2.speed(0)
r.hideturtle()
r.speed(0)
w.screensize(4100,4000)
t.bgcolor("#454545")
r2.pencolor("#2d2d2d")
yr2=-1950
for i in range(80):
    r2.up()
    r2.goto(-2050,yr2)
    r2.down()
    r2.goto(2050,yr2)
    yr2+=50


# r.up()
# r.goto(-700,200)
# r.down()
#                         2 долора =10 пикселей   10 долорав =50 пикселей!!!!!!!!!!!
mashtab=5

url= 'https://api.binance.com/api/v3/ticker/price'

a=req.get(url,params={'symbol':'BTCUSDT'})

price_object=a.json()

price = float(price_object['price'])

print(price)
first_price=price
first_price2=first_price
t.up()
t.goto(-2000,price*mashtab-first_price*mashtab)
t.down()
t.write(price,font=('Arial',10, 'normal'))
t.up()
t.goto(-1940,price*mashtab-first_price*mashtab)
t.down()
t.pencolor("#257acf")
t.dot(10)


first_y=0+(((price-int(price))*800)-400)

s=-1940

while True:

    a=req.get(url,params={'symbol':'BTCUSDT'})

    price_object=a.json()

    price = float(price_object['price'])

    print(price)

    # if int(price)>int(first_price):
    #     t.goto(s,0+(((price-int(price))*800*10)-400))
    #     continue


    # if price-int(price)==0:
    #     aswd=0+(((price-int(price))*800)-400)-first_price-int(first_price)
    #     t.goto(s,aswd)#first_price-int(first_price)
    #     continue

    # elif first_price-int(first_price)<10:
    #     price*=10


    if price>first_price2:
        t.pencolor('green')
        t.goto(s,price*mashtab-first_price*mashtab)
        r.up()
        r.goto(s,price*mashtab-first_price*mashtab)
        r.down()
        r.clear()
        r.write(f"{price:.2f}", align="center", font=("Arial", 10, "normal"))


        # r.pencolor("#454545")
        # r.dot(150)
        # r.pencolor('#000000')
        # r.write(price,font=('Arial',10, 'normal'))


    elif price<first_price2:
        t.pencolor('red')
        t.goto(s,price*mashtab-first_price*mashtab)
        r.up()
        r.goto(s,price*mashtab-first_price*mashtab)
        r.down()
        r.clear()
        r.write(f"{price:.2f}", align="center", font=("Arial", 10, "normal"))
        # r.pencolor("#454545")
        # r.dot(150)
        # r.pencolor('#000000')
        # r.write(price,font=('Arial',10, 'normal'))


    else:
        t.pencolor('#000000')
        t.goto(s,price*mashtab-first_price*mashtab)
        r.up()
        r.goto(s,price*mashtab-first_price*mashtab)
        r.down()
        r.clear()
        r.write(f"{price:.2f}", align="center", font=("Arial", 10, "normal"))
        # r.pencolor("#454545")
        # r.dot(150)
        # r.pencolor('#000000')

        # r.write(price,font=('Arial',10, 'normal'))
    first_price2=price


    


    s+=5
    # if price<10:
    #     first_price=price*10
    # else:
    #     first_price=price

w.mainloop()

