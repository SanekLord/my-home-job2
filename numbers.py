# Наименьшее из чисел
print("Enter three numbers and I'll tell you which one is the smallest")
numa = int(input("Enter the first number"))
numb = int(input("Enter the second number"))
numc = int(input("Enter the third number"))
if numb >= numa <= numc:
    print(f"The smallest number will be: {numa}")
elif numa >= numb <= numc:
    print(f"The smallest number will be: {numb}")
else:
    print(f"The smallest number will be: {numc}")


