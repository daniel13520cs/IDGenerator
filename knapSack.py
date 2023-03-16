from typing import List

class Thing:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def bruteforce(things: List[Thing], weight_limit: int):
    if len(things) == 0:
        return 0, []

    max_value = 0
    max_valued_packed = []
    for i, thing in enumerate(things):
        if thing.weight > weight_limit:
            continue

        value, packed = bruteforce(things[i + 1:], weight_limit - thing.weight)
        if value + thing.value >= max_value:
            max_value = value + thing.value
            max_valued_packed = [thing] + packed

    return max_value, max_valued_packed

if __name__ == '__main__':
    wallet = Thing(5, 3)
    watches = Thing(4, 10)
    things = [wallet, watches]
    value, collected = bruteforce(things, 10)
    print(value)
    print(collected)
