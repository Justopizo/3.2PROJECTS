


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setObjectName("ChangePasswordDialog")
        ChangePasswordDialog.resize(248, 257)
        self.label = QtWidgets.QLabel(parent=ChangePasswordDialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=ChangePasswordDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 191, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.generatedNumberLinedit = QtWidgets.QLineEdit(parent=ChangePasswordDialog)
        self.generatedNumberLinedit.setGeometry(QtCore.QRect(10, 70, 221, 22))
        self.generatedNumberLinedit.setObjectName("generatedNumberLinedit")
        self.label_3 = QtWidgets.QLabel(parent=ChangePasswordDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 191, 16))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.resetPasswordUsernAmeLINeEdit = QtWidgets.QLineEdit(parent=ChangePasswordDialog)
        self.resetPasswordUsernAmeLINeEdit.setGeometry(QtCore.QRect(10, 120, 211, 22))
        self.resetPasswordUsernAmeLINeEdit.setObjectName("resetPasswordUsernAmeLINeEdit")
        self.label_4 = QtWidgets.QLabel(parent=ChangePasswordDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 191, 16))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.newpasswordLinedit = QtWidgets.QLineEdit(parent=ChangePasswordDialog)
        self.newpasswordLinedit.setGeometry(QtCore.QRect(10, 170, 211, 22))
        self.newpasswordLinedit.setObjectName("newpasswordLinedit")
        self.resetpushButton = QtWidgets.QPushButton(parent=ChangePasswordDialog)
        self.resetpushButton.setGeometry(QtCore.QRect(10, 210, 93, 28))
        self.resetpushButton.setObjectName("resetpushButton")

        self.retranslateUi(ChangePasswordDialog)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordDialog)

    def retranslateUi(self, ChangePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordDialog.setWindowTitle(_translate("ChangePasswordDialog", "Forgot Password"))
        self.label.setText(_translate("ChangePasswordDialog", "0000"))
        self.label_2.setText(_translate("ChangePasswordDialog", "Enter The Number Above"))
        self.label_3.setText(_translate("ChangePasswordDialog", "Your Username"))
        self.label_4.setText(_translate("ChangePasswordDialog", "New Password"))
        self.resetpushButton.setText(_translate("ChangePasswordDialog", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePasswordDialog = QtWidgets.QDialog()
    ui = Ui_ChangePasswordDialog()
    ui.setupUi(ChangePasswordDialog)
    ChangePasswordDialog.show()
    sys.exit(app.exec())
