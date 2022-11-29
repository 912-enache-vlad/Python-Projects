
#functions

from random import randint

def generate_four_digit_random():
    '''
    The function generate a four different digits number
    @return: the number generated
    '''
    used = [False]*10
    n = randint(1, 9)
    used[n] = True

    for i in range(3):
        d = randint(0, 9)
        while(used[d] == True):
            d = randint(1, 9)
        used[d] = True
        n = n * 10 + d
    return n

def valid_guess(n:int):
    #
    used = [False] * 10
    while(n > 10):
        last = int(n % 10)
        if used[last] == True:
            return False
        else:
            used[last] = True
            n //= 10
    if n == 0 or used[n] == True:
        return False
    return True

def number_of_codes_and_runners(guess:int, secret_number:int):
    used = [False] * 10
    codes = 0
    runners = 0
    # from number into list
    sn = [0] * 4
    i = 3
    while(i >= 0):
        sn[i] = secret_number % 10
        secret_number //= 10
        i -= 1

    g = [0] * 4
    i = 3
    while (i >= 0):
        g[i] = guess % 10
        guess //= 10
        i -= 1

    for i in [0, 1, 2, 3]:
        if g[i] == sn[i]:
            codes += 1
            used[g[i]] = True

    for i in [0, 1, 2, 3]:
        if g[i] in sn and used[g[i]] == False:
            runners += 1

    return codes, runners


