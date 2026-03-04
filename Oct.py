import math  #Импорт нужных библиотек
import matplotlib.pyplot as plt  #Импорт нужных библиотек
import matplotlib.patches as mpatches #Импорт нужных библиотек


class Octagon:  #Задаем класс
    def __init__(self, side):  #Конструктор
        self.side = side
        self.engle = 135
        self.k = 1 + math.sqrt(2)

    def opis_okr(self): #Метод 1
        R_1 = self.side / (math.sqrt(self.k / (self.k - 1)))
        S_1 = math.pi * R_1 ** 2
        print(f"Радиус описанной окружности: {R_1}")
        print(f"Площадь описанной окружности: {S_1}")

    def vpis_okr(self): #Метод 2
        R_2 = self.k * self.side / 2
        S_2 = math.pi * R_2 ** 2
        print(f"Радиус вписанной окружности: {R_2}")
        print(f"Площадь вписанной окружности: {S_2}")

    def oct(self): #Метод 3
        P_3 = 8 * self.side
        S_3 = 2 * self.k * self.side ** 2
        print(f"Периметр октагона: {P_3}")
        print(f"Плоащдь октагона: {S_3}")

    def koord(self): #Метод 4
        R_1 = self.side * (math.sqrt(self.k / (self.k - 1)))
        R_2 = self.k * self.side / 2

        ax = plt.gca() #Создаем координатную плоскость
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_position('zero') #https://stackoverflow.com/questions/13430231/how-i-can-get-cartesian-coordinate-system-in-matplotlib
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')

        axes = plt.subplot()
        a = plt.Circle((0 , 0), R_1, color = "red", fill = False, ) #Создаем описанную окружность
        b = plt.Circle((0 , 0), R_2, color = "green", fill = False, )  #Создаем вписанную окружность
        shapes = [mpatches.RegularPolygon((0, 0), 8, radius = R_1, fill = False, color = "blue")]  #Создаем многоугольник (октагон)
        for shape in shapes:
            axes.add_artist(shape)
        plt.xlim([-1.5*self.side, 1.5 * self.side]) #
        plt.ylim([-1.5*self.side, 1.5 * self.side])
        axes.set_aspect(1)
        axes.add_artist(a)  #Добавление окружности на график
        axes.add_artist(b)  #Добавление окружности на график
        
        plt.show()  #Выводим график

    def __del__(self):  #Деструктор
        print("deleted")

