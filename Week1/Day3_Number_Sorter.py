# 🔥 Day 3 Python Challenge: Sorting Numbers
# This program takes five numbers from the user and sorts them in ascending or descending order based on user choice.

# 🖥 Taking user input for two numbers
first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: "))
third_number = float(input("Enter Third Number:"))
fourth_number = float(input("Enter Fourth Number:"))
fifth_number = float(input("Enter Fifth Number:"))

# 📌 Storing the numbers in a list for sorting
number_list = [first_number, second_number, third_number, fourth_number, fifth_number]

# 🔄 Asking user for sorting choice
sort_choice = input("Choose sorting order ('A' for Ascending, 'D' for Descending): ").upper()  # Convert input to uppercase for consistency

# 🚀 Sorting based on user's choice
if sort_choice == 'A':
    number_list.sort()  # Ascending order
    print(f"✅ Numbers in Ascending Order: {number_list}")

elif sort_choice == 'D':
    number_list.sort(reverse=True)  # Descending order
    print(f"✅ Numbers in Descending Order: {number_list}")

else:
    print("⚠️ Invalid input! Please choose 'A' for Ascending or 'D' for Descending.")
