# Multiple levels of basic math to help a second grader with their basic math

#starts with level 1, basic math, advances to addition, subtraction, multiples of addition/ subtraction
#every 25 correct, advance a level
# skip to next level if get 10 right in a row
# q to quit

#TODO:
#remove recursion in levels 7-10
#add multiplication tutorial level 10
#add number tracking
#add loop in main so program does not exit after one question

import math
import string
import random

#Globals
#level = 0
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
    print(f"Level 9 is adding and subtracting multiple numbers less than 1000.")
    print(f"Level 10 is showing addition and multiplying two numbers less than 10.")

def makeMath(level):# -> tuple[int, list, list]:
    working_nums = 2
    answer = 0
    m = []
    seq = []
    #Level 1 is adding two numbers less than 10.
    if level == 1:
        working_nums = 2
        for _ in range(0, working_nums):
            m.append(random.randint(0,10))
        for _ in range(0, working_nums-1):
            seq.append("+")
        for a in m:
            answer += a
    #Level 2 is adding two numbers less than 100.
    elif level == 2:
        working_nums = 2
        for _ in range(0, working_nums):
            m.append(random.randint(0,100))
        for _ in range(0, working_nums-1):
            seq.append("+")
        for a in m:
            answer += a
    #Level 3 is adding multiple numbers less than 100.
    elif level == 3:
        working_nums = random.randint(2,8)
        for _ in range(0, working_nums):
            m.append(random.randint(0,100))
        for _ in range(0, working_nums-1):
            seq.append("+")
        for a in m:
            answer += a
    #Level 4 is subtracting two numbers less than 10.
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
    #Level 5 is subtracting two numbers less than 100.
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
    #Level 6 is subtracting multiple numbers less than 100.
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
            m[0] += -1*answer + random.randint(1,100)
            answer = m[0]
            for a in m:
                if a == m[0]:
                    pass
                else:
                    answer -= a
    #Level 7 is adding and subtracting three numbers less than 10.
    elif level == 7:
        working_nums = 3
        for _ in range(0, working_nums):
            m.append(random.randint(0,10))
        partialSort(m)
        answer = m[0]
        for _ in range(0, working_nums-1):
            if random.randint(0,1) == 0:
                seq.append("+")
                answer += m[_]
            else:
                seq.append("-")
                answer -= m[_]
        if answer < 0:
            m[0] + -1*answer + random.randint(0,5)
            #TODO:  fix this so m[0] is never > 10
    #Level 8 is adding and subtracting three numbers less than 100.
    elif level == 8:
        working_nums = 3
        for _ in range(0, working_nums):
            m.append(random.randint(0,100))
        partialSort(m)
        answer = m[0]
        for _ in range(0, working_nums-1):
            if random.randint(0,1) == 0:
                seq.append("+")
                answer += m[_]
            else:
                seq.append("-")
                answer -= m[_]
        if answer < 0:
            m[0] + -1*answer + random.randint(0,25)
            #TODO:  fix this so m[0] is never > 100
    #Level 9 is adding and subtracting multiple numbers less than 1000.
    elif level == 9:
        working_nums = 3
        for _ in range(0, working_nums):
            m.append(random.randint(0,1000))
        partialSort(m)
        answer = m[0]
        for _ in range(0, working_nums-1):
            if random.randint(0,1) == 0:
                seq.append("+")
                answer += m[_]
            else:
                seq.append("-")
                answer -= m[_]
        if answer < 0:
            m[0] + -1*answer + random.randint(0,250)
            #TODO:  fix this so m[0] is never > 1000
    #Level 10 is showing addition and multiplying two numbers less than 10.
    elif level == 10:
        working_nums = 2
        for _ in range(0, working_nums):
            m.append(random.randint(0,10))
        answer = m[0] * m[1]
        # for a in m:
        #     answer += a
    
    #TODO:  move the string creation from main into here, return answer [int], ansStr [string]
    #for level 10, ansStr should be of the form m[0] * m[1] = m[0] + m[0] + ... = 
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