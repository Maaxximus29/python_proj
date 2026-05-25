coins = int(input())
for _ in range(coins):
    x,y = map(int, input().split())
    diff = y - 0
    if x > 0 and y > 0:
        print("YES")
        continue
    if y > x and y > 0:
        print("YES")
        continue
    elif diff == 0:
        print("YES")
        continue
    elif diff == 1 or diff == -1:
        print("YES")
        continue
    elif diff != 1 or diff != -1:
        print("NO")
        continue


#1989A Catch the Coin