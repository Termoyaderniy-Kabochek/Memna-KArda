#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('Столица России?','Москва','Архангельск','Волгоград','Мурманск'))
questions_list.append(Question('Какого цвета нет на флаге России?','Зеленый','Белый','Синий','Красный'))
questions_list.append(Question('Национальная хижина якутов?','Ураса','Юрта','Иглу','Изба'))
questions_list.append(Question('Что из нижеперечисленного не имеет отношения к компьютеру?','Дверь','Крыса','Форточка','Мыло'))
questions_list.append(Question('Какая денежная единица была самой весомой в 1900 году?','Английский фунт','Немецкая марка','Американский доллар','Российский рубль'))
questions_list.append(Question('Как называлось самое крупное воинское подразделение армии Древнего Рима?','Легион','Когорта','Манипула','Центурия'))
questions_list.append(Question('Какой из этих кораблей используется сегодня как противолодочной, а также для противовоздушной обороны судов?','Фрегат','Линкор','Коргат','Авианосец'))
questions_list.append(Question('Во что впадают зимой некоторые животные?','В спячку','В бешенство','В маразм','В нирвану'))
questions_list.append(Question('Какого из этих животных не было среди Бременских музыкантов?','Козел','Кот','Петух','Осел'))
questions_list.append(Question('В каком городе был построен единственный в Советском Союзе завод кондиционеров?','Баку','Одесса','Минск','Москва'))
questions_list.append(('По улице ходила... Кто?','Большая крокодила','Зеленая кобыла','Зубастая горилла','Невеста Автандила'))


app = QApplication([])

window = QWidget()
window.setWindowTitle('Mem Card')

btn_OK = QPushButton('Ответить') #КНОПКА ОТВЕТА
lb_Question = QLabel('Сколько хромосом у человека?') #ТЕКСТ ВОПРОСА


RadioGroupBox = QGroupBox('Варианты ответов') #ГРУППА НА ЭКРАНЕ ДЛЯ ПЕРЕКЛЮЧАТЕЛЕЙ С ОТВЕТАМИ
rbtn_1 = QRadioButton('46')
rbtn_2 = QRadioButton('47')
rbtn_3 = QRadioButton('45')
rbtn_4 = QRadioButton('44')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() #ВЕРТИКАЛЬНЫЕ БУДУТ ВНУТРИ ГОРИЗОТАЛЬНОГО
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) #2 ОТВЕТА В 1 СТОЛБЕЦ
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) #2 ОТВЕТА ВО 2
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) #РАЗМЕСТИТ СТОЛБЦЫ В 1 СТРОКЕ

RadioGroupBox.setLayout(layout_ans1) #ГОТОВА ПАНЕЛЬ С ВАРИАНТАМИ ОТВЕТА

#СОЗДАЕМ ПАНЕЛЬ РЕЗУЛЬТАТА
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

#Размещ ыиджеты в окне
layout_line1 = QHBoxLayout() #ВОПРОС
layout_line2 = QHBoxLayout() #ВАРИАНТЫ ОТВЕТОВ ИЛИ РЕЗУЛЬАТ ТЕСТА
layout_line3 = QHBoxLayout() #КНОПКА ОТВЕТИТЬ

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)# БОЛЬШАЯ КНОПКА
layout_line3.addStretch(1)

# СОЗДАННЫЕ СТРОКИ РАЗМЕСТИМ ДРУГ ПОД ДРУГОМ
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) #ПРОБЕЛЫ МЕЖДУ СОДЕРЖИМЫМ

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следущий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) #сняли ограничения для сброса выбора на кнопках
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #вернули ограничения, тепеь можно выбрать только 1 кнопку
    
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
        
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\nПравильных ответов: ',window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\nПравильных ответов: ',window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

q = Question('Сколько хромосом у человека','46','47', '45', '44')
ask(q)

btn_OK.clicked.connect(click_OK) #проверяем что панель ответов показывается при нажатии на кнопку

window.cur_question = -1


window.score = 0 
window.total = 0
next_question()
window.setLayout(layout_card)
window.show()
app.exec()