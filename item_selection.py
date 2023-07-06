from PyQt5 import QtCore, QtGui, QtWidgets

class UI_Item_Selector(object):

    def update_board(self, board_window):
        self.board_window.enemy_unit_1_1.setText("test")

    def setup_ui_item_selector(self, item_selector, main_window, board_window, champion_window, selected_champion, selected_level, position, state):

        main_window_ref = main_window
        champion_window_ref = champion_window
        board_window_ref = board_window
        item_selector_ref = item_selector

        item_selector.setObjectName("item_selector")
        item_selector.resize(1084, 459)
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
        item_selector.setPalette(palette)
        self.next_button = QtWidgets.QPushButton(item_selector)
        self.next_button.setGeometry(QtCore.QRect(960, 350, 101, 41))
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
        self.next_button.setIconSize(QtCore.QSize(75, 75))
        self.next_button.setObjectName("next_button")
        self.predict_button = QtWidgets.QPushButton(item_selector)
        self.predict_button.setGeometry(QtCore.QRect(960, 400, 101, 41))
        self.predict_button.setStyleSheet("QPushButton {\n"
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
        self.predict_button.setIconSize(QtCore.QSize(75, 75))
        self.predict_button.setObjectName("predict_button")
        self.selected_item_1 = QtWidgets.QLabel(item_selector)
        self.selected_item_1.setGeometry(QtCore.QRect(760, 160, 82, 82))
        self.selected_item_1.setAutoFillBackground(False)
        self.selected_item_1.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid white;\n"
                                               "}\n"
                                               "")
        self.selected_item_1.setText("")
        self.selected_item_1.setScaledContents(True)
        self.selected_item_1.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_item_1.setObjectName("selected_item_1")
        self.item_tab = QtWidgets.QTabWidget(item_selector)
        self.item_tab.setGeometry(QtCore.QRect(20, 20, 700, 380))
        self.item_tab.setStyleSheet("background-color: rgb(18, 48, 64);")
        self.item_tab.setDocumentMode(True)
        self.item_tab.setObjectName("item_tab")
        self.standard = QtWidgets.QWidget()
        self.standard.setObjectName("standard")
        self.standard_scroll_area = QtWidgets.QScrollArea(self.standard)
        self.standard_scroll_area.setGeometry(QtCore.QRect(-1, -1, 700, 360))
        self.standard_scroll_area.setMinimumSize(QtCore.QSize(700, 360))
        self.standard_scroll_area.setMaximumSize(QtCore.QSize(700, 360))
        self.standard_scroll_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.standard_scroll_area.setWidgetResizable(True)
        self.standard_scroll_area.setObjectName("standard_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 681, 628))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.standard_button_47 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_47.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_47.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_47.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_47.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/zzrot_portal.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_47.setIcon(icon)
        self.standard_button_47.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_47.setObjectName("standard_button_47")
        self.gridLayout.addWidget(self.standard_button_47, 7, 6, 1, 1)
        self.standard_button_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_14.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_14.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_14.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_14.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/guinsoos_rageblade.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_14.setIcon(icon1)
        self.standard_button_14.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_14.setObjectName("standard_button_14")
        self.gridLayout.addWidget(self.standard_button_14, 2, 2, 1, 1)
        self.standard_button_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_15.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_15.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_15.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_15.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/hextech_gunblade.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_15.setIcon(icon2)
        self.standard_button_15.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_15.setObjectName("standard_button_15")
        self.gridLayout.addWidget(self.standard_button_15, 2, 4, 1, 1)
        self.standard_button_29 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_29.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_29.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_29.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_29.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/runaans_hurricane.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_29.setIcon(icon3)
        self.standard_button_29.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_29.setObjectName("standard_button_29")
        self.gridLayout.addWidget(self.standard_button_29, 5, 4, 1, 1)
        self.standard_button_23 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_23.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_23.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_23.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_23.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/negatron_cloak.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_23.setIcon(icon4)
        self.standard_button_23.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_23.setObjectName("standard_button_23")
        self.gridLayout.addWidget(self.standard_button_23, 4, 5, 1, 1)
        self.standard_button_37 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_37.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_37.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_37.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_37.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/tacticians_crown.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_37.setIcon(icon5)
        self.standard_button_37.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_37.setObjectName("standard_button_37")
        self.gridLayout.addWidget(self.standard_button_37, 6, 5, 1, 1)
        self.standard_button_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_6.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_6.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_6.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/chalice_of_power.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_6.setIcon(icon6)
        self.standard_button_6.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_6.setObjectName("standard_button_6")
        self.gridLayout.addWidget(self.standard_button_6, 0, 8, 1, 1)
        self.standard_button_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_1.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_1.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_1.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/archangels_staff.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_1.setIcon(icon7)
        self.standard_button_1.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_1.setObjectName("standard_button_1")
        self.gridLayout.addWidget(self.standard_button_1, 0, 2, 1, 1)
        self.standard_button_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_3.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_3.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_3.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_3.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/bloodthirster.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_3.setIcon(icon8)
        self.standard_button_3.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_3.setObjectName("standard_button_3")
        self.gridLayout.addWidget(self.standard_button_3, 0, 4, 1, 1)
        self.standard_button_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_2.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_2.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_2.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_2.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/bf_sword.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_2.setIcon(icon9)
        self.standard_button_2.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_2.setObjectName("standard_button_2")
        self.gridLayout.addWidget(self.standard_button_2, 0, 3, 1, 1)
        self.standard_button_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_4.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_4.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_4.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_4.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/blue_buff.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_4.setIcon(icon10)
        self.standard_button_4.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_4.setObjectName("standard_button_4")
        self.gridLayout.addWidget(self.standard_button_4, 0, 5, 1, 1)
        self.standard_button_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_5.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_5.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_5.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_5.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/bramble_vest.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_5.setIcon(icon11)
        self.standard_button_5.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_5.setObjectName("standard_button_5")
        self.gridLayout.addWidget(self.standard_button_5, 0, 6, 1, 1)
        self.standard_button_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_17.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_17.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_17.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_17.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/ionic_spark.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_17.setIcon(icon12)
        self.standard_button_17.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_17.setObjectName("standard_button_17")
        self.gridLayout.addWidget(self.standard_button_17, 2, 6, 1, 1)
        self.standard_button_22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_22.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_22.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_22.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_22.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/needlessly_large_rod.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_22.setIcon(icon13)
        self.standard_button_22.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_22.setObjectName("standard_button_22")
        self.gridLayout.addWidget(self.standard_button_22, 4, 4, 1, 1)
        self.standard_button_24 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_24.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_24.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_24.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_24.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/quicksilver.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_24.setIcon(icon14)
        self.standard_button_24.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_24.setObjectName("standard_button_24")
        self.gridLayout.addWidget(self.standard_button_24, 4, 6, 1, 1)
        self.standard_button_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_13.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_13.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_13.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_13.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/guardian_angel.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_13.setIcon(icon15)
        self.standard_button_13.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_13.setObjectName("standard_button_13")
        self.gridLayout.addWidget(self.standard_button_13, 1, 8, 1, 1)
        self.standard_button_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_10.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_10.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_10.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_10.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/giants_belt.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_10.setIcon(icon16)
        self.standard_button_10.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_10.setObjectName("standard_button_10")
        self.gridLayout.addWidget(self.standard_button_10, 1, 5, 1, 1)
        self.standard_button_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_9.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_9.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_9.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_9.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/edge_of_night.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_9.setIcon(icon17)
        self.standard_button_9.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_9.setObjectName("standard_button_9")
        self.gridLayout.addWidget(self.standard_button_9, 1, 4, 1, 1)
        self.standard_button_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_18.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_18.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_18.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_18.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/jeweled_gauntlet.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_18.setIcon(icon18)
        self.standard_button_18.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_18.setObjectName("standard_button_18")
        self.gridLayout.addWidget(self.standard_button_18, 2, 7, 1, 1)
        self.standard_button_31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_31.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_31.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_31.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_31.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/sparring_gloves.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_31.setIcon(icon19)
        self.standard_button_31.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_31.setObjectName("standard_button_31")
        self.gridLayout.addWidget(self.standard_button_31, 5, 6, 1, 1)
        self.standard_button_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_20.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_20.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_20.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_20.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/locket_of_the_iron_solari.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_20.setIcon(icon20)
        self.standard_button_20.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_20.setObjectName("standard_button_20")
        self.gridLayout.addWidget(self.standard_button_20, 4, 2, 1, 1)
        self.standard_button_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_19.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_19.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_19.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_19.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/last_whisper.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_19.setIcon(icon21)
        self.standard_button_19.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_19.setObjectName("standard_button_19")
        self.gridLayout.addWidget(self.standard_button_19, 2, 8, 1, 1)
        self.standard_button_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_21.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_21.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_21.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_21.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/morellonomicon.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_21.setIcon(icon22)
        self.standard_button_21.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_21.setObjectName("standard_button_21")
        self.gridLayout.addWidget(self.standard_button_21, 4, 3, 1, 1)
        self.standard_button_25 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_25.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_25.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_25.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_25.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/rabadons_deathcap.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_25.setIcon(icon23)
        self.standard_button_25.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_25.setObjectName("standard_button_25")
        self.gridLayout.addWidget(self.standard_button_25, 4, 7, 1, 1)
        self.standard_button_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_12.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_12.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_12.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_12.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/giant_slayer.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_12.setIcon(icon24)
        self.standard_button_12.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_12.setObjectName("standard_button_12")
        self.gridLayout.addWidget(self.standard_button_12, 1, 7, 1, 1)
        self.standard_button_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_16.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_16.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_16.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_16.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/infinity_edge.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_16.setIcon(icon25)
        self.standard_button_16.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_16.setObjectName("standard_button_16")
        self.gridLayout.addWidget(self.standard_button_16, 2, 5, 1, 1)
        self.standard_button_46 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_46.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_46.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_46.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_46.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/hand_of_justice.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_46.setIcon(icon26)
        self.standard_button_46.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_46.setObjectName("standard_button_46")
        self.gridLayout.addWidget(self.standard_button_46, 2, 3, 1, 1)
        self.standard_button_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_7.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_7.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_7.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_7.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/death_blade.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_7.setIcon(icon27)
        self.standard_button_7.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_7.setObjectName("standard_button_7")
        self.gridLayout.addWidget(self.standard_button_7, 1, 2, 1, 1)
        self.standard_button_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_11.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_11.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_11.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_11.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/gargoyle_stoneplate.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_11.setIcon(icon28)
        self.standard_button_11.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_11.setObjectName("standard_button_11")
        self.gridLayout.addWidget(self.standard_button_11, 1, 6, 1, 1)
        self.standard_button_26 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_26.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_26.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_26.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_26.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/rapid_fire_cannon.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_26.setIcon(icon29)
        self.standard_button_26.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_26.setObjectName("standard_button_26")
        self.gridLayout.addWidget(self.standard_button_26, 4, 8, 1, 1)
        self.standard_button_35 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_35.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_35.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_35.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_35.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/guardbreaker.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_35.setIcon(icon30)
        self.standard_button_35.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_35.setObjectName("standard_button_35")
        self.gridLayout.addWidget(self.standard_button_35, 6, 3, 1, 1)
        self.standard_button_45 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_45.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_45.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_45.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_45.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/chain_vest.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_45.setIcon(icon31)
        self.standard_button_45.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_45.setObjectName("standard_button_45")
        self.gridLayout.addWidget(self.standard_button_45, 0, 7, 1, 1)
        self.standard_button_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_8.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_8.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_8.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.standard_button_8.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/dragons_claw.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_8.setIcon(icon32)
        self.standard_button_8.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_8.setObjectName("standard_button_8")
        self.gridLayout.addWidget(self.standard_button_8, 1, 3, 1, 1)
        self.standard_button_34 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_34.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_34.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_34.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_34.setText("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/statikk_shiv.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_34.setIcon(icon33)
        self.standard_button_34.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_34.setObjectName("standard_button_34")
        self.gridLayout.addWidget(self.standard_button_34, 6, 2, 1, 1)
        self.standard_button_30 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_30.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_30.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_30.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_30.setText("")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/shroud_of_stillness.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_30.setIcon(icon34)
        self.standard_button_30.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_30.setObjectName("standard_button_30")
        self.gridLayout.addWidget(self.standard_button_30, 5, 5, 1, 1)
        self.standard_button_33 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_33.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_33.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_33.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_33.setText("")
        icon35 = QtGui.QIcon()
        icon35.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/spear_of_shojin.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_33.setIcon(icon35)
        self.standard_button_33.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_33.setObjectName("standard_button_33")
        self.gridLayout.addWidget(self.standard_button_33, 5, 8, 1, 1)
        self.standard_button_32 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_32.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_32.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_32.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_32.setText("")
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/spatula.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_32.setIcon(icon36)
        self.standard_button_32.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_32.setObjectName("standard_button_32")
        self.gridLayout.addWidget(self.standard_button_32, 5, 7, 1, 1)
        self.standard_button_27 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_27.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_27.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_27.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_27.setText("")
        icon37 = QtGui.QIcon()
        icon37.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/recurve_bow.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_27.setIcon(icon37)
        self.standard_button_27.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_27.setObjectName("standard_button_27")
        self.gridLayout.addWidget(self.standard_button_27, 5, 2, 1, 1)
        self.standard_button_28 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_28.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_28.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_28.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_28.setText("")
        icon38 = QtGui.QIcon()
        icon38.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/redemption.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_28.setIcon(icon38)
        self.standard_button_28.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_28.setObjectName("standard_button_28")
        self.gridLayout.addWidget(self.standard_button_28, 5, 3, 1, 1)
        self.standard_button_36 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_36.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_36.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_36.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_36.setText("")
        icon39 = QtGui.QIcon()
        icon39.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/sunfire_cape.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_36.setIcon(icon39)
        self.standard_button_36.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_36.setObjectName("standard_button_36")
        self.gridLayout.addWidget(self.standard_button_36, 6, 4, 1, 1)
        self.standard_button_38 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_38.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_38.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_38.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_38.setText("")
        icon40 = QtGui.QIcon()
        icon40.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/tear_of_the_goddess.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_38.setIcon(icon40)
        self.standard_button_38.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_38.setObjectName("standard_button_38")
        self.gridLayout.addWidget(self.standard_button_38, 6, 6, 1, 1)
        self.standard_button_39 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_39.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_39.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_39.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_39.setText("")
        icon41 = QtGui.QIcon()
        icon41.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/thieves_gloves.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_39.setIcon(icon41)
        self.standard_button_39.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_39.setObjectName("standard_button_39")
        self.gridLayout.addWidget(self.standard_button_39, 6, 7, 1, 1)
        self.standard_button_40 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_40.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_40.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_40.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_40.setText("")
        icon42 = QtGui.QIcon()
        icon42.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/titans_resolve.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_40.setIcon(icon42)
        self.standard_button_40.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_40.setObjectName("standard_button_40")
        self.gridLayout.addWidget(self.standard_button_40, 6, 8, 1, 1)
        self.standard_button_43 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_43.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_43.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_43.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_43.setText("")
        icon43 = QtGui.QIcon()
        icon43.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/zekes_herald.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_43.setIcon(icon43)
        self.standard_button_43.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_43.setObjectName("standard_button_43")
        self.gridLayout.addWidget(self.standard_button_43, 7, 4, 1, 1)
        self.standard_button_41 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_41.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_41.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_41.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_41.setText("")
        icon44 = QtGui.QIcon()
        icon44.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/warmogs_armor.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_41.setIcon(icon44)
        self.standard_button_41.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_41.setObjectName("standard_button_41")
        self.gridLayout.addWidget(self.standard_button_41, 7, 2, 1, 1)
        self.standard_button_42 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_42.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_42.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_42.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_42.setText("")
        icon45 = QtGui.QIcon()
        icon45.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/protectors_vow.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_42.setIcon(icon45)
        self.standard_button_42.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_42.setObjectName("standard_button_42")
        self.gridLayout.addWidget(self.standard_button_42, 7, 3, 1, 1)
        self.standard_button_44 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.standard_button_44.setMinimumSize(QtCore.QSize(82, 82))
        self.standard_button_44.setMaximumSize(QtCore.QSize(82, 82))
        self.standard_button_44.setStyleSheet("QPushButton {\n"
                                              "background: #195778;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "background: white;\n"
                                              "}")
        self.standard_button_44.setText("")
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/zephyr.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.standard_button_44.setIcon(icon46)
        self.standard_button_44.setIconSize(QtCore.QSize(75, 75))
        self.standard_button_44.setObjectName("standard_button_44")
        self.gridLayout.addWidget(self.standard_button_44, 7, 5, 1, 1)
        self.standard_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.item_tab.addTab(self.standard, "")
        self.Radiant = QtWidgets.QWidget()
        self.Radiant.setObjectName("Radiant")
        self.radiant_scroll_area_ = QtWidgets.QScrollArea(self.Radiant)
        self.radiant_scroll_area_.setGeometry(QtCore.QRect(-1, -1, 700, 360))
        self.radiant_scroll_area_.setMinimumSize(QtCore.QSize(700, 360))
        self.radiant_scroll_area_.setMaximumSize(QtCore.QSize(700, 360))
        self.radiant_scroll_area_.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.radiant_scroll_area_.setWidgetResizable(True)
        self.radiant_scroll_area_.setObjectName("radiant_scroll_area_")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, -5, 681, 540))
        self.scrollAreaWidgetContents_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radiant_button_26 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_26.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_26.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_26.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_26.setText("")
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/shroud_of_stillness_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_26.setIcon(icon47)
        self.radiant_button_26.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_26.setObjectName("radiant_button_26")
        self.gridLayout_3.addWidget(self.radiant_button_26, 3, 7, 1, 1)
        self.radiant_button_27 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_27.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_27.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_27.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_27.setText("")
        icon48 = QtGui.QIcon()
        icon48.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/spear_of_shojin_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_27.setIcon(icon48)
        self.radiant_button_27.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_27.setObjectName("radiant_button_27")
        self.gridLayout_3.addWidget(self.radiant_button_27, 3, 8, 1, 1)
        self.radiant_button_29 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_29.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_29.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_29.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_29.setText("")
        icon49 = QtGui.QIcon()
        icon49.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/guardbreaker_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_29.setIcon(icon49)
        self.radiant_button_29.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_29.setObjectName("radiant_button_29")
        self.gridLayout_3.addWidget(self.radiant_button_29, 4, 2, 1, 1)
        self.radiant_button_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_1.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_1.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_1.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_1.setText("")
        icon50 = QtGui.QIcon()
        icon50.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/archangels_staff_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_1.setIcon(icon50)
        self.radiant_button_1.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_1.setObjectName("radiant_button_1")
        self.gridLayout_3.addWidget(self.radiant_button_1, 0, 2, 1, 1)
        self.radiant_button_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_2.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_2.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_2.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_2.setText("")
        icon51 = QtGui.QIcon()
        icon51.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/bloodthirster_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_2.setIcon(icon51)
        self.radiant_button_2.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_2.setObjectName("radiant_button_2")
        self.gridLayout_3.addWidget(self.radiant_button_2, 0, 3, 1, 1)
        self.radiant_button_28 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_28.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_28.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_28.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_28.setText("")
        icon52 = QtGui.QIcon()
        icon52.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/statikk_shiv_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_28.setIcon(icon52)
        self.radiant_button_28.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_28.setObjectName("radiant_button_28")
        self.gridLayout_3.addWidget(self.radiant_button_28, 3, 9, 1, 1)
        self.radiant_button_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_4.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_4.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_4.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_4.setText("")
        icon53 = QtGui.QIcon()
        icon53.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/bramble_vest_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_4.setIcon(icon53)
        self.radiant_button_4.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_4.setObjectName("radiant_button_4")
        self.gridLayout_3.addWidget(self.radiant_button_4, 0, 6, 1, 1)
        self.radiant_button_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_5.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_5.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_5.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_5.setText("")
        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/chalice_of_power_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_5.setIcon(icon54)
        self.radiant_button_5.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_5.setObjectName("radiant_button_5")
        self.gridLayout_3.addWidget(self.radiant_button_5, 0, 7, 1, 1)
        self.radiant_button_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_3.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_3.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_3.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_3.setText("")
        icon55 = QtGui.QIcon()
        icon55.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/blue_buff_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_3.setIcon(icon55)
        self.radiant_button_3.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_3.setObjectName("radiant_button_3")
        self.gridLayout_3.addWidget(self.radiant_button_3, 0, 4, 1, 1)
        self.radiant_button_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_6.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_6.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_6.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_6.setText("")
        icon56 = QtGui.QIcon()
        icon56.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/death_blade_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_6.setIcon(icon56)
        self.radiant_button_6.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_6.setObjectName("radiant_button_6")
        self.gridLayout_3.addWidget(self.radiant_button_6, 0, 8, 1, 1)
        self.radiant_button_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_7.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_7.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_7.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_7.setText("")
        icon57 = QtGui.QIcon()
        icon57.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/dragons_claw_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_7.setIcon(icon57)
        self.radiant_button_7.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_7.setObjectName("radiant_button_7")
        self.gridLayout_3.addWidget(self.radiant_button_7, 0, 9, 1, 1)
        self.radiant_button_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_8.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_8.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_8.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_8.setText("")
        icon58 = QtGui.QIcon()
        icon58.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/edge_of_night_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_8.setIcon(icon58)
        self.radiant_button_8.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_8.setObjectName("radiant_button_8")
        self.gridLayout_3.addWidget(self.radiant_button_8, 1, 2, 1, 1)
        self.radiant_button_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_9.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_9.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_9.setStyleSheet("QPushButton {\n"
                                            "background: #195778;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background: white;\n"
                                            "}")
        self.radiant_button_9.setText("")
        icon59 = QtGui.QIcon()
        icon59.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/protectors_vow_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_9.setIcon(icon59)
        self.radiant_button_9.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_9.setObjectName("radiant_button_9")
        self.gridLayout_3.addWidget(self.radiant_button_9, 1, 3, 1, 1)
        self.radiant_button_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_10.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_10.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_10.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_10.setText("")
        icon60 = QtGui.QIcon()
        icon60.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/gargoyle_stoneplate_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_10.setIcon(icon60)
        self.radiant_button_10.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_10.setObjectName("radiant_button_10")
        self.gridLayout_3.addWidget(self.radiant_button_10, 1, 4, 1, 1)
        self.radiant_button_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_13.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_13.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_13.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_13.setText("")
        icon61 = QtGui.QIcon()
        icon61.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/hand_of_justice_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_13.setIcon(icon61)
        self.radiant_button_13.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_13.setObjectName("radiant_button_13")
        self.gridLayout_3.addWidget(self.radiant_button_13, 1, 8, 1, 1)
        self.radiant_button_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_11.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_11.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_11.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_11.setText("")
        icon62 = QtGui.QIcon()
        icon62.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/giant_slayer_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_11.setIcon(icon62)
        self.radiant_button_11.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_11.setObjectName("radiant_button_11")
        self.gridLayout_3.addWidget(self.radiant_button_11, 1, 6, 1, 1)
        self.radiant_button_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_12.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_12.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_12.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_12.setText("")
        icon63 = QtGui.QIcon()
        icon63.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/guinsoos_rageblade_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_12.setIcon(icon63)
        self.radiant_button_12.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_12.setObjectName("radiant_button_12")
        self.gridLayout_3.addWidget(self.radiant_button_12, 1, 7, 1, 1)
        self.radiant_button_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_15.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_15.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_15.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_15.setText("")
        icon64 = QtGui.QIcon()
        icon64.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/infinity_edge_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_15.setIcon(icon64)
        self.radiant_button_15.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_15.setObjectName("radiant_button_15")
        self.gridLayout_3.addWidget(self.radiant_button_15, 2, 2, 1, 1)
        self.radiant_button_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_14.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_14.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_14.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_14.setText("")
        icon65 = QtGui.QIcon()
        icon65.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/hextech_gunblade_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_14.setIcon(icon65)
        self.radiant_button_14.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_14.setObjectName("radiant_button_14")
        self.gridLayout_3.addWidget(self.radiant_button_14, 1, 9, 1, 1)
        self.radiant_button_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_17.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_17.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_17.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_17.setText("")
        icon66 = QtGui.QIcon()
        icon66.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/jeweled_gauntlet_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_17.setIcon(icon66)
        self.radiant_button_17.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_17.setObjectName("radiant_button_17")
        self.gridLayout_3.addWidget(self.radiant_button_17, 2, 4, 1, 1)
        self.radiant_button_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_16.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_16.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_16.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_16.setText("")
        icon67 = QtGui.QIcon()
        icon67.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/ionic_spark_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_16.setIcon(icon67)
        self.radiant_button_16.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_16.setObjectName("radiant_button_16")
        self.gridLayout_3.addWidget(self.radiant_button_16, 2, 3, 1, 1)
        self.radiant_button_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_18.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_18.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_18.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_18.setText("")
        icon68 = QtGui.QIcon()
        icon68.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/last_whisper_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_18.setIcon(icon68)
        self.radiant_button_18.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_18.setObjectName("radiant_button_18")
        self.gridLayout_3.addWidget(self.radiant_button_18, 2, 6, 1, 1)
        self.radiant_button_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_20.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_20.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_20.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_20.setText("")
        icon69 = QtGui.QIcon()
        icon69.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/morellonomicon_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_20.setIcon(icon69)
        self.radiant_button_20.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_20.setObjectName("radiant_button_20")
        self.gridLayout_3.addWidget(self.radiant_button_20, 2, 8, 1, 1)
        self.radiant_button_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_19.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_19.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_19.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_19.setText("")
        icon70 = QtGui.QIcon()
        icon70.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/locket_of_the_iron_solari_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_19.setIcon(icon70)
        self.radiant_button_19.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_19.setObjectName("radiant_button_19")
        self.gridLayout_3.addWidget(self.radiant_button_19, 2, 7, 1, 1)
        self.radiant_button_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_21.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_21.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_21.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_21.setText("")
        icon71 = QtGui.QIcon()
        icon71.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/quicksilver_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_21.setIcon(icon71)
        self.radiant_button_21.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_21.setObjectName("radiant_button_21")
        self.gridLayout_3.addWidget(self.radiant_button_21, 2, 9, 1, 1)
        self.radiant_button_22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_22.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_22.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_22.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_22.setText("")
        icon72 = QtGui.QIcon()
        icon72.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/rabadons_deathcap_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_22.setIcon(icon72)
        self.radiant_button_22.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_22.setObjectName("radiant_button_22")
        self.gridLayout_3.addWidget(self.radiant_button_22, 3, 2, 1, 1)
        self.radiant_button_23 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_23.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_23.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_23.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_23.setText("")
        icon73 = QtGui.QIcon()
        icon73.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/rapid_fire_cannon_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_23.setIcon(icon73)
        self.radiant_button_23.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_23.setObjectName("radiant_button_23")
        self.gridLayout_3.addWidget(self.radiant_button_23, 3, 3, 1, 1)
        self.radiant_button_25 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_25.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_25.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_25.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_25.setText("")
        icon74 = QtGui.QIcon()
        icon74.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/runaans_hurricane_radiant.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_25.setIcon(icon74)
        self.radiant_button_25.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_25.setObjectName("radiant_button_25")
        self.gridLayout_3.addWidget(self.radiant_button_25, 3, 6, 1, 1)
        self.radiant_button_24 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_24.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_24.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_24.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_24.setText("")
        icon75 = QtGui.QIcon()
        icon75.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/redemption_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_24.setIcon(icon75)
        self.radiant_button_24.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_24.setObjectName("radiant_button_24")
        self.gridLayout_3.addWidget(self.radiant_button_24, 3, 4, 1, 1)
        self.radiant_button_31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_31.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_31.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_31.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_31.setText("")
        icon76 = QtGui.QIcon()
        icon76.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/thieves_gloves_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_31.setIcon(icon76)
        self.radiant_button_31.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_31.setObjectName("radiant_button_31")
        self.gridLayout_3.addWidget(self.radiant_button_31, 4, 4, 1, 1)
        self.radiant_button_30 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_30.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_30.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_30.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_30.setText("")
        icon77 = QtGui.QIcon()
        icon77.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/sunfire_cape_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_30.setIcon(icon77)
        self.radiant_button_30.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_30.setObjectName("radiant_button_30")
        self.gridLayout_3.addWidget(self.radiant_button_30, 4, 3, 1, 1)
        self.radiant_button_32 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_32.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_32.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_32.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_32.setText("")
        icon78 = QtGui.QIcon()
        icon78.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/titans_resolve_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_32.setIcon(icon78)
        self.radiant_button_32.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_32.setObjectName("radiant_button_32")
        self.gridLayout_3.addWidget(self.radiant_button_32, 4, 6, 1, 1)
        self.radiant_button_33 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_33.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_33.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_33.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_33.setText("")
        icon79 = QtGui.QIcon()
        icon79.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/warmogs_armor_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_33.setIcon(icon79)
        self.radiant_button_33.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_33.setObjectName("radiant_button_33")
        self.gridLayout_3.addWidget(self.radiant_button_33, 4, 7, 1, 1)
        self.radiant_button_35 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_35.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_35.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_35.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_35.setText("")
        icon80 = QtGui.QIcon()
        icon80.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/zephyr_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_35.setIcon(icon80)
        self.radiant_button_35.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_35.setObjectName("radiant_button_35")
        self.gridLayout_3.addWidget(self.radiant_button_35, 4, 9, 1, 1)
        self.radiant_button_34 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_34.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_34.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_34.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_34.setText("")
        icon81 = QtGui.QIcon()
        icon81.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/zekes_herald_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_34.setIcon(icon81)
        self.radiant_button_34.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_34.setObjectName("radiant_button_34")
        self.gridLayout_3.addWidget(self.radiant_button_34, 4, 8, 1, 1)
        self.radiant_button_36 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.radiant_button_36.setMinimumSize(QtCore.QSize(82, 82))
        self.radiant_button_36.setMaximumSize(QtCore.QSize(82, 82))
        self.radiant_button_36.setStyleSheet("QPushButton {\n"
                                             "background: #195778;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background: white;\n"
                                             "}")
        self.radiant_button_36.setText("")
        icon82 = QtGui.QIcon()
        icon82.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/zzrot_portal_radiant.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiant_button_36.setIcon(icon82)
        self.radiant_button_36.setIconSize(QtCore.QSize(75, 75))
        self.radiant_button_36.setObjectName("radiant_button_36")
        self.gridLayout_3.addWidget(self.radiant_button_36, 5, 2, 1, 1)
        self.radiant_scroll_area_.setWidget(self.scrollAreaWidgetContents_3)
        self.item_tab.addTab(self.Radiant, "")
        self.trait = QtWidgets.QWidget()
        self.trait.setObjectName("trait")
        self.trait_scroll_area = QtWidgets.QScrollArea(self.trait)
        self.trait_scroll_area.setGeometry(QtCore.QRect(-1, -1, 700, 360))
        self.trait_scroll_area.setMinimumSize(QtCore.QSize(700, 360))
        self.trait_scroll_area.setMaximumSize(QtCore.QSize(700, 360))
        self.trait_scroll_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.trait_scroll_area.setWidgetResizable(True)
        self.trait_scroll_area.setObjectName("trait_scroll_area")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 698, 358))
        self.scrollAreaWidgetContents_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.trait_button_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_17.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_17.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_17.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_17.setText("")
        icon83 = QtGui.QIcon()
        icon83.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/juggernaut.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_17.setIcon(icon83)
        self.trait_button_17.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_17.setObjectName("trait_button_17")
        self.gridLayout_4.addWidget(self.trait_button_17, 2, 4, 1, 1)
        self.trait_button_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_2.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_2.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_2.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_2.setText("")
        icon84 = QtGui.QIcon()
        icon84.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/bruiser.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_2.setIcon(icon84)
        self.trait_button_2.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_2.setObjectName("trait_button_2")
        self.gridLayout_4.addWidget(self.trait_button_2, 0, 3, 1, 1)
        self.trait_button_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_1.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_1.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_1.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_1.setText("")
        icon85 = QtGui.QIcon()
        icon85.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/bastion.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_1.setIcon(icon85)
        self.trait_button_1.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_1.setObjectName("trait_button_1")
        self.gridLayout_4.addWidget(self.trait_button_1, 0, 2, 1, 1)
        self.trait_button_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_10.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_10.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_10.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_10.setText("")
        icon86 = QtGui.QIcon()
        icon86.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/strategist.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_10.setIcon(icon86)
        self.trait_button_10.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_10.setObjectName("trait_button_10")
        self.gridLayout_4.addWidget(self.trait_button_10, 1, 4, 1, 1)
        self.trait_button_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_6.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_6.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_6.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_6.setText("")
        icon87 = QtGui.QIcon()
        icon87.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/piltover.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_6.setIcon(icon87)
        self.trait_button_6.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_6.setObjectName("trait_button_6")
        self.gridLayout_4.addWidget(self.trait_button_6, 0, 7, 1, 1)
        self.trait_button_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_3.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_3.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_3.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_3.setText("")
        icon88 = QtGui.QIcon()
        icon88.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/deadeye.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_3.setIcon(icon88)
        self.trait_button_3.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_3.setObjectName("trait_button_3")
        self.gridLayout_4.addWidget(self.trait_button_3, 0, 4, 1, 1)
        self.trait_button_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_14.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_14.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_14.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_14.setText("")
        icon89 = QtGui.QIcon()
        icon89.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/challenger.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_14.setIcon(icon89)
        self.trait_button_14.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_14.setObjectName("trait_button_14")
        self.gridLayout_4.addWidget(self.trait_button_14, 1, 8, 1, 1)
        self.trait_button_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_15.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_15.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_15.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_15.setText("")
        icon90 = QtGui.QIcon()
        icon90.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/demacia.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_15.setIcon(icon90)
        self.trait_button_15.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_15.setObjectName("trait_button_15")
        self.gridLayout_4.addWidget(self.trait_button_15, 2, 2, 1, 1)
        self.trait_button_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_8.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_8.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_8.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_8.setText("")
        icon91 = QtGui.QIcon()
        icon91.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/rogue.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_8.setIcon(icon91)
        self.trait_button_8.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_8.setObjectName("trait_button_8")
        self.gridLayout_4.addWidget(self.trait_button_8, 1, 2, 1, 1)
        self.trait_button_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_4.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_4.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_4.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_4.setText("")
        icon92 = QtGui.QIcon()
        icon92.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/freljord.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_4.setIcon(icon92)
        self.trait_button_4.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_4.setObjectName("trait_button_4")
        self.gridLayout_4.addWidget(self.trait_button_4, 0, 5, 1, 1)
        self.trait_button_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_9.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_9.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_9.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_9.setText("")
        icon93 = QtGui.QIcon()
        icon93.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/shadowisles.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_9.setIcon(icon93)
        self.trait_button_9.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_9.setObjectName("trait_button_9")
        self.gridLayout_4.addWidget(self.trait_button_9, 1, 3, 1, 1)
        self.trait_button_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_5.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_5.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_5.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_5.setText("")
        icon94 = QtGui.QIcon()
        icon94.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/gunner.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_5.setIcon(icon94)
        self.trait_button_5.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_5.setObjectName("trait_button_5")
        self.gridLayout_4.addWidget(self.trait_button_5, 0, 6, 1, 1)
        self.trait_button_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_7.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_7.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_7.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.trait_button_7.setText("")
        icon95 = QtGui.QIcon()
        icon95.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/invoker.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_7.setIcon(icon95)
        self.trait_button_7.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_7.setObjectName("trait_button_7")
        self.gridLayout_4.addWidget(self.trait_button_7, 0, 8, 1, 1)
        self.trait_button_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_18.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_18.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_18.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_18.setText("")
        icon96 = QtGui.QIcon()
        icon96.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/noxus.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_18.setIcon(icon96)
        self.trait_button_18.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_18.setObjectName("trait_button_18")
        self.gridLayout_4.addWidget(self.trait_button_18, 2, 5, 1, 1)
        self.trait_button_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_11.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_11.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_11.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_11.setText("")
        icon97 = QtGui.QIcon()
        icon97.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/targon.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_11.setIcon(icon97)
        self.trait_button_11.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_11.setObjectName("trait_button_11")
        self.gridLayout_4.addWidget(self.trait_button_11, 1, 5, 1, 1)
        self.trait_button_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_16.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_16.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_16.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_16.setText("")
        icon98 = QtGui.QIcon()
        icon98.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/ionia.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_16.setIcon(icon98)
        self.trait_button_16.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_16.setObjectName("trait_button_16")
        self.gridLayout_4.addWidget(self.trait_button_16, 2, 3, 1, 1)
        self.trait_button_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_12.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_12.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_12.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_12.setText("")
        icon99 = QtGui.QIcon()
        icon99.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/void.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_12.setIcon(icon99)
        self.trait_button_12.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_12.setObjectName("trait_button_12")
        self.gridLayout_4.addWidget(self.trait_button_12, 1, 6, 1, 1)
        self.trait_button_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_20.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_20.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_20.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_20.setText("")
        icon100 = QtGui.QIcon()
        icon100.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/slayer.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_20.setIcon(icon100)
        self.trait_button_20.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_20.setObjectName("trait_button_20")
        self.gridLayout_4.addWidget(self.trait_button_20, 2, 7, 1, 1)
        self.trait_button_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_19.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_19.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_19.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_19.setText("")
        icon101 = QtGui.QIcon()
        icon101.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/shurima.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_19.setIcon(icon101)
        self.trait_button_19.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_19.setObjectName("trait_button_19")
        self.gridLayout_4.addWidget(self.trait_button_19, 2, 6, 1, 1)
        self.trait_button_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_21.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_21.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_21.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_21.setText("")
        icon102 = QtGui.QIcon()
        icon102.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/sorcerer.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_21.setIcon(icon102)
        self.trait_button_21.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_21.setObjectName("trait_button_21")
        self.gridLayout_4.addWidget(self.trait_button_21, 2, 8, 1, 1)
        self.trait_button_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.trait_button_13.setMinimumSize(QtCore.QSize(82, 82))
        self.trait_button_13.setMaximumSize(QtCore.QSize(82, 82))
        self.trait_button_13.setStyleSheet("QPushButton {\n"
                                           "background: #195778;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: white;\n"
                                           "}")
        self.trait_button_13.setText("")
        icon103 = QtGui.QIcon()
        icon103.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/zaun.tft_set9.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trait_button_13.setIcon(icon103)
        self.trait_button_13.setIconSize(QtCore.QSize(75, 75))
        self.trait_button_13.setObjectName("trait_button_13")
        self.gridLayout_4.addWidget(self.trait_button_13, 1, 7, 1, 1)
        self.trait_scroll_area.setWidget(self.scrollAreaWidgetContents_4)
        self.item_tab.addTab(self.trait, "")
        self.Ornn = QtWidgets.QWidget()
        self.Ornn.setObjectName("Ornn")
        self.gadget_scroll_area_3 = QtWidgets.QScrollArea(self.Ornn)
        self.gadget_scroll_area_3.setGeometry(QtCore.QRect(-1, -1, 700, 360))
        self.gadget_scroll_area_3.setMinimumSize(QtCore.QSize(700, 360))
        self.gadget_scroll_area_3.setMaximumSize(QtCore.QSize(700, 360))
        self.gadget_scroll_area_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.gadget_scroll_area_3.setWidgetResizable(True)
        self.gadget_scroll_area_3.setObjectName("gadget_scroll_area_3")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 698, 358))
        self.scrollAreaWidgetContents_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ornn_button_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_1.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_1.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_1.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_1.setText("")
        icon104 = QtGui.QIcon()
        icon104.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/obsidian_cleaver.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_1.setIcon(icon104)
        self.ornn_button_1.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_1.setObjectName("ornn_button_1")
        self.gridLayout_9.addWidget(self.ornn_button_1, 0, 2, 1, 1)
        self.ornn_button_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_2.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_2.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_2.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_2.setText("")
        icon105 = QtGui.QIcon()
        icon105.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/gold_collector.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_2.setIcon(icon105)
        self.ornn_button_2.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_2.setObjectName("ornn_button_2")
        self.gridLayout_9.addWidget(self.ornn_button_2, 0, 3, 1, 1)
        self.ornn_button_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_4.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_4.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_4.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_4.setText("")
        icon106 = QtGui.QIcon()
        icon106.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/eternal_winter.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_4.setIcon(icon106)
        self.ornn_button_4.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_4.setObjectName("ornn_button_4")
        self.gridLayout_9.addWidget(self.ornn_button_4, 0, 5, 1, 1)
        self.ornn_button_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_6.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_6.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_6.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_6.setText("")
        icon107 = QtGui.QIcon()
        icon107.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/randuins_sanctum.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_6.setIcon(icon107)
        self.ornn_button_6.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_6.setObjectName("ornn_button_6")
        self.gridLayout_9.addWidget(self.ornn_button_6, 0, 7, 1, 1)
        self.ornn_button_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_5.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_5.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_5.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_5.setText("")
        icon108 = QtGui.QIcon()
        icon108.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/manazane.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_5.setIcon(icon108)
        self.ornn_button_5.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_5.setObjectName("ornn_button_5")
        self.gridLayout_9.addWidget(self.ornn_button_5, 0, 6, 1, 1)
        self.ornn_button_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_3.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_3.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_3.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_3.setText("")
        icon109 = QtGui.QIcon()
        icon109.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/deaths_defiance.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_3.setIcon(icon109)
        self.ornn_button_3.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_3.setObjectName("ornn_button_3")
        self.gridLayout_9.addWidget(self.ornn_button_3, 0, 4, 1, 1)
        self.ornn_button_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_7.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_7.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_7.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_7.setText("")
        icon110 = QtGui.QIcon()
        icon110.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/hullcrusher.png"),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_7.setIcon(icon110)
        self.ornn_button_7.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_7.setObjectName("ornn_button_7")
        self.gridLayout_9.addWidget(self.ornn_button_7, 0, 8, 1, 1)
        self.ornn_button_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_8.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_8.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_8.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_8.setText("")
        icon111 = QtGui.QIcon()
        icon111.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/anima_visage.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_8.setIcon(icon111)
        self.ornn_button_8.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_8.setObjectName("ornn_button_8")
        self.gridLayout_9.addWidget(self.ornn_button_8, 1, 2, 1, 1)
        self.ornn_button_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_9.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_9.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_9.setStyleSheet("QPushButton {\n"
                                         "background: #195778;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "background: white;\n"
                                         "}")
        self.ornn_button_9.setText("")
        icon112 = QtGui.QIcon()
        icon112.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/infinity_force.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_9.setIcon(icon112)
        self.ornn_button_9.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_9.setObjectName("ornn_button_9")
        self.gridLayout_9.addWidget(self.ornn_button_9, 1, 3, 1, 1)
        self.ornn_button_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_10.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_10.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_10.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.ornn_button_10.setText("")
        icon113 = QtGui.QIcon()
        icon113.addPixmap(
            QtGui.QPixmap("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/zhonyas_paradox.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_10.setIcon(icon113)
        self.ornn_button_10.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_10.setObjectName("ornn_button_10")
        self.gridLayout_9.addWidget(self.ornn_button_10, 1, 4, 1, 1)
        self.ornn_button_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_14.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_14.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_14.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.ornn_button_14.setText("")
        icon114 = QtGui.QIcon()
        icon114.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/tricksters_glass.png"),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_14.setIcon(icon114)
        self.ornn_button_14.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_14.setObjectName("ornn_button_14")
        self.gridLayout_9.addWidget(self.ornn_button_14, 1, 8, 1, 1)
        self.ornn_button_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_13.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_13.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_13.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.ornn_button_13.setText("")
        icon115 = QtGui.QIcon()
        icon115.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/snipers_focus.png"),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_13.setIcon(icon115)
        self.ornn_button_13.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_13.setObjectName("ornn_button_13")
        self.gridLayout_9.addWidget(self.ornn_button_13, 1, 7, 1, 1)
        self.ornn_button_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_12.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_12.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_12.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.ornn_button_12.setText("")
        icon116 = QtGui.QIcon()
        icon116.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/deathfire_grasp.png"),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_12.setIcon(icon116)
        self.ornn_button_12.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_12.setObjectName("ornn_button_12")
        self.gridLayout_9.addWidget(self.ornn_button_12, 1, 6, 1, 1)
        self.ornn_button_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.ornn_button_11.setMinimumSize(QtCore.QSize(82, 82))
        self.ornn_button_11.setMaximumSize(QtCore.QSize(82, 82))
        self.ornn_button_11.setStyleSheet("QPushButton {\n"
                                          "background: #195778;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: white;\n"
                                          "}")
        self.ornn_button_11.setText("")
        icon117 = QtGui.QIcon()
        icon117.addPixmap(QtGui.QPixmap(
            "C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/blacksmiths_gloves.png"),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ornn_button_11.setIcon(icon117)
        self.ornn_button_11.setIconSize(QtCore.QSize(75, 75))
        self.ornn_button_11.setObjectName("ornn_button_11")
        self.gridLayout_9.addWidget(self.ornn_button_11, 1, 5, 1, 1)
        self.gadget_scroll_area_3.setWidget(self.scrollAreaWidgetContents_9)
        self.item_tab.addTab(self.Ornn, "")
        self.selected_item_2 = QtWidgets.QLabel(item_selector)
        self.selected_item_2.setGeometry(QtCore.QRect(870, 160, 82, 82))
        self.selected_item_2.setAutoFillBackground(False)
        self.selected_item_2.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid #195778;\n"
                                               "}\n"
                                               "")
        self.selected_item_2.setText("")
        self.selected_item_2.setScaledContents(True)
        self.selected_item_2.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_item_2.setObjectName("selected_item_2")
        self.selected_item_3 = QtWidgets.QLabel(item_selector)
        self.selected_item_3.setGeometry(QtCore.QRect(980, 160, 82, 82))
        self.selected_item_3.setAutoFillBackground(False)
        self.selected_item_3.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid #195778;\n"
                                               "}\n"
                                               "")
        self.selected_item_3.setText("")
        self.selected_item_3.setScaledContents(True)
        self.selected_item_3.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_item_3.setObjectName("selected_item_3")
        self.change_button = QtWidgets.QPushButton(item_selector)
        self.change_button.setGeometry(QtCore.QRect(860, 300, 100, 40))
        self.change_button.setStyleSheet("QPushButton {\n"
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
        self.change_button.setObjectName("change_button")
        self.current_select_label = QtWidgets.QLabel(item_selector)
        self.current_select_label.setGeometry(QtCore.QRect(766, 100, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.current_select_label.setFont(font)
        self.current_select_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_select_label.setObjectName("current_select_label")
        self.item_name_label_1 = QtWidgets.QLabel(item_selector)
        self.item_name_label_1.setGeometry(QtCore.QRect(751, 250, 101, 31))
        self.item_name_label_1.setText("")
        self.item_name_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.item_name_label_1.setObjectName("item_name_label_1")
        self.item_name_label_1.setWordWrap(True)
        self.item_name_label_2 = QtWidgets.QLabel(item_selector)
        self.item_name_label_2.setGeometry(QtCore.QRect(861, 250, 101, 31))
        self.item_name_label_2.setText("")
        self.item_name_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.item_name_label_2.setObjectName("item_name_label_2")
        self.item_name_label_2.setWordWrap(True)
        self.item_name_label_3 = QtWidgets.QLabel(item_selector)
        self.item_name_label_3.setGeometry(QtCore.QRect(971, 250, 101, 31))
        self.item_name_label_3.setText("")
        self.item_name_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.item_name_label_3.setObjectName("item_name_label_3")
        self.item_name_label_3.setWordWrap(True)
        self.selected_item_1.raise_()
        self.next_button.raise_()
        self.predict_button.raise_()
        self.item_tab.raise_()
        self.selected_item_2.raise_()
        self.selected_item_3.raise_()
        self.change_button.raise_()
        self.current_select_label.raise_()
        self.item_name_label_1.raise_()
        self.item_name_label_2.raise_()
        self.item_name_label_3.raise_()

        self.retranslateUi(item_selector)
        self.item_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(item_selector)

        self.standard_button_1.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/archangels_staff.png", "Archangel's staff"))
        self.standard_button_2.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/Bf_sword.png", "BF Sword"))
        self.standard_button_3.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/bloodthirster.png", "Bloodthirster"))
        self.standard_button_4.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/blue_buff.png", "Blue buff"))
        self.standard_button_5.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/bramble_vest.png", "Bramble Vest"))
        self.standard_button_45.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/chain_vest.png", "Chain Vest"))
        self.standard_button_6.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/chalice_of_power.png", "Chalice of Power"))
        self.standard_button_7.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/death_blade.png", "Death Blade"))
        self.standard_button_8.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/dragons_claw.png", "Dragon's Claw"))
        self.standard_button_9.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/edge_of_night.png", "Edge of Night"))
        self.standard_button_10.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/giants_belt.png", "Giant's Belt"))
        self.standard_button_11.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/gargoyle_stoneplate.png", "Gargoyle Stoneplate"))
        self.standard_button_12.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/giant_slayer.png", "Giant Slayer"))
        self.standard_button_13.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/guardian_angel.png", "Guardian Angel"))
        self.standard_button_14.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/guinsoos_rageblade.png", "Guinsoo's Rageblade"))
        self.standard_button_46.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/hand_of_justice.png", "Hand of Justice"))
        self.standard_button_15.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/hextech_gunblade.png", "Hextech Gunblade"))
        self.standard_button_16.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/infinity_edge.png", "Infinity Edge"))
        self.standard_button_17.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/ionic_spark.png", "Ionic Spark"))
        self.standard_button_18.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/jeweled_gauntlet.png", "Jeweled Gauntlet"))
        self.standard_button_19.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/last_whisper.png", "Last Whisper"))
        self.standard_button_20.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/locket_of_the_iron_solari.png", "Locket of the Iron Solari"))
        self.standard_button_21.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/morellonomicon.png", "Morellonomicon"))
        self.standard_button_22.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/needlessly_large_rod.png", "Needlessly Large Rod"))
        self.standard_button_23.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/negatron_cloak.png", "Negatron Cloak"))
        self.standard_button_24.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/quicksilver.png", "Quicksilver"))
        self.standard_button_25.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/rabadons_deathcap.png", "Rabadon's Deathcap"))
        self.standard_button_26.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/rapid_fire_cannon.png", "Rapid Fire Cannon"))
        self.standard_button_27.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/recurve_bow.png", "Recurve Bow"))
        self.standard_button_28.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/redemption.png", "Redemption"))
        self.standard_button_29.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/runaans_hurricane.png", "Runaan's Hurricane"))
        self.standard_button_30.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/shroud_of_stillness.png", "Shroud of Stillness"))
        self.standard_button_31.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/sparring_gloves.png", "Sparring Gloves"))
        self.standard_button_32.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/spatula.png", "Spatula"))
        self.standard_button_33.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/spear_of_shojin.png", "Spear of Shojin"))
        self.standard_button_34.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/statikk_shiv.png", "Statikk Shiv"))
        self.standard_button_35.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/guardbreaker.png", "Guardbreaker"))
        self.standard_button_36.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/sunfire_cape.png", "Sunfire Cape"))
        self.standard_button_37.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/tacticians_crown.png", "Tactician's Crown"))
        self.standard_button_38.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/tear_of_the_goddess.png", "Tear of the Goddess"))
        self.standard_button_39.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/thieves_gloves.png", "Thief's Gloves"))
        self.standard_button_40.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/titans_resolve.png", "Titan's Resolve"))
        self.standard_button_41.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/warmogs_armor.png", "Warmog's Armor"))
        self.standard_button_42.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/protectors_vow.png", "Protector's Vow"))
        self.standard_button_43.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/zekes_herald.png", "Zeke's Herald"))
        self.standard_button_44.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/zephyr.png", "Zephyr"))
        self.standard_button_47.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/standard/zzrot_portal.png", "Zz'Rot Portal"))

        self.radiant_button_1.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/archangels_staff_radiant.png", "Archangel's Staff Radiant"))
        self.radiant_button_2.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/bloodthirster_radiant.png", "Bloodthirster Radiant"))
        self.radiant_button_3.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/blue_buff_radiant.png", "Blue buff Radiant"))
        self.radiant_button_4.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/bramble_vest_radiant.png", "Bramble Vest Radiant"))
        self.radiant_button_5.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/chalice_of_power_radiant.png", "Chalice of Power Radiant"))
        self.radiant_button_6.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/death_blade_radiant.png", "Deathblade Radiant"))
        self.radiant_button_7.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/dragons_claw_radiant.png", "Dragon's Claw Radiant"))
        self.radiant_button_8.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/edge_of_night_radiant.png", "Edge of Night Radiant"))
        self.radiant_button_9.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/protectors_vow_radiant.png", "Protector's Vow Radiant"))
        self.radiant_button_10.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/gargoyle_stoneplate_radiant.png", "Gargoyle Stoneplate Radiant"))
        self.radiant_button_11.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/giant_slayer_radiant.png", "Giant Slayer Radiant"))
        self.radiant_button_12.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/guinsoos_rageblade_radiant.png", "Guinsoo's Rageblade Radiant"))
        self.radiant_button_13.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/hand_of_justice_radiant.png", "Hand of Justice Radiant"))
        self.radiant_button_14.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/hextech_gunblade_radiant.png", "Hextech Gunblade Radiant"))
        self.radiant_button_15.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/infinity_edge_radiant.png", "Infinity Edge Radiant"))
        self.radiant_button_16.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/ionic_spark_radiant.png", "Ionic Spark Radiant"))
        self.radiant_button_17.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/jeweled_gauntlet_radiant.png", "Jeweled Gauntlet Radiant"))
        self.radiant_button_18.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/last_whisper_radiant.png", "Last Whisper Radiant"))
        self.radiant_button_19.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/locket_of_the_iron_solari_radiant.png", "Locket of the Iron Solari Radiant"))
        self.radiant_button_20.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/morellonomicon_radiant.png", "Morellonomicon Radiant"))
        self.radiant_button_21.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/quicksilver_radiant.png", "Quicksilver Radiant"))
        self.radiant_button_22.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/rabadons_deathcap_radiant.png", "Rabadon's Deathcap Radiant"))
        self.radiant_button_23.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/rapid_fire_cannon_radiant.png", "Rapid Fire Cannon Radiant"))
        self.radiant_button_24.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/redemption_radiant.png", "Redemption Radiant"))
        self.radiant_button_25.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/runaans_hurricane_radiant.png", "Runaan's Hurricane Radiant"))
        self.radiant_button_26.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/shroud_of_stillness_radiant.png", "Shroud of Stillness Radiant"))
        self.radiant_button_27.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/spear_of_shojin_radiant.png", "Spear of Shojin Radiant"))
        self.radiant_button_28.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/statikk_shiv_radiant.png", "Statikk Shiv Radiant"))
        self.radiant_button_29.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/guardbreaker_radiant.png", "Guardbreaker Radiant"))
        self.radiant_button_30.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/sunfire_cape_radiant.png", "Sunfire Cape Radiant"))
        self.radiant_button_31.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/thieves_gloves_radiant.png", "Thief's Gloves Radiant"))
        self.radiant_button_32.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/titans_resolve_radiant.png", "Titan's Resolve Radiant"))
        self.radiant_button_33.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/warmogs_armor_radiant.png", "Warmog's Armor Radiant"))
        self.radiant_button_34.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/zekes_herald_radiant.png", "Zeke's Herald Radiant"))
        self.radiant_button_35.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/zephyr_radiant.png", "Zephyr Radiant"))
        self.radiant_button_36.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/radiant/zzrot_portal_radiant.png", "Zz'Rot Portal Radiant"))

        self.trait_button_1.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/bastion.tft_set9.png", "Bastion Emblem"))
        self.trait_button_2.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/bruiser.tft_set9.png", "Bruiser Emblem"))
        self.trait_button_3.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/deadeye.tft_set9.png", "Deadeye Emblem"))
        self.trait_button_4.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/freljord.tft_set9.png", "Freljord Emblem"))
        self.trait_button_5.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/gunner.tft_set9.png", "Gunner Emblem"))
        self.trait_button_6.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/piltover.tft_set9.png", "Piltover Emblem"))
        self.trait_button_7.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/invoker.tft_set9.png", "Invoker Emblem"))
        self.trait_button_8.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/rogue.tft_set9.png", "Rogue Emblem"))
        self.trait_button_9.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/shadowisles.tft_set9.png", "Shadow Isles Emblem"))
        self.trait_button_10.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/strategist.tft_set9.png", "Strategist Emblem"))
        self.trait_button_11.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/targon.tft_set9.png", "Targon Emblem"))
        self.trait_button_12.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/void.tft_set9.png", "Void Emblem"))
        self.trait_button_13.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/zaun.tft_set9.png", "Zaun Emblem"))
        self.trait_button_14.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/challenger.tft_set9.png", "Challenger Emblem"))
        self.trait_button_15.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/demacia.tft_set9.png", "Demancia Emblem"))
        self.trait_button_16.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/ionia.tft_set9.png", "Ionia Emblem"))
        self.trait_button_17.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/juggernaut.tft_set9.png", "Juggernaut Emblem"))
        self.trait_button_18.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/noxus.tft_set9.png", "Noxus Emblem"))
        self.trait_button_19.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/shurima.tft_set9.png", "Shurima Emblem"))
        self.trait_button_20.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/slayer.tft_set9.png", "Slayer Emblem"))
        self.trait_button_21.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/trait/sorcerer.tft_set9.png", "Sorcerer Emblem"))

        self.ornn_button_1.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/obsidian_cleaver.png", "Obsidian Cleaver"))
        self.ornn_button_2.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/gold_collector.png", "Gold Collector"))
        self.ornn_button_3.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/deaths_defiance.png", "Death's Defiance"))
        self.ornn_button_4.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/eternal_winter.png", "Eternal Winter"))
        self.ornn_button_5.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/manazane.png", "Manazane"))
        self.ornn_button_6.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/randuins_sanctum.png", "Randuin's Sanctum"))
        self.ornn_button_7.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/hullcrusher.png", "Hullcrusher"))
        self.ornn_button_8.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/anima_visage.png", "Anima Visage"))
        self.ornn_button_9.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/infinity_force.png", "Infinity Force"))
        self.ornn_button_10.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/zhonyas_paradox.png", "Zhonya's Paradox"))
        self.ornn_button_11.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/blacksmiths_gloves.png", "Blacksmith's Gloves"))
        self.ornn_button_12.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/deathfire_grasp.png", "Deathfire Grasp"))
        self.ornn_button_13.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/snipers_focus.png", "Sniper's Focus"))
        self.ornn_button_14.clicked.connect(lambda: self.item_clicked("C:/Uni/Year 4/Semester 1/Honour\'s Project/image/Items/ornn/tricksters_glass.png", "Trickster's Glass"))

        self.change_button.clicked.connect(lambda: self.change_clicked())

        self.next_button.clicked.connect(lambda: self.next_clicked(item_selector_ref, main_window_ref,board_window_ref, champion_window_ref, selected_champion, selected_level, position, state, "update"))
        self.predict_button.clicked.connect(lambda: self.next_clicked(item_selector_ref, main_window_ref, board_window_ref, champion_window_ref, selected_champion, selected_level, position, state, "predict"))

    def retranslateUi(self, item_selector):
        _translate = QtCore.QCoreApplication.translate
        item_selector.setWindowTitle(_translate("item_selector", "Item Selection"))
        self.next_button.setText(_translate("item_selector", "Only Update Board"))
        self.predict_button.setText(_translate("item_selector", "Update and Predict"))
        self.item_tab.setTabText(self.item_tab.indexOf(self.standard), _translate("item_selector", "Standard"))
        self.item_tab.setTabText(self.item_tab.indexOf(self.Radiant), _translate("item_selector", "Radiant"))
        self.item_tab.setTabText(self.item_tab.indexOf(self.trait), _translate("item_selector", "Trait"))
        self.item_tab.setTabText(self.item_tab.indexOf(self.Ornn), _translate("item_selector", "Ornn"))
        self.change_button.setText(_translate("item_selector", "Change Select"))
        self.current_select_label.setText(_translate("item_selector", "Currently selecting item slot 1"))

    def next_clicked(self, item_selector, main_window, board_window, champion_window, selected_champion, selected_level, position, state, option):

        if self.item_name_label_1.text() == "":
            item_one = "null"
        else:
            item_one = self.item_name_label_1.text()

        if self.item_name_label_2.text() == "":
            item_two = "null"
        else:
            item_two = self.item_name_label_2.text()

        if self.item_name_label_3.text() == "":
            item_three = "null"
        else:
            item_three = self.item_name_label_3.text()

        new_state = position + "|" + selected_champion.lower() + "|" + str(selected_level) + "|" + item_one + "|" + item_two + "|" + item_three

        if state == "new":
            board_window.close()
            champion_window.close()

            from board import UI_Board_Widget

            self.window = UI_Board_Widget()
            self.ui = UI_Board_Widget()
            self.ui.setup_ui_board_widget(self.window, main_window, new_state, option)
            self.window.show()

        else:
            current_state = state.split(",")
            modified_state = None
            for unit_informaiton in current_state:
                taken_position = unit_informaiton.split("|")
                if taken_position[0] == position:
                    pass
                else:
                    if modified_state is None:
                        modified_state = unit_informaiton
                    else:
                        modified_state = modified_state + "," + unit_informaiton

            modified_state = modified_state + "," + new_state
            board_window.close()
            champion_window.close()

            from board import UI_Board_Widget
            self.window = UI_Board_Widget()
            self.ui = UI_Board_Widget()
            self.ui.setup_ui_board_widget(self.window, main_window, modified_state, option)
            self.window.show()

        item_selector.close()

    def item_clicked(self, image_path, item_name):
        if self.current_select_label.text() == "Currently selecting item slot 1":
            self.selected_item_1.setPixmap(QtGui.QPixmap(image_path))
            self.item_name_label_1.setText(item_name)
        elif self.current_select_label.text() == "Currently selecting item slot 2":
            self.selected_item_2.setPixmap(QtGui.QPixmap(image_path))
            self.item_name_label_2.setText(item_name)
        elif self.current_select_label.text() == "Currently selecting item slot 3":
            self.selected_item_3.setPixmap(QtGui.QPixmap(image_path))
            self.item_name_label_3.setText(item_name)

    def change_clicked(self):
        if self.current_select_label.text() == "Currently selecting item slot 1":
            self.current_select_label.setText("Currently selecting item slot 2")
            self.selected_item_1.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid #195778;\n"
                                               "}\n"
                                               "")
            self.selected_item_2.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid white;\n"
                                               "}\n"
                                               "")
        elif self.current_select_label.text() == "Currently selecting item slot 2":
            self.current_select_label.setText("Currently selecting item slot 3")
            self.selected_item_2.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid #195778;\n"
                                               "}\n"
                                               "")
            self.selected_item_3.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid white;\n"
                                               "}\n"
                                               "")
        elif self.current_select_label.text() == "Currently selecting item slot 3":
            self.current_select_label.setText("Currently selecting item slot 1")
            self.selected_item_3.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid #195778;\n"
                                               "}\n"
                                               "")
            self.selected_item_1.setStyleSheet("QLabel {\n"
                                               "background: rgb(18, 48, 64);\n"
                                               "border: 2px solid white;\n"
                                               "}\n"
                                               "")

