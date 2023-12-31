# Form implementation generated from reading ui file 'src/ui/ui_main.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NoteManager(object):
    def setupUi(self, NoteManager):
        NoteManager.setObjectName("NoteManager")
        NoteManager.resize(928, 659)
        NoteManager.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.179, y1:0.227273, x2:1, y2:1, stop:0.149254 rgba(139, 175, 255, 255), stop:0.59204 rgba(163, 125, 215, 255));\n"
"font: 8pt \"Constantia\";")
        self.centralwidget = QtWidgets.QWidget(parent=NoteManager)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: transparent;")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.lineEdit_title = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_title.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"")
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout.addWidget(self.lineEdit_title)
        self.label_content = QtWidgets.QLabel(parent=self.frame)
        self.label_content.setEnabled(True)
        self.label_content.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_content.setObjectName("label_content")
        self.verticalLayout.addWidget(self.label_content)
        self.textEdit_content = QtWidgets.QTextEdit(parent=self.frame)
        self.textEdit_content.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"")
        self.textEdit_content.setObjectName("textEdit_content")
        self.verticalLayout.addWidget(self.textEdit_content)
        self.pushButton_addNote = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_addNote.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.pushButton_addNote.setObjectName("pushButton_addNote")
        self.verticalLayout.addWidget(self.pushButton_addNote)
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)
        self.frame1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame1.setStyleSheet("background-color: transparent;\n"
"")
        self.frame1.setObjectName("frame1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_noteLists = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_noteLists.setFont(font)
        self.label_noteLists.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_noteLists.setObjectName("label_noteLists")
        self.verticalLayout_2.addWidget(self.label_noteLists)
        self.listWidget_noteLists = QtWidgets.QListWidget(parent=self.frame1)
        self.listWidget_noteLists.setStyleSheet("background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.listWidget_noteLists.setObjectName("listWidget_noteLists")
        self.verticalLayout_2.addWidget(self.listWidget_noteLists)
        self.pushButton_deleteNote = QtWidgets.QPushButton(parent=self.frame1)
        self.pushButton_deleteNote.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.pushButton_deleteNote.setObjectName("pushButton_deleteNote")
        self.verticalLayout_2.addWidget(self.pushButton_deleteNote)
        self.gridLayout.addWidget(self.frame1, 0, 1, 2, 1)
        self.frame2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame2.setStyleSheet("background-color: transparent;\n"
"")
        self.frame2.setObjectName("frame2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_search = QtWidgets.QLineEdit(parent=self.frame2)
        self.lineEdit_search.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.verticalLayout_3.addWidget(self.lineEdit_search)
        self.pushButton_searchTitle = QtWidgets.QPushButton(parent=self.frame2)
        self.pushButton_searchTitle.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_searchTitle.setFont(font)
        self.pushButton_searchTitle.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/edit_white_24dp.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_searchTitle.setIcon(icon)
        self.pushButton_searchTitle.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_searchTitle.setObjectName("pushButton_searchTitle")
        self.verticalLayout_3.addWidget(self.pushButton_searchTitle)
        self.pushButton_searchContent = QtWidgets.QPushButton(parent=self.frame2)
        self.pushButton_searchContent.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_searchContent.setFont(font)
        self.pushButton_searchContent.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.pushButton_searchContent.setIcon(icon)
        self.pushButton_searchContent.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_searchContent.setObjectName("pushButton_searchContent")
        self.verticalLayout_3.addWidget(self.pushButton_searchContent)
        self.pushButton_all_note = QtWidgets.QPushButton(parent=self.frame2)
        self.pushButton_all_note.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.pushButton_all_note.setObjectName("pushButton_all_note")
        self.verticalLayout_3.addWidget(self.pushButton_all_note)
        self.gridLayout.addWidget(self.frame2, 0, 2, 1, 1)
        self.label_note = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_note.setStyleSheet("color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_note.setText("")
        self.label_note.setObjectName("label_note")
        self.gridLayout.addWidget(self.label_note, 1, 2, 1, 1)
        NoteManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(NoteManager)
        QtCore.QMetaObject.connectSlotsByName(NoteManager)

    def retranslateUi(self, NoteManager):
        _translate = QtCore.QCoreApplication.translate
        NoteManager.setWindowTitle(_translate("NoteManager", "Note Manager"))
        self.label_title.setText(_translate("NoteManager", "Title:"))
        self.label_content.setText(_translate("NoteManager", "Content:"))
        self.pushButton_addNote.setText(_translate("NoteManager", "Add Note"))
        self.label_noteLists.setText(_translate("NoteManager", "Notes list"))
        self.pushButton_deleteNote.setText(_translate("NoteManager", "Delete Note"))
        self.pushButton_searchTitle.setText(_translate("NoteManager", "Search by Title"))
        self.pushButton_searchContent.setText(_translate("NoteManager", "Search by Content"))
        self.pushButton_all_note.setText(_translate("NoteManager", "All Notes"))
