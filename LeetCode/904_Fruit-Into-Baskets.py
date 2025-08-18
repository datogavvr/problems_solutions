class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxon = 1 # макс число фруктов
        current = 1 # число фруктов в текущем подсчете
        first_type = fruits[0] # тип фруктов в первой корзине
        second_type = -1 # тип фруктов во второй корзине
        last_substring = [first_type, 1] # число и тип последних одинаковых фруктов

        for i in range(1, len(fruits)):
            fruit = fruits[i]
            if fruit != first_type and fruit != second_type:
                current = last_substring[1]
                first_type = fruits[i-1]
                second_type = fruit
                last_substring = [second_type, 1]
            else:
                if fruit == fruits[i-1]:
                    last_substring[1] += 1
                else:
                    last_substring[1] = 1
            current += 1
            if maxon < current:
                maxon = current
        return maxon