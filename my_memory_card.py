
#подключение модулей
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QGroupBox, QButtonGroup, QRadioButton, 
    QPushButton, QLabel)
from random import shuffle

#класс вопрос
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
    #задать строки при созднии объекта , они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Год основания Соединенных Штатов Америки', '1776', '1785', '1699', '1750'))
questions_list.append(Question('Сколько лет Тому и Джерри', '77', '63', '84', '55'))
questions_list.append(Question('Год выпуска начальной версии майнкрафта', '2009', '2011', '2008', '2015'))
questions_list.append(Question('Первый язык программирования высокого уровня', 'FORTRAN', 'Java', 'Python', 'C++'))
questions_list.append(Question('Самое высокое здание в мире', 'Бурдж-Халифа', 'Шанхайская башня', 'Башня Lotte World', 'Королевская часовая башня'))
questions_list.append(Question('Где был создан телефон', 'США', 'Германия', 'Швеция', 'Казахстан'))
questions_list.append(Question('Кто открыл Америку', 'Христофор Колумб', 'Джордж Вашингтон', 'Джордж Флойд', 'Обэмэ'))
questions_list.append(Question('Чайка летела через лес кидаясь яблоками в крабов, сколько абрикосов съел Дима, если ежик ехал в Казахстан', 'феррари', '50', 'Лос-Анджелес', '10'))
questions_list.append(Question('Почему?', 'А', 'Ну ладно', 'ок', 'ничего'))
questions_list.append(Question('Как чихнул Пушкин в ???? году?', 'да', 'сильно', 'Пушкин не чихал', 'Казахстан'))
questions_list.append(Question('Кто создал Кириллицу?', 'Кирилл и Мефодий', 'Князь Владимир', 'Ленин', 'Илья Муромец'))
questions_list.append(Question('Самое популярное видео на youtube', 'Baby Shark Dance', 'Despacito', 'Let Her Go', 'Girls Like You'))
questions_list.append(Question('Самый популярный канал на youtube', 'T-Series', 'PewDiePie', 'SET India', 'Cocomelon - Nursery Rhymes'))
questions_list.append(Question('самое популярное видео на youtube', 'Baby Shark Dance', 'Despacito', 'Let Her Go', 'Girls Like You'))
questions_list.append(Question('Сколько лет Тому и Джерри', '77', '63', '84', '55'))

#создание приложения
app = QApplication([])

#создание окна
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 200)

#панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

#группа ответов
RadioGroupBox = QGroupBox('Варианты ответов')
#варианты ответов
rbtn_1=QRadioButton('Вариант 1')
rbtn_2=QRadioButton('Вариант 2')
rbtn_3=QRadioButton('Вариант 3')
rbtn_4=QRadioButton('Вариант 4')

#Группа кнопок
RadioGroup = QButtonGroup()
#кнопки
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
#расположение виджетов
layout_ans1=QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) #два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) #два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

#панель результата
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?') #надпись првильно или нет
lb_Correct = QLabel('ответ будет тут!') #будет написан текст правильного ответа

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

#размещаем виджеты в окне
layout_line1 = QHBoxLayout() #вопрос
layout_line2 = QHBoxLayout() #варианты ответов или результат теста
layout_line3 = QHBoxLayout() #кнопка ответить

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

#размещаем в одной строке обе панели, одна из них скрывается, другая показывается
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() #эту панель мы уже видели, скроем, посмотрим, как получилась панел с ответом

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) #кнопка должна быть большой (растягиваем)
layout_line3.addStretch(1)

#Созданные строки разместим друг под другой
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) #пробелы между содержимым

#показать панель ответов
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
#показать панель вопросов
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    #сюросить выбранную радиокнопку
    RadioGroup.setExclusive(False)#отключить все ограничения
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)#вернуть ограничения

#список ответов
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

#функция записывает значения вопроса и ответов в соответствующие виджеты,
#при этом варианты ответов распределяются случайным образом
def ask(q: Question):
    shuffle(answers)#перемешать список кнопок
    answers[0].setText(q.right_answer)#в первый элемент списка поместим правильный ответ, остальные неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)#вопрос
    lb_Correct.setText(q.right_answer)#ответ
    show_question() #показываем панель вопросов
#показать результат - установим переданный текст в надпись результат
#и покажем нужную панель
def show_correct(res):
    lb_Result.setText(res)
    show_result()

#если выбран вариант ответа, проверить и показать панель ответов
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
            show_correct('Неверно!')

#следующий вопрос
def next_question():
    #нужна переменная, в которой указывается номер текущего вопроса
    #ее можно сделать глобальной, или свойством глобального объекта (app или window)
    #далее заводится свойство window.cur_question
    main_win.cur_question = main_win.cur_question + 1 #переход к следующему вопросу
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0 #если список закончился, идем сначала
    q = questions_list[main_win.cur_question]#взяли вопрос
    ask(q) #спросили

#определяет надо ли показывать другой вопрос либо проверить ответ на этот
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer() #проверка ответа
    else:
        next_question() #следующий вопрос

#отображение окна
main_win.setLayout(layout_card)

#текущий вопрос из списка делаем свойством объекта окно, также мы можем спокойно менять его из функции:
main_win.cur_question = -1

btn_OK.clicked.connect(click_OK) #при нажатии на кнопку выбираем, чт конкретно происходит

#осталось задать вопрос и показать окно
next_question()
main_win.resize(400,300)
main_win.show()
app.exec_()