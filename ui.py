def correct_input(s):
    is_error = True
    while is_error:
        input_variant = input('Ваш выбор: ')
        if input_variant in s:
            is_error = False
        else:
            print('Некорректный выбор, повторите попытку')
    return input_variant

def choice_operation():
    print('''Добро пожаловать в "Телефонный справочник 2022"
    Выберете вариант использования прогараммы:
        1 - Добавить данные с клавиатуры
        2 - Просмотр справочника
        3 - Импорт данных из файла
        4 - Экспорт данных в файл
        5 - Выход''')
    operation = correct_input(('1', '2', '3', '4', '5'))
    return operation

def choice_format():
    print('''Выберете формат данных:
        1 - На одной строке хранится одна часть записи, пустая строка - разделитель
        2 - На одной строке хранятся все записи, символ разделитель - ,''')
    data_format = correct_input(('1', '2'))
    return data_format

def input_PC():
    a = input('Введите фамилию: ')
    b = input('Введите имя: ')
    c = input('Введите телефон: ')
    d = input('Введите описание: ')
    return [a, b, c, d]

def repeat_input():
    print('Вы хотите добавить еще контакт? Да/Нет')
    return correct_input(('Да', 'Нет'))