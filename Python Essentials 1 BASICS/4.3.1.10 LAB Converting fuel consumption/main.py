def liters_100km_to_miles_gallon(liters):
    galon = 3.785411784 # L
    mile = 1609.344 # m
    liters_to_galon = liters / galon
    km_to_miles = 100_000 / mile
    return km_to_miles / liters_to_galon

def miles_gallon_to_liters_100km(miles):
    galon = 3.785411784 # L
    mile = 1609.344 # m
    galon_to_liters = galon
    miles_to_100km = miles * mile / 100_000
    return galon_to_liters / miles_to_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
