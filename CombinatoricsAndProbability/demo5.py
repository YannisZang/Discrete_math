from random import randint, seed

seed(27)

dice1 = [2, 2, 2, 2, 3, 3]
dice2 = [1, 1, 1, 1, 6, 6]

num_rounds = 10 ** 5
num_dice1_wins = 0

for _ in range(num_rounds):
    dice1_result = dice1[randint(0, 5)]
    dice2_result = dice2[randint(0, 5)]

    if dice1_result > dice2_result:
        num_dice1_wins += 1

print(f'Out of {num_rounds} throws, dice1 won {num_dice1_wins} times')