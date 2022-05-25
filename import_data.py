import csv
import data_base

def import_csv_format1(file_name):
    import_csv = open(file_name, 'r')
    s = csv.reader(import_csv)
    temp = []
    for row in s:
        if row != []:
            temp.append(''.join(row))
        else:
            data_base.write_base(temp)
            temp = []
    import_csv.close()

def import_csv_format2(file_name):
    import_csv = open(file_name, 'r')
    s = csv.reader(import_csv)
    for row in s:
        row[3] = row[3][:-1]
        data_base.write_base(row)
    import_csv.close()