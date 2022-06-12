import random
def play():
    user =input("What's your choice? ('r'for rock,'p'for paper,'s' for scissors) : ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return '*******************************************************************\nIt\'s a tie'

    elif who_is_win(user,computer):
        return'*******************************************************************\nCongrats, You won!'

    return'*******************************************************************\nOh, You lost!\n'
def who_is_win(player,opponent):

   #return true if player wins

   # r>s, s>p, p>r

    if (player =='r'and opponent =='s') or (player =='s'and opponent == 'p') or (player == 'p' and opponent =='r'):
        return True

print(play())