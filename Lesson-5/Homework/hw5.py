## Question 1
y = int(input())
if y % 4 == 0 and y % 400 == 0 and y % 100 != 0:
    print("y is a leap year")
else: 
    print("y is not a leap yaer")
  ## Question 2
n = int(input())
1 <= n <= 100
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n in range(2,5):
    print("Not Weird")
elif n % 2 == 0 and n in range(6,20):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird") 
## Question 3
a = int(input())
b = int(input())
## Solution 1
if a % 2 == 0:
    print("even number")
else:
    print("odd number")
if b % 2 == 0:
    print("even number")
else:
    print("odd number")
## Solution 2
a = int(input())
b = int(input())
result = {0: "even number", 1: "odd number"}
print(result[a%2])
print(result[b%2])
