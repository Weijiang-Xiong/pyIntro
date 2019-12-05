from random import randrange

coinUser, coinBot = 10, 10 # 可以用一个赋值符号分别为多个变量赋值
roundOfGames = 0

def bet(dice, wager):
    '''[summary]
    
    Arguments:
        dice {[int]} -- [随机产生的一个数字]
        wager {[char]} -- [b大,s小,q退出 三选一]
    
    Returns:
        [none] -- [no return value is provided]
    '''
    if dice == 7:
        print(f'The dice is {dice};\nDRAW!\n') # \n 是换行符号
        return 0
    elif dice < 7:
        if wager == 's':
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1
        else:
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
    elif dice > 7:
        if wager == 's':
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
        else:
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1
            
while True:         #  除 for 之外的另外一个循环语句
    print(f'You: {coinUser}\t Bot: {coinBot}')
    dice = randrange(2, 13)   # 生成一个 2 到 12 的随机数
    wager = input("What's your bet? ")
    if wager == 'q':
        break 
    elif wager in 'bs':  # 只有当用户输入的是 b 或者 s 得时候，才“掷骰子”……
        result = bet(dice, wager)
        coinUser += result    # coinUser += result 相当于 coinUser = coinUser + result
        coinBot -= result
        roundOfGames += 1
    if coinUser == 0:
        print("Woops, you've LOST ALL, and game over!")
        break
    elif coinBot == 0:
        print("Woops, the robot's LOST ALL, and game over!")
        break
   
print(f"You've played {roundOfGames} rounds.\n")
print(f"You have {coinUser} coins now.\nBye!")