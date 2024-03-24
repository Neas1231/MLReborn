import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QCheckBox,
    QMessageBox,
)
from pathlib import Path
import pickle


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # window settings
        self.setWindowTitle("Check_box")
        self.setWindowIcon(QtGui.QIcon(r'overall_decision_icon_149904.png'))
        # self.setGeometry(100, 100, 400, 100)
        self.setMaximumSize(400, 0)

        # layout setting
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # dir text
        self.filename_edit = QLineEdit()
        self.filename_edit.returnPressed.connect(self.construct_box)

        # dir selection
        direct_browse = QPushButton('Browse')
        direct_browse.clicked.connect(self.open_dir_dialog)

        # confirmation
        check_boxes_construct = QPushButton('OK')
        check_boxes_construct.clicked.connect(self.construct_box)

        # saving
        check_boxes_save = QPushButton('SAVE')
        check_boxes_save.clicked.connect(self.save_result)

        # widget setup
        self.layout.addWidget(QLabel('File:'), 1, 0)
        self.layout.addWidget(self.filename_edit, 1, 1, 1, 2)
        self.layout.addWidget(direct_browse, 1, 3, 1, 5)
        self.layout.addWidget(check_boxes_construct, 2, 3, 1, 5)
        self.layout.addWidget(check_boxes_save, 2, 0)

        self.show()

        # dict for {file : button}
        self.filenames_buttons_dict = {}

    def construct_box(self):
        try:
            from os import listdir
            from os.path import exists
            from math import ceil
            self.catalogue = self.filename_edit.text()[self.filename_edit.text().rfind('\\') + 1:]
            self.content = {f for f in listdir(self.filename_edit.text())}

            if exists(f'{self.catalogue}.pickle'):
                with open(f'{self.catalogue}.pickle', 'rb') as file:
                    saved_conf = pickle.load(file)
                for file in self.content:
                    if file not in self.filenames_buttons_dict:
                        cbutton = QCheckBox(f"{file}")
                        self.filenames_buttons_dict[file] = cbutton
                        if file in saved_conf:
                            self.filenames_buttons_dict[file].setCheckState(saved_conf[file])
                        self.layout.addWidget(self.filenames_buttons_dict[file])
                    else:
                        pass

            else:
                for file in self.content:
                    if file not in self.filenames_buttons_dict:
                        cbutton = QCheckBox(f"{file}")
                        self.filenames_buttons_dict[file] = cbutton
                        self.layout.addWidget(self.filenames_buttons_dict[file])
                    else:
                        pass
            remove_btn = QPushButton('Remove')
            remove_btn.clicked.connect(self.delete_checkboxes)
            self.layout.addWidget(remove_btn, 2, 3, 1, 5)
            self.setLayout(self.layout)
        except:
            pass

    def delete_checkboxes(self):
        widgets_count = self.layout.count() - 1
        while widgets_count > 4:
            self.layout.takeAt(widgets_count).widget().deleteLater()
            widgets_count -= 1
        self.filenames_buttons_dict = {}

    def open_dir_dialog(self):
        direct = str(QFileDialog.getExistingDirectory(self, "Select Directory", "Select directory"))
        if direct:
            path = Path(direct)
            self.filename_edit.setText(str(path))

    def save_result(self):
        try:
            save_dict = {}
            for file in self.content:
                save_dict[file] = self.filenames_buttons_dict[file].checkState()
            with open(f'{self.catalogue}.pickle', "wb") as file:
                pickle.dump(save_dict, file)
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Error with saving checkboxes")
            dlg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

# %%
