# Membership Functions

def low(temp):
    if temp <= 20:
        return 1
    elif 20 < temp < 30:
        return (30 - temp) / 10
    else:
        return 0


def medium(temp):
    if 20 < temp < 30:
        return (temp - 20) / 10
    elif 30 <= temp < 40:
        return (40 - temp) / 10
    else:
        return 0


def high(temp):
    if temp <= 30:
        return 0
    elif 30 < temp < 40:
        return (temp - 30) / 10
    else:
        return 1


temperature = float(input("Enter Temperature: "))

low_value = low(temperature)
medium_value = medium(temperature)
high_value = high(temperature)

print("Membership Values")
print("Low =", round(low_value, 2))
print("Medium =", round(medium_value, 2))
print("High =", round(high_value, 2))

if high_value >= max(low_value, medium_value):
    print("Fan Speed: HIGH")
elif medium_value >= low_value:
    print("Fan Speed: MEDIUM")
else:
    print("Fan Speed: LOW")