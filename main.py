from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QApplication, QSpacerItem, QSizePolicy, QDialog
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore
import numpy as np
import sys
import random
import pickle

class GameReset(QDialog):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        super(GameReset, self).__init__()
        self.initwindow()

    def initwindow(self):
        self.setWindowTitle(self.MainWindow.Title)
        self.setGeometry(self.MainWindow.Left+210, self.MainWindow.Top, self.MainWindow.Width, self.MainWindow.Height)
        self.create_depend_layout()
        self.create_game_reset_layout()
        self.linking_Button()

    def linking_Button(self):
        self.CloseButton.clicked.connect(self.MainWindow.close_game)
        self.GameResetButton.clicked.connect(self.reset_game)

    def reset_game(self):
        self.MainWindow.reset_game()
        self.close()

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
                           "margin-top:0px;\n" \
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
        self.GameReset_MsgLabel = QLabel("")
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
        self.GameReset_MsgLabel.setStyleSheet(self.MsgLabel_StyleSheet_Green)
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

        # Game Algo Variable
        self.Winner = None
        self.Reserved_Block = []
        self.Blocks_Matrix = self.get_empty_array()

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
        Loop = True
        if not self.set_value_in_block(block, "X"):
            return
        value = self.check_patter()
        if self.take_game_winandlos_disicion(value):
            self.reset_game()
            self.set_default_StyleSheet_ofBlock()
            return

        while Loop:
            Loop = False
            self.teke_step()
            value = self.check_patter()
            if self.take_game_winandlos_disicion(value):
                self.reset_game()
                self.set_default_StyleSheet_ofBlock()
                Loop = True

    def select_from_empty_block(self, emptyblock, value):
        selected = 0
        mat_pattern = [[(0, 0), (0, 1), (0, 2), (1, 2, 3)],
                       [(1, 0), (1, 1), (1, 2), (4, 5, 6)],
                       [(2, 0), (2, 1), (2, 2), (7, 8, 9)],
                       [(0, 0), (1, 1), (2, 2), (1, 5, 9)],
                       [(0, 2), (1, 1), (2, 0), (3, 5, 7)],
                       [(0, 0), (1, 0), (2, 0), (1, 4, 7)],
                       [(0, 1), (1, 1), (2, 1), (2, 5, 8)],
                       [(0, 2), (1, 2), (2, 2), (3, 6, 9)]]
        for block in mat_pattern:
            c1, c2, c3, blocks = block
            b1, b2, b3 = blocks
            if self.Blocks_Matrix[c1] == value or self.Blocks_Matrix[c1] == 'E':
                if self.Blocks_Matrix[c1] == 'E':
                    if b1 in emptyblock:
                        selected = b1
                    else:
                        selected = 0
                        continue
                if self.Blocks_Matrix[c2] == value or self.Blocks_Matrix[c2] == 'E':
                    if self.Blocks_Matrix[c2] == 'E':
                        if selected == b1:
                            selected = 0
                            continue
                        if b2 in emptyblock:
                            selected = b2
                        else:
                            selected = 0
                            continue
                    if self.Blocks_Matrix[c3] == value or self.Blocks_Matrix[c3] == 'E':
                        if self.Blocks_Matrix[c3] == 'E':
                            if selected == b2 or selected == b1:
                                selected = 0
                                continue
                            if b3 in emptyblock:
                                selected = b3
                                return selected
                            else:
                                selected = 0
                                continue
                        else:
                            if selected != 0:
                                return selected
            else:
                selected = 0
                continue
        return False


    def take_game_winandlos_disicion(self, value):
        if value != False:
            if value == 'X':
                self.Winner = 'user'
                self.GameReset.GameReset_MsgLabel.setText("You Won")
            elif value == 'O':
                self.Winner = 'pc'
                self.GameReset.GameReset_MsgLabel.setText("You Lost")
            self.GameReset.exec_()
            return True
        if len(self.Reserved_Block) == 9:
            self.Winner = 'drow'
            self.GameReset.GameReset_MsgLabel.setText("Game Drow")
            self.GameReset.exec_()
            return True
        return False

    def set_default_StyleSheet_ofBlock(self):
        self.PlayGame_Block_1.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_2.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_3.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_4.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_5.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_6.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_7.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_8.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_9.setStyleSheet(self.Block_StyleSheet)

    def teke_step(self):
        unreserved_block = self.get_unreserved_block()
        selected = self.select_from_empty_block(unreserved_block, 'O')
        if not selected:
            selected = self.select_from_empty_block(unreserved_block, 'X')
            if not selected:
                if 5 in unreserved_block:
                    self.set_value_in_block(5, 'O')
                else:
                    selected = random.randint(0, len(unreserved_block)-1)
                    self.set_value_in_block(unreserved_block[selected], 'O')
            else:
                self.set_value_in_block(selected, 'O')
        else:
            self.set_value_in_block(selected, 'O')

    def set_value_in_block(self, block, value):
        if block == 1 and block not in self.Reserved_Block:
            self.PlayGame_Block_1.setText(value)
            self.Blocks_Matrix[0, 0] = value
            self.Reserved_Block.append(block)
        elif block == 2 and block not in self.Reserved_Block:
            self.PlayGame_Block_2.setText(value)
            self.Blocks_Matrix[0, 1] = value
            self.Reserved_Block.append(block)
        elif block == 3 and block not in self.Reserved_Block:
            self.PlayGame_Block_3.setText(value)
            self.Blocks_Matrix[0, 2] = value
            self.Reserved_Block.append(block)
        elif block == 4 and block not in self.Reserved_Block:
            self.PlayGame_Block_4.setText(value)
            self.Blocks_Matrix[1, 0] = value
            self.Reserved_Block.append(block)
        elif block == 5 and block not in self.Reserved_Block:
            self.PlayGame_Block_5.setText(value)
            self.Blocks_Matrix[1, 1] = value
            self.Reserved_Block.append(block)
        elif block == 6 and block not in self.Reserved_Block:
            self.PlayGame_Block_6.setText(value)
            self.Blocks_Matrix[1, 2] = value
            self.Reserved_Block.append(block)
        elif block == 7 and block not in self.Reserved_Block:
            self.PlayGame_Block_7.setText(value)
            self.Blocks_Matrix[2, 0] = value
            self.Reserved_Block.append(block)
        elif block == 8 and block not in self.Reserved_Block:
            self.PlayGame_Block_8.setText(value)
            self.Blocks_Matrix[2, 1] = value
            self.Reserved_Block.append(block)
        elif block == 9 and block not in self.Reserved_Block:
            self.PlayGame_Block_9.setText(value)
            self.Blocks_Matrix[2, 2] = value
            self.Reserved_Block.append(block)
        else:
            return False
        return True

    def get_empty_array(self):
        array = np.array([['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']])
        return array

    def get_unreserved_block(self):
        count = 1
        unreserved_block = []
        while count <= 9:
            if count not in self.Reserved_Block:
                unreserved_block.append(count)
            count += 1
        return unreserved_block

    def check_patter(self, blocks_matrix=None, change_block_color=True):
        if blocks_matrix is None:
            blocks_matrix = self.Blocks_Matrix
        pattern = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
        mat_pattern = [[(0, 0), (0, 1), (0, 2), (1, 2, 3)],
                       [(1, 0), (1, 1), (1, 2), (4, 5, 6)],
                       [(2, 0), (2, 1), (2, 2), (7, 8, 9)],
                       [(0, 0), (1, 1), (2, 2), (1, 5, 9)],
                       [(0, 2), (1, 1), (2, 0), (3, 5, 7)],
                       [(0, 0), (1, 0), (2, 0), (1, 4, 7)],
                       [(0, 1), (1, 1), (2, 1), (2, 5, 8)],
                       [(0, 2), (1, 2), (2, 2), (3, 6, 9)]]
        for p_data in mat_pattern:
            c1, c2, c3, group = p_data
            if blocks_matrix[c1] != "E" and blocks_matrix[c2] != "E" and blocks_matrix[c3] != "E":
                if blocks_matrix[c1] == blocks_matrix[c2] == blocks_matrix[c3]:
                    if change_block_color:
                        b1, b2, b3 = group
                        if b1 == 1 or b2 == 1 or b3 == 1:
                            self.PlayGame_Block_1.setStyleSheet(self.WinBlock_StyleSheet)
                        if b1 == 2 or b2 == 2 or b3 == 2:
                            self.PlayGame_Block_2.setStyleSheet(self.WinBlock_StyleSheet)
                        if b1 == 3 or b2 == 3 or b3 == 3:
                            self.PlayGame_Block_3.setStyleSheet(self.WinBlock_StyleSheet)
                        if b1 == 4 or b2 == 4 or b3 == 4:
                            self.PlayGame_Block_4.setStyleSheet(self.WinBlock_StyleSheet)
                        if b1 == 5 or b2 == 5 or b3 == 5:
                            self.PlayGame_Block_5.setStyleSheet(self.WinBlock_StyleSheet)
                        if b1 == 6 or b2 == 6 or b3 == 6:
                            self.PlayGame_Block_6.setStyleSheet(self.WinBlock_StyleSheet)
                        if b1 == 7 or b2 == 7 or b3 == 7:
                            self.PlayGame_Block_7.setStyleSheet(self.WinBlock_StyleSheet)
                        if b1 == 8 or b2 == 8 or b3 == 8:
                            self.PlayGame_Block_8.setStyleSheet(self.WinBlock_StyleSheet)
                        if b1 == 9 or b2 == 9 or b3 == 9:
                            self.PlayGame_Block_9.setStyleSheet(self.WinBlock_StyleSheet)

                    return blocks_matrix[c1]
        else:
            return False

    def reset_game(self, bybutton=False):
        self.Winner = None
        self.Reserved_Block = []
        self.Blocks_Matrix = self.get_empty_array()
        self.PlayGame_Block_1.setText("")
        self.PlayGame_Block_2.setText("")
        self.PlayGame_Block_3.setText("")
        self.PlayGame_Block_4.setText("")
        self.PlayGame_Block_5.setText("")
        self.PlayGame_Block_6.setText("")
        self.PlayGame_Block_7.setText("")
        self.PlayGame_Block_8.setText("")
        self.PlayGame_Block_9.setText("")

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
        self.ResetButton.clicked.connect(lambda x: self.reset_game(True))


    def get_QIcon(self, path):
        icon = QtGui.QIcon(path)
        return icon

    def get_QSize(self, width, height):
        return QtCore.QSize(width, height)

    def get_QCursor(self, cursor):
        if cursor == 'pointer':
            return QtCore.Qt.PointingHandCursor

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
                           "margin-top:0px;\n" \
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

        self.Block_StyleSheet = "QPushButton{\n" \
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
        self.WinBlock_StyleSheet = "QPushButton{\n" \
                                   "background: transparent;\n" \
                                   "background-color: green;\n" \
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
        self.PlayGame_Block_1.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_2.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_3.setStyleSheet(self.Block_StyleSheet)
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
        self.PlayGame_Block_4.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_5.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_6.setStyleSheet(self.Block_StyleSheet)
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
        self.PlayGame_Block_7.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_8.setStyleSheet(self.Block_StyleSheet)
        self.PlayGame_Block_9.setStyleSheet(self.Block_StyleSheet)
        HBoxLayout.addItem(self.HSpacerItem)
        HBoxLayout.addWidget(self.PlayGame_Block_7)
        HBoxLayout.addWidget(self.PlayGame_Block_8)
        HBoxLayout.addWidget(self.PlayGame_Block_9)
        HBoxLayout.addItem(self.HSpacerItem)
        self.PlayGame_BlocksVBoxLayout.addLayout(HBoxLayout)

        # reset Button H Box Layout.
        self.ResetButton_HBoxLayout = QHBoxLayout()
        self.ResetButton_HBoxLayout.setSpacing(0)
        self.ResetButton_HBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.GamePlayLayout_VBoxLayout.addLayout(self.ResetButton_HBoxLayout)

        # creating reset button.
        self.ResetButton = QPushButton("")
        StyleSheet = "QPushButton{\n" \
                     "background: transparent;\n" \
                     "}\n" \
                     "QPushButton:hover{\n" \
                     "background-color: #22B8CF;" \
                     "border-radius: 5px;\n" \
                     "}"
        self.ResetButton.setStyleSheet(StyleSheet)
        self.ResetButton.setCursor(self.get_QCursor("pointer"))
        self.ResetButton.setIcon(self.get_QIcon("Media/Icon/replay.png"))
        self.ResetButton_HBoxLayout.addItem(self.HSpacerItem)
        self.ResetButton_HBoxLayout.addWidget(self.ResetButton)
        self.ResetButton_HBoxLayout.addItem(self.HSpacerItem)

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
                           "margin-top:10px;\n" \
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
