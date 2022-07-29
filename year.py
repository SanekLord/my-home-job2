# высокосный ли год
print("Let's find out if it's a leap year")
year = int(input("Enter year"))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"Yes {year} it really is a leap year.")
    print("Did you know that some people are afraid")
    print("of the leap year, considering it to be mystically bad?")
else:
    print(f"no, it's not a leap {year} year.")

    