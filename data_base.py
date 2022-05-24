num = 0
def write_base(s):
    global num
    s = ' '.join(s)
    num += 1
    data_csv = open("data.csv", 'a')
    data_csv.write(f'{num} {s}\n')
    data_csv.close()

