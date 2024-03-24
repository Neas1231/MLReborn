from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import sip
from PyQt6.QtCore import Qt
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
    QVBoxLayout,
    QScrollArea
)

import sys
from pathlib import Path
import pickle


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # window settings
        self.setWindowTitle("Check_box")
        self.setWindowIcon(QtGui.QIcon(r'overall_decision_icon_149904.png'))

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        # layout setting
        self.layout = QGridLayout()

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

        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.mainLayout.addLayout(self.layout)

        self.show()

        # dict for {file : button}
        self.filenames_buttons_dict = {}

    def construct_box(self):
        try:
            from os import listdir
            from os.path import exists
            from math import ceil
            scroll = QScrollArea()
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            scroll.setWidgetResizable(True)
            widget = QWidget()
            self.checkbox_layout = QVBoxLayout()
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
                        self.checkbox_layout.addWidget(self.filenames_buttons_dict[file])
                    else:
                        pass

            else:
                for file in self.content:
                    if file not in self.filenames_buttons_dict:
                        cbutton = QCheckBox(f"{file}")
                        self.filenames_buttons_dict[file] = cbutton
                        self.checkbox_layout.addWidget(self.filenames_buttons_dict[file])
                    else:
                        pass
            remove_btn = QPushButton('Remove')
            remove_btn.clicked.connect(self.delete_checkboxes)
            self.layout.addWidget(remove_btn, 2, 3, 1, 5)
            widget.setLayout(self.checkbox_layout)
            scroll.setWidget(widget)
            self.mainLayout.addWidget(scroll)
        except:
            pass

    def delete_checkboxes(self):
        if self.checkbox_layout is not None:
            while self.checkbox_layout.count():
                item = self.checkbox_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(self.checkbox_layout)
        self.mainLayout.itemAt(1).widget().deleteLater()
        self.layout.itemAt(5).widget().deleteLater()
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
