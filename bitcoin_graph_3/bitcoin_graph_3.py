#==================== <import modules> / <импорт модулей> \/\/\/
import turtle as t
import time
import requests as req
import tkinter as tk

#==================== <set screen settings> / <насторйки экрана> \/\/\/
win = t.Screen()
win.setup(width = 1320,height = 910)
win._root.resizable(False,False)
win._root.title('ГРАФИК БИТКОИНА')

img = tk.PhotoImage(file='bitcoin_graph_3_icon.png')
win._root.iconphoto(False, img)


#==================== <set turtels> / <создание черепах> \/\/\/
interface_lines = t.Turtle()
interface_palets = t.Turtle()
back_to_live_palet = t.Turtle()
price_lines = t.Turtle()
price_line_text = t.Turtle()
static_text = t.Turtle()
time_text = t.Turtle()
write_price = t.Turtle()
price_percent = t.Turtle()
upper_graph = t.Turtle()
lower_graph = t.Turtle()
max_price_text_line = t.Turtle()
min_price_text_line = t.Turtle()
startscreen = t.Turtle()
startscreen_2 = t.Turtle()

#==================== <set turtle settings> / <установк параметров черепах> \/\/\/
interface_lines.pensize(4)
interface_palets.pensize(4)
upper_graph.pensize(4)
lower_graph.pensize(2)
back_to_live_palet.pensize(2)


t.hideturtle()
interface_lines.hideturtle()
interface_palets.hideturtle()
back_to_live_palet.hideturtle()
price_lines.hideturtle()
price_line_text.hideturtle()
static_text.hideturtle()
time_text.hideturtle()
write_price.hideturtle()
price_percent.hideturtle()
upper_graph.hideturtle()
lower_graph.hideturtle()
max_price_text_line.hideturtle()
min_price_text_line.hideturtle()
startscreen.hideturtle()
startscreen_2.hideturtle()


static_text.up()
time_text.up()
write_price.up()
price_percent.up()
price_lines.up()
price_line_text.up()
max_price_text_line.up()
min_price_text_line.up()

startscreen_2.speed(0)


t.bgcolor("#3F3F3F")
price_lines.pencolor("#858585")
price_line_text.pencolor("#858585")


#==================== <variables> / <переменные> \/\/\/
dollars_for_pixel = 0.05

upper_graph_x = -620
lower_graph_x = -650

isend_upper_graph = None
is_real_time_graph = True
navigating = False

start_page_time = None
current_time = None

price_matrix_index = 0
price_matrix = []
price_list = []
blocks_edges = []
times_list = []

BASE_PRICE = None

theme = None

#==================== <version> / <версия> \/\/\/

VERSION = "version 1.0.1"

#==================== <start screen> / <стартовый экран> \/\/\/
def start_screen():
    startscreen.shape("turtle")
    startscreen.shapesize(15)

    startscreen.pencolor("#383838")
    startscreen.dot(10000)
    startscreen.pencolor("#303030")
    startscreen.dot(1500)
    startscreen.pencolor("#2B2B2B")
    startscreen.dot(1200)
    startscreen.pencolor("#272727")
    startscreen.dot(750)
    startscreen.pencolor("#242424")
    startscreen.dot(300)


    startscreen.up()
    startscreen.goto(-590, 250)
    startscreen.speed(0)

    startscreen.pencolor("#000000")
    startscreen.write("B", font = ("Times New Roman" , 100))
    startscreen.forward(90)
    startscreen.write("I", font = ("Times New Roman" , 100))
    startscreen.forward(50)
    startscreen.write("T", font = ("Times New Roman" , 100))
    startscreen.forward(80)
    startscreen.write("C", font = ("Times New Roman" , 100))
    startscreen.forward(90)
    startscreen.write("O", font = ("Times New Roman" , 100))
    startscreen.forward(90)
    startscreen.write("I", font = ("Times New Roman" , 100))
    startscreen.forward(60)
    startscreen.write("N", font = ("Times New Roman" , 100))
    startscreen.forward(140)
    startscreen.write("G", font = ("Times New Roman" , 100))
    startscreen.forward(100)
    startscreen.write("R", font = ("Times New Roman" , 100))
    startscreen.forward(100)
    startscreen.write("A", font = ("Times New Roman" , 100))
    startscreen.forward(100)
    startscreen.write("P", font = ("Times New Roman" , 100))
    startscreen.forward(80)
    startscreen.write("H", font = ("Times New Roman" , 100))
    startscreen.forward(140)
    startscreen.write("3", font = ("Times New Roman" , 100))

    startscreen.speed(5)

    startscreen.up()
    startscreen.goto(-630, 100)
    startscreen.speed(0)

    startscreen.pencolor("#000000")
    startscreen.write("P", font = ("Times New Roman" , 85))
    startscreen.forward(70)
    startscreen.write("O", font = ("Times New Roman" , 85))
    startscreen.forward(80)
    startscreen.write("W", font = ("Times New Roman" , 85))
    startscreen.forward(110)
    startscreen.write("E", font = ("Times New Roman" , 85))
    startscreen.forward(70)
    startscreen.write("R", font = ("Times New Roman" , 85))
    startscreen.forward(80)
    startscreen.write("E", font = ("Times New Roman" , 85))
    startscreen.forward(70)
    startscreen.write("D", font = ("Times New Roman" , 85))
    startscreen.forward(120)
    startscreen.write("B", font = ("Times New Roman" , 85))
    startscreen.forward(80)
    startscreen.write("Y", font = ("Times New Roman" , 85))
    startscreen.forward(120)
    startscreen.write("T", font = ("Times New Roman" , 85))
    startscreen.forward(80)
    startscreen.write("U", font = ("Times New Roman" , 85))
    startscreen.forward(90)
    startscreen.write("R", font = ("Times New Roman" , 85))
    startscreen.forward(70)
    startscreen.write("T", font = ("Times New Roman" , 85))
    startscreen.forward(70)
    startscreen.write("L", font = ("Times New Roman" , 85))
    startscreen.forward(70)
    startscreen.write("E", font = ("Times New Roman" , 85))


    time.sleep(1)


    win.tracer(0)
    startscreen.pencolor("#000000")
    startscreen.up()
    startscreen.goto(-650, -445)
    startscreen.write(VERSION, font = ("Times New Roman" , 25))

    startscreen.goto(0,-200)
    startscreen.left(90)
    startscreen.showturtle()
    win.tracer(1)

    time.sleep(2)

    win.tracer(0)

    startscreen.up()
    startscreen.goto(0,0)
    startscreen.down()
    startscreen.pencolor("#383838")
    startscreen.dot(10000)
    startscreen.pencolor("#303030")
    startscreen.dot(1500)
    startscreen.pencolor("#2B2B2B")
    startscreen.dot(1200)
    startscreen.pencolor("#272727")
    startscreen.dot(750)
    startscreen.pencolor("#242424")
    startscreen.dot(300)
    startscreen.hideturtle()

    startscreen.up()
    startscreen.pencolor("#000000")
    startscreen.goto(-650, -445)
    startscreen.write(VERSION, font = ("Times New Roman" , 25))

    startscreen.goto(-630, 320)
    startscreen.write("Select theme:", font = ("Times New Roman" , 80))

    startscreen.pencolor("#0d3b31")
    startscreen.fillcolor("#145f4f")
    startscreen.pensize(6)
    startscreen.goto(-500, 200)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-400, 200)
    startscreen.goto(-400, 100)
    startscreen.goto(-500, 100)
    startscreen.goto(-500, 200)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4)
    startscreen.up()
    startscreen.goto(-475, 75)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-425, 75)
    startscreen.goto(-425, 25)
    startscreen.goto(-475, 25)
    startscreen.goto(-475, 75)
    startscreen.end_fill()

    startscreen.pencolor("#c97c35")
    startscreen.fillcolor("#e4974f")
    startscreen.pensize(6)
    startscreen.up()
    startscreen.goto(-200, 200)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-100, 200)
    startscreen.goto(-100, 100)
    startscreen.goto(-200, 100)
    startscreen.goto(-200, 200)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4)
    startscreen.up()
    startscreen.goto(-175, 75)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-125, 75)
    startscreen.goto(-125, 25)
    startscreen.goto(-175, 25)
    startscreen.goto(-175, 75)
    startscreen.end_fill()

    startscreen.pencolor("#13335e")
    startscreen.fillcolor("#1e416e")
    startscreen.pensize(6)
    startscreen.up()
    startscreen.goto(200, 200)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(100, 200)
    startscreen.goto(100, 100)
    startscreen.goto(200, 100)
    startscreen.goto(200, 200)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4)
    startscreen.up()
    startscreen.goto(175, 75)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(125, 75)
    startscreen.goto(125, 25)
    startscreen.goto(175, 25)
    startscreen.goto(175, 75)
    startscreen.end_fill()


    startscreen.pencolor("#af2929")
    startscreen.fillcolor("#c53a3a")
    startscreen.pensize(6)
    startscreen.up()
    startscreen.goto(500, 200)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(400, 200)
    startscreen.goto(400, 100)
    startscreen.goto(500, 100)
    startscreen.goto(500, 200)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4)
    startscreen.up()
    startscreen.goto(475, 75)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(425, 75)
    startscreen.goto(425, 25)
    startscreen.goto(475, 25)
    startscreen.goto(475, 75)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4)
    startscreen.up()
    startscreen.goto(-170, -150)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(170, -150)
    startscreen.goto(170, -250)
    startscreen.goto(-170, -250)
    startscreen.goto(-170, -150)
    startscreen.end_fill()

    startscreen.pencolor("#000000")
    startscreen.up()
    startscreen.goto(-160, -260)
    startscreen.write("START", font = ("Times New Roman" , 75))

    win.tracer(1)


    startscreen_2.pencolor("#3d3d3d")
    
    def click(x, y):
        global theme, color_1, color_2, pale_color_1, pale_color_2, bright_color_1, bright_color_2
        if x < -400 and x > -500 and y > 100 and y < 200:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(-450, 50)
            startscreen_2.down()
            theme = "green"
            startscreen_2.dot(25)
        elif x < -100 and x > -200 and y > 100 and y < 200:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(-150, 50)
            startscreen_2.down()
            theme = "orange"
            startscreen_2.dot(25)
        elif x < 200 and x > 100 and y > 100 and y < 200:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(150, 50)
            startscreen_2.down()
            theme = "blue"
            startscreen_2.dot(25)
        elif x < 500 and x > 400 and y > 100 and y < 200:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(450, 50)
            startscreen_2.down()
            theme = "red"
            startscreen_2.dot(25)
        elif x < 170 and x > -170 and y > -250 and y < -150:
            if theme == "green":
                color_1 = "#0d3b31"
                color_2 = "#145f4f"
                pale_color_1 = "#374744"
                pale_color_2 = "#4b5c59"
                bright_color_1 = "#125042"
                bright_color_2 = "#1b866f"      
            elif theme == "orange":
                color_1 = "#c97c35"
                color_2 = "#e4974f"
                pale_color_1 = "#917459"
                pale_color_2 = "#B8906B"
                bright_color_1 = "#df8c3f"
                bright_color_2 = "#ebac71"
            elif theme == "blue":
                color_1 = "#13335e"
                color_2 = "#1e416e"
                pale_color_1 = "#40608a"
                pale_color_2 = "#50709b"
                bright_color_1 = "#204474"
                bright_color_2 = "#407ac7"
            elif theme == "red":
                color_1 = "#af2929"
                color_2 = "#c53a3a"
                pale_color_1 = "#964b4b"
                pale_color_2 = "#a55555"
                bright_color_1 = "#b93737"
                bright_color_2 = "#d65252"
            if theme:
                startscreen.clear()
                startscreen_2.clear()
                start()   


    win.onclick(click, 1)

start_screen()



def start():
    global BASE_PRICE, upper_graph_x, lower_graph_x, max_price, min_price, dollars_for_pixel, isend_upper_graph, is_real_time_graph, navigating, start_page_time, current_time, price_matrix_index, price_matrix, price_list, blocks_edges, times_list
    #==================== <determining the starting price> / <оперделение старовой цены> \/\/\/
    while not BASE_PRICE:
        try:
            url= 'https://api.binance.com/api/v3/ticker/price'
            response = req.get(url,params={'symbol':'BTCUSDT'}, timeout=5)
            BASE_PRICE = float(response.json()['price'])
        except req.exceptions.ConnectionError:
            print('ошибка соединения')
            BASE_PRICE = None


    #==================== <preparing the program> / <подготовка программы> \/\/\/
    max_price = BASE_PRICE
    min_price = BASE_PRICE



    win.tracer(0)

    upper_graph.up()
    upper_graph.goto(-620, 180)
    upper_graph.down()

    t.up()
    t.goto(0,0)
    t.down()
    t.pencolor("#383838")
    t.dot(10000)
    t.pencolor("#303030")
    t.dot(1500)
    t.pencolor("#2B2B2B")
    t.dot(1200)
    t.pencolor("#272727")
    t.dot(750)
    t.pencolor("#242424")
    t.dot(300)


    price_len = len(str(int(BASE_PRICE)))*15.5 + 80
    end_palet_1 = -650 + len(str(int(BASE_PRICE)))*15.5 + 90
    #==================== <draw interface> / <отрисовка интерфейса> \/\/\/
    #========== <first palet> / <первая табличка> \/\/\/
    #===== <price/period of time> / <цена/период времени> \/\/\/
    interface_palets.pencolor(color_1)
    interface_palets.fillcolor(color_2)
    interface_palets.up()
    interface_palets.goto(-650, 400)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(-650, 440)
    interface_palets.goto(end_palet_1, 440)
    interface_palets.goto(end_palet_1, 400)
    interface_palets.goto(-650, 400)
    interface_palets.end_fill()

    write_price.goto(-645, 402)

    interface_lines.up()
    interface_lines.goto(10 + end_palet_1, 455)
    interface_lines.down()
    interface_lines.goto(10 + end_palet_1, 390)


    #========== <second and third palets> / <вторая и третья таблички> \/\/\/
    #===== <start time - last time> / <стартовое время - последнее время> \/\/\/
    #=== <second palet> / <вторая табличка> \/\/\/
    interface_palets.up()
    interface_palets.goto(20 + end_palet_1, 400)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(20 + end_palet_1, 440)
    interface_palets.goto(110 + end_palet_1, 440)
    interface_palets.goto(110 + end_palet_1, 400)
    interface_palets.goto(20 + end_palet_1, 400)
    interface_palets.end_fill()

    static_text.goto(25 + end_palet_1, 402)
    static_text.write(time.strftime("%H:%M", time.localtime()) ,font = ("Times New Roman" , 25))

    end_palet_2 = 110 + end_palet_1

    interface_lines.up()
    interface_lines.goto(10 + end_palet_2, 420)
    interface_lines.down()
    interface_lines.forward(10)

    #=== <third palet> / <третья табличка> \/\/\/
    interface_palets.up()
    interface_palets.goto(end_palet_2 + 30, 400)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(end_palet_2 + 30, 440)
    interface_palets.goto(end_palet_2 + 120, 440)
    interface_palets.goto(end_palet_2 + 120, 400)
    interface_palets.goto(end_palet_2 + 30, 400)
    interface_palets.end_fill()

    current_time = time.strftime("%H:%M", time.localtime())
    time_text.goto(35 + end_palet_2, 402)
    time_text.write(current_time ,font = ("Times New Roman" , 25))

    end_palet_3 = 120 + end_palet_2

    interface_lines.up()
    interface_lines.goto(10 + end_palet_3, 455)
    interface_lines.down()
    interface_lines.goto(10 + end_palet_3, 390)


    #========== <fourth palet> / <четвёртая табличка> \/\/\/
    #===== <max price> / <максимальноя цена> \/\/\/
    interface_palets.up()
    interface_palets.goto(20 + end_palet_3, 400)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(15 + 16*9 + end_palet_3 + price_len, 400)
    interface_palets.goto(15 + 16*9 + end_palet_3 + price_len, 440)
    interface_palets.goto(20 + end_palet_3, 440)
    interface_palets.goto(20 + end_palet_3, 400)
    interface_palets.end_fill()

    static_text.goto(25 + end_palet_3, 405)
    static_text.write('MAX PRICE:',font = ("Times New Roman" , 19))

    max_price_text_line.goto(170 + end_palet_3, 403)
    max_price_text_line.write(f"{BASE_PRICE}$", font = ("Times New Roman" , 20))

    end_palet_4 = 15 + 16*9 + end_palet_3 + price_len

    interface_lines.up()
    interface_lines.goto(10 + end_palet_4, 455)
    interface_lines.down()
    interface_lines.goto(10 + end_palet_4, 390)


    #========== <fifth palet> / <пятая табличка> \/\/\/
    #===== <min price> / <минимальноя цена> \/\/\/
    interface_palets.up()
    interface_palets.goto(20 + end_palet_4, 400)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(8 + 16*9 + end_palet_4 + price_len, 400)
    interface_palets.goto(8 + 16*9 + end_palet_4 + price_len, 440)
    interface_palets.goto(20 + end_palet_4, 440)
    interface_palets.goto(20 + end_palet_4, 400)
    interface_palets.end_fill()

    static_text.goto(25 + end_palet_4, 405)
    static_text.write('MIN PRICE:',font = ("Times New Roman" , 19))

    min_price_text_line.goto(160 + end_palet_4, 403)
    min_price_text_line.write(f"{BASE_PRICE}$", font = ("Times New Roman" , 20))

    end_palet_5 = 8 + 16*9 + end_palet_4 + price_len

    interface_lines.up()
    interface_lines.goto(10 + end_palet_5, 455)
    interface_lines.down()
    interface_lines.goto(10 + end_palet_5, 390)


    #========== <sixth palet> / <шестая табличка> \/\/\/
    #===== <percent from start program> / <процент с начала программы> \/\/\/
    interface_palets.up()
    interface_palets.goto(20 + end_palet_5, 400)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(265 + end_palet_5, 400)
    interface_palets.goto(265 + end_palet_5, 440)
    interface_palets.goto(20 + end_palet_5, 440)
    interface_palets.goto(20 + end_palet_5, 400)
    interface_palets.end_fill()

    static_text.goto(25 + end_palet_5, 405)
    static_text.write('FROM START',font = ("Times New Roman" , 18))

    price_percent.goto(175 + end_palet_5, 405)
    price_percent.write('+0.000%',font = ("Times New Roman" , 17))

    end_palet_6 = 265 + end_palet_5

    interface_lines.up()
    interface_lines.goto(10 + end_palet_6, 455)
    interface_lines.down()
    interface_lines.goto(10 + end_palet_6, 390)


    #========== <price lines> / <линии цены> \/\/\/

    MASHTAB_1 = 180 / BASE_PRICE
    MASHTAB_2 = -240 / BASE_PRICE

    #===== <lines for upper graph> / <линии для верхнего графика> \/\/\/
    #=== <from the center of the upper graph down> / <от центра верхнего графика вниз> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660, BASE_PRICE*MASHTAB_1 - i*20)
        price_lines.down()
        price_lines.goto(575, BASE_PRICE*MASHTAB_1 - i*20)
        price_line_text.goto(580, BASE_PRICE*MASHTAB_1 - i*20 - 8)
        price_line_text.write(f"{BASE_PRICE - (i*20)*dollars_for_pixel}$", font = ("Arial" , 10, 'normal'))

    #=== <from the center of the upper graph up> / <от центра верхнего графика вверх> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660, BASE_PRICE*MASHTAB_1 + i*20)
        price_lines.down()
        price_lines.goto(575, BASE_PRICE*MASHTAB_1 + i*20)
        price_line_text.goto(580, BASE_PRICE*MASHTAB_1 + i*20 - 8)
        price_line_text.write(f"{BASE_PRICE + (i*20)*dollars_for_pixel}$", font = ("Arial" , 10, 'normal'))


    #===== <lines for lower graph> / <линии для нижнего графика> \/\/\/
    #=== <from the center of the lower graph down> / <от центра нижнего графика вниз> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660, BASE_PRICE*MASHTAB_2 - i*20)
        price_lines.down()
        price_lines.goto(575, BASE_PRICE*MASHTAB_2 - i*20)
        price_line_text.goto(580, BASE_PRICE*MASHTAB_2 - i*20 - 8)
        price_line_text.write(f"{BASE_PRICE - (i*20)*dollars_for_pixel}$", font = ("Arial" , 10, 'normal'))

    #=== <from the center of the lower graph up> / <от центра нижнего графика вверх> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660, BASE_PRICE*MASHTAB_2 + i*20)
        price_lines.down()
        price_lines.goto(575, BASE_PRICE*MASHTAB_2 + i*20)
        price_line_text.goto(580, BASE_PRICE*MASHTAB_2 + i*20 - 8)
        price_line_text.write(f"{BASE_PRICE + (i*20)*dollars_for_pixel}$", font = ("Arial" , 10, 'normal'))


    #========== <arrow keys to move between history pages> / <стреслки для перемещения между страницами истории> \/\/\/
    #===== <left arrow button> / <кнопка стрелка влево> \/\/\/
    #=== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
    interface_palets.pencolor("#353535")
    interface_palets.fillcolor("#3A3A3A")

    interface_palets.up()
    interface_palets.goto(-660, 210)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(-660, 150)
    interface_palets.goto(-630, 150)
    interface_palets.goto(-630, 210)
    interface_palets.goto(-660, 210)
    interface_palets.end_fill()


    #=== <arrow> / <стрелка> \/\/\/
    interface_palets.pencolor(pale_color_1)
    interface_palets.fillcolor(pale_color_2)

    interface_palets.up()
    interface_palets.goto(-655, 180)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(-635, 200)
    interface_palets.goto(-635, 160)
    interface_palets.goto(-655, 180)
    interface_palets.end_fill()



    #===== <right arrow button> / <кнопка стрелка вправо> \/\/\/
    #=== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
    interface_palets.pencolor("#353535")
    interface_palets.fillcolor("#3A3A3A")

    interface_palets.up()
    interface_palets.goto(560, 210)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(560, 150)
    interface_palets.goto(530, 150)
    interface_palets.goto(530, 210)
    interface_palets.goto(560, 210)
    interface_palets.end_fill()


    #=== <arrow> / <стрелка> \/\/\/
    interface_palets.pencolor(pale_color_1)
    interface_palets.fillcolor(pale_color_2)

    interface_palets.up()
    interface_palets.goto(555, 180)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(535, 200)
    interface_palets.goto(535, 160)
    interface_palets.goto(555, 180)
    interface_palets.end_fill()



    #========== <interface_lines> / <линии интерфейса> \/\/\/
    interface_lines.up()
    interface_lines.goto(560, 390)
    interface_lines.down()
    interface_lines.goto(560,-450)

    interface_lines.up()
    interface_lines.goto(-660, 390)
    interface_lines.down()
    interface_lines.goto(660, 390)

    interface_lines.up()
    interface_lines.goto(-660, -30)
    interface_lines.down()
    interface_lines.goto(660, -30)


    #========== <version display> / <отображение версии> \/\/\/
    interface_lines.up()
    interface_lines.pencolor("#000000")
    interface_lines.goto(-650, -445)
    interface_lines.write(VERSION, font = ("Times New Roman" , 25))


    #==================== <screen update> / <обновление экрана> \/\/\/
    win.tracer(1)


    #==================== <functions> / <функции> \/\/\/
    #========== <function to get price> / <функция для получения цены> \/\/\/
    def get_price() -> float:
        try:
            url= 'https://api.binance.com/api/v3/ticker/price'
            response = req.get(url,params={'symbol':'BTCUSDT'},timeout=10)
            return float(response.json()['price'])
        except (req.exceptions.ConnectionError,req.ReadTimeout):
            print('ошибка соединения')
            return -1



    #========== <function to update the maximum price> / <функция для обновления максимальной цены> \/\/\/
    def update_max_price(price):
        max_price_text_line.clear()
        max_price_text_line.write(f"{price}$", font = ("Times New Roman" , 20))

        y = 180 + (price - BASE_PRICE)/dollars_for_pixel

        max_price_text_line.up()
        max_price_text_line.goto(-660, y)
        max_price_text_line.down()
        max_price_text_line.pencolor('green')
        max_price_text_line.goto(575, y)
            
        max_price_text_line.up()
        max_price_text_line.pencolor('black')
        max_price_text_line.goto(170 + end_palet_3, 403)

        update_interface()
        if is_real_time_graph:
            last_price = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            start_y = 180 + (last_price - BASE_PRICE)/dollars_for_pixel
            prev_last = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            redraw_prices(price_list, start_y, prev_last)

        if price_matrix:
            y = -240 + (price - BASE_PRICE)/dollars_for_pixel

            max_price_text_line.up()
            max_price_text_line.goto(-660, y)
            max_price_text_line.down()
            max_price_text_line.pencolor('green')
            max_price_text_line.goto(575, y)
                
            max_price_text_line.up()
            max_price_text_line.pencolor('black')
            max_price_text_line.goto(170 + end_palet_3, 403)



            if y < -210 and y > -300:
                redraw_back_to_live_palet()



    #========== <function to update the minimum price> / <функция для обновления минимальной цены> \/\/\/
    def update_min_price(price):
        min_price_text_line.clear()
        min_price_text_line.write(f"{price}$", font = ("Times New Roman" , 20))

        y = 180 + (price - BASE_PRICE)/dollars_for_pixel

        min_price_text_line.up()
        min_price_text_line.goto(-660, y)
        min_price_text_line.down()
        min_price_text_line.pencolor('red')
        min_price_text_line.goto(575, y)
            
        min_price_text_line.up()
        min_price_text_line.pencolor('black')
        min_price_text_line.goto(160 + end_palet_4, 403)


        update_interface()
        if is_real_time_graph:
            last_price = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            start_y = 180 + (last_price - BASE_PRICE)/dollars_for_pixel
            prev_last = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            redraw_prices(price_list, start_y, prev_last)

        if price_matrix:
            y = -240 + (price - BASE_PRICE)/dollars_for_pixel

            min_price_text_line.up()
            min_price_text_line.goto(-660, y)
            min_price_text_line.down()
            min_price_text_line.pencolor('red')
            min_price_text_line.goto(575, y)
                
            min_price_text_line.up()
            min_price_text_line.pencolor('black')
            min_price_text_line.goto(160 + end_palet_4, 403)

            if y < -210 and y > -300:
                redraw_back_to_live_palet()



    #========== <function to update the price text> / <функция для обновления текста с ценой> \/\/\/
    def update_price(price):
        write_price.clear()

        if is_real_time_graph and price:
            write_price.write(f"{price}$", font = ("Times New Roman", 25))
        else:
            write_price.goto(-645, 404)
            write_price.write(f"{blocks_edges[price_matrix_index][4][0]}-{blocks_edges[price_matrix_index][4][1]}🔰", font = ("Times New Roman", 20))
            write_price.goto(-645, 402)



    #========== <function to update the persent text> / <функция для обновления текста с процентом> \/\/\/
    def update_percent(price):
        price_percent.clear()
        present = (price - BASE_PRICE)/BASE_PRICE*100

        if abs(present) < 0.0001:
            present = 0.0

        price_percent.write(f'{present:+.3f}%', font = ("Times New Roman", 17))



    #========== <function to update the time text> / <функция для обновления текста с временем> \/\/\/
    def update_time():
        time_text.clear()
        time_text.write(current_time ,font = ("Times New Roman" , 25))



    #========== <function to draw segment of upper graph> / <функция для отрисовки сегмента верхнего графика> \/\/\/
    def draw_upper_graph(last_price, price):
            global upper_graph_x


            if is_real_time_graph:
                #===== <segment color definition> / <определение цвета сегмента> \/\/\/
                color = 'green' if last_price < price else '#cc0000' if last_price > price else "#000000"
                upper_graph.pencolor(color)

                #===== <y coord definition> / <определение вертикальной координаты> \/\/\/
                y = 180 + (price - BASE_PRICE)/dollars_for_pixel

                #===== <checking for appropriate scale> / <проверка на подходящий масштаб> \/\/\/
                if y >= 385 or y <= -25:
                    return 'autoscaling'

                #===== <draw segment> / <отрисовка сегмента> \/\/\/
                upper_graph_x += 19
                upper_graph.goto(upper_graph_x, y)



    #========== <function to draw segment of lower graph> / <функция для отрисовки сегмента нижнего графика> \/\/\/
    def draw_lower_graph():
            global lower_graph_x, blocks_edges, start_page_time


            #===== <data preparation> / <подготовка данных> \/\/\/
            list_with_prices = price_matrix[-1]

            first_price = list_with_prices[0]
            last_price = list_with_prices[-1]

            max_price_for_y = max(list_with_prices)
            min_price_for_y = min(list_with_prices)


            #===== <segment color definition> / <определение цвета сегмента> \/\/\/
            if len(price_matrix) != 60:
                color = 'green' if first_price < last_price else "#cc0000" if first_price > last_price else "#202020"
            else:
                color = '#00AA00' if first_price < last_price else "#ff2222" if first_price > last_price else "#353535"

            #===== <coords preparation> / <подготовка координат> \/\/\/
            y1 = -240 + (first_price - BASE_PRICE)/dollars_for_pixel
            y2 = -240 + (last_price - BASE_PRICE)/dollars_for_pixel

            max_y = -240 + (max_price_for_y - BASE_PRICE)/dollars_for_pixel
            min_y = -240 + (min_price_for_y - BASE_PRICE)/dollars_for_pixel

            max_y_hitbox = max_y            
            min_y_hitbox = min_y

            if max_y + abs(min_y) < 20:
                additional_hitxob = (20-(max_y + abs(min_y)))/2
                max_y_hitbox += additional_hitxob            
                min_y_hitbox -= additional_hitxob

            
            #===== <time preparation> / <подготовка времени> \/\/\/
            current_time = time.strftime("%H:%M", time.localtime())
            times_list.append([start_page_time, current_time])

            #===== <adding data to the block hitbox list> / <добавление данных в список хитбоксов блоков> \/\/\/
            edges = [lower_graph_x, lower_graph_x + 20, min_y_hitbox, max_y_hitbox, times_list[-1]]
            blocks_edges.append(edges)

            start_page_time = current_time

            #===== <draw block> / <отрисовка блока> \/\/\/
            lower_graph.pencolor(color)
            lower_graph.up()
            lower_graph.goto(lower_graph_x + 10, max_y)
            lower_graph.down()
            lower_graph.goto(lower_graph_x + 10, min_y)

            lower_graph.up()
            lower_graph.goto(lower_graph_x, y1)

            lower_graph.pencolor('#000000')
            lower_graph.fillcolor(color)        

            lower_graph.begin_fill()
            lower_graph.down()   
            lower_graph.goto(lower_graph_x, y2)
            lower_graph.goto(lower_graph_x + 20, y2)
            lower_graph.goto(lower_graph_x + 20, y1)
            lower_graph.goto(lower_graph_x, y1)
            lower_graph.end_fill()

            lower_graph_x += 20

            #====== <Bugfix for the maximum and minimum price lines> / <багфикс линий максимальной и минимальной цены> \/\/\/
            if len(price_matrix) == 1:
                update_max_price(max_price)
                update_min_price(min_price)
                update_interface()



    #========== <function to redraw the page of upper graph> / <функция для перерисовки страницы верхнего графика> \/\/\/
    def redraw_prices(prices, start_y, prev_last = BASE_PRICE):
        global upper_graph_x

        #===== <preparing> / <подготовка> \/\/\/
        upper_graph_x = -620
        upper_graph.clear()

        upper_graph.up()
        upper_graph.goto(upper_graph_x, start_y)
        upper_graph.down()


        #===== <redrawing> / <перерисовка> \/\/\/
        for i in range(len(prices)):
            #=== <data preparation> / <подготовка данных> \/\/\/
            last_price = prices[i - 1] if i > 0 else prev_last
            price = prices[i]

            #=== <segment color definition> / <определение цвета сегмента> \/\/\/
            color = 'green' if last_price < price else "#cc0000" if last_price > price else 'black'
            upper_graph.pencolor(color)

            #=== <draw segment> / <отрисовка сегмента> \/\/\/
            y = 180 + (price - BASE_PRICE)/dollars_for_pixel

            upper_graph_x += 19
            upper_graph.goto(upper_graph_x, y)



    #========== <function to redraw lower graph> / <функция для перерисовки нижнего графика> \/\/\/
    def redraw_lower_graph():
        global lower_graph_x

        #===== <preparing> / <подготовка> \/\/\/
        lower_graph_x = -650

        lower_graph.clear()

        #===== <redrawing> / <перерисовка> \/\/\/
        for i in range(len(price_matrix)):
            #=== <data preparation> / <подготовка данных> \/\/\/
            list_with_prices = price_matrix[i]

            first_price = list_with_prices[0]
            last_price = list_with_prices[-1]

            max_price_for_y  = max(list_with_prices)
            min_price_for_y  = min(list_with_prices)

            #=== <segment color definition> / <определение цвета сегмента> \/\/\/
            if i == price_matrix_index:
                color = "#00AA00" if first_price < last_price else "#ff2222"
            else:   
                color = 'green' if first_price < last_price else "#cc0000"

            #=== <coords preparation> / <подготовка координат> \/\/\/
            y1 = -240 + (first_price - BASE_PRICE)/dollars_for_pixel
            y2 = -240 + (last_price - BASE_PRICE)/dollars_for_pixel

            max_y = -240 + (max_price_for_y - BASE_PRICE)/dollars_for_pixel
            min_y = -240 + (min_price_for_y - BASE_PRICE)/dollars_for_pixel

            #=== <draw block> / <отрисовка блока> \/\/\/
            lower_graph.pencolor(color)
            lower_graph.up()
            lower_graph.goto(lower_graph_x + 10, max_y)
            lower_graph.down()
            lower_graph.goto(lower_graph_x + 10, min_y)

            lower_graph.pencolor('#000000')
            lower_graph.fillcolor(color)

            lower_graph.up()
            lower_graph.goto(lower_graph_x, y1)

            lower_graph.begin_fill()
            lower_graph.down()        
            lower_graph.goto(lower_graph_x, y2)
            lower_graph.goto(lower_graph_x + 20, y2)
            lower_graph.goto(lower_graph_x + 20, y1)
            lower_graph.goto(lower_graph_x, y1)
            lower_graph.end_fill()

            lower_graph_x += 20


    #========== <function to redraw the live button> / <функция для перерисовки кнопки live> \/\/\/
    def redraw_back_to_live_palet():
        #===== <preparing> / <подготовка> \/\/\/
        back_to_live_palet.clear()

        #===== <draw button> / <отрисовка кнопки> \/\/\/
        if len(price_matrix) != 60:
            back_to_live_palet.up()
            back_to_live_palet.goto(lower_graph_x, -210)
            back_to_live_palet.down()

            #=== <button color definition> / <определение цвета кнопки> \/\/\/
            if is_real_time_graph:
                back_to_live_palet.pencolor(bright_color_1) #"#125042"
                back_to_live_palet.fillcolor(bright_color_2) #  "#1b866f"     
            else:
                back_to_live_palet.pencolor(color_1)#"#0d3b31"
                back_to_live_palet.fillcolor(color_2)#"#145f4f"


            #=== <redrawing> / <перерисовка> \/\/\/
            back_to_live_palet.begin_fill()
            back_to_live_palet.goto(lower_graph_x + 20, -210)
            back_to_live_palet.goto(lower_graph_x + 20, -300)
            back_to_live_palet.goto(lower_graph_x, -300)
            back_to_live_palet.goto(lower_graph_x, -210)
            back_to_live_palet.end_fill()


            #=== <redrawing text> / <перерисовка текста> \/\/\/
            back_to_live_palet.up()
            back_to_live_palet.goto(lower_graph_x + 5, -235)
            back_to_live_palet.write("L", font = ("Times New Roman" , 14, "bold"))
            back_to_live_palet.goto(lower_graph_x + 7, -255)
            back_to_live_palet.write("I", font = ("Times New Roman" , 14, "bold"))
            back_to_live_palet.goto(lower_graph_x + 4, -275)
            back_to_live_palet.write("V", font = ("Times New Roman" , 14, "bold"))
            back_to_live_palet.goto(lower_graph_x + 5, -295)
            back_to_live_palet.write("E", font = ("Times New Roman" , 14, "bold"))



    #========== <function for changing the scale of a graph> / <функция для изменения масштаба графика> \/\/\/
    def autoscaling():
        global dollars_for_pixel, upper_graph_x, lower_graph_x

        #===== <checking for the need for autoscaling> / <проверка на необходимость автомасштабирования> \/\/\/
        if (upper_graph.ycor() >= 385 or upper_graph.ycor() <= -25) or ((180 + (price_list[-1] - BASE_PRICE)/dollars_for_pixel) >= 385 or (180 + (price_list[-1] - BASE_PRICE)/dollars_for_pixel) <= -30):
            #===== <preparing> / <подготовка> \/\/\/
            upper_graph.clear()
            lower_graph.clear()
            price_line_text.clear()

            upper_graph_x = -620

            #===== <changes in scale> / <изменеия масштаба> \/\/\/
            if dollars_for_pixel == 0.05:
                dollars_for_pixel = 0.1
            elif dollars_for_pixel == 0.1:
                dollars_for_pixel = 0.15
            elif dollars_for_pixel <= 0.15:
                dollars_for_pixel = 0.25
            elif dollars_for_pixel <= 0.25:
                dollars_for_pixel = 0.35
            elif dollars_for_pixel <= 0.35:
                dollars_for_pixel = 0.5
            elif dollars_for_pixel == 0.5:
                dollars_for_pixel = 0.75
            elif dollars_for_pixel == 0.75:
                dollars_for_pixel = 1
            elif dollars_for_pixel == 1:
                dollars_for_pixel = 1.75
            elif dollars_for_pixel == 1.75:
                dollars_for_pixel = 2.5
            elif dollars_for_pixel == 2.5:
                dollars_for_pixel = 5
            else:
                dollars_for_pixel += 5



            #===== <if the program is in live mode> / <если программа в live режиме> \/\/\/
            if is_real_time_graph:
                last_price = BASE_PRICE if not price_matrix else price_matrix[-1][-1]

                upper_graph.up()
                upper_graph.goto(upper_graph_x, 180 + (last_price - BASE_PRICE)/dollars_for_pixel)
                upper_graph.down()

                #=== <redrawing> / <перерисовка> \/\/\/
                for i in range(len(price_list)):
                    #== <data preparation> / <подготовка данных> \/\/\/
                    last_price = BASE_PRICE if not price_matrix and i == 0 else price_matrix[-1][-1] if price_matrix and i == 0 else price_list[i-1]
                    price = price_list[i]

                    #== <segment color definition> / <определение цвета сегмента> \/\/\/
                    color = 'green' if last_price < price else '#cc0000' if last_price > price else 'black'
                    upper_graph.pencolor(color)


                    #== <y coord definition> / <определение вертикальной координаты> \/\/\/
                    y = 180 + (price - BASE_PRICE)/dollars_for_pixel

                    #== <checking for appropriate scale> / <проверка на подходящий масштаб> \/\/\/
                    if y >= 385 or y <= -25:
                        autoscaling()

                    #== <draw segment> / <отрисовка сегмента> \/\/\/
                    upper_graph_x += 19
                    upper_graph.goto(upper_graph_x, y)

            #===== <if the program is in history mode> / <если программа в режиме истории> \/\/\/
            else:
                #=== <preparing> / <подготовка> \/\/\/
                first_price = price_matrix[price_matrix_index][0]

                upper_graph.up()
                upper_graph.goto(upper_graph_x, 180 + (first_price - BASE_PRICE)/dollars_for_pixel)
                upper_graph.down()

                #=== <redrawing> / <перерисовка> \/\/\/
                for i in range(len(price_matrix[price_matrix_index])):
                    #== <data preparation> / <подготовка данных> \/\/\/
                    last_price = BASE_PRICE if i == 0 and price_matrix_index == 0 else price_matrix[price_matrix_index - 1][-1] if i == 0 and price_matrix_index != 0 else price_matrix[price_matrix_index][i - 1]
                    list_with_prices_autoscaling = price_matrix[price_matrix_index]
                    price = list_with_prices_autoscaling[i]

                    #== <segment color definition> / <определение цвета сегмента> \/\/\/
                    color = 'green' if last_price < price else '#cc0000' if last_price > price else 'black'
                    upper_graph.pencolor(color)

                    #== <y coord definition> / <определение вертикальной координаты> \/\/\/
                    y = 180 + (price - BASE_PRICE)/dollars_for_pixel

                    #== <checking for appropriate scale> / <проверка на подходящий масштаб> \/\/\/
                    if y >= 385 or y <= -25:
                        autoscaling()

                    #== <draw segment> / <отрисовка сегмента> \/\/\/
                    upper_graph_x += 19
                    upper_graph.goto(upper_graph_x, y)

            #===== <if there are blocks in the lower graph> / <если есть блоки нижнего графика> \/\/\/
            if price_matrix:
                #=== <preparing> / <подготовка> \/\/\/
                lower_graph_x = -650
                blocks_edges.clear()

                #=== <redrawing> / <перерисовка> \/\/\/
                for i in range(len(price_matrix)):
                    #== <data preparation> / <подготовка данных> \/\/\/
                    list_with_prices = price_matrix[i]

                    first_price = list_with_prices[0]
                    last_price = list_with_prices[-1]

                    max_price_for_y = max(list_with_prices)
                    min_price_for_y = min(list_with_prices)


                    #== <block color definition> / <определение цвета блока> \/\/\/
                    if i == price_matrix_index:
                        color = "#00AA00" if first_price < last_price else "#ff2222"
                    else:   
                        color = 'green' if first_price < last_price else "#cc0000"


                    #== <coords preparation> / <подготовка координат> \/\/\/
                    y1 = -240 + (first_price - BASE_PRICE)/dollars_for_pixel
                    y2 = -240 + (last_price - BASE_PRICE)/dollars_for_pixel

                    max_y = -240 + (max_price_for_y - BASE_PRICE)/dollars_for_pixel
                    min_y = -240 + (min_price_for_y - BASE_PRICE)/dollars_for_pixel

                    max_y_hitbox = max_y            
                    min_y_hitbox = min_y

                    if max_y + abs(min_y) < 20:
                        additional_hitxob = (20-(max_y + abs(min_y)))/2
                        max_y_hitbox += additional_hitxob            
                        min_y_hitbox -= additional_hitxob

                    #== <adding data to the block hitbox list> / <добавление данных в список хитбоксов блоков> \/\/\/
                    edges = [lower_graph_x, lower_graph_x + 20, min_y_hitbox, max_y_hitbox, times_list[i]]
                    blocks_edges.append(edges)


                    #== <draw block> / <отрисовка блока> \/\/\/
                    lower_graph.pencolor(color)
                    lower_graph.up()
                    lower_graph.goto(lower_graph_x + 10, max_y)
                    lower_graph.down()
                    lower_graph.goto(lower_graph_x + 10, min_y)

                    lower_graph.pencolor('#000000')
                    lower_graph.fillcolor(color)

                    lower_graph.up()
                    lower_graph.goto(lower_graph_x, y1)

                    lower_graph.begin_fill()
                    lower_graph.down()        
                    lower_graph.goto(lower_graph_x, y2)
                    lower_graph.goto(lower_graph_x + 20, y2)
                    lower_graph.goto(lower_graph_x + 20, y1)
                    lower_graph.goto(lower_graph_x, y1)
                    lower_graph.end_fill()

                    lower_graph_x += 20

            #===== <updating the maximum and minimum prices> / <обновление максимальной и мнинимальной цены> \/\/\/
            update_max_price(max_price)
            update_min_price(min_price)


            #===== <updating the prices> / <обновление цен> \/\/\/     
            for i in range(11):
                price_line_text.goto(580, BASE_PRICE*MASHTAB_1 - i*20 - 8)
                price_line_text.write(f"{BASE_PRICE - (i*20)*dollars_for_pixel}$", font = ("Arial" , 10, 'normal'))


            for i in range(11):
                price_line_text.goto(580, BASE_PRICE*MASHTAB_1 + i*20 - 8)
                price_line_text.write(f"{BASE_PRICE + (i*20)*dollars_for_pixel}$", font = ("Arial" , 10, 'normal'))


            for i in range(11):
                price_line_text.goto(580, BASE_PRICE*MASHTAB_2 - i*20 - 8)
                price_line_text.write(f"{BASE_PRICE - (i*20)*dollars_for_pixel}$", font = ("Arial" , 10, 'normal'))


            for i in range(11):
                price_line_text.goto(580, BASE_PRICE*MASHTAB_2 + i*20 - 8)
                price_line_text.write(f"{BASE_PRICE + (i*20)*dollars_for_pixel}$", font = ("Arial" , 10, 'normal'))


    #========== <function of redrawing some parts of the interface> / <функция перерисовки некоторых частей интерфейса> \/\/\/
    def update_interface():

        #===== <arrow keys to move between history pages> / <стреслки для перемещения между страницами истории> \/\/\/
        #=== <left arrow button> / <кнопка стрелка влево> \/\/\/
        #== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
        interface_palets.pencolor("#353535")
        interface_palets.fillcolor("#3A3A3A")

        interface_palets.up()
        interface_palets.goto(-660, 210)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(-660, 150)
        interface_palets.goto(-630, 150)
        interface_palets.goto(-630, 210)
        interface_palets.goto(-660, 210)
        interface_palets.end_fill()

        if price_matrix_index > 0:
            interface_palets.pencolor(color_1)
            interface_palets.fillcolor(color_2)
        else:
            interface_palets.pencolor(pale_color_1)
            interface_palets.fillcolor(pale_color_2)

        #== <arrow> / <стрелка> \/\/\/
        interface_palets.up()
        interface_palets.goto(-655, 180)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(-635, 200)
        interface_palets.goto(-635, 160)
        interface_palets.goto(-655, 180)
        interface_palets.end_fill()


        #=== <right arrow button> / <кнопка стрелка вправо> \/\/\/
        #== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
        interface_palets.pencolor("#353535")
        interface_palets.fillcolor("#3A3A3A")

        interface_palets.up()
        interface_palets.goto(560, 210)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(560, 150)
        interface_palets.goto(530, 150)
        interface_palets.goto(530, 210)
        interface_palets.goto(560, 210)
        interface_palets.end_fill()

        can_go_right = False
        if not is_real_time_graph:
            if price_matrix_index <= len(price_matrix) - 1:
                can_go_right = True

        if price_matrix_index == 59:
            can_go_right = False
        
        if can_go_right:
            interface_palets.pencolor(color_1)
            interface_palets.fillcolor(color_2)
        else:
            interface_palets.pencolor(pale_color_1)
            interface_palets.fillcolor(pale_color_2)

        #== <arrow> / <стрелка> \/\/\/
        interface_palets.up()
        interface_palets.goto(555, 180)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(535, 200)
        interface_palets.goto(535, 160)
        interface_palets.goto(555, 180)
        interface_palets.end_fill()


        #===== <interface_lines> / <линии интерфейса> \/\/\/
        interface_lines.up()
        interface_lines.goto(560, 390)
        interface_lines.down()
        interface_lines.goto(560,-450)

        interface_lines.up()
        interface_lines.goto(-660, 390)
        interface_lines.down()
        interface_lines.goto(660, 390)

        interface_lines.up()
        interface_lines.goto(-660, -30)
        interface_lines.down()
        interface_lines.goto(660, -30)

        if len(price_matrix) != 60:
            redraw_back_to_live_palet()


        #========== <version display> / <отображение версии> \/\/\/
        interface_lines.up()
        interface_lines.pencolor("#000000")
        interface_lines.goto(-650, -445)
        interface_lines.write(VERSION, font = ("Times New Roman" , 25))


    #========== <function for reading keystrokes> / <функция для считывания нажатий> \/\/\/
    def on_click(x, y):
        global price_matrix_index, is_real_time_graph, navigating

        #===== <click on candle> / <клик по свече> \/\/\/
        if price_matrix:
            
            for i in range(len(blocks_edges)):
                #=== <hitbox hit check> / <проверка на поподание в хитбокс> \/\/\/
                if (x > blocks_edges[i][0] and x < blocks_edges[i][1]) and (y > blocks_edges[i][2] and y < blocks_edges[i][3]):
                    if i + 1 != 2:
                        is_real_time_graph = False

                    #=== <drawing the history page> / <отрисовка страници истории> \/\/\/
                    win.tracer(0)
                    go_to_history_page(i)
                    update_interface()
                    win.tracer(1)

                    return

        if navigating:
            return
        navigating = True


        try:
            #===== <click on the arrow> / <клик по стрелке> \/\/\/
            #=== <click on the left arrow> / <клик по стрелке влево> \/\/\/
            #== <hitbox hit check> / <проверка на поподание в хитбокс> \/\/\/
            if x > -660 and x < -630 and y > 150 and y < 210 and price_matrix_index != 0:
                if is_real_time_graph:
                    if not price_matrix:
                        return
                    is_real_time_graph = False

                price_matrix_index -= 1

                #== <data preparation> / <подготовка данных> \/\/\/
                prices = price_matrix[price_matrix_index]
                start_y = 180 + (prices[0] - BASE_PRICE) / dollars_for_pixel
                prev_last = price_matrix[price_matrix_index - 1][-1] if price_matrix_index > 0 else BASE_PRICE


                #== <drawing the history page> / <отрисовка страници истории> \/\/\/
                win.tracer(0)
                redraw_prices(prices=prices, start_y=start_y, prev_last=prev_last)
                redraw_lower_graph()
                update_interface()
                update_price(price_list[-1] if price_list else None)
                win.tracer(1)


            #=== <click on the right arrow> / <клик по стрелке вправо> \/\/\/
            elif x > 530 and x < 560 and y > 150 and y < 210:
                if not is_real_time_graph:
                    #== <if the graph is not in live mode after moving> /
                    #== <Если после перемещения график не находится в live режиме> \/\/\/
                    if price_matrix_index < len(price_matrix) - 1:
                        price_matrix_index += 1

                        #= <data preparation> / <подготовка данных> \/\/\/
                        prices = price_matrix[price_matrix_index]
                        prev_last = price_matrix[price_matrix_index - 1][-1]
                        start_y = 180 + (prices[0] - BASE_PRICE) / dollars_for_pixel


                        #== <drawing the history page> / <отрисовка страници истории> \/\/\/
                        win.tracer(0)
                        redraw_prices(prices=prices, start_y=start_y, prev_last=prev_last)
                        redraw_lower_graph()
                        update_interface()
                        update_price(price_list[-1] if price_list else None)
                        win.tracer(1)


                    #== <if after moving the graph goes into live mode> /
                    #== <Если после перемещения график переходит в live режим> \/\/\/
                    elif price_matrix_index == len(price_matrix) - 1 and price_list:
                        is_real_time_graph = True
                        price_matrix_index += 1

                        #= <data preparation> / <подготовка данных> \/\/\/
                        prev_last = price_matrix[-1][-1]
                        start_y = 180 + (prev_last - BASE_PRICE) / dollars_for_pixel


                        #== <drawing the history page> / <отрисовка страници истории> \/\/\/
                        win.tracer(0)
                        redraw_prices(price_list, start_y, prev_last)
                        redraw_lower_graph()
                        update_interface()
                        update_price(price_list[-1] if price_list else None)
                        win.tracer(1)

            #===== <click on the back to live button> / <клик по конпке возврата в live> \/\/\/
            elif x > lower_graph_x and x < lower_graph_x + 20 and y > -300 and y < -210:
                if not is_real_time_graph:
                    if len(price_matrix) != 60:

                        #=== <data preparation> / <подготовка данных> \/\/\/
                        prev_last = price_matrix[-1][-1]
                        start_y = 180 + (prev_last - BASE_PRICE) / dollars_for_pixel
                        is_real_time_graph = True
                        price_matrix_index = len(price_matrix)

                        #== <drawing live graph> / <отрисовка live графика> \/\/\/
                        win.tracer(0)
                        redraw_prices(price_list, start_y, prev_last)
                        redraw_lower_graph()
                        update_interface()                        
                        update_price(price_list[-1] if price_list else price_matrix[-1][-1])
                        win.tracer(1)
                        

        finally:
            navigating = False
            

    #========== <function to move to the history page> / <функция перемещения на страницу истории> \/\/\/
    def go_to_history_page(page):
        global is_real_time_graph, price_matrix_index, navigating
                    
        if navigating:
            return
        navigating = True

        price_matrix_index = page

        #===== <data preparation> / <подготовка данных> \/\/\/
        prices = price_matrix[price_matrix_index]
        start_y = 180 + (prices[0] - BASE_PRICE)/dollars_for_pixel
        prev_last = price_matrix[price_matrix_index - 1][-1] if price_matrix_index != 0 else BASE_PRICE

        #===== <drawing the history page> / <отрисовка страници истории> \/\/\/
        redraw_prices(prices = prices, start_y = start_y, prev_last = prev_last)
        redraw_lower_graph()

        navigating = False

        update_price(price_list[-1] if price_list else None)


    #========== <function to check if the top graph is complete> / <функция для проверки заавершения верхнего графика> \/\/\/
    def end_upper_graph():
        global isend_upper_graph
        if len(price_list) == 60:
            if is_real_time_graph:            
                isend_upper_graph = 'upper_graph_end'
            else:
                isend_upper_graph = 'upper_graph_end_in_history'


    #==================== <program preparation> / <подготовка программы> \/\/\/
    start_page_time = time.strftime("%H:%M", time.localtime())

    win.tracer(0)
    redraw_back_to_live_palet()
    win.tracer(1)


    #==================== <function main> / <главная функция> \/\/\/
    def main():
        global price_matrix, price_list, upper_graph_x, max_price, min_price, price_matrix_index, isend_upper_graph, current_time
        try:
            win.tracer(0)

            #========== <check for completion> / <проверка на завершение> \/\/\/
            end_upper_graph()

            if isend_upper_graph == 'upper_graph_end':
                price_matrix.append(price_list.copy())

                if len(price_matrix) == 60:
                    print('end')
                    draw_lower_graph()
                    update_max_price(max_price)
                    update_min_price(min_price)
                    price_list.clear()
                    back_to_live_palet.clear()
                    update_price(None)
                    win.update()
                    return


                price_list.clear()
                upper_graph.clear()


                isend_upper_graph = None


                upper_graph_x = -620

                upper_graph.up()                
                upper_graph.goto(upper_graph_x, upper_graph.ycor())
                upper_graph.down()

                price_matrix_index += 1
                draw_lower_graph()
                redraw_back_to_live_palet()

            elif isend_upper_graph == 'upper_graph_end_in_history':
                price_matrix.append(price_list.copy())

                if len(price_matrix) == 60:
                    draw_lower_graph()
                    update_max_price(max_price)
                    update_min_price(min_price)
                    price_list.clear()
                    back_to_live_palet.clear()
                    update_price(None)
                    win.update()
                    return

                price_list.clear()

                isend_upper_graph = None

                draw_lower_graph()
                redraw_back_to_live_palet()

            price = get_price()


            #========== <graph update> / <обновление графика> \/\/\/
            if price == -1:
                win.ontimer(main, 1000)
                return
            else:
                price_list.append(price)    
                
                if is_real_time_graph:
                    if len(price_list) == 1:
                        is_autoscaling = draw_upper_graph(BASE_PRICE if not price_matrix else price_matrix[-1][-1], price_list[-1])
                    else:
                        is_autoscaling = draw_upper_graph(price_list[-2], price_list[-1])

                        if is_autoscaling == 'autoscaling': #это багфикс
                            autoscaling()
                    
                autoscaling()

                #========== <time, price, percent update> / <обновление времени, цены, процента> \/\/\/
                if current_time != time.strftime("%H:%M", time.localtime()):
                    current_time = time.strftime("%H:%M", time.localtime())
                    update_time()

                update_price(price)
                update_percent(price)
                

                #========== <min, max price updates> / <обновление максимальной и минимальной цены> \/\/\/
                if price > max_price:
                    max_price = price
                    update_max_price(price)
                elif price < min_price:
                    min_price = price
                    update_min_price(price)


            #========== <recursive call> / <рекурсивный вызов> \/\/\/
            win.ontimer(main, 1000)


        #========== <error handling> / <обработка ошибок> \/\/\/
        except tk.TclError:
            return
        finally:     
            win.tracer(1)

    #==================== <call main> / <вызов main> \/\/\/
    main()


    win.onclick(on_click, 1)
    win.listen()


win.mainloop()

