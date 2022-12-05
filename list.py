def count(lst):
    even = 0
    odd = 0
    for i in lst:
     if i%2 == 0:
        even+=1
     else:
        odd+=1
    return odd,even

lst = [10,35,77,64,56,33,22,31,69]  
odd,even = count(lst)     

print(even)
print(odd)
print("even :{} and odd: {}".format(even,odd) )
