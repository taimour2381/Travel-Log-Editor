travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

Add = "yes"
while Add == "yes":
    print("Add destinations to your travel log.")
    add_travel_log = {"country": "A", "visits": 0, "cities": "C"}
    country = input("Add the country that you have visited: ")
    add_travel_log["country"] = country
    visits = input("How many times have you visited this country: ")
    add_travel_log["visits"] = visits
    cities = input("Which cities have you visited: ").split()
    add_travel_log["cities"] = cities
    travel_log.append(add_travel_log)
    print(f"You have visited {country}, {visits} times. You have visited {', '.join(cities)} in {country}.")
    print("The destination have been added to your travel log")
    Add = input("Do you want to add more destinations to your travel log?: ")

print(travel_log)
