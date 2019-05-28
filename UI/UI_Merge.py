# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Merge.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormMerge(object):
    def setupUi(self, FormMerge):
        FormMerge.setObjectName("FormMerge")
        FormMerge.resize(500, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormMerge.sizePolicy().hasHeightForWidth())
        FormMerge.setSizePolicy(sizePolicy)
        FormMerge.setMinimumSize(QtCore.QSize(500, 110))
        FormMerge.setMaximumSize(QtCore.QSize(500, 110))
        self.Btn_AppFileOpen = QtWidgets.QPushButton(FormMerge)
        self.Btn_AppFileOpen.setGeometry(QtCore.QRect(380, 40, 111, 23))
        self.Btn_AppFileOpen.setObjectName("Btn_AppFileOpen")
        self.lineEdit_BootFileName = QtWidgets.QLineEdit(FormMerge)
        self.lineEdit_BootFileName.setEnabled(True)
        self.lineEdit_BootFileName.setGeometry(QtCore.QRect(10, 10, 361, 20))
        self.lineEdit_BootFileName.setDragEnabled(False)
        self.lineEdit_BootFileName.setReadOnly(True)
        self.lineEdit_BootFileName.setObjectName("lineEdit_BootFileName")
        self.Btn_Merge = QtWidgets.QPushButton(FormMerge)
        self.Btn_Merge.setGeometry(QtCore.QRect(380, 80, 111, 23))
        self.Btn_Merge.setObjectName("Btn_Merge")
        self.Btn_BootFileOpen = QtWidgets.QPushButton(FormMerge)
        self.Btn_BootFileOpen.setGeometry(QtCore.QRect(380, 10, 111, 23))
        self.Btn_BootFileOpen.setObjectName("Btn_BootFileOpen")
        self.label_Status = QtWidgets.QLabel(FormMerge)
        self.label_Status.setGeometry(QtCore.QRect(13, 69, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Status.setFont(font)
        self.label_Status.setObjectName("label_Status")
        self.lineEdit_AppFileName = QtWidgets.QLineEdit(FormMerge)
        self.lineEdit_AppFileName.setEnabled(True)
        self.lineEdit_AppFileName.setGeometry(QtCore.QRect(10, 40, 361, 20))
        self.lineEdit_AppFileName.setReadOnly(True)
        self.lineEdit_AppFileName.setObjectName("lineEdit_AppFileName")

        self.retranslateUi(FormMerge)
        QtCore.QMetaObject.connectSlotsByName(FormMerge)

    def retranslateUi(self, FormMerge):
        _translate = QtCore.QCoreApplication.translate
        FormMerge.setWindowTitle(_translate("FormMerge", "Merge Intel Hex File"))
        self.Btn_AppFileOpen.setText(_translate("FormMerge", "Open App File"))
        self.lineEdit_BootFileName.setText(_translate("FormMerge", "Open Bootloader Hex File"))
        self.Btn_Merge.setText(_translate("FormMerge", "Merge"))
        self.Btn_BootFileOpen.setText(_translate("FormMerge", "Open Boot File"))
        self.label_Status.setText(_translate("FormMerge", "Prepare Merging"))
        self.lineEdit_AppFileName.setText(_translate("FormMerge", "Open Application Hex File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormMerge = QtWidgets.QWidget()
    ui = Ui_FormMerge()
    ui.setupUi(FormMerge)
    FormMerge.show()
    sys.exit(app.exec_())

