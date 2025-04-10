def Facto(n):
  if n<0:
    return "Number should not be Negative"
  result=1
  for i in range(1,n+1):
    result*=i
  return result
num = int(input("ENter Number "))
print("Factorial :",Facto(num))