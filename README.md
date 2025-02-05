# QuickRideCompany Bus Booking Management System

## Overview
QuickRideCompany is a robust **Bus Booking Management System** built using **Python (PyQt6) and PostgreSQL**. It provides an efficient way for travelers to book bus tickets, while offering an admin panel for managing bookings, buses, and payments.

## Features
### 1. **Traveler Dashboard**
- Book a bus ticket by selecting departure and destination cities.
- Choose travel date, number of seats, and bus category (VIP, Regular).
- View booked trips and cancel bookings if needed.
- Save booking confirmation as a **.docx** file.
- Make payments via **MPesa API integration**.

### 2. **Admin Dashboard**
- **Manage Bookings**: View, edit, or cancel bookings.
- **Manage Buses**: Add, update, and remove bus details.
- **Manage Routes & Pricing**: Configure travel routes and set fare prices.
- **View Payments**: Track completed and pending transactions.
- **User Management**: Monitor and manage registered users.
- **Reports & Analytics**: Generate reports for bookings, revenue, and system performance.
- **System Settings**: Update company info, MPesa API keys, and configurations.

## Database Structure
The system uses **PostgreSQL** with the following key tables:

### 1. `bookridetable`
Stores travelers' bookings.
```
Columns: fromplace, destination, traveldate, noofseats, buscategory, name, phone
```

### 2. `bustable`
Holds information about buses.
```
Columns: departuretime, busreg
```

### 3. `payment`
Records payment transactions.
```
Columns: fromplace, destination, seats, payment_method, total_cost
```

## Pricing Structure
The fare price is calculated based on departure and destination:
- **Mombasa → Nairobi**: KES 2500
- **Nairobi → Kisii**: KES 1000
- **Kisumu → Nairobi**: KES 800
- **Kakamega → Nairobi**: KES 1500
- Other cities (Lamu, Bungoma, Naivasha, Nakuru) → Nairobi: **KES 1000**

## MPesa API Integration
- Supports MPesa STK push for seamless payments.
- Uses **consumer key and secret** for authentication.
- Requires **internet access** for transactions.
- Users enter their phone number for payment processing.

## How to Use
### **Traveler Panel**
1. **Sign Up / Log In**.
2. **Book a Ride** – Select route, date, and category.
3. **Pay via MPesa**.
4. **Download Booking Confirmation**.
5. **Cancel Booking (if necessary)**.

### **Admin Panel**
1. **Log In**.
2. **Manage Bookings & Buses**.
3. **View Payment Transactions**.
4. **Analyze Reports & System Data**.

## Developers
- **Justin Omare Ratemo** – Lead Developer ([justopizo01@gmail.com](mailto:justopizo01@gmail.com))
- **Amos Kilonzo** – Senior GUI Developer

## Installation & Setup
### Requirements
- Python 3.x
- PostgreSQL
- PyQt6
- `docx` (for saving booking confirmations)
- Internet connection (for MPesa API)

### Running the Project
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/QuickRideCompany.git
   cd QuickRideCompany
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up the PostgreSQL database**
   - Create the required tables.
4. **Run the Application**
   ```bash
   python main.py
   ```

## License
This project is open-source under the MIT License.

