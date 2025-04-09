l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
common_item=[]
 
for item1 in l1:
   for item2 in l2:
     if item1 == item2:
       common_item.append(item1)
print(common_item)