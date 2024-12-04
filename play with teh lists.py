l = [4, 5, 2 ,1, 3, 6, 7, 9, 8 ,10]
print("Original list:", l )

count = 0 

for i in l:
    count += i

avg = count/len(l)

print("sum = ", count)
print("average = ", avg)

l.sort()

print("The smallest element is:", l[0])
print("The largest element is:", l[-1])


