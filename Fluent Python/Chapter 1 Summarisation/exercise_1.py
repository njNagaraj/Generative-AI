# demonstrate how len() works inside in py 
# You can modify len() as you want by modyfying __len__(self)

class MyCustomClass:
    def __init__(self, data):
        self.data = data
        print(self.data)
    
    def __len__(self):
        return len(self.data) + 5

my_obj = MyCustomClass([1, 2, 3, 4, 5])
print(len(my_obj))  # Output: 10