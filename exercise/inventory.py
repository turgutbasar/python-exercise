from .dbmock import DbMock

class Inventory(dict):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        result = f"--=={self.name}==--"
        for record in self.values():
            result += "\n" + str(record)
        return result

    def add_item(self, item):
        record = self.get(item.get_key() + "_" +  self.name)
        if record:
            record.add_item()
        else:
            record = InventoryRecord(item, self.name)
            self[item.get_key() + "_" +  self.name] = record

    def delete_item(self, item):
        record = self.get(item.get_key() + "_" +  self.name)
        if record:
            if record.delete_item() == 0:
                self.pop(record.key)

db = DbMock()
class InventoryRecord:
    def __init__(self, item, inventory_name):
        self._number_of_copy = 1
        self.key = item.get_key() + "_" + inventory_name
        self.item = item
        self._update()

    def _update(self):
        """
        TODO : Update what we have in this record to db using context manager you created
        """
        db.update_record(self.key, {"iten" : self.item.as_dict(), "copy": self._number_of_copy})
        db.commit()

    def _delete(self):
        """
        TODO : Delete this record using context manager you created
        """
        db.delete_record(self.key)
        db.commit()

    def add_item(self):
        self._number_of_copy += 1
        self._update()

    def delete_item(self):
        self._number_of_copy -= 1
        if self._number_of_copy == 0:
            self._delete()
        else:
            self._update()
        return self._number_of_copy

    def __str__(self):
        result = str(self.item)
        result += "\nCopy :: " + str(self._number_of_copy)
        result += "\nKey :: " + self.key
        return result


class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_key(self):
        return self.title.replace(" ", "") + "_" + self.author.replace(" ", "")

    def as_dict(self):
        return {
            "title": self.title,
            "author": self.author
        }

    def __str__(self):
        return "Not Implemented"


# TODO : Implement needed fields and methods
class Book(Item):
    pass

# TODO : Implement magazine class with additional fields and necessary overrides
