n=int(input("enter the no. of stock prices: "))

prices=[]
for i in range(n):
    prices.append(float(input()))

for i in range(10):
    swapped=False

    for j in range(n-i-1):
        if prices[j]>prices[j+1]:
            prices[j],prices[j+1]=prices[j+1],prices[j]
            swapped=True

    if not swapped:
        break

unique=[]
for i in range(n):
    if i==0 or prices[i]!=prices[i-1]:
        unique.append(prices[i])

print("\nTop 10 highest prices: ")
for i in range(n-1, n-11, -1):
    print(prices[i])

print("\nUnique Readings:")
print(unique)
