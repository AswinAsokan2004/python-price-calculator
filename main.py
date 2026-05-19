def calculate_total(price, quantity, percentageDiscount):
    total = price * quantity + 10
    total *= total * percentageDiscount / 100
    return total

def main():
    price = 100
    quantity = 2
    percentageTax = 10

    total = calculate_total(price, quantity, percentageTax)
    print(f"Total amount12: {total}")


main()
