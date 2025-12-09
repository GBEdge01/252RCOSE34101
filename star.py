a = int(input("몇 층까지 쌓을까요? "))

b = int(input("한 층에 몇 개의 별을 쌓을까요? "))

for i in range(1, a + 1):
    for j in range(b):
        print("*", end="")
    print()