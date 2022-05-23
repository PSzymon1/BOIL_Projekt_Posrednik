
import numpy as np


def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(str(table[i][j]) + "; ", end="")
        print()

def iterate(table, earnings):
    alpha = [None for _ in range(len(table[0]))]
    beta = [None for _ in range(len(table))]
    alpha[0] = 0
    for i in range(len(table[0])):
        for j in range(len(table)):
            if beta[j] is None and table[i][j] != 0 and alpha[i] is not None:
                beta[j] = table[i][j] - alpha[i]
            elif beta[j] is not None and table[i][j] != 0 and alpha[i] is None:
                alpha[i] = table[i][j] - beta[j]


def calculate_total(sellers, buyers, earnings):
    sell_amt = sum(sellers)
    buy_amt = sum(buyers)
    temp_sellers = sellers
    temp_buyers = buyers
    temp_earnings = earnings
    table = [[0 for _ in range(len(sellers))] for _ in range(len(buyers))]
    while sum(temp_sellers) + sum(temp_buyers) > 0:
        for i in range(len(buyers)):
            for j in range(len(sellers)):
                if np.amax(temp_earnings) == temp_earnings[i][j]:
                    temp_earnings[i][j] = -99999
                    if temp_sellers[j] >= temp_buyers[i]:
                        table[i][j] = temp_buyers[i]
                        temp_sellers[j] -= temp_buyers[i]
                        temp_buyers[i] = 0

                    else:
                        table[i][j] = temp_sellers[j]
                        temp_buyers[i] -= temp_sellers[j]
                        temp_sellers[j] = 0

    return table


if __name__ == '__main__':
    sellers = [20, 30, 65]
    buyers = [10, 28, 27, 50]
    earnings = [[12, 6, 0],[1, 4, 0],[3, -1, 0],[0, 0, 0]]
    tab = calculate_total(sellers, buyers, earnings)
    print_table(tab)

