def general_poly(L):
    def inside(x):
        total = 0
        for i in range(len(L)):
            k = (len(L)-1) - i 
            total += (L[i] * (x**k))
        return total
    return inside
