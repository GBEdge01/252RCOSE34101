a = int(input("몇 층까지 쌓을까요? "))

for i in range(a):
    for j in range(a - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()