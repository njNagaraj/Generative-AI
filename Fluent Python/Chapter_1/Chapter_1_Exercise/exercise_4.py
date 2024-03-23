# demonstrating how loop works inside
class MyIterable:
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        print("Calling __iter__")
        return iter(self.data)
    
    def __getitem__(self, index):
        print("Calling __getitem__")
        return self.data[index]

# Creating an instance of MyIterable
my_iterable = MyIterable([1, 2, 3, 4, 5])

# Iterating over the instance using a for loop
for i in my_iterable: # will call __iter__()
    print(i)

# Accessing elements using indexing
print(my_iterable[2]) #will call __getitem_()
print(my_iterable[4])
