class Item:

    last_sku_used = 0

    def __init__(self, name, price, taxable):

        self.sku = Item.last_sku_used + 1
        self.name = name
        self.price = price
        self.taxable = taxable
        Item.last_sku_used = self.sku

    def get_item_base_price(self):
        return self.price

    def get_item_tax_price_GST(self):
        return self.price * 0.05

    def get_item_tax_price_PST(self):
        return self.price * 0.09975

    def get_item_total(self):
        return self.get_item_tax_price_GST() + self.get_item_tax_price_PST() + self.get_item_base_price()

    def print_item(self):

        return_string = ""
        return_string = return_string + (self.name + "........." + str(self.price))

        if self.taxable:
            return_string += ("  T")

        return return_string

a1 = Item("Banana",2.00, True)

print(a1.print_item())
