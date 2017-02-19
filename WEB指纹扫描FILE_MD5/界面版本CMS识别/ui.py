# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Wed Mar 05 20:21:30 2014
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
        Dialog.resize(1047, 567)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1041, 561))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.groupBox = QtGui.QGroupBox(self.tab_1)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 651, 451))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tableView_1 = QtGui.QTableView(self.groupBox)
        self.tableView_1.setGeometry(QtCore.QRect(10, 20, 631, 421))
        self.tableView_1.setObjectName(_fromUtf8("tableView_1"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_2.setGeometry(QtCore.QRect(670, 0, 361, 501))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.messagebox_textEdit = QtGui.QTextEdit(self.groupBox_2)
        self.messagebox_textEdit.setGeometry(QtCore.QRect(10, 20, 341, 471))
        self.messagebox_textEdit.setObjectName(_fromUtf8("messagebox_textEdit"))
        self.pushButton = QtGui.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_3.setGeometry(QtCore.QRect(120, 0, 281, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox.setGeometry(QtCore.QRect(60, 20, 61, 22))
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 50)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(140, 20, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_2.setGeometry(QtCore.QRect(210, 20, 61, 22))
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setProperty("value", 300)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 10, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.progressBar = QtGui.QProgressBar(self.tab_1)
        self.progressBar.setGeometry(QtCore.QRect(10, 510, 651, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_2 = QtGui.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(670, 510, 361, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 10, 121, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab5_textEdit_1 = QtGui.QTextEdit(self.tab_2)
        self.tab5_textEdit_1.setGeometry(QtCore.QRect(0, 0, 1031, 71))
        self.tab5_textEdit_1.setObjectName(_fromUtf8("tab5_textEdit_1"))
        self.webView = QtWebKit.QWebView(self.tab_2)
        self.webView.setGeometry(QtCore.QRect(0, 80, 1031, 421))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "域名列表", None))
        self.groupBox_2.setTitle(_translate("Dialog", "messagebox消息提示", None))
        self.pushButton.setText(_translate("Dialog", "导入URL地址", None))
        self.groupBox_3.setTitle(_translate("Dialog", "参数设置", None))
        self.label_6.setText(_translate("Dialog", "线程数：", None))
        self.label.setText(_translate("Dialog", "识别超时/s：", None))
        self.pushButton_2.setText(_translate("Dialog", "开始CMS识别", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">共:0条URL/扫描完成:0/已识别出来CMS:0</p></body></html>", None))
        self.pushButton_3.setText(_translate("Dialog", "导出扫描结果", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "CMS(KEY关键字--文件MD5)识别", None))
        self.tab5_textEdit_1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            BY:神龙 QQ:29295842 BLOG:<a href=\"http://hi.baidu.com/alalmn\"><span style=\" text-decoration: underline; color:#0000ff;\">http://hi.baidu.com/alalmn</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">希望大家能提供宝贵意见  好让我改进  大家的支持是我开发的动力</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">声明：本软件只是测试网站使用请勿做任何违法行为(如果做了 与本人无关 请遵守所在国的相关法律)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">网络安全技术交流 QQ群:220695354   </p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "软件说明", None))

from PyQt4 import QtWebKit
