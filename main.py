# 1. Sonning juft yoki toqligini aniqlash
n = int(input("Son kiriting: "))
print("Juft" if n % 2 == 0 else "Toq")

# 2. 3 ta sondan eng kattasini topish
a, b, c = map(int, input().split())
print(max(a, b, c))

# 3. 1 dan n gacha yig‘indi
n = int(input())
print(sum(range(1, n+1)))

# 4. Faktorial
n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
print(f)

# 5. Sonni teskarisiga o‘girish
n = input()
print(n[::-1])
