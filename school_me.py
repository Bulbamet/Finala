class Attendance:
    def __init__(self):
        pass

    def display_Attendance(self):
        print('\nКоличество пропусков студентов: ')
        for i in visitings:
            print(i, visitings[i])

    def add_Attendance_rep(self,name):
        visitings[name][0]+=1

    def add_Attendance_no_rep(self,name):
        visitings[name][1]+=1

class progress:
    def __init__(self,diary_math, diary_ru_lang, diary_istor):
        self.diary_math=diary_math
        self.diary_ru_lang=diary_ru_lang
        self.diary_istor=diary_istor

    def display_all_progress(self):
        print('\nМатематике: ')
        for i in diary_math:
            print(i, *diary_math[i])
        print('\nРусский язык: ')
        for i in diary_ru_lang:
            print(i, *diary_ru_lang[i])
        print('\n История: ')
        for i in diary_istor:
            print(i, *diary_istor[i])

    def add_progress(self, rate,subject,name):
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
            if name in self.diary_istor:
                self.diary_istor[name].append(rate)
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
        diary_istor[name] = []
        visitings[name] = 0

    def remove_student(self, name):
        diary_math.pop(name)
        diary_ru_lang.pop(name)
        diary_istor.pop(name)



diary_math = {
    'Роман Михалых': [5,2,3,4],
    'Николай Евтушенков': [4,5,3,5]
}

diary_ru_lang = {
    'Роман Михалых': [2,2,3,4],
   'Николай Евтушенков': [4,5,2,5]
}

diary_istor = {
    'Роман Михалых': [5,5,5,4],
   'Николай Евтушенков': [4,5,5,5]
}

visitings = {
    'Роман Михалых': [1,1],
    'Николай Евтушенков': [2,2]
}

a = Attendance()
p = progress(diary_math, diary_ru_lang, diary_istor)
s = Students()

while True:
    print('Оценки по предметам:')
    p.display_all_progress()
    print('-----------------------------')
    choise = input('\nВыберите действие: (1)Выставить оценку (2)Показать пропуски (3)Ученики (4)Выкл: ')
    if choise == '1':
        imya = input('Введите имя и фамилию ученика: ')
        while True:
            sub = input('\nВыберите предмет: (1)Математика (2)Русский язык (3)Английский язык (4)Назад: ')
            if sub != '4':
                gr = input('Введите оценку: ')
                p.add_progress(gr,sub,imya)
                p.display_all_progress()
                print('-----------------------------')
            else:
                break
    elif choise == '2':
        a.display_Attendance()
        print('-----------------------------')
        while True:
            choise2 = input('\nВыберите действие: (1)Выставить пропуски (2)Назад: ')
            if choise2 == '1':
                choise4 = input('\nВыберите действие: (1)По уважительной  (2)По не уважительной (3)Назад: ')
                if choise4 == '1':
                    stu = input('Введите имя и фамилию ученика: ')
                    a.add_Attendance_rep(stu)
                    a.display_Attendance()
                    print('-----------------------------')
                elif choise4 == '2':
                    stu = input('Введите имя и фамилию ученика: ')    
                    a.add_Attendance_no_rep(stu)
                    a.display_Attendance()
                    print('-----------------------------')
                elif choise4 == '3':
                    break
            elif choise2 == '2':
                break
    elif choise == '3':
        while True:
            print()
            for i in diary_math:
                print(i)
            print('-----------------------------')
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
