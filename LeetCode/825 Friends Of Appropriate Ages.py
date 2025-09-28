class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        same_age = {} # возраст -> кол-во ровесников
        for i in range(len(ages)):
            if ages[i] in same_age:
                same_age[ages[i]] += 1
            else:
                same_age[ages[i]] = 1
        ages = sorted(list(set(ages)))
        if len(ages) == 1:
            if ages[0] > 0.5*ages[0]+7:
                return same_age[ages[0]] * (same_age[ages[0]]-1)
            else:
                return 0
        res = 0
        for x in range(len(ages)):
            l, r = 0, x-1
            m = 0
            while l <= r: # поиск младшего получателя запроса в друзья
                m = (l+r)//2
                if ages[m] > 0.5*ages[x]+7:
                    r = m-1
                else:
                    l = m+1
            for y in range(m, x): # запросы от младшего к старшему
                if ages[y] > 0.5*ages[x]+7:
                    res += same_age[ages[y]] * same_age[ages[x]]
            if same_age[ages[x]] > 1: # запросы между ровесниками
                if ages[x] > 0.5*ages[x]+7:
                    res += same_age[ages[x]] * (same_age[ages[x]]-1)
        return res