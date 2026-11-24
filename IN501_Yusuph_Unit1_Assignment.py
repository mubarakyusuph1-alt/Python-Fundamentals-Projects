# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    print("Enter three temperatures in Fahrenheit:")

    # Accept user input
    try:
        temp1 = float(input("Temperature 1 (°F): "))
        temp2 = float(input("Temperature 2 (°F): "))
        temp3 = float(input("Temperature 3 (°F): "))
    except ValueError:
        print("Please enter valid numerical values!")
        return

    # Convert to Celsius
    celsius1 = round(fahrenheit_to_celsius(temp1), 1)
    celsius2 = round(fahrenheit_to_celsius(temp2), 1)
    celsius3 = round(fahrenheit_to_celsius(temp3), 1)

    # Calculate averages
    avg_fahrenheit = round((temp1 + temp2 + temp3) / 3, 1)
    avg_celsius = round((celsius1 + celsius2 + celsius3) / 3, 1)

    # Display results
    print("\nFahrenheit | Celsius")
    print(f"{temp1:<11} | {celsius1}")
    print(f"{temp2:<11} | {celsius2}")
    print(f"{temp3:<11} | {celsius3}")
    print("_" * 20)
    print(f"{avg_fahrenheit:<11} | {avg_celsius}  Average")

# Run the program
if __name__ == "__main__":
    main()
