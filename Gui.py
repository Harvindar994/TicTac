from PyQt5.QtWidgets import QPushButton, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QWidget, QApplication, QMainWindow, QAction
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QGroupBox, QSpacerItem, QSizePolicy, QLineEdit, QScrollArea, QMenu, QMessageBox
from PyQt5.QtWidgets import  QListWidget, QListView



class test(QWidget):
    def __init__(self):
        self.title = "test window"
        self.X = 100
        self.Y = 100
        self.Width = 300
        self.Height = 300
        super(test, self).__init__()
        self.init_window()

    def init_window(self):
        self.title = "It Is A Test Window"
        self.setWindowTitle(self.title)
        self.setGeometry(self.X, self.Y, self.Width, self.Height)
        self.add_element_in_main_window()
        self.show()

    def list_item(self):
        item = self.list.currentItem()
        print(item.text())
        print(self.list.currentRow())

    def connect(self):
        pass

    def close_application(self):
        self.close()

    def add_element_in_main_window(self):
        self.MainLayout = QHBoxLayout()
        self.setLayout(self.MainLayout)

        self.list = QListWidget()

        # designe

        self.list.setAlternatingRowColors(True)

        #self.list.insertItem(0, "Harvindar Singh")
        #self.list.insertItem(1, "Jagmohan singh")
        #self.list.insertItem(2, "Gurpreet Kaur")
        #self.list.insertItem(3, "Jagjeet Singh")
        #self.list.insertItem(4, "Rupendar Kaur")
        #self.list.insertItem(5, "Harvindar Singh")
        #self.list.insertItem(6, "Jagmohan singh")
        #self.list.insertItem(7, "Gurpreet Kaur")
        #self.list.insertItem(8, "Jagjeet Singh")
        #self.list.insertItem(9, "Rupendar Kaur")

        l1 = QLabel("harvindar Singh")
        l2 = QLabel("Harjindar Singh")
        l3 = QLabel("Gurpreet Kaur")

        self.listLayout1 = QHBoxLayout()
        self.listLayout1.addWidget(l1)
        self.listLayout1.addWidget(l2)
        self.listLayout1.addWidget(l3)

        l1 = QLabel("harvindar Singh")
        l2 = QLabel("Harjindar Singh")
        l3 = QLabel("Gurpreet Kaur")

        self.listLayout2 = QHBoxLayout()
        self.listLayout2.addWidget(l1)
        self.listLayout2.addWidget(l2)
        self.listLayout2.addWidget(l3)

        self.listLayout = QVBoxLayout()
        self.listLayout.addLayout(self.listLayout1)
        self.listLayout.addLayout(self.listLayout2)

        self.list.setLayout(self.listLayout)


        self.list.clicked.connect(self.list_item)

        self.MainLayout.addWidget(self.list)



class SecondTest(QWidget):
    def __init__(self):
        self.title = "test window"
        self.X = 100
        self.Y = 100
        self.Width = 300
        self.Height = 300
        super(SecondTest, self).__init__()
        self.init_window()

    def init_window(self):
        self.title = "It Is A Test Window"
        self.setWindowTitle(self.title)
        self.setGeometry(self.X, self.Y, self.Width, self.Height)
        self.create_gui()
        self.show()

    def create_gui(self):
        # creating spacer item
        self.VSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.HSpacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MainLayout = QHBoxLayout()
        self.setLayout(self.MainLayout)

        # Menu Button's
        self.MenuLayout = QVBoxLayout()
        self.MainLayout.addLayout(self.MenuLayout)
        self.FirstSlide = QPushButton("First Slide")
        self.SecondSlide = QPushButton("Second Slide")
        self.ThirdSlide = QPushButton("Third Slide")
        self.FirstSlide.clicked.connect(lambda l: self.change_slide_count(1))
        self.SecondSlide.clicked.connect(lambda l: self.change_slide_count(2))
        self.ThirdSlide.clicked.connect(lambda l: self.change_slide_count(3))
        self.SlideNumber = QLabel("1..........")
        self.MenuLayout.addWidget(self.FirstSlide)
        self.MenuLayout.addWidget(self.SecondSlide)
        self.MenuLayout.addWidget(self.ThirdSlide)
        self.MenuLayout.addWidget(self.SlideNumber)
        self.MenuLayout.addItem(self.VSpacerItem)

        #self.MainSlideFrame = QFrame()
        #self.MainLayout.addWidget(self.MainSlideFrame)

        #slide 1st

        self.SlideFrame1 = QFrame()
        self.SlideLayout1 = QHBoxLayout()
        self.SlideFrame1.setLayout(self.SlideLayout1)
        button = QPushButton("111111111111111111")
        self.SlideLayout1.addWidget(button)

        # slide 2st

        self.SlideFrame2 = QFrame()
        self.SlideLayout2 = QHBoxLayout()
        self.SlideFrame2.setLayout(self.SlideLayout2)
        button = QPushButton("222222222222")
        self.SlideLayout2.addWidget(button)

        # slide 3st

        self.SlideFrame3 = QFrame()
        self.SlideLayout3 = QHBoxLayout()
        self.SlideFrame3.setLayout(self.SlideLayout3)
        button = QPushButton("333333")
        self.SlideLayout3.addWidget(button)

        #self.MainSlideFrame.setLayout(self.SlideLayout1)
        #self.LastSlide = self.SlideLayout1
        self.MainLayout.addWidget(self.SlideFrame1)
        self.MainLayout.addWidget(self.SlideFrame2)
        self.MainLayout.addWidget(self.SlideFrame3)


    def change_slide_count1(self, slide):
        if slide == 1:
            print(self.MainLayout)
            self.MainLayout.removeWidget(self.LastSlide)

            self.LastSlide = self.SlideFrame1
            self.MainLayout.addWidget(self.SlideFrame1)
            self.SlideNumber.setText("1.....")
        elif slide == 2:
            self.MainLayout.removeWidget(self.LastSlide)
            self.LastSlide = self.SlideFrame2
            self.MainLayout.addWidget(self.SlideFrame2)
            self.SlideNumber.setText("2.....")
        elif slide == 3:
            self.MainLayout.removeWidget(self.LastSlide)
            self.LastSlide = self.SlideFrame3
            self.MainLayout.addWidget(self.SlideFrame3)
            self.SlideNumber.setText("3.....")

    def change_slide_count2(self, slide):
        if slide == 1:
            self.MainSlideFrame.setLayout(self.SlideLayout1)
            self.SlideNumber.setText("1.....")
        if slide == 2:
            self.MainSlideFrame.setLayout(self.SlideLayout2)
            self.SlideNumber.setText("2.....")
        if slide == 3:
            self.MainSlideFrame.setLayout(self.SlideLayout3)
            self.SlideNumber.setText("3.....")

    def change_slide_count(self, slide):
        if slide == 1:
            self.SlideFrame1.show()
            self.SlideFrame2.hide()
            self.SlideFrame3.hide()
        if slide == 2:
            self.SlideFrame2.show()
            self.SlideFrame3.hide()
            self.SlideFrame1.hide()
        if slide == 3:
            self.SlideFrame3.show()
            self.SlideFrame2.hide()
            self.SlideFrame1.hide()

aap = QApplication([])

window = test()

sys.exit(aap.exec_())