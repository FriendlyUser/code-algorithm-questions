### Biggest 2 digit palindrome is 9009
### Just brute force
### palidrome is when a string is the same both ways

# checks if the number is a palidrome
def checkPali(prod):
    strProd = str(prod)
    return strProd == strProd[::-1]


# Computers are fast, so we can implement this solution directly without any clever math.
def compute():
    maxPali = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if checkPali(prod) and prod > maxPali:
                maxPali = prod
    return str(maxPali)


def efficient_answer():
    ans = max(
        i * j
        for i in range(100, 1000)
        for j in range(100, 1000)
        if str(i * j) == str(i * j)[::-1]
    )
    return str(ans)


ans = efficient_answer()
print(ans)