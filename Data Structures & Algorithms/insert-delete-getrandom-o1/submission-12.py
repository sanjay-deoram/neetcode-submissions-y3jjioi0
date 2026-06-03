class RandomizedSet:
    """
    Time complexity: O(1)
    Space complexity: O(n)
    n is the number of elements stored in the RandomizedSet
    """
    def __init__(self):
        self.val_idx = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val not in self.val_idx:
            self.val_idx[val] = len(self.values)
            self.values.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_idx:
            idx = self.val_idx[val]
            last_element = self.values[-1]
            self.values[idx] = last_element
            self.val_idx[last_element] = idx
            self.values.pop()
            del self.val_idx[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)