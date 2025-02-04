def calculate_total_fare(fromplace, destination, seats):
    pricing = {
        ("mombasa", "nairobi"): 2500,
        ("nairobi", "kisii"): 1000,
        ("kisumu", "nairobi"): 800,
        ("kakamega", "nairobi"): 1500,
        ("lamu", "nairobi"): 1000,
        ("bungoma", "nairobi"): 1000,
        ("naivasha", "nairobi"): 1000,
        ("nakuru", "nairobi"): 1000
    }

    

    price_per_seat = pricing.get((fromplace, destination), 1000)  
    total_cost = price_per_seat * seats
    return total_cost





