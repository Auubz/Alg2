class Item:

    last_sku_used = 0

    def __init__(self,name,price,taxable):

        self.sku = Item.last_sku_used + 1
        self.name = ""
        self.price = 0
        self.taxable = taxable

        Item.last_sku_used = self.sku



a1 = Item("first_item", 2.00, True)
a2 = Item("Second item",3.00, False)


