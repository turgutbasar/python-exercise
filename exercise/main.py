"""
In this exercise,
We will have a functioning library inventory system eventually. This system have an
in-memory db to store inventory information as inventory records.

Following class will be the starting point for this exercise. You can execute this
script to test inventory system. Please add whatever you want to do with inventory :
add books, delete books, merge inventories.

Requested Features :
- We should be able add two inventories and assign final result to new var inv3.
Don't change anything in inv1 and inv2. Hint : Keep name of inv1 as name of result, merge records
Eg : inv3 = inv1 + inv2

- We should be able to update database and delete records. Define a context manager
"OpenDB" and interact with instance of DBMock class. Please fill InventoryRecord._update and
InventoryRecord._delete methods properly using context manager we created.

- Implement Book class to add more book related fields and override as_dict and __str__

- Implement Magazine class similar to book and add it to inventories

- Implement a decorator to count spent db credits. Update = 2 credit, Delete = 2, Read = 1

- Override __new__ method of Inventory class to allow only 2 inventories to be created. Test it
with following code
"""
from exercise.inventory import Inventory, Book


class InventoryApp:
    def __init__(self):
        self.inventories = {
            "social_books": Inventory("social_books"),
            "science_books": Inventory("science_books"),
            "other_science_material": Inventory("other_science_material")
        }

    def run(self):
        social_inv = self.inventories.get("social_books")
        science_inv = self.inventories.get("science_books")
        other_inv = self.inventories.get("other_science_material")
        book = Book("Some Book", "Some Writer")

        social_inv.add_item(book)
        social_inv.add_item(book)

        book2 = Book("Some Book2", "Some Writer")

        social_inv.add_item(book2)

        book3 = Book("Some Book3", "Some Writer2")

        science_inv.add_item(book3)
        science_inv.add_item(book2)
        science_inv.delete_item(book2)

        book4 = Book("Some Book4", "Some Writer")

        science_inv.add_item(book4)
        science_inv.add_item(book3)

        # TODO : Add some science "magazine" and "books" to "other_science_material" inventory
        #magazine = Magazine(...)
        #other_inv.add_item(magazine)

        for inventory in self.inventories.values():
            print(inventory)

        # TODO : After implementing addition overload, uncomment to test
        #some_new_inventory = science_inv + other_inv
        #print(some_new_inventory)


if __name__ == "__main__":
    InventoryApp().run()
