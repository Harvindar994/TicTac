from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QApplication, QSpacerItem, QSizePolicy
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
import sys

class TicTac(QWidget):
    def __init__(self):
        self.Title = "Tic Tac"
        self.Top = 200
        self.Left = 300
        self.Width = 200
        self.Height = 250
        super(TicTac, self).__init__()
        self.initwindow()

    def initwindow(self):
        self.setWindowTitle(self.Title)
        self.setGeometry(self.Left, self.Top, self.Width, self.Height)
        self.setStyleSheet("background-image: url(Media/background/Tictac.png);")
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
        self.setLayout(self.MainLayout)

        # creating game play layout. VBoxLayout
        self.GamePlayLayout_VBoxLayout = QVBoxLayout()
        self.set_layout_in_mainlayout(self.GamePlayLayout_VBoxLayout)

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
        Label = QLabel("TIC TAC")
        Label_StyleSheet = "QLabel{\n" \
                           "font-size: 28px;\n" \
                           "color: white;\n" \
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
                           "font-size: 28px;\n" \
                           "color: white;\n" \
                           "}"
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
