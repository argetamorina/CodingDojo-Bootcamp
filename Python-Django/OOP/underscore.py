class Underscore(object):
    def map(self, arr, func):
        result = []
        for x in arr:
            result.append(func(x))
        return result

    def reduce(self, arr, func, memo):
        for x in arr:
            memo = func(x, memo)
        return memo

    def find(self, arr, func):
        for x in arr:
            if func(x):
                return x
        return "undefined"

    def filter(self, arr, func):
        result = []
        for x in arr:
            if func(x):
                result.append(x)
        return result

    def reject(self, arr, func):
        result = []
        for x in arr:
            if not func(x):
                result.append(x)
        return result

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore()

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print evens

finds = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print finds

mappings = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 6)
print mappings

reducing = _.reduce([1, 2, 3, 4, 5, 6], (lambda x, y: x + y), 6)
print reducing

rejecting = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 1)
print rejecting
