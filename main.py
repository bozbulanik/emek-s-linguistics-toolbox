#emek's linguistics tool
from PyQt5 import QtCore, QtGui, QtWidgets
class PlainTextWithButton(QtWidgets.QFrame):
    def __init__(self, parent):
        QtWidgets.QFrame.__init__(self, parent)
        
        self.setStyleSheet("""
                
        QFrame{
        background: #e4e4e4;
        color: #000;
        border-radius: 7px;

        }
        QPlainText:text::highlighted{
        color: rgb(3, 218, 197);
        }
        QPushButton{
        background: #e4e4e4;
        border-radius: 7px;
        color: rgb(133, 218, 210);
        }
        QPushButton:hover{
        background: rgb(218, 218, 218);
            color: rgb(133, 218, 210);
        }
        QPushButton:clicked{
        background:rgb(176, 176, 176);
        rgb(156, 255, 246)
        }
        """)
        self.textArea = QtWidgets.QPlainTextEdit(self)
        self.textArea.setGeometry(0,0,770,110)
        self.textArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textArea.setReadOnly(True)
        self.copyButton = QtWidgets.QPushButton(self)
        self.copyButton.setGeometry(660,110,100,32)
        self.copyButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
        self.copyButton.setMinimumSize(100,0)
        self.copyButton.setText("KOPYALA")
        self.textArea.setPlainText("QtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedvQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.FixedQtWidgets.QSizePolicy.Fixedv")

class Content(QtWidgets.QFrame):
    def __init__(self, parent):
        QtWidgets.QFrame.__init__(self, parent)
        self.setGeometry(0,0,770,490)
        self.setStyleSheet("background-color: none;")
        self.flayout = QtWidgets.QGridLayout()
        self.flayout.setContentsMargins(15,15,15,15)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hece ayırıcı v0.1")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.flayout.addWidget(self.label)

        self.text = QtWidgets.QPlainTextEdit(self)
        self.text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text.setPlaceholderText("Giriniz...")
        self.flayout.addWidget(self.text)
        self.text.setStyleSheet("""
        QPlainTextEdit{
            color: #fff;
            background-color: #2f2f2f;
            border: none;
            border-radius: 7px;
        }
        QPlainTextEdit:focus{
            color: #fff;
            background-color: #393939;
            border-top: none;
            border-bottom: 1px solid  rgb(88, 145, 138);
        }
        """)
        self.but = QtWidgets.QPushButton(self)
        self.but.setText("Transcibe")
        #self.but.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Fixed)
        self.but.setStyleSheet("""
        QPushButton{
        background-color: rgb(88, 145, 138);
            font: bold 10pt "Roboto";
            height: 32px;
            width: 32px;
            border-radius: 5px;

        }
        QPushButton:hover{
        background-color: rgb(117, 193, 183);
        }
        QPushButton:pressed{
        background-color: rgb(147, 241, 229);
        }
        """)
        self.flayout.addWidget(self.but)
        self.twb = PlainTextWithButton(self)
        self.twb.setGeometry(0,340,770,150)
        self.twb.setMinimumSize(0,150)

        self.flayout.addWidget(self.twb)
        self.setLayout(self.flayout)

class PicButton(QtWidgets.QAbstractButton):
    enterEventSignal = QtCore.pyqtSignal()
    leaveEventSignal = QtCore.pyqtSignal()

    def __init__(self, pixmap, pixmap_hover, pixmap_pressed, buttonHeight, buttonWidth, leftbar, parent=None):
        super(PicButton, self).__init__(parent)
        self.leftbar = leftbar
        self.buttonHeight = buttonHeight
        self.buttonWidth = buttonWidth
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed
        self.pressed.connect(self.update)
        self.released.connect(self.update)

    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QtGui.QPainter(self)
        painter.drawPixmap(event.rect(), pix)

    def enterEvent(self, event):
        # if(self.leftbar):
        #     self.setGeometry(0,0,120,60)
        self.enterEventSignal.emit()
        self.update()
        

    def leaveEvent(self, event):
        self.leaveEventSignal.emit()

        # if(self.leftbar):
        #     self.setGeometry(0,0,60,60)
        self.update()
    

    def sizeHint(self):
        return QtCore.QSize(self.buttonWidth, self.buttonHeight)

class UiWindow(QtWidgets.QMainWindow):
    factor = 1.5
    def __init__(self, parent=None):
        super(UiWindow, self).__init__(parent)
        self.setStyleSheet("""
        QFrame{

            background-color: #121212;

        }
        QLabel{
            color: #fff;
            font:  8pt "Roboto";

        }
        QPlainTextEdit{
            color: #fff;
            background-color: #2f2f2f;
            border: none;
            border-radius: 7px;
        }
        QPlainTextEdit:focus{
            color: #fff;
            background-color: #393939;
            border-top: none;
            border-bottom: 1px solid  rgb(88, 145, 138);
        }
        QPushButton{
        background-color: rgb(88, 145, 138);
            font: bold 10pt "Roboto";
            height: 32px;
            width: 32px;
            border-radius: 5px;

        }
        QPushButton:hover{
        background-color: rgb(117, 193, 183);
        }
        QPushButton:clicked{
        background-color: rgb(147, 241, 229);
        }
        QScrollBar:vertical{
            background-color: #292929;
            
            border: none;
            width: 10px;


        }
        QScrollBar::handle:vertical{

            background-color: #292929;
            min-height: 5px;
            border-radius: 5px;


        }
        QScrollBar::handle:vertical:hover{
            
            background-color:#6b6b6b;
        }
        QScrollBar::handle:vertical:pressed{
            
            
            background-color:#7e7e7e;
        }
        QScrollBar::sub-line:vertical{
            border: none;
            background-color:#292929;
            height: 15px;
            border-top-left-radius: 7px;
            border-top-right-radius: 7px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical:hover{
            background-color: #292929;
        }
        QScrollBar::sub-line:vertical:pressed{
            
            background-color: #292929;
        }
        QScrollBar::add-line:vertical:hover{
            background-color: #292929;
        }
        QScrollBar::add-line:vertical:pressed{
            
            background-color: #292929;
        }
        QScrollBar::add-line:vertical{
            border: none;
            background-color: #292929;
            height: 15px;
            border-top-left-radius: 7px;
            border-top-right-radius: 7px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
            background: none;
            
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{
            background: none;
        }
        """)
        self.setWindowTitle("emek's linguistics tools")
        self.setFixedSize(940,520)
        self.offset = None

        self.initUI()

        c1 = Content(self.contentWorkFrame)
        self.contentWorkFrameInit.hide()
        self.setCentralWidget(self.bgFrame)
        

    def initUI(self):
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint
        )
        self.bgFrame = QtWidgets.QFrame()
        
        self.mainFrame = QtWidgets.QFrame(self.bgFrame)
        
        self.topBarFrame = QtWidgets.QFrame(self.mainFrame)
        self.appFrame = QtWidgets.QFrame(self.mainFrame)

        self.leftMenuFrame = QtWidgets.QFrame(self.appFrame)
        self.contentFrame = QtWidgets.QFrame(self.appFrame)
        self.contentWorkFrame = QtWidgets.QFrame(self.contentFrame)
        self.contentWorkFrameInit = QtWidgets.QFrame(self.contentWorkFrame)
        
        self.mainFrame.setGeometry(0,0,940,520)
        self.topBarFrame.setGeometry(0,0,940,30)
        self.appFrame.setGeometry(0,30,940,490)
        self.leftMenuFrame.setGeometry(0,0,170,490)
        self.contentFrame.setGeometry(170,0,770,490)
        self.contentWorkFrame.setGeometry(0,0,770,490)
        self.contentWorkFrameInit.setGeometry(0,0,770,490)
        self.topBarFrame.setStyleSheet("background-color: #202020;")
        self.topBarFrameEffect = QtWidgets.QGraphicsDropShadowEffect(self.topBarFrame, enabled=True, blurRadius=25,offset=QtCore.QPointF(0.0,5.0))
        self.topBarFrameEffect.setColor(QtGui.QColor("#000000"))
        self.topBarFrame.setGraphicsEffect(self.topBarFrameEffect)
        self.leftMenuFrameEffect = QtWidgets.QGraphicsDropShadowEffect(self.leftMenuFrame, enabled=True, blurRadius=50,offset=QtCore.QPointF(1.0,0.0))
        self.leftMenuFrameEffect.setColor(QtGui.QColor("#000000"))
        self.leftMenuFrame.setGraphicsEffect(self.leftMenuFrameEffect)
        #self.topBarFrame.setStyleSheet("background-color: rgb(52, 60, 81);")

        self.leftMenuFrameLayout = QtWidgets.QVBoxLayout()
        self.navbar = QtWidgets.QTreeWidget()
        self.navbar.setStyleSheet("""
            QScrollBar:vertical{
                background-color:  #292929;
                border: none;
                width: 10px;

            }
            QTreeWidget{
                border: none;
                background-color: #292929;
                color: #ffffff;
                font: 8pt "Roboto";
            }
            QTreeWidget::item{
                background-color: #292929;
                border:none;
                
                border-bottom: 1px solid  #3a3a3a;
                height: 30px;
            }
            QTreeWidget::item:hover{
                background-color: #383838;
                border: none;
            }
            QTreeWidget::item:selected{
                background-color: #484848;
                border: none;
                color: #fff;
            }
            QTreeView::branch:has-children:!has-siblings:closed,
            QTreeView::branch:closed:has-children:has-siblings {
                    border-image: none;
                    image: url(c:/users/emekk/desktop/masa/m/zoom/closeButton.png);
            }

            QTreeView::branch:open:has-children:!has-siblings,
            QTreeView::branch:open:has-children:has-siblings  {
                    border-image: none;
                    image: url(c:/users/emekk/desktop/masa/m/zoom/minimizeButton.png);
            }
        """)
        self.navbar.setHeaderHidden(True)
        self.navbar.setAnimated(True)
        self.navbar.setVerticalScrollBarPolicy(2)
        self.navbar.setFocusPolicy(QtCore.Qt.NoFocus)

        
        
        
        topics = ["Sesbilim","Sözdizim","Biçimbilim"]
        topicIcons = [f"c:/users/emekk/desktop/masa/m/zoom/minimizeButton.png","c:/users/emekk/desktop/masa/m/zoom/closeButton.png","c:/users/emekk/desktop/masa/m/zoom/closeButton.png"]
        subtopics = {
            "Sesbilim": ["Hece Ayırıcı"],
            "Sözdizim": ["Yok"],
            "Biçimbilim": ["Yok2"],


        }
        for c, topic in enumerate(topics):
            topicItem = QtWidgets.QTreeWidgetItem()
            topicItem.setText(0,topic)
            topicItem.setIcon(0,QtGui.QIcon(topicIcons[c]))
            self.navbar.addTopLevelItem(topicItem)
            for subtopic in subtopics[topic]:
                subtopicItem = QtWidgets.QTreeWidgetItem()
                subtopicItem.setText(0,subtopic)
                topicItem.addChild(subtopicItem)

        self.leftMenuFrameLayout.addWidget(self.navbar)
        self.leftMenuFrame.setLayout(self.leftMenuFrameLayout)
        self.leftMenuFrameLayout.setContentsMargins(0,0,0,0)


        self.contentWorkFrameInitLayout = QtWidgets.QHBoxLayout()
        self.welcomeTitle = QtWidgets.QLabel(self.contentWorkFrameInit)
        self.welcomeTitle.setText("Hoş geldiniz!")
        #self.welcomeTitle.setFont(QtGui.QFont('Helvetica', 32))
        self.welcomeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.contentWorkFrameInitLayout.addWidget(self.welcomeTitle)
        self.contentWorkFrameInit.setLayout(self.contentWorkFrameInitLayout)

        #self.leftMenuFrame.setStyleSheet("background-color: rgb(33, 39, 45);")
        self.leftMenuFrame.setStyleSheet("background-color: rgb(45, 49, 53);")

        #self.leftMenuFrame.setStyleSheet("background-color: rgb(45, 53, 71);")
        self.contentFrame.setStyleSheet("background-color: none;")

        self.titleLabel = QtWidgets.QLabel(self.topBarFrame)
        #self.titleLabel.setFont(QtGui.QFont('Helvetica', 8))
        self.titleLabel.setGeometry(50,0,200,30)
        self.titleLabel.setStyleSheet("color: rgb(202, 202, 202);")
        self.titleLabel.setText("<html><head/><body><p><span style=\" font-size:10pt;\">Emek's Linguistics Tools</span></p></body></html>")
        self.titleLabel.setToolTip("bozbulanik v0.01")
        #self.titleLabel.mousePressEvent = self.aboutContent

        self.appIcon = QtWidgets.QLabel(self.topBarFrame)
        self.appIcon.setGeometry(15,0,30,30)
        self.appIcon.setPixmap(QtGui.QPixmap(f"C:/Users/emekk/Desktop/masa/m/zoom/simge.png"))
        self.appIcon.setToolTip("Lingua")

        self.minimizeButton = PicButton(QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/minimizeButton.png"),QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/minimizeHover.png"),QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/minimizeHover.png"),30,30,False,self.topBarFrame)
        self.minimizeButton.setGeometry(880,0,30,30)
        self.closeButton = PicButton(QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/closeButton.png"),QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/closeHover.png"),QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/closeHover.png"),30,30,False,self.topBarFrame)
        self.closeButton.setGeometry(910,0,30,30)

        self.minimizeButton.clicked.connect(self.showMinimized)
        self.closeButton.clicked.connect(self.close)
        
        # self.newButton = PicButton(QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/newfile.png"),QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/newfile_hover.png"),QtGui.QPixmap(f"c:/users/emekk/desktop/masa/m/zoom/newfile_hover.png"),30,30,True,self.leftMenuFrame)
        # self.newButton.setGeometry(0,0,60,60)
        # #self.newButton.clicked.connect(self.newFile)   
        # self.newButton.setToolTip("Create new file")

    def aboutContent(self, event):
        self.aboutMessageBox = QtWidgets.QMessageBox(self)
        self.aboutMessageBox.setIcon(QtWidgets.QMessageBox.Information)
        self.aboutMessageBox.setWindowTitle("About")
        self.aboutMessageBox.setInformativeText("Emek's Linguistics Tools \n Author: Emek Kırarslan \n Version: 0.01")
        self.aboutMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.aboutMessageBoxButton = self.aboutMessageBox.button(QtWidgets.QMessageBox.Ok)
        self.aboutMessageBoxButton.setText("Nice!")
        returnValue = self.aboutMessageBox.exec_()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and event.y() <= 30:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self,event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  

    ui = UiWindow()
    ui.show()
    sys.exit(app.exec_())