from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import psycopg2

class CancelBookingDialog(QDialog):
    def __init__(self, db_connection):
        super().__init__()
        self.db_connection = db_connection
        self.setWindowTitle("Cancel Booking")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.name_label = QLabel("Enter Your Name:")
        self.name_input = QLineEdit()
        self.phone_label = QLabel("Enter Your Phone Number:")
        self.phone_input = QLineEdit()
        
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)

        
        self.cancel_button = QPushButton("Cancel Booking")
        self.cancel_button.clicked.connect(self.cancel_booking)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def cancel_booking(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        if not name or not phone:
            QMessageBox.warning(self, "Input Error", "Please enter both Name and Phone Number!")
            return

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM bookaridetable WHERE name=%s AND phoneno=%s RETURNING *", (name, phone))
            deleted_row = cursor.fetchone()
            self.db_connection.commit()

            if deleted_row:
                QMessageBox.information(self, "Success", "Your booking has been cancelled successfully.")
            else:
                QMessageBox.warning(self, "Not Found", "No booking found with the given details.")

        except psycopg2.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error cancelling booking: {str(e)}")

        finally:
            cursor.close()
            self.close()
