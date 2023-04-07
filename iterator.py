class myCount:
    def __iter__(self):
        self.start = 0
        return self
        
    def __next__(self):
        step = self.start
        if step < 12:
            self.start += 2
            return step
        else:
            raise StopIteration

myClass = myCount()
myIter = iter(myClass)
for x in myIter:
    print(x)