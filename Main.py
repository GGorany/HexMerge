import os
import sys
from intelhex import IntelHex
from PyQt5 import QtWidgets, QtGui, QtCore
from UI.UI_Merge import Ui_FormMerge


class MyForm(QtWidgets.QWidget, Ui_FormMerge):
    def __init__(self):
        super().__init__()
        self.form_class = Ui_FormMerge()
        self.setupUi(self)
        self.Btn_BootFileOpen.clicked.connect(self.BootOpenBtnClicked)
        self.Btn_AppFileOpen.clicked.connect(self.AppOpenBtnClicked)
        self.Btn_Merge.clicked.connect(self.MergeBtnClicked)
        self.fBoot = IntelHex()
        self.fApp = IntelHex()
        self.fMerge = IntelHex()
        self.palette_red = QtGui.QPalette()
        self.palette_red.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        self.palette_darkgreen = QtGui.QPalette()
        self.palette_darkgreen.setColor(QtGui.QPalette.Text, QtCore.Qt.darkGreen)

    def BootOpenBtnClicked(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Hex file', "", "Hex Files(*.Hex)")
        if fname[0]:
            try:
                self.fBoot = IntelHex(fname[0])
            except:
                exc = sys.exc_info()[1]  # current exception
                self.lineEdit_BootFileName.setPalette(self.palette_red)
                self.lineEdit_BootFileName.setText(str(exc))
                self.label_Status.setText("<font color=red><b>" + "File Open Failed." + "</b></font>")
                self.fBoot = IntelHex()
                return
            else:
                temp = os.path.split(fname[0])
                self.lineEdit_BootFileName.setPalette(self.palette_darkgreen)
                self.lineEdit_BootFileName.setText(temp[1])
                self.label_Status.setText("Boot Hex Opened.")

    def AppOpenBtnClicked(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Hex file', "", "Hex Files(*.Hex)")
        if fname[0]:
            try:
                self.fApp = IntelHex(fname[0])
            except:
                exc = sys.exc_info()[1]  # current exception
                self.lineEdit_AppFileName.setPalette(self.palette_red)
                self.lineEdit_AppFileName.setText(str(exc))
                self.label_Status.setText("<font color=red><b>" + "File Open Failed." + "</b></font>")
                self.fApp = IntelHex()
                return False
            else:
                temp = os.path.split(fname[0])
                self.lineEdit_AppFileName.setPalette(self.palette_darkgreen)
                self.lineEdit_AppFileName.setText(temp[1])
                self.label_Status.setText("App Hex Opened.")

    def MergeBtnClicked(self):
        self.label_Status.setText("Merging.")
        if (self.fBoot.start_addr is not None) and (self.fApp.start_addr is not None):
            try:
                self.fMerge.merge(self.fBoot, overlap='replace')
                self.fMerge.merge(self.fApp, overlap='replace')
            except:
                self.label_Status.setText("<font color=red><b>" + "File Merge Failed." + "</b></font>")
                return False
            else:
                self.fMerge.tofile("Merge_Result.hex", format='hex')
                self.fMerge = IntelHex()
                self.label_Status.setText("<font color=green><b>" + "Merge Done." + "</b></font>")
        else:
            self.fMerge = IntelHex()
            self.label_Status.setText("<font color=red><b>" + "File is not Opened yet." + "</b></font>")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myForm = MyForm()
    myForm.show()
    app.exec_()
