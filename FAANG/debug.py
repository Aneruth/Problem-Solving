asd = [1,2,2,3,4]
def foo(asd):
    for i in asd:
        for j in range(len(asd)):
            if i == asd[j]:
                out = True
            else:
                out = False    
    return out
print(foo(asd))