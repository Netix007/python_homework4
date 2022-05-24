import ui
import data_base

def button_click():
    if ui.choice_operation() == '1':
        is_end = False
        while not is_end:
            data_base.write_base(ui.input_PC())
            if ui.repeat_input() == 'Нет':
                is_end = True