# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sat Feb 14 21:37:06 2015
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1446, 810)
        self.pushButton1 = QtGui.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(10, 750, 81, 51))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.SQLite_tableView = QtGui.QTableView(Dialog)
        self.SQLite_tableView.setGeometry(QtCore.QRect(10, 10, 901, 721))
        self.SQLite_tableView.setObjectName(_fromUtf8("SQLite_tableView"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(100, 740, 311, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.SQL_Button_1 = QtGui.QPushButton(self.groupBox)
        self.SQL_Button_1.setGeometry(QtCore.QRect(10, 20, 93, 31))
        self.SQL_Button_1.setObjectName(_fromUtf8("SQL_Button_1"))
        self.SQL_Button_2 = QtGui.QPushButton(self.groupBox)
        self.SQL_Button_2.setGeometry(QtCore.QRect(110, 20, 93, 31))
        self.SQL_Button_2.setObjectName(_fromUtf8("SQL_Button_2"))
        self.SQL_Button_3 = QtGui.QPushButton(self.groupBox)
        self.SQL_Button_3.setGeometry(QtCore.QRect(210, 20, 93, 31))
        self.SQL_Button_3.setObjectName(_fromUtf8("SQL_Button_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 740, 331, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.re_textEdit = QtGui.QTextEdit(self.groupBox_2)
        self.re_textEdit.setGeometry(QtCore.QRect(60, 20, 181, 31))
        self.re_textEdit.setObjectName(_fromUtf8("re_textEdit"))
        self.RE_Button = QtGui.QPushButton(self.groupBox_2)
        self.RE_Button.setGeometry(QtCore.QRect(250, 20, 71, 31))
        self.RE_Button.setObjectName(_fromUtf8("RE_Button"))
        self.pushButton2 = QtGui.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(760, 750, 71, 51))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButton3 = QtGui.QPushButton(Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(840, 750, 71, 51))
        self.pushButton3.setObjectName(_fromUtf8("pushButton3"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(920, 10, 511, 771))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 41, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 173, 41, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(170, 220, 101, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(50, 20, 451, 131))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 153, 451, 61))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox.setGeometry(QtCore.QRect(270, 221, 121, 31))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 223, 141, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(410, 220, 93, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit_3 = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 260, 491, 501))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(1030, 780, 331, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "链接整理器v1.0 (灰帽SEO) 落雪技术支持   BLOG:http://2602159946.lofter.com/", None))
        self.pushButton1.setText(_translate("Dialog", "导入链接", None))
        self.groupBox.setTitle(_translate("Dialog", "数据库", None))
        self.SQL_Button_1.setText(_translate("Dialog", "全部显示", None))
        self.SQL_Button_2.setText(_translate("Dialog", "显示状态OK", None))
        self.SQL_Button_3.setText(_translate("Dialog", "显示状态NO", None))
        self.groupBox_2.setTitle(_translate("Dialog", "检测链接", None))
        self.label.setText(_translate("Dialog", "正则：", None))
        self.RE_Button.setText(_translate("Dialog", "查询", None))
        self.pushButton2.setText(_translate("Dialog", "导出数据", None))
        self.pushButton3.setText(_translate("Dialog", "删除数据", None))
        self.groupBox_3.setTitle(_translate("Dialog", "链接组合", None))
        self.label_2.setText(_translate("Dialog", "链接\n"
"顶部：", None))
        self.label_3.setText(_translate("Dialog", "链接\n"
"底部：", None))
        self.label_4.setText(_translate("Dialog", "内容部分随机\n"
"抽取多少条：", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "下面为生成内容：", None))
        self.pushButton.setText(_translate("Dialog", "生成内容", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><a href=\"http://2602159946.lofter.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">落雪技术支持 QQ:2602159946</span></a></p></body></html>", None))

