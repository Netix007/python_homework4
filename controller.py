import ui, import_data
import data_base
import os
import export


def button_click():
    end = False
    while not end:
        os.system('CLS')
        choice = ui.choice_operation()
        if choice == '1':
            is_end = False
            while not is_end:
                data_base.write_base(ui.input_PC())
                if ui.repeat_input() == 'Нет':
                    is_end = True
        elif choice == '2':
            os.system('CLS')
            data_base.view_base()
        elif choice == '3':
            os.system('CLS')
            if ui.choice_format() == '1':
                import_data.import_csv_format1('import.csv')
            else:
                import_data.import_csv_format2('import.csv')
        elif choice == '4':
            os.system('CLS')
            if ui.choice_format() == '1':
                export.export_csv_format1()
            else:
                export.export_csv_format2()
        elif choice == '5':
            end = True