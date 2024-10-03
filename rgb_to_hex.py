import math

def nums(a):
    if a > 255:
        a = 255
    if a < 0:
        a = 0
    a = a / 16
    a = list(math.modf(a))
    a1 = a[1]
    a1 = int(a1)
    a2 = a[0] * 16
    a2 = int(a2)  
    return a1, a2

def rgb(r, g, b):
    r1, r2 = nums(r)
    g1, g2 = nums(g)
    b1, b2 = nums(b)

    hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']         
    new_r = hex[r1] + hex[r2]
    new_g = hex[g1] + hex[g2]
    new_b = hex[b1] + hex[b2]
    rgb_to_hex = new_r + "" + new_g + "" + new_b
    return rgb_to_hex