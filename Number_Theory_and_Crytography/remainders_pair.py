import matplotlib.pyplot as plt

a, b = 10, 5
n = a * b

plt.plot([i % a for i in range(n)], [i % b for i in range(n)],
         color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

plt.axis('square')
plt.xlim(-1, a)
plt.ylim(-1, b)
plt.xlabel(f'm mod {a}')
plt.ylabel(f'm mod {b}')

plt.savefig('crt-10-5.png')