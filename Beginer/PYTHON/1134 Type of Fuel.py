alcohol = 0
gasoline = 0
diesel = 0

while True:
    n = int(input())
    if 1 <= n <= 3:
        if n == 1:
            alcohol += 1
        elif n == 2:
            gasoline += 1
        elif n == 3:
            diesel += 1
    elif n == 4:
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alcohol}")
print(f"Gasolina: {gasoline}")
print(f"Diesel: {diesel}")
