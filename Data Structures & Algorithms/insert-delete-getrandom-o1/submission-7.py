class RandomizedSet:

    def __init__(self):
        self.set_map = {}
        self.val_list= []

    def insert(self, val: int) -> bool:
        if val not in self.set_map:
            self.set_map[val] = len(self.val_list)
            self.val_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set_map:
            # gets the index of that element
            idx = self.set_map[val]
            # Update the map for the last element moving to the new index
            last_element = self.val_list[-1]
            self.val_list[idx] = last_element
            self.set_map[last_element] = idx
            # Clean up
            self.val_list.pop()
            del self.set_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.val_list)