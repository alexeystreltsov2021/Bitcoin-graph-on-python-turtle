#==================== <import modules> / <импорт модулей> \/\/\/
import turtle as t
import time
import requests as req
import tkinter as tk


#==================== <set screen settings> / <насторйки экрана> \/\/\/
win = t.Screen()

#========== <set scale constant> / <задание константы для масштабирования> \/\/\/
display_height = win._root.winfo_screenheight()

SCALE_CONSTANT = (display_height - 170)/910


win.setup(width = 1320*SCALE_CONSTANT,height = 910*SCALE_CONSTANT)
win._root.resizable(False,False)
win._root.title('ГРАФИК БИТКОИНА')


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
interface_lines.pensize(4*SCALE_CONSTANT)
interface_palets.pensize(4*SCALE_CONSTANT)
upper_graph.pensize(4*SCALE_CONSTANT)
lower_graph.pensize(2*SCALE_CONSTANT)
back_to_live_palet.pensize(2*SCALE_CONSTANT)


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

startscreen.shape("turtle")
startscreen.shapesize(15*SCALE_CONSTANT)

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




#==================== <constants> / <константы> \/\/\/
#========== <number of blocks in the lower graph> / <количество блоков нажнего графика>
LOWER_GRAPH_BLOCKS = 60

#========== <number of segments in the upper graph> / <количество сегментов верхнего графика>
UPPER_GRAPH_SEGMENTS = 60

#========== <delay between segments of the upper graph> / <задержка между сегментами верхнего графика>
TIME_INTERVAL_FOR_ONE_SEGMENT = 1000

BLOCK_WIDTH = 1200*SCALE_CONSTANT/LOWER_GRAPH_BLOCKS
SEGMENT_WIDTH = 1140*SCALE_CONSTANT/UPPER_GRAPH_SEGMENTS

UPPER_GRAPH_X = -620*SCALE_CONSTANT
LOWER_GRAPH_X = -650*SCALE_CONSTANT


#==================== <variables> / <переменные> \/\/\/
dollars_for_pixel = 0.05*SCALE_CONSTANT

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

VERSION = "version 1.0.5"

#==================== <start screen> / <стартовый экран> \/\/\/
def start_screen():
    #========== <background> / <задний фон> \/\/\/
    startscreen.pencolor("#383838")
    startscreen.dot(10000*SCALE_CONSTANT)
    startscreen.pencolor("#303030")
    startscreen.dot(1500*SCALE_CONSTANT)
    startscreen.pencolor("#2B2B2B")
    startscreen.dot(1200*SCALE_CONSTANT)
    startscreen.pencolor("#272727")
    startscreen.dot(750*SCALE_CONSTANT)
    startscreen.pencolor("#242424")
    startscreen.dot(300*SCALE_CONSTANT)


    startscreen.up()
    startscreen.goto(-590*SCALE_CONSTANT, 250*SCALE_CONSTANT)
    startscreen.speed(0)

    #========== <the inscription "BITCOIN GRAPH 3"> / <надпись "BITCOIN GRAPH 3"> \/\/\/
    startscreen.pencolor("#000000")
    startscreen.write("B", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(90*SCALE_CONSTANT)
    startscreen.write("I", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(50*SCALE_CONSTANT)
    startscreen.write("T", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(80*SCALE_CONSTANT)
    startscreen.write("C", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(90*SCALE_CONSTANT)
    startscreen.write("O", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(90*SCALE_CONSTANT)
    startscreen.write("I", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(60*SCALE_CONSTANT)
    startscreen.write("N", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(140*SCALE_CONSTANT)
    startscreen.write("G", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(100*SCALE_CONSTANT)
    startscreen.write("R", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(100*SCALE_CONSTANT)
    startscreen.write("A", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(100*SCALE_CONSTANT)
    startscreen.write("P", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(80*SCALE_CONSTANT)
    startscreen.write("H", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))
    startscreen.forward(140*SCALE_CONSTANT)
    startscreen.write("3", font = ("Times New Roman" , int(100*SCALE_CONSTANT)))

    #========== <delay> / <задержка> \/\/\/
    startscreen.speed(5)

    #========== <preparing> / <подготовка> \/\/\/
    startscreen.up()
    startscreen.goto(-630*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.speed(0)

    #========== <the inscription "POWERED BY TURTLE"> / <надпись "POWERED BY TURTLE"> \/\/\/
    startscreen.pencolor("#000000")
    startscreen.write("P", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(70*SCALE_CONSTANT)
    startscreen.write("O", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(80*SCALE_CONSTANT)
    startscreen.write("W", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(110*SCALE_CONSTANT)
    startscreen.write("E", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(70*SCALE_CONSTANT)
    startscreen.write("R", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(80*SCALE_CONSTANT)
    startscreen.write("E", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(70*SCALE_CONSTANT)
    startscreen.write("D", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(120*SCALE_CONSTANT)
    startscreen.write("B", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(80*SCALE_CONSTANT)
    startscreen.write("Y", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(120*SCALE_CONSTANT)
    startscreen.write("T", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(80*SCALE_CONSTANT)
    startscreen.write("U", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(90*SCALE_CONSTANT)
    startscreen.write("R", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(70*SCALE_CONSTANT)
    startscreen.write("T", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(70*SCALE_CONSTANT)
    startscreen.write("L", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))
    startscreen.forward(70*SCALE_CONSTANT)
    startscreen.write("E", font = ("Times New Roman" , int(85*SCALE_CONSTANT)))

    #========== <preparing> / <подготовка> \/\/\/
    time.sleep(1)

    #========== <version display> / <отображение версии> \/\/\/
    win.tracer(0)
    startscreen.pencolor("#000000")
    startscreen.up()
    startscreen.goto(-650*SCALE_CONSTANT, -445*SCALE_CONSTANT)
    startscreen.write(VERSION, font = ("Times New Roman" , int(25*SCALE_CONSTANT)))

    startscreen.goto(0,-200*SCALE_CONSTANT)
    startscreen.left(90)
    startscreen.showturtle()
    win.tracer(1)

    #========== <delay> / <задержка> \/\/\/
    time.sleep(2)

    win.tracer(0)
    startscreen.hideturtle()


    #========== <background> / <задний фон> \/\/\/
    startscreen.goto(0,0)
    startscreen.pencolor("#383838")
    startscreen.dot(10000*SCALE_CONSTANT)
    startscreen.pencolor("#303030")
    startscreen.dot(1500*SCALE_CONSTANT)
    startscreen.pencolor("#2B2B2B")
    startscreen.dot(1200*SCALE_CONSTANT)
    startscreen.pencolor("#272727")
    startscreen.dot(750*SCALE_CONSTANT)
    startscreen.pencolor("#242424")
    startscreen.dot(300*SCALE_CONSTANT)

    #========== <version display> / <отображение версии> \/\/\/
    startscreen.up()
    startscreen.pencolor("#000000")
    startscreen.goto(-650*SCALE_CONSTANT, -445*SCALE_CONSTANT)
    startscreen.write(VERSION, font = ("Times New Roman" , int(25*SCALE_CONSTANT)))

    #========== <the inscription "Select theme:"> / <надпись "Select theme:"> \/\/\/
    startscreen.goto(-630*SCALE_CONSTANT, 320*SCALE_CONSTANT)
    startscreen.write("Select theme:", font = ("Times New Roman" , int(80*SCALE_CONSTANT)))


    #========== <green theme block> / <блок зеленой темы> \/\/\/
    startscreen.pencolor("#0d3b31")
    startscreen.fillcolor("#145f4f")
    startscreen.pensize(6*SCALE_CONSTANT)
    startscreen.goto(-550*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-450*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.goto(-450*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(-550*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(-550*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(-525*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-475*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.goto(-475*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(-525*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(-525*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.end_fill()


    #========== <orange theme block> / <блок оранжевой темы> \/\/\/
    startscreen.pencolor("#d68a43")
    startscreen.fillcolor("#e4974f")
    startscreen.pensize(6*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(-350*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-250*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.goto(-250*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(-350*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(-350*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(-325*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-275*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.goto(-275*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(-325*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(-325*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.end_fill()


    #========== <blue theme block> / <блок синей темы> \/\/\/
    startscreen.pencolor("#13335e")
    startscreen.fillcolor("#1e416e")
    startscreen.pensize(6*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(-50*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-150*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.goto(-150*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(-50*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(-50*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(-75*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(-125*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.goto(-125*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(-75*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(-75*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.end_fill()


    #========== <green violet block> / <блок фиолетовой темы> \/\/\/
    startscreen.pencolor("#492f57")
    startscreen.fillcolor("#523461")
    startscreen.pensize(6*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(50*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(150*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.goto(150*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(50*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(50*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(125*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(75*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.goto(75*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(125*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(125*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.end_fill()


    #========== <green red block> / <блок красной темы> \/\/\/
    startscreen.pencolor("#af2929")
    startscreen.fillcolor("#c53a3a")
    startscreen.pensize(6*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(350*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(250*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.goto(250*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(350*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(350*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(325*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(275*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.goto(275*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(325*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(325*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.end_fill()


    #========== <green white block> / <блок белой темы> \/\/\/
    startscreen.pencolor("#969696")
    startscreen.fillcolor("#A3A3A3")
    startscreen.pensize(6*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(550*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(450*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.goto(450*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(550*SCALE_CONSTANT, 100*SCALE_CONSTANT)
    startscreen.goto(550*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    startscreen.end_fill()

    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(525*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(475*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.goto(475*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(525*SCALE_CONSTANT, 25*SCALE_CONSTANT)
    startscreen.goto(525*SCALE_CONSTANT, 75*SCALE_CONSTANT)
    startscreen.end_fill()


    #========== <start button> / <кнопка старт> \/\/\/
    #===== <block> / <основа> \/\/\/
    startscreen.pencolor("#3d3d3d")
    startscreen.fillcolor("#4D4D4D")
    startscreen.pensize(4*SCALE_CONSTANT)
    startscreen.up()
    startscreen.goto(-170*SCALE_CONSTANT, -150*SCALE_CONSTANT)
    startscreen.down()
    startscreen.begin_fill()
    startscreen.goto(170*SCALE_CONSTANT, -150*SCALE_CONSTANT)
    startscreen.goto(170*SCALE_CONSTANT, -250*SCALE_CONSTANT)
    startscreen.goto(-170*SCALE_CONSTANT, -250*SCALE_CONSTANT)
    startscreen.goto(-170*SCALE_CONSTANT, -150*SCALE_CONSTANT)
    startscreen.end_fill()

    #===== <text> / <текст> \/\/\/
    startscreen.pencolor("#000000")
    startscreen.up()
    startscreen.goto(-160*SCALE_CONSTANT, -260*SCALE_CONSTANT)
    startscreen.write("START", font = ("Times New Roman" , int(75*SCALE_CONSTANT)))

    win.tracer(1)

    startscreen_2.pencolor("#3d3d3d")

    #========== <click test> / <проверка нажатия> \/\/\/
    def click(x, y):
        global theme, color_1, color_2, pale_color_1, pale_color_2, bright_color_1, bright_color_2
        #===== <green theme selection check> / <проверка на выбор зеленой темы> \/\/\/
        if x < -450*SCALE_CONSTANT and x > -550*SCALE_CONSTANT and y > 100*SCALE_CONSTANT and y < 200*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(-500*SCALE_CONSTANT, 50*SCALE_CONSTANT)
            startscreen_2.down()
            theme = "green"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <orange theme selection check> / <проверка на выбор оранжевой темы> \/\/\/
        elif x < -250*SCALE_CONSTANT and x > -350*SCALE_CONSTANT and y > 100*SCALE_CONSTANT and y < 200*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(-300*SCALE_CONSTANT, 50*SCALE_CONSTANT)
            startscreen_2.down()
            theme = "orange"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <blue theme selection check> / <проверка на выбор синей темы> \/\/\/
        elif x < -50*SCALE_CONSTANT and x > -150*SCALE_CONSTANT and y > 100*SCALE_CONSTANT and y < 200*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(-100*SCALE_CONSTANT, 50*SCALE_CONSTANT)
            startscreen_2.down()
            theme = "blue"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <violet theme selection check> / <проверка на выбор фиолетовой темы> \/\/\/
        elif x < 150*SCALE_CONSTANT and x > 50*SCALE_CONSTANT and y > 100*SCALE_CONSTANT and y < 200*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(100*SCALE_CONSTANT, 50*SCALE_CONSTANT)
            startscreen_2.down()
            theme = "violet"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <red theme selection check> / <проверка на выбор красной темы> \/\/\/
        elif x < 350*SCALE_CONSTANT and x > 250*SCALE_CONSTANT and y > 100*SCALE_CONSTANT and y < 200*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(300*SCALE_CONSTANT, 50*SCALE_CONSTANT)
            startscreen_2.down()
            theme = "red"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <white theme selection check> / <проверка на выбор белой темы> \/\/\/
        elif x < 550*SCALE_CONSTANT and x > 450*SCALE_CONSTANT and y > 100*SCALE_CONSTANT and y < 200*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(500*SCALE_CONSTANT, 50*SCALE_CONSTANT)
            startscreen_2.down()
            theme = "white"
            startscreen_2.dot(25*SCALE_CONSTANT)

        #===== <theme installation> / <установка темы> \/\/\/
        elif x < 170*SCALE_CONSTANT and x > -170*SCALE_CONSTANT and y > -250*SCALE_CONSTANT and y < -150*SCALE_CONSTANT:
            if theme == "green":
                color_1 = "#0d3b31"
                color_2 = "#145f4f"
                pale_color_1 = "#374744"
                pale_color_2 = "#4b5c59"
                bright_color_1 = "#125042"
                bright_color_2 = "#1b866f"      
            elif theme == "orange":
                color_1 = "#d68a43"
                color_2 = "#e4974f"
                pale_color_1 = "#9C7B5C"
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
            elif theme == "white":
                color_1 = "#969696"
                color_2 = "#A3A3A3"
                pale_color_1 = "#646464"
                pale_color_2 = "#6D6D6D"
                bright_color_1 = "#b4b4b4"
                bright_color_2 = "#cccccc"
            elif theme == "violet":
                color_1 = "#492f57"
                color_2 = "#523461"
                pale_color_1 = "#52415C"
                pale_color_2 = "#5B4B64"
                bright_color_1 = "#68387E"
                bright_color_2 = "#8440A7"
            if theme:
                startscreen.clear()
                startscreen_2.clear()
                start()   



    win.onclick(click, 1)

start_screen()



def start():
    global BASE_PRICE, UPPER_GRAPH_X, LOWER_GRAPH_X, max_price, min_price, dollars_for_pixel, isend_upper_graph, is_real_time_graph, navigating, start_page_time, current_time, price_matrix_index, price_matrix, price_list, blocks_edges, times_list
    #==================== <determining the starting price> / <оперделение старовой цены> \/\/\/
    while not BASE_PRICE:
        try:
            url= 'https://api.binance.com/api/v3/ticker/price'
            response = req.get(url,params={'symbol':'BTCUSDT'}, timeout=5)
            BASE_PRICE = round(float(response.json()['price']), 2)
        except req.exceptions.ConnectionError:
            print('ошибка соединения')
            BASE_PRICE = None

    print(BASE_PRICE)

    #==================== <preparing the program> / <подготовка программы> \/\/\/
    max_price = BASE_PRICE
    min_price = BASE_PRICE



    win.tracer(0)

    upper_graph.up()
    upper_graph.goto(-620*SCALE_CONSTANT, 180*SCALE_CONSTANT)
    upper_graph.down()

    t.up()
    t.goto(0,0)
    t.down()
    t.pencolor("#383838")
    t.dot(10000*SCALE_CONSTANT)
    t.pencolor("#303030")
    t.dot(1500*SCALE_CONSTANT)
    t.pencolor("#2B2B2B")
    t.dot(1200*SCALE_CONSTANT)
    t.pencolor("#272727")
    t.dot(750*SCALE_CONSTANT)
    t.pencolor("#242424")
    t.dot(300*SCALE_CONSTANT)


    price_len = len(str(int(BASE_PRICE)))*15.5*SCALE_CONSTANT + 80*SCALE_CONSTANT
    end_palet_1 = -650*SCALE_CONSTANT + len(str(int(BASE_PRICE)))*15.5*SCALE_CONSTANT + 90*SCALE_CONSTANT
    #==================== <draw interface> / <отрисовка интерфейса> \/\/\/
    #========== <first palet> / <первая табличка> \/\/\/
    #===== <price/period of time> / <цена/период времени> \/\/\/
    interface_palets.pencolor(color_1)
    interface_palets.fillcolor(color_2)
    interface_palets.up()
    interface_palets.goto(-650*SCALE_CONSTANT, 400*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(-650*SCALE_CONSTANT, 440*SCALE_CONSTANT)
    interface_palets.goto(end_palet_1, 440*SCALE_CONSTANT)
    interface_palets.goto(end_palet_1, 400*SCALE_CONSTANT)
    interface_palets.goto(-650*SCALE_CONSTANT, 400*SCALE_CONSTANT)
    interface_palets.end_fill()

    write_price.goto(-645*SCALE_CONSTANT, 402*SCALE_CONSTANT)

    interface_lines.up()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_1, 455*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_1, 390*SCALE_CONSTANT)


    #========== <second and third palets> / <вторая и третья таблички> \/\/\/
    #===== <start time - last time> / <стартовое время - последнее время> \/\/\/
    #=== <second palet> / <вторая табличка> \/\/\/
    interface_palets.up()
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_1, 400*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_1, 440*SCALE_CONSTANT)
    interface_palets.goto(110*SCALE_CONSTANT + end_palet_1, 440*SCALE_CONSTANT)
    interface_palets.goto(110*SCALE_CONSTANT + end_palet_1, 400*SCALE_CONSTANT)
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_1, 400*SCALE_CONSTANT)
    interface_palets.end_fill()

    static_text.goto(25*SCALE_CONSTANT + end_palet_1, 402*SCALE_CONSTANT)
    static_text.write(time.strftime("%H:%M", time.localtime()) ,font = ("Times New Roman" , int(25*SCALE_CONSTANT)))

    end_palet_2 = 110*SCALE_CONSTANT + end_palet_1

    interface_lines.up()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_2, 420*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.forward(10*SCALE_CONSTANT)

    #=== <third palet> / <третья табличка> \/\/\/
    interface_palets.up()
    interface_palets.goto(end_palet_2 + 30*SCALE_CONSTANT, 400*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(end_palet_2 + 30*SCALE_CONSTANT, 440*SCALE_CONSTANT)
    interface_palets.goto(end_palet_2 + 120*SCALE_CONSTANT, 440*SCALE_CONSTANT)
    interface_palets.goto(end_palet_2 + 120*SCALE_CONSTANT, 400*SCALE_CONSTANT)
    interface_palets.goto(end_palet_2 + 30*SCALE_CONSTANT, 400*SCALE_CONSTANT)
    interface_palets.end_fill()

    current_time = time.strftime("%H:%M", time.localtime())
    time_text.goto(35*SCALE_CONSTANT + end_palet_2, 402*SCALE_CONSTANT)
    time_text.write(current_time ,font = ("Times New Roman" , int(25*SCALE_CONSTANT)))

    end_palet_3 = 120*SCALE_CONSTANT + end_palet_2

    interface_lines.up()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_3, 455*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_3, 390*SCALE_CONSTANT)


    #========== <fourth palet> / <четвёртая табличка> \/\/\/
    #===== <max price> / <максимальноя цена> \/\/\/
    interface_palets.up()
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_3, 400*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(15*SCALE_CONSTANT + 16*9*SCALE_CONSTANT + end_palet_3 + price_len, 400*SCALE_CONSTANT)
    interface_palets.goto(15*SCALE_CONSTANT + 16*9*SCALE_CONSTANT + end_palet_3 + price_len, 440*SCALE_CONSTANT)
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_3, 440*SCALE_CONSTANT)
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_3, 400*SCALE_CONSTANT)
    interface_palets.end_fill()

    static_text.goto(25*SCALE_CONSTANT + end_palet_3, 405*SCALE_CONSTANT)
    static_text.write('MAX PRICE:',font = ("Times New Roman" , int(19*SCALE_CONSTANT)))

    max_price_text_line.goto(170*SCALE_CONSTANT + end_palet_3, 403*SCALE_CONSTANT)
    max_price_text_line.write(f"{BASE_PRICE}$", font = ("Times New Roman" , int(20*SCALE_CONSTANT)))

    end_palet_4 = 15*SCALE_CONSTANT + 16*9*SCALE_CONSTANT + end_palet_3 + price_len

    interface_lines.up()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_4, 455*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_4, 390*SCALE_CONSTANT)


    #========== <fifth palet> / <пятая табличка> \/\/\/
    #===== <min price> / <минимальноя цена> \/\/\/
    interface_palets.up()
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_4, 400*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(8*SCALE_CONSTANT + 16*9*SCALE_CONSTANT + end_palet_4 + price_len, 400*SCALE_CONSTANT)
    interface_palets.goto(8*SCALE_CONSTANT + 16*9*SCALE_CONSTANT + end_palet_4 + price_len, 440*SCALE_CONSTANT)
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_4, 440*SCALE_CONSTANT)
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_4, 400*SCALE_CONSTANT)
    interface_palets.end_fill()

    static_text.goto(25*SCALE_CONSTANT + end_palet_4, 405*SCALE_CONSTANT)
    static_text.write('MIN PRICE:',font = ("Times New Roman" , int(19*SCALE_CONSTANT)))

    min_price_text_line.goto(160*SCALE_CONSTANT + end_palet_4, 403*SCALE_CONSTANT)
    min_price_text_line.write(f"{BASE_PRICE}$", font = ("Times New Roman" , int(20*SCALE_CONSTANT)))

    end_palet_5 = 8*SCALE_CONSTANT + 16*9*SCALE_CONSTANT + end_palet_4 + price_len

    interface_lines.up()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_5, 455*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_5, 390*SCALE_CONSTANT)


    #========== <sixth palet> / <шестая табличка> \/\/\/
    #===== <percent from start program> / <процент с начала программы> \/\/\/
    interface_palets.up()
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_5, 400*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(265*SCALE_CONSTANT + end_palet_5, 400*SCALE_CONSTANT)
    interface_palets.goto(265*SCALE_CONSTANT + end_palet_5, 440*SCALE_CONSTANT)
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_5, 440*SCALE_CONSTANT)
    interface_palets.goto(20*SCALE_CONSTANT + end_palet_5, 400*SCALE_CONSTANT)
    interface_palets.end_fill()

    static_text.goto(25*SCALE_CONSTANT + end_palet_5, 405*SCALE_CONSTANT)
    static_text.write('FROM START:',font = ("Times New Roman" , int(17*SCALE_CONSTANT)))

    price_percent.goto(175*SCALE_CONSTANT + end_palet_5, 405*SCALE_CONSTANT)
    price_percent.write('+0.000%',font = ("Times New Roman" , int(17*SCALE_CONSTANT)))

    end_palet_6 = 265*SCALE_CONSTANT + end_palet_5

    interface_lines.up()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_6, 455*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.goto(10*SCALE_CONSTANT + end_palet_6, 390*SCALE_CONSTANT)


    #========== <price lines> / <линии цены> \/\/\/

    MASHTAB_1 = 180*SCALE_CONSTANT / BASE_PRICE
    MASHTAB_2 = -240*SCALE_CONSTANT / BASE_PRICE

    font_size = int(10*SCALE_CONSTANT)

    #===== <lines for upper graph> / <линии для верхнего графика> \/\/\/
    #=== <from the center of the upper graph down> / <от центра верхнего графика вниз> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 - i*20*SCALE_CONSTANT)
        price_lines.down()
        price_lines.goto(575*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 - i*20*SCALE_CONSTANT)
        price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 - i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
        price_line_text.write(f"{round(BASE_PRICE - i*20*dollars_for_pixel, 2)}$", font = ("Arial" , font_size, 'normal'))

    #=== <from the center of the upper graph up> / <от центра верхнего графика вверх> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 + i*20*SCALE_CONSTANT)
        price_lines.down()
        price_lines.goto(575*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 + i*20*SCALE_CONSTANT)
        price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 + i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
        price_line_text.write(f"{round(BASE_PRICE + i*20*dollars_for_pixel, 2)}$", font = ("Arial" , font_size, 'normal'))


    #===== <lines for lower graph> / <линии для нижнего графика> \/\/\/
    #=== <from the center of the lower graph down> / <от центра нижнего графика вниз> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 - i*20*SCALE_CONSTANT)
        price_lines.down()
        price_lines.goto(575*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 - i*20*SCALE_CONSTANT)
        price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 - i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
        price_line_text.write(f"{round(BASE_PRICE - i*20*dollars_for_pixel, 2)}$", font = ("Arial" , font_size, 'normal'))

    #=== <from the center of the lower graph up> / <от центра нижнего графика вверх> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 + i*20*SCALE_CONSTANT)
        price_lines.down()
        price_lines.goto(575*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 + i*20*SCALE_CONSTANT)
        price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 + i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
        price_line_text.write(f"{round(BASE_PRICE + i*20*dollars_for_pixel, 2)}$", font = ("Arial" , font_size, 'normal'))


    #========== <arrow keys to move between history pages> / <стреслки для перемещения между страницами истории> \/\/\/
    #===== <left arrow button> / <кнопка стрелка влево> \/\/\/
    #=== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
    interface_palets.pencolor("#353535")
    interface_palets.fillcolor("#3A3A3A")

    interface_palets.up()
    interface_palets.goto(-660*SCALE_CONSTANT, 210*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(-660*SCALE_CONSTANT, 150*SCALE_CONSTANT)
    interface_palets.goto(-630*SCALE_CONSTANT, 150*SCALE_CONSTANT)
    interface_palets.goto(-630*SCALE_CONSTANT, 210*SCALE_CONSTANT)
    interface_palets.goto(-660*SCALE_CONSTANT, 210*SCALE_CONSTANT)
    interface_palets.end_fill()


    #=== <arrow> / <стрелка> \/\/\/
    interface_palets.pencolor(pale_color_1)
    interface_palets.fillcolor(pale_color_2)

    interface_palets.up()
    interface_palets.goto(-655*SCALE_CONSTANT, 180*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(-635*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    interface_palets.goto(-635*SCALE_CONSTANT, 160*SCALE_CONSTANT)
    interface_palets.goto(-655*SCALE_CONSTANT, 180*SCALE_CONSTANT)
    interface_palets.end_fill()



    #===== <right arrow button> / <кнопка стрелка вправо> \/\/\/
    #=== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
    interface_palets.pencolor("#353535")
    interface_palets.fillcolor("#3A3A3A")

    interface_palets.up()
    interface_palets.goto(560*SCALE_CONSTANT, 210*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(560*SCALE_CONSTANT, 150*SCALE_CONSTANT)
    interface_palets.goto(530*SCALE_CONSTANT, 150*SCALE_CONSTANT)
    interface_palets.goto(530*SCALE_CONSTANT, 210*SCALE_CONSTANT)
    interface_palets.goto(560*SCALE_CONSTANT, 210*SCALE_CONSTANT)
    interface_palets.end_fill()


    #=== <arrow> / <стрелка> \/\/\/
    interface_palets.pencolor(pale_color_1)
    interface_palets.fillcolor(pale_color_2)

    interface_palets.up()
    interface_palets.goto(555*SCALE_CONSTANT, 180*SCALE_CONSTANT)
    interface_palets.down()
    interface_palets.begin_fill()
    interface_palets.goto(535*SCALE_CONSTANT, 200*SCALE_CONSTANT)
    interface_palets.goto(535*SCALE_CONSTANT, 160*SCALE_CONSTANT)
    interface_palets.goto(555*SCALE_CONSTANT, 180*SCALE_CONSTANT)
    interface_palets.end_fill()



    #========== <interface_lines> / <линии интерфейса> \/\/\/
    interface_lines.up()
    interface_lines.goto(560*SCALE_CONSTANT, 390*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.goto(560*SCALE_CONSTANT,-450*SCALE_CONSTANT)

    interface_lines.up()
    interface_lines.goto(-660*SCALE_CONSTANT, 390*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.goto(660*SCALE_CONSTANT, 390*SCALE_CONSTANT)

    interface_lines.up()
    interface_lines.goto(-660*SCALE_CONSTANT, -30*SCALE_CONSTANT)
    interface_lines.down()
    interface_lines.goto(660*SCALE_CONSTANT, -30*SCALE_CONSTANT)


    #========== <version display> / <отображение версии> \/\/\/
    interface_lines.up()
    interface_lines.pencolor("#000000")
    interface_lines.goto(-650*SCALE_CONSTANT, -445*SCALE_CONSTANT)
    interface_lines.write(VERSION, font = ("Times New Roman" , int(25*SCALE_CONSTANT)))


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
        max_price_text_line.write(f"{price}$", font = ("Times New Roman" , int(20*SCALE_CONSTANT)))

        y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_pixel

        max_price_text_line.up()
        max_price_text_line.goto(-660*SCALE_CONSTANT, y)
        max_price_text_line.down()
        max_price_text_line.pencolor('green')
        max_price_text_line.goto(575*SCALE_CONSTANT, y)
            
        max_price_text_line.up()
        max_price_text_line.pencolor('black')
        max_price_text_line.goto(170*SCALE_CONSTANT + end_palet_3, 403*SCALE_CONSTANT)


        if is_real_time_graph:
            last_price = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            start_y = 180*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_pixel
            prev_last = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            redraw_prices(price_list, start_y, prev_last)

        if price_matrix:
            y = -240*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_pixel

            max_price_text_line.up()
            max_price_text_line.goto(-660*SCALE_CONSTANT, y)
            max_price_text_line.down()
            max_price_text_line.pencolor('green')
            max_price_text_line.goto(575*SCALE_CONSTANT, y)
                
            max_price_text_line.up()
            max_price_text_line.pencolor('black')
            max_price_text_line.goto(170*SCALE_CONSTANT + end_palet_3, 403*SCALE_CONSTANT)


            if y < -210*SCALE_CONSTANT and y > -300*SCALE_CONSTANT:
                redraw_back_to_live_palet()

        update_interface()


    #========== <function to update the minimum price> / <функция для обновления минимальной цены> \/\/\/
    def update_min_price(price):
        min_price_text_line.clear()
        min_price_text_line.write(f"{price}$", font = ("Times New Roman" , int(20*SCALE_CONSTANT)))

        y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_pixel

        min_price_text_line.up()
        min_price_text_line.goto(-660*SCALE_CONSTANT, y)
        min_price_text_line.down()
        min_price_text_line.pencolor('red')
        min_price_text_line.goto(575*SCALE_CONSTANT, y)
            
        min_price_text_line.up()
        min_price_text_line.pencolor('black')
        min_price_text_line.goto(160*SCALE_CONSTANT + end_palet_4, 403*SCALE_CONSTANT)


        if is_real_time_graph:
            last_price = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            start_y = 180*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_pixel
            prev_last = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            redraw_prices(price_list, start_y, prev_last)

        if price_matrix:
            y = -240*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_pixel

            min_price_text_line.up()
            min_price_text_line.goto(-660*SCALE_CONSTANT, y)
            min_price_text_line.down()
            min_price_text_line.pencolor('red')
            min_price_text_line.goto(575*SCALE_CONSTANT, y)
                
            min_price_text_line.up()
            min_price_text_line.pencolor('black')
            min_price_text_line.goto(160*SCALE_CONSTANT + end_palet_4, 403*SCALE_CONSTANT)

            if y < -210*SCALE_CONSTANT and y > -300*SCALE_CONSTANT:
                redraw_back_to_live_palet()

        update_interface()


    #========== <function to update the price text> / <функция для обновления текста с ценой> \/\/\/
    def update_price(price):
        write_price.clear()

        if is_real_time_graph and price:
            write_price.write(f"{price}$", font = ("Times New Roman", int(25*SCALE_CONSTANT)))
        else:
            write_price.goto(-645*SCALE_CONSTANT, 404*SCALE_CONSTANT)
            write_price.write(f"{blocks_edges[price_matrix_index][4][0]}-{blocks_edges[price_matrix_index][4][1]}🔰", font = ("Times New Roman", int(20*SCALE_CONSTANT)))
            write_price.goto(-645*SCALE_CONSTANT, 402*SCALE_CONSTANT)



    #========== <function to update the persent text> / <функция для обновления текста с процентом> \/\/\/
    def update_percent(price):

        price_percent.clear()
        present = (price - BASE_PRICE)/BASE_PRICE*100

        if abs(present) < 0.0001:
            present = 0.0

        price_percent.write(f'{present:+.3f}%', font = ("Times New Roman", int(17*SCALE_CONSTANT)))



    #========== <function to update the time text> / <функция для обновления текста с временем> \/\/\/
    def update_time():
        time_text.clear()
        time_text.write(current_time ,font = ("Times New Roman" , int(25*SCALE_CONSTANT)))



    #========== <function to draw segment of upper graph> / <функция для отрисовки сегмента верхнего графика> \/\/\/
    def draw_upper_graph(last_price, price):
            global UPPER_GRAPH_X


            if is_real_time_graph:
                #===== <segment color definition> / <определение цвета сегмента> \/\/\/
                color = 'green' if last_price < price else '#cc0000' if last_price > price else "#000000"
                upper_graph.pencolor(color)

                #===== <y coord definition> / <определение вертикальной координаты> \/\/\/
                y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_pixel

                #===== <checking for appropriate scale> / <проверка на подходящий масштаб> \/\/\/
                if y >= 385*SCALE_CONSTANT or y <= -25*SCALE_CONSTANT:
                    return 'autoscaling'

                #===== <draw segment> / <отрисовка сегмента> \/\/\/
                UPPER_GRAPH_X += SEGMENT_WIDTH
                upper_graph.goto(UPPER_GRAPH_X, y)



    #========== <function to draw segment of lower graph> / <функция для отрисовки сегмента нижнего графика> \/\/\/
    def draw_lower_graph():
            global LOWER_GRAPH_X, blocks_edges, start_page_time


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
            y1 = -240*SCALE_CONSTANT + (first_price - BASE_PRICE)/dollars_for_pixel
            y2 = -240*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_pixel

            max_y = -240*SCALE_CONSTANT + (max_price_for_y - BASE_PRICE)/dollars_for_pixel
            min_y = -240*SCALE_CONSTANT + (min_price_for_y - BASE_PRICE)/dollars_for_pixel

            max_y_hitbox = max_y            
            min_y_hitbox = min_y

            if max_y + abs(min_y) < 20*SCALE_CONSTANT:
                additional_hitxob = (20*SCALE_CONSTANT - (max_y + abs(min_y)))/2
                max_y_hitbox += additional_hitxob            
                min_y_hitbox -= additional_hitxob

            
            #===== <time preparation> / <подготовка времени> \/\/\/
            current_time = time.strftime("%H:%M", time.localtime())
            times_list.append([start_page_time, current_time])

            #===== <adding data to the block hitbox list> / <добавление данных в список хитбоксов блоков> \/\/\/
            edges = [LOWER_GRAPH_X, LOWER_GRAPH_X + BLOCK_WIDTH, min_y_hitbox, max_y_hitbox, times_list[-1]]
            blocks_edges.append(edges)

            start_page_time = current_time

            #===== <draw block> / <отрисовка блока> \/\/\/
            lower_graph.pencolor(color)
            lower_graph.up()
            lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH/2, max_y)
            lower_graph.down()
            lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH/2, min_y)

            lower_graph.up()
            lower_graph.goto(LOWER_GRAPH_X, y1)

            lower_graph.pencolor('#000000')
            lower_graph.fillcolor(color)        

            lower_graph.begin_fill()
            lower_graph.down()   
            lower_graph.goto(LOWER_GRAPH_X, y2)
            lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH, y2)
            lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH, y1)
            lower_graph.goto(LOWER_GRAPH_X, y1)
            lower_graph.end_fill()

            LOWER_GRAPH_X += BLOCK_WIDTH

            #====== <Bugfix for the maximum and minimum price lines> / <багфикс линий максимальной и минимальной цены> \/\/\/
            if len(price_matrix) == 1:
                update_max_price(max_price)
                update_min_price(min_price)
                update_interface()



    #========== <function to redraw the page of upper graph> / <функция для перерисовки страницы верхнего графика> \/\/\/
    def redraw_prices(prices, start_y, prev_last = BASE_PRICE):
        global UPPER_GRAPH_X

        #===== <preparing> / <подготовка> \/\/\/
        UPPER_GRAPH_X = -620*SCALE_CONSTANT
        upper_graph.clear()

        upper_graph.up()
        upper_graph.goto(UPPER_GRAPH_X, start_y)
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
            y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_pixel

            UPPER_GRAPH_X += SEGMENT_WIDTH
            upper_graph.goto(UPPER_GRAPH_X, y)



    #========== <function to redraw lower graph> / <функция для перерисовки нижнего графика> \/\/\/
    def redraw_lower_graph():
        global LOWER_GRAPH_X

        #===== <preparing> / <подготовка> \/\/\/
        LOWER_GRAPH_X = -650*SCALE_CONSTANT

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
            y1 = -240*SCALE_CONSTANT + (first_price - BASE_PRICE)/dollars_for_pixel
            y2 = -240*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_pixel

            max_y = -240*SCALE_CONSTANT + (max_price_for_y - BASE_PRICE)/dollars_for_pixel
            min_y = -240*SCALE_CONSTANT + (min_price_for_y - BASE_PRICE)/dollars_for_pixel

            #=== <draw block> / <отрисовка блока> \/\/\/
            lower_graph.pencolor(color)
            lower_graph.up()
            lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH/2, max_y)
            lower_graph.down()
            lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH/2, min_y)

            lower_graph.pencolor('#000000')
            lower_graph.fillcolor(color)

            lower_graph.up()
            lower_graph.goto(LOWER_GRAPH_X, y1)

            lower_graph.begin_fill()
            lower_graph.down()        
            lower_graph.goto(LOWER_GRAPH_X, y2)
            lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH, y2)
            lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH, y1)
            lower_graph.goto(LOWER_GRAPH_X, y1)
            lower_graph.end_fill()

            LOWER_GRAPH_X += BLOCK_WIDTH


    #========== <function to redraw the live button> / <функция для перерисовки кнопки live> \/\/\/
    def redraw_back_to_live_palet():
        #===== <preparing> / <подготовка> \/\/\/
        back_to_live_palet.clear()

        #===== <draw button> / <отрисовка кнопки> \/\/\/
        if len(price_matrix) != LOWER_GRAPH_BLOCKS:
            back_to_live_palet.up()
            back_to_live_palet.goto(LOWER_GRAPH_X, -200*SCALE_CONSTANT)
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
            back_to_live_palet.goto(LOWER_GRAPH_X + 20*SCALE_CONSTANT, -200*SCALE_CONSTANT)
            back_to_live_palet.goto(LOWER_GRAPH_X + 20*SCALE_CONSTANT, -280*SCALE_CONSTANT)
            back_to_live_palet.goto(LOWER_GRAPH_X, -280*SCALE_CONSTANT)
            back_to_live_palet.goto(LOWER_GRAPH_X, -200*SCALE_CONSTANT)
            back_to_live_palet.end_fill()


            #=== <redrawing text> / <перерисовка текста> \/\/\/
            back_to_live_palet.up()
            back_to_live_palet.goto(LOWER_GRAPH_X + 5*SCALE_CONSTANT, -221*SCALE_CONSTANT)
            back_to_live_palet.write("L", font = ("Times New Roman" , int(14*SCALE_CONSTANT), "bold"))
            back_to_live_palet.goto(LOWER_GRAPH_X + 7*SCALE_CONSTANT, -241*SCALE_CONSTANT)
            back_to_live_palet.write("I", font = ("Times New Roman" , int(14*SCALE_CONSTANT), "bold"))
            back_to_live_palet.goto(LOWER_GRAPH_X + 4*SCALE_CONSTANT, -261*SCALE_CONSTANT)
            back_to_live_palet.write("V", font = ("Times New Roman" , int(14*SCALE_CONSTANT), "bold"))
            back_to_live_palet.goto(LOWER_GRAPH_X + 5*SCALE_CONSTANT, -281*SCALE_CONSTANT)
            back_to_live_palet.write("E", font = ("Times New Roman" , int(14*SCALE_CONSTANT), "bold"))



    #========== <function for changing the scale of a graph> / <функция для изменения масштаба графика> \/\/\/
    def autoscaling():
        global dollars_for_pixel, UPPER_GRAPH_X, LOWER_GRAPH_X

        #===== <checking for the need for autoscaling> / <проверка на необходимость автомасштабирования> \/\/\/
        if (upper_graph.ycor() >= 385*SCALE_CONSTANT or upper_graph.ycor() <= -25*SCALE_CONSTANT) or ((180*SCALE_CONSTANT + (price_list[-1] - BASE_PRICE)/dollars_for_pixel) >= 385*SCALE_CONSTANT or (180*SCALE_CONSTANT + (price_list[-1] - BASE_PRICE)/dollars_for_pixel) <= -30*SCALE_CONSTANT):
            #===== <preparing> / <подготовка> \/\/\/
            upper_graph.clear()
            lower_graph.clear()
            price_line_text.clear()

            UPPER_GRAPH_X = -620*SCALE_CONSTANT

            #===== <changes in scale> / <изменеия масштаба> \/\/\/
            if dollars_for_pixel == 0.05*SCALE_CONSTANT:
                dollars_for_pixel = 0.1*SCALE_CONSTANT
            elif dollars_for_pixel == 0.1*SCALE_CONSTANT:
                dollars_for_pixel = 0.15*SCALE_CONSTANT
            elif dollars_for_pixel <= 0.15*SCALE_CONSTANT:
                dollars_for_pixel = 0.25*SCALE_CONSTANT
            elif dollars_for_pixel <= 0.25*SCALE_CONSTANT:
                dollars_for_pixel = 0.35*SCALE_CONSTANT
            elif dollars_for_pixel <= 0.35*SCALE_CONSTANT:
                dollars_for_pixel = 0.5*SCALE_CONSTANT
            elif dollars_for_pixel == 0.5*SCALE_CONSTANT:
                dollars_for_pixel = 0.75*SCALE_CONSTANT
            elif dollars_for_pixel == 0.75*SCALE_CONSTANT:
                dollars_for_pixel = 1*SCALE_CONSTANT
            elif dollars_for_pixel == 1*SCALE_CONSTANT:
                dollars_for_pixel = 1.75*SCALE_CONSTANT
            elif dollars_for_pixel == 1.75*SCALE_CONSTANT:
                dollars_for_pixel = 2.5*SCALE_CONSTANT
            elif dollars_for_pixel == 2.5*SCALE_CONSTANT:
                dollars_for_pixel = 5*SCALE_CONSTANT
            else:
                dollars_for_pixel += 5*SCALE_CONSTANT



            #===== <if the program is in live mode> / <если программа в live режиме> \/\/\/
            if is_real_time_graph:
                last_price = BASE_PRICE if not price_matrix else price_matrix[-1][-1]

                upper_graph.up()
                upper_graph.goto(UPPER_GRAPH_X, 180*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_pixel)
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
                    y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_pixel

                    #== <checking for appropriate scale> / <проверка на подходящий масштаб> \/\/\/
                    if y >= 385*SCALE_CONSTANT or y <= -25*SCALE_CONSTANT:
                        autoscaling()

                    #== <draw segment> / <отрисовка сегмента> \/\/\/
                    UPPER_GRAPH_X += SEGMENT_WIDTH
                    upper_graph.goto(UPPER_GRAPH_X, y)

            #===== <if the program is in history mode> / <если программа в режиме истории> \/\/\/
            else:
                #=== <preparing> / <подготовка> \/\/\/
                first_price = price_matrix[price_matrix_index][0]

                upper_graph.up()
                upper_graph.goto(UPPER_GRAPH_X, 180*SCALE_CONSTANT + (first_price - BASE_PRICE)/dollars_for_pixel)
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
                    y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_pixel

                    #== <checking for appropriate scale> / <проверка на подходящий масштаб> \/\/\/
                    if y >= 385*SCALE_CONSTANT or y <= -25*SCALE_CONSTANT:
                        autoscaling()

                    #== <draw segment> / <отрисовка сегмента> \/\/\/
                    UPPER_GRAPH_X += SEGMENT_WIDTH
                    upper_graph.goto(UPPER_GRAPH_X, y)

            #===== <if there are blocks in the lower graph> / <если есть блоки нижнего графика> \/\/\/
            if price_matrix:
                #=== <preparing> / <подготовка> \/\/\/
                LOWER_GRAPH_X = -650*SCALE_CONSTANT
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
                    y1 = -240*SCALE_CONSTANT + (first_price - BASE_PRICE)/dollars_for_pixel
                    y2 = -240*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_pixel

                    max_y = -240*SCALE_CONSTANT + (max_price_for_y - BASE_PRICE)/dollars_for_pixel
                    min_y = -240*SCALE_CONSTANT + (min_price_for_y - BASE_PRICE)/dollars_for_pixel

                    max_y_hitbox = max_y            
                    min_y_hitbox = min_y

                    if max_y + abs(min_y) < 20*SCALE_CONSTANT:
                        additional_hitxob = (20*SCALE_CONSTANT-(max_y + abs(min_y)))/2
                        max_y_hitbox += additional_hitxob            
                        min_y_hitbox -= additional_hitxob

                    #== <adding data to the block hitbox list> / <добавление данных в список хитбоксов блоков> \/\/\/
                    edges = [LOWER_GRAPH_X, LOWER_GRAPH_X + BLOCK_WIDTH, min_y_hitbox, max_y_hitbox, times_list[i]]
                    blocks_edges.append(edges)


                    #== <draw block> / <отрисовка блока> \/\/\/
                    lower_graph.pencolor(color)
                    lower_graph.up()
                    lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH/2, max_y)
                    lower_graph.down()
                    lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH/2, min_y)

                    lower_graph.pencolor('#000000')
                    lower_graph.fillcolor(color)

                    lower_graph.up()
                    lower_graph.goto(LOWER_GRAPH_X, y1)

                    lower_graph.begin_fill()
                    lower_graph.down()        
                    lower_graph.goto(LOWER_GRAPH_X, y2)
                    lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH, y2)
                    lower_graph.goto(LOWER_GRAPH_X + BLOCK_WIDTH, y1)
                    lower_graph.goto(LOWER_GRAPH_X, y1)
                    lower_graph.end_fill()

                    LOWER_GRAPH_X += BLOCK_WIDTH

            #===== <updating the maximum and minimum prices> / <обновление максимальной и мнинимальной цены> \/\/\/
            update_max_price(max_price)
            update_min_price(min_price)
            update_interface()


            #===== <updating the prices> / <обновление цен> \/\/\/     
            for i in range(11):
                price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 - i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
                price_line_text.write(f"{round(BASE_PRICE - (i*20)*dollars_for_pixel, 2)}$", font = ("Arial" , font_size, 'normal'))


            for i in range(11):
                price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 + i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
                price_line_text.write(f"{round(BASE_PRICE + (i*20)*dollars_for_pixel, 2)}$", font = ("Arial" , font_size, 'normal'))


            for i in range(11):
                price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 - i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
                price_line_text.write(f"{round(BASE_PRICE - (i*20)*dollars_for_pixel, 2)}$", font = ("Arial" , font_size, 'normal'))


            for i in range(11):
                price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 + i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
                price_line_text.write(f"{round(BASE_PRICE + (i*20)*dollars_for_pixel, 2)}$", font = ("Arial" , font_size, 'normal'))


    #========== <function of redrawing some parts of the interface> / <функция перерисовки некоторых частей интерфейса> \/\/\/
    def update_interface():
        interface_lines.clear()

        #===== <arrow keys to move between history pages> / <стреслки для перемещения между страницами истории> \/\/\/
        #=== <left arrow button> / <кнопка стрелка влево> \/\/\/
        #== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
        interface_palets.pencolor("#353535")
        interface_palets.fillcolor("#3A3A3A")

        interface_palets.up()
        interface_palets.goto(-660*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(-660*SCALE_CONSTANT, 150*SCALE_CONSTANT)
        interface_palets.goto(-630*SCALE_CONSTANT, 150*SCALE_CONSTANT)
        interface_palets.goto(-630*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.goto(-660*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.end_fill()

        if price_matrix_index > 0:
            interface_palets.pencolor(color_1)
            interface_palets.fillcolor(color_2)
        else:
            interface_palets.pencolor(pale_color_1)
            interface_palets.fillcolor(pale_color_2)

        #== <arrow> / <стрелка> \/\/\/
        interface_palets.up()
        interface_palets.goto(-655*SCALE_CONSTANT, 180*SCALE_CONSTANT)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(-635*SCALE_CONSTANT, 200*SCALE_CONSTANT)
        interface_palets.goto(-635*SCALE_CONSTANT, 160*SCALE_CONSTANT)
        interface_palets.goto(-655*SCALE_CONSTANT, 180*SCALE_CONSTANT)
        interface_palets.end_fill()


        #=== <right arrow button> / <кнопка стрелка вправо> \/\/\/
        #== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
        interface_palets.pencolor("#353535")
        interface_palets.fillcolor("#3A3A3A")

        interface_palets.up()
        interface_palets.goto(560*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(560*SCALE_CONSTANT, 150*SCALE_CONSTANT)
        interface_palets.goto(530*SCALE_CONSTANT, 150*SCALE_CONSTANT)
        interface_palets.goto(530*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.goto(560*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.end_fill()

        can_go_right = False
        if not is_real_time_graph:
            if price_matrix_index <= len(price_matrix) - 1:
                can_go_right = True

        if price_matrix_index == LOWER_GRAPH_BLOCKS-1:
            can_go_right = False
        
        if can_go_right:
            interface_palets.pencolor(color_1)
            interface_palets.fillcolor(color_2)
        else:
            interface_palets.pencolor(pale_color_1)
            interface_palets.fillcolor(pale_color_2)

        #== <arrow> / <стрелка> \/\/\/
        interface_palets.up()
        interface_palets.goto(555*SCALE_CONSTANT, 180*SCALE_CONSTANT)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(535*SCALE_CONSTANT, 200*SCALE_CONSTANT)
        interface_palets.goto(535*SCALE_CONSTANT, 160*SCALE_CONSTANT)
        interface_palets.goto(555*SCALE_CONSTANT, 180*SCALE_CONSTANT)
        interface_palets.end_fill()


        #===== <interface_lines> / <линии интерфейса> \/\/\/
        interface_lines.up()
        interface_lines.goto(560*SCALE_CONSTANT, 390*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.goto(560*SCALE_CONSTANT,-450*SCALE_CONSTANT)

        interface_lines.up()
        interface_lines.goto(-660*SCALE_CONSTANT, 390*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.goto(660*SCALE_CONSTANT, 390*SCALE_CONSTANT)

        interface_lines.up()
        interface_lines.goto(-660*SCALE_CONSTANT, -30*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.goto(660*SCALE_CONSTANT, -30*SCALE_CONSTANT)


        interface_lines.up()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_1, 455*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_1, 390*SCALE_CONSTANT)

        interface_lines.up()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_2, 420*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.forward(10*SCALE_CONSTANT)

        interface_lines.up()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_3, 455*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_3, 390*SCALE_CONSTANT)

        interface_lines.up()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_4, 455*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_4, 390*SCALE_CONSTANT)

        interface_lines.up()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_5, 455*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_5, 390*SCALE_CONSTANT)

        interface_lines.up()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_6, 455*SCALE_CONSTANT)
        interface_lines.down()
        interface_lines.goto(10*SCALE_CONSTANT + end_palet_6, 390*SCALE_CONSTANT)


        if len(price_matrix) != LOWER_GRAPH_BLOCKS:
            redraw_back_to_live_palet()

        #========== <version display> / <отображение версии> \/\/\/
        interface_lines.up()
        interface_lines.pencolor("#000000")
        interface_lines.goto(-650*SCALE_CONSTANT, -445*SCALE_CONSTANT)
        interface_lines.write(VERSION, font = ("Times New Roman" , int(25*SCALE_CONSTANT)))


    #========== <function for reading keystrokes> / <функция для считывания нажатий> \/\/\/
    def on_click(x, y):
        global price_matrix_index, is_real_time_graph, navigating


        if navigating:
            return
        navigating = True


        try:
            #===== <click on candle> / <клик по свече> \/\/\/
            if price_matrix:
                for i in range(len(blocks_edges)):
                    #=== <hitbox hit check> / <проверка на поподание в хитбокс> \/\/\/
                    if (x > blocks_edges[i][0] and x < blocks_edges[i][1]) and (y > blocks_edges[i][2] and y < blocks_edges[i][3]):
                        if i + 1 != LOWER_GRAPH_BLOCKS:
                            is_real_time_graph = False
                        else:
                            is_real_time_graph = True

                        #=== <drawing the history page> / <отрисовка страници истории> \/\/\/
                        win.tracer(0)
                        go_to_history_page(i)
                        update_interface()
                        win.tracer(1)

                        return


            #===== <click on the arrow> / <клик по стрелке> \/\/\/
            #=== <click on the left arrow> / <клик по стрелке влево> \/\/\/
            #== <hitbox hit check> / <проверка на поподание в хитбокс> \/\/\/
            if x > -660*SCALE_CONSTANT and x < -630*SCALE_CONSTANT and y > 150*SCALE_CONSTANT and y < 210*SCALE_CONSTANT and price_matrix_index != 0:
                if is_real_time_graph:
                    if not price_matrix:
                        return
                    is_real_time_graph = False

                price_matrix_index -= 1

                #== <data preparation> / <подготовка данных> \/\/\/
                prices = price_matrix[price_matrix_index]
                start_y = 180*SCALE_CONSTANT + (prices[0] - BASE_PRICE) / dollars_for_pixel
                prev_last = price_matrix[price_matrix_index - 1][-1] if price_matrix_index > 0 else BASE_PRICE


                #== <drawing the history page> / <отрисовка страници истории> \/\/\/
                win.tracer(0)
                redraw_prices(prices=prices, start_y=start_y, prev_last=prev_last)
                redraw_lower_graph()
                update_interface()
                update_price(price_list[-1] if price_list else None)
                win.tracer(1)


            #=== <click on the right arrow> / <клик по стрелке вправо> \/\/\/
            elif x > 530*SCALE_CONSTANT and x < 560*SCALE_CONSTANT and y > 150*SCALE_CONSTANT and y < 210*SCALE_CONSTANT:
                if not is_real_time_graph:
                    #== <if the graph is not in live mode after moving> /
                    #== <Если после перемещения график не находится в live режиме> \/\/\/
                    if price_matrix_index < len(price_matrix) - 1:
                        price_matrix_index += 1

                        #= <data preparation> / <подготовка данных> \/\/\/
                        prices = price_matrix[price_matrix_index]
                        prev_last = price_matrix[price_matrix_index - 1][-1]
                        start_y = 180*SCALE_CONSTANT + (prices[0] - BASE_PRICE) / dollars_for_pixel


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
                        start_y = 180*SCALE_CONSTANT + (prev_last - BASE_PRICE) / dollars_for_pixel


                        #== <drawing the history page> / <отрисовка страници истории> \/\/\/
                        win.tracer(0)
                        redraw_prices(price_list, start_y, prev_last)
                        redraw_lower_graph()
                        update_interface()
                        update_price(price_list[-1] if price_list else None)
                        win.tracer(1)

            #===== <click on the back to live button> / <клик по конпке возврата в live> \/\/\/
            elif x > LOWER_GRAPH_X and x < LOWER_GRAPH_X + 20*SCALE_CONSTANT and y > -300*SCALE_CONSTANT and y < -210*SCALE_CONSTANT:
                if not is_real_time_graph:
                    if len(price_matrix) != LOWER_GRAPH_BLOCKS:

                        #=== <data preparation> / <подготовка данных> \/\/\/
                        prev_last = price_matrix[-1][-1]
                        start_y = 180*SCALE_CONSTANT + (prev_last - BASE_PRICE) / dollars_for_pixel
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
                    

        price_matrix_index = page

        #===== <data preparation> / <подготовка данных> \/\/\/
        prices = price_matrix[price_matrix_index]
        start_y = 180*SCALE_CONSTANT + (prices[0] - BASE_PRICE)/dollars_for_pixel
        prev_last = price_matrix[price_matrix_index - 1][-1] if price_matrix_index != 0 else BASE_PRICE

        #===== <drawing the history page> / <отрисовка страници истории> \/\/\/
        redraw_prices(prices = prices, start_y = start_y, prev_last = prev_last)
        redraw_lower_graph()


        update_price(price_list[-1] if price_list else None)


    #========== <function to check if the top graph is complete> / <функция для проверки заавершения верхнего графика> \/\/\/
    def end_upper_graph():
        global isend_upper_graph
        if len(price_list) == UPPER_GRAPH_SEGMENTS:
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
        global price_matrix, price_list, UPPER_GRAPH_X, max_price, min_price, price_matrix_index, isend_upper_graph, current_time
        try:
            win.tracer(0)

            #========== <check for completion> / <проверка на завершение> \/\/\/
            end_upper_graph()

            if isend_upper_graph == 'upper_graph_end':
                price_matrix.append(price_list.copy())

                if len(price_matrix) == LOWER_GRAPH_BLOCKS:
                    print('end')
                    draw_lower_graph()
                    update_interface()
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


                UPPER_GRAPH_X = -620*SCALE_CONSTANT

                upper_graph.up()                
                upper_graph.goto(UPPER_GRAPH_X, upper_graph.ycor())
                upper_graph.down()

                price_matrix_index += 1
                draw_lower_graph()
                redraw_back_to_live_palet()

            elif isend_upper_graph == 'upper_graph_end_in_history':
                price_matrix.append(price_list.copy())

                if len(price_matrix) == LOWER_GRAPH_BLOCKS:
                    draw_lower_graph()
                    update_interface()
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
                win.ontimer(main, 100)
                return
            else:
                price_list.append(price)    
                
                if is_real_time_graph:
                    if len(price_list) == 1:
                        is_autoscaling = draw_upper_graph(BASE_PRICE if not price_matrix else price_matrix[-1][-1], price_list[-1])
                    else:
                        is_autoscaling = draw_upper_graph(price_list[-2], price_list[-1])

                        if is_autoscaling == 'autoscaling':
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
            win.ontimer(main, TIME_INTERVAL_FOR_ONE_SEGMENT)


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

