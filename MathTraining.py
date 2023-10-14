# G. Stangler
# 14 Mar 2023
# Ken math training
# Multiple levels of basic math to help Ken

#starts with level 1, basic math, advances to addition, subtraction, multiples of addition/ subtraction
#every 25 correct, advance a level
# skip to next level if get 10 right in a row
# q to quit

import math
import string
import random

#Globals
level = 0
MAX_LEVEL = 7
MIN_LEVEL = 1

def help():
    print(f"Level 1 is adding two numbers less than 10.")
    print(f"Level 2 is adding two numbers less than 100.")
    print(f"Level 3 is adding multiple numbers less than 100.")
    print(f"Level 4 is subtracting two numbers less than 10.")
    print(f"Level 5 is subtracting two numbers less than 100.")
    print(f"Level 6 is subtracting multiple numbers less than 100.")
    print(f"Level 7 is adding and subtracting three numbers less than 10.")
    print(f"Level 8 is adding and subtracting three numbers less than 100.")
    print(f"Level 9 is adding and subtracting multiple numbers less than 100.")
    print(f"Level 10 is adding and subtracting multiple numbers less than 100.")

def makeMath(level, recursionDepth=0):# -> tuple[int, list, list]:
    working_nums = 2
    answer = 0
    m = []
    seq = []
    if level == 1:
        working_nums = 2
        for _ in range(0, working_nums):
            m.append(random.randint(0,10))
        for _ in range(0, working_nums-1):
            seq.append("+")
        for a in m:
            answer += a
    elif level == 2:
        working_nums = 2
        for _ in range(0, working_nums):
            m.append(random.randint(0,100))
        for _ in range(0, working_nums-1):
            seq.append("+")
        for a in m:
            answer += a
    elif level == 3:
        working_nums = random.randint(2,8)
        for _ in range(0, working_nums):
            m.append(random.randint(0,100))
        for _ in range(0, working_nums-1):
            seq.append("+")
        for a in m:
            answer += a
    elif level == 4:
        working_nums = 2
        for _ in range(0, working_nums):
            m.append(random.randint(0,10))
        m.sort(reverse=True)
        for _ in range(0, working_nums-1):
            seq.append("-")
        answer = m[0]
        for a in m:
            if a == m[0]:
                pass
            else:
                answer -= a
    elif level == 5:
        working_nums = 2
        for _ in range(0, working_nums):
            m.append(random.randint(0,100))
        m.sort(reverse=True)
        for _ in range(0, working_nums-1):
            seq.append("-")
        answer = m[0]
        for a in m:
            if a == m[0]:
                pass
            else:
                answer -= a
    elif level == 6:
        working_nums = random.randint(2,8)
        for _ in range(0, working_nums):
            m.append(random.randint(0,100))
        m.sort(reverse=True)
        for _ in range(0, working_nums-1):
            seq.append("-")
        answer = m[0]
        for a in m:
            if a == m[0]:
                pass
            else:
                answer -= a
        if answer < 0:
            recursionDepth += 1
            if recursionDepth < 10:
                answer, m, seq = makeMath(level, recursionDepth)
            else:
                print(f"Level 6 maximum recursion reached.")
                answer, m, seq = makeMath(5, 0)
    elif level == 7:
        working_nums = random.randint(2,8)
        for _ in range(0, working_nums):
            m.append(random.randint(0,100))
        m.sort(reverse=True)
        for _ in range(0, working_nums-1):

            seq.append("-")
        answer = m[0]
        for a in m:
            if a == m[0]:
                pass
            else:
                answer -= a
        if answer < 0:
            recursionDepth += 1
            if recursionDepth < 10:
                answer, m, seq = makeMath(level, recursionDepth)
            else:
                print(f"Level 7 maximum recursion reached.")
                answer, m, seq = makeMath(3, 0)
    elif level == 8:
        pass
        # working_nums = 2
        # for _ in range(0, working_nums):
        #     m.append(random.randint(0,10))
        # for a in m:
        #     answer += a
    elif level == 9:
        pass
        # working_nums = 2
        # for _ in range(0, working_nums):
        #     m.append(random.randint(0,10))
        # for a in m:
        #     answer += a
    elif level == 10:
        pass
        # working_nums = 2
        # for _ in range(0, working_nums):
        #     m.append(random.randint(0,10))
        # for a in m:
        #     answer += a
    
    return answer, m, seq


def fullSort(numList):
    return numList.sort(reversed=True)

def partialSort(Q):
    #Q[0], Q.index(max(Q)) = Q.index(max(Q)), Q[0]
    a = Q.index(max(Q))
    Q[0], Q[a] = Q[a], Q[0]
    return Q

def stats():
    pass

def main() -> int:
    level = input(f"Input your starting level (currently supports {MIN_LEVEL} - {MAX_LEVEL} only), h for help, q for quit.")
    try:
        if level.upper() == 'Q':
            stats()
            return 0
        elif level.upper() == 'H':
            help()
        else:        
            level = int(level)
    except Exception as e:
        print(f"Bad input, level should be a number between {MIN_LEVEL} and {MAX_LEVEL}, or q to quit")
        print(f"Exception thrown is str{e}")
        return 0

    if (level < 1) or (level > 10):
        print("Unsupported level")
    else:
        answer, problemNumbers, symbols = makeMath(level)
        ansStr = ''
        for m in range(0,len(symbols)):
            ansStr += f"{problemNumbers[m]} {symbols[m]} "
        ansStr += f'{problemNumbers[-1]} = '
        inputtedAnswer = input(ansStr)

        if inputtedAnswer.upper() == 'Q':
            print ("Exiting.")
            stats()
            return 0
        inputtedAnswer = int(inputtedAnswer)
        if (inputtedAnswer == answer):
            print ("Correct!")
        else:
            print (f"The answer I got is {answer}")


#    while True:
#        pass

if __name__ == "__main__":
    main()