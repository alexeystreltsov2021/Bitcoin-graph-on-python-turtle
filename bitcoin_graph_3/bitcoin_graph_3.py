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
win._root.title('ГРАФИК БИТКОИНА 3')


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
#========== <set pen size> / <установк толщины пера> \/\/\/
interface_lines.pensize(4*SCALE_CONSTANT)
interface_palets.pensize(4*SCALE_CONSTANT)
upper_graph.pensize(4*SCALE_CONSTANT)
lower_graph.pensize(2*SCALE_CONSTANT)
back_to_live_palet.pensize(2*SCALE_CONSTANT)


#========== <setting up invisibility for turtles> / <установка невидимости черепахам> \/\/\/
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

#========== <preparing the turtle logo> / <подготовка логотипа черепхи> \/\/\/
startscreen.shape("turtle")
startscreen.shapesize(15*SCALE_CONSTANT)

#========== <disable drawing> / <отключение рисования> \/\/\/
static_text.up()
time_text.up()
write_price.up()
price_percent.up()
price_lines.up()
price_line_text.up()
max_price_text_line.up()
min_price_text_line.up()


#========== <additional settings> / <дополнительные настройки> \/\/\/
startscreen_2.speed(0)
t.bgcolor("#3F3F3F")


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
dollars_for_gap_between_lines = 0.05*SCALE_CONSTANT

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

theme = "DARK"
theme_color = "green"
bg_index = 0

arrow_button_bg1 = "#353535"
arrow_button_bg2 = "#3A3A3A"

#==================== <version> / <версия> \/\/\/

VERSION = "version 3.0.7"


#==================== <start screen> / <стартовый экран> \/\/\/
def start_screen():
    global theme_color, arrow_button_bg1, arrow_button_bg2

    win.tracer(0)

    #========== <background> / <задний фон> \/\/\/
    startscreen.pencolor("#383838")
    startscreen.dot(10000*SCALE_CONSTANT)
    startscreen.pencolor("#303030")
    startscreen.dot(1500*SCALE_CONSTANT)
    startscreen.pencolor("#2B2B2B")
    startscreen.dot(1300*SCALE_CONSTANT)
    startscreen.pencolor("#272727")
    startscreen.dot(950*SCALE_CONSTANT)
    startscreen.pencolor("#242424")
    startscreen.dot(550*SCALE_CONSTANT)
    startscreen.pencolor("#222222")
    startscreen.dot(250*SCALE_CONSTANT)

    win.tracer(1)

    #========== <for a short delay> / <для небольшой задержки> \/\/\/
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
    startscreen.speed(4)

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


    #========== <last preparation of the first screen> / <последняя подготовка первого экрана> \/\/\/  
    win.tracer(0)

    #===== <version display> / <отображение версии> \/\/\/    
    startscreen.pencolor("#000000")
    startscreen.up()
    startscreen.goto(-650*SCALE_CONSTANT, -445*SCALE_CONSTANT)
    startscreen.write(VERSION, font = ("Times New Roman" , int(25*SCALE_CONSTANT)))

    #===== <logo display> / <отображение логотипа> \/\/\/ 
    startscreen.goto(0,-200*SCALE_CONSTANT)
    startscreen.left(90)
    startscreen.showturtle()

    win.tracer(1)


    #========== <delay> / <задержка> \/\/\/
    time.sleep(2)

    #========== <preparation for the second screen> / <подготовка для второго экрана> \/\/\/
    startscreen.hideturtle()


    #========== <function for drawing blocks for choosing theme colors> / <функция для отрисовки блоков для выбора цвета темы> \/\/\/
    def draw_theme_block(x1, x2, y1, y2, color_1, color_2):
        #===== <drawing a block for choosing a theme color> / <отрисовка блока для выбора цвета темы> \/\/\/
        startscreen.pencolor(color_1)
        startscreen.fillcolor(color_2)
        startscreen.pensize(6*SCALE_CONSTANT)
        startscreen.up()
        startscreen.goto(x1*SCALE_CONSTANT, y1*SCALE_CONSTANT)
        startscreen.down()
        startscreen.begin_fill()
        startscreen.goto(x2*SCALE_CONSTANT, y1*SCALE_CONSTANT)
        startscreen.goto(x2*SCALE_CONSTANT, y2*SCALE_CONSTANT)
        startscreen.goto(x1*SCALE_CONSTANT, y2*SCALE_CONSTANT)
        startscreen.goto(x1*SCALE_CONSTANT, y1*SCALE_CONSTANT)
        startscreen.end_fill()

        #===== <preparation for drawing field to indicate the selected color> / <подготовка к рисованию поля для индикации выбраного цвета> \/\/\/
        if theme == "DARK":
            startscreen.pencolor("#3d3d3d")
            startscreen.fillcolor("#4D4D4D")
        elif theme == "LIGHT":
            startscreen.pencolor("#6B6B6B")
            startscreen.fillcolor("#777777")

        #===== <drawing field to indicate the selected color> / <отрисовка поля для индикации выбраного цвета> \/\/\/
        startscreen.pensize(4*SCALE_CONSTANT)
        startscreen.up()
        startscreen.goto(x1*SCALE_CONSTANT+25*SCALE_CONSTANT, 55*SCALE_CONSTANT)
        startscreen.down()
        startscreen.begin_fill()
        startscreen.goto(x2*SCALE_CONSTANT-25*SCALE_CONSTANT, 55*SCALE_CONSTANT)
        startscreen.goto(x2*SCALE_CONSTANT-25*SCALE_CONSTANT, 5)
        startscreen.goto(x1*SCALE_CONSTANT+25*SCALE_CONSTANT, 5)
        startscreen.goto(x1*SCALE_CONSTANT+25*SCALE_CONSTANT, 55*SCALE_CONSTANT)
        startscreen.end_fill()


    #========== <function for drawing bg> / <функция для отрисовки заднего фона> \/\/\/
    def draw_bg(theme, bg_index):
        #========== <if theme is DARK> / <если тема тёмная> \/\/\/
        if theme == "DARK":
            #========== <first bg> / <первый фон> \/\/\/
            if bg_index == 0:
                startscreen.goto(0,0)
                startscreen.pencolor("#383838")
                startscreen.dot(10000*SCALE_CONSTANT)
                startscreen.pencolor("#303030")
                startscreen.dot(1500*SCALE_CONSTANT)
                startscreen.pencolor("#2B2B2B")
                startscreen.dot(1300*SCALE_CONSTANT)
                startscreen.pencolor("#272727")
                startscreen.dot(950*SCALE_CONSTANT)
                startscreen.pencolor("#242424")
                startscreen.dot(550*SCALE_CONSTANT)
                startscreen.pencolor("#222222")
                startscreen.dot(250*SCALE_CONSTANT)
            #========== <second bg> / <второй фон> \/\/\/
            elif bg_index == 1:
                startscreen.pencolor("#303030")
                startscreen.dot(10000*SCALE_CONSTANT)
                startscreen.pensize(1*SCALE_CONSTANT)                
                startscreen.pencolor("#0C0C0C")
                startscreen.fillcolor("#2C2C2C")

                for i in range(22):
                    startscreen.up()
                    startscreen.goto((-660+(i*80))*SCALE_CONSTANT, 455*SCALE_CONSTANT)
                    startscreen.down()
                    startscreen.begin_fill()
                    startscreen.goto((-580+(i*80))*SCALE_CONSTANT, 455*SCALE_CONSTANT)
                    startscreen.goto(-660*SCALE_CONSTANT, (295-(i*160))*SCALE_CONSTANT)
                    startscreen.goto(-660*SCALE_CONSTANT, (375-(i*160))*SCALE_CONSTANT)
                    startscreen.goto((-660+(i*80))*SCALE_CONSTANT, 455*SCALE_CONSTANT)
                    startscreen.end_fill()
            #========== <third bg> / <третий фон> \/\/\/
            elif bg_index == 2:
                startscreen.pencolor("#2C2C2C")
                startscreen.dot(10000*SCALE_CONSTANT)


        #========== <if theme is LIGHT> / <если тема светлая> \/\/\/
        elif theme == "LIGHT":
            #========== <first bg> / <первый фон> \/\/\/
            if bg_index == 0:
                startscreen.goto(0,0)
                startscreen.pencolor("#BBBBBB")
                startscreen.dot(10000*SCALE_CONSTANT)
                startscreen.pencolor("#B6B6B6")
                startscreen.dot(1500*SCALE_CONSTANT)
                startscreen.pencolor("#ACACAC")
                startscreen.dot(1300*SCALE_CONSTANT)
                startscreen.pencolor("#9C9C9C")
                startscreen.dot(950*SCALE_CONSTANT)
                startscreen.pencolor("#8F8F8F")
                startscreen.dot(550*SCALE_CONSTANT)
                startscreen.pencolor("#888888")
                startscreen.dot(250*SCALE_CONSTANT)
            #========== <second bg> / <второй фон> \/\/\/
            elif bg_index == 1:
                startscreen.pencolor("#B4B4B4")
                startscreen.dot(10000*SCALE_CONSTANT)
                startscreen.pensize(1*SCALE_CONSTANT)                
                startscreen.pencolor("#5A5A5A")
                startscreen.fillcolor("#A8A8A8")

                for i in range(22):
                    startscreen.up()
                    startscreen.goto((-660+(i*80))*SCALE_CONSTANT, 455*SCALE_CONSTANT)
                    startscreen.down()
                    startscreen.begin_fill()
                    startscreen.goto((-580+(i*80))*SCALE_CONSTANT, 455*SCALE_CONSTANT)
                    startscreen.goto(-660*SCALE_CONSTANT, (295-(i*160))*SCALE_CONSTANT)
                    startscreen.goto(-660*SCALE_CONSTANT, (375-(i*160))*SCALE_CONSTANT)
                    startscreen.goto((-660+(i*80))*SCALE_CONSTANT, 455*SCALE_CONSTANT)
                    startscreen.end_fill()
            #========== <third bg> / <третий фон> \/\/\/
            elif bg_index == 2:
                startscreen.pencolor("#808080")
                startscreen.dot(10000*SCALE_CONSTANT)


    #========== <function for redrawing the settings screen> / <функция для перерисовки экрана с настройками> \/\/\/
    def redraw_setting_screen(theme, bg_index):
        #===== <draw background> / <отрисовка заднего фона> \/\/\/
        draw_bg(theme, bg_index)

        #===== <choice of color depending on the chosen theme> / <выбор цвета в зависимости от выбранной темы> \/\/\/
        if theme == "DARK":
            startscreen.pencolor("#000000")
        elif theme == "LIGHT":
            startscreen.pencolor("#252525")

        #========== <version display> / <отображение версии> \/\/\/
        startscreen.up()
        startscreen.goto(-650*SCALE_CONSTANT, -445*SCALE_CONSTANT)
        startscreen.write(VERSION, font = ("Times New Roman" , int(25*SCALE_CONSTANT)))

        #========== <the inscription "Select theme:"> / <надпись "Select theme:"> \/\/\/
        startscreen.goto(-630*SCALE_CONSTANT, 320*SCALE_CONSTANT)
        startscreen.write("Select theme:", font = ("Times New Roman" , int(80*SCALE_CONSTANT)))

        #========== <the inscription "Select theme:"> / <надпись "Select theme color:"> \/\/\/
        startscreen.goto(-630*SCALE_CONSTANT, 200*SCALE_CONSTANT)
        startscreen.write("Select theme color:", font = ("Times New Roman" , int(80*SCALE_CONSTANT)))

        #========== <the inscription "Switch bg"> / <надпись "Switch bg"> \/\/\/
        startscreen.goto(-630*SCALE_CONSTANT, -155*SCALE_CONSTANT)
        startscreen.write("Switch bg:", font = ("Times New Roman" , int(80*SCALE_CONSTANT)))

        #========== <if theme is DARK> / <если тема тёмная> \/\/\/
        if theme == "DARK":
            #===== <change theme button> / <кнопка изменения темы> \/\/\/
            #===== <block> / <основа> \/\/\/
            startscreen.pencolor("#1B1B1B")
            startscreen.fillcolor("#222222")
            startscreen.pensize(4*SCALE_CONSTANT)
            startscreen.up()
            startscreen.goto(-35*SCALE_CONSTANT, 330*SCALE_CONSTANT)
            startscreen.down()
            startscreen.begin_fill()
            startscreen.goto(-35*SCALE_CONSTANT, 420*SCALE_CONSTANT)
            startscreen.goto(285*SCALE_CONSTANT, 420*SCALE_CONSTANT)
            startscreen.goto(285*SCALE_CONSTANT, 330*SCALE_CONSTANT)
            startscreen.goto(-35*SCALE_CONSTANT, 330*SCALE_CONSTANT)
            startscreen.end_fill()

            #===== <text> / <текст> \/\/\/
            startscreen.up()
            startscreen.goto(-25*SCALE_CONSTANT, 312*SCALE_CONSTANT)
            startscreen.pencolor("#0F0F0F")
            startscreen.write("DARK", font = ("Times New Roman" , int(80*SCALE_CONSTANT)))


            #===== <background change button> / <кнопка изменения заднего фона> \/\/\/
            #===== <block> / <основа> \/\/\/
            startscreen.pencolor("#1B1B1B")
            startscreen.fillcolor("#222222")
            startscreen.pensize(4*SCALE_CONSTANT)
            startscreen.up()
            startscreen.goto(-150*SCALE_CONSTANT, -150*SCALE_CONSTANT)
            startscreen.down()
            startscreen.begin_fill()
            startscreen.goto(-150*SCALE_CONSTANT, -50*SCALE_CONSTANT)
            startscreen.goto(280*SCALE_CONSTANT, -50*SCALE_CONSTANT)
            startscreen.goto(280*SCALE_CONSTANT, -150*SCALE_CONSTANT)
            startscreen.goto(-150*SCALE_CONSTANT, -150*SCALE_CONSTANT)
            startscreen.end_fill()

            #===== <text> / <текст> \/\/\/
            startscreen.up()
            startscreen.goto(-140*SCALE_CONSTANT, -160*SCALE_CONSTANT)
            startscreen.pencolor("#0F0F0F")
            startscreen.write("SWITCH", font = ("Times New Roman" , int(80*SCALE_CONSTANT)))


            #========== <start button> / <кнопка старт> \/\/\/
            #===== <block> / <основа> \/\/\/
            startscreen.pencolor("#3d3d3d")
            startscreen.fillcolor("#4D4D4D")
            startscreen.pensize(4*SCALE_CONSTANT)
            startscreen.up()
            startscreen.goto(-170*SCALE_CONSTANT, -250*SCALE_CONSTANT)
            startscreen.down()
            startscreen.begin_fill()
            startscreen.goto(170*SCALE_CONSTANT, -250*SCALE_CONSTANT)
            startscreen.goto(170*SCALE_CONSTANT, -350*SCALE_CONSTANT)
            startscreen.goto(-170*SCALE_CONSTANT, -350*SCALE_CONSTANT)
            startscreen.goto(-170*SCALE_CONSTANT, -250*SCALE_CONSTANT)
            startscreen.end_fill()

            #===== <text> / <текст> \/\/\/
            startscreen.pencolor("#000000")
            startscreen.up()
            startscreen.goto(-160*SCALE_CONSTANT, -360*SCALE_CONSTANT)
            startscreen.write("START", font = ("Times New Roman" , int(75*SCALE_CONSTANT)))


            #========== <green theme block> / <блок зеленой темы> \/\/\/
            draw_theme_block(-550, -450, 180, 80, "#0d3b31", "#145f4f")

            #========== <orange theme block> / <блок оранжевой темы> \/\/\/
            draw_theme_block(-350, -250, 180, 80, "#d68a43", "#e4974f")

            #========== <blue theme block> / <блок синей темы> \/\/\/   
            draw_theme_block(-150, -50, 180, 80, "#153a6b", "#1e416e")

            #========== <green violet block> / <блок фиолетовой темы> \/\/\/
            draw_theme_block(50, 150, 180, 80, "#492f57", "#523461")

            #========== <green red block> / <блок красной темы> \/\/\/
            draw_theme_block(250, 350, 180, 80, "#af2929", "#c53a3a")

            #========== <green white block> / <блок белой темы> \/\/\/
            draw_theme_block(450, 550, 180, 80, "#969696", "#A3A3A3")


        #========== <if theme is LIGHT> / <если тема светая> \/\/\/
        elif theme == "LIGHT":
            #===== <change theme button> / <кнопка изменения темы> \/\/\/
            #===== <block> / <основа> \/\/\/
            startscreen.pencolor("#B4B4B4")
            startscreen.fillcolor("#CCCCCC")
            startscreen.pensize(4*SCALE_CONSTANT)
            startscreen.up()
            startscreen.goto(-35*SCALE_CONSTANT, 330*SCALE_CONSTANT)
            startscreen.down()
            startscreen.begin_fill()
            startscreen.goto(-35*SCALE_CONSTANT, 420*SCALE_CONSTANT)
            startscreen.goto(300*SCALE_CONSTANT, 420*SCALE_CONSTANT)
            startscreen.goto(300*SCALE_CONSTANT, 330*SCALE_CONSTANT)
            startscreen.goto(-35*SCALE_CONSTANT, 330*SCALE_CONSTANT)
            startscreen.end_fill()

            #===== <text> / <текст> \/\/\/
            startscreen.up()
            startscreen.goto(-25*SCALE_CONSTANT, 312*SCALE_CONSTANT)
            startscreen.pencolor("#AAAAAA")
            startscreen.write("LIGHT", font = ("Times New Roman" , int(80*SCALE_CONSTANT)))


            #===== <background change button> / <кнопка изменения заднего фона> \/\/\/
            #===== <block> / <основа> \/\/\/
            startscreen.pencolor("#B4B4B4")
            startscreen.fillcolor("#CCCCCC")
            startscreen.pensize(4*SCALE_CONSTANT)
            startscreen.up()
            startscreen.goto(-150*SCALE_CONSTANT, -150*SCALE_CONSTANT)
            startscreen.down()
            startscreen.begin_fill()
            startscreen.goto(-150*SCALE_CONSTANT, -50*SCALE_CONSTANT)
            startscreen.goto(280*SCALE_CONSTANT, -50*SCALE_CONSTANT)
            startscreen.goto(280*SCALE_CONSTANT, -150*SCALE_CONSTANT)
            startscreen.goto(-150*SCALE_CONSTANT, -150*SCALE_CONSTANT)
            startscreen.end_fill()

            #===== <text> / <текст> \/\/\/
            startscreen.up()
            startscreen.goto(-140*SCALE_CONSTANT, -160*SCALE_CONSTANT)
            startscreen.pencolor("#AAAAAA")
            startscreen.write("SWITCH", font = ("Times New Roman" , int(80*SCALE_CONSTANT)))


            #========== <start button> / <кнопка старт> \/\/\/
            #===== <block> / <основа> \/\/\/
            startscreen.pencolor("#666666")
            startscreen.fillcolor("#727272")
            startscreen.pensize(4*SCALE_CONSTANT)
            startscreen.up()
            startscreen.goto(-170*SCALE_CONSTANT, -250*SCALE_CONSTANT)
            startscreen.down()
            startscreen.begin_fill()
            startscreen.goto(170*SCALE_CONSTANT, -250*SCALE_CONSTANT)
            startscreen.goto(170*SCALE_CONSTANT, -350*SCALE_CONSTANT)
            startscreen.goto(-170*SCALE_CONSTANT, -350*SCALE_CONSTANT)
            startscreen.goto(-170*SCALE_CONSTANT, -250*SCALE_CONSTANT)
            startscreen.end_fill()

            #===== <text> / <текст> \/\/\/
            startscreen.pencolor("#353535")
            startscreen.up()
            startscreen.goto(-160*SCALE_CONSTANT, -360*SCALE_CONSTANT)
            startscreen.write("START", font = ("Times New Roman" , int(75*SCALE_CONSTANT)))


            #========== <green theme block> / <блок зеленой темы> \/\/\/
            draw_theme_block(-550, -450, 180, 80, "#2F8D79", "#33a088")

            #========== <orange theme block> / <блок оранжевой темы> \/\/\/
            draw_theme_block(-350, -250, 180, 80, "#e7a567", "#f3b47a")

            #========== <blue theme block> / <блок синей темы> \/\/\/   
            draw_theme_block(-150, -50, 180, 80, "#4077c0", "#4983cf")

            #========== <green violet block> / <блок фиолетовой темы> \/\/\/
            draw_theme_block(50, 150, 180, 80, "#8a5ba3", "#9361ad")

            #========== <green red block> / <блок красной темы> \/\/\/
            draw_theme_block(250, 350, 180, 80, "#d45858", "#e06969")

            #========== <green white block> / <блок белой темы> \/\/\/
            draw_theme_block(450, 550, 180, 80, "#666666", "#727272")



        #========== <indicator dot of the selected theme> / <точка-индикатор выбранной темы> \/\/\/
        list_with_colors = ["green", "orange", "blue", "violet", "red", "white"]
        ind = list_with_colors.index(theme_color)

        if theme == "DARK":
            startscreen_2.pencolor("#3d3d3d")
        elif theme == "LIGHT":
            startscreen_2.pencolor("#696969")

        startscreen_2.clear()
        startscreen_2.up()
        startscreen_2.goto((-500 + ind*200)*SCALE_CONSTANT, 30*SCALE_CONSTANT)
        startscreen_2.down()
        startscreen_2.dot(25*SCALE_CONSTANT)


    #========== <setting default value> / <установка заначения по умолчанию> \/\/\/
    win.tracer(0)

    startscreen_2.up()
    startscreen_2.goto(-500*SCALE_CONSTANT, 150*SCALE_CONSTANT)
    startscreen_2.down()

    startscreen_2.pencolor("#3d3d3d")
    startscreen_2.dot(25*SCALE_CONSTANT)

    #========== <draw second screen> / <отрисока второго экрана> \/\/\/
    redraw_setting_screen("DARK", bg_index)

    win.tracer(1)


    #========== <click test> / <проверка нажатия> \/\/\/
    def click(x, y):
        global theme, theme_color, bg_index, color_1, color_2, pale_color_1, pale_color_2, bright_color_1, bright_color_2, arrow_button_bg1, arrow_button_bg2
        #===== <checking for a change of theme> / <проверка на смену темы> \/\/\/
        if x < 285*SCALE_CONSTANT and x > -35*SCALE_CONSTANT and y > 330*SCALE_CONSTANT and y < 420*SCALE_CONSTANT:
            startscreen.clear()
            win.tracer(0)
            if theme == "DARK":
                theme = "LIGHT"
                redraw_setting_screen(theme, bg_index)
            elif theme == "LIGHT":
                theme = "DARK"
                redraw_setting_screen(theme, bg_index)
            win.tracer(1)

        #===== <checking for background change> / <проверка на смену заднего фона> \/\/\/
        if x < 280*SCALE_CONSTANT and x > -150*SCALE_CONSTANT and y > -150*SCALE_CONSTANT and y < -50*SCALE_CONSTANT:
            if bg_index != 2:
                bg_index += 1
            else:
                bg_index = 0

            win.tracer(0)
            redraw_setting_screen(theme, bg_index)
            win.tracer(1)
        
        #===== <green theme color selection check> / <проверка на выбор зеленого цвета темы> \/\/\/
        elif x < -450*SCALE_CONSTANT and x > -550*SCALE_CONSTANT and y > 80*SCALE_CONSTANT and y < 180*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(-500*SCALE_CONSTANT, 30*SCALE_CONSTANT)
            startscreen_2.down()
            theme_color = "green"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <orange theme color selection check> / <проверка на выбор оранжевого цвета темы> \/\/\/
        elif x < -250*SCALE_CONSTANT and x > -350*SCALE_CONSTANT and y > 80*SCALE_CONSTANT and y < 180*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(-300*SCALE_CONSTANT, 30*SCALE_CONSTANT)
            startscreen_2.down()
            theme_color = "orange"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <blue theme color selection check> / <проверка на выбор синего цвета темы> \/\/\/
        elif x < -50*SCALE_CONSTANT and x > -150*SCALE_CONSTANT and y > 80*SCALE_CONSTANT and y < 180*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(-100*SCALE_CONSTANT, 30*SCALE_CONSTANT)
            startscreen_2.down()
            theme_color = "blue"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <violet theme color selection check> / <проверка на выбор фиолетового цвета темы> \/\/\/
        elif x < 150*SCALE_CONSTANT and x > 50*SCALE_CONSTANT and y > 80*SCALE_CONSTANT and y < 180*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(100*SCALE_CONSTANT, 30*SCALE_CONSTANT)
            startscreen_2.down()
            theme_color = "violet"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <red theme color selection check> / <проверка на выбор красного цвета темы> \/\/\/
        elif x < 350*SCALE_CONSTANT and x > 250*SCALE_CONSTANT and y > 80*SCALE_CONSTANT and y < 180*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(300*SCALE_CONSTANT, 30*SCALE_CONSTANT)
            startscreen_2.down()
            theme_color = "red"
            startscreen_2.dot(25*SCALE_CONSTANT)
        #===== <white theme color selection check> / <проверка на выбор белого цвета темы> \/\/\/
        elif x < 550*SCALE_CONSTANT and x > 450*SCALE_CONSTANT and y > 80*SCALE_CONSTANT and y < 180*SCALE_CONSTANT:
            startscreen_2.clear()
            startscreen_2.up()
            startscreen_2.goto(500*SCALE_CONSTANT, 30*SCALE_CONSTANT)
            startscreen_2.down()
            theme_color = "white"
            startscreen_2.dot(25*SCALE_CONSTANT)

        #===== <theme color installation> / <установка цвета темы> \/\/\/
        elif x < 170*SCALE_CONSTANT and x > -170*SCALE_CONSTANT and y > -350*SCALE_CONSTANT and y < -250*SCALE_CONSTANT:
                #=== <if theme is DARK> / <если тема тёмная> \/\/\/            
            if theme == "DARK":
                arrow_button_bg1 = "#353535"
                arrow_button_bg1 = "#3A3A3A"
                interface_lines.pencolor("#000000")
                price_lines.pencolor("#858585")
                price_line_text.pencolor("#858585")

                if theme_color == "green":
                    color_1 = "#0d3b31"
                    color_2 = "#145f4f"
                    pale_color_1 = "#374744"
                    pale_color_2 = "#4b5c59"
                    bright_color_1 = "#125042"
                    bright_color_2 = "#1b866f"      
                elif theme_color == "orange":
                    color_1 = "#d68a43"
                    color_2 = "#e4974f"
                    pale_color_1 = "#9C7B5C"
                    pale_color_2 = "#B8906B"
                    bright_color_1 = "#df8c3f"
                    bright_color_2 = "#ebac71"
                elif theme_color == "blue":
                    color_1 = "#153a6b"
                    color_2 = "#1e416e"
                    pale_color_1 = "#40608a"
                    pale_color_2 = "#50709b"
                    bright_color_1 = "#235596"
                    bright_color_2 = "#407ac7"
                elif theme_color == "violet":
                    color_1 = "#492f57"
                    color_2 = "#523461"
                    pale_color_1 = "#52415C"
                    pale_color_2 = "#5B4B64"
                    bright_color_1 = "#68387E"
                    bright_color_2 = "#8440A7"                    
                elif theme_color == "red":
                    color_1 = "#af2929"
                    color_2 = "#c53a3a"
                    pale_color_1 = "#964b4b"
                    pale_color_2 = "#a55555"
                    bright_color_1 = "#b93737"
                    bright_color_2 = "#d65252"
                elif theme_color == "white":
                    color_1 = "#969696"
                    color_2 = "#A3A3A3"
                    pale_color_1 = "#646464"
                    pale_color_2 = "#6D6D6D"
                    bright_color_1 = "#b4b4b4"
                    bright_color_2 = "#cccccc"

            #=== <if theme is LIGHT> / <если тема светая> \/\/\/
            elif theme == "LIGHT":
                arrow_button_bg1 = "#808080"
                arrow_button_bg2 = "#8A8A8A"
                interface_lines.pencolor("#303030")
                price_lines.pencolor("#222222")
                price_line_text.pencolor("#222222")

                if theme_color == "green":
                    color_1 = "#2F8D79"
                    color_2 = "#33a088"
                    pale_color_1 = "#5B8178"
                    pale_color_2 = "#658A83"
                    bright_color_1 = "#39BDA0"
                    bright_color_2 = "#57E4C5" 
                elif theme_color == "orange":
                    color_1 = "#e7a567"
                    color_2 = "#f3b47a"
                    pale_color_1 = "#BB9572"
                    pale_color_2 = "#C29D7B"
                    bright_color_1 = "#e69d58"
                    bright_color_2 = "#ebb583"
                elif theme_color == "blue":
                    color_1 = "#4077c0"
                    color_2 = "#4983cf"
                    pale_color_1 = "#5D7592"
                    pale_color_2 = "#647d9b"
                    bright_color_1 = "#5186CA"
                    bright_color_2 = "#83AFE7"
                elif theme_color == "violet":
                    color_1 = "#8a5ba3"
                    color_2 = "#9361ad"
                    pale_color_1 = "#7A6885"
                    pale_color_2 = "#857092"
                    bright_color_1 = "#A863C9"
                    bright_color_2 = "#C17BE2"                   
                elif theme_color == "red":
                    color_1 = "#d45858"
                    color_2 = "#e06969"
                    pale_color_1 = "#a76868"
                    pale_color_2 = "#b36c6c"
                    bright_color_1 = "#f86161"
                    bright_color_2 = "#f78080"
                elif theme_color == "white":
                    color_1 = "#666666"
                    color_2 = "#727272"
                    pale_color_1 = "#999999"
                    pale_color_2 = "#A5A5A5"
                    bright_color_1 = "#7E7E7E"
                    bright_color_2 = "#8D8D8D"


            startscreen.clear()
            startscreen_2.clear()
            start(draw_bg)


    win.onclick(click, 1)

start_screen()


def start(func_draw_bg):
    global BASE_PRICE, UPPER_GRAPH_X, LOWER_GRAPH_X    
    global max_price, min_price, price_matrix, price_list
    global start_page_time, current_time, times_list
    global dollars_for_gap_between_lines
    global isend_upper_graph, is_real_time_graph, navigating,price_matrix_index, blocks_edges
    #==================== <determining the starting price> / <оперделение старовой цены> \/\/\/
    while not BASE_PRICE:
        try:
            url= 'https://api.binance.com/api/v3/ticker/price'
            response = req.get(url,params={'symbol':'BTCUSDT'}, timeout=5)
            BASE_PRICE = round(float(response.json()['price']), 2)
        except req.exceptions.ConnectionError:
            print('ошибка соединения')
            BASE_PRICE = None

    #==================== <preparing the program> / <подготовка программы> \/\/\/
    max_price = BASE_PRICE
    min_price = BASE_PRICE



    win.tracer(0)

    upper_graph.up()
    upper_graph.goto(-620*SCALE_CONSTANT, 180*SCALE_CONSTANT)
    upper_graph.down()


    func_draw_bg(theme, bg_index)

    t.pencolor("#000000")
    t.fillcolor("#000000")


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
        price_line_text.write(f"{round(BASE_PRICE - i*20*dollars_for_gap_between_lines, 2)}$", font = ("Arial" , font_size, 'normal'))

    #=== <from the center of the upper graph up> / <от центра верхнего графика вверх> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 + i*20*SCALE_CONSTANT)
        price_lines.down()
        price_lines.goto(575*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 + i*20*SCALE_CONSTANT)
        price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 + i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
        price_line_text.write(f"{round(BASE_PRICE + i*20*dollars_for_gap_between_lines, 2)}$", font = ("Arial" , font_size, 'normal'))


    #===== <lines for lower graph> / <линии для нижнего графика> \/\/\/
    #=== <from the center of the lower graph down> / <от центра нижнего графика вниз> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 - i*20*SCALE_CONSTANT)
        price_lines.down()
        price_lines.goto(575*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 - i*20*SCALE_CONSTANT)
        price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 - i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
        price_line_text.write(f"{round(BASE_PRICE - i*20*dollars_for_gap_between_lines, 2)}$", font = ("Arial" , font_size, 'normal'))

    #=== <from the center of the lower graph up> / <от центра нижнего графика вверх> \/\/\/
    for i in range(11):
        price_lines.up()
        price_lines.goto(-660*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 + i*20*SCALE_CONSTANT)
        price_lines.down()
        price_lines.goto(575*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 + i*20*SCALE_CONSTANT)
        price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 + i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
        price_line_text.write(f"{round(BASE_PRICE + i*20*dollars_for_gap_between_lines, 2)}$", font = ("Arial" , font_size, 'normal'))


    #========== <arrow keys to move between history pages> / <стреслки для перемещения между страницами истории> \/\/\/
    #===== <left arrow button> / <кнопка стрелка влево> \/\/\/
    #=== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/

    interface_palets.pencolor(arrow_button_bg1)
    interface_palets.fillcolor(arrow_button_bg2)


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
    interface_palets.pencolor(arrow_button_bg1)
    interface_palets.fillcolor(arrow_button_bg2)

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

        y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_gap_between_lines

        max_price_text_line.up()
        max_price_text_line.goto(-660*SCALE_CONSTANT, y)
        max_price_text_line.down()
        max_price_text_line.pencolor("green")
        max_price_text_line.goto(575*SCALE_CONSTANT, y)
            
        max_price_text_line.up()
        max_price_text_line.pencolor('black')
        max_price_text_line.goto(170*SCALE_CONSTANT + end_palet_3, 403*SCALE_CONSTANT)


        if is_real_time_graph:
            last_price = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            start_y = 180*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_gap_between_lines
            prev_last = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            redraw_prices(price_list, start_y, prev_last)

        if price_matrix:
            y = -240*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_gap_between_lines

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

        y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_gap_between_lines

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
            start_y = 180*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_gap_between_lines
            prev_last = price_matrix[-1][-1] if price_matrix else BASE_PRICE
            redraw_prices(price_list, start_y, prev_last)

        if price_matrix:
            y = -240*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_gap_between_lines

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
                y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_gap_between_lines

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
            if len(price_matrix) != LOWER_GRAPH_BLOCKS:
                color = 'green' if first_price < last_price else "#cc0000" if first_price > last_price else "#202020"
            else:
                if is_real_time_graph:
                    color = '#00AA00' if first_price < last_price else "#ff2222" if first_price > last_price else "#353535"
                else:
                    color = 'green' if first_price < last_price else "#cc0000" if first_price > last_price else "#202020"

            #===== <coords preparation> / <подготовка координат> \/\/\/
            y1 = -240*SCALE_CONSTANT + (first_price - BASE_PRICE)/dollars_for_gap_between_lines
            y2 = -240*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_gap_between_lines

            max_y = -240*SCALE_CONSTANT + (max_price_for_y - BASE_PRICE)/dollars_for_gap_between_lines
            min_y = -240*SCALE_CONSTANT + (min_price_for_y - BASE_PRICE)/dollars_for_gap_between_lines

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
            y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_gap_between_lines

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
            y1 = -240*SCALE_CONSTANT + (first_price - BASE_PRICE)/dollars_for_gap_between_lines
            y2 = -240*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_gap_between_lines

            max_y = -240*SCALE_CONSTANT + (max_price_for_y - BASE_PRICE)/dollars_for_gap_between_lines
            min_y = -240*SCALE_CONSTANT + (min_price_for_y - BASE_PRICE)/dollars_for_gap_between_lines

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
                back_to_live_palet.pencolor(bright_color_1)
                back_to_live_palet.fillcolor(bright_color_2)   
            else:
                back_to_live_palet.pencolor(color_1)
                back_to_live_palet.fillcolor(color_2)


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
        global dollars_for_gap_between_lines, UPPER_GRAPH_X, LOWER_GRAPH_X

        #===== <checking for the need for autoscaling> / <проверка на необходимость автомасштабирования> \/\/\/
        if (upper_graph.ycor() >= 385*SCALE_CONSTANT or upper_graph.ycor() <= -25*SCALE_CONSTANT) or ((180*SCALE_CONSTANT + (price_list[-1] - BASE_PRICE)/dollars_for_gap_between_lines) >= 385*SCALE_CONSTANT or (180*SCALE_CONSTANT + (price_list[-1] - BASE_PRICE)/dollars_for_gap_between_lines) <= -30*SCALE_CONSTANT):
            #===== <preparing> / <подготовка> \/\/\/
            upper_graph.clear()
            lower_graph.clear()
            price_line_text.clear()

            UPPER_GRAPH_X = -620*SCALE_CONSTANT

            #===== <changes in scale> / <изменеия масштаба> \/\/\/
            if dollars_for_gap_between_lines == 0.05:
                dollars_for_gap_between_lines = 0.1
            elif dollars_for_gap_between_lines == 0.1:
                dollars_for_gap_between_lines = 0.15
            elif dollars_for_gap_between_lines <= 0.15:
                dollars_for_gap_between_lines = 0.25
            elif dollars_for_gap_between_lines <= 0.25:
                dollars_for_gap_between_lines = 0.35
            elif dollars_for_gap_between_lines <= 0.35:
                dollars_for_gap_between_lines = 0.5
            elif dollars_for_gap_between_lines == 0.5:
                dollars_for_gap_between_lines = 0.75
            elif dollars_for_gap_between_lines == 0.75:
                dollars_for_gap_between_lines = 1
            elif dollars_for_gap_between_lines == 1:
                dollars_for_gap_between_lines = 1.75
            elif dollars_for_gap_between_lines == 1.75:
                dollars_for_gap_between_lines = 2.5
            elif dollars_for_gap_between_lines == 2.5:
                dollars_for_gap_between_lines = 3.75
            elif dollars_for_gap_between_lines == 3.75:
                dollars_for_gap_between_lines = 5
            else:
                dollars_for_gap_between_lines += 5



            #===== <if the program is in live mode> / <если программа в live режиме> \/\/\/
            if is_real_time_graph:
                last_price = BASE_PRICE if not price_matrix else price_matrix[-1][-1]

                upper_graph.up()
                upper_graph.goto(UPPER_GRAPH_X, 180*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_gap_between_lines)
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
                    y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_gap_between_lines

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
                upper_graph.goto(UPPER_GRAPH_X, 180*SCALE_CONSTANT + (first_price - BASE_PRICE)/dollars_for_gap_between_lines)
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
                    y = 180*SCALE_CONSTANT + (price - BASE_PRICE)/dollars_for_gap_between_lines

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
                    y1 = -240*SCALE_CONSTANT + (first_price - BASE_PRICE)/dollars_for_gap_between_lines
                    y2 = -240*SCALE_CONSTANT + (last_price - BASE_PRICE)/dollars_for_gap_between_lines

                    max_y = -240*SCALE_CONSTANT + (max_price_for_y - BASE_PRICE)/dollars_for_gap_between_lines
                    min_y = -240*SCALE_CONSTANT + (min_price_for_y - BASE_PRICE)/dollars_for_gap_between_lines

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
                price_line_text.write(f"{round(BASE_PRICE - (i*20)*dollars_for_gap_between_lines, 2)}$", font = ("Arial" , font_size, 'normal'))


            for i in range(11):
                price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_1 + i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
                price_line_text.write(f"{round(BASE_PRICE + (i*20)*dollars_for_gap_between_lines, 2)}$", font = ("Arial" , font_size, 'normal'))


            for i in range(11):
                price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 - i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
                price_line_text.write(f"{round(BASE_PRICE - (i*20)*dollars_for_gap_between_lines, 2)}$", font = ("Arial" , font_size, 'normal'))


            for i in range(11):
                price_line_text.goto(580*SCALE_CONSTANT, BASE_PRICE*MASHTAB_2 + i*20*SCALE_CONSTANT - 8*SCALE_CONSTANT)
                price_line_text.write(f"{round(BASE_PRICE + (i*20)*dollars_for_gap_between_lines, 2)}$", font = ("Arial" , font_size, 'normal'))


    #========== <function of redrawing some parts of the interface> / <функция перерисовки некоторых частей интерфейса> \/\/\/
    def update_interface():
        interface_lines.clear()

        #===== <arrow keys to move between history pages> / <стреслки для перемещения между страницами истории> \/\/\/
        #=== <left arrow button> / <кнопка стрелка влево> \/\/\/
        #== <back rectangle/gb for arrow> / <задний прямоугольник/фон для стрелки> \/\/\/
        interface_palets.pencolor(arrow_button_bg1)
        interface_palets.fillcolor(arrow_button_bg2)

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
            interface_palets.pencolor(bright_color_1)
            interface_palets.fillcolor(bright_color_2)
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
        interface_palets.pencolor(arrow_button_bg1)
        interface_palets.fillcolor(arrow_button_bg2)

        interface_palets.up()
        interface_palets.goto(560*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.down()
        interface_palets.begin_fill()
        interface_palets.goto(560*SCALE_CONSTANT, 150*SCALE_CONSTANT)
        interface_palets.goto(530*SCALE_CONSTANT, 150*SCALE_CONSTANT)
        interface_palets.goto(530*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.goto(560*SCALE_CONSTANT, 210*SCALE_CONSTANT)
        interface_palets.end_fill()


        if not is_real_time_graph and price_matrix_index != LOWER_GRAPH_BLOCKS-1:
            interface_palets.pencolor(bright_color_1)
            interface_palets.fillcolor(bright_color_2)
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

        if theme == "DARK":
            interface_lines.pencolor("#000000")        
        elif theme == "LIGHT":
            interface_lines.pencolor("#303030")

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
                        is_real_time_graph = False

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
                if not price_matrix or price_matrix_index == 0:
                    return

                is_real_time_graph = False

                price_matrix_index -= 1

                #= <data preparation> / <подготовка данных> \/\/\/
                prices = price_matrix[price_matrix_index]
                start_y = 180*SCALE_CONSTANT + (prices[0] - BASE_PRICE) / dollars_for_gap_between_lines
                prev_last = price_matrix[price_matrix_index - 1][-1] if price_matrix_index > 0 else BASE_PRICE


                #= <drawing the history page> / <отрисовка страници истории> \/\/\/
                win.tracer(0)
                redraw_prices(prices=prices, start_y=start_y, prev_last=prev_last)
                redraw_lower_graph()
                update_interface()
                update_price(price_list[-1] if price_list else None)
                win.tracer(1)


            #=== <click on the right arrow> / <клик по стрелке вправо> \/\/\/
            elif x > 530*SCALE_CONSTANT and x < 560*SCALE_CONSTANT and y > 150*SCALE_CONSTANT and y < 210*SCALE_CONSTANT:
                if not is_real_time_graph and price_matrix_index != LOWER_GRAPH_BLOCKS-1:
                    #== <if the graph is not in live mode after moving> /
                    #= <Если после перемещения график не находится в live режиме> \/\/\/
                    if price_matrix_index < len(price_matrix) - 1:
                        price_matrix_index += 1

                        #= <data preparation> / <подготовка данных> \/\/\/
                        prices = price_matrix[price_matrix_index]
                        prev_last = price_matrix[price_matrix_index - 1][-1]
                        start_y = 180*SCALE_CONSTANT + (prices[0] - BASE_PRICE) / dollars_for_gap_between_lines


                        #= <drawing the history page> / <отрисовка страници истории> \/\/\/
                        win.tracer(0)
                        redraw_prices(prices=prices, start_y=start_y, prev_last=prev_last)
                        redraw_lower_graph()
                        update_interface()
                        update_price(price_list[-1] if price_list else None)
                        win.tracer(1)


                    #== <if after moving the graph goes into live mode> /
                    #= <Если после перемещения график переходит в live режим> \/\/\/
                    elif price_matrix_index == len(price_matrix) - 1 and price_list:
                        is_real_time_graph = True
                        price_matrix_index += 1

                        #= <data preparation> / <подготовка данных> \/\/\/
                        prev_last = price_matrix[-1][-1]
                        start_y = 180*SCALE_CONSTANT + (prev_last - BASE_PRICE) / dollars_for_gap_between_lines


                        #= <drawing the history page> / <отрисовка страници истории> \/\/\/
                        win.tracer(0)
                        redraw_prices(price_list, start_y, prev_last)
                        redraw_lower_graph()
                        update_interface()
                        update_price(price_list[-1] if price_list else None)
                        win.tracer(1)

            #===== <click on the back to live button> / <клик по конпке возврата в live> \/\/\/
            elif x > LOWER_GRAPH_X and x < LOWER_GRAPH_X + 20*SCALE_CONSTANT and y > -300*SCALE_CONSTANT and y < -210*SCALE_CONSTANT:
                if not is_real_time_graph and price_matrix_index != LOWER_GRAPH_BLOCKS-1:
                    if len(price_matrix) != LOWER_GRAPH_BLOCKS:

                        #=== <data preparation> / <подготовка данных> \/\/\/
                        prev_last = price_matrix[-1][-1]
                        start_y = 180*SCALE_CONSTANT + (prev_last - BASE_PRICE) / dollars_for_gap_between_lines
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
        global price_matrix_index, navigating
                    

        price_matrix_index = page

        #===== <data preparation> / <подготовка данных> \/\/\/
        prices = price_matrix[price_matrix_index]
        start_y = 180*SCALE_CONSTANT + (prices[0] - BASE_PRICE)/dollars_for_gap_between_lines
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
        global price_matrix, price_list, max_price, min_price
        global UPPER_GRAPH_X, price_matrix_index, isend_upper_graph, is_real_time_graph, current_time
        try:
            win.tracer(0)

            #========== <check for completion of the upper graph> / <проверка на завершение верхнего графика> \/\/\/
            end_upper_graph()

            #===== <if the upperp graph ends in live mode> / <если верхний график заканчивается в live режиме> \/\/\/
            if isend_upper_graph == 'upper_graph_end':
                price_matrix.append(price_list.copy())

                #=== <check for completion of the lower graph> / <проверка на завершение нижнего графика> \/\/\/
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

                    is_real_time_graph = False
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

            #===== <if the upperp graph ends in history mode> / <если верхний график заканчивается в режиме истории> \/\/\/
            elif isend_upper_graph == 'upper_graph_end_in_history':
                price_matrix.append(price_list.copy())

                #=== <check for completion of the lower graph> / <проверка на завершение нижнего графика> \/\/\/
                if len(price_matrix) == LOWER_GRAPH_BLOCKS:
                    draw_lower_graph()
                    update_interface()
                    update_max_price(max_price)
                    update_min_price(min_price)
                    price_list.clear()
                    back_to_live_palet.clear()
                    update_price(None)
                    win.update()

                    is_real_time_graph = False
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

