for i in range(0, 30):
    tot1 = int(input("input test1 score: "))
    tot2 = int(input("input test2 score: "))
    tot3 = int(input("input test3 score: "))
    ave1 = ave1 + tot1
    ave2 = ave2 + tot2
    ave3 = ave3 + tot3
tot = (ave1 + ave2 + ave3) / 30
ave1 = ave1 / 30
ave2 = ave2 / 30
ave3 = ave3 / 30

print("test1 average", ave1)
print("test2 average", ave2)
print("test3 average", ave3)
print("total average", tot)