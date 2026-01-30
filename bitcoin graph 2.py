#------------------------------------------------ <import modules>

import requests as req
import turtle as t
import time

#------------------------------------------------ <set screen settings>

w=t.Screen()
w.setup(width = 1200,height = 700)
w._root.resizable(False,False)
w._root.title('график биткоина')

#------------------------------------------------ <set turtels>

r2=t.Turtle()
graph = t.Turtle()
line = t.Turtle()
grid = t.Turtle()
bg = t.Turtle()
write_prices = t.Turtle()
price_1 = t.Turtle()
price_2 = t.Turtle()
bitcoin = t.Turtle()
tim = t.Turtle()
tim2 = t.Turtle()
tim3 = t.Turtle()

#------------------------------------------------ <set turtle settings>

t.hideturtle()
r2.hideturtle()
graph.hideturtle()
line.hideturtle()
grid.hideturtle()
bg.hideturtle()
write_prices.hideturtle()
price_1.hideturtle()
price_2.hideturtle()
tim.hideturtle()
tim2.hideturtle()
tim3.hideturtle()
bitcoin.hideturtle()

t.speed(0)
r2.speed(0)
graph.speed(0)
line.speed(0)
grid.speed(0)
bg.speed(0)
write_prices.speed(0)
price_1.speed(0)
price_2.speed(0)
tim.speed(0)
tim2.speed(0)
tim3.speed(0)
bitcoin.speed(0)

#------------------------------------------------ <preparing the program>

t.pensize(2)

write_prices.up()
write_prices.goto(-585,308)
write_prices.down()

tim3.up()

#------------------------------------------------ <drew the background>
print('================================================')
t.bgcolor("#454545")
bg.pencolor("#393939")
bg.dot(1200)
bg.pencolor("#2E2E2E")
bg.dot(1000)
bg.pencolor("#272727")
bg.dot(800)
bg.pencolor("#202020")
bg.dot(600)
bg.pencolor("#1D1D1D")
bg.dot(400)

#------------------------------------------------ <constants>

pixels_for_dollar = 0.2
STEP = 20
Interval = 60
offset = -20

#------------------------------------------------ <variables>

first_price = 0
x = -580
elements_for_block = []
all_prices = []

#------------------------------------------------ <function scale>

def scale(price):
    return (price-BASE_PRICE) * pixels_for_dollar
    
#------------------------------------------------ <draw interface>

try:
    url= 'https://api.binance.com/api/v3/ticker/price'
    response = req.get(url,params={'symbol':'BTCUSDT'},timeout=5)
    BASE_PRICE = float(response.json()['price'])
except req.exceptions.ConnectionError:
    print('ошибка соединения')
    

grid.up()
grid.goto(-590,340)
grid.down()
grid.pensize(3)
grid.pencolor("#ff9531")
grid.fillcolor("#feab5c")
grid.begin_fill()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5 + 13,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5 + 13,310)
grid.goto(-590,310)
grid.goto(-590,340)
grid.end_fill()
grid.pencolor('#000000')
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+10 + 13,300)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+10 + 13,350)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+20 + 13,310)
grid.down()
grid.pensize(3)
grid.pencolor("#ff9531")
grid.fillcolor("#feab5c")
grid.begin_fill()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5 + 20 + 70 + 13,310)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5 + 20 + 70 + 13,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+20 + 13,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+20 + 13,310)
grid.end_fill()
tim.up()
tim.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+25 + 13,325)
tim.write(time.strftime("%d.%m.%Y", time.localtime()),font = ("Times New Roman" , 10))
tim.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+25 + 13,310)
tim.write(time.strftime("%H:%M", time.localtime()),font = ("Times New Roman" , 10))
tim.down()
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 13,310)
grid.down()
grid.begin_fill()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 70 + 13,310)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 70 + 13,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 13,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 13,310)
grid.end_fill()

tim.up()
tim.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+25 + 72 + 13,313)
tim.write('-',font = ("Times New Roman" , 20))
tim.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+25 + 90 + 13,325)
tim.write(time.strftime("%d.%m.%Y", time.localtime()),font = ("Times New Roman" , 10))

grid.up()
grid.pencolor('#000000')
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 80 + 13,300)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 80 + 13,350)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 90 + 13,310)
grid.pencolor("#ff9531")
grid.down()
grid.begin_fill()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 155 + 13,310)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 155 + 13,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 90 + 13,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 90 + 13,310)
grid.end_fill()

tim2.up()
tim2.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 92 + 13,308)
tim2.write(time.strftime("%H:%M", time.localtime()),font = ("Times New Roman" , 20))

grid.up()
grid.pencolor('#000000')
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 13,300)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 13,350)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 10 + 13,310)
grid.down()
grid.pencolor("#ff9531")
grid.begin_fill()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 13 * 2,310)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 13 * 2,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 10 + 13,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 10 + 13,310)
grid.end_fill()

price_1.up()
price_1.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 170 + 15 + 9*15.5 + 13,308)

grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 170 + 10 + 13,309)
grid.pencolor('#000000')
grid.write('MAX PRICE:',font = ("Times New Roman" , 19))
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + 13 * 2,300)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + 13 * 2,350)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 25 + 13 * 2,310)
grid.down()
grid.pencolor("#ff9531")
grid.begin_fill()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 13 * 3,310)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 13 * 3,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 25 + 13 * 2,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 25 + 13 * 2,310)
grid.end_fill()

price_1.up()
price_1.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 170 + 15 + 9*15.5 + 13,308)

price_2.up()
price_2.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 170 + 20 + 9*15.5 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + 13 * 2,308)

grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 170 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 25 + 13 * 2,309)
grid.pencolor('#000000')
grid.write('MIN PRICE:',font = ("Times New Roman" , 19))
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 13 * 3,300)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 13 * 3,350)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 5 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 30 + 13 * 3,310)
grid.down()
grid.pencolor("#ff9531")
grid.begin_fill()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 15 + 13 * 3,310)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 15 + 13 * 3,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 10 + 13 * 3,340)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 10 + 13 * 3,310)
grid.end_fill()

bitcoin.up()
bitcoin.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 30 + 13 * 3,308)
bitcoin.write('BITCOIN',font = ("Times New Roman" , 20))

grid.pencolor('#000000')
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 25 + 13 * 3,300)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 25 + 13 * 3,350)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 13 * 3,308)
grid.down()
grid.pencolor("#ff9531")
grid.begin_fill()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 117,308)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 117,343)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 13 * 3,343)
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 13 * 3,308)
grid.end_fill()
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 13 * 3,308)
grid.down()
grid.pencolor("#ff9531")
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 117,343)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 13 * 3,343)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 117,308)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 13 * 3,325.5)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 117,325.5)
grid.up()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 58.5 +(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 117 -(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 13 * 3))/4,343)
grid.down()
grid.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 58.5 +(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 117 -(-590+len(str(round(BASE_PRICE,1)))*15.5+ 20 + 90 + 165 + 15 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 10 + len(str(round(BASE_PRICE,1)))*15.5 + 9*15.5 + 15 + 7*15.5 + 32 + 13 * 3))/4,308)


MASTAB = 350/BASE_PRICE
price = BASE_PRICE / pixels_for_dollar * MASTAB -100
line.pencolor("#a6a6a6")
y1 = int(-8000*pixels_for_dollar)
y2 = int(7500*pixels_for_dollar)
y3 = int(500*pixels_for_dollar)
for i in range(y1,y2,y3):
        p2 = BASE_PRICE + i
        y =scale(p2)
        line.penup()
        line.goto(-600, y)
        line.pendown()
        line.goto(515, y)
        line.penup()
        line.goto(525, y - 7)
        line.pendown()
        line.write(f"{p2:.2f}$", font=("Arial", 10, "normal"))

line.up()
line.goto(-600,300)
line.down()
line.pencolor('#000000')
line.pensize(4)
line.goto(600,300)
line.up()
line.goto(500,300)
line.down()
line.goto(500,-350)

#------------------------------------------------ <function get_price>

def get_price()->float:
    try:
        url= 'https://api.binance.com/api/v3/ticker/price'
        response = req.get(url,params={'symbol':'BTCUSDT'},timeout=10)
        return float(response.json()['price'])
    except (req.exceptions.ConnectionError,req.ReadTimeout):
        print('ошибка соединения')
        return -1

#------------------------------------------------ <function draw_block>

def draw_block(prices, offset):
    last_price = prices[-1]
    max_price = max(prices)
    min_price = min(prices)
    first_price = prices[0]
    y_open = scale(first_price)
    y_close = scale(last_price)
    y_high = scale(max_price)
    y_low = scale(min_price)

    print('================================================')

    color = 'green' if last_price > first_price else 'red'
    graph.fillcolor(color)
    graph.pencolor(color)

    graph.up()
    graph.goto(x + 15 + offset, y_low)
    graph.down()
    graph.goto(x + 15 + offset, y_high)

    graph.up()
    graph.goto(x + 5 + offset, y_open)
    graph.down()
    graph.pencolor('black')
    graph.begin_fill()
    graph.goto(x + 25 + offset, y_open)
    graph.goto(x + 25 + offset, y_close)
    graph.goto(x + 5 + offset, y_close)
    graph.goto(x + 5 + offset, y_open)
    graph.end_fill()

#------------------------------------------------ <function update_time>

def update_time():
    tim2.clear()
    current_time = time.strftime("%H:%M", time.localtime())
    tim2.up()
    tim2.goto(-590 + len(str(round(BASE_PRICE, 1))) * 15.5 + 20 + 90 + 92 + 13, 308)
    tim2.write(current_time, font=("Times New Roman", 20))
    tim3.clear()
    tim2.up()
    tim3.goto(-590+len(str(round(BASE_PRICE,1)))*15.5+25 + 90 + 13,310)
    tim3.write(time.strftime("%H:%M", time.localtime()),font = ("Times New Roman" , 10))
    grid.up()
    w.ontimer(update_time, 60000)

#------------------------------------------------ <function end>

def end():
    if graph.xcor()>450:
        print('END')
        return -2

#------------------------------------------------ <function update_graph>

def update_graph():
    isand_end = end()
    if isand_end == -2:
        return
    global offset
    first_price = get_price()
    if first_price == -1:
        w.ontimer(update_graph, Interval * 1000)
        return
    prices = []
    #-------------------- <function collect_prices>
    def collect_prices():
        nonlocal prices
        global offset
        price = get_price()
        if price != -1:
            prices.append(price)
            all_prices.append(price)
            print(price)
            write_prices.clear()
            write_prices.write(f'{price:.1f}$',font = ("Times New Roman" , 20))
            price_1.clear()
            price_1.write(f'{max(all_prices):.1f}$',font = ("Times New Roman" , 20))
            price_2.clear()
            price_2.write(f'{min(all_prices):.1f}$',font = ("Times New Roman" , 20))
        if len(prices) < Interval:
              w.ontimer(collect_prices, 1000)
        else:
            draw_block(prices, offset)
            offset += STEP
            w.update()
            w.ontimer(update_graph, 1000)
    collect_prices()

#------------------------------------------------ <start program>

update_time()
update_graph()

w.mainloop()





