class Parent:
    def __init__(self):
        self.value = "Parent"
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Child"

obj = Child()
print(obj.value)