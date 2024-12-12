class Visiting:
    def __init__(self):
        pass

    def display_visitings(self):
        print('\nКоличество пропусков студентов: ')
        for i in visitings:
            print(i, visitings[i])

    def add_visitings(self,name):
        visitings[name]+=1

class Rates:
    def __init__(self,diary_math, diary_ru_lang, diary_en_lang):
        self.diary_math=diary_math
        self.diary_ru_lang=diary_ru_lang
        self.diary_en_lang=diary_en_lang

    def display_all_rates(self):
        print('\nМатематике: ')
        for i in diary_math:
            print(i, *diary_math[i])
        print('\nРусский язык: ')
        for i in diary_ru_lang:
            print(i, *diary_ru_lang[i])
        print('\nАнглийский язык: ')
        for i in diary_en_lang:
            print(i, *diary_en_lang[i])

    def add_rate(self, rate,subject,name):
        if subject == '1':
            if name in self.diary_math:
                self.diary_math[name].append(rate)  
            else:
                print('\nТакого ученика нет.')  

        elif subject == '2':
            if name in self.diary_ru_lang:
                self.diary_ru_lang[name].append(rate)
            else:
                print('\nТакого ученика нет.')

        elif subject == '3':
            if name in self.diary_en_lang:
                self.diary_en_lang[name].append(rate)
            else:
                print('\nТакого ученика нет.')
        else:
            print("\nНеизвестный предмет.")


class Students:
    def __init__(self):
        pass

    def add_student(self, name):
        diary_math[name] = []
        diary_ru_lang[name] = []
        diary_en_lang[name] = []
        visitings[name] = 0

    def remove_student(self, name):
        diary_math.pop(name)
        diary_ru_lang.pop(name)
        diary_en_lang.pop(name)



diary_math = {
    'Прохор Тигранович': [5,2,3,4],
    'Эльнара Андреевна': [4,5,3,5]
}

diary_ru_lang = {
    'Прохор Тигранович': [2,2,3,4],
    'Эльнара Андреевна': [4,5,2,5]
}

diary_en_lang = {
    'Прохор Тигранович': [5,5,5,4],
    'Эльнара Андреевна': [4,5,5,5]
}

visitings = {
    'Прохор Тигранович': 1,
    'Эльнара Андреевна': 2
}

v = Visiting()
r = Rates(diary_math, diary_ru_lang, diary_en_lang)
s = Students()

while True:
    print('Оценки по предметам:')
    r.display_all_rates()
    choise = input('\nВыберите действие: (1)Выставить оценку (2)Показать пропуски (3)Ученики (4)Выкл: ')
    if choise == '1':
        imya = input('Введите имя и фамилию ученика: ')
        while True:
            sub = input('\nВыберите предмет: (1)Математика (2)Русский язык (3)Английский язык (4)Назад: ')
            if sub != '4':
                gr = input('Введите оценку: ')
                r.add_rate(gr,sub,imya)
                r.display_all_rates()
            else:
                break
    elif choise == '2':
        v.display_visitings()
        while True:
            choise2 = input('\nВыберите действие: (1)Выставить пропуски (2)Назад: ')
            if choise2 == '1':
                stu = input('\nВведите имя и фамилию ученика: ')
                v.add_visitings(stu)
                v.display_visitings()
            elif choise2 == '2':
                break
    elif choise == '3':
        while True:
            print()
            for i in diary_math:
                print(i)
            choise3 = input('\n(1)Зачислить ученика (2)Отчислить ученика (3)Назад: ')
            if choise3 == '1':
                stu = input('Введите имя и фамилию ученика: ')
                s.add_student(stu)
            elif choise3 == '2':
                stu = input('Введите имя и фамилию ученика: ')
                s.remove_student(stu)
            else:
                break
    else:
        break
