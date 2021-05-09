import random
import re
import time

from quantiphy import Quantity as Qty


# ssssssss


def converted(a):
    # check if a, the INPUT STRING, is a (float)number OR any other string(non-number)
    # if it is a string, return False
    # for number return True

    try:
        number = float(a)
        # if (type(number) in (int, float)):
        if isinstance(number, float):
            # TODO also check if number isn't big/small enough not to fit in a float
            print(type(number))
            return number
    except ValueError as my_except:  # or is it TypeError
        # print('My exception:', my_except, type(my_except))
        # print("It is possible that the number is not a float")
        return False
    except Exception as e:
        print('Exception:', e)
        print('some other exception rise in conversion str to float')
        return False
# problem 5
def problem5():

    hint_list = ['Formula for force', 'Formula for work', 'Formula for power']
    mass5 = random.randint(2, 15)
    multiplier_mass5 = ["grams", "kilograms", "tons"]
    multiplier_time5=['seconds', 'minutes']
    multiplier_dist5=['meters', 'kilometers']
    pm5 = random.choices(multiplier_mass5, weights=[2, 3, 1], k=1)
    md5 = random.choices(multiplier_dist5, weights=[1, 2], k=1)
    nr51 = random.randint(1, 100)
    nr5=random.randint(1, 60)
    minsec5 = random.choices(multiplier_time5, weights=[1, 2], k=1)

    problem5 = f'\n Problem5: A mass of {mass5} {pm5[0]} is to be raised to a height of {nr5} {md5[0]} in {nr51} {minsec5[0]}. ' \
             f'What work needs to be done and what is the power is necessary for thi action?'
    print(10*'_', problem5)

    multiplmass5 = 1
    multipldist5 = 1
    multipltime5 = 1
    accel5 = 9.81

    if pm5[0] == 'grams':
        multiplmass5 = 10**-3
    elif pm5[0] == 'kilograms':
        multiplmass5 = 10**0
    elif pm5[0] == 'tons':
        multiplmass5 = 10**3

    if md5[0] == 'meters':
        multipldist5 = 10 ** 0
    elif md5[0] == 'kilometers':
        multipldist5 = 10 ** 3

    if minsec5[0] == 'seconds':
        multipltime5 = 1
    elif minsec5[0] == 'minutes':
        multipltime5 = 60

    force5 = (mass5*multiplmass5)*accel5
    #print('force=''%fN' %force5)
    print(f'Force={Qty(force5)}N')
    dist5 = nr5*multipldist5

    work5 = force5*dist5
    #print('work=', work5)
    print(f'Work={Qty(work5)}N/s')
    time5 = nr5*multipltime5

    power5 = work5/time5
    print('power=', power5)

    print(f'power={Qty(power5)}J/s = {Qty(power5)}W')

    result_5 = [hint_list, force5, work5, power5]

    return result_5

# problem4
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

# ############ Game START
# Force the problem chosen to be a particular one
#prbl_list=('problem4()', 'problem4()')
prbl_list=('problem5()', 'problem5()')

# the real list, to be updated with other problems
# prbl_list=('problem4()', 'problem5()')


# todo: to fix: number of points (sa fie) > number of hints, sa fie din ce scadea si sa si ramana ceva
# todo: create the pages for action codes, main, settings etc
# todo: create so that books and chapters can be selected via gui;
# which problems will be in the pool f probable current game prblms

def start_game(prbl_list):

    # chose randomly(for now) a prbl from the list of problems
    # later you can implement the ratio of each problem to be chosen
    chosen_problem = random.choice(prbl_list)

    # name&score; but score not implemented yet?
    player = {'name': 'Nobody', 'alt': 10}

    print('----' * 10)

    print('Enter player name:')
    player['name'] = input()
    print('----' * 10)

    new_round = True
    counter = 0
    points = 0
    print(f'%s, here\'s the first problem:' % player['name'])
    first_execution_ret = eval(chosen_problem)

    #print('\nxxxxxxxx',first_execution_ret)
    # for now i input directly nr of hints but
    # this needs to be changed to the returned value of the problem
    hint_list = first_execution_ret[0]
    number_of_hints = len(hint_list)
    max_points = 10 * number_of_hints
    #hint_list = ['Work=Force(N)*distance(m)', 'Work=Force(N)*distance(m)']

    while new_round:
        work = 10 # this var needs to contain the calculated answer as a float
        # TODO: change work with problems value ;work is a mock up number to check if probl works \
        # in the code check if number AND extension(exkNM) match or if the num isn't shortened version (no k)
        points_inc = 0
        print(20 * '_')  # spacer text to look nicer

        # get the input h,q or number
        itr = 0
        while True:
            input_str = input("\nType q to quit. \nH for a hint or \n\033[1mInput your answer:\033[0m\n")

            # check if input is q/quit OR if user wants hints
            # check if input is a good number if False continue to ask for a input number not a string
            # if it is a usable number check if its the good answer to the problem

            m = converted(input_str)

            if input_str == 'q':
                print('you selected \'quit\'. Bye!')
                print('\nYour exiting points are %d, made in %d rounds,' % (points, counter))
                exit()
            elif input_str == 'h':
                if itr < number_of_hints:
                    print('Your hint nr', itr + 1, ' is: ', hint_list[itr], '. It consts you -5 points ')
                    print(10 * '-')
                    points_inc += -5
                    print("out of", max_points, ", you lost", abs(points_inc), 'points')
                    itr += 1

                else:
                    print('No more hints for you :(')
                    print(10 * '-')

            elif m == False:
                print(input_str, 'input is not number. Try again')
                continue
            else:
                # break outside infinite loop, the number input is good to be used
                # print('!!!!!!!!!!!!!!!input is a number!!!!!!')
                break


        # todo: check what re,compile and findall do and comment it stupido
        # re.compile: this regex would help you to find all the scientific notation in the text.

        match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
        curated_nr = [float(x) for x in re.findall(match_number, input_str)]

        #print('your curated answer is:', curated_nr[0])

        # if you calculated correctly score++
        if curated_nr[0] == work:
            print("\nCongrats, you got the right number")
            points_inc = points_inc + max_points
            points = points + points_inc
            counter += 1
            print("Way to go. You made %d points in %d rounds" % (points, counter))

            # you're right but do you want another round? get the answer
            inp = input('\nDo you want another round y/n?')
            if inp == 'n'or inp == "q":
                # exit te game loop
                new_round = False
            elif inp == 'y':
                print('\nNext problem:')
                eval(chosen_problem)
        # you're answer is wrong, but do you want another round? get the answer
        else:
            print('You got it wrong, right answer is:', work)
            counter += 1
            print('You made %d points in %d rounds' % (points, counter))
            inp = input('\nDo you want another round y/q?')

            # for 'n' break out of the game, any other keystroke continues with another round
            if inp == "n" or inp == "q":
                new_round = False
            elif inp == 'y':
                print('\nNew problem:')
                eval(chosen_problem)
            else:
                print('\nAnother problem:')
                eval(chosen_problem)

        print('\nYour exiting points are %d, made in %d rounds,' % (points, counter))

    # just wait a bit before exit, wait for the player to read his score on terminal

    time.sleep(2)

    # todo: check with real values(work); at first given not random nr, to test problem
    # shortify and comment the problem, there is to much (ugly)code


    # TODO: insert more problems in game, update list(tuple) of problems
    # todo: fix problem5 = don't show the results!
    #todo: set the hints/formulas


# asd asd
# bsd bsd

if __name__ == "__main__":
    start_game(prbl_list)
