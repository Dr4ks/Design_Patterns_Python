class SortStrategy:
    def sort(self, data):
        pass

class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        print("Sorting using QuickSort")
        return sorted(data)

class MergeSortStrategy(SortStrategy):
    def sort(self, data):
        print("Sorting using MergeSort")
        return sorted(data)

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

data = [5, 3, 1, 4, 2]
strategy = QuickSortStrategy()
sorter = Sorter(strategy)
result = sorter.sort_data(data)
print(result)

strategy = MergeSortStrategy()
sorter = Sorter(strategy)
result = sorter.sort_data(data)
print(result)
