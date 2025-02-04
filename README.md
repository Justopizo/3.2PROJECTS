

# QuickRideCompany Bus Booking Management System

This is a Python-based Bus Booking Management System for the QuickRideCompany, using **PostgreSQL** as the backend database. The system allows users to book tickets, view available buses, and manage reservations seamlessly through a graphical user interface (GUI) built using **PyQt6**.

## Features
- **Traveler Dashboard**: Displays available buses, allows the traveler to view booking details, and manage reservations.
- **Booking Management**: Enables users to make bookings, modify them, or cancel reservations.
- **Login System**: A secure login interface to manage user authentication.
- **Save and Export Booking Information**: Allows the user to save booking details as a `.docx` file.
- **Progress Indicator**: Displays a loading animation while the booking details are being processed.
- **User Management**: Admin can manage users and their associated bookings.

## Technology Stack
- **Backend**: PostgreSQL
- **GUI**: PyQt6
- **Document Generation**: Python-docx
- **File Dialogs**: QFileDialog from PyQt6
- **Loading Animations**: QProgressDialog

## Database Structure
The system uses a PostgreSQL database with tables such as:
- **userlogin**: Contains columns for `username` and `password` for user authentication.
- **bookings**: Stores booking details such as passenger information, travel date, and bus assigned.

## Setup Instructions

1. **Install PostgreSQL**: Ensure you have PostgreSQL installed and running on your local machine or a remote server.
2. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/quickridecompany-bus-booking-system.git
   ```
3. **Set up the database**:
   - Create a new database and tables based on the SQL schema provided in the project.
   - Configure database connection settings in the Python code where necessary.
4. **Install required libraries**:  
   Create and activate a virtual environment, then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the application**:
   - Start the GUI application:
   ```bash
   python travellerDashboard.py
   ```

## Features in Progress
- Adding more detailed user roles and permissions.
- Enhanced reporting and analytics for bookings.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Y# 3.2PROJECTS
