from sortedcontainers import SortedList


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.available = {}
        self.rented = SortedList()
        self.prices = {(shop, movie): price for shop, movie, price in entries}

        for i in entries:
            shop, movie, price = i
            if not movie in self.available:
                self.available[movie] = SortedList()
            self.available[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        if movie in self.available:
            res = [entry[1] for entry in self.available[movie][:5]]
        else:
            res = []
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        res = [entry[1:] for entry in self.rented[:5]]
        return res
