def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Choose the conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    try:
        choice = int(input("Enter 1 or 2: "))
        if choice not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
            return

        temperature = float(input("Enter the temperature you want to convert: "))
        
        if choice == 1:
            converted_temp = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp}°F.")
        elif choice == 2:
            converted_temp = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp}°C.")
            
    except ValueError:
        print("Invalid input. Please enter numerical values only.")

# Test the program with different input values
temperature_converter()
