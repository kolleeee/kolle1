# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dz_bbs.ui'
#
# Created: Tue Dec 31 02:42:28 2013
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
        Dialog.resize(644, 542)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(570, 10, 71, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(70, 10, 321, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 50, 231, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(340, 50, 221, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 60, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 10, 51, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit_4 = QtGui.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(460, 10, 101, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 41, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 41, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textEdit_5 = QtGui.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(70, 90, 321, 41))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(70, 140, 321, 41))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 90, 71, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 140, 71, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textEdit_7 = QtGui.QTextEdit(Dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(520, 120, 41, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(490, 120, 31, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 190, 191, 181))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 31, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 31, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(20, 110, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 140, 54, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.textEdit_8 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_8.setGeometry(QtCore.QRect(60, 20, 121, 31))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.textEdit_9 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_9.setGeometry(QtCore.QRect(60, 60, 121, 31))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.textEdit_10 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_10.setGeometry(QtCore.QRect(60, 100, 121, 31))
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.textEdit_11 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_11.setGeometry(QtCore.QRect(73, 140, 41, 31))
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 190, 181, 141))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 70, 54, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 100, 54, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.textEdit_12 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_12.setGeometry(QtCore.QRect(50, 20, 121, 31))
        self.textEdit_12.setObjectName(_fromUtf8("textEdit_12"))
        self.textEdit_13 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_13.setGeometry(QtCore.QRect(50, 60, 121, 31))
        self.textEdit_13.setObjectName(_fromUtf8("textEdit_13"))
        self.textEdit_14 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_14.setGeometry(QtCore.QRect(73, 100, 41, 31))
        self.textEdit_14.setObjectName(_fromUtf8("textEdit_14"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(400, 180, 231, 151))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.messagebox = QtGui.QTextEdit(Dialog)
        self.messagebox.setGeometry(QtCore.QRect(10, 380, 621, 151))
        self.messagebox.setObjectName(_fromUtf8("messagebox"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(400, 110, 54, 12))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(400, 160, 54, 12))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.textEdit_15 = QtGui.QTextEdit(Dialog)
        self.textEdit_15.setGeometry(QtCore.QRect(440, 100, 41, 31))
        self.textEdit_15.setObjectName(_fromUtf8("textEdit_15"))
        self.textEdit_16 = QtGui.QTextEdit(Dialog)
        self.textEdit_16.setGeometry(QtCore.QRect(440, 150, 41, 31))
        self.textEdit_16.setObjectName(_fromUtf8("textEdit_16"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "登陆网站", None))
        self.label.setText(_translate("Dialog", "登陆网址：", None))
        self.label_2.setText(_translate("Dialog", "用户名：", None))
        self.label_3.setText(_translate("Dialog", "密码：", None))
        self.label_4.setText(_translate("Dialog", "登陆成功\n"
"关键字：", None))
        self.label_5.setText(_translate("Dialog", "批量发\n"
"布评论：", None))
        self.label_6.setText(_translate("Dialog", "批量发\n"
"布帖子：", None))
        self.pushButton_2.setText(_translate("Dialog", "发布帖子", None))
        self.pushButton_3.setText(_translate("Dialog", "发布评论", None))
        self.label_7.setText(_translate("Dialog", "延时\n"
"秒/S：", None))
        self.groupBox.setTitle(_translate("Dialog", "帖子/随机抽取/一行一条", None))
        self.label_8.setText(_translate("Dialog", "标题：", None))
        self.label_9.setText(_translate("Dialog", "内容：", None))
        self.label_11.setText(_translate("Dialog", "链接：", None))
        self.label_12.setText(_translate("Dialog", "内容插入\n"
"链接条数：", None))
        self.groupBox_2.setTitle(_translate("Dialog", "评论/随机抽取/一行一条", None))
        self.label_13.setText(_translate("Dialog", "评论：", None))
        self.label_14.setText(_translate("Dialog", "链接：", None))
        self.label_15.setText(_translate("Dialog", "评论插入\n"
"链接条数：", None))
        self.label_10.setText(_translate("Dialog", "软件说明：  V0.1\n"
"本软件主要针对discuzX BBS  而写\n"
"因为  初次写群发\n"
"以下功能还无法实现群发(后面会改进)\n"
"带验证码登陆----无法实现登陆\n"
"发帖带验证----无法实现\n"
"留言带验证----无法实现\n"
"(大家的支持是我开发的动力)", None))
        self.label_16.setText(_translate("Dialog", "数量：", None))
        self.label_17.setText(_translate("Dialog", "数量：", None))

