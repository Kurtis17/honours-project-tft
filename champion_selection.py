from PyQt5 import QtCore, QtGui, QtWidgets
from item_selection import UI_Item_Selector

class UI_Champion_Selector_Window(object):

    def open_item_window(self, board_window, current_window, selected_champion, selected_level, position, state):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_Item_Selector()
        self.ui.setup_ui_item_selector(self.window, board_window, current_window, selected_champion, selected_level, position, state)
        self.window.show()

    def setup_ui_champion_selector_window(self, champion_level_selector, board_window, position, state):
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
        self.cassiopeia_button = QtWidgets.QPushButton(self.tier_one)
        self.cassiopeia_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.cassiopeia_button.setStyleSheet("QPushButton {\n"
                                       "background: #9f9b92;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.cassiopeia_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_cassiopeia_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cassiopeia_button.setIcon(icon)
        self.cassiopeia_button.setIconSize(QtCore.QSize(75, 75))
        self.cassiopeia_button.setFlat(False)
        self.cassiopeia_button.setObjectName("cassiopeia_button")
        self.chogath_button = QtWidgets.QPushButton(self.tier_one)
        self.chogath_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.chogath_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.chogath_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_chogath_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chogath_button.setIcon(icon1)
        self.chogath_button.setIconSize(QtCore.QSize(75, 75))
        self.chogath_button.setFlat(False)
        self.chogath_button.setObjectName("chogath_button")
        self.irelia_button = QtWidgets.QPushButton(self.tier_one)
        self.irelia_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.irelia_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.irelia_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_irelia_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.irelia_button.setIcon(icon2)
        self.irelia_button.setIconSize(QtCore.QSize(75, 75))
        self.irelia_button.setFlat(False)
        self.irelia_button.setObjectName("irelia_button")
        self.jhin_button = QtWidgets.QPushButton(self.tier_one)
        self.jhin_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.jhin_button.setStyleSheet("QPushButton {\n"
                                            "background: #9f9b92;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.jhin_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_jhin_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jhin_button.setIcon(icon3)
        self.jhin_button.setIconSize(QtCore.QSize(75, 75))
        self.jhin_button.setFlat(False)
        self.jhin_button.setObjectName("jhin_button")
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
        icon4.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kayle_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kayle_button.setIcon(icon4)
        self.kayle_button.setIconSize(QtCore.QSize(75, 75))
        self.kayle_button.setFlat(False)
        self.kayle_button.setObjectName("kayle_button")
        self.malzahar_button = QtWidgets.QPushButton(self.tier_one)
        self.malzahar_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.malzahar_button.setStyleSheet("QPushButton {\n"
                                       "background: #9f9b92;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.malzahar_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_malzahar_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.malzahar_button.setIcon(icon5)
        self.malzahar_button.setIconSize(QtCore.QSize(75, 75))
        self.malzahar_button.setFlat(False)
        self.malzahar_button.setObjectName("malzahar_button")
        self.maokai_button = QtWidgets.QPushButton(self.tier_one)
        self.maokai_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.maokai_button.setStyleSheet("QPushButton {\n"
                                      "background: #9f9b92;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.maokai_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_maokai_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maokai_button.setIcon(icon6)
        self.maokai_button.setIconSize(QtCore.QSize(75, 75))
        self.maokai_button.setFlat(False)
        self.maokai_button.setObjectName("maokai_button")
        self.orianna_button = QtWidgets.QPushButton(self.tier_one)
        self.orianna_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.orianna_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.orianna_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_orianna_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.orianna_button.setIcon(icon7)
        self.orianna_button.setIconSize(QtCore.QSize(75, 75))
        self.orianna_button.setFlat(False)
        self.orianna_button.setObjectName("orianna_button")
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
        icon8.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_poppy_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon9.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_renekton_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renekton_button.setIcon(icon9)
        self.renekton_button.setIconSize(QtCore.QSize(75, 75))
        self.renekton_button.setFlat(False)
        self.renekton_button.setObjectName("renekton_button")
        self.samira_button = QtWidgets.QPushButton(self.tier_one)
        self.samira_button.setGeometry(QtCore.QRect(460, 130, 82, 82))
        self.samira_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.samira_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_samira_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.samira_button.setIcon(icon10)
        self.samira_button.setIconSize(QtCore.QSize(75, 75))
        self.samira_button.setFlat(False)
        self.samira_button.setObjectName("samira_button")
        self.tristana_button = QtWidgets.QPushButton(self.tier_one)
        self.tristana_button.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.tristana_button.setStyleSheet("QPushButton {\n"
                                        "background: #9f9b92;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.tristana_button.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_tristana_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tristana_button.setIcon(icon11)
        self.tristana_button.setIconSize(QtCore.QSize(75, 75))
        self.tristana_button.setFlat(False)
        self.tristana_button.setObjectName("tristana_button")
        self.viego_button= QtWidgets.QPushButton(self.tier_one)
        self.viego_button.setGeometry(QtCore.QRect(20, 240, 82, 82))
        self.viego_button.setStyleSheet("QPushButton {\n"
                                         "background: #9f9b92;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.viego_button  .setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_viego_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viego_button.setIcon(icon12)
        self.viego_button.setIconSize(QtCore.QSize(75, 75))
        self.viego_button.setFlat(False)
        self.viego_button.setObjectName("viego_button")
        self.champion_tab.addTab(self.tier_one, "")
        self.tier_two = QtWidgets.QWidget()
        self.tier_two.setObjectName("tier_two")
        self.ashe_button = QtWidgets.QPushButton(self.tier_two)
        self.ashe_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.ashe_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.ashe_button.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ashe_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ashe_button.setIcon(icon13)
        self.ashe_button.setIconSize(QtCore.QSize(75, 75))
        self.ashe_button.setFlat(False)
        self.ashe_button.setObjectName("ashe_button")
        self.galio_button = QtWidgets.QPushButton(self.tier_two)
        self.galio_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.galio_button.setStyleSheet("QPushButton {\n"
                                          "background: #25b05c;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.galio_button.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_galio_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.galio_button.setIcon(icon14)
        self.galio_button.setIconSize(QtCore.QSize(75, 75))
        self.galio_button.setFlat(False)
        self.galio_button.setObjectName("galio_button")
        self.jinx_button = QtWidgets.QPushButton(self.tier_two)
        self.jinx_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.jinx_button.setStyleSheet("QPushButton {\n"
                                         "background: #25b05c;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.jinx_button.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_jinx_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jinx_button.setIcon(icon15)
        self.jinx_button.setIconSize(QtCore.QSize(75, 75))
        self.jinx_button.setFlat(False)
        self.jinx_button.setObjectName("jinx_button")
        self.kassadin_button = QtWidgets.QPushButton(self.tier_two)
        self.kassadin_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.kassadin_button.setStyleSheet("QPushButton {\n"
                                         "background: #25b05c;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.kassadin_button.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kassadin_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kassadin_button.setIcon(icon16)
        self.kassadin_button.setIconSize(QtCore.QSize(75, 75))
        self.kassadin_button.setFlat(False)
        self.kassadin_button.setObjectName("kassadin_button")
        self.kled_button = QtWidgets.QPushButton(self.tier_two)
        self.kled_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.kled_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.kled_button.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kled_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kled_button.setIcon(icon17)
        self.kled_button.setIconSize(QtCore.QSize(75, 75))
        self.kled_button.setFlat(False)
        self.kled_button.setObjectName("kled_button")
        self.sett_button = QtWidgets.QPushButton(self.tier_two)
        self.sett_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.sett_button.setStyleSheet("QPushButton {\n"
                                       "background: #25b05c;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.sett_button.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_sett_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sett_button.setIcon(icon18)
        self.sett_button.setIconSize(QtCore.QSize(75, 75))
        self.sett_button.setFlat(False)
        self.sett_button.setObjectName("sett_button")
        self.soraka_button = QtWidgets.QPushButton(self.tier_two)
        self.soraka_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.soraka_button.setStyleSheet("QPushButton {\n"
                                         "background: #25b05c;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.soraka_button.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_soraka_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soraka_button.setIcon(icon19)
        self.soraka_button.setIconSize(QtCore.QSize(75, 75))
        self.soraka_button.setFlat(False)
        self.soraka_button.setObjectName("soraka_button")
        self.swain_button = QtWidgets.QPushButton(self.tier_two)
        self.swain_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.swain_button.setStyleSheet("QPushButton {\n"
                                           "background: #25b05c;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.swain_button.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_swain_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.swain_button.setIcon(icon20)
        self.swain_button.setIconSize(QtCore.QSize(75, 75))
        self.swain_button.setFlat(False)
        self.swain_button.setObjectName("swain_button")
        self.taliyah_button = QtWidgets.QPushButton(self.tier_two)
        self.taliyah_button.setGeometry(QtCore.QRect(240, 130, 82, 82))
        self.taliyah_button.setStyleSheet("QPushButton {\n"
                                       "background: #25b05c;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.taliyah_button.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_taliyah_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.taliyah_button.setIcon(icon21)
        self.taliyah_button.setIconSize(QtCore.QSize(75, 75))
        self.taliyah_button.setFlat(False)
        self.taliyah_button.setObjectName("taliyah_button")
        self.teemo_button = QtWidgets.QPushButton(self.tier_two)
        self.teemo_button.setGeometry(QtCore.QRect(350, 130, 82, 82))
        self.teemo_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.teemo_button.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_teemo_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.teemo_button.setIcon(icon22)
        self.teemo_button.setIconSize(QtCore.QSize(75, 75))
        self.teemo_button.setFlat(False)
        self.teemo_button.setObjectName("teemo_button")
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
        icon23.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_vi_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vi_button.setIcon(icon23)
        self.vi_button.setIconSize(QtCore.QSize(75, 75))
        self.vi_button.setFlat(False)
        self.vi_button.setObjectName("vi_button")
        self.warwick_button = QtWidgets.QPushButton(self.tier_two)
        self.warwick_button.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.warwick_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.warwick_button.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_warwick_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.warwick_button.setIcon(icon24)
        self.warwick_button.setIconSize(QtCore.QSize(75, 75))
        self.warwick_button.setFlat(False)
        self.warwick_button.setObjectName("warwick_button")
        self.zed_button = QtWidgets.QPushButton(self.tier_two)
        self.zed_button.setGeometry(QtCore.QRect(20, 240, 82, 82))
        self.zed_button.setStyleSheet("QPushButton {\n"
                                        "background: #25b05c;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.zed_button.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_zed_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zed_button.setIcon(icon25)
        self.zed_button.setIconSize(QtCore.QSize(75, 75))
        self.zed_button.setFlat(False)
        self.zed_button.setObjectName("zed_button")
        self.champion_tab.addTab(self.tier_two, "")
        self.tier_three = QtWidgets.QWidget()
        self.tier_three.setObjectName("tier_three")
        self.akshan_button = QtWidgets.QPushButton(self.tier_three)
        self.akshan_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.akshan_button.setStyleSheet("QPushButton {\n"
                                          "background: #26a5c9;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.akshan_button.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_akshan_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.akshan_button.setIcon(icon26)
        self.akshan_button.setIconSize(QtCore.QSize(75, 75))
        self.akshan_button.setFlat(False)
        self.akshan_button.setObjectName("akshan_button")
        self.darius_button = QtWidgets.QPushButton(self.tier_three)
        self.darius_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.darius_button.setStyleSheet("QPushButton {\n"
                                          "background: #26a5c9;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.darius_button.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_darius_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.darius_button.setIcon(icon27)
        self.darius_button.setIconSize(QtCore.QSize(75, 75))
        self.darius_button.setFlat(False)
        self.darius_button.setObjectName("darius_button")
        self.ekko_button = QtWidgets.QPushButton(self.tier_three)
        self.ekko_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.ekko_button.setStyleSheet("QPushButton {\n"
                                      "background: #26a5c9;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.ekko_button.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ekko_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ekko_button.setIcon(icon28)
        self.ekko_button.setIconSize(QtCore.QSize(75, 75))
        self.ekko_button.setFlat(False)
        self.ekko_button.setObjectName("ekko_button")
        self.garen_button = QtWidgets.QPushButton(self.tier_three)
        self.garen_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.garen_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.garen_button.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_garen_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.garen_button.setIcon(icon29)
        self.garen_button.setIconSize(QtCore.QSize(75, 75))
        self.garen_button.setFlat(False)
        self.garen_button.setObjectName("garen_button")
        self.jayce_button = QtWidgets.QPushButton(self.tier_three)
        self.jayce_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.jayce_button.setStyleSheet("QPushButton {\n"
                                          "background: #26a5c9;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.jayce_button.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_jayce_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jayce_button.setIcon(icon30)
        self.jayce_button.setIconSize(QtCore.QSize(75, 75))
        self.jayce_button.setFlat(False)
        self.jayce_button.setObjectName("jayce_button")
        self.kalista_button = QtWidgets.QPushButton(self.tier_three)
        self.kalista_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.kalista_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.kalista_button.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kalista_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kalista_button.setIcon(icon31)
        self.kalista_button.setIconSize(QtCore.QSize(75, 75))
        self.kalista_button.setFlat(False)
        self.kalista_button.setObjectName("kalista_button")
        self.karma_button = QtWidgets.QPushButton(self.tier_three)
        self.karma_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.karma_button.setStyleSheet("QPushButton {\n"
                                         "background: #26a5c9;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.karma_button.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_karma_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.karma_button.setIcon(icon32)
        self.karma_button.setIconSize(QtCore.QSize(75, 75))
        self.karma_button.setFlat(False)
        self.karma_button.setObjectName("karma_button")
        self.katarina_button = QtWidgets.QPushButton(self.tier_three)
        self.katarina_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.katarina_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.katarina_button.setText("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_katarina_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.katarina_button.setIcon(icon33)
        self.katarina_button.setIconSize(QtCore.QSize(75, 75))
        self.katarina_button.setFlat(False)
        self.katarina_button.setObjectName("katarina_button")
        self.lissandra_button = QtWidgets.QPushButton(self.tier_three)
        self.lissandra_button.setGeometry(QtCore.QRect(240, 130, 82, 82))
        self.lissandra_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.lissandra_button.setText("")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_lissandra_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lissandra_button.setIcon(icon34)
        self.lissandra_button.setIconSize(QtCore.QSize(75, 75))
        self.lissandra_button.setFlat(False)
        self.lissandra_button.setObjectName("lissandra_button")
        self.reksai_button = QtWidgets.QPushButton(self.tier_three)
        self.reksai_button.setGeometry(QtCore.QRect(350, 130, 82, 82))
        self.reksai_button.setStyleSheet("QPushButton {\n"
                                       "background: #26a5c9;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.reksai_button.setText("")
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_reksai_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reksai_button.setIcon(icon35)
        self.reksai_button.setIconSize(QtCore.QSize(75, 75))
        self.reksai_button.setFlat(False)
        self.reksai_button.setObjectName("reksai_button")
        self.sona_button = QtWidgets.QPushButton(self.tier_three)
        self.sona_button.setGeometry(QtCore.QRect(460, 130, 82, 82))
        self.sona_button.setStyleSheet("QPushButton {\n"
                                        "background: #26a5c9;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.sona_button.setText("")
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_sona_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sona_button.setIcon(icon36)
        self.sona_button.setIconSize(QtCore.QSize(75, 75))
        self.sona_button.setFlat(False)
        self.sona_button.setObjectName("sona_button")
        self.taric_button = QtWidgets.QPushButton(self.tier_three)
        self.taric_button.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.taric_button.setStyleSheet("QPushButton {\n"
                                         "background: #26a5c9;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.taric_button.setText("")
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_taric_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.taric_button.setIcon(icon37)
        self.taric_button.setIconSize(QtCore.QSize(75, 75))
        self.taric_button.setFlat(False)
        self.taric_button.setObjectName("taric_button")
        self.velkoz_button = QtWidgets.QPushButton(self.tier_three)
        self.velkoz_button.setGeometry(QtCore.QRect(20, 240, 82, 82))
        self.velkoz_button.setStyleSheet("QPushButton {\n"
                                      "background: #26a5c9;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.velkoz_button.setText("")
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_velkoz_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.velkoz_button.setIcon(icon38)
        self.velkoz_button.setIconSize(QtCore.QSize(75, 75))
        self.velkoz_button.setFlat(False)
        self.velkoz_button.setObjectName("velkoz_button")
        self.champion_tab.addTab(self.tier_three, "")
        self.tier_four = QtWidgets.QWidget()
        self.tier_four.setObjectName("tier_four")
        self.alphelios_button = QtWidgets.QPushButton(self.tier_four)
        self.alphelios_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.alphelios_button.setStyleSheet("QPushButton {\n"
                                              "background: #6610f2;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.alphelios_button.setText("")
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_aphelios_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alphelios_button.setIcon(icon39)
        self.alphelios_button.setIconSize(QtCore.QSize(75, 75))
        self.alphelios_button.setFlat(False)
        self.alphelios_button.setObjectName("alphelios_button")
        self.azir_button = QtWidgets.QPushButton(self.tier_four)
        self.azir_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.azir_button.setStyleSheet("QPushButton {\n"
                                          "background: #6610f2;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.azir_button.setText("")
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_azir_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.azir_button.setIcon(icon40)
        self.azir_button.setIconSize(QtCore.QSize(75, 75))
        self.azir_button.setFlat(False)
        self.azir_button.setObjectName("azir_button")
        self.gwen_button = QtWidgets.QPushButton(self.tier_four)
        self.gwen_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.gwen_button.setStyleSheet("QPushButton {\n"
                                       "background: #6610f2;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.gwen_button.setText("")
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_gwen_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gwen_button.setIcon(icon41)
        self.gwen_button.setIconSize(QtCore.QSize(75, 75))
        self.gwen_button.setFlat(False)
        self.gwen_button.setObjectName("gwen_button")
        self.jarvan_button = QtWidgets.QPushButton(self.tier_four)
        self.jarvan_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.jarvan_button.setStyleSheet("QPushButton {\n"
                                              "background: #6610f2;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.jarvan_button.setText("")
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_jarvaniv_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jarvan_button.setIcon(icon42)
        self.jarvan_button.setIconSize(QtCore.QSize(75, 75))
        self.jarvan_button.setFlat(False)
        self.jarvan_button.setObjectName("jarvan_button")
        self.kaisa_button = QtWidgets.QPushButton(self.tier_four)
        self.kaisa_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.kaisa_button.setStyleSheet("QPushButton {\n"
                                         "background: #6610f2;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.kaisa_button.setText("")
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kaisa_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kaisa_button.setIcon(icon43)
        self.kaisa_button.setIconSize(QtCore.QSize(75, 75))
        self.kaisa_button.setFlat(False)
        self.kaisa_button.setObjectName("kaisa_button")
        self.lux_button = QtWidgets.QPushButton(self.tier_four)
        self.lux_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.lux_button.setStyleSheet("QPushButton {\n"
                                          "background: #6610f2;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.lux_button.setText("")
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_lux_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lux_button.setIcon(icon44)
        self.lux_button.setIconSize(QtCore.QSize(75, 75))
        self.lux_button.setFlat(False)
        self.lux_button.setObjectName("lux_button")
        self.nasus_button = QtWidgets.QPushButton(self.tier_four)
        self.nasus_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.nasus_button.setStyleSheet("QPushButton {\n"
                                       "background: #6610f2;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.nasus_button.setText("")
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_nasus_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nasus_button.setIcon(icon45)
        self.nasus_button.setIconSize(QtCore.QSize(75, 75))
        self.nasus_button.setFlat(False)
        self.nasus_button.setObjectName("nasus_button")
        self.sejuani_button = QtWidgets.QPushButton(self.tier_four)
        self.sejuani_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.sejuani_button.setStyleSheet("QPushButton {\n"
                                         "background: #6610f2;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.sejuani_button.setText("")
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_sejuani_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sejuani_button.setIcon(icon46)
        self.sejuani_button.setIconSize(QtCore.QSize(75, 75))
        self.sejuani_button.setFlat(False)
        self.sejuani_button.setObjectName("sejuani_button")
        self.shen_button = QtWidgets.QPushButton(self.tier_four)
        self.shen_button.setGeometry(QtCore.QRect(240, 131, 82, 82))
        self.shen_button.setStyleSheet("QPushButton {\n"
                                          "background: #6610f2;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.shen_button.setText("")
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_shen_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shen_button.setIcon(icon47)
        self.shen_button.setIconSize(QtCore.QSize(75, 75))
        self.shen_button.setFlat(False)
        self.shen_button.setObjectName("shen_button")
        self.urgot_button = QtWidgets.QPushButton(self.tier_four)
        self.urgot_button.setGeometry(QtCore.QRect(350, 130, 82, 82))
        self.urgot_button.setStyleSheet("QPushButton {\n"
                                        "background: #6610f2;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.urgot_button.setText("")
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_urgot_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.urgot_button.setIcon(icon48)
        self.urgot_button.setIconSize(QtCore.QSize(75, 75))
        self.urgot_button.setFlat(False)
        self.urgot_button.setObjectName("urgot_button")
        self.yasuo_button = QtWidgets.QPushButton(self.tier_four)
        self.yasuo_button.setGeometry(QtCore.QRect(460, 130, 82, 82))
        self.yasuo_button.setStyleSheet("QPushButton {\n"
                                      "background: #6610f2;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.yasuo_button.setText("")
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_yasuo_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yasuo_button.setIcon(icon49)
        self.yasuo_button.setIconSize(QtCore.QSize(75, 75))
        self.yasuo_button.setFlat(False)
        self.yasuo_button.setObjectName("yasuo_button")
        self.zeri_button = QtWidgets.QPushButton(self.tier_four)
        self.zeri_button.setGeometry(QtCore.QRect(570, 130, 82, 82))
        self.zeri_button.setStyleSheet("QPushButton {\n"
                                      "background: #6610f2;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background: white;\n"
                                      "}")
        self.zeri_button.setText("")
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_zeri_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zeri_button.setIcon(icon50)
        self.zeri_button.setIconSize(QtCore.QSize(75, 75))
        self.zeri_button.setFlat(False)
        self.zeri_button.setObjectName("zeri_button")
        self.champion_tab.addTab(self.tier_four, "")
        self.tier_five = QtWidgets.QWidget()
        self.tier_five.setObjectName("tier_five")
        self.aatrox_button = QtWidgets.QPushButton(self.tier_five)
        self.aatrox_button.setGeometry(QtCore.QRect(20, 20, 82, 82))
        self.aatrox_button.setStyleSheet("QPushButton {\n"
                                           "background: #f9b428;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.aatrox_button.setText("")
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_aatrox_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aatrox_button.setIcon(icon51)
        self.aatrox_button.setIconSize(QtCore.QSize(75, 75))
        self.aatrox_button.setFlat(False)
        self.aatrox_button.setObjectName("aatrox_button")
        self.ahri_button = QtWidgets.QPushButton(self.tier_five)
        self.ahri_button.setGeometry(QtCore.QRect(130, 20, 82, 82))
        self.ahri_button.setStyleSheet("QPushButton {\n"
                                               "background: #f9b428;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "background: white;\n"
                                               "}")
        self.ahri_button.setText("")
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ahri_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ahri_button.setIcon(icon52)
        self.ahri_button.setIconSize(QtCore.QSize(75, 75))
        self.ahri_button.setFlat(False)
        self.ahri_button.setObjectName("ahri_button")
        self.belveth_button = QtWidgets.QPushButton(self.tier_five)
        self.belveth_button.setGeometry(QtCore.QRect(240, 20, 82, 82))
        self.belveth_button.setStyleSheet("QPushButton {\n"
                                        "background: #f9b428;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.belveth_button.setText("")
        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_belveth_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.belveth_button.setIcon(icon53)
        self.belveth_button.setIconSize(QtCore.QSize(75, 75))
        self.belveth_button.setFlat(False)
        self.belveth_button.setObjectName("belveth_button")
        self.sion_button = QtWidgets.QPushButton(self.tier_five)
        self.sion_button.setGeometry(QtCore.QRect(20, 130, 82, 82))
        self.sion_button.setStyleSheet("QPushButton {\n"
                                         "background: #f9b428;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.sion_button.setText("")
        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_sion_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sion_button.setIcon(icon54)
        self.sion_button.setIconSize(QtCore.QSize(75, 75))
        self.sion_button.setFlat(False)
        self.sion_button.setObjectName("sion_button")
        self.heimerdinger_button = QtWidgets.QPushButton(self.tier_five)
        self.heimerdinger_button.setGeometry(QtCore.QRect(350, 20, 82, 82))
        self.heimerdinger_button.setStyleSheet("QPushButton {\n"
                                        "background: #f9b428;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.heimerdinger_button.setText("")
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_heimerdinger_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heimerdinger_button.setIcon(icon55)
        self.heimerdinger_button.setIconSize(QtCore.QSize(75, 75))
        self.heimerdinger_button.setFlat(False)
        self.heimerdinger_button.setObjectName("heimerdinger_button")
        self.ksante_button = QtWidgets.QPushButton(self.tier_five)
        self.ksante_button.setGeometry(QtCore.QRect(460, 20, 82, 82))
        self.ksante_button.setStyleSheet("QPushButton {\n"
                                              "background: #f9b428;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.ksante_button.setText("")
        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ksante_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ksante_button.setIcon(icon56)
        self.ksante_button.setIconSize(QtCore.QSize(75, 75))
        self.ksante_button.setFlat(False)
        self.ksante_button.setObjectName("ksante_button")
        self.senna_button = QtWidgets.QPushButton(self.tier_five)
        self.senna_button.setGeometry(QtCore.QRect(570, 20, 82, 82))
        self.senna_button.setStyleSheet("QPushButton {\n"
                                       "background: #f9b428;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background: white;\n"
                                       "}")
        self.senna_button.setText("")
        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_senna_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.senna_button.setIcon(icon57)
        self.senna_button.setIconSize(QtCore.QSize(75, 75))
        self.senna_button.setFlat(False)
        self.senna_button.setObjectName("senna_button")
        self.ryze_button = QtWidgets.QPushButton(self.tier_five)
        self.ryze_button.setGeometry(QtCore.QRect(130, 130, 82, 82))
        self.ryze_button.setStyleSheet("QPushButton {\n"
                                        "background: #f9b428;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background: white;\n"
                                        "}")
        self.ryze_button.setText("")
        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ryze_mobile.tft_set9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ryze_button.setIcon(icon58)
        self.ryze_button.setIconSize(QtCore.QSize(75, 75))
        self.ryze_button.setFlat(False)
        self.ryze_button.setObjectName("ryze_button")
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
        self.selected_level.setScaledContents(True)
        self.champion_tab.raise_()
        self.champion_name.raise_()
        self.selected_champion.raise_()
        self.next_button.raise_()
        self.selected_level.raise_()

        self.retranslate_ui_champion_selector_window(champion_level_selector)
        self.champion_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(champion_level_selector)

        self.cassiopeia_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_cassiopeia_mobile.tft_set9.png", "Cassiopeia"))
        self.chogath_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_chogath_mobile.tft_set9.png", "Chogath"))
        self.irelia_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_irelia_mobile.tft_set9.png", "Irelia"))
        self.jhin_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_jhin_mobile.tft_set9.png", "Jhin"))
        self.kayle_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kayle_mobile.tft_set9.png", "Kayle"))
        self.malzahar_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_malzahar_mobile.tft_set9.png", "Malzahar"))
        self.maokai_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_maokai_mobile.tft_set9.png", "Maokai"))
        self.orianna_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_orianna_mobile.tft_set9.png", "Orianna"))
        self.poppy_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_poppy_mobile.tft_set9.png", "Poppy"))
        self.renekton_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_renekton_mobile.tft_set9.png", "Renekton"))
        self.samira_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_samira_mobile.tft_set9.png", "Samira"))
        self.tristana_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_tristana_mobile.tft_set9.png", "Tristana"))
        self.viego_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_viego_mobile.tft_set9.png", "Viego"))

        self.ashe_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ashe_mobile.tft_set9.png", "Ashe"))
        self.galio_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_galio_mobile.tft_set9.png", "Galio"))
        self.jinx_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_jinx_mobile.tft_set9.png", "Jinx"))
        self.kassadin_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kassadin_mobile.tft_set9.png", "Kassadin"))
        self.kled_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kled_mobile.tft_set9.png", "Kled"))
        self.sett_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_sett_mobile.tft_set9.png", "Sett"))
        self.soraka_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_soraka_mobile.tft_set9.png", "Soraka"))
        self.swain_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_swain_mobile.tft_set9.png", "Swain"))
        self.taliyah_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_taliyah_mobile.tft_set9.png", "Taliyah"))
        self.teemo_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_teemo_mobile.tft_set9.png", "Teemo"))
        self.vi_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_vi_mobile.tft_set9.png", "Vi"))
        self.warwick_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_warwick_mobile.tft_set9.png", "Warwick"))
        self.zed_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_zed_mobile.tft_set9.png", "Zed"))

        self.akshan_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_akshan_mobile.tft_set9.png", "Akshan"))
        self.darius_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_darius_mobile.tft_set9.png", "Darius"))
        self.ekko_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ekko_mobile.tft_set9.png", "Ekko")) #
        self.garen_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_garen_mobile.tft_set9.png", "Garen"))
        self.jayce_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_jayce_mobile.tft_set9.png", "Jayce"))
        self.kalista_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kalista_mobile.tft_set9.png", "Kalista"))
        self.karma_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_karma_mobile.tft_set9.png", "Karma"))
        self.katarina_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_katarina_mobile.tft_set9.png", "Katarina"))
        self.lissandra_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_lissandra_mobile.tft_set9.png", "Lissandra"))
        self.reksai_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_reksai_mobile.tft_set9.png", "RekSai"))
        self.sona_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_sona_mobile.tft_set9.png", "Sona"))
        self.taric_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_taric_mobile.tft_set9.png", "Taric"))
        self.velkoz_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_velkoz_mobile.tft_set9.png", "Velkoz"))

        self.alphelios_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_aphelios_mobile.tft_set9.png", "Alphelios"))
        self.azir_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_azir_mobile.tft_set9.png", "Azir"))
        self.gwen_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_gwen_mobile.tft_set9.png", "Gwen"))
        self.jarvan_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_jarvaniv_mobile.tft_set9.png", "Jarvan IV"))
        self.kaisa_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_kaisa_mobile.tft_set9.png", "Kaisa"))
        self.lux_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_lux_mobile.tft_set9.png", "Lux"))
        self.nasus_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_nasus_mobile.tft_set9.png", "Nasus"))
        self.sejuani_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_sejuani_mobile.tft_set9.png", "Sejuani"))
        self.shen_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_shen_mobile.tft_set9.png", "Shen"))
        self.urgot_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_urgot_mobile.tft_set9.png", "Urgot"))
        self.yasuo_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_yasuo_mobile.tft_set9.png", "Yasuo"))
        self.zeri_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_zeri_mobile.tft_set9.png", "Zeri"))

        self.aatrox_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_aatrox_mobile.tft_set9.png", "Aatrox"))
        self.ahri_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ahri_mobile.tft_set9.png", "Ahri"))
        self.belveth_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_belveth_mobile.tft_set9.png", "Belveth"))
        self.heimerdinger_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_heimerdinger_mobile.tft_set9.png", "Heimerdinger"))
        self.ksante_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ksante_mobile.tft_set9.png", "Ksante"))
        self.senna_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_senna_mobile.tft_set9.png", "Senna"))
        self.sion_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_sion_mobile.tft_set9.png", "Sion"))
        self.ryze_button.clicked.connect(lambda: self.unit_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/TFT9/CHAMPIONS/tft9_ryze_mobile.tft_set9.png", "Ryze"))

        self.next_button.clicked.connect(lambda: self.next_clicked(board_window, champion_level_selector, position, state))

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

    tracker = 0

    def unit_clicked(self, image_path, champion_name):
        if self.champion_name.text() == champion_name:
            if self.tracker == 1:
                self.tracker = 2
                self.selected_level.setPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Two.png"))
            elif self.tracker == 2:
                self.tracker = 3
                self.selected_level.setPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Three.png"))
            elif self.tracker == 3:
                self.tracker = 1
                self.selected_level.setPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/One.png"))
        else:
            self.selected_level.setPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/One.png"))
            self.champion_name.setText(champion_name)
            self.selected_champion.setPixmap(QtGui.QPixmap(image_path))
            self.tracker = 1

    def next_clicked(self, board_window, champion_window, position, state):
        if self.champion_name.text() == "Name":
            print("test - worked no champion selected")
        else:
            ##self.open_item_window(board_window, champion_window, state, self.champion_name.text())
            self.open_item_window(board_window, champion_window, self.champion_name.text(), self.tracker, position, state)