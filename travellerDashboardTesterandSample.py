from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QHBoxLayout
from PyQt6.QtGui import QIcon
import sys

class TravelerDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traveler Dashboard - QuickRideCompany")
        self.setGeometry(100, 100, 800, 500)
        
        # Main layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # Sidebar
        self.sidebar = QVBoxLayout()
        self.sidebar.setContentsMargins(10, 10, 10, 10)
        self.sidebar.setSpacing(10)
        
        self.buttons = {
            "Home": QPushButton("Home"),
            "Book a Ride": QPushButton("Book a Ride"),
            "My Bookings": QPushButton("My Bookings"),
            "Payments": QPushButton("Payments"),
            "Profile": QPushButton("Profile"),
            "Notifications": QPushButton("Notifications"),
            "Help & Support": QPushButton("Help & Support"),
            "Logout": QPushButton("Logout")
        }
        
        for btn in self.buttons.values():
            btn.setStyleSheet("padding: 10px; font-size: 14px;")
            self.sidebar.addWidget(btn)
        
        # Content area
        self.stack = QStackedWidget()
        
        self.pages = {
            "Home": QLabel("Welcome to QuickRideCompany!"),
            "Book a Ride": QLabel("Search and Book a Ride."),
            "My Bookings": QLabel("View and Manage Bookings."),
            "Payments": QLabel("View Payment History."),
            "Profile": QLabel("Edit Your Profile."),
            "Notifications": QLabel("Check Notifications."),
            "Help & Support": QLabel("Contact Support and FAQs."),
            "Logout": QLabel("Logging out...")
        }
        
        for page in self.pages.values():
            page.setStyleSheet("font-size: 16px; padding: 20px;")
            container = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(page)
            container.setLayout(layout)
            self.stack.addWidget(container)
        
        # Connect buttons to stack widget
        for i, (name, btn) in enumerate(self.buttons.items()):
            btn.clicked.connect(lambda _, idx=i: self.stack.setCurrentIndex(idx))
        
        # Add sidebar and content to main layout
        sidebar_widget = QWidget()
        sidebar_widget.setLayout(self.sidebar)
        sidebar_widget.setFixedWidth(200)
        sidebar_widget.setStyleSheet("background-color: #2c3e50; color: white;")
        
        main_layout.addWidget(sidebar_widget)
        main_layout.addWidget(self.stack)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TravelerDashboard()
    window.show()
    sys.exit(app.exec())
