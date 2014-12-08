from Items import Item, Invoice

def main():
    print("Let's create an invoice!")

    invoice = Invoice()

    item_name = input("What is the name of the first item?")
    while(len(item_name) > 0):
        item_count = int(input("How many were purchase?"))
        item_price = float(input("What was the cost per item?"))

        item = Item(item_name, item_count, item_price)

        invoice.add_item(item)

        item_name = input("What is the name of the next item? (Leave Blank to exit.)")

    for item in invoice.item_list:
        print("%-30s %10.2f %12d" % (item.name, item.cost, item.quantity, item.total_price))

main()
