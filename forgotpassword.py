from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import psycopg2
import random

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
        
        self.resetpushButton.clicked.connect(self.resetpushButtonclicked)

        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_generated_number)
        self.timer.start(30000) 

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
    
    def resetpushButtonclicked(self):
        username = self.resetPasswordUsernAmeLINeEdit.text().strip().lower()
        newpassword = self.newpasswordLinedit.text().strip()
        gnno = self.generatedNumberLinedit.text().strip()
        
        if not username or not newpassword or not gnno:
            QMessageBox.warning(None, "Error", "All Fields Are required!")
        else:
            try:
                connection = psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="3062",
                    database="quickrideCompany"
                )
                cursor = connection.cursor()
                cursor.execute("SELECT username FROM userLogin WHERE username = %s", (username,))
                result = cursor.fetchone()

                if result:
                    changepassquery = "UPDATE userlogin SET password=%s WHERE username=%s"
                    cursor.execute(changepassquery, (newpassword, username))
                    
                    connection.commit()
                    cursor.close()
                    connection.close()
                    QMessageBox.information(None, "Success", "Password Updated Successfully!")
                else:
                    QMessageBox.critical(None, "User Error", "User Doesn't Exist In the database!")
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Error occurred: {e}")

    def update_generated_number(self):
        
        random_number = random.randint(1000, 10000)
        self.label.setText(str(random_number))  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePasswordDialog = QtWidgets.QDialog()
    ui = Ui_ChangePasswordDialog()
    ui.setupUi(ChangePasswordDialog)
    ChangePasswordDialog.show()
    sys.exit(app.exec())
