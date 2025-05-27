# 🔥 Day 4 Python Challenge: Even & Odd Number Extractor

# 📌 Taking user input for range
starting_point = int(input("Enter Start Number: "))
end_point = int(input("Enter End Number: "))

# 🚀 Loop through the range of numbers
for number in range(starting_point, end_point + 1):  # Include the end number

    if number % 2 == 0:  # ✅ Even numbers
        print(f"✅ Even Number:", number)

    elif number % 2 != 0:  # ✅ Odd numbers
        print(f"🔥 Odd Number:", number)

    else:  # 🔄 Handles unexpected cases
        print("⚠️ FOLLOW INSTRUCTIONS")
