def celsius_to_fahrenheit(celsius, round_to=1):
    temp = (celsius * 9/5) + 32
    return temp

def fahrenheit_to_celsius(fahrenheit, round_to=1):
    temp = (fahrenheit - 32) * 5/9
    return temp

print("\n   °C  |     °F")
print("-------+----------")
for i in range(0, 101, 20):
    print(f"{i:5} | {celsius_to_fahrenheit(i):6}")

print("98.6 °F = ", fahrenheit_to_celsius(98.6), "°C")

print("37 °C = ")