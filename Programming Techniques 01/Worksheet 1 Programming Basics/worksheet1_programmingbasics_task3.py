car_mileage_old = int(input("Car mileage last time car was filled:"))
car_mileage_new = int(input("Car mileage now:"))
litres = int(input("Litres taken to fill tank:"))

one_gallon_in_litres = 4.596

gallons = litres / one_gallon_in_litres
distance = car_mileage_new - car_mileage_old
miles_per_gallon = distance / gallons
miles_per_gallon = round(miles_per_gallon,3)
print(miles_per_gallon, "miles per gallon.")

