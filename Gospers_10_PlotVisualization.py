
import matplotlib.pyplot as plt
import math

L = [[], [], [], [], [], [], [], [], [], []]
for s in range(170):
    
    n = s + 1
    
    for a in range(6):
        
        for i in range(100):
            
            k = i*(10**(-a - 1))
            f = math.factorial(n)
            
            aprx = math.sqrt((2*n + 1/3 + k)*math.pi)*((n/math.e)**n)
            r = f/aprx
            R = -math.log10(abs(math.log(r)))
            print("k =", k,"R =", R)
            L[i%10].append(R)

plt.plot(L[0], 'C0.')
plt.plot(L[1], 'C1.')
plt.plot(L[2], 'C2.')
plt.plot(L[3], 'C3.')
plt.plot(L[4], 'C4.')
plt.plot(L[5], 'C5.')
plt.plot(L[6], 'C6.')
plt.plot(L[7], 'C7.')
plt.plot(L[8], 'C8.')
plt.plot(L[9], 'C9.')

plt.show()
