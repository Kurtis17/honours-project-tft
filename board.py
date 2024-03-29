from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from champion_selection import UI_Champion_Selector_Window
import joblib
import os

class UI_Board_Widget(QWidget):
    tracker = 0
    updated_state = None

    def open_champion_window(self, main_window, current_window, position, state):
        if self.tracker == 1:
            self.window.close()

        self.window = QtWidgets.QMainWindow()
        self.ui = UI_Champion_Selector_Window()
        self.ui.setup_ui_champion_selector_window(self.window, main_window, current_window, position, state)
        self.window.show()
        self.tracker = 1

    def testing(self, text):
        self.updated_state = text

    def setup_ui_board_widget(self, Board_Widget, main_window, state, option):
        main_window_ref = main_window
        Board_Widget.setObjectName("Board_Widget")
        Board_Widget.resize(850, 900)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 48, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 40, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 16, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 21, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 16, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 48, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 40, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 16, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 21, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 16, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 16, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 48, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 40, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 16, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 21, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 16, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 16, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Board_Widget.setPalette(palette)
        self.enemy_unit_1_6 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_1_6.setGeometry(QtCore.QRect(520, 20, 82, 82))
        self.enemy_unit_1_6.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_1_6.setText("")
        self.enemy_unit_1_6.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_1_6.setObjectName("enemy_unit_1_6")
        self.item_three_16 = QtWidgets.QLabel(Board_Widget)
        self.item_three_16.setEnabled(True)
        self.item_three_16.setGeometry(QtCore.QRect(170, 310, 20, 18))
        self.item_three_16.setText("")
        self.item_three_16.setScaledContents(True)
        self.item_three_16.setObjectName("item_three_16")
        self.item_two_11 = QtWidgets.QLabel(Board_Widget)
        self.item_two_11.setEnabled(True)
        self.item_two_11.setGeometry(QtCore.QRect(400, 200, 20, 18))
        self.item_two_11.setText("")
        self.item_two_11.setScaledContents(True)
        self.item_two_11.setObjectName("item_two_11")
        self.item_two = QtWidgets.QLabel(Board_Widget)
        self.item_two.setEnabled(True)
        self.item_two.setGeometry(QtCore.QRect(50, 90, 20, 18))
        self.item_two.setText("")
        self.item_two.setScaledContents(True)
        self.item_two.setObjectName("item_two")
        self.item_three_3 = QtWidgets.QLabel(Board_Widget)
        self.item_three_3.setEnabled(True)
        self.item_three_3.setGeometry(QtCore.QRect(270, 90, 20, 18))
        self.item_three_3.setText("")
        self.item_three_3.setScaledContents(True)
        self.item_three_3.setObjectName("item_three_3")
        self.item_one_29 = QtWidgets.QLabel(Board_Widget)
        self.item_one_29.setEnabled(True)
        self.item_one_29.setGeometry(QtCore.QRect(30, 540, 20, 18))
        self.item_one_29.setText("")
        self.item_one_29.setScaledContents(True)
        self.item_one_29.setObjectName("item_one_29")
        self.item_one_16 = QtWidgets.QLabel(Board_Widget)
        self.item_one_16.setEnabled(True)
        self.item_one_16.setGeometry(QtCore.QRect(130, 310, 20, 18))
        self.item_one_16.setText("")
        self.item_one_16.setScaledContents(True)
        self.item_one_16.setObjectName("item_one_16")
        self.item_three_7 = QtWidgets.QLabel(Board_Widget)
        self.item_three_7.setEnabled(True)
        self.item_three_7.setGeometry(QtCore.QRect(670, 90, 20, 18))
        self.item_three_7.setText("")
        self.item_three_7.setScaledContents(True)
        self.item_three_7.setObjectName("item_three_7")
        self.user_unit_4_3 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_4_3.setGeometry(QtCore.QRect(270, 800, 82, 82))
        self.user_unit_4_3.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_4_3.setText("")
        self.user_unit_4_3.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_4_3.setObjectName("user_unit_4_3")
        self.enemy_unit_1_5 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_1_5.setGeometry(QtCore.QRect(420, 20, 82, 82))
        self.enemy_unit_1_5.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_1_5.setText("")
        self.enemy_unit_1_5.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_1_5.setObjectName("enemy_unit_1_5")
        self.item_two_5 = QtWidgets.QLabel(Board_Widget)
        self.item_two_5.setEnabled(True)
        self.item_two_5.setGeometry(QtCore.QRect(450, 90, 20, 18))
        self.item_two_5.setText("")
        self.item_two_5.setScaledContents(True)
        self.item_two_5.setObjectName("item_two_5")
        self.level_36 = QtWidgets.QLabel(Board_Widget)
        self.level_36.setEnabled(True)
        self.level_36.setGeometry(QtCore.QRect(90, 570, 40, 15))
        self.level_36.setText("")
        self.level_36.setScaledContents(True)
        self.level_36.setObjectName("level_36")
        self.item_three_24 = QtWidgets.QLabel(Board_Widget)
        self.item_three_24.setEnabled(True)
        self.item_three_24.setGeometry(QtCore.QRect(320, 420, 20, 18))
        self.item_three_24.setText("")
        self.item_three_24.setScaledContents(True)
        self.item_three_24.setObjectName("item_three_24")
        self.user_unit_4_6 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_4_6.setGeometry(QtCore.QRect(570, 800, 82, 82))
        self.user_unit_4_6.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_4_6.setText("")
        self.user_unit_4_6.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_4_6.setObjectName("user_unit_4_6")
        self.user_unit_3_7 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_3_7.setGeometry(QtCore.QRect(620, 690, 82, 82))
        self.user_unit_3_7.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_3_7.setText("")
        self.user_unit_3_7.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_3_7.setObjectName("user_unit_3_7")
        self.item_three_52 = QtWidgets.QLabel(Board_Widget)
        self.item_three_52.setEnabled(True)
        self.item_three_52.setGeometry(QtCore.QRect(320, 870, 20, 18))
        self.item_three_52.setText("")
        self.item_three_52.setScaledContents(True)
        self.item_three_52.setObjectName("item_three_52")
        self.item_two_52 = QtWidgets.QLabel(Board_Widget)
        self.item_two_52.setEnabled(True)
        self.item_two_52.setGeometry(QtCore.QRect(300, 870, 20, 18))
        self.item_two_52.setText("")
        self.item_two_52.setScaledContents(True)
        self.item_two_52.setObjectName("item_two_52")
        self.user_unit_4_2 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_4_2.setGeometry(QtCore.QRect(170, 800, 82, 82))
        self.user_unit_4_2.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_4_2.setText("")
        self.user_unit_4_2.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_4_2.setObjectName("user_unit_4_2")
        self.item_two_32 = QtWidgets.QLabel(Board_Widget)
        self.item_two_32.setEnabled(True)
        self.item_two_32.setGeometry(QtCore.QRect(350, 540, 20, 18))
        self.item_two_32.setText("")
        self.item_two_32.setScaledContents(True)
        self.item_two_32.setObjectName("item_two_32")
        self.item_three_19 = QtWidgets.QLabel(Board_Widget)
        self.item_three_19.setEnabled(True)
        self.item_three_19.setGeometry(QtCore.QRect(470, 310, 20, 18))
        self.item_three_19.setText("")
        self.item_three_19.setScaledContents(True)
        self.item_three_19.setObjectName("item_three_19")
        self.item_one_27 = QtWidgets.QLabel(Board_Widget)
        self.item_one_27.setEnabled(True)
        self.item_one_27.setGeometry(QtCore.QRect(580, 420, 20, 18))
        self.item_one_27.setText("")
        self.item_one_27.setScaledContents(True)
        self.item_one_27.setObjectName("item_one_27")
        self.item_three_42 = QtWidgets.QLabel(Board_Widget)
        self.item_three_42.setEnabled(True)
        self.item_three_42.setGeometry(QtCore.QRect(720, 650, 20, 18))
        self.item_three_42.setText("")
        self.item_three_42.setScaledContents(True)
        self.item_three_42.setObjectName("item_three_42")
        self.item_two_43 = QtWidgets.QLabel(Board_Widget)
        self.item_two_43.setEnabled(True)
        self.item_two_43.setGeometry(QtCore.QRect(50, 760, 20, 18))
        self.item_two_43.setText("")
        self.item_two_43.setScaledContents(True)
        self.item_two_43.setObjectName("item_two_43")
        self.item_two_41 = QtWidgets.QLabel(Board_Widget)
        self.item_two_41.setEnabled(True)
        self.item_two_41.setGeometry(QtCore.QRect(600, 650, 20, 18))
        self.item_two_41.setText("")
        self.item_two_41.setScaledContents(True)
        self.item_two_41.setObjectName("item_two_41")
        self.item_two_33 = QtWidgets.QLabel(Board_Widget)
        self.item_two_33.setEnabled(True)
        self.item_two_33.setGeometry(QtCore.QRect(450, 540, 20, 18))
        self.item_two_33.setText("")
        self.item_two_33.setScaledContents(True)
        self.item_two_33.setObjectName("item_two_33")
        self.item_one_33 = QtWidgets.QLabel(Board_Widget)
        self.item_one_33.setEnabled(True)
        self.item_one_33.setGeometry(QtCore.QRect(430, 540, 20, 18))
        self.item_one_33.setText("")
        self.item_one_33.setScaledContents(True)
        self.item_one_33.setObjectName("item_one_33")
        self.level_22 = QtWidgets.QLabel(Board_Widget)
        self.level_22.setEnabled(True)
        self.level_22.setGeometry(QtCore.QRect(90, 340, 40, 15))
        self.level_22.setText("")
        self.level_22.setScaledContents(True)
        self.level_22.setObjectName("level_22")
        self.item_two_50 = QtWidgets.QLabel(Board_Widget)
        self.item_two_50.setEnabled(True)
        self.item_two_50.setGeometry(QtCore.QRect(100, 870, 20, 18))
        self.item_two_50.setText("")
        self.item_two_50.setScaledContents(True)
        self.item_two_50.setObjectName("item_two_50")
        self.item_one_18 = QtWidgets.QLabel(Board_Widget)
        self.item_one_18.setEnabled(True)
        self.item_one_18.setGeometry(QtCore.QRect(330, 310, 20, 18))
        self.item_one_18.setText("")
        self.item_one_18.setScaledContents(True)
        self.item_one_18.setObjectName("item_one_18")
        self.item_two_8 = QtWidgets.QLabel(Board_Widget)
        self.item_two_8.setEnabled(True)
        self.item_two_8.setGeometry(QtCore.QRect(100, 200, 20, 18))
        self.item_two_8.setText("")
        self.item_two_8.setScaledContents(True)
        self.item_two_8.setObjectName("item_two_8")
        self.item_three_50 = QtWidgets.QLabel(Board_Widget)
        self.item_three_50.setEnabled(True)
        self.item_three_50.setGeometry(QtCore.QRect(120, 870, 20, 18))
        self.item_three_50.setText("")
        self.item_three_50.setScaledContents(True)
        self.item_three_50.setObjectName("item_three_50")
        self.item_one_11 = QtWidgets.QLabel(Board_Widget)
        self.item_one_11.setEnabled(True)
        self.item_one_11.setGeometry(QtCore.QRect(380, 200, 20, 18))
        self.item_one_11.setText("")
        self.item_one_11.setScaledContents(True)
        self.item_one_11.setObjectName("item_one_11")
        self.item_three_14 = QtWidgets.QLabel(Board_Widget)
        self.item_three_14.setEnabled(True)
        self.item_three_14.setGeometry(QtCore.QRect(720, 200, 20, 18))
        self.item_three_14.setText("")
        self.item_three_14.setScaledContents(True)
        self.item_three_14.setObjectName("item_three_14")
        self.item_three_43 = QtWidgets.QLabel(Board_Widget)
        self.item_three_43.setEnabled(True)
        self.item_three_43.setGeometry(QtCore.QRect(70, 760, 20, 18))
        self.item_three_43.setText("")
        self.item_three_43.setScaledContents(True)
        self.item_three_43.setObjectName("item_three_43")
        self.item_one_50 = QtWidgets.QLabel(Board_Widget)
        self.item_one_50.setEnabled(True)
        self.item_one_50.setGeometry(QtCore.QRect(80, 870, 20, 18))
        self.item_one_50.setText("")
        self.item_one_50.setScaledContents(True)
        self.item_one_50.setObjectName("item_one_50")
        self.item_two_22 = QtWidgets.QLabel(Board_Widget)
        self.item_two_22.setEnabled(True)
        self.item_two_22.setGeometry(QtCore.QRect(100, 420, 20, 18))
        self.item_two_22.setText("")
        self.item_two_22.setScaledContents(True)
        self.item_two_22.setObjectName("item_two_22")
        self.item_two_3 = QtWidgets.QLabel(Board_Widget)
        self.item_two_3.setEnabled(True)
        self.item_two_3.setGeometry(QtCore.QRect(250, 90, 20, 18))
        self.item_two_3.setText("")
        self.item_two_3.setScaledContents(True)
        self.item_two_3.setObjectName("item_two_3")
        self.item_two_31 = QtWidgets.QLabel(Board_Widget)
        self.item_two_31.setEnabled(True)
        self.item_two_31.setGeometry(QtCore.QRect(250, 540, 20, 18))
        self.item_two_31.setText("")
        self.item_two_31.setScaledContents(True)
        self.item_two_31.setObjectName("item_two_31")
        self.item_two_13 = QtWidgets.QLabel(Board_Widget)
        self.item_two_13.setEnabled(True)
        self.item_two_13.setGeometry(QtCore.QRect(600, 200, 20, 18))
        self.item_two_13.setText("")
        self.item_two_13.setScaledContents(True)
        self.item_two_13.setObjectName("item_two_13")
        self.item_one_9 = QtWidgets.QLabel(Board_Widget)
        self.item_one_9.setEnabled(True)
        self.item_one_9.setGeometry(QtCore.QRect(180, 200, 20, 18))
        self.item_one_9.setText("")
        self.item_one_9.setScaledContents(True)
        self.item_one_9.setObjectName("item_one_9")
        self.level_12 = QtWidgets.QLabel(Board_Widget)
        self.level_12.setEnabled(True)
        self.level_12.setGeometry(QtCore.QRect(490, 120, 40, 15))
        self.level_12.setText("")
        self.level_12.setScaledContents(True)
        self.level_12.setObjectName("level_12")
        self.item_three_18 = QtWidgets.QLabel(Board_Widget)
        self.item_three_18.setEnabled(True)
        self.item_three_18.setGeometry(QtCore.QRect(370, 310, 20, 18))
        self.item_three_18.setText("")
        self.item_three_18.setScaledContents(True)
        self.item_three_18.setObjectName("item_three_18")
        self.level_7 = QtWidgets.QLabel(Board_Widget)
        self.level_7.setEnabled(True)
        self.level_7.setGeometry(QtCore.QRect(640, 10, 40, 15))
        self.level_7.setText("")
        self.level_7.setScaledContents(True)
        self.level_7.setObjectName("level_7")
        self.item_two_34 = QtWidgets.QLabel(Board_Widget)
        self.item_two_34.setEnabled(True)
        self.item_two_34.setGeometry(QtCore.QRect(550, 540, 20, 18))
        self.item_two_34.setText("")
        self.item_two_34.setScaledContents(True)
        self.item_two_34.setObjectName("item_two_34")
        self.item_one_38 = QtWidgets.QLabel(Board_Widget)
        self.item_one_38.setEnabled(True)
        self.item_one_38.setGeometry(QtCore.QRect(280, 650, 20, 18))
        self.item_one_38.setText("")
        self.item_one_38.setScaledContents(True)
        self.item_one_38.setObjectName("item_one_38")
        self.user_unit_3_3 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_3_3.setGeometry(QtCore.QRect(220, 690, 82, 82))
        self.user_unit_3_3.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_3_3.setText("")
        self.user_unit_3_3.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_3_3.setObjectName("user_unit_3_3")
        self.level_19 = QtWidgets.QLabel(Board_Widget)
        self.level_19.setEnabled(True)
        self.level_19.setGeometry(QtCore.QRect(440, 230, 40, 15))
        self.level_19.setText("")
        self.level_19.setScaledContents(True)
        self.level_19.setObjectName("level_19")
        self.item_three_21 = QtWidgets.QLabel(Board_Widget)
        self.item_three_21.setEnabled(True)
        self.item_three_21.setGeometry(QtCore.QRect(670, 310, 20, 18))
        self.item_three_21.setText("")
        self.item_three_21.setScaledContents(True)
        self.item_three_21.setObjectName("item_three_21")
        self.item_two_48 = QtWidgets.QLabel(Board_Widget)
        self.item_two_48.setEnabled(True)
        self.item_two_48.setGeometry(QtCore.QRect(550, 760, 20, 18))
        self.item_two_48.setText("")
        self.item_two_48.setScaledContents(True)
        self.item_two_48.setObjectName("item_two_48")
        self.level_50 = QtWidgets.QLabel(Board_Widget)
        self.level_50.setEnabled(True)
        self.level_50.setGeometry(QtCore.QRect(90, 790, 40, 15))
        self.level_50.setText("")
        self.level_50.setScaledContents(True)
        self.level_50.setObjectName("level_50")
        self.user_unit_2_3 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_2_3.setGeometry(QtCore.QRect(270, 580, 82, 82))
        self.user_unit_2_3.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_2_3.setText("")
        self.user_unit_2_3.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_2_3.setObjectName("user_unit_2_3")
        self.item_three_33 = QtWidgets.QLabel(Board_Widget)
        self.item_three_33.setEnabled(True)
        self.item_three_33.setGeometry(QtCore.QRect(470, 540, 20, 18))
        self.item_three_33.setText("")
        self.item_three_33.setScaledContents(True)
        self.item_three_33.setObjectName("item_three_33")
        self.level_16 = QtWidgets.QLabel(Board_Widget)
        self.level_16.setEnabled(True)
        self.level_16.setGeometry(QtCore.QRect(140, 230, 40, 15))
        self.level_16.setText("")
        self.level_16.setScaledContents(True)
        self.level_16.setObjectName("level_16")
        self.level_40 = QtWidgets.QLabel(Board_Widget)
        self.level_40.setEnabled(True)
        self.level_40.setGeometry(QtCore.QRect(490, 570, 40, 15))
        self.level_40.setText("")
        self.level_40.setScaledContents(True)
        self.level_40.setObjectName("level_40")
        self.user_unit_1_3 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_1_3.setGeometry(QtCore.QRect(220, 470, 82, 82))
        self.user_unit_1_3.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_1_3.setText("")
        self.user_unit_1_3.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_1_3.setObjectName("user_unit_1_3")
        self.item_two_45 = QtWidgets.QLabel(Board_Widget)
        self.item_two_45.setEnabled(True)
        self.item_two_45.setGeometry(QtCore.QRect(250, 760, 20, 18))
        self.item_two_45.setText("")
        self.item_two_45.setScaledContents(True)
        self.item_two_45.setObjectName("item_two_45")
        self.enemy_unit_3_5 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_3_5.setGeometry(QtCore.QRect(420, 240, 82, 82))
        self.enemy_unit_3_5.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_3_5.setText("")
        self.enemy_unit_3_5.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_3_5.setObjectName("enemy_unit_3_5")
        self.item_one_43 = QtWidgets.QLabel(Board_Widget)
        self.item_one_43.setEnabled(True)
        self.item_one_43.setGeometry(QtCore.QRect(30, 760, 20, 18))
        self.item_one_43.setText("")
        self.item_one_43.setScaledContents(True)
        self.item_one_43.setObjectName("item_one_43")
        self.item_two_54 = QtWidgets.QLabel(Board_Widget)
        self.item_two_54.setEnabled(True)
        self.item_two_54.setGeometry(QtCore.QRect(500, 870, 20, 18))
        self.item_two_54.setText("")
        self.item_two_54.setScaledContents(True)
        self.item_two_54.setObjectName("item_two_54")
        self.item_one_41 = QtWidgets.QLabel(Board_Widget)
        self.item_one_41.setEnabled(True)
        self.item_one_41.setGeometry(QtCore.QRect(580, 650, 20, 18))
        self.item_one_41.setText("")
        self.item_one_41.setScaledContents(True)
        self.item_one_41.setObjectName("item_one_41")
        self.item_one_32 = QtWidgets.QLabel(Board_Widget)
        self.item_one_32.setEnabled(True)
        self.item_one_32.setGeometry(QtCore.QRect(330, 540, 20, 18))
        self.item_one_32.setText("")
        self.item_one_32.setScaledContents(True)
        self.item_one_32.setObjectName("item_one_32")
        self.item_one_23 = QtWidgets.QLabel(Board_Widget)
        self.item_one_23.setEnabled(True)
        self.item_one_23.setGeometry(QtCore.QRect(180, 420, 20, 18))
        self.item_one_23.setText("")
        self.item_one_23.setScaledContents(True)
        self.item_one_23.setObjectName("item_one_23")
        self.item_three_29 = QtWidgets.QLabel(Board_Widget)
        self.item_three_29.setEnabled(True)
        self.item_three_29.setGeometry(QtCore.QRect(70, 540, 20, 18))
        self.item_three_29.setText("")
        self.item_three_29.setScaledContents(True)
        self.item_three_29.setObjectName("item_three_29")
        self.item_three_12 = QtWidgets.QLabel(Board_Widget)
        self.item_three_12.setEnabled(True)
        self.item_three_12.setGeometry(QtCore.QRect(520, 200, 20, 18))
        self.item_three_12.setText("")
        self.item_three_12.setScaledContents(True)
        self.item_three_12.setObjectName("item_three_12")
        self.item_one_4 = QtWidgets.QLabel(Board_Widget)
        self.item_one_4.setEnabled(True)
        self.item_one_4.setGeometry(QtCore.QRect(330, 90, 20, 18))
        self.item_one_4.setText("")
        self.item_one_4.setScaledContents(True)
        self.item_one_4.setObjectName("item_one_4")
        self.level_34 = QtWidgets.QLabel(Board_Widget)
        self.level_34.setEnabled(True)
        self.level_34.setGeometry(QtCore.QRect(540, 460, 40, 15))
        self.level_34.setText("")
        self.level_34.setScaledContents(True)
        self.level_34.setObjectName("level_34")
        self.item_one_47 = QtWidgets.QLabel(Board_Widget)
        self.item_one_47.setEnabled(True)
        self.item_one_47.setGeometry(QtCore.QRect(430, 760, 20, 18))
        self.item_one_47.setText("")
        self.item_one_47.setScaledContents(True)
        self.item_one_47.setObjectName("item_one_47")
        self.item_three_37 = QtWidgets.QLabel(Board_Widget)
        self.item_three_37.setEnabled(True)
        self.item_three_37.setGeometry(QtCore.QRect(220, 650, 20, 18))
        self.item_three_37.setText("")
        self.item_three_37.setScaledContents(True)
        self.item_three_37.setObjectName("item_three_37")
        self.user_unit_1_7 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_1_7.setGeometry(QtCore.QRect(620, 470, 82, 82))
        self.user_unit_1_7.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_1_7.setText("")
        self.user_unit_1_7.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_1_7.setObjectName("user_unit_1_7")
        self.level_44 = QtWidgets.QLabel(Board_Widget)
        self.level_44.setEnabled(True)
        self.level_44.setGeometry(QtCore.QRect(140, 680, 40, 15))
        self.level_44.setText("")
        self.level_44.setScaledContents(True)
        self.level_44.setObjectName("level_44")
        self.enemy_unit_1_7 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_1_7.setGeometry(QtCore.QRect(620, 20, 82, 82))
        self.enemy_unit_1_7.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_1_7.setText("")
        self.enemy_unit_1_7.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_1_7.setObjectName("enemy_unit_1_7")
        self.enemy_unit_2_7 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_2_7.setGeometry(QtCore.QRect(670, 130, 82, 82))
        self.enemy_unit_2_7.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_2_7.setText("")
        self.enemy_unit_2_7.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_2_7.setObjectName("enemy_unit_2_7")
        self.item_two_39 = QtWidgets.QLabel(Board_Widget)
        self.item_two_39.setEnabled(True)
        self.item_two_39.setGeometry(QtCore.QRect(400, 650, 20, 18))
        self.item_two_39.setText("")
        self.item_two_39.setScaledContents(True)
        self.item_two_39.setObjectName("item_two_39")
        self.level_55 = QtWidgets.QLabel(Board_Widget)
        self.level_55.setEnabled(True)
        self.level_55.setGeometry(QtCore.QRect(590, 790, 40, 15))
        self.level_55.setText("")
        self.level_55.setScaledContents(True)
        self.level_55.setObjectName("level_55")
        self.user_unit_1_4 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_1_4.setGeometry(QtCore.QRect(320, 470, 82, 82))
        self.user_unit_1_4.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_1_4.setText("")
        self.user_unit_1_4.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_1_4.setObjectName("user_unit_1_4")
        self.item_two_15 = QtWidgets.QLabel(Board_Widget)
        self.item_two_15.setEnabled(True)
        self.item_two_15.setGeometry(QtCore.QRect(50, 310, 20, 18))
        self.item_two_15.setText("")
        self.item_two_15.setScaledContents(True)
        self.item_two_15.setObjectName("item_two_15")
        self.level_48 = QtWidgets.QLabel(Board_Widget)
        self.level_48.setEnabled(True)
        self.level_48.setGeometry(QtCore.QRect(540, 680, 40, 15))
        self.level_48.setText("")
        self.level_48.setScaledContents(True)
        self.level_48.setObjectName("level_48")
        self.item_two_20 = QtWidgets.QLabel(Board_Widget)
        self.item_two_20.setEnabled(True)
        self.item_two_20.setGeometry(QtCore.QRect(550, 310, 20, 18))
        self.item_two_20.setText("")
        self.item_two_20.setScaledContents(True)
        self.item_two_20.setObjectName("item_two_20")
        self.level_45 = QtWidgets.QLabel(Board_Widget)
        self.level_45.setEnabled(True)
        self.level_45.setGeometry(QtCore.QRect(240, 680, 40, 15))
        self.level_45.setText("")
        self.level_45.setScaledContents(True)
        self.level_45.setObjectName("level_45")
        self.level_43 = QtWidgets.QLabel(Board_Widget)
        self.level_43.setEnabled(True)
        self.level_43.setGeometry(QtCore.QRect(40, 680, 40, 15))
        self.level_43.setText("")
        self.level_43.setScaledContents(True)
        self.level_43.setObjectName("level_43")
        self.enemy_unit_2_4 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_2_4.setGeometry(QtCore.QRect(370, 130, 82, 82))
        self.enemy_unit_2_4.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_2_4.setText("")
        self.enemy_unit_2_4.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_2_4.setObjectName("enemy_unit_2_4")
        self.enemy_unit_1_2 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_1_2.setGeometry(QtCore.QRect(120, 20, 82, 82))
        self.enemy_unit_1_2.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_1_2.setText("")
        self.enemy_unit_1_2.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_1_2.setObjectName("enemy_unit_1_2")
        self.item_three_22 = QtWidgets.QLabel(Board_Widget)
        self.item_three_22.setEnabled(True)
        self.item_three_22.setGeometry(QtCore.QRect(120, 420, 20, 18))
        self.item_three_22.setText("")
        self.item_three_22.setScaledContents(True)
        self.item_three_22.setObjectName("item_three_22")
        self.item_three_10 = QtWidgets.QLabel(Board_Widget)
        self.item_three_10.setEnabled(True)
        self.item_three_10.setGeometry(QtCore.QRect(320, 200, 20, 18))
        self.item_three_10.setText("")
        self.item_three_10.setScaledContents(True)
        self.item_three_10.setObjectName("item_three_10")
        self.item_two_2 = QtWidgets.QLabel(Board_Widget)
        self.item_two_2.setEnabled(True)
        self.item_two_2.setGeometry(QtCore.QRect(150, 90, 20, 18))
        self.item_two_2.setText("")
        self.item_two_2.setScaledContents(True)
        self.item_two_2.setObjectName("item_two_2")
        self.level_46 = QtWidgets.QLabel(Board_Widget)
        self.level_46.setEnabled(True)
        self.level_46.setGeometry(QtCore.QRect(340, 680, 40, 15))
        self.level_46.setText("")
        self.level_46.setScaledContents(True)
        self.level_46.setObjectName("level_46")
        self.item_two_35 = QtWidgets.QLabel(Board_Widget)
        self.item_two_35.setEnabled(True)
        self.item_two_35.setGeometry(QtCore.QRect(650, 540, 20, 18))
        self.item_two_35.setText("")
        self.item_two_35.setScaledContents(True)
        self.item_two_35.setObjectName("item_two_35")
        self.enemy_unit_4_7 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_4_7.setGeometry(QtCore.QRect(670, 350, 82, 82))
        self.enemy_unit_4_7.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_4_7.setText("")
        self.enemy_unit_4_7.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_4_7.setObjectName("enemy_unit_4_7")
        self.item_one_13 = QtWidgets.QLabel(Board_Widget)
        self.item_one_13.setEnabled(True)
        self.item_one_13.setGeometry(QtCore.QRect(580, 200, 20, 18))
        self.item_one_13.setText("")
        self.item_one_13.setScaledContents(True)
        self.item_one_13.setObjectName("item_one_13")
        self.user_unit_3_1 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_3_1.setGeometry(QtCore.QRect(20, 690, 82, 82))
        self.user_unit_3_1.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_3_1.setText("")
        self.user_unit_3_1.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_3_1.setObjectName("user_unit_3_1")
        self.item_one_45 = QtWidgets.QLabel(Board_Widget)
        self.item_one_45.setEnabled(True)
        self.item_one_45.setGeometry(QtCore.QRect(230, 760, 20, 18))
        self.item_one_45.setText("")
        self.item_one_45.setScaledContents(True)
        self.item_one_45.setObjectName("item_one_45")
        self.item_three_2 = QtWidgets.QLabel(Board_Widget)
        self.item_three_2.setEnabled(True)
        self.item_three_2.setGeometry(QtCore.QRect(170, 90, 20, 18))
        self.item_three_2.setText("")
        self.item_three_2.setScaledContents(True)
        self.item_three_2.setObjectName("item_three_2")
        self.level_52 = QtWidgets.QLabel(Board_Widget)
        self.level_52.setEnabled(True)
        self.level_52.setGeometry(QtCore.QRect(290, 790, 40, 15))
        self.level_52.setText("")
        self.level_52.setScaledContents(True)
        self.level_52.setObjectName("level_52")
        self.level_38 = QtWidgets.QLabel(Board_Widget)
        self.level_38.setEnabled(True)
        self.level_38.setGeometry(QtCore.QRect(290, 570, 40, 15))
        self.level_38.setText("")
        self.level_38.setScaledContents(True)
        self.level_38.setObjectName("level_38")
        self.item_one_12 = QtWidgets.QLabel(Board_Widget)
        self.item_one_12.setEnabled(True)
        self.item_one_12.setGeometry(QtCore.QRect(480, 200, 20, 18))
        self.item_one_12.setText("")
        self.item_one_12.setScaledContents(True)
        self.item_one_12.setObjectName("item_one_12")
        self.item_two_53 = QtWidgets.QLabel(Board_Widget)
        self.item_two_53.setEnabled(True)
        self.item_two_53.setGeometry(QtCore.QRect(400, 870, 20, 18))
        self.item_two_53.setText("")
        self.item_two_53.setScaledContents(True)
        self.item_two_53.setObjectName("item_two_53")
        self.level_14 = QtWidgets.QLabel(Board_Widget)
        self.level_14.setEnabled(True)
        self.level_14.setGeometry(QtCore.QRect(690, 120, 40, 15))
        self.level_14.setText("")
        self.level_14.setScaledContents(True)
        self.level_14.setObjectName("level_14")
        self.level_56 = QtWidgets.QLabel(Board_Widget)
        self.level_56.setEnabled(True)
        self.level_56.setGeometry(QtCore.QRect(690, 790, 40, 15))
        self.level_56.setText("")
        self.level_56.setScaledContents(True)
        self.level_56.setObjectName("level_56")
        self.item_two_30 = QtWidgets.QLabel(Board_Widget)
        self.item_two_30.setEnabled(True)
        self.item_two_30.setGeometry(QtCore.QRect(150, 540, 20, 18))
        self.item_two_30.setText("")
        self.item_two_30.setScaledContents(True)
        self.item_two_30.setObjectName("item_two_30")
        self.item_one_37 = QtWidgets.QLabel(Board_Widget)
        self.item_one_37.setEnabled(True)
        self.item_one_37.setGeometry(QtCore.QRect(180, 650, 20, 18))
        self.item_one_37.setText("")
        self.item_one_37.setScaledContents(True)
        self.item_one_37.setObjectName("item_one_37")
        self.item_two_25 = QtWidgets.QLabel(Board_Widget)
        self.item_two_25.setEnabled(True)
        self.item_two_25.setGeometry(QtCore.QRect(400, 420, 20, 18))
        self.item_two_25.setText("")
        self.item_two_25.setScaledContents(True)
        self.item_two_25.setObjectName("item_two_25")
        self.item_two_42 = QtWidgets.QLabel(Board_Widget)
        self.item_two_42.setEnabled(True)
        self.item_two_42.setGeometry(QtCore.QRect(700, 650, 20, 18))
        self.item_two_42.setText("")
        self.item_two_42.setScaledContents(True)
        self.item_two_42.setObjectName("item_two_42")
        self.item_two_12 = QtWidgets.QLabel(Board_Widget)
        self.item_two_12.setEnabled(True)
        self.item_two_12.setGeometry(QtCore.QRect(500, 200, 20, 18))
        self.item_two_12.setText("")
        self.item_two_12.setScaledContents(True)
        self.item_two_12.setObjectName("item_two_12")
        self.item_three_26 = QtWidgets.QLabel(Board_Widget)
        self.item_three_26.setEnabled(True)
        self.item_three_26.setGeometry(QtCore.QRect(520, 420, 20, 18))
        self.item_three_26.setText("")
        self.item_three_26.setScaledContents(True)
        self.item_three_26.setObjectName("item_three_26")
        self.item_two_27 = QtWidgets.QLabel(Board_Widget)
        self.item_two_27.setEnabled(True)
        self.item_two_27.setGeometry(QtCore.QRect(600, 420, 20, 18))
        self.item_two_27.setText("")
        self.item_two_27.setScaledContents(True)
        self.item_two_27.setObjectName("item_two_27")
        self.level_20 = QtWidgets.QLabel(Board_Widget)
        self.level_20.setEnabled(True)
        self.level_20.setGeometry(QtCore.QRect(540, 230, 40, 15))
        self.level_20.setText("")
        self.level_20.setScaledContents(True)
        self.level_20.setObjectName("level_20")
        self.enemy_unit_2_3 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_2_3.setGeometry(QtCore.QRect(270, 130, 82, 82))
        self.enemy_unit_2_3.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_2_3.setText("")
        self.enemy_unit_2_3.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_2_3.setObjectName("enemy_unit_2_3")
        self.item_three_5 = QtWidgets.QLabel(Board_Widget)
        self.item_three_5.setEnabled(True)
        self.item_three_5.setGeometry(QtCore.QRect(470, 90, 20, 18))
        self.item_three_5.setText("")
        self.item_three_5.setScaledContents(True)
        self.item_three_5.setObjectName("item_three_5")
        self.level_13 = QtWidgets.QLabel(Board_Widget)
        self.level_13.setEnabled(True)
        self.level_13.setGeometry(QtCore.QRect(590, 120, 40, 15))
        self.level_13.setText("")
        self.level_13.setScaledContents(True)
        self.level_13.setObjectName("level_13")
        self.item_two_55 = QtWidgets.QLabel(Board_Widget)
        self.item_two_55.setEnabled(True)
        self.item_two_55.setGeometry(QtCore.QRect(600, 870, 20, 18))
        self.item_two_55.setText("")
        self.item_two_55.setScaledContents(True)
        self.item_two_55.setObjectName("item_two_55")
        self.level_6 = QtWidgets.QLabel(Board_Widget)
        self.level_6.setEnabled(True)
        self.level_6.setGeometry(QtCore.QRect(540, 10, 40, 15))
        self.level_6.setText("")
        self.level_6.setScaledContents(True)
        self.level_6.setObjectName("level_6")
        self.item_three_4 = QtWidgets.QLabel(Board_Widget)
        self.item_three_4.setEnabled(True)
        self.item_three_4.setGeometry(QtCore.QRect(370, 90, 20, 18))
        self.item_three_4.setText("")
        self.item_three_4.setScaledContents(True)
        self.item_three_4.setObjectName("item_three_4")
        self.item_two_47 = QtWidgets.QLabel(Board_Widget)
        self.item_two_47.setEnabled(True)
        self.item_two_47.setGeometry(QtCore.QRect(450, 760, 20, 18))
        self.item_two_47.setText("")
        self.item_two_47.setScaledContents(True)
        self.item_two_47.setObjectName("item_two_47")
        self.level_15 = QtWidgets.QLabel(Board_Widget)
        self.level_15.setEnabled(True)
        self.level_15.setGeometry(QtCore.QRect(40, 230, 40, 15))
        self.level_15.setText("")
        self.level_15.setScaledContents(True)
        self.level_15.setObjectName("level_15")
        self.enemy_unit_2_6 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_2_6.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.enemy_unit_2_6.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_2_6.setText("")
        self.enemy_unit_2_6.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_2_6.setObjectName("enemy_unit_2_6")
        self.item_one_22 = QtWidgets.QLabel(Board_Widget)
        self.item_one_22.setEnabled(True)
        self.item_one_22.setGeometry(QtCore.QRect(80, 420, 20, 18))
        self.item_one_22.setText("")
        self.item_one_22.setScaledContents(True)
        self.item_one_22.setObjectName("item_one_22")
        self.enemy_unit_4_3 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_4_3.setGeometry(QtCore.QRect(270, 350, 82, 82))
        self.enemy_unit_4_3.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_4_3.setText("")
        self.enemy_unit_4_3.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_4_3.setObjectName("enemy_unit_4_3")
        self.item_one_31 = QtWidgets.QLabel(Board_Widget)
        self.item_one_31.setEnabled(True)
        self.item_one_31.setGeometry(QtCore.QRect(230, 540, 20, 18))
        self.item_one_31.setText("")
        self.item_one_31.setScaledContents(True)
        self.item_one_31.setObjectName("item_one_31")
        self.item_two_46 = QtWidgets.QLabel(Board_Widget)
        self.item_two_46.setEnabled(True)
        self.item_two_46.setGeometry(QtCore.QRect(350, 760, 20, 18))
        self.item_two_46.setText("")
        self.item_two_46.setScaledContents(True)
        self.item_two_46.setObjectName("item_two_46")
        self.item_one_34 = QtWidgets.QLabel(Board_Widget)
        self.item_one_34.setEnabled(True)
        self.item_one_34.setGeometry(QtCore.QRect(530, 540, 20, 18))
        self.item_one_34.setText("")
        self.item_one_34.setScaledContents(True)
        self.item_one_34.setObjectName("item_one_34")
        self.level_25 = QtWidgets.QLabel(Board_Widget)
        self.level_25.setEnabled(True)
        self.level_25.setGeometry(QtCore.QRect(390, 340, 40, 15))
        self.level_25.setText("")
        self.level_25.setScaledContents(True)
        self.level_25.setObjectName("level_25")
        self.enemy_unit_4_2 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_4_2.setGeometry(QtCore.QRect(170, 350, 82, 82))
        self.enemy_unit_4_2.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_4_2.setText("")
        self.enemy_unit_4_2.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_4_2.setObjectName("enemy_unit_4_2")
        self.item_one = QtWidgets.QLabel(Board_Widget)
        self.item_one.setEnabled(True)
        self.item_one.setGeometry(QtCore.QRect(30, 90, 20, 18))
        self.item_one.setText("")
        self.item_one.setScaledContents(True)
        self.item_one.setObjectName("item_one")
        self.item_three_44 = QtWidgets.QLabel(Board_Widget)
        self.item_three_44.setEnabled(True)
        self.item_three_44.setGeometry(QtCore.QRect(170, 760, 20, 18))
        self.item_three_44.setText("")
        self.item_three_44.setScaledContents(True)
        self.item_three_44.setObjectName("item_three_44")
        self.item_one_54 = QtWidgets.QLabel(Board_Widget)
        self.item_one_54.setEnabled(True)
        self.item_one_54.setGeometry(QtCore.QRect(480, 870, 20, 18))
        self.item_one_54.setText("")
        self.item_one_54.setScaledContents(True)
        self.item_one_54.setObjectName("item_one_54")
        self.item_three_49 = QtWidgets.QLabel(Board_Widget)
        self.item_three_49.setEnabled(True)
        self.item_three_49.setGeometry(QtCore.QRect(670, 760, 20, 18))
        self.item_three_49.setText("")
        self.item_three_49.setScaledContents(True)
        self.item_three_49.setObjectName("item_three_49")
        self.user_unit_3_6 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_3_6.setGeometry(QtCore.QRect(520, 690, 82, 82))
        self.user_unit_3_6.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_3_6.setText("")
        self.user_unit_3_6.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_3_6.setObjectName("user_unit_3_6")
        self.item_one_5 = QtWidgets.QLabel(Board_Widget)
        self.item_one_5.setEnabled(True)
        self.item_one_5.setGeometry(QtCore.QRect(430, 90, 20, 18))
        self.item_one_5.setText("")
        self.item_one_5.setScaledContents(True)
        self.item_one_5.setObjectName("item_one_5")
        self.item_three_35 = QtWidgets.QLabel(Board_Widget)
        self.item_three_35.setEnabled(True)
        self.item_three_35.setGeometry(QtCore.QRect(670, 540, 20, 18))
        self.item_three_35.setText("")
        self.item_three_35.setScaledContents(True)
        self.item_three_35.setObjectName("item_three_35")
        self.level_21 = QtWidgets.QLabel(Board_Widget)
        self.level_21.setEnabled(True)
        self.level_21.setGeometry(QtCore.QRect(640, 230, 40, 15))
        self.level_21.setText("")
        self.level_21.setScaledContents(True)
        self.level_21.setObjectName("level_21")
        self.item_two_4 = QtWidgets.QLabel(Board_Widget)
        self.item_two_4.setEnabled(True)
        self.item_two_4.setGeometry(QtCore.QRect(350, 90, 20, 18))
        self.item_two_4.setText("")
        self.item_two_4.setScaledContents(True)
        self.item_two_4.setObjectName("item_two_4")
        self.level_32 = QtWidgets.QLabel(Board_Widget)
        self.level_32.setEnabled(True)
        self.level_32.setGeometry(QtCore.QRect(340, 460, 40, 15))
        self.level_32.setText("")
        self.level_32.setScaledContents(True)
        self.level_32.setObjectName("level_32")
        self.item_two_17 = QtWidgets.QLabel(Board_Widget)
        self.item_two_17.setEnabled(True)
        self.item_two_17.setGeometry(QtCore.QRect(250, 310, 20, 18))
        self.item_two_17.setText("")
        self.item_two_17.setScaledContents(True)
        self.item_two_17.setObjectName("item_two_17")
        self.item_three_9 = QtWidgets.QLabel(Board_Widget)
        self.item_three_9.setEnabled(True)
        self.item_three_9.setGeometry(QtCore.QRect(220, 200, 20, 18))
        self.item_three_9.setText("")
        self.item_three_9.setScaledContents(True)
        self.item_three_9.setObjectName("item_three_9")
        self.item_one_30 = QtWidgets.QLabel(Board_Widget)
        self.item_one_30.setEnabled(True)
        self.item_one_30.setGeometry(QtCore.QRect(130, 540, 20, 18))
        self.item_one_30.setText("")
        self.item_one_30.setScaledContents(True)
        self.item_one_30.setObjectName("item_one_30")
        self.item_one_52 = QtWidgets.QLabel(Board_Widget)
        self.item_one_52.setEnabled(True)
        self.item_one_52.setGeometry(QtCore.QRect(280, 870, 20, 18))
        self.item_one_52.setText("")
        self.item_one_52.setScaledContents(True)
        self.item_one_52.setObjectName("item_one_52")
        self.item_two_14 = QtWidgets.QLabel(Board_Widget)
        self.item_two_14.setEnabled(True)
        self.item_two_14.setGeometry(QtCore.QRect(700, 200, 20, 18))
        self.item_two_14.setText("")
        self.item_two_14.setScaledContents(True)
        self.item_two_14.setObjectName("item_two_14")
        self.level_17 = QtWidgets.QLabel(Board_Widget)
        self.level_17.setEnabled(True)
        self.level_17.setGeometry(QtCore.QRect(240, 230, 40, 15))
        self.level_17.setText("")
        self.level_17.setScaledContents(True)
        self.level_17.setObjectName("level_17")
        self.enemy_unit_1_1 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_1_1.setGeometry(QtCore.QRect(20, 20, 80, 80))
        self.enemy_unit_1_1.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_1_1.setText("")
        self.enemy_unit_1_1.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_1_1.setObjectName("enemy_unit_1_1")
        self.item_three_28 = QtWidgets.QLabel(Board_Widget)
        self.item_three_28.setEnabled(True)
        self.item_three_28.setGeometry(QtCore.QRect(720, 420, 20, 18))
        self.item_three_28.setText("")
        self.item_three_28.setScaledContents(True)
        self.item_three_28.setObjectName("item_three_28")
        self.item_two_44 = QtWidgets.QLabel(Board_Widget)
        self.item_two_44.setEnabled(True)
        self.item_two_44.setGeometry(QtCore.QRect(150, 760, 20, 18))
        self.item_two_44.setText("")
        self.item_two_44.setScaledContents(True)
        self.item_two_44.setObjectName("item_two_44")
        self.enemy_unit_4_5 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_4_5.setGeometry(QtCore.QRect(470, 350, 82, 82))
        self.enemy_unit_4_5.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_4_5.setText("")
        self.enemy_unit_4_5.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_4_5.setObjectName("enemy_unit_4_5")
        self.item_three_30 = QtWidgets.QLabel(Board_Widget)
        self.item_three_30.setEnabled(True)
        self.item_three_30.setGeometry(QtCore.QRect(170, 540, 20, 18))
        self.item_three_30.setText("")
        self.item_three_30.setScaledContents(True)
        self.item_three_30.setObjectName("item_three_30")
        self.item_three_13 = QtWidgets.QLabel(Board_Widget)
        self.item_three_13.setEnabled(True)
        self.item_three_13.setGeometry(QtCore.QRect(620, 200, 20, 18))
        self.item_three_13.setText("")
        self.item_three_13.setScaledContents(True)
        self.item_three_13.setObjectName("item_three_13")
        self.level_3 = QtWidgets.QLabel(Board_Widget)
        self.level_3.setEnabled(True)
        self.level_3.setGeometry(QtCore.QRect(240, 10, 40, 15))
        self.level_3.setText("")
        self.level_3.setScaledContents(True)
        self.level_3.setObjectName("level_3")
        self.item_three_45 = QtWidgets.QLabel(Board_Widget)
        self.item_three_45.setEnabled(True)
        self.item_three_45.setGeometry(QtCore.QRect(270, 760, 20, 18))
        self.item_three_45.setText("")
        self.item_three_45.setScaledContents(True)
        self.item_three_45.setObjectName("item_three_45")
        self.item_three_41 = QtWidgets.QLabel(Board_Widget)
        self.item_three_41.setEnabled(True)
        self.item_three_41.setGeometry(QtCore.QRect(620, 650, 20, 18))
        self.item_three_41.setText("")
        self.item_three_41.setScaledContents(True)
        self.item_three_41.setObjectName("item_three_41")
        self.level_2 = QtWidgets.QLabel(Board_Widget)
        self.level_2.setEnabled(True)
        self.level_2.setGeometry(QtCore.QRect(140, 10, 40, 15))
        self.level_2.setText("")
        self.level_2.setScaledContents(True)
        self.level_2.setObjectName("level_2")
        self.item_three_15 = QtWidgets.QLabel(Board_Widget)
        self.item_three_15.setEnabled(True)
        self.item_three_15.setGeometry(QtCore.QRect(70, 310, 20, 18))
        self.item_three_15.setText("")
        self.item_three_15.setScaledContents(True)
        self.item_three_15.setObjectName("item_three_15")
        self.item_three_32 = QtWidgets.QLabel(Board_Widget)
        self.item_three_32.setEnabled(True)
        self.item_three_32.setGeometry(QtCore.QRect(370, 540, 20, 18))
        self.item_three_32.setText("")
        self.item_three_32.setScaledContents(True)
        self.item_three_32.setObjectName("item_three_32")
        self.item_two_38 = QtWidgets.QLabel(Board_Widget)
        self.item_two_38.setEnabled(True)
        self.item_two_38.setGeometry(QtCore.QRect(300, 650, 20, 18))
        self.item_two_38.setText("")
        self.item_two_38.setScaledContents(True)
        self.item_two_38.setObjectName("item_two_38")
        self.item_two_16 = QtWidgets.QLabel(Board_Widget)
        self.item_two_16.setEnabled(True)
        self.item_two_16.setGeometry(QtCore.QRect(150, 310, 20, 18))
        self.item_two_16.setText("")
        self.item_two_16.setScaledContents(True)
        self.item_two_16.setObjectName("item_two_16")
        self.level_26 = QtWidgets.QLabel(Board_Widget)
        self.level_26.setEnabled(True)
        self.level_26.setGeometry(QtCore.QRect(490, 340, 40, 15))
        self.level_26.setText("")
        self.level_26.setScaledContents(True)
        self.level_26.setObjectName("level_26")
        self.item_one_28 = QtWidgets.QLabel(Board_Widget)
        self.item_one_28.setEnabled(True)
        self.item_one_28.setGeometry(QtCore.QRect(680, 420, 20, 18))
        self.item_one_28.setText("")
        self.item_one_28.setScaledContents(True)
        self.item_one_28.setObjectName("item_one_28")
        self.enemy_unit_3_2 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_3_2.setGeometry(QtCore.QRect(120, 240, 82, 82))
        self.enemy_unit_3_2.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_3_2.setText("")
        self.enemy_unit_3_2.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_3_2.setObjectName("enemy_unit_3_2")
        self.level_5 = QtWidgets.QLabel(Board_Widget)
        self.level_5.setEnabled(True)
        self.level_5.setGeometry(QtCore.QRect(440, 10, 40, 15))
        self.level_5.setText("")
        self.level_5.setScaledContents(True)
        self.level_5.setObjectName("level_5")
        self.item_one_48 = QtWidgets.QLabel(Board_Widget)
        self.item_one_48.setEnabled(True)
        self.item_one_48.setGeometry(QtCore.QRect(530, 760, 20, 18))
        self.item_one_48.setText("")
        self.item_one_48.setScaledContents(True)
        self.item_one_48.setObjectName("item_one_48")
        self.item_one_40 = QtWidgets.QLabel(Board_Widget)
        self.item_one_40.setEnabled(True)
        self.item_one_40.setGeometry(QtCore.QRect(480, 650, 20, 18))
        self.item_one_40.setText("")
        self.item_one_40.setScaledContents(True)
        self.item_one_40.setObjectName("item_one_40")
        self.level_11 = QtWidgets.QLabel(Board_Widget)
        self.level_11.setEnabled(True)
        self.level_11.setGeometry(QtCore.QRect(390, 120, 40, 15))
        self.level_11.setText("")
        self.level_11.setScaledContents(True)
        self.level_11.setObjectName("level_11")
        self.item_two_37 = QtWidgets.QLabel(Board_Widget)
        self.item_two_37.setEnabled(True)
        self.item_two_37.setGeometry(QtCore.QRect(200, 650, 20, 18))
        self.item_two_37.setText("")
        self.item_two_37.setScaledContents(True)
        self.item_two_37.setObjectName("item_two_37")
        self.enemy_unit_3_3 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_3_3.setGeometry(QtCore.QRect(220, 240, 82, 82))
        self.enemy_unit_3_3.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_3_3.setText("")
        self.enemy_unit_3_3.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_3_3.setObjectName("enemy_unit_3_3")
        self.enemy_unit_2_1 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_2_1.setGeometry(QtCore.QRect(70, 130, 82, 82))
        self.enemy_unit_2_1.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_2_1.setText("")
        self.enemy_unit_2_1.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_2_1.setObjectName("enemy_unit_2_1")
        self.item_two_7 = QtWidgets.QLabel(Board_Widget)
        self.item_two_7.setEnabled(True)
        self.item_two_7.setGeometry(QtCore.QRect(650, 90, 20, 18))
        self.item_two_7.setText("")
        self.item_two_7.setScaledContents(True)
        self.item_two_7.setObjectName("item_two_7")
        self.level_31 = QtWidgets.QLabel(Board_Widget)
        self.level_31.setEnabled(True)
        self.level_31.setGeometry(QtCore.QRect(240, 460, 40, 15))
        self.level_31.setText("")
        self.level_31.setScaledContents(True)
        self.level_31.setObjectName("level_31")
        self.user_unit_2_2 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_2_2.setGeometry(QtCore.QRect(170, 580, 82, 82))
        self.user_unit_2_2.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_2_2.setText("")
        self.user_unit_2_2.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_2_2.setObjectName("user_unit_2_2")
        self.item_two_26 = QtWidgets.QLabel(Board_Widget)
        self.item_two_26.setEnabled(True)
        self.item_two_26.setGeometry(QtCore.QRect(500, 420, 20, 18))
        self.item_two_26.setText("")
        self.item_two_26.setScaledContents(True)
        self.item_two_26.setObjectName("item_two_26")
        self.line = QtWidgets.QFrame(Board_Widget)
        self.line.setGeometry(QtCore.QRect(0, 440, 850, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.level_47 = QtWidgets.QLabel(Board_Widget)
        self.level_47.setEnabled(True)
        self.level_47.setGeometry(QtCore.QRect(440, 680, 40, 15))
        self.level_47.setText("")
        self.level_47.setScaledContents(True)
        self.level_47.setObjectName("level_47")
        self.item_three_38 = QtWidgets.QLabel(Board_Widget)
        self.item_three_38.setEnabled(True)
        self.item_three_38.setGeometry(QtCore.QRect(320, 650, 20, 18))
        self.item_three_38.setText("")
        self.item_three_38.setScaledContents(True)
        self.item_three_38.setObjectName("item_three_38")
        self.item_one_55 = QtWidgets.QLabel(Board_Widget)
        self.item_one_55.setEnabled(True)
        self.item_one_55.setGeometry(QtCore.QRect(580, 870, 20, 18))
        self.item_one_55.setText("")
        self.item_one_55.setScaledContents(True)
        self.item_one_55.setObjectName("item_one_55")
        self.enemy_unit_1_3 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_1_3.setGeometry(QtCore.QRect(220, 20, 82, 82))
        self.enemy_unit_1_3.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_1_3.setText("")
        self.enemy_unit_1_3.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_1_3.setObjectName("enemy_unit_1_3")
        self.item_two_51 = QtWidgets.QLabel(Board_Widget)
        self.item_two_51.setEnabled(True)
        self.item_two_51.setGeometry(QtCore.QRect(200, 870, 20, 18))
        self.item_two_51.setText("")
        self.item_two_51.setScaledContents(True)
        self.item_two_51.setObjectName("item_two_51")
        self.user_unit_3_2 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_3_2.setGeometry(QtCore.QRect(120, 690, 82, 82))
        self.user_unit_3_2.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_3_2.setText("")
        self.user_unit_3_2.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_3_2.setObjectName("user_unit_3_2")
        self.enemy_unit_1_4 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_1_4.setGeometry(QtCore.QRect(320, 20, 82, 82))
        self.enemy_unit_1_4.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_1_4.setText("")
        self.enemy_unit_1_4.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_1_4.setObjectName("enemy_unit_1_4")
        self.item_three_20 = QtWidgets.QLabel(Board_Widget)
        self.item_three_20.setEnabled(True)
        self.item_three_20.setGeometry(QtCore.QRect(570, 310, 20, 18))
        self.item_three_20.setText("")
        self.item_three_20.setScaledContents(True)
        self.item_three_20.setObjectName("item_three_20")
        self.item_three_31 = QtWidgets.QLabel(Board_Widget)
        self.item_three_31.setEnabled(True)
        self.item_three_31.setGeometry(QtCore.QRect(270, 540, 20, 18))
        self.item_three_31.setText("")
        self.item_three_31.setScaledContents(True)
        self.item_three_31.setObjectName("item_three_31")
        self.user_unit_2_1 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_2_1.setGeometry(QtCore.QRect(70, 580, 82, 82))
        self.user_unit_2_1.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_2_1.setText("")
        self.user_unit_2_1.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_2_1.setObjectName("user_unit_2_1")
        self.item_one_17 = QtWidgets.QLabel(Board_Widget)
        self.item_one_17.setEnabled(True)
        self.item_one_17.setGeometry(QtCore.QRect(230, 310, 20, 18))
        self.item_one_17.setText("")
        self.item_one_17.setScaledContents(True)
        self.item_one_17.setObjectName("item_one_17")
        self.level_28 = QtWidgets.QLabel(Board_Widget)
        self.level_28.setEnabled(True)
        self.level_28.setGeometry(QtCore.QRect(690, 340, 40, 15))
        self.level_28.setText("")
        self.level_28.setScaledContents(True)
        self.level_28.setObjectName("level_28")
        self.level_29 = QtWidgets.QLabel(Board_Widget)
        self.level_29.setEnabled(True)
        self.level_29.setGeometry(QtCore.QRect(40, 460, 40, 15))
        self.level_29.setText("")
        self.level_29.setScaledContents(True)
        self.level_29.setObjectName("level_29")
        self.item_one_51 = QtWidgets.QLabel(Board_Widget)
        self.item_one_51.setEnabled(True)
        self.item_one_51.setGeometry(QtCore.QRect(180, 870, 20, 18))
        self.item_one_51.setText("")
        self.item_one_51.setScaledContents(True)
        self.item_one_51.setObjectName("item_one_51")
        self.user_unit_2_5 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_2_5.setGeometry(QtCore.QRect(470, 580, 82, 82))
        self.user_unit_2_5.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_2_5.setText("")
        self.user_unit_2_5.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_2_5.setObjectName("user_unit_2_5")
        self.item_three_54 = QtWidgets.QLabel(Board_Widget)
        self.item_three_54.setEnabled(True)
        self.item_three_54.setGeometry(QtCore.QRect(520, 870, 20, 18))
        self.item_three_54.setText("")
        self.item_three_54.setScaledContents(True)
        self.item_three_54.setObjectName("item_three_54")
        self.level_18 = QtWidgets.QLabel(Board_Widget)
        self.level_18.setEnabled(True)
        self.level_18.setGeometry(QtCore.QRect(340, 230, 40, 15))
        self.level_18.setText("")
        self.level_18.setScaledContents(True)
        self.level_18.setObjectName("level_18")
        self.enemy_unit_3_6 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_3_6.setGeometry(QtCore.QRect(520, 240, 82, 82))
        self.enemy_unit_3_6.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_3_6.setText("")
        self.enemy_unit_3_6.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_3_6.setObjectName("enemy_unit_3_6")
        self.item_one_19 = QtWidgets.QLabel(Board_Widget)
        self.item_one_19.setEnabled(True)
        self.item_one_19.setGeometry(QtCore.QRect(430, 310, 20, 18))
        self.item_one_19.setText("")
        self.item_one_19.setScaledContents(True)
        self.item_one_19.setObjectName("item_one_19")
        self.enemy_unit_4_4 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_4_4.setGeometry(QtCore.QRect(370, 350, 82, 82))
        self.enemy_unit_4_4.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_4_4.setText("")
        self.enemy_unit_4_4.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_4_4.setObjectName("enemy_unit_4_4")
        self.item_three_23 = QtWidgets.QLabel(Board_Widget)
        self.item_three_23.setEnabled(True)
        self.item_three_23.setGeometry(QtCore.QRect(220, 420, 20, 18))
        self.item_three_23.setText("")
        self.item_three_23.setScaledContents(True)
        self.item_three_23.setObjectName("item_three_23")
        self.level_41 = QtWidgets.QLabel(Board_Widget)
        self.level_41.setEnabled(True)
        self.level_41.setGeometry(QtCore.QRect(590, 570, 40, 15))
        self.level_41.setText("")
        self.level_41.setScaledContents(True)
        self.level_41.setObjectName("level_41")
        self.enemy_win_indicator = QtWidgets.QLabel(Board_Widget)
        self.enemy_win_indicator.setGeometry(QtCore.QRect(780, 10, 48, 13))
        self.enemy_win_indicator.setStyleSheet("color: white;")
        self.enemy_win_indicator.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.enemy_win_indicator.setObjectName("enemy_win_indicator")
        self.level_27 = QtWidgets.QLabel(Board_Widget)
        self.level_27.setEnabled(True)
        self.level_27.setGeometry(QtCore.QRect(590, 340, 40, 15))
        self.level_27.setText("")
        self.level_27.setScaledContents(True)
        self.level_27.setObjectName("level_27")
        self.item_one_10 = QtWidgets.QLabel(Board_Widget)
        self.item_one_10.setEnabled(True)
        self.item_one_10.setGeometry(QtCore.QRect(280, 200, 20, 18))
        self.item_one_10.setText("")
        self.item_one_10.setScaledContents(True)
        self.item_one_10.setObjectName("item_one_10")
        self.item_one_21 = QtWidgets.QLabel(Board_Widget)
        self.item_one_21.setEnabled(True)
        self.item_one_21.setGeometry(QtCore.QRect(630, 310, 20, 18))
        self.item_one_21.setText("")
        self.item_one_21.setScaledContents(True)
        self.item_one_21.setObjectName("item_one_21")
        self.item_two_40 = QtWidgets.QLabel(Board_Widget)
        self.item_two_40.setEnabled(True)
        self.item_two_40.setGeometry(QtCore.QRect(500, 650, 20, 18))
        self.item_two_40.setText("")
        self.item_two_40.setScaledContents(True)
        self.item_two_40.setObjectName("item_two_40")
        self.user_unit_3_4 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_3_4.setGeometry(QtCore.QRect(320, 690, 82, 82))
        self.user_unit_3_4.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_3_4.setText("")
        self.user_unit_3_4.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_3_4.setObjectName("user_unit_3_4")
        self.item_three_36 = QtWidgets.QLabel(Board_Widget)
        self.item_three_36.setEnabled(True)
        self.item_three_36.setGeometry(QtCore.QRect(120, 650, 20, 18))
        self.item_three_36.setText("")
        self.item_three_36.setScaledContents(True)
        self.item_three_36.setObjectName("item_three_36")
        self.user_unit_2_6 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_2_6.setGeometry(QtCore.QRect(570, 580, 82, 82))
        self.user_unit_2_6.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_2_6.setText("")
        self.user_unit_2_6.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_2_6.setObjectName("user_unit_2_6")
        self.user_unit_1_6 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_1_6.setGeometry(QtCore.QRect(520, 470, 82, 82))
        self.user_unit_1_6.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_1_6.setText("")
        self.user_unit_1_6.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_1_6.setObjectName("user_unit_1_6")
        self.user_unit_1_2 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_1_2.setGeometry(QtCore.QRect(120, 470, 82, 82))
        self.user_unit_1_2.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_1_2.setText("")
        self.user_unit_1_2.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_1_2.setObjectName("user_unit_1_2")
        self.item_one_53 = QtWidgets.QLabel(Board_Widget)
        self.item_one_53.setEnabled(True)
        self.item_one_53.setGeometry(QtCore.QRect(380, 870, 20, 18))
        self.item_one_53.setText("")
        self.item_one_53.setScaledContents(True)
        self.item_one_53.setObjectName("item_one_53")
        self.user_unit_3_5 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_3_5.setGeometry(QtCore.QRect(420, 690, 82, 82))
        self.user_unit_3_5.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_3_5.setText("")
        self.user_unit_3_5.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_3_5.setObjectName("user_unit_3_5")
        self.item_one_3 = QtWidgets.QLabel(Board_Widget)
        self.item_one_3.setEnabled(True)
        self.item_one_3.setGeometry(QtCore.QRect(230, 90, 20, 18))
        self.item_one_3.setText("")
        self.item_one_3.setScaledContents(True)
        self.item_one_3.setObjectName("item_one_3")
        self.item_one_25 = QtWidgets.QLabel(Board_Widget)
        self.item_one_25.setEnabled(True)
        self.item_one_25.setGeometry(QtCore.QRect(380, 420, 20, 18))
        self.item_one_25.setText("")
        self.item_one_25.setScaledContents(True)
        self.item_one_25.setObjectName("item_one_25")
        self.item_two_10 = QtWidgets.QLabel(Board_Widget)
        self.item_two_10.setEnabled(True)
        self.item_two_10.setGeometry(QtCore.QRect(300, 200, 20, 18))
        self.item_two_10.setText("")
        self.item_two_10.setScaledContents(True)
        self.item_two_10.setObjectName("item_two_10")
        self.item_two_23 = QtWidgets.QLabel(Board_Widget)
        self.item_two_23.setEnabled(True)
        self.item_two_23.setGeometry(QtCore.QRect(200, 420, 20, 18))
        self.item_two_23.setText("")
        self.item_two_23.setScaledContents(True)
        self.item_two_23.setObjectName("item_two_23")
        self.item_two_28 = QtWidgets.QLabel(Board_Widget)
        self.item_two_28.setEnabled(True)
        self.item_two_28.setGeometry(QtCore.QRect(700, 420, 20, 18))
        self.item_two_28.setText("")
        self.item_two_28.setScaledContents(True)
        self.item_two_28.setObjectName("item_two_28")
        self.level_9 = QtWidgets.QLabel(Board_Widget)
        self.level_9.setEnabled(True)
        self.level_9.setGeometry(QtCore.QRect(190, 120, 40, 15))
        self.level_9.setText("")
        self.level_9.setScaledContents(True)
        self.level_9.setObjectName("level_9")
        self.item_three_51 = QtWidgets.QLabel(Board_Widget)
        self.item_three_51.setEnabled(True)
        self.item_three_51.setGeometry(QtCore.QRect(220, 870, 20, 18))
        self.item_three_51.setText("")
        self.item_three_51.setScaledContents(True)
        self.item_three_51.setObjectName("item_three_51")
        self.level_53 = QtWidgets.QLabel(Board_Widget)
        self.level_53.setEnabled(True)
        self.level_53.setGeometry(QtCore.QRect(390, 790, 40, 15))
        self.level_53.setText("")
        self.level_53.setScaledContents(True)
        self.level_53.setObjectName("level_53")
        self.item_one_56 = QtWidgets.QLabel(Board_Widget)
        self.item_one_56.setEnabled(True)
        self.item_one_56.setGeometry(QtCore.QRect(680, 870, 20, 18))
        self.item_one_56.setText("")
        self.item_one_56.setScaledContents(True)
        self.item_one_56.setObjectName("item_one_56")
        self.item_one_8 = QtWidgets.QLabel(Board_Widget)
        self.item_one_8.setEnabled(True)
        self.item_one_8.setGeometry(QtCore.QRect(80, 200, 20, 18))
        self.item_one_8.setText("")
        self.item_one_8.setScaledContents(True)
        self.item_one_8.setObjectName("item_one_8")
        self.item_three_53 = QtWidgets.QLabel(Board_Widget)
        self.item_three_53.setEnabled(True)
        self.item_three_53.setGeometry(QtCore.QRect(420, 870, 20, 18))
        self.item_three_53.setText("")
        self.item_three_53.setScaledContents(True)
        self.item_three_53.setObjectName("item_three_53")
        self.user_unit_4_5 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_4_5.setGeometry(QtCore.QRect(470, 800, 82, 82))
        self.user_unit_4_5.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_4_5.setText("")
        self.user_unit_4_5.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_4_5.setObjectName("user_unit_4_5")
        self.item_one_24 = QtWidgets.QLabel(Board_Widget)
        self.item_one_24.setEnabled(True)
        self.item_one_24.setGeometry(QtCore.QRect(280, 420, 20, 18))
        self.item_one_24.setText("")
        self.item_one_24.setScaledContents(True)
        self.item_one_24.setObjectName("item_one_24")
        self.item_three_47 = QtWidgets.QLabel(Board_Widget)
        self.item_three_47.setEnabled(True)
        self.item_three_47.setGeometry(QtCore.QRect(470, 760, 20, 18))
        self.item_three_47.setText("")
        self.item_three_47.setScaledContents(True)
        self.item_three_47.setObjectName("item_three_47")
        self.item_three_48 = QtWidgets.QLabel(Board_Widget)
        self.item_three_48.setEnabled(True)
        self.item_three_48.setGeometry(QtCore.QRect(570, 760, 20, 18))
        self.item_three_48.setText("")
        self.item_three_48.setScaledContents(True)
        self.item_three_48.setObjectName("item_three_48")
        self.item_two_36 = QtWidgets.QLabel(Board_Widget)
        self.item_two_36.setEnabled(True)
        self.item_two_36.setGeometry(QtCore.QRect(100, 650, 20, 18))
        self.item_two_36.setText("")
        self.item_two_36.setScaledContents(True)
        self.item_two_36.setObjectName("item_two_36")
        self.user_unit_4_4 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_4_4.setGeometry(QtCore.QRect(370, 800, 82, 82))
        self.user_unit_4_4.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_4_4.setText("")
        self.user_unit_4_4.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_4_4.setObjectName("user_unit_4_4")
        self.item_three_39 = QtWidgets.QLabel(Board_Widget)
        self.item_three_39.setEnabled(True)
        self.item_three_39.setGeometry(QtCore.QRect(420, 650, 20, 18))
        self.item_three_39.setText("")
        self.item_three_39.setScaledContents(True)
        self.item_three_39.setObjectName("item_three_39")
        self.user_win_indicator = QtWidgets.QLabel(Board_Widget)
        self.user_win_indicator.setGeometry(QtCore.QRect(780, 460, 47, 13))
        self.user_win_indicator.setStyleSheet("color: white;")
        self.user_win_indicator.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.user_win_indicator.setObjectName("user_win_indicator")
        self.enemy_unit_4_1 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_4_1.setGeometry(QtCore.QRect(70, 350, 82, 82))
        self.enemy_unit_4_1.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_4_1.setText("")
        self.enemy_unit_4_1.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_4_1.setObjectName("enemy_unit_4_1")
        self.item_two_18 = QtWidgets.QLabel(Board_Widget)
        self.item_two_18.setEnabled(True)
        self.item_two_18.setGeometry(QtCore.QRect(350, 310, 20, 18))
        self.item_two_18.setText("")
        self.item_two_18.setScaledContents(True)
        self.item_two_18.setObjectName("item_two_18")
        self.item_three_11 = QtWidgets.QLabel(Board_Widget)
        self.item_three_11.setEnabled(True)
        self.item_three_11.setGeometry(QtCore.QRect(420, 200, 20, 18))
        self.item_three_11.setText("")
        self.item_three_11.setScaledContents(True)
        self.item_three_11.setObjectName("item_three_11")
        self.level_39 = QtWidgets.QLabel(Board_Widget)
        self.level_39.setEnabled(True)
        self.level_39.setGeometry(QtCore.QRect(390, 570, 40, 15))
        self.level_39.setText("")
        self.level_39.setScaledContents(True)
        self.level_39.setObjectName("level_39")
        self.level_10 = QtWidgets.QLabel(Board_Widget)
        self.level_10.setEnabled(True)
        self.level_10.setGeometry(QtCore.QRect(290, 120, 40, 15))
        self.level_10.setText("")
        self.level_10.setScaledContents(True)
        self.level_10.setObjectName("level_10")
        self.level_24 = QtWidgets.QLabel(Board_Widget)
        self.level_24.setEnabled(True)
        self.level_24.setGeometry(QtCore.QRect(290, 340, 40, 15))
        self.level_24.setText("")
        self.level_24.setScaledContents(True)
        self.level_24.setObjectName("level_24")
        self.item_three_27 = QtWidgets.QLabel(Board_Widget)
        self.item_three_27.setEnabled(True)
        self.item_three_27.setGeometry(QtCore.QRect(620, 420, 20, 18))
        self.item_three_27.setText("")
        self.item_three_27.setScaledContents(True)
        self.item_three_27.setObjectName("item_three_27")
        self.user_unit_1_5 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_1_5.setGeometry(QtCore.QRect(420, 470, 82, 82))
        self.user_unit_1_5.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_1_5.setText("")
        self.user_unit_1_5.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_1_5.setObjectName("user_unit_1_5")
        self.enemy_unit_2_2 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_2_2.setGeometry(QtCore.QRect(170, 130, 82, 82))
        self.enemy_unit_2_2.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_2_2.setText("")
        self.enemy_unit_2_2.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_2_2.setObjectName("enemy_unit_2_2")
        self.item_one_46 = QtWidgets.QLabel(Board_Widget)
        self.item_one_46.setEnabled(True)
        self.item_one_46.setGeometry(QtCore.QRect(330, 760, 20, 18))
        self.item_one_46.setText("")
        self.item_one_46.setScaledContents(True)
        self.item_one_46.setObjectName("item_one_46")
        self.level_49 = QtWidgets.QLabel(Board_Widget)
        self.level_49.setEnabled(True)
        self.level_49.setGeometry(QtCore.QRect(640, 680, 40, 15))
        self.level_49.setText("")
        self.level_49.setScaledContents(True)
        self.level_49.setObjectName("level_49")
        self.level_8 = QtWidgets.QLabel(Board_Widget)
        self.level_8.setEnabled(True)
        self.level_8.setGeometry(QtCore.QRect(90, 120, 40, 15))
        self.level_8.setText("")
        self.level_8.setScaledContents(True)
        self.level_8.setObjectName("level_8")
        self.item_two_29 = QtWidgets.QLabel(Board_Widget)
        self.item_two_29.setEnabled(True)
        self.item_two_29.setGeometry(QtCore.QRect(50, 540, 20, 18))
        self.item_two_29.setText("")
        self.item_two_29.setScaledContents(True)
        self.item_two_29.setObjectName("item_two_29")
        self.item_three_6 = QtWidgets.QLabel(Board_Widget)
        self.item_three_6.setEnabled(True)
        self.item_three_6.setGeometry(QtCore.QRect(570, 90, 20, 18))
        self.item_three_6.setText("")
        self.item_three_6.setScaledContents(True)
        self.item_three_6.setObjectName("item_three_6")
        self.item_two_19 = QtWidgets.QLabel(Board_Widget)
        self.item_two_19.setEnabled(True)
        self.item_two_19.setGeometry(QtCore.QRect(450, 310, 20, 18))
        self.item_two_19.setText("")
        self.item_two_19.setScaledContents(True)
        self.item_two_19.setObjectName("item_two_19")
        self.level_51 = QtWidgets.QLabel(Board_Widget)
        self.level_51.setEnabled(True)
        self.level_51.setGeometry(QtCore.QRect(190, 790, 40, 15))
        self.level_51.setText("")
        self.level_51.setScaledContents(True)
        self.level_51.setObjectName("level_51")
        self.item_three_55 = QtWidgets.QLabel(Board_Widget)
        self.item_three_55.setEnabled(True)
        self.item_three_55.setGeometry(QtCore.QRect(620, 870, 20, 18))
        self.item_three_55.setText("")
        self.item_three_55.setScaledContents(True)
        self.item_three_55.setObjectName("item_three_55")
        self.item_two_49 = QtWidgets.QLabel(Board_Widget)
        self.item_two_49.setEnabled(True)
        self.item_two_49.setGeometry(QtCore.QRect(650, 760, 20, 18))
        self.item_two_49.setText("")
        self.item_two_49.setScaledContents(True)
        self.item_two_49.setObjectName("item_two_49")
        self.item_one_39 = QtWidgets.QLabel(Board_Widget)
        self.item_one_39.setEnabled(True)
        self.item_one_39.setGeometry(QtCore.QRect(380, 650, 20, 18))
        self.item_one_39.setText("")
        self.item_one_39.setScaledContents(True)
        self.item_one_39.setObjectName("item_one_39")
        self.item_three_25 = QtWidgets.QLabel(Board_Widget)
        self.item_three_25.setEnabled(True)
        self.item_three_25.setGeometry(QtCore.QRect(420, 420, 20, 18))
        self.item_three_25.setText("")
        self.item_three_25.setScaledContents(True)
        self.item_three_25.setObjectName("item_three_25")
        self.item_one_26 = QtWidgets.QLabel(Board_Widget)
        self.item_one_26.setEnabled(True)
        self.item_one_26.setGeometry(QtCore.QRect(480, 420, 20, 18))
        self.item_one_26.setText("")
        self.item_one_26.setScaledContents(True)
        self.item_one_26.setObjectName("item_one_26")
        self.item_one_7 = QtWidgets.QLabel(Board_Widget)
        self.item_one_7.setEnabled(True)
        self.item_one_7.setGeometry(QtCore.QRect(630, 90, 20, 18))
        self.item_one_7.setText("")
        self.item_one_7.setScaledContents(True)
        self.item_one_7.setObjectName("item_one_7")
        self.item_one_42 = QtWidgets.QLabel(Board_Widget)
        self.item_one_42.setEnabled(True)
        self.item_one_42.setGeometry(QtCore.QRect(680, 650, 20, 18))
        self.item_one_42.setText("")
        self.item_one_42.setScaledContents(True)
        self.item_one_42.setObjectName("item_one_42")
        self.level_37 = QtWidgets.QLabel(Board_Widget)
        self.level_37.setEnabled(True)
        self.level_37.setGeometry(QtCore.QRect(190, 570, 40, 15))
        self.level_37.setText("")
        self.level_37.setScaledContents(True)
        self.level_37.setObjectName("level_37")
        self.enemy_unit_2_5 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_2_5.setGeometry(QtCore.QRect(470, 130, 82, 82))
        self.enemy_unit_2_5.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_2_5.setText("")
        self.enemy_unit_2_5.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_2_5.setObjectName("enemy_unit_2_5")
        self.level_42 = QtWidgets.QLabel(Board_Widget)
        self.level_42.setEnabled(True)
        self.level_42.setGeometry(QtCore.QRect(690, 570, 40, 15))
        self.level_42.setText("")
        self.level_42.setScaledContents(True)
        self.level_42.setObjectName("level_42")
        self.item_one_35 = QtWidgets.QLabel(Board_Widget)
        self.item_one_35.setEnabled(True)
        self.item_one_35.setGeometry(QtCore.QRect(630, 540, 20, 18))
        self.item_one_35.setText("")
        self.item_one_35.setScaledContents(True)
        self.item_one_35.setObjectName("item_one_35")
        self.user_unit_2_4 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_2_4.setGeometry(QtCore.QRect(370, 580, 82, 82))
        self.user_unit_2_4.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_2_4.setText("")
        self.user_unit_2_4.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_2_4.setObjectName("user_unit_2_4")
        self.item_one_14 = QtWidgets.QLabel(Board_Widget)
        self.item_one_14.setEnabled(True)
        self.item_one_14.setGeometry(QtCore.QRect(680, 200, 20, 18))
        self.item_one_14.setText("")
        self.item_one_14.setScaledContents(True)
        self.item_one_14.setObjectName("item_one_14")
        self.item_three_46 = QtWidgets.QLabel(Board_Widget)
        self.item_three_46.setEnabled(True)
        self.item_three_46.setGeometry(QtCore.QRect(370, 760, 20, 18))
        self.item_three_46.setText("")
        self.item_three_46.setScaledContents(True)
        self.item_three_46.setObjectName("item_three_46")
        self.level = QtWidgets.QLabel(Board_Widget)
        self.level.setEnabled(True)
        self.level.setGeometry(QtCore.QRect(40, 10, 40, 15))
        self.level.setText("")
        self.level.setScaledContents(True)
        self.level.setObjectName("level")
        self.item_one_2 = QtWidgets.QLabel(Board_Widget)
        self.item_one_2.setEnabled(True)
        self.item_one_2.setGeometry(QtCore.QRect(130, 90, 20, 18))
        self.item_one_2.setText("")
        self.item_one_2.setScaledContents(True)
        self.item_one_2.setObjectName("item_one_2")
        self.item_one_49 = QtWidgets.QLabel(Board_Widget)
        self.item_one_49.setEnabled(True)
        self.item_one_49.setGeometry(QtCore.QRect(630, 760, 20, 18))
        self.item_one_49.setText("")
        self.item_one_49.setScaledContents(True)
        self.item_one_49.setObjectName("item_one_49")
        self.item_three_34 = QtWidgets.QLabel(Board_Widget)
        self.item_three_34.setEnabled(True)
        self.item_three_34.setGeometry(QtCore.QRect(570, 540, 20, 18))
        self.item_three_34.setText("")
        self.item_three_34.setScaledContents(True)
        self.item_three_34.setObjectName("item_three_34")
        self.level_30 = QtWidgets.QLabel(Board_Widget)
        self.level_30.setEnabled(True)
        self.level_30.setGeometry(QtCore.QRect(140, 460, 40, 15))
        self.level_30.setText("")
        self.level_30.setScaledContents(True)
        self.level_30.setObjectName("level_30")
        self.user_unit_4_7 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_4_7.setGeometry(QtCore.QRect(670, 800, 82, 82))
        self.user_unit_4_7.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_4_7.setText("")
        self.user_unit_4_7.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_4_7.setObjectName("user_unit_4_7")
        self.item_one_44 = QtWidgets.QLabel(Board_Widget)
        self.item_one_44.setEnabled(True)
        self.item_one_44.setGeometry(QtCore.QRect(130, 760, 20, 18))
        self.item_one_44.setText("")
        self.item_one_44.setScaledContents(True)
        self.item_one_44.setObjectName("item_one_44")
        self.level_4 = QtWidgets.QLabel(Board_Widget)
        self.level_4.setEnabled(True)
        self.level_4.setGeometry(QtCore.QRect(340, 10, 40, 15))
        self.level_4.setText("")
        self.level_4.setScaledContents(True)
        self.level_4.setObjectName("level_4")
        self.enemy_unit_3_1 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_3_1.setGeometry(QtCore.QRect(20, 240, 82, 82))
        self.enemy_unit_3_1.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_3_1.setText("")
        self.enemy_unit_3_1.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_3_1.setObjectName("enemy_unit_3_1")
        self.item_one_20 = QtWidgets.QLabel(Board_Widget)
        self.item_one_20.setEnabled(True)
        self.item_one_20.setGeometry(QtCore.QRect(530, 310, 20, 18))
        self.item_one_20.setText("")
        self.item_one_20.setScaledContents(True)
        self.item_one_20.setObjectName("item_one_20")
        self.user_unit_4_1 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_4_1.setGeometry(QtCore.QRect(70, 800, 82, 82))
        self.user_unit_4_1.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_4_1.setText("")
        self.user_unit_4_1.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_4_1.setObjectName("user_unit_4_1")
        self.level_35 = QtWidgets.QLabel(Board_Widget)
        self.level_35.setEnabled(True)
        self.level_35.setGeometry(QtCore.QRect(640, 460, 40, 15))
        self.level_35.setText("")
        self.level_35.setScaledContents(True)
        self.level_35.setObjectName("level_35")
        self.item_three_40 = QtWidgets.QLabel(Board_Widget)
        self.item_three_40.setEnabled(True)
        self.item_three_40.setGeometry(QtCore.QRect(520, 650, 20, 18))
        self.item_three_40.setText("")
        self.item_three_40.setScaledContents(True)
        self.item_three_40.setObjectName("item_three_40")
        self.enemy_unit_3_4 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_3_4.setGeometry(QtCore.QRect(320, 240, 82, 82))
        self.enemy_unit_3_4.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_3_4.setText("")
        self.enemy_unit_3_4.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_3_4.setObjectName("enemy_unit_3_4")
        self.item_three_56 = QtWidgets.QLabel(Board_Widget)
        self.item_three_56.setEnabled(True)
        self.item_three_56.setGeometry(QtCore.QRect(720, 870, 20, 18))
        self.item_three_56.setText("")
        self.item_three_56.setScaledContents(True)
        self.item_three_56.setObjectName("item_three_56")
        self.item_two_24 = QtWidgets.QLabel(Board_Widget)
        self.item_two_24.setEnabled(True)
        self.item_two_24.setGeometry(QtCore.QRect(300, 420, 20, 18))
        self.item_two_24.setText("")
        self.item_two_24.setScaledContents(True)
        self.item_two_24.setObjectName("item_two_24")
        self.level_54 = QtWidgets.QLabel(Board_Widget)
        self.level_54.setEnabled(True)
        self.level_54.setGeometry(QtCore.QRect(490, 790, 40, 15))
        self.level_54.setText("")
        self.level_54.setScaledContents(True)
        self.level_54.setObjectName("level_54")
        self.item_two_6 = QtWidgets.QLabel(Board_Widget)
        self.item_two_6.setEnabled(True)
        self.item_two_6.setGeometry(QtCore.QRect(550, 90, 20, 18))
        self.item_two_6.setText("")
        self.item_two_6.setScaledContents(True)
        self.item_two_6.setObjectName("item_two_6")
        self.item_two_56 = QtWidgets.QLabel(Board_Widget)
        self.item_two_56.setEnabled(True)
        self.item_two_56.setGeometry(QtCore.QRect(700, 870, 20, 18))
        self.item_two_56.setText("")
        self.item_two_56.setScaledContents(True)
        self.item_two_56.setObjectName("item_two_56")
        self.item_three_8 = QtWidgets.QLabel(Board_Widget)
        self.item_three_8.setEnabled(True)
        self.item_three_8.setGeometry(QtCore.QRect(120, 200, 20, 18))
        self.item_three_8.setText("")
        self.item_three_8.setScaledContents(True)
        self.item_three_8.setObjectName("item_three_8")
        self.item_three = QtWidgets.QLabel(Board_Widget)
        self.item_three.setEnabled(True)
        self.item_three.setGeometry(QtCore.QRect(70, 90, 20, 18))
        self.item_three.setText("")
        self.item_three.setScaledContents(True)
        self.item_three.setObjectName("item_three")
        self.item_one_36 = QtWidgets.QLabel(Board_Widget)
        self.item_one_36.setEnabled(True)
        self.item_one_36.setGeometry(QtCore.QRect(80, 650, 20, 18))
        self.item_one_36.setText("")
        self.item_one_36.setScaledContents(True)
        self.item_one_36.setObjectName("item_one_36")
        self.level_23 = QtWidgets.QLabel(Board_Widget)
        self.level_23.setEnabled(True)
        self.level_23.setGeometry(QtCore.QRect(190, 340, 40, 15))
        self.level_23.setText("")
        self.level_23.setScaledContents(True)
        self.level_23.setObjectName("level_23")
        self.item_two_21 = QtWidgets.QLabel(Board_Widget)
        self.item_two_21.setEnabled(True)
        self.item_two_21.setGeometry(QtCore.QRect(650, 310, 20, 18))
        self.item_two_21.setText("")
        self.item_two_21.setScaledContents(True)
        self.item_two_21.setObjectName("item_two_21")
        self.item_one_15 = QtWidgets.QLabel(Board_Widget)
        self.item_one_15.setEnabled(True)
        self.item_one_15.setGeometry(QtCore.QRect(30, 310, 20, 18))
        self.item_one_15.setText("")
        self.item_one_15.setScaledContents(True)
        self.item_one_15.setObjectName("item_one_15")
        self.item_three_17 = QtWidgets.QLabel(Board_Widget)
        self.item_three_17.setEnabled(True)
        self.item_three_17.setGeometry(QtCore.QRect(270, 310, 20, 18))
        self.item_three_17.setText("")
        self.item_three_17.setScaledContents(True)
        self.item_three_17.setObjectName("item_three_17")
        self.enemy_unit_4_6 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_4_6.setGeometry(QtCore.QRect(570, 350, 82, 82))
        self.enemy_unit_4_6.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_4_6.setText("")
        self.enemy_unit_4_6.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_4_6.setObjectName("enemy_unit_4_6")
        self.item_two_9 = QtWidgets.QLabel(Board_Widget)
        self.item_two_9.setEnabled(True)
        self.item_two_9.setGeometry(QtCore.QRect(200, 200, 20, 18))
        self.item_two_9.setText("")
        self.item_two_9.setScaledContents(True)
        self.item_two_9.setObjectName("item_two_9")
        self.user_unit_2_7 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_2_7.setGeometry(QtCore.QRect(670, 580, 82, 82))
        self.user_unit_2_7.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_2_7.setText("")
        self.user_unit_2_7.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_2_7.setObjectName("user_unit_2_7")
        self.enemy_unit_3_7 = QtWidgets.QPushButton(Board_Widget)
        self.enemy_unit_3_7.setGeometry(QtCore.QRect(620, 240, 82, 82))
        self.enemy_unit_3_7.setStyleSheet("QPushButton{\n"
                                          "background: #123040\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #195778;\n"
                                          "}")
        self.enemy_unit_3_7.setText("")
        self.enemy_unit_3_7.setIconSize(QtCore.QSize(75, 75))
        self.enemy_unit_3_7.setObjectName("enemy_unit_3_7")
        self.user_unit_1_1 = QtWidgets.QPushButton(Board_Widget)
        self.user_unit_1_1.setGeometry(QtCore.QRect(20, 470, 82, 82))
        self.user_unit_1_1.setAutoFillBackground(False)
        self.user_unit_1_1.setStyleSheet("QPushButton{\n"
                                         "background: #123040\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: #195778;\n"
                                         "}")
        self.user_unit_1_1.setText("")
        self.user_unit_1_1.setIconSize(QtCore.QSize(75, 75))
        self.user_unit_1_1.setObjectName("user_unit_1_1")
        self.level_33 = QtWidgets.QLabel(Board_Widget)
        self.level_33.setEnabled(True)
        self.level_33.setGeometry(QtCore.QRect(440, 460, 40, 15))
        self.level_33.setText("")
        self.level_33.setScaledContents(True)
        self.level_33.setObjectName("level_33")
        self.item_one_6 = QtWidgets.QLabel(Board_Widget)
        self.item_one_6.setEnabled(True)
        self.item_one_6.setGeometry(QtCore.QRect(530, 90, 20, 18))
        self.item_one_6.setText("")
        self.item_one_6.setScaledContents(True)
        self.item_one_6.setObjectName("item_one_6")

        if state == "new":
            pass
        else:
            current_board_state = state.split(",")
            enemy = None
            user = None
            for position in current_board_state:
                if position[0] == "e":
                    if enemy == None:
                        enemy = position
                    else:
                        enemy = enemy + "," + position
                    position_information = position.split("|")
                    button = getattr(self, f"enemy_unit_{position[1]}_{position[3]}")
                    if position[1] == "1":
                        if not position[3] == "1":
                            level_position = int(position[3])
                    elif position[1] == "2":
                        level_position = int(position[3]) + 7
                    elif position[1] == "3":
                        level_position = int(position[3]) + 14
                    elif position[1] == "4":
                        level_position = int(position[3]) + 21

                    if not position_information[0] == "e1_1":
                        level_label = getattr(self, f"level_{level_position}")
                        item_one_label = getattr(self, f"item_one_{level_position}")
                        item_two_label = getattr(self, f"item_two_{level_position}")
                        item_three_label = getattr(self, f"item_three_{level_position}")

                elif position[0] == "u":
                    if user == None:
                        user = position
                    else:
                        user = user + "," + position
                    position_information = position.split("|")
                    button = getattr(self, f"user_unit_{position[1]}_{position[3]}")
                    if position[1] == "1":
                        level_position = int(position[3]) + 28
                    elif position[1] == "2":
                        level_position = int(position[3]) + 35
                    elif position[1] == "3":
                        level_position = int(position[3]) + 42
                    elif position[1] == "4":
                        level_position = int(position[3]) + 49

                    level_label = getattr(self, f"level_{level_position}")
                    item_one_label = getattr(self, f"item_one_{level_position}")
                    item_two_label = getattr(self, f"item_two_{level_position}")
                    item_three_label = getattr(self, f"item_three_{level_position}")

                image_path = f"image/TFT9/CHAMPIONS/tft9_{position_information[1]}_mobile.tft_set9.png"

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                button.setIcon(icon)

                if position_information[0] == "e1_1":
                    if position_information[2] == "1":
                        self.level.setPixmap(QtGui.QPixmap("image/One.png"))
                    elif position_information[2] == "2":
                            self.level.setPixmap(QtGui.QPixmap("image/Two.png"))
                    elif position_information[2] == "3":
                        self.level.setPixmap(QtGui.QPixmap("image/Three.png"))

                    if not position_information[3] == "null":
                        remove_space = position_information[3].replace(" ","_")
                        final_information = remove_space.replace("'","")
                        final_information = final_information.lower()

                        if "radiant" in final_information:
                            item_one_image = f"image/Items/radiant/{final_information}.png"
                            self.item_one.setPixmap(QtGui.QPixmap(item_one_image))
                        elif "emblem" in final_information:
                            embelm_path = final_information.replace("_emblem", "")
                            item_one_image = f"image/Items/trait/{embelm_path}.tft_set9.png"
                            self.item_one.setPixmap(QtGui.QPixmap(item_one_image))
                        else:
                            item_one_image = f"image/Items/standard/{final_information}.png"

                            if os.path.isfile(item_one_image):
                                self.item_one.setPixmap(QtGui.QPixmap(item_one_image))
                            else:
                                item_one_image = f"image/Items/ornn/{final_information}.png"
                                self.item_one.setPixmap(QtGui.QPixmap(item_one_image))

                    if not position_information[4] == "null":

                        remove_space = position_information[4].replace(" ", "_")
                        final_information = remove_space.replace("'", "")
                        final_information = final_information.lower()

                        if "radiant" in final_information:
                            item_two_image = f"image/Items/radiant/{final_information}.png"
                            self.item_two.setPixmap(QtGui.QPixmap(item_two_image))
                        elif "emblem" in final_information:
                            embelm_path = final_information.replace("_emblem", "")
                            item_two_image = f"image/Items/trait/{embelm_path}.tft_set9.png"
                            self.item_two.setPixmap(QtGui.QPixmap(item_two_image))
                        else:
                            item_two_image = f"image/Items/standard/{final_information}.png"

                            if os.path.isfile(item_two_image):
                                self.item_two.setPixmap(QtGui.QPixmap(item_two_image))
                            else:
                                item_two_image = f"image/Items/ornn/{final_information}.png"
                                self.item_two.setPixmap(QtGui.QPixmap(item_two_image))

                    if not position_information[5] == "null":

                        remove_space = position_information[5].replace(" ", "_")
                        final_information = remove_space.replace("'", "")
                        final_information = final_information.lower()

                        if "radiant" in final_information:
                            item_three_image = f"image/Items/radiant/{final_information}.png"
                            self.item_three.setPixmap(QtGui.QPixmap(item_three_image))
                        elif "emblem" in final_information:
                            embelm_path = final_information.replace("_emblem", "")
                            item_three_image = f"image/Items/trait/{embelm_path}.tft_set9.png"
                            self.item_three.setPixmap(QtGui.QPixmap(item_three_image))
                        else:
                            item_three_image = f"image/Items/standard/{final_information}.png"

                            if os.path.isfile(item_three_image):
                                self.item_three.setPixmap(QtGui.QPixmap(item_three_image))
                            else:
                                item_three_image = f"image/Items/ornn/{final_information}.png"
                                self.item_three.setPixmap(QtGui.QPixmap(item_three_image))

                else:

                    if position_information[2] == "1":
                        level_label.setPixmap(QtGui.QPixmap("image/One.png"))
                    elif position_information[2] == "2":
                        level_label.setPixmap(QtGui.QPixmap("image/Two.png"))
                    elif position_information[2] == "3":
                        level_label.setPixmap(QtGui.QPixmap("image/Three.png"))


                    if not position_information[3] == "null":
                        remove_space = position_information[3].replace(" ","_")
                        final_information = remove_space.replace("'","")
                        final_information = final_information.lower()

                        if "radiant" in final_information:
                            item_one_image = f"image/Items/radiant/{final_information}.png"
                            item_one_label.setPixmap(QtGui.QPixmap(item_one_image))
                        elif "emblem" in final_information:
                            embelm_path = final_information.replace("_emblem", "")
                            item_one_image = f"image/Items/trait/{embelm_path}.tft_set9.png"
                            item_one_label.setPixmap(QtGui.QPixmap(item_one_image))
                        else:
                            item_one_image = f"image/Items/standard/{final_information}.png"

                            if os.path.isfile(item_one_image):
                                item_one_label.setPixmap(QtGui.QPixmap(item_one_image))
                            else:
                                item_one_image = f"image/Items/ornn/{final_information}.png"
                                item_one_label.setPixmap(QtGui.QPixmap(item_one_image))

                    if not position_information[4] == "null":

                        remove_space = position_information[4].replace(" ", "_")
                        final_information = remove_space.replace("'", "")
                        final_information = final_information.lower()

                        if "radiant" in final_information:
                            item_two_image = f"image/Items/radiant/{final_information}.png"
                            item_two_label.setPixmap(QtGui.QPixmap(item_two_image))
                        elif "emblem" in final_information:
                            embelm_path = final_information.replace("_emblem", "")
                            item_two_image = f"image/Items/trait/{embelm_path}.tft_set9.png"
                            item_two_label.setPixmap(QtGui.QPixmap(item_two_image))
                        else:
                            item_two_image = f"image/Items/standard/{final_information}.png"

                            if os.path.isfile(item_two_image):
                                item_two_label.setPixmap(QtGui.QPixmap(item_two_image))
                            else:
                                item_two_image = f"image/Items/ornn/{final_information}.png"
                                item_two_label.setPixmap(QtGui.QPixmap(item_two_image))

                    if not position_information[5] == "null":

                        remove_space = position_information[5].replace(" ", "_")
                        final_information = remove_space.replace("'", "")
                        final_information = final_information.lower()

                        if "radiant" in final_information:
                            item_three_image = f"image/Items/radiant/{final_information}.png"
                            item_three_label.setPixmap(QtGui.QPixmap(item_three_image))
                        elif "emblem" in final_information:
                            embelm_path = final_information.replace("_emblem", "")
                            item_three_image = f"image/Items/trait/{embelm_path}.tft_set9.png"
                            item_three_label.setPixmap(QtGui.QPixmap(item_three_image))
                        else:
                            item_three_image = f"image/Items/standard/{final_information}.png"

                            if os.path.isfile(item_three_image):
                                item_three_label.setPixmap(QtGui.QPixmap(item_three_image))
                            else:
                                item_three_image = f"image/Items/ornn/{final_information}.png"
                                item_three_label.setPixmap(QtGui.QPixmap(item_three_image))

            if option == "predict":

                enenmy_board = [
                    ["null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",]
                    ]

                user_board = [
                    ["null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",
                    "null", "null", "null", "null", "null",]
                    ]

                def classification_prediction(data):
                    loaded_model_classfication = joblib.load('test.joblib')
                    loaded_encoder = joblib.load('encoder.joblib')
                    loaded_scaler = joblib.load('scaler.joblib')

                    y = loaded_encoder.transform(data)
                    prediction = loaded_model_classfication.predict(y)

                    return prediction

                def regression_prediction(data):
                    loaded_model_regression = joblib.load('svm_trained_model.joblib')
                    loaded_encoder = joblib.load('encoder.joblib')
                    loaded_scaler = joblib.load('scaler.joblib')

                    y = loaded_encoder.transform(data)
                    y = loaded_scaler.transform(y)
                    prediction = loaded_model_regression.predict(y)

                    return prediction

                enemy_class_score = 8
                user_class_score = 8
                enemy_regres_score = 8
                user_regres_score = 8

                if enemy is not None:
                    enemy_list = enemy.split(",")
                    enemy_adjuster = 0
                    for unit in enemy_list:
                        unit_detail = unit.split("|")
                        enenmy_board[0][0 + enemy_adjuster] = unit_detail[1].capitalize()
                        enenmy_board[0][1 + enemy_adjuster] = unit_detail[3].replace(" ", "").replace("'", "").replace("-",
                                                                                                                   "")
                        enenmy_board[0][2 + enemy_adjuster] = unit_detail[4].replace(" ", "").replace("'", "").replace("-",
                                                                                                                   "")
                        enenmy_board[0][3 + enemy_adjuster] = unit_detail[5].replace(" ", "").replace("'", "").replace("-",
                                                                                                                   "")
                        enenmy_board[0][4 + enemy_adjuster] = int(unit_detail[2])
                        enemy_adjuster = enemy_adjuster + 5

                    enemy_class_score = classification_prediction(enenmy_board)
                    enemy_regres_score = regression_prediction(user_board)

                if user is not None:
                    user_list = user.split(",")
                    user_adjuster = 0
                    for unit in user_list:
                        unit_detail = unit.split("|")
                        user_board[0][0 + user_adjuster] = unit_detail[1].capitalize()
                        user_board[0][1 + user_adjuster] = unit_detail[3].replace(" ", "").replace("'", "").replace("-", "")
                        user_board[0][2 + user_adjuster] = unit_detail[4].replace(" ", "").replace("'", "").replace("-", "")
                        user_board[0][3 + user_adjuster] = unit_detail[5].replace(" ", "").replace("'", "").replace("-", "")
                        user_board[0][4 + user_adjuster] = int(unit_detail[2])
                        user_adjuster = user_adjuster + 5

                    user_class_score = classification_prediction(user_board)
                    user_regres_score = regression_prediction(user_board)

                if enemy_class_score == user_class_score:
                    self.user_win_indicator.setText("Draw")
                    self.enemy_win_indicator.setText("Draw")
                    print("Classification: Draw")
                elif enemy_class_score < user_class_score:
                    self.user_win_indicator.setText("Lose")
                    self.enemy_win_indicator.setText("Win")
                    print("Classification: Enemy Win")
                elif enemy_class_score > user_class_score:
                    self.user_win_indicator.setText("Win")
                    self.enemy_win_indicator.setText("Lose")
                    print("Classification: User Win")

                if enemy_regres_score == user_regres_score:
                    self.user_win_indicator.setText("Draw")
                    self.enemy_win_indicator.setText("Draw")
                    print("Regression: Draw")
                elif enemy_regres_score < user_regres_score:
                    self.user_win_indicator.setText("Lose")
                    self.enemy_win_indicator.setText("Win")
                    print("Regression: Enemy Win")
                elif enemy_regres_score > user_regres_score:
                    self.user_win_indicator.setText("Win")
                    self.enemy_win_indicator.setText("Lose")
                    print("Regression: User Win")

                print("---------------------------------------------------------")
            elif option == "update":
                pass

        self.level.raise_()
        self.item_one.raise_()
        self.item_two.raise_()
        self.item_three.raise_()

        for i in range(2,56):
            label_level = getattr(self, f"level_{i}")
            label_level.raise_()

        for i in range(2,56):
            label_one = getattr(self, f"item_one_{i}")
            label_one.raise_()

        for i in range(2,56):
            label_two = getattr(self, f"item_two_{i}")
            label_two.raise_()

        for i in range(2,56):
            label_three = getattr(self, f"item_three_{i}")
            label_three.raise_()


        self.retranslate_ui_board_widget(Board_Widget)
        QtCore.QMetaObject.connectSlotsByName(Board_Widget)

        self.retranslate_ui_board_widget(Board_Widget)
        QtCore.QMetaObject.connectSlotsByName(Board_Widget)

        self.enemy_unit_1_1.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e1_1", state))
        self.enemy_unit_1_2.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e1_2", state))
        self.enemy_unit_1_3.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e1_3", state))
        self.enemy_unit_1_4.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e1_4", state))
        self.enemy_unit_1_5.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e1_5", state))
        self.enemy_unit_1_6.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e1_6", state))
        self.enemy_unit_1_7.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e1_7", state))

        self.enemy_unit_2_1.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e2_1", state))
        self.enemy_unit_2_2.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e2_2", state))
        self.enemy_unit_2_3.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e2_3", state))
        self.enemy_unit_2_4.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e2_4", state))
        self.enemy_unit_2_5.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e2_5", state))
        self.enemy_unit_2_6.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e2_6", state))
        self.enemy_unit_2_7.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e2_7", state))

        self.enemy_unit_3_1.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e3_1", state))
        self.enemy_unit_3_2.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e3_2", state))
        self.enemy_unit_3_3.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e3_3", state))
        self.enemy_unit_3_4.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e3_4", state))
        self.enemy_unit_3_5.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e3_5", state))
        self.enemy_unit_3_6.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e3_6", state))
        self.enemy_unit_3_7.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e3_7", state))

        self.enemy_unit_4_1.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e4_1", state))
        self.enemy_unit_4_2.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e4_2", state))
        self.enemy_unit_4_3.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e4_3", state))
        self.enemy_unit_4_4.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e4_4", state))
        self.enemy_unit_4_5.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e4_5", state))
        self.enemy_unit_4_6.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e4_6", state))
        self.enemy_unit_4_7.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "e4_7", state))

        self.user_unit_1_1.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u1_1", state))
        self.user_unit_1_2.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u1_2", state))
        self.user_unit_1_3.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u1_3", state))
        self.user_unit_1_4.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u1_4", state))
        self.user_unit_1_5.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u1_5", state))
        self.user_unit_1_6.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u1_6", state))
        self.user_unit_1_7.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u1_7", state))

        self.user_unit_2_1.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u2_1", state))
        self.user_unit_2_2.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u2_2", state))
        self.user_unit_2_3.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u2_3", state))
        self.user_unit_2_4.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u2_4", state))
        self.user_unit_2_5.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u2_5", state))
        self.user_unit_2_6.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u2_6", state))
        self.user_unit_2_7.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u2_7", state))

        self.user_unit_3_1.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u3_1", state))
        self.user_unit_3_2.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u3_2", state))
        self.user_unit_3_3.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u3_3", state))
        self.user_unit_3_4.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u3_4", state))
        self.user_unit_3_5.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u3_5", state))
        self.user_unit_3_6.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u3_6", state))
        self.user_unit_3_7.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u3_7", state))

        self.user_unit_4_1.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u4_1", state))
        self.user_unit_4_2.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u4_2", state))
        self.user_unit_4_3.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u4_3", state))
        self.user_unit_4_4.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u4_4", state))
        self.user_unit_4_5.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u4_5", state))
        self.user_unit_4_6.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u4_6", state))
        self.user_unit_4_7.clicked.connect(lambda: self.unit_clicked(main_window, Board_Widget, "u4_7", state))

    """
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.close()
            print('Window closed')
        else:
            event.ignore()
    """

    def retranslate_ui_board_widget(self, Board_Widget):
        _translate = QtCore.QCoreApplication.translate
        Board_Widget.setWindowTitle(_translate("Board_Widget", "Board"))
        self.enemy_win_indicator.setStatusTip(_translate("Board_Widget", "Enemy\'s prediction"))
        self.user_win_indicator.setStatusTip(_translate("Board_Widget", "Your prediction"))

    def unit_clicked(self, main_window, current_win, position, state):
        self.open_champion_window(main_window, current_win, position, state)
        #if the position's thing has not change then dont run the prediction else the prediction of win/loss for both boards

    def update_board(self, text):
        self.enemy_unit_1_1.setText(Text)