row=5
for i in range(1,row+1):
  if i%2!=0:
    print(" "*(row-i)+" *"*i)
for i in range(row-1,0,-1):
  if i%2!=0:
    print(" "*(row-i)+" *"*i)

