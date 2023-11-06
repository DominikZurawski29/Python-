import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton
from PySide6.QtGui import QFontDatabase
import random
from PySide6.QtCore import QEventLoop, QCoreApplication
from design import Ui_MainWindow
import time
ksztalty = ["kwadrat_pole", "prostokat_pole", "trojkat_pole", "kwadrat_obwod", "prostokat_obwod", "trojkat_obwod"]
class Calculator(QMainWindow):
    qq = 0.5
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))
        self.ui.btn_clear.clicked.connect(self.handle_input)
        self.ui.btn_backspace.clicked.connect(self.clear_last_digit)
        self.current_question = None
        self.loop = None
    def add_digit(self, btn_text: str) -> None:
        entry = self.ui.le_entry.text()
        if entry == '0':
            self.ui.le_entry.setText(btn_text)
        else:
            self.ui.le_entry.setText(entry + btn_text)
    def clear_entry(self):
        self.ui.le_entry.setText('0')
    def clear_last_digit(self):
        entry = self.ui.le_entry.text()
        if entry != '0':
            self.ui.le_entry.setText(entry[:-1])
    def handle_input(self):
        global entry
        entry = self.ui.le_entry.text()
        entry = int(entry)
        self.loop.quit()
        self.ui.le_entry.setText('0')
    def choose_question_type(self):
        self.ui.lbl_temp.setText("Wybierz typ zadań (1 - Algebra, 2 - Geometria).")
        self.loop = QEventLoop(self)
        self.loop.exec()
        type = int(entry)
        if type == 1:
            self.quiz()
        elif type == 2 :
            self.geometr()
        else :
            self.choose_question_type()
    def algebra_question(self, diff):
        global problem, answer
        operator = ''
        operator1 = ''
        if diff in (1, 2, 3, 4, 5, 6, 7):
            if diff == 1:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                operator = random.choice(['+', '-'])
                if x < y and operator == '-':
                    x, y = y, x
            elif diff == 2:
                x = random.randint(1, 20)
                y = random.randint(1, 20)
                operator = random.choice(['+', '-'])
                if x < y and operator == '-':
                    x, y = y, x
            elif diff == 3:
                x = random.randint(1, 50)
                y = random.randint(1, 50)
                operator = random.choice(['+', '-', ])
                if x < y and operator == '-':
                    x, y = y, x
            elif diff == 4:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                operator = random.choice(['+', '-', '*'])
                if x < y and operator == '-':
                    x, y = y, x
            elif diff == 5:
                x = random.randint(1, 20)
                y = random.randint(1, 20)
                operator = random.choice(['+', '-', '*'])
                if x > y and operator == '-':
                    x, y = y, x
            elif diff == 6:
                x = random.randint(1, 50)
                y = random.randint(1, 50)
                operator = random.choice(['+', '-', '*'])
                if x < y :
                    x,y = y,x
            elif diff == 7:
                x = random.randint(1, 50)
                y = random.randint(1, 50)
                operator = random.choice(['+', '-', '*', '/'])
                while operator == '/' and x % y != 0:
                    x = x * y
                if x < y and operator == '-' :
                    x,y = y,x
            type_question = random.randint(0, 2)
            if type_question == 1:
                answer = eval(f"{x} {operator} {y} {operator1} ")
                problem = f" x {operator} {y} {operator1} = {answer}"
                answer = x
            elif type_question == 2:
                answer = eval(f"{x} {operator} {y} {operator1} ")
                problem = f" {x} {operator} y {operator1} = {answer}"
                answer = y
            elif type_question == 0:
                problem = f"{x} {operator} {y}"
                answer = eval(f"{x} {operator} {y}")
            self.problem = problem
            return answer
        elif diff in (8, 9, 10):
            if diff == 8:
                x = random.randint(1, 20)
                y = random.randint(1, 15)
                z = random.randint(1, 20)
                operator = random.choice(['+', '-', '*', '/'])
                operator1 = random.choice(['+', '-'])
                while operator == '/' and x % y != 0:
                    x = x * y
                if x < y and operator == '-' :
                    x,y = y,x
                if y < z and operator == '-' :
                    y,z = z,y
            elif diff == 9:
                x = random.randint(1, 40)
                y = random.randint(1, 20)
                z = random.randint(1, 20)
                operator = random.choice(['+', '-', '*', '/'])
                operator1 = random.choice(['+', '-', '*'])
                while operator == '/' and x % y != 0:
                    x = x * y
                if x < y and operator == '-' :
                    x,y = y,x
                if y < z and operator == '-' :
                    y,z = z,y
            elif diff == 10:
                x = random.randint(1, 50)
                y = random.randint(1, 50)
                z = random.randint(1, 50)
                operator = random.choice(['+', '-', '*', '/'])
                operator1 = random.choice(['+', '-', '*', '/'])
                while (operator == '/' and x % y != 0)  :
                     x = x * y
                while (operator1 == '/' and y % z != 0):
                    y = y * z
                if x < y and operator == '-' :
                    x,y = y,x
                if y < z and operator == '-' :
                    y,z = z,y
            type_question = random.randint(0, 3)
            if type_question == 1:
                answer = eval(f"{x} {operator} {y} {operator1} {z}")
                problem = f" x {operator} {y} {operator1} {z} = {answer}"
                answer = x
            elif type_question == 2:
                answer = eval(f"{x} {operator} {y} {operator1} {z}")
                problem = f" {x} {operator} y {operator1} {z} = {answer}"
                answer = y
            elif type_question == 3:
                answer = eval(f"{x} {operator} {y} {operator1} {z}")
                problem = f" {x} {operator} {y} {operator1} z = {answer}"
                answer = z
            elif type_question == 0:
                problem = f"{x} {operator} {y} {operator1} {z}"
                answer = eval(f"{x} {operator} {y} {operator1} {z}")
        else:
            print("Zły poziom trudności")
    def geometry_question(self, diff):
        global answer
        ksztalt = random.choice(ksztalty)
        maks_bok = 10 * diff
        answer = 0
        if ksztalt == "kwadrat_pole":
            a = random.randint(1, maks_bok)
            self.ui.lbl_temp.setText(f"Oblicz pole kwadratu o boku {a} cm.")
            answer = a*a
        elif ksztalt == "prostokat_pole":
            a = random.randint(1, maks_bok)
            b = random.randint(1, maks_bok)
            while a == b:
                b = random.randint(1, maks_bok)
            self.ui.lbl_temp.setText(f"Oblicz pole prostokata o bokach {a} cm i {b} cm.")
            answer = a*b
        elif ksztalt == "trojkat_pole":
            a = random.randint(1, maks_bok)
            b = random.randint(1, maks_bok)
            self.ui.lbl_temp.setText(f"Oblicz pole trójkąta o podstawie {a} cm i wysokości {b} cm.")
            answer = a*b/2
        elif ksztalt == "kwadrat_obwod":
            a = random.randint(1, maks_bok)
            b = random.randint(1, maks_bok)
            self.ui.lbl_temp.setText(f"Oblicz obwód kwadrata o boku {a} cm.")
            answer = 4*a
        elif ksztalt == "prostokat_obwod":
            a = random.randint(1, maks_bok)
            b = random.randint(1, maks_bok)
            self.ui.lbl_temp.setText(f"Oblicz obwód prostokąta o bokach {a} cm i {b} cm.")
            answer = 2*a + 2*b
        elif ksztalt == "trojkat_obwod":
            a = random.randint(1, maks_bok)
            b = random.randint(1, maks_bok)
            c = random.randint(1, maks_bok)
            self.ui.lbl_temp.setText(f"Oblicz obwód trójkąta o bokach {a} cm, {b} cm и {c} сm")
            answer = a + b + c
        return answer
    def geometr(self):
        self.ui.lbl_temp.setText("Wybierz poziom trudności 1 - 10 ")
        self.loop = QEventLoop(self)
        self.loop.exec()
        diff = int(entry)
        score = 0
        self.ui.lbl_temp.setText("Podaj ilość pytań")
        self.loop = QEventLoop(self)
        self.loop.exec()
        il = int(entry)
        for x in range(il):
            self.geometry_question(diff)
            self.loop = QEventLoop(self)
            self.loop.exec()
            user = entry

            if user == answer:
                score += 1
                self.ui.lbl_temp.setText("Prawidłowo + 1,Kontynujemy? (1) tak || (2) nie")
                self.loop = QEventLoop(self)
                self.loop.exec()
                user = entry
                if user == 2:
                    break
                if diff <= 9:
                    diff += 1
            else:
                self.ui.lbl_temp.setText(f"Niepoprawna, prawidłowa odpowiedź: {answer} , Kontynujemy? (1) tak || (2) nie")
                self.loop = QEventLoop(self)
                self.loop.exec()
                user = entry
                if user == 2:
                    break
                if diff >= 2:
                    diff -= 1
            self.ui.le_entry.setText('0')
        self.ui.lbl_temp.setText(f"Masz {score} punktów / {il}")
        time.sleep(5)
        QCoreApplication.quit()
    def quiz(self):
        self.ui.lbl_temp.setText("Wybierz poziom trudności 1 - 10 ")
        self.loop = QEventLoop(self)
        self.loop.exec()
        diff = int(entry)
        score = 0
        self.ui.lbl_temp.setText("Podaj ilość pytań")
        self.loop = QEventLoop(self)
        self.loop.exec()
        il = int(entry)

        for _ in range(il):
            self.algebra_question(diff)
            print(answer)
            self.ui.lbl_temp.setText(f"{problem}")
            self.loop = QEventLoop(self)
            self.loop.exec()
            user = int(entry)
            print(user)
            if user == answer:
                self.ui.lbl_temp.setText("Prawidłowo + 1,Kontynujemy? (1) tak || (2) nie")
                self.loop = QEventLoop(self)
                self.loop.exec()
                score += 1
                if diff <= 9:
                    diff += 1
                user = entry
                if user == 2:
                    break
            else:
                self.ui.lbl_temp.setText(f"Niepoprawna, prawidłowa odpowiedź: {answer},Kontynujemy? (1) tak || (2) nie")
                if diff >= 2:
                    diff -= 1
                self.loop = QEventLoop(self)
                self.loop.exec()
                user = entry
                if user == 2:
                    break
            self.ui.le_entry.setText('0')
        self.ui.lbl_temp.setText(f"Masz {score} punktów / {il}")
        time.sleep(5)
        QCoreApplication.quit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    window.choose_question_type()
    sys.exit(app.exec())