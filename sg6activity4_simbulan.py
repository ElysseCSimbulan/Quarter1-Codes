name = input("Enter your full name (First, Middle, Last): ")

first, middle, last = name.split(",")
first = first.strip().capitalize()
last = last.strip().title()
middle = middle.strip()[0].upper() + "."

formatted = f"{last}, {first} {middle}"

print("Formatted Name: ", formatted)