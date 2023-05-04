num = int(input("Введіть тризначне число: "))

# Розділюємо число на окремі цифри
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10


# Виводимо кожну цифру в окремому рядку
print(digit1)
print(digit2)
print(digit3)