# Деление яблок поровну и остаток в корзинку
print("Hi, I'm judge Alexander!")
print("I was created so that you and your friends do not quarrel and share food evenly")
food = input("what do you share?")
name = int(input(f"How much do you have {food} ?"))
children = int(input("How many people are you?"))
if name % children == 0:
    print("wow! equally!")
else:
    print(f"Leave for later {name % children} {food}")
print(int(name / children), food, "everyone should get")
