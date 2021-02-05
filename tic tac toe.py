import random, sys

matx = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]

cases = [[1,2,3],[4,5,6],[7,8,9],
             [1,4,7],[2,5,8],[3,6,9],
             [1,5,9],[3,5,7]]

botsym ,mansym = '0', 'X'
previous_choices =[]
manc , botc = [] , []
win = []

def check(con):
    for i in range(0,len(con),2):
        manc.append(con[i])       
    for i in range(1,len(con),2):
        botc.append(con[i])       

     #for man conditions   
    for case in cases:
        count =0
        for no in case:
            if no in manc:
                count +=1
            else:
                break
        if count ==3:
            win.append(mansym)  
            break

     #for bot conditions   
    for case in cases:
        count =0
        for no in case:
            if no in botc:
                count +=1
            else:
                break
        if count ==3:
            win.append(botsym)  
            break

    #finally giving appreciations
    if (len(win)==0) and (len(previous_choices)==9):
        print('game is draw')
        return True
    elif (win !=[]):
        if win[0]==mansym:
            print('CONGO you win')
            return True
        elif win[0]==botsym:
            print('bot win')
            return True
    else:
        return False


def move(choice,player):
    if player =='bot':
        value = botsym
    if player =='man':
        value = mansym
        
    if choice ==1:
        matx[0][0] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    elif choice ==2:
        matx[0][1] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    elif choice ==3:
        matx[0][2] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    elif choice ==4:
        matx[1][0] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    elif choice ==5:
        matx[1][1] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    elif choice ==6:
        matx[1][2] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    elif choice ==7:
        matx[2][0] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    elif choice ==8:
        matx[2][1] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    elif choice ==9:
        matx[2][2] = value
        print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
    


def bot():
    bot_choice= random.randint(1,9)
    if (bot_choice not in previous_choices) and (bot_choice<10 and bot_choice>0) and (len(previous_choices)<10)  and (not check(previous_choices)):
        previous_choices.append(bot_choice)
        move(bot_choice,'bot')
        check(previous_choices)
        print('bot finished its move\n')
    elif (check(previous_choices)):
        sys.exit()
    else:
        bot()
    

def man():
    choice = int(input('enter a no as per the boxno'))
    if (choice not in previous_choices) and (choice<10 and choice>0) and (len(previous_choices)<10) and (not check(previous_choices)):
        previous_choices.append(choice)
        move(choice,'man')
        check(previous_choices)
        bot()
    elif (check(previous_choices)):
        sys.exit()
    else:
        man()

print(matx[0],'\n',matx[1],'\n',matx[2],'\n')
try:
    for i in range(5):    
            man()
except:
    RecursionError
