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


def calculate_total(sellers, buyers, earnings, e_input):
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
    print(e_input)
    table = calculate_step(table, e_input)
    return table


def calculate_optimum(tab, alpha, beta, earnings):
    stage = [[None for _ in range(len(alpha))] for _ in range(len(beta))]

    for i in range(len(beta)):
        for j in range(len(alpha)):
            if tab[i][j] == 0:
                stage[i][j] = earnings[i][j] - alpha[j] - beta[i]

    return stage


def calculate_ab(tab, earnings):
    def alpha_row(alpha, beta, n):
        for i in range(len(beta)):
            if beta[i] is None and tab[i][n] != 0:
                beta[i] = earnings[i][n] - alpha[n]
                alpha, beta = beta_row(alpha, beta, i)
        return alpha, beta

    def beta_row(alpha, beta, m):
        for i in range(len(alpha)):
            if alpha[i] is None and tab[m][i] != 0:
                alpha[i] = earnings[m][i] - beta[m]
                alpha, beta = alpha_row(alpha, beta, i)
        return alpha, beta
    #print(earnings)
    alpha = [None for _ in range(len(tab[0]))]
    beta = [None for _ in range(len(tab))]
    alpha[0] = 0
    alpha, beta = alpha_row(alpha, beta, 0)
    return alpha, beta


def is_optimal(stage, alpha, beta):
    for i in range(len(beta)):
        for j in range(len(alpha)):
            if stage[i][j] is not None and stage[i][j] > 0:
                return False
    return True


def cycle(tab, stage, alpha, beta):
    n = None
    m = None
    for i in range(len(beta)):
        for j in range(len(alpha)):
            if stage[i][j] is not None and stage[i][j] > 0:
                if n is not None:
                    if stage[i][j] > stage[n][m]:
                        n = i
                        m = j
                else:
                    n = i
                    m = j

    for i in range(len(beta)):
        if stage[i][m] is None:
            for j in range(len(alpha)):
                if stage[i][j] is None and j != m:
                    if stage[n][j] is None:
                        value = np.amax([tab[n][m], tab[i][j]])
                        tab[n][m] -= value
                        tab[i][j] -= value
                        tab[n][j] += value
                        tab[i][m] += value

    return tab


def calculate_step(tab, earnings):
    alpha, beta = calculate_ab(tab, earnings)
    #print(alpha)
    #print(beta)
    stage = calculate_optimum(tab, alpha, beta, earnings)

    while not is_optimal(stage, alpha, beta):
        alpha, beta = calculate_ab(tab, earnings)
        stage = calculate_optimum(tab, alpha, beta, earnings)
        tab = cycle(tab, stage, alpha, beta)

    return tab


if __name__ == '__main__':
    sellers = [20, 30, 65]
    buyers = [10, 28, 27, 50]
    earnings = [[12, 6, 0], [1, 4, 0], [3, -1, 0], [0, 0, 0]]
    e = np.copy(earnings)
    tab = calculate_total(sellers, buyers, earnings, e)
    # print_table(tab)
    print(np.transpose(np.matrix(tab)))
