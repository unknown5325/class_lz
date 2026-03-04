from Oct import Octagon  #Импорт нашего класса

n = int(input("Длина стороны октагона: "))  #Выбор длины стороны октагона
octag = Octagon(n)
ch = int(input("Выбрать задание (1-4): "))

def main():
    match ch:
        case 1:
            octag.opis_okr() #Метод 1
        case 2:
            octag.vpis_okr()  #Метод 2
        case 3:
            octag.oct()  #Метод 3
        case 4:
            octag.koord()  #Метод 4
        case _:
            print("Больше заданий нет")


if __name__ == "__main__":
    main()