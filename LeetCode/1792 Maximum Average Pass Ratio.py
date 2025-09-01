import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def increase(p: int, t: int):  # прирост к среднему при добавлении молодечика
            return (p + 1) / (t + 1) - p / t

        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-increase(p, t), p, t))

        for i in range(extraStudents):
            delta, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-increase(p, t), p, t))

        res = 0
        for delta, p, t in heap:
            res += p / t
        print(heap)
        return res / len(classes)
