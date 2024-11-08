def inverso_modular(a: int, n: int):
    return a**(n-2)%n



print(inverso_modular(3, 131))

# a * b = 1 mod n
# a ** n  = a mod n
# a ** n-1 = 1 mod n
# a * a ** n-2 = 1 mod n
# b = a ** n-2 mod n

# 40 = 40 mod 100
# 140 = 40 mod 100
# 240 = 40 mod 100
# 340 = 40 mod 100
# 1040 = 40 mod 100