import random
import time


def problem4():
    hint_list = ['Formula1', 'Formula2']
    force4 = random.randint(1, 1000)
    distance4 = random.randint(1, 100)
    time4 = random.randint(1, 60)
    problem = f'Problem4:A movable object requires a force of {force4}N to move it. ' \
              f'How much work is done if the object is moved {distance4}m ' \
              f'and what average power is utilized if the movement takes {time4} seconds? '
    print(10 * '-')
    for char in problem:
        print(char, end='')
        time.sleep(.01)

    work4 = force4 * distance4
    power4 = work4 / time4

    # print(f'Work={Qty(work4)}Nm = {Qty(work4)}J')
    # print(f'Power = {Qty(power4)}W')
    # asd = str(Qty(power4))
    # print('print  string %s' % asd)

    result_4 = [hint_list, work4, power4]

    return result_4


# problem 5
def problem5():
    hint_list = ['Formula for force', 'Formula for work', 'Formula for power']
    mass5 = random.randint(2, 15)
    multiplier_mass5 = ["grams", "kilograms", "tons"]
    multiplier_time5 = ['seconds', 'minutes']
    multiplier_dist5 = ['meters', 'kilometers']
    pm5 = random.choices(multiplier_mass5, weights=[2, 3, 1], k=1)
    md5 = random.choices(multiplier_dist5, weights=[1, 2], k=1)
    nr51 = random.randint(1, 100)
    nr5 = random.randint(1, 60)
    minsec5 = random.choices(multiplier_time5, weights=[1, 2], k=1)

    problem5 = f'\n Problem5: A mass of {mass5} {pm5[0]} is to be raised to a height of {nr5} {md5[0]} in {nr51} {minsec5[0]}. ' \
               f'What work needs to be done and what is the power is necessary for thi action?'
    print(10 * '_', problem5)

    multiplmass5 = 1
    multipldist5 = 1
    multipltime5 = 1
    accel5 = 9.81

    if pm5[0] == 'grams':
        multiplmass5 = 10 ** -3
    elif pm5[0] == 'kilograms':
        multiplmass5 = 10 ** 0
    elif pm5[0] == 'tons':
        multiplmass5 = 10 ** 3

    if md5[0] == 'meters':
        multipldist5 = 10 ** 0
    elif md5[0] == 'kilometers':
        multipldist5 = 10 ** 3

    if minsec5[0] == 'seconds':
        multipltime5 = 1
    elif minsec5[0] == 'minutes':
        multipltime5 = 60

    force5 = (mass5 * multiplmass5) * accel5
    # print('force=''%fN' %force5)
    print(f'Force={Qty(force5)}N')
    dist5 = nr5 * multipldist5

    work5 = force5 * dist5
    # print('work=', work5)
    print(f'Work={Qty(work5)}N/s')
    time5 = nr5 * multipltime5

    power5 = work5 / time5
    print('power=', power5)

    print(f'power={Qty(power5)}J/s = {Qty(power5)}W')

    result_5 = [hint_list, force5, work5, power5]

    return result_5
