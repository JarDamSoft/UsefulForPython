# A company has determined that its annual profit is typically 23 percent of total sales.
# Write a program that asks the user to enter the projected amount of total sales,
# and then displays the profit that will be made from that amount. Hint: Use the value 0.23 to represent 23 percent.


def calculate():
    totalSale = float(input('Give total sales amount: '))
    profit = totalSale * 0.23

    print('Profit of total sales is: ${:.3f}' .format(profit))


def calculate2():
    totalSale = float(input('Give total sales amount: '))
    profit = totalSale * 0.23

    print(f'Profit of total sales is: ${profit:,.2f}')


calculate()
calculate2()
