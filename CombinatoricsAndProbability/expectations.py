import itertools as it
import operator as op
import matplotlib.pyplot as plt


num_days = 365

factors = [1 - i / num_days for i in range(num_days)]
prob_no_collision = list(it.accumulate(factors, op.mul))
prob_collision = [1 - p for p in prob_no_collision]

for n in (22, 23, 35, 100):
    print(f'The collision probability for {n} people '
          f'is {prob_collision[n - 1]}')

print('\n')

for n in (22, 23, 35, 100):
    print(f'The no collision probability for {n} people '
          f'is {prob_no_collision[n - 1]}')

plt.plot(prob_collision, label='$Collision_probability$')
plt.plot(prob_no_collision, label='$No collision_probability$')
plt.legend(loc='lower right')
plt.savefig('birthdays.png')
