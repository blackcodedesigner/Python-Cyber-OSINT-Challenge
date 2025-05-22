# 🔥 Day 2 Python Challenge: Temperature Converter
# This script converts Celsius to Fahrenheit in a continuous loop until the user decides to exit.

while True:  # Loop to keep running unless user chooses to stop

    # 📌 Taking user input for the temperature in Celsius
    first_input = float(input("Enter the number to be converted (Celsius): "))

    # 🔄 Formula for conversion: Fahrenheit = (Celsius * 9/5) + 32
    converting = (first_input * 9 / 5) + 32

    # 🖥 Displaying the converted temperature
    print(f"The output in Fahrenheit is:", converting)

    # 🔄 Asking user if they want to continue or exit
    loop = input("Do you want to continue? (yes/no): ")

    # 🚀 If user enters 'no', the program will exit
    if loop.lower() != "yes":  # Ensures case insensitivity
        print("🚀 Closing the converter. See you next time!")
        break  # Exit the loop
