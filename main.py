from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QApplication, QSpacerItem, QSizePolicy
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
import sys

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
        self.show()

    def set_layout_in_mainlayout(self, new_layout, old_layout=None):
        if old_layout is not None:
            self.MainLayout.removeLayout(old_layout)
        self.MainLayout.addLayout(new_layout)

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
        self.PlayGame_Block_1 = QPushButton("O")
        self.PlayGame_Block_2 = QPushButton("O")
        self.PlayGame_Block_3 = QPushButton("X")
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
        self.PlayGame_Block_4 = QPushButton("X")
        self.PlayGame_Block_5 = QPushButton("X")
        self.PlayGame_Block_6 = QPushButton("X")
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
