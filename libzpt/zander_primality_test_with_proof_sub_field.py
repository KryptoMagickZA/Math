# Zander Primality Test
# Odd number (mod 3) equals 2 is prime, if raised to the power of 2 and mod 3 equals 1
# First step is always prime if 0 or 2 and second step proves primality if 1
# First step is always prime if 0 or 2 and second step proves primality if the second step is equal to 1

# Zulu Akula Hunter

pp = "Provable Prime"
npp = "Non-Provable Prime"

# Provable Prime

print(pp)

a = 980327
b = (9 + 8 + 0 + 3 + 2 + 7) % 3
c = ((9 + 8 + 0 + 3 + 2 + 7) ** 2) % 3

print(a)
print(b)
print(c)

# Non-Provable Prime

print(npp)

a = 980321
b = (9 + 8 + 0 + 3 + 1 + 3) % 3
print(a)
print(b)

# Non-Provable Prime

print(npp)

a = 980319
b = (9 + 8 + 0 + 3 + 1 + 9) % 3
c = ((9 + 8 + 0 + 3 + 1 + 9) ** 2) % 3
print(a)
print(b)

# Provable Prime

print(pp)

a = 980321
b = (9 + 8 + 0 + 3 + 2 + 1) % 3
c = ((9 + 8 + 0 + 3 + 2 + 1) ** 2) % 3
print(a)
print(b)
print(c)

# Proof of ZPT Primaility in Base Field

p = (980321 * 2) % 3
print("Proof of ZPT Primaility in Field", 980321, p)
print(p)

# Proof of ZPT Primaility in Base Field

n = (980319 * 2) % 3
print("Proof of ZPT Primaility in Field", 980319, n)
print(n)

# Proof of ZPT Primaility in Base Field

z = (980327 * 2) % 3
print("Proof of ZPT Primaility in Field", 980327, z)
print(z)


# Proof of ZPT Primaility in Field

p = (3 * 2 ** int(980321 / 2)) % 980321
print("Proof of ZPT Primaility in Field", 980321, p)
print(p)

# Proof of ZPT Primaility in Field

n = (3 * 2 ** int(980319 / 2)) % 980319
print("Proof of ZPT Primaility in Field", 980319, n)
print(n)

# Proof of ZPT Primaility in Field

z = (3 * 2 ** int(980327 / 2)) % 980327
print("Proof of ZPT Primaility in Field", 980327, z)
print(z)


# Proof of ZPT Primaility in Sub-Field

p = (3 * 2 ** int(980321 / 2)) % 980321
print("Proof of ZPT Primaility in Field", 980321, p)
print(p)

# Proof of ZPT Primaility in Sub-Field

n = (3 * 2 ** int(980319 / 2)) % 980319
print("Proof of ZPT Primaility in Field", 980319, n)
print(n)

# Proof of ZPT Primaility in Sub-Field

z = (3 * 2 ** int(980327 / 2)) % 980327
print("Proof of ZPT Primaility in Field", 980327, z)
print(z)
