from PyQt5.QtWidgets import QApplication, QMainWindow
import page_replacement as PR
import sys


class UserWindow(QMainWindow):
    # noinspection PyArgumentList
    def __init__(self):
        super().__init__()
        self.ui = PR.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit_result.setEnabled(True)
        self.ui.lineEdit_string.setPlaceholderText("1,3,0,3,5,6 or 130356 or 1, 3, 0, 3, 5, 6")
        self.ui.lineEdit_string.setFocus(True)
        self.ui.pushButton_check.setDisabled(True)  # disable two buttons at the startup

        self.ui.lineEdit_string.textEdited.connect(self.validation)
        self.ui.lineEdit_frame.textEdited.connect(self.validation)

        self.ui.pushButton_check.clicked.connect(self.call_module)
        self.ui.pushButton_reset.clicked.connect(self.reset_all)

        self.value = 0
        self.ui.actionFIFO.triggered.connect(lambda: self.set_value("0"))
        self.ui.actionLRU.triggered.connect(lambda: self.set_value("1"))
        self.ui.actionOptimal_Page_Replacement.triggered.connect(lambda: self.set_value("2"))

    def set_value(self, value):
        self.heading = ""
        self.value = int(value)
        if int(value) == 0:
            heading_text = "YOU ARE CALCULATING USING FIFO TECHNIQUE"
        elif int(value) == 1:
            heading_text = "YOU ARE CALCULATING USING LRU TECHNIQUE"
        else:
            heading_text = "YOU ARE CALCULATING USING OPTIMAL PAGE REPLACEMENT TECHNIQUE"

        self.heading = heading_text
        self.ui.label_heading.setText(self.heading)

    def reset_all(self):
        self.ui.pushButton_check.setDisabled(True)
        self.ui.lineEdit_frame.setText("")
        self.ui.lineEdit_string.setText("")

        self.ui.label_heading.setText("YOU ARE CALCULATING USING FIFO TECHNIQUE")

    def validation(self):
        self.frame_length = self.ui.lineEdit_frame.text()
        self.input_string = self.ui.lineEdit_string.text()
        proceed_flag = 0
        if len(self.frame_length) > 0 and len(self.input_string) > 0:
            if self.frame_length.isdigit():
                if int(self.frame_length) > 0:
                    self.ui.pushButton_check.setEnabled(True)
                    proceed_flag = 1
                else:
                    self.ui.pushButton_check.setDisabled(True)
            else:
                self.ui.pushButton_check.setDisabled(True)
        else:
            self.ui.pushButton_check.setDisabled(True)

        # show the text to confirm:
        display_text = f"Input String:{self.input_string}\nFrame Length:{self.frame_length}\nlength of Input String:{len(self.input_string)}"
        self.ui.textEdit_result.setText(display_text)
        return proceed_flag

    def call_module(self):
        response = self.validation()
        self.ui.textEdit_result.setText("")
        display_text = ""
        # call different modules here
        if response == 1:  # 1 means--> validation is successful, otherwise not
            string_list, frame_length = self.input_modification(self.input_string, self.frame_length)

            if self.value == 0:
                # call fifo module
                import FIFO_method_hit_miss_count as fifo
                display_text = fifo.solve(string_list, frame_length)
            elif self.value == 1:
                # call LRU module
                import LRU_miss_hit_count as lru
                display_text = lru.solve(string_list, frame_length)
            else:
                # call optimal page replacement
                import optimal_page_replacement_hit_miss_count as optim
                display_text = optim.solve(string_list, frame_length)
            self.ui.textEdit_result.setText(display_text)

    def input_modification(self, string, frame_length):  # create an acceptable string list
        if ',' in string:
            string_list = string.replace(' ', '').split(',')
        else:
            string_list = [i for i in string]
        frame_length = int(frame_length)
        return string_list, frame_length


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UserWindow()
    w.show()
    sys.exit(app.exec_())
