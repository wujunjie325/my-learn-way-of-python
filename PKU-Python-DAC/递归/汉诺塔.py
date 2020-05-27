def moveTower(n, f, w, t):
    if n < 1:
        return
    moveTower(n - 1, f, t, w)
    moveDisk(n, f, t)
    moveTower(n - 1, w, f, t)

def moveDisk(d, f, t):
    print(f"moving disk[{d}] from{f} to {t}")

moveTower(3, " 1 ", " 2 ", " 3 ")