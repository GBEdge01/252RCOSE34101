a = int(input("몇 층까지 쌓을까요? "))

for i in range(a):
    for j in range(a):
        if i == 0 or i == a - 1:
            print("*", end="")
        elif j == 0:
            print("*", end="")
        elif j == a - 1:
            print("*", end="")
        elif i == j:
            print("*", end="")
        elif j == a - i - 1: 
            print("*", end="")
        else:
            print(" ", end="")        
    print()