FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):

    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get temperature input from the user
        temp_input = input("Enter the temperature to convert: ")

        # Validate if the input is a numeric value
        temp_value = float(temp_input)
        
        # Get the unit of temperature (C for Celsius, F for Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            # Convert from Celsius to Fahrenheit
            result = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {result}°F")
        elif unit == "F":
            # Convert from Fahrenheit to Celsius
            result = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {result}°C")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
