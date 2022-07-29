# Сколько минут прошло от начала дня и который тогда сейчас час и минут
clock = int(input("Enter how many minutes have passed and I'll tell you what time it is"))
hours = clock % (60 * 24) // 60
minute = clock % 60
if hours <= 6:
    print(f"Good night! {hours} hours {minute} minutes ")
elif hours <= 12:
    print(f"Good morning! {hours} hours {minute} minutes")
elif hours <= 17:
    print(f"Good afternoon! {hours} hours {minute} minutes")
elif hours <= 23:
    print(f"Good evening! {hours} hours {minute} minutes")
