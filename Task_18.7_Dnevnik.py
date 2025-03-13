import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценки ученика по предмету
        5. Удалить предмет
        6. Изменить оценку ученика по предмету
        7. Изменить название предмета
        8. Вывести оценки для определенного ученика
        9. Вывести средний балл по каждому предмету по определенному ученику  
        10. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика по предмету: ')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        print(f'''{student} 
            Оценки по {class_}: {students_marks[student][class_]}''')
        mark = int(input('Введите оценку, которую нужно удалить: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print('Оценка удалена')
                print(f'''{student}
                {students_marks[student]}''')
        else:
            print('Оценки в списке нет')

    elif command == 5:
        print('5. Удалить предмет:')
        print(classes)
        subject = input('Введите название предмета, которое нужно удалить: ')
        if subject in classes:
            classes.remove(subject)
            print(f'Предмет {subject} удалён.')
            print(classes)
        else:
            print('Предмета в списке нет')

    elif command == 6:
        print('6. Изменить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(f'''{student} 
                    Оценки по {class_}: {students_marks[student][class_]}''')
            mark = int(input('Введите оценку, которую нужно заменить: '))
            for index in range(len(students_marks[student][class_])):
                if mark == students_marks[student][class_][index]:
                    students_marks[student][class_].pop(index)
                    break
            new_mark = int(input('Введите новую оценку: '))
            students_marks[student][class_].append(new_mark)
            print(f'Оценка заменена.')
            print(f'''{student} 
                    Оценки по {class_}: {students_marks[student][class_]}''')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 7:
        print('7. Изменить название предмет')
        print(f'Список всех предметов: {classes}')
        sub = input('Введите название предмета, который нужно заменить: ')
        if sub in classes:
            for index in range(len(classes)):
                if sub == classes[index]:
                    classes.pop(index)
                    break
            new_sub = input('Введите название нового предмета: ')
            classes.append(new_sub)
            for student in students:
                students_marks[student][new_sub] = students_marks[student][class_]

            print('Название предмета изменено.')
            print(f'Обновлённый список всех предметов: {classes}')
        else:
            print('Такого предмета в списке нет.')

    elif command == 8:
        print('8. Вывести оценки для определенного ученика')
        print(f'Список всех учеников: {students}')
        student = input('Введите имя ученика, для которого нужно вывести оценки по предметам: ')
        if student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 9:
        print('9. Вывести средний балл по определенному ученику по каждому предметам')
        print(f'Список учеников: {students}')
        student = input('Введите имя ученика: ')
        if student in students:
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
                print()

    elif command == 10:
        print('10. Выход из программы')
        break