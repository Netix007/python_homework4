import csv
from re import S

def check_base(temp):
    view_csv = open("data.csv", 'r')
    s = csv.reader(view_csv)
    for row in s:
        if [' '.join(temp)] == row:
            check_status = False
            break
    else:
        check_status = True
    view_csv.close()
    return check_status

def write_base(s):
    if check_base(s):
        s = ' '.join(s)
        data_csv = open("data.csv", 'a')
        data_csv.write(f'{s}\n')
        data_csv.close()

def view_base():
    view_csv = open("data.csv", 'r')
    s = csv.reader(view_csv)
    for row in s:
        print(*row)
    view_csv.close()
    try:
        input("\nНажмите любую клавишу...")
    except SyntaxError:
        pass
