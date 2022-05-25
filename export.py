import csv

def export_csv_format1():
    view_csv = open("data.csv", 'r')
    export_csv = open("export.csv", 'w')
    s = csv.reader(view_csv)
    for row in s:
        for i in ''.join(row).split():
            export_csv.write(i + '\n')
        export_csv.write('\n')
    export_csv.close()
    view_csv.close()

def export_csv_format2():
    view_csv = open("data.csv", 'r')
    export_csv = open("export.csv", 'w')
    s = csv.reader(view_csv)
    for row in s:
        export_csv.write(','.join(''.join(row).split()) + ';')
        export_csv.write('\n')
    export_csv.close()
    view_csv.close()
