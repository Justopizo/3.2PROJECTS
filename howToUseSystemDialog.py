from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class HowToUseDialog(QDialog):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("How to Use the System")
        self.resize(500, 400)  # Adjust dialog size
        self.setMinimumSize(600, 400) 
        

        layout = QVBoxLayout()

        instructions = """
        Welcome to the QuickRide Bus Booking System!

        1. **Login to the System:**
           - Use your credentials to login.

        2. **View Available Buses:**
           - Once logged in, you will see a list of available buses for booking.

        3. **Make a Booking:**
           - Select the source and destination of your travel, choose the number of seats, and book your ride.
           - Confirm the details and proceed to payment.

        4. **Cancel a Booking:**
           - To cancel a booking, click the 'Cancel Booking' button and follow the instructions.
        
        5. **Check Your Bookings:**
           - View your current bookings and upcoming travel details in the dashboard.

        6. **Other Functions:**
           - You can check bus departure times and bus registration numbers from the dashboard.

        Enjoy your ride with QuickRide Company!
        """
        
        label = QLabel(instructions)
        layout.addWidget(label)

        
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

        
        self.setLayout(layout)
