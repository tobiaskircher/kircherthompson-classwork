print("Enter kilo value:")
kilo = input()
print("Enter pound value:")
pound = input()
kilo_to_pound = int(kilo)* 2.205
kilo_to_pound = round(kilo_to_pound,2)
pound_to_kilo = int(pound) / 2.205
pound_to_kilo = round(pound_to_kilo,2)
print(kilo,"kilos is equivalent to",kilo_to_pound,"pounds.")
print(pound,"pounds is equivalent to",pound_to_kilo,"kilos.")
