"""
Conor Jackson
Professor Deever
Blackout Math

This program allows the user to enter an unequal equation (ex. (4*4/7) = (4*4+1))
The equations are equaled by crossing out two of the integers in the string
"""

def compute():
    eq = "1+1=abd"
    n = 0
    while n != len(eq) - 1:
        if eq[n] == '=':
            eq1 = eq[:n]
            eq2 = eq[n+1:]
        else:
            n = n + 1
    m = len(eq1) - 1
    o = len(eq2) - 1
    leftSide(eq1, m)
    print(leftSide(eq1, m))
    
def leftSide(eq1, m):
    a = 1
    b = 0
    c = 0
    d = 0
    e = 0
    while a != m-1:
        if eq1[a] == "+":
            plus = eq1[a+1:]
            h = len(plus) - 1
            while b != h:
                if plus[b] == "+" or plus[b] == "-" or plus[b] == "*" or plus == "/":
                    left = float(eq1[:a]) + float(plus[:b])
                    eq1 = str(left) + plus[b:]
                    m = len(eq1)
                    b = b+1
                    print(left)
                else:
                    b = b + 1
        elif eq1[a] == "-":
            minus = eq1[a+1:]
            i = len(minus) - 1
            while c != i:
                if minus[c] == "+" or minus[c] == "-" or minus[c] == "*" or minus[c] == "/":
                    left = float(eq1[:a]) - float(minus[:c])
                    eq1 = str(left) + minus[c:]
                    m = len(eq1)
                    print(left)
                    c = c + 1
                else:
                    c = c+1
        elif eq1[a] == "*":
            times = eq1[a+1:]
            j = len(times) - 1
            while d != j:
                if times[d] == "+" or times[d] == "-" or times[d] == "*" or times[d] == "/":
                    left = float(eq1[:a]) * float(times[:d])
                    eq1 = str(left) + times[d:]
                    m = len(eq1)
                else:
                    d = d + 1
        elif eq1[a] == "/":
            divid = eq1[a+1:]
            k = len(divid) - 1
            while e != k:
                if divid[e] == "+" or divid[e] == "-" or divid[e] == "*" or divid[e] == "/":
                    left = float(eq1[:a]) / float(divid[:e])
                    eq1 = str(left) + divid[e:]
                    m = len(eq1)
                    e =e+1
                else:
                    e = e+1
        elif a >= m:
            break
        else:
            a = a + 1
        
            

