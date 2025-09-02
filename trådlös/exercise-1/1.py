import math
# 1a
print("exercise 1 a)")
R = 5
C = 300*(10**(-12))
L = 0.844*(10**(-6))
def calc(R, C, L):
    w0 = math.sqrt(1/(L*C))
    print("w0", w0)
    Q = 1/(R*C*w0)
    print("Q", Q)
    B_3db = w0/(2*math.pi*Q)
    print("B_3db", B_3db/1000000, "MHz")
calc(R,C,L)
# 1b
print("exercsie 1 b)")
print("i)")
calc(R*2, C, L)
print("ii)")
calc(R, C*2, L)
print("iii)")
calc(R, C, L*2)
# exercise 3

print("exercise 3")

print("N_th", 1.38*291*10**(-23))