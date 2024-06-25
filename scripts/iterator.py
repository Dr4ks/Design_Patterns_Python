from __future__ import annotations
from typing import Any, List, Optional

# Iterator interface
class Iterator:
    def __init__(self, collection: MyList):
        self._collection = collection
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._collection)

    def next(self) -> Optional[Any]:  # getNext()
        if self.has_next():
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            return None

# Aggregate interface
class Aggregate:
    def create_iterator(self) -> Iterator: # createIterator()
        pass

# Concrete Aggregate
class MyList(Aggregate):
    def __init__(self):
        self._items: List[Any] = []

    def add_item(self, item: Any):
        self._items.append(item)

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

    def __len__(self) -> int:
        return len(self._items)

    def create_iterator(self) -> Iterator:  # createIterator()
        return Iterator(self)

# Client code
def client_code(collection: Aggregate):
    iterator = collection.create_iterator()

    while iterator.has_next():
        item = iterator.next()
        print(item)

# Usage
my_list = MyList()
my_list.add_item("Item 1")
my_list.add_item("Item 2")
my_list.add_item("Item 3")

client_code(my_list)

## Output
# Item 1
# Item 2
# Item 3