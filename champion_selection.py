from PyQt5 import QtCore, QtGui, QtWidgets
from item_selection import UI_Item_Selector

class UI_Champion_Selector_Window(object):

    def test(self, board_window, current_window, selected_champion, selected_level, position):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_Item_Selector()
        self.ui.setup_ui_item_selector(self.window, board_window, current_window, selected_champion, selected_level, position)
        self.window.show()

    def setup_ui_champion_selector_window(self, champion_level_selector, board_window, position):
        champion_level_selector.setObjectName("champion_level_selector")
        champion_level_selector.resize(900, 425)
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
        champion_level_selector.setPalette(palette)
        self.champion_tab = QtWidgets.QTabWidget(champion_level_selector)
        self.champion_tab.setGeometry(QtCore.QRect(30, 20, 671, 371))
        self.champion_tab.setMinimumSize(QtCore.QSize(8, 6))
        self.champion_tab.setMaximumSize(QtCore.QSize(43545, 6556456))
        self.champion_tab.setAutoFillBackground(False)
        self.champion_tab.setStyleSheet("background-color: rgb(18, 48, 64);")
        self.champion_tab.setDocumentMode(True)
        self.champion_tab.setObjectName("champion_tab")
        self.tier_one = QtWidgets.QWidget()
        self.tier_one.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tier_one.setObjectName("tier_one")
        self.ashe_button = QtWidgets.QPushButton(self.tier_one)
        self.ashe_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.ashe_button.setStyleSheet("QPushButton {\n"
                                       "background: #9f9b92;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.ashe_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_ashe_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ashe_button.setIcon(icon)
        self.ashe_button.setIconSize(QtCore.QSize(75, 75))
        self.ashe_button.setFlat(False)
        self.ashe_button.setObjectName("ashe_button")
        self.blitz_button = QtWidgets.QPushButton(self.tier_one)
        self.blitz_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.blitz_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.blitz_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_blitzcrank_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blitz_button.setIcon(icon1)
        self.blitz_button.setIconSize(QtCore.QSize(75, 75))
        self.blitz_button.setFlat(False)
        self.blitz_button.setObjectName("blitz_button")
        self.galio_button = QtWidgets.QPushButton(self.tier_one)
        self.galio_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.galio_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.galio_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_galio_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.galio_button.setIcon(icon2)
        self.galio_button.setIconSize(QtCore.QSize(75, 75))
        self.galio_button.setFlat(False)
        self.galio_button.setObjectName("galio_button")
        self.gangplank_button = QtWidgets.QPushButton(self.tier_one)
        self.gangplank_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.gangplank_button.setStyleSheet("QPushButton {\n"
                                            "background: #9f9b92;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.gangplank_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_gangplank_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gangplank_button.setIcon(icon3)
        self.gangplank_button.setIconSize(QtCore.QSize(75, 75))
        self.gangplank_button.setFlat(False)
        self.gangplank_button.setObjectName("gangplank_button")
        self.kayle_button = QtWidgets.QPushButton(self.tier_one)
        self.kayle_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.kayle_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.kayle_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_kayle_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kayle_button.setIcon(icon4)
        self.kayle_button.setIconSize(QtCore.QSize(75, 75))
        self.kayle_button.setFlat(False)
        self.kayle_button.setObjectName("kayle_button")
        self.lulu_button = QtWidgets.QPushButton(self.tier_one)
        self.lulu_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.lulu_button.setStyleSheet("QPushButton {\n"
                                       "background: #9f9b92;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.lulu_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_lulu_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lulu_button.setIcon(icon5)
        self.lulu_button.setIconSize(QtCore.QSize(75, 75))
        self.lulu_button.setFlat(False)
        self.lulu_button.setObjectName("lulu_button")
        self.lux_button = QtWidgets.QPushButton(self.tier_one)
        self.lux_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.lux_button.setStyleSheet("QPushButton {\n"
                                      "background: #9f9b92;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.lux_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_lux_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lux_button.setIcon(icon6)
        self.lux_button.setIconSize(QtCore.QSize(75, 75))
        self.lux_button.setFlat(False)
        self.lux_button.setObjectName("lux_button")
        self.nasus_button = QtWidgets.QPushButton(self.tier_one)
        self.nasus_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.nasus_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.nasus_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_nasus_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nasus_button.setIcon(icon7)
        self.nasus_button.setIconSize(QtCore.QSize(75, 75))
        self.nasus_button.setFlat(False)
        self.nasus_button.setObjectName("nasus_button")
        self.poppy_button = QtWidgets.QPushButton(self.tier_one)
        self.poppy_button.setGeometry(QtCore.QRect(240, 130, 82, 82))
        self.poppy_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.poppy_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_poppy_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.poppy_button.setIcon(icon8)
        self.poppy_button.setIconSize(QtCore.QSize(75, 75))
        self.poppy_button.setFlat(False)
        self.poppy_button.setObjectName("poppy_button")
        self.renekton_button = QtWidgets.QPushButton(self.tier_one)
        self.renekton_button.setGeometry(QtCore.QRect(350, 130, 82, 82))
        self.renekton_button.setStyleSheet("QPushButton {\n"
                                           "background: #9f9b92;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.renekton_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_renekton_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renekton_button.setIcon(icon9)
        self.renekton_button.setIconSize(QtCore.QSize(75, 75))
        self.renekton_button.setFlat(False)
        self.renekton_button.setObjectName("renekton_button")
        self.sylas_button = QtWidgets.QPushButton(self.tier_one)
        self.sylas_button.setGeometry(QtCore.QRect(460, 130, 82, 82))
        self.sylas_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.sylas_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sylas_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sylas_button.setIcon(icon10)
        self.sylas_button.setIconSize(QtCore.QSize(75, 75))
        self.sylas_button.setFlat(False)
        self.sylas_button.setObjectName("sylas_button")
        self.talon_button = QtWidgets.QPushButton(self.tier_one)
        self.talon_button.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.talon_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.talon_button.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_talon_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.talon_button.setIcon(icon11)
        self.talon_button.setIconSize(QtCore.QSize(75, 75))
        self.talon_button.setFlat(False)
        self.talon_button.setObjectName("talon_button")
        self.wukong_button= QtWidgets.QPushButton(self.tier_one)
        self.wukong_button.setGeometry(QtCore.QRect(20, 240, 82, 82))
        self.wukong_button.setStyleSheet("QPushButton {\n"
                                         "background: #9f9b92;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.wukong_button  .setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_wukong_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wukong_button.setIcon(icon12)
        self.wukong_button.setIconSize(QtCore.QSize(75, 75))
        self.wukong_button.setFlat(False)
        self.wukong_button.setObjectName("wukong_button")
        self.champion_tab.addTab(self.tier_one, "")
        self.tier_two = QtWidgets.QWidget()
        self.tier_two.setObjectName("tier_two")
        self.annie_button = QtWidgets.QPushButton(self.tier_two)
        self.annie_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.annie_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.annie_button.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_annie_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.annie_button.setIcon(icon13)
        self.annie_button.setIconSize(QtCore.QSize(75, 75))
        self.annie_button.setFlat(False)
        self.annie_button.setObjectName("annie_button")
        self.camille_button = QtWidgets.QPushButton(self.tier_two)
        self.camille_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.camille_button.setStyleSheet("QPushButton {\n"
                                          "background: #25b05c;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.camille_button.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_camille_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camille_button.setIcon(icon14)
        self.camille_button.setIconSize(QtCore.QSize(75, 75))
        self.camille_button.setFlat(False)
        self.camille_button.setObjectName("camile_button")
        self.draven_button = QtWidgets.QPushButton(self.tier_two)
        self.draven_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.draven_button.setStyleSheet("QPushButton {\n"
                                         "background: #25b05c;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.draven_button.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_draven_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.draven_button.setIcon(icon15)
        self.draven_button.setIconSize(QtCore.QSize(75, 75))
        self.draven_button.setFlat(False)
        self.draven_button.setObjectName("draven_button")
        self.ezreal_button = QtWidgets.QPushButton(self.tier_two)
        self.ezreal_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.ezreal_button.setStyleSheet("QPushButton {\n"
                                         "background: #25b05c;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ezreal_button.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_ezreal_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ezreal_button.setIcon(icon16)
        self.ezreal_button.setIconSize(QtCore.QSize(75, 75))
        self.ezreal_button.setFlat(False)
        self.ezreal_button.setObjectName("ezreal_button")
        self.fiora_button = QtWidgets.QPushButton(self.tier_two)
        self.fiora_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.fiora_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.fiora_button.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_fiora_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fiora_button.setIcon(icon17)
        self.fiora_button.setIconSize(QtCore.QSize(75, 75))
        self.fiora_button.setFlat(False)
        self.fiora_button.setObjectName("fiora_button")
        self.jinx_button = QtWidgets.QPushButton(self.tier_two)
        self.jinx_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.jinx_button.setStyleSheet("QPushButton {\n"
                                       "background: #25b05c;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.jinx_button.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_jinx_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jinx_button.setIcon(icon18)
        self.jinx_button.setIconSize(QtCore.QSize(75, 75))
        self.jinx_button.setFlat(False)
        self.jinx_button.setObjectName("jinx_button")
        self.leesin_button = QtWidgets.QPushButton(self.tier_two)
        self.leesin_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.leesin_button.setStyleSheet("QPushButton {\n"
                                         "background: #25b05c;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.leesin_button.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_leesin_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leesin_button.setIcon(icon19)
        self.leesin_button.setIconSize(QtCore.QSize(75, 75))
        self.leesin_button.setFlat(False)
        self.leesin_button.setObjectName("leesin_button")
        self.malphite_button = QtWidgets.QPushButton(self.tier_two)
        self.malphite_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.malphite_button.setStyleSheet("QPushButton {\n"
                                           "background: #25b05c;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.malphite_button.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_malphite_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.malphite_button.setIcon(icon20)
        self.malphite_button.setIconSize(QtCore.QSize(75, 75))
        self.malphite_button.setFlat(False)
        self.malphite_button.setObjectName("malphite_button")
        self.rell_button = QtWidgets.QPushButton(self.tier_two)
        self.rell_button.setGeometry(QtCore.QRect(240, 130, 82, 82))
        self.rell_button.setStyleSheet("QPushButton {\n"
                                       "background: #25b05c;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.rell_button.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_rell_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rell_button.setIcon(icon21)
        self.rell_button.setIconSize(QtCore.QSize(75, 75))
        self.rell_button.setFlat(False)
        self.rell_button.setObjectName("rell_button")
        self.sivir_button = QtWidgets.QPushButton(self.tier_two)
        self.sivir_button.setGeometry(QtCore.QRect(350, 130, 82, 82))
        self.sivir_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.sivir_button.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sivir_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sivir_button.setIcon(icon22)
        self.sivir_button.setIconSize(QtCore.QSize(75, 75))
        self.sivir_button.setFlat(False)
        self.sivir_button.setObjectName("sivir_button")
        self.vi_button = QtWidgets.QPushButton(self.tier_two)
        self.vi_button.setGeometry(QtCore.QRect(460, 130, 82, 82))
        self.vi_button.setStyleSheet("QPushButton {\n"
                                     "background: #25b05c;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background: white;\n"
                                     "}")
        self.vi_button.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_vi_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vi_button.setIcon(icon23)
        self.vi_button.setIconSize(QtCore.QSize(75, 75))
        self.vi_button.setFlat(False)
        self.vi_button.setObjectName("vi_button")
        self.yasuo_button = QtWidgets.QPushButton(self.tier_two)
        self.yasuo_button.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.yasuo_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.yasuo_button.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_yasuo_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yasuo_button.setIcon(icon24)
        self.yasuo_button.setIconSize(QtCore.QSize(75, 75))
        self.yasuo_button.setFlat(False)
        self.yasuo_button.setObjectName("yasuo_button")
        self.yuumi_button = QtWidgets.QPushButton(self.tier_two)
        self.yuumi_button.setGeometry(QtCore.QRect(20, 240, 82, 82))
        self.yuumi_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.yuumi_button.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_yuumi_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yuumi_button.setIcon(icon25)
        self.yuumi_button.setIconSize(QtCore.QSize(75, 75))
        self.yuumi_button.setFlat(False)
        self.yuumi_button.setObjectName("yuumi_button")
        self.champion_tab.addTab(self.tier_two, "")
        self.tier_three = QtWidgets.QWidget()
        self.tier_three.setObjectName("tier_three")
        self.alistar_button = QtWidgets.QPushButton(self.tier_three)
        self.alistar_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.alistar_button.setStyleSheet("QPushButton {\n"
                                          "background: #26a5c9;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.alistar_button.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_alistar_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alistar_button.setIcon(icon26)
        self.alistar_button.setIconSize(QtCore.QSize(75, 75))
        self.alistar_button.setFlat(False)
        self.alistar_button.setObjectName("alistar_button")
        self.chogath_button = QtWidgets.QPushButton(self.tier_three)
        self.chogath_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.chogath_button.setStyleSheet("QPushButton {\n"
                                          "background: #26a5c9;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.chogath_button.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_chogath_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chogath_button.setIcon(icon27)
        self.chogath_button.setIconSize(QtCore.QSize(75, 75))
        self.chogath_button.setFlat(False)
        self.chogath_button.setObjectName("chogath_button")
        self.jax_button = QtWidgets.QPushButton(self.tier_three)
        self.jax_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.jax_button.setStyleSheet("QPushButton {\n"
                                      "background: #26a5c9;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.jax_button.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_jax_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jax_button.setIcon(icon28)
        self.jax_button.setIconSize(QtCore.QSize(75, 75))
        self.jax_button.setFlat(False)
        self.jax_button.setObjectName("jax_button")
        self.kaisa_button = QtWidgets.QPushButton(self.tier_three)
        self.kaisa_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.kaisa_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.kaisa_button.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_kaisa_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kaisa_button.setIcon(icon29)
        self.kaisa_button.setIconSize(QtCore.QSize(75, 75))
        self.kaisa_button.setFlat(False)
        self.kaisa_button.setObjectName("kaisa_button")
        self.leblanc_button = QtWidgets.QPushButton(self.tier_three)
        self.leblanc_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.leblanc_button.setStyleSheet("QPushButton {\n"
                                          "background: #26a5c9;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.leblanc_button.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_leblanc_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leblanc_button.setIcon(icon30)
        self.leblanc_button.setIconSize(QtCore.QSize(75, 75))
        self.leblanc_button.setFlat(False)
        self.leblanc_button.setObjectName("leblanc_button")
        self.nilah_button = QtWidgets.QPushButton(self.tier_three)
        self.nilah_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.nilah_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.nilah_button.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_nilah_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nilah_button.setIcon(icon31)
        self.nilah_button.setIconSize(QtCore.QSize(75, 75))
        self.nilah_button.setFlat(False)
        self.nilah_button.setObjectName("nilah_button")
        self.rammus_button = QtWidgets.QPushButton(self.tier_three)
        self.rammus_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.rammus_button.setStyleSheet("QPushButton {\n"
                                         "background: #26a5c9;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.rammus_button.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_rammus_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rammus_button.setIcon(icon32)
        self.rammus_button.setIconSize(QtCore.QSize(75, 75))
        self.rammus_button.setFlat(False)
        self.rammus_button.setObjectName("rammus_button")
        self.riven_button = QtWidgets.QPushButton(self.tier_three)
        self.riven_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.riven_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.riven_button.setText("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_riven_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.riven_button.setIcon(icon33)
        self.riven_button.setIconSize(QtCore.QSize(75, 75))
        self.riven_button.setFlat(False)
        self.riven_button.setObjectName("riven_button")
        self.senna_button = QtWidgets.QPushButton(self.tier_three)
        self.senna_button.setGeometry(QtCore.QRect(240, 130, 82, 82))
        self.senna_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.senna_button.setText("")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_senna_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.senna_button.setIcon(icon34)
        self.senna_button.setIconSize(QtCore.QSize(75, 75))
        self.senna_button.setFlat(False)
        self.senna_button.setObjectName("senna_button")
        self.sona_button = QtWidgets.QPushButton(self.tier_three)
        self.sona_button.setGeometry(QtCore.QRect(350, 130, 82, 82))
        self.sona_button.setStyleSheet("QPushButton {\n"
                                       "background: #26a5c9;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.sona_button.setText("")
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sona_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sona_button.setIcon(icon35)
        self.sona_button.setIconSize(QtCore.QSize(75, 75))
        self.sona_button.setFlat(False)
        self.sona_button.setObjectName("sona_button")
        self.vayne_button = QtWidgets.QPushButton(self.tier_three)
        self.vayne_button.setGeometry(QtCore.QRect(460, 130, 82, 82))
        self.vayne_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.vayne_button.setText("")
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_vayne_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vayne_button.setIcon(icon36)
        self.vayne_button.setIconSize(QtCore.QSize(75, 75))
        self.vayne_button.setFlat(False)
        self.vayne_button.setObjectName("vayne_button")
        self.velkoz_button = QtWidgets.QPushButton(self.tier_three)
        self.velkoz_button.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.velkoz_button.setStyleSheet("QPushButton {\n"
                                         "background: #26a5c9;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.velkoz_button.setText("")
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_velkoz_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.velkoz_button.setIcon(icon37)
        self.velkoz_button.setIconSize(QtCore.QSize(75, 75))
        self.velkoz_button.setFlat(False)
        self.velkoz_button.setObjectName("velkoz_button")
        self.zoe_button = QtWidgets.QPushButton(self.tier_three)
        self.zoe_button.setGeometry(QtCore.QRect(20, 240, 82, 82))
        self.zoe_button.setStyleSheet("QPushButton {\n"
                                      "background: #26a5c9;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.zoe_button.setText("")
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_zoe_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoe_button.setIcon(icon38)
        self.zoe_button.setIconSize(QtCore.QSize(75, 75))
        self.zoe_button.setFlat(False)
        self.zoe_button.setObjectName("zoe_button")
        self.champion_tab.addTab(self.tier_three, "")
        self.tier_four = QtWidgets.QWidget()
        self.tier_four.setObjectName("tier_four")
        self.aurelionsol_button = QtWidgets.QPushButton(self.tier_four)
        self.aurelionsol_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.aurelionsol_button.setStyleSheet("QPushButton {\n"
                                              "background: #6610f2;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.aurelionsol_button.setText("")
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_aurelionsol_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aurelionsol_button.setIcon(icon39)
        self.aurelionsol_button.setIconSize(QtCore.QSize(75, 75))
        self.aurelionsol_button.setFlat(False)
        self.aurelionsol_button.setObjectName("aurelionsol_button")
        self.belveth_button = QtWidgets.QPushButton(self.tier_four)
        self.belveth_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.belveth_button.setStyleSheet("QPushButton {\n"
                                          "background: #6610f2;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.belveth_button.setText("")
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_belveth_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.belveth_button.setIcon(icon40)
        self.belveth_button.setIconSize(QtCore.QSize(75, 75))
        self.belveth_button.setFlat(False)
        self.belveth_button.setObjectName("belveth_button")
        self.ekko_button = QtWidgets.QPushButton(self.tier_four)
        self.ekko_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.ekko_button.setStyleSheet("QPushButton {\n"
                                       "background: #6610f2;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.ekko_button.setText("")
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_ekko_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ekko_button.setIcon(icon41)
        self.ekko_button.setIconSize(QtCore.QSize(75, 75))
        self.ekko_button.setFlat(False)
        self.ekko_button.setObjectName("ekko_button")
        self.missfortune_button = QtWidgets.QPushButton(self.tier_four)
        self.missfortune_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.missfortune_button.setStyleSheet("QPushButton {\n"
                                              "background: #6610f2;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.missfortune_button.setText("")
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_missfortune_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.missfortune_button.setIcon(icon42)
        self.missfortune_button.setIconSize(QtCore.QSize(75, 75))
        self.missfortune_button.setFlat(False)
        self.missfortune_button.setObjectName("missfortune_button")
        self.samira_button = QtWidgets.QPushButton(self.tier_four)
        self.samira_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.samira_button.setStyleSheet("QPushButton {\n"
                                         "background: #6610f2;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.samira_button.setText("")
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_samira_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.samira_button.setIcon(icon43)
        self.samira_button.setIconSize(QtCore.QSize(75, 75))
        self.samira_button.setFlat(False)
        self.samira_button.setObjectName("samira_button")
        self.sejuani_button = QtWidgets.QPushButton(self.tier_four)
        self.sejuani_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.sejuani_button.setStyleSheet("QPushButton {\n"
                                          "background: #6610f2;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.sejuani_button.setText("")
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sejuani_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sejuani_button.setIcon(icon44)
        self.sejuani_button.setIconSize(QtCore.QSize(75, 75))
        self.sejuani_button.setFlat(False)
        self.sejuani_button.setObjectName("sejuani_button")
        self.sett_button = QtWidgets.QPushButton(self.tier_four)
        self.sett_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.sett_button.setStyleSheet("QPushButton {\n"
                                       "background: #6610f2;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.sett_button.setText("")
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sett_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sett_button.setIcon(icon45)
        self.sett_button.setIconSize(QtCore.QSize(75, 75))
        self.sett_button.setFlat(False)
        self.sett_button.setObjectName("sett_button")
        self.soraka_button = QtWidgets.QPushButton(self.tier_four)
        self.soraka_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.soraka_button.setStyleSheet("QPushButton {\n"
                                         "background: #6610f2;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.soraka_button.setText("")
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_soraka_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soraka_button.setIcon(icon46)
        self.soraka_button.setIconSize(QtCore.QSize(75, 75))
        self.soraka_button.setFlat(False)
        self.soraka_button.setObjectName("soraka_button")
        self.taliyah_button = QtWidgets.QPushButton(self.tier_four)
        self.taliyah_button.setGeometry(QtCore.QRect(240, 131, 82, 82))
        self.taliyah_button.setStyleSheet("QPushButton {\n"
                                          "background: #6610f2;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.taliyah_button.setText("")
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_taliyah_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.taliyah_button.setIcon(icon47)
        self.taliyah_button.setIconSize(QtCore.QSize(75, 75))
        self.taliyah_button.setFlat(False)
        self.taliyah_button.setObjectName("taliyah_button")
        self.viego_button = QtWidgets.QPushButton(self.tier_four)
        self.viego_button.setGeometry(QtCore.QRect(350, 130, 82, 82))
        self.viego_button.setStyleSheet("QPushButton {\n"
                                        "background: #6610f2;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.viego_button.setText("")
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_viego_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viego_button.setIcon(icon48)
        self.viego_button.setIconSize(QtCore.QSize(75, 75))
        self.viego_button.setFlat(False)
        self.viego_button.setObjectName("viego_button")
        self.zac_button = QtWidgets.QPushButton(self.tier_four)
        self.zac_button.setGeometry(QtCore.QRect(460, 130, 82, 82))
        self.zac_button.setStyleSheet("QPushButton {\n"
                                      "background: #6610f2;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.zac_button.setText("")
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_zac_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zac_button.setIcon(icon49)
        self.zac_button.setIconSize(QtCore.QSize(75, 75))
        self.zac_button.setFlat(False)
        self.zac_button.setObjectName("zac_button")
        self.zed_button = QtWidgets.QPushButton(self.tier_four)
        self.zed_button.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.zed_button.setStyleSheet("QPushButton {\n"
                                      "background: #6610f2;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.zed_button.setText("")
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_zed_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zed_button.setIcon(icon50)
        self.zed_button.setIconSize(QtCore.QSize(75, 75))
        self.zed_button.setFlat(False)
        self.zed_button.setObjectName("zed_button")
        self.champion_tab.addTab(self.tier_four, "")
        self.tier_five = QtWidgets.QWidget()
        self.tier_five.setObjectName("tier_five")
        self.aphelios_button = QtWidgets.QPushButton(self.tier_five)
        self.aphelios_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.aphelios_button.setStyleSheet("QPushButton {\n"
                                           "background: #f9b428;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.aphelios_button.setText("")
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_aphelios_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aphelios_button.setIcon(icon51)
        self.aphelios_button.setIconSize(QtCore.QSize(75, 75))
        self.aphelios_button.setFlat(False)
        self.aphelios_button.setObjectName("alphelios_button")
        self.fiddlesticks_button = QtWidgets.QPushButton(self.tier_five)
        self.fiddlesticks_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.fiddlesticks_button.setStyleSheet("QPushButton {\n"
                                               "background: #f9b428;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "background: white;\n"
                                               "}")
        self.fiddlesticks_button.setText("")
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_fiddlesticks_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fiddlesticks_button.setIcon(icon52)
        self.fiddlesticks_button.setIconSize(QtCore.QSize(75, 75))
        self.fiddlesticks_button.setFlat(False)
        self.fiddlesticks_button.setObjectName("fiddlesticks_button")
        self.janna_button = QtWidgets.QPushButton(self.tier_five)
        self.janna_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.janna_button.setStyleSheet("QPushButton {\n"
                                        "background: #f9b428;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.janna_button.setText("")
        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_janna_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.janna_button.setIcon(icon53)
        self.janna_button.setIconSize(QtCore.QSize(75, 75))
        self.janna_button.setFlat(False)
        self.janna_button.setObjectName("janna_button")
        self.syndra_button = QtWidgets.QPushButton(self.tier_five)
        self.syndra_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.syndra_button.setStyleSheet("QPushButton {\n"
                                         "background: #f9b428;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.syndra_button.setText("")
        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_syndra_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.syndra_button.setIcon(icon54)
        self.syndra_button.setIconSize(QtCore.QSize(75, 75))
        self.syndra_button.setFlat(False)
        self.syndra_button.setObjectName("syndra_button")
        self.leona_button = QtWidgets.QPushButton(self.tier_five)
        self.leona_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.leona_button.setStyleSheet("QPushButton {\n"
                                        "background: #f9b428;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.leona_button.setText("")
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_leona_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leona_button.setIcon(icon55)
        self.leona_button.setIconSize(QtCore.QSize(75, 75))
        self.leona_button.setFlat(False)
        self.leona_button.setObjectName("leona_button")
        self.mordekaiser_button = QtWidgets.QPushButton(self.tier_five)
        self.mordekaiser_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.mordekaiser_button.setStyleSheet("QPushButton {\n"
                                              "background: #f9b428;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.mordekaiser_button.setText("")
        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_mordekaiser_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mordekaiser_button.setIcon(icon56)
        self.mordekaiser_button.setIconSize(QtCore.QSize(75, 75))
        self.mordekaiser_button.setFlat(False)
        self.mordekaiser_button.setObjectName("mordekaiser")
        self.nunu_button = QtWidgets.QPushButton(self.tier_five)
        self.nunu_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.nunu_button.setStyleSheet("QPushButton {\n"
                                       "background: #f9b428;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.nunu_button.setText("")
        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_nunu_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nunu_button.setIcon(icon57)
        self.nunu_button.setIconSize(QtCore.QSize(75, 75))
        self.nunu_button.setFlat(False)
        self.nunu_button.setObjectName("nunu_button")
        self.urgot_button = QtWidgets.QPushButton(self.tier_five)
        self.urgot_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.urgot_button.setStyleSheet("QPushButton {\n"
                                        "background: #f9b428;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.urgot_button.setText("")
        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_urgot_square.tft_set8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.urgot_button.setIcon(icon58)
        self.urgot_button.setIconSize(QtCore.QSize(75, 75))
        self.urgot_button.setFlat(False)
        self.urgot_button.setObjectName("urgot_button")
        self.champion_tab.addTab(self.tier_five, "")
        self.champion_name = QtWidgets.QLabel(champion_level_selector)
        self.champion_name.setGeometry(QtCore.QRect(740, 210, 120, 20))
        self.champion_name.setAlignment(QtCore.Qt.AlignCenter)
        self.champion_name.setObjectName("champion_name")
        self.next_button = QtWidgets.QPushButton(champion_level_selector)
        self.next_button.setGeometry(QtCore.QRect(750, 280, 101, 41))
        self.next_button.setStyleSheet("QPushButton {\n"
                                       "color: white;\n"
                                       "border-radius: 20px;\n"
                                       "background: qradialgradient(\n"
                                       "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                       "radius: 1.35, stop: 0 #123040, stop: 1 #123040);\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "background: qradialgradient(\n"
                                       "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                       "radius: 1.35, stop: 0 #195778, stop: 1 #195778);\n"
                                       "}")
        self.next_button.setObjectName("next_button")
        self.selected_champion = QtWidgets.QLabel(champion_level_selector)
        self.selected_champion.setGeometry(QtCore.QRect(750, 100, 101, 101))
        self.selected_champion.setScaledContents(True)
        self.selected_champion.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_champion.setObjectName("selected_champion")
        self.selected_level = QtWidgets.QLabel(champion_level_selector)
        self.selected_level.setGeometry(QtCore.QRect(750, 80, 101, 20))
        self.selected_level.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_level.setObjectName("label")
        self.champion_tab.raise_()
        self.champion_name.raise_()
        self.selected_champion.raise_()
        self.next_button.raise_()
        self.selected_level.raise_()

        self.retranslate_ui_champion_selector_window(champion_level_selector)
        self.champion_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(champion_level_selector)

        self.ashe_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_ashe_square.tft_set8.png", "Ashe"))
        self.blitz_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_blitzcrank_square.tft_set8.png", "Blitzcrank"))
        self.galio_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_galio_square.tft_set8.png", "Galio"))
        self.gangplank_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_gangplank_square.tft_set8.png", "Gangplank"))
        self.kayle_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_kayle_square.tft_set8.png", "Kayle"))
        self.lulu_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_lulu_square.tft_set8.png", "Lulu"))
        self.lux_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_lux_square.tft_set8.png", "Lux"))
        self.nasus_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_nasus_square.tft_set8.png", "Nasus"))
        self.poppy_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_poppy_square.tft_set8.png", "Poppy"))
        self.renekton_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_renekton_square.tft_set8.png", "Renekton"))
        self.sylas_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sylas_square.tft_set8.png", "Sylas"))
        self.talon_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_talon_square.tft_set8.png", "Talon"))
        self.wukong_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_wukong_square.tft_set8.png", "Wukong"))

        self.annie_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_annie_square.tft_set8.png", "Annie"))
        self.camille_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_camille_square.tft_set8.png", "Camille"))
        self.draven_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_draven_square.tft_set8.png", "Draven"))
        self.ezreal_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_ezreal_square.tft_set8.png", "Ezreal"))
        self.fiora_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_fiora_square.tft_set8.png", "Fiora"))
        self.jinx_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_jinx_square.tft_set8.png", "Jinx"))
        self.leesin_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_leesin_square.tft_set8.png", "Lee Sin"))
        self.malphite_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_malphite_square.tft_set8.png", "Malphite"))
        self.rell_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_rell_square.tft_set8.png", "Rell"))
        self.sivir_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sivir_square.tft_set8.png", "Sivir"))
        self.vi_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_vi_square.tft_set8.png", "Vi"))
        self.yasuo_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_yasuo_square.tft_set8.png", "Yasuo"))
        self.yuumi_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_yuumi_square.tft_set8.png", "Yuumi"))

        self.alistar_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_alistar_square.tft_set8.png", "Alistar"))
        self.chogath_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_chogath_square.tft_set8.png", "Cho'gath"))
        self.jax_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_jax_square.tft_set8.png", "Jax"))
        self.kaisa_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_kaisa_square.tft_set8.png", "Kaisa"))
        self.leblanc_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_leblanc_square.tft_set8.png", "Leblanc"))
        self.nilah_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_nilah_square.tft_set8.png", "Nilah"))
        self.rammus_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_rammus_square.tft_set8.png", "Rammus"))
        self.riven_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_riven_square.tft_set8.png", "Riven"))
        self.senna_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_senna_square.tft_set8.png", "Senna"))
        self.sona_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sona_square.tft_set8.png", "Sona"))
        self.vayne_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_vayne_square.tft_set8.png", "Vayne"))
        self.velkoz_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_velkoz_square.tft_set8.png", "Velkoz"))
        self.zoe_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_zoe_square.tft_set8.png", "Zoe"))

        self.aurelionsol_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_aurelionsol_square.tft_set8.png", "Aurelion Sol"))
        self.belveth_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_belveth_square.tft_set8.png", "Bel'Veth"))
        self.ekko_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_ekko_square.tft_set8.png", "Ekko"))
        self.missfortune_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_missfortune_square.tft_set8.png", "Miss Fortune"))
        self.samira_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_samira_square.tft_set8.png", "Samira"))
        self.sejuani_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sejuani_square.tft_set8.png", "Sejuani"))
        self.sett_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_sett_square.tft_set8.png", "Sett"))
        self.leblanc_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_leblanc_square.tft_set8.png", "Leblanc"))
        self.taliyah_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_taliyah_square.tft_set8.png", "Taliyah"))
        self.viego_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_viego_square.tft_set8.png", "Viego"))
        self.zac_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_zac_square.tft_set8.png", "Zac"))
        self.zed_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_zed_square.tft_set8.png", "Zed"))

        self.aphelios_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_aphelios_square.tft_set8.png", "Aphelios"))
        self.fiddlesticks_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_fiddlesticks_square.tft_set8.png", "Fiddlesticks"))
        self.janna_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_janna_square.tft_set8.png", "Janna"))
        self.leona_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_leona_square.tft_set8.png", "Leona"))
        self.mordekaiser_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_mordekaiser_square.tft_set8.png", "Mordekaiser"))
        self.nunu_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_nunu_square.tft_set8.png", "Nunu & Willump"))
        self.syndra_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_syndra_square.tft_set8.png", "Syndra"))
        self.urgot_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/tft8_urgot_square.tft_set8.png", "Urgot"))

        self.next_button.clicked.connect(lambda: self.next_clicked(board_window, champion_level_selector, position))

    def retranslate_ui_champion_selector_window(self, champion_level_selector):
        _translate = QtCore.QCoreApplication.translate
        champion_level_selector.setWindowTitle(_translate("champion_level_selector", "Champion Selection"))
        self.champion_tab.setTabText(self.champion_tab.indexOf(self.tier_one), _translate("champion_level_selector", "Tier 1"))
        self.champion_tab.setTabText(self.champion_tab.indexOf(self.tier_two), _translate("champion_level_selector", "Tier 2"))
        self.champion_tab.setTabText(self.champion_tab.indexOf(self.tier_three), _translate("champion_level_selector", "Tier 3"))
        self.champion_tab.setTabText(self.champion_tab.indexOf(self.tier_four), _translate("champion_level_selector", "Tier 4"))
        self.champion_tab.setTabText(self.champion_tab.indexOf(self.tier_five), _translate("champion_level_selector", "Tier 5"))
        self.champion_name.setText(_translate("champion_level_selector", "Name"))
        self.next_button.setText(_translate("champion_level_selector", "Next"))
        self.selected_champion.setText(_translate("champion_level_selector", "selected champion"))
        self.selected_level.setText(_translate("champion_level_selector", "Lvl"))

    def unit_clicked(self, image_path, champion_name):
        if self.champion_name.text() == champion_name:
            if self.selected_level.text() == "Lvl":
                self.selected_level.setText("Lvl 1")
            elif self.selected_level.text() == "Lvl 1":
                self.selected_level.setText("Lvl 2")
            elif self.selected_level.text() == "Lvl 2":
                self.selected_level.setText("Lvl 3")
            elif self.selected_level.text() == "Lvl 3":
                self.selected_level.setText("Lvl 1")
        else:
            self.selected_level.setText("Lvl 1")
            self.champion_name.setText(champion_name)
            self.selected_champion.setPixmap(QtGui.QPixmap(image_path))

    def next_clicked(self, board_window, champion_window, position):
        if self.champion_name.text() == "Name":
            print("test - worked no champion selected")
        else:
            ##self.open_item_window(board_window, champion_window, position, self.champion_name.text())
            self.test(board_window, champion_window, self.champion_name.text(), self.selected_level.text(), position)