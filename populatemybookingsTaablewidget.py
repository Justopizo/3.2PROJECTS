import psycopg2
from PyQt6.QtWidgets import QTableWidgetItem

def populate_booking_table(table_widget, connectDB):
    connection=psycopg2.connect(
        host="localhost",
        user="postgres",
        password="3062",
        database="quickrideCompany"
    )
    
    if not connection:
        return

    cursor = connection.cursor()


    cursor.execute("SELECT fromplace, destination, noofseats FROM bookaridetable;")
    ride_rows = cursor.fetchall()

    cursor.execute("SELECT departuretime, busreg FROM bustable;")
    bus_rows = cursor.fetchall()

    pricing = {
        ("Mombasa", "Nairobi"): 2500,
        ("Nairobi", "Kisii"): 1000,
        ("Kisumu", "Nairobi"): 800,
        ("Kakamega", "Nairobi"): 1500,
        ("Lamu", "Nairobi"): 1000,
        ("Bungoma", "Nairobi"): 1000,
        ("Naivasha", "Nairobi"): 1000,
        ("Nakuru", "Nairobi"): 1000
    }

    table_widget.setRowCount(len(ride_rows))

    for row_idx, (fromplace, destination, noofseats) in enumerate(ride_rows):
        price_per_seat = pricing.get((fromplace, destination), 1000)
        total_cost = price_per_seat * noofseats

       
        departuretime, busreg = bus_rows[row_idx % len(bus_rows)] if bus_rows else ("N/A", "N/A")

        table_data = [fromplace, destination, str(noofseats), str(total_cost), departuretime, busreg]

        for col_idx, data in enumerate(table_data):
            table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    cursor.close()
    connection.close()
