from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        l, r = 0, len(self.calendar) - 1
        if startTime == 2 and endTime == 10:
            print(self.calendar)
        while l <= r:
            if startTime == 2 and endTime == 10:
                print(l, r)
            m = (l + r) // 2
            event = self.calendar[m]
            if (event[0] <= startTime < event[1] or
                    event[0] < endTime <= event[1] or
                    startTime <= event[0] <= event[1] <= endTime):
                return False
            if event[0] >= endTime:
                r = m - 1
            elif event[1] <= startTime:
                l = m + 1
        self.calendar.add([startTime, endTime])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)