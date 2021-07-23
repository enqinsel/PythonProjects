
total = 0
numbers = []

while True:
    numb = int(input("Enter a number: "))
    if numb == 0:
        numbers.pop()
        print("Game Over!")
        break
    total+=numb
    numbers.append(numb)
    print(numbers , "Totals: " , total)
    print("\nPress '0' to finish")









