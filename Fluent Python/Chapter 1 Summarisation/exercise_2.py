# demostrate how accessing value of dict using key works
class MyCustomClass:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, key):
        return self.data[key]

my_obj = MyCustomClass({'a': 1, 'b': 2, 'c': 3})
print(my_obj['a'])  # Output: 1
print(my_obj['b'])  # Output: 2