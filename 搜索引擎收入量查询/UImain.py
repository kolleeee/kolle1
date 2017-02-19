# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created: Sun Dec 08 20:07:32 2013
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
        Dialog.resize(854, 472)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 50, 851, 391))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 442, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 851, 41))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(695, 20, 131, 16))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_1 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_1.setGeometry(QtCore.QRect(35, 20, 131, 16))
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(365, 20, 119, 16))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(200, 20, 155, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(530, 20, 125, 16))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 439, 741, 31))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "查询/从新查询", None))
        self.groupBox.setTitle(_translate("Dialog", "选择需要那些搜索引擎", None))
        self.checkBox_5.setText(_translate("Dialog", "搜狗|www.sogou.com", None))
        self.checkBox_1.setText(_translate("Dialog", "百度|www.baidu.com", None))
        self.checkBox_3.setText(_translate("Dialog", "微软|cn.bing.com", None))
        self.checkBox_2.setText(_translate("Dialog", "谷歌|www.google.com.hk", None))
        self.checkBox_4.setText(_translate("Dialog", "360搜索|so.360.cn", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">查询内容总数:0--百度收入:0--谷歌收入:0--微软收入:0--360搜索收入:0--搜狗收入:0</span></p></body></html>", None))

