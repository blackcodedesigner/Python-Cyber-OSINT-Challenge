# Day one of Python challenge for OSINT and Cybersecurity
# Today is easy because we are creating a calculator

while True:  # Loop to keep the calculator running

    # Take input for the 1st number
    first_number = float(input("Enter 1st Number: "))

    # Take input for the 2nd number
    second_number = float(input("Enter 2nd Number: "))

    # Take input for the operation
    operations = input("Choose Operator '+', '-', '*', '/' or type 'exit' to stop: ")

    # Check if user wants to exit
    if operations.lower() == 'exit':
        print("🚀 Calculator stopped. See you next time!")
        break  # Exit the loop

    # Summation of numbers/variables
    if operations == '+':
        print(f"The sum of numbers is:", first_number + second_number)

    # Multiplication of numbers/variables
    elif operations == '*':
        print(f"The multiplication of numbers is:", first_number * second_number)

    # Division of numbers/variables
    elif operations == '/':
        print(f"The division of numbers is:", first_number / second_number)

    # Subtraction of numbers/variables
    elif operations == '-':
        print(f"The subtraction of numbers is:", first_number - second_number)

    # If input doesn't match any valid operation
    else:
        print("⚠️ FOLLOW INSTRUCTIONS: Enter a valid operator!")

    # Ask if user wants to continue
    continue_choice = input("\nDo you want to continue? (yes/no): ")
    if continue_choice.lower() != 'yes':
        print("🚀 Calculator closed. See you next time!")
        break  # Exit loop if user says "no"