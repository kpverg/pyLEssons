my_list=[1,2,3]
it=iter(my_list)

print(next(it))
print(next(it))
print(next(it))

my_dict={"a":1,
        "b":2}

it=iter(my_dict)
print(next(it))
print(next(it))


class MyIterator:
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        self.n+=1000
        if self.n<=100000000:
            return list(range(self.n-1000,self.n))
        else:
            raise StopIteration
        

for xiliada in MyIterator():
    for num in xiliada:
        print(num)

