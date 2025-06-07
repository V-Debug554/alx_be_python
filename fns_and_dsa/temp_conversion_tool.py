#Script to convert temperature from degrees fahrenheit to celsius and vice versa
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#Function to convert degrees fahrenheit to degrees celsius
def convert_to_celsius(temperature):
    global celsius
    celsius = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

#Function to convert degrees celcius to fahrenheit
def convert_to_fahrenheit(temperature):
    global fahrenheit
    fahrenheit = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

try:
    temperature_input = float(input("Enter the temperature to convert: "))
    temperature_measurement = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
    if temperature_measurement == 'C':
        convert_to_fahrenheit(temperature_input)
        print(f"{temperature_input}°C is {fahrenheit}")
    elif temperature_measurement == 'F':
        convert_to_celsius(fahrenheit)
        print(f"{temperature_input}°F is {celsius}")
    else:
        print("Invalid temperature measurement selection")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
