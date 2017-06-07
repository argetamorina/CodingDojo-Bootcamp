class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            self.result -= num
        return self

print MathDojo().add(4).add(9, 5).subtract(10, 5).result

# PART II
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            if isinstance(num, list):
                for idx in num:
                    self.result += idx
            else:
                self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            if isinstance(num, list):
                for idx in num:
                    self.result -= idx
            else:
                self.result -= num
        return self


print MathDojo().add([0],3,4).add([3, 5, 5, 8], [4, 6, 4.25]).subtract(2, [5, 3], [3.3, 4.3]).result

#PART III
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            if isinstance(num, (list, tuple)):
                for idx in range(0,len(num)):
                    self.result += num[idx]
            else:
                self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            if isinstance(num, (list, tuple)):
                for idx in range(0,len(num)):
                    self.result -= num[idx]
            else:
                self.result -= num
        return self

print MathDojo().add([1, 4, 2], 2, (6, 2, 4), 2).subtract([2, 6, 8], (1, 5), 3).result
