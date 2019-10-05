from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QApplication, QSpacerItem, QSizePolicy, QDialog
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
import sys

class GameReset(QDialog):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        super(GameReset, self).__init__()
        self.initwindow()

    def initwindow(self):
        self.setWindowTitle(self.MainWindow.Title)
        self.setGeometry(self.MainWindow.Left, self.MainWindow.Top, self.MainWindow.Width, self.MainWindow.Height)
        self.create_depend_layout()
        self.create_game_reset_layout()
        self.linking_Button()

    def linking_Button(self):
        self.CloseButton.clicked.connect(self.MainWindow.close_game)

    def create_depend_layout(self):
        # creating spacer item
        self.VSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.HSpacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # creating vertical line
        self.VLine = QFrame()
        self.VLine.setFrameShape(QFrame.VLine)
        self.VLine_StyleSheet = "QFrame{\n" \
                                "color: #CCCCCC;\n" \
                                "}"
        self.VLine.setStyleSheet(self.VLine_StyleSheet)
        self.VLine.setObjectName("VLine")

        # creating horizatal line
        self.HLine = QFrame()
        self.HLine.setFrameShape(QFrame.HLine)
        self.HLine_StyleSheet = "QFrame{\n" \
                                "color: #CCCCCC;\n" \
                                "}"
        self.HLine.setStyleSheet(self.VLine_StyleSheet)
        self.HLine.setObjectName("HLine")

    def create_game_reset_layout(self):
        # creating main Layout.
        self.MainLayout = QHBoxLayout()
        self.MainLayout.setSpacing(0)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.MainLayout)

        # creating game Play Frame Main.
        self.GameReset_MainFrame = QFrame()
        StyleSheet = "QFrame{\n" \
                     "background-image: url(Media/background/Tictac.png);\n" \
                     "}"
        self.GameReset_MainFrame.setStyleSheet(StyleSheet)
        self.MainLayout.addWidget(self.GameReset_MainFrame)

        # creating game play layout. VBoxLayout
        self.GameReset_VBoxLayout = QVBoxLayout()
        self.GameReset_VBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.GameReset_VBoxLayout.setSpacing(0)
        self.GameReset_MainFrame.setLayout(self.GameReset_VBoxLayout)

        # creating game name label top Layout.
        self.GameResetLayout_NameLayout = QVBoxLayout()
        self.GameResetLayout_NameLayout.setSpacing(0)
        self.GameResetLayout_NameLayout.setContentsMargins(0, 0, 0, 0)
        self.GameReset_VBoxLayout.addLayout(self.GameResetLayout_NameLayout)
        HBoxLayout = QHBoxLayout()
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.setSpacing(0)
        self.GameResetLayout_NameLayout.addLayout(HBoxLayout)
        HBoxLayout.addItem(self.HSpacerItem)
        Label = QLabel("Tic Tac")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 40px;\n" \
                           "background: transparent;\n" \
                           "color: white;\n" \
                           "font-family: Glacial Indifference;\n" \
                           "margin-top:8px;\n" \
                           "}"
        Label.setStyleSheet(Label_StyleSheet)
        HBoxLayout.addWidget(Label)
        HBoxLayout.addItem(self.HSpacerItem)

        HBoxLayout = QHBoxLayout()
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.setSpacing(0)
        self.GameResetLayout_NameLayout.addLayout(HBoxLayout)
        HBoxLayout.addItem(self.HSpacerItem)
        Label = QLabel("BRIGHTGOAL")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 12px;\n" \
                           "color: white;\n" \
                           "font-family: Glacial Indifference;\n" \
                           "background: transparent;\n" \
                           "letter-spacing:2px;\n" \
                           "margin-top: -10px;\n" \
                           "margin-left: 50px;\n" \
                           "}"
        Label.setStyleSheet(Label_StyleSheet)
        HBoxLayout.addWidget(Label)
        HBoxLayout.addItem(self.HSpacerItem)

        # creating frame to set ResetGame_BlockVBoxLayout.
        self.GameReset_MainBlocksFrame = QFrame()
        StyleSheet = "QFrame{\n" \
                     "margin-top: 0px;\n" \
                     "margin-bottom: 0px;\n" \
                     "background-image: url(Media/background/transbg.png);\n" \
                     "}"
        self.GameReset_MainBlocksFrame.setStyleSheet(StyleSheet)

        # creating Reset Or Close Button

        self.GameReset_BlocksVBoxLayout  = QVBoxLayout()
        self.GameReset_BlocksVBoxLayout.setSpacing(5)
        self.GameReset_MainBlocksFrame.setLayout(self.GameReset_BlocksVBoxLayout)

        StyleSheet = "QPushButton{\n" \
                     "background: transparent;\n" \
                     "background-image: url(Media/Background/blockbg.png);\n" \
                     "color: white;\n" \
                     "border: 0px solid #9EDFEF;\n" \
                     "border-bottom: 4px solid #3C3F41;\n" \
                     "padding: 10px 20px 10px 20px;\n" \
                     "font-size: 15px;\n" \
                     "}\n" \
                     "QPushButton:hover{\n" \
                     "background-image: url(Media/Background/blockbghover.png);\n" \
                     "color: white;\n" \
                     "}"
        # creating msg label.
        MsgHBoxLayout = QHBoxLayout()
        self.GameReset_MsgLabel = QLabel("You Won")
        self.MsgLabel_StyleSheet_Green = "QLabel{\n" \
                              "color: white;\n" \
                              "font-size: 17px;\n" \
                              "color: white;\n" \
                              "background-color: green;\n" \
                              "padding: 5px 15px 5px 15px;\n" \
                              "border-radius: 15px;\n" \
                              "font-family: Glacial Indifference;\n" \
                              "margin-bottom: 10px;\n" \
                              "margin-top: 10px;\n" \
                              "}"
        self.MsgLabel_StyleSheet_Red = "QLabel{\n" \
                                         "color: white;\n" \
                                         "font-size: 17px;\n" \
                                         "color: white;\n" \
                                         "background-color: #DD5044;\n" \
                                         "padding: 5px 15px 5px 15px;\n" \
                                         "border-radius: 15px;\n" \
                                         "font-family: Glacial Indifference;\n" \
                                         "margin-bottom: 10px;\n" \
                                         "margin-top: 10px;\n" \
                                         "}"
        self.MsgLabel_StyleSheet_yellow = "QLabel{\n" \
                                          "color: white;\n" \
                                          "font-size: 17px;\n" \
                                          "color: white;\n" \
                                          "background-color: #FF9800;\n" \
                                          "padding: 5px 15px 5px 15px;\n" \
                                          "border-radius: 15px;\n" \
                                          "font-family: Glacial Indifference;\n" \
                                          "margin-bottom: 10px;\n" \
                                          "margin-top: 10px;\n" \
                                          "}"
        self.GameReset_MsgLabel.setStyleSheet(self.MsgLabel_StyleSheet_yellow)
        MsgHBoxLayout.addItem(self.HSpacerItem)
        MsgHBoxLayout.addWidget(self.GameReset_MsgLabel)
        MsgHBoxLayout.addItem(self.HSpacerItem)
        self.GameReset_BlocksVBoxLayout.addLayout(MsgHBoxLayout)

        self.GameResetButton = QPushButton("Reset")
        self.GameResetButton.setStyleSheet(StyleSheet)

        self.CloseButton = QPushButton("Close")
        self.CloseButton.setStyleSheet(StyleSheet)

        self.GameReset_BlocksVBoxLayout.addWidget(self.GameResetButton)
        self.GameReset_BlocksVBoxLayout.addWidget(self.CloseButton)

        self.GameReset_VBoxLayout.addWidget(self.GameReset_MainBlocksFrame)

        # creating bottom developer Name.
        self.GameResetLayout_DeveloperNameLayout = QVBoxLayout()
        self.GameResetLayout_DeveloperNameLayout.setSpacing(0)
        self.GameResetLayout_DeveloperNameLayout.setContentsMargins(0, 0, 0, 0)
        self.GameReset_VBoxLayout.addLayout(self.GameResetLayout_DeveloperNameLayout)
        HBoxLayout = QHBoxLayout()
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.setSpacing(0)
        self.GameResetLayout_DeveloperNameLayout.addLayout(HBoxLayout)
        HBoxLayout.addItem(self.HSpacerItem)
        Label = QLabel("DEVELOPED BY")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 12px;\n" \
                           "background: transparent;\n" \
                           "color: white;\n" \
                           "font-family: Glacial Indifference;\n" \
                           "margin-top:15px;\n" \
                           "}"
        Label.setStyleSheet(Label_StyleSheet)
        HBoxLayout.addWidget(Label)
        HBoxLayout.addItem(self.HSpacerItem)

        HBoxLayout = QHBoxLayout()
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.setSpacing(0)
        self.GameResetLayout_DeveloperNameLayout.addLayout(HBoxLayout)
        HBoxLayout.addItem(self.HSpacerItem)
        Label = QLabel("HARVINDAR SINGH")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 12px;\n" \
                           "color: white;\n" \
                           "font-family: Glacial Indifference;\n" \
                           "background: transparent;\n" \
                           "letter-spacing:2px;\n" \
                           "margin-top: -10px;\n" \
                           "margin-bottom: 5px;\n" \
                           "}"
        Label.setStyleSheet(Label_StyleSheet)
        HBoxLayout.addWidget(Label)
        HBoxLayout.addItem(self.HSpacerItem)

        self.GameReset_VBoxLayout.addItem(self.VSpacerItem)

class TicTac(QWidget):
    def __init__(self):
        self.Title = "Tic Tac"
        self.Top = 200
        self.Left = 300
        self.Width = 190
        self.Height = 300
        QtGui.QFontDatabase.addApplicationFont("Media/Font/Glacial Indifference.otf")
        QtGui.QFontDatabase.addApplicationFont("Media/Font/Glacial Indifference Bold.otf")
        super(TicTac, self).__init__()
        self.initwindow()

    def initwindow(self):
        self.setWindowTitle(self.Title)
        self.setGeometry(self.Left, self.Top, self.Width, self.Height)
        self.create_depend_layout()
        self.create_game_play_layout()
        self.connect_button()
        # creating Game Reset Window
        self.GameReset = GameReset(self)
        self.show()

    def play_next(self, block):
        if block == 1:
            self.PlayGame_Block_1.setText("X")
        elif block == 2:
            self.PlayGame_Block_2.setText("X")
        elif block == 3:
            self.PlayGame_Block_3.setText("X")
        elif block == 4:
            self.PlayGame_Block_4.setText("X")
        elif block == 5:
            self.PlayGame_Block_5.setText("X")
        elif block == 6:
            self.PlayGame_Block_6.setText("X")
        elif block == 7:
            self.PlayGame_Block_7.setText("X")
        elif block == 8:
            self.PlayGame_Block_8.setText("X")
        elif block == 9:
            self.PlayGame_Block_9.setText("X")

    def connect_button(self):
        self.PlayGame_Block_1.clicked.connect(lambda x: self.play_next(1))
        self.PlayGame_Block_2.clicked.connect(lambda x: self.play_next(2))
        self.PlayGame_Block_3.clicked.connect(lambda x: self.play_next(3))
        self.PlayGame_Block_4.clicked.connect(lambda x: self.play_next(4))
        self.PlayGame_Block_5.clicked.connect(lambda x: self.play_next(5))
        self.PlayGame_Block_6.clicked.connect(lambda x: self.play_next(6))
        self.PlayGame_Block_7.clicked.connect(lambda x: self.play_next(7))
        self.PlayGame_Block_8.clicked.connect(lambda x: self.play_next(8))
        self.PlayGame_Block_9.clicked.connect(lambda x: self.play_next(9))

    def set_layout_in_mainlayout(self, new_layout, old_layout=None):
        if old_layout is not None:
            self.MainLayout.removeLayout(old_layout)
        self.MainLayout.addLayout(new_layout)

    def close_game(self):
        self.GameReset.close()
        self.close()
        sys.exit()

    def create_game_play_layout(self):
        # creating main Layout of playgame
        self.MainLayout = QHBoxLayout()
        self.MainLayout.setSpacing(0)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.MainLayout)

        # creating game Play Frame Main.
        self.GamePlayMainFrame = QFrame()
        StyleSheet = "QFrame{\n" \
                     "background-image: url(Media/background/Tictac.png);\n" \
                     "}"
        self.GamePlayMainFrame.setStyleSheet(StyleSheet)
        self.MainLayout.addWidget(self.GamePlayMainFrame)

        # creating game play layout. VBoxLayout
        self.GamePlayLayout_VBoxLayout = QVBoxLayout()
        self.GamePlayLayout_VBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.GamePlayLayout_VBoxLayout.setSpacing(0)
        self.GamePlayMainFrame.setLayout(self.GamePlayLayout_VBoxLayout)

        # creating game name label top Layout.
        self.GamePlayLayout_NameLayout = QVBoxLayout()
        self.GamePlayLayout_NameLayout.setSpacing(0)
        self.GamePlayLayout_NameLayout.setContentsMargins(0, 0, 0, 0)
        self.GamePlayLayout_VBoxLayout.addLayout(self.GamePlayLayout_NameLayout)
        HBoxLayout = QHBoxLayout()
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.setSpacing(0)
        self.GamePlayLayout_NameLayout.addLayout(HBoxLayout)
        HBoxLayout.addItem(self.HSpacerItem)
        Label = QLabel("Tic Tac")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 40px;\n" \
                           "background: transparent;\n" \
                           "color: white;\n" \
                           "font-family: Glacial Indifference;\n" \
                           "margin-top:8px;\n" \
                           "}"
        Label.setStyleSheet(Label_StyleSheet)
        HBoxLayout.addWidget(Label)
        HBoxLayout.addItem(self.HSpacerItem)

        HBoxLayout = QHBoxLayout()
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.setSpacing(0)
        self.GamePlayLayout_NameLayout.addLayout(HBoxLayout)
        HBoxLayout.addItem(self.HSpacerItem)
        Label = QLabel("BRIGHTGOAL")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 12px;\n" \
                           "color: white;\n" \
                           "font-family: Glacial Indifference;\n" \
                           "background: transparent;\n" \
                           "letter-spacing:2px;\n" \
                           "margin-top: -10px;\n" \
                           "margin-left: 50px;\n" \
                           "}"
        Label.setStyleSheet(Label_StyleSheet)
        HBoxLayout.addWidget(Label)
        HBoxLayout.addItem(self.HSpacerItem)

        # creating frame to set PlayGame_BlockVBoxLayout.
        self.PlayGame_MainBlocksFrame = QFrame()
        StyleSheet = "QFrame{\n" \
                     "margin-top: 10px;\n" \
                     "background-image: url(Media/background/transbg.png);\n" \
                     "}"
        self.PlayGame_MainBlocksFrame.setStyleSheet(StyleSheet)
        self.GamePlayLayout_VBoxLayout.addWidget(self.PlayGame_MainBlocksFrame)

        # creating block of play game.
        self.PlayGame_BlocksVBoxLayout  = QVBoxLayout()
        self.PlayGame_BlocksVBoxLayout.setSpacing(5)
        self.PlayGame_MainBlocksFrame.setLayout(self.PlayGame_BlocksVBoxLayout)

        StyleSheet = "QPushButton{\n" \
                     "background: transparent;\n" \
                     "background-image: url(Media/Background/blockbg.png);\n" \
                     "color: white;\n" \
                     "border: 0px solid #9EDFEF;\n" \
                     "border-bottom: 4px solid #3C3F41;\n" \
                     "padding: 10px 20px 10px 20px;\n" \
                     "font-size: 15px;\n" \
                     "}\n" \
                     "QPushButton:hover{\n" \
                     "background-image: url(Media/Background/blockbghover.png);\n" \
                     "color: white;\n" \
                     "}"

        MaxWidth = 49
        HBoxLayout = QHBoxLayout()
        self.PlayGame_Block_1 = QPushButton("")
        self.PlayGame_Block_2 = QPushButton("")
        self.PlayGame_Block_3 = QPushButton("")
        self.PlayGame_Block_1.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_2.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_3.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_1.setStyleSheet(StyleSheet)
        self.PlayGame_Block_2.setStyleSheet(StyleSheet)
        self.PlayGame_Block_3.setStyleSheet(StyleSheet)
        HBoxLayout.addItem(self.HSpacerItem)
        HBoxLayout.addWidget(self.PlayGame_Block_1)
        HBoxLayout.addWidget(self.PlayGame_Block_2)
        HBoxLayout.addWidget(self.PlayGame_Block_3)
        HBoxLayout.addItem(self.HSpacerItem)
        self.PlayGame_BlocksVBoxLayout.addLayout(HBoxLayout)

        HBoxLayout = QHBoxLayout()
        self.PlayGame_Block_4 = QPushButton("")
        self.PlayGame_Block_5 = QPushButton("")
        self.PlayGame_Block_6 = QPushButton("")
        self.PlayGame_Block_4.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_5.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_6.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_4.setStyleSheet(StyleSheet)
        self.PlayGame_Block_5.setStyleSheet(StyleSheet)
        self.PlayGame_Block_6.setStyleSheet(StyleSheet)
        HBoxLayout.addItem(self.HSpacerItem)
        HBoxLayout.addWidget(self.PlayGame_Block_4)
        HBoxLayout.addWidget(self.PlayGame_Block_5)
        HBoxLayout.addWidget(self.PlayGame_Block_6)
        HBoxLayout.addItem(self.HSpacerItem)
        self.PlayGame_BlocksVBoxLayout.addLayout(HBoxLayout)

        HBoxLayout = QHBoxLayout()
        self.PlayGame_Block_7 = QPushButton("")
        self.PlayGame_Block_8 = QPushButton("")
        self.PlayGame_Block_9 = QPushButton("")
        self.PlayGame_Block_7.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_8.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_9.setMaximumWidth(MaxWidth)
        self.PlayGame_Block_7.setStyleSheet(StyleSheet)
        self.PlayGame_Block_8.setStyleSheet(StyleSheet)
        self.PlayGame_Block_9.setStyleSheet(StyleSheet)
        HBoxLayout.addItem(self.HSpacerItem)
        HBoxLayout.addWidget(self.PlayGame_Block_7)
        HBoxLayout.addWidget(self.PlayGame_Block_8)
        HBoxLayout.addWidget(self.PlayGame_Block_9)
        HBoxLayout.addItem(self.HSpacerItem)
        self.PlayGame_BlocksVBoxLayout.addLayout(HBoxLayout)

        # creating reset button.
        self.ResetButton = QPushButton("reset")
        self.GamePlayLayout_VBoxLayout.addWidget(self.ResetButton)

        # creating bottom developer Name.
        self.GamePlayLayout_DeveloperNameLayout = QVBoxLayout()
        self.GamePlayLayout_DeveloperNameLayout.setSpacing(0)
        self.GamePlayLayout_DeveloperNameLayout.setContentsMargins(0, 0, 0, 0)
        self.GamePlayLayout_VBoxLayout.addLayout(self.GamePlayLayout_DeveloperNameLayout)
        HBoxLayout = QHBoxLayout()
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.setSpacing(0)
        self.GamePlayLayout_DeveloperNameLayout.addLayout(HBoxLayout)
        HBoxLayout.addItem(self.HSpacerItem)
        Label = QLabel("DEVELOPED BY")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 12px;\n" \
                           "background: transparent;\n" \
                           "color: white;\n" \
                           "font-family: Glacial Indifference;\n" \
                           "margin-top:15px;\n" \
                           "}"
        Label.setStyleSheet(Label_StyleSheet)
        HBoxLayout.addWidget(Label)
        HBoxLayout.addItem(self.HSpacerItem)

        HBoxLayout = QHBoxLayout()
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.setSpacing(0)
        self.GamePlayLayout_DeveloperNameLayout.addLayout(HBoxLayout)
        HBoxLayout.addItem(self.HSpacerItem)
        Label = QLabel("HARVINDAR SINGH")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 12px;\n" \
                           "color: white;\n" \
                           "font-family: Glacial Indifference;\n" \
                           "background: transparent;\n" \
                           "letter-spacing:2px;\n" \
                           "margin-top: -10px;\n" \
                           "margin-bottom: 5px;\n" \
                           "}"
        Label.setStyleSheet(Label_StyleSheet)
        HBoxLayout.addWidget(Label)
        HBoxLayout.addItem(self.HSpacerItem)


        self.GamePlayLayout_VBoxLayout.addItem(self.VSpacerItem)

    def create_depend_layout(self):
        # creating spacer item
        self.VSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.HSpacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # creating vertical line
        self.VLine = QFrame()
        self.VLine.setFrameShape(QFrame.VLine)
        self.VLine_StyleSheet = "QFrame{\n" \
                                "color: #CCCCCC;\n" \
                                "}"
        self.VLine.setStyleSheet(self.VLine_StyleSheet)
        self.VLine.setObjectName("VLine")

        # creating horizatal line
        self.HLine = QFrame()
        self.HLine.setFrameShape(QFrame.HLine)
        self.HLine_StyleSheet = "QFrame{\n" \
                                "color: #CCCCCC;\n" \
                                "}"
        self.HLine.setStyleSheet(self.VLine_StyleSheet)
        self.HLine.setObjectName("HLine")

TicTacApplication = QApplication(sys.argv)
Window = TicTac()
sys.exit(TicTacApplication.exec_())
