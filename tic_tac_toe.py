def arrange(a,b,c):#a=list,b=symbol,c=position
    a[c]=b
    print(f"{a[1]}|{a[2]}|{a[3]}")
    print(f"{a[4]}|{a[5]}|{a[6]}")
    print(f"{a[7]}|{a[8]}|{a[9]}")

def play(n,m,l):#n=board,m=symbol,l=player number
    a=0
    x=[]
    while(a<9):
        b=int(input(f"Player{l}, enter your position(1-9):{m} "))
        if b>9 or b<1:
            print("ERROR!! Position value should be between 1-9, enter again: ")
            continue
        if b in x:
            print("ERROR!! Position already taken, enter some other position: ")
            continue
        x.append(b)
        arrange(n,m,b)#n=board,m=symbol,b=position
        if n[1] == n[2] == n[3] == m or n[4] == n[5] == n[6] == m or n[7] == n[8] == n[9] == m or n[1] == n[4] == n[
            7] == m or n[2] == n[5] ==n[8] == m or n[3] == n[6] == n[9] == m or n[3] == n[5] == n[7] == m or n[1] == n[
            5] == n[9] == m:
            print(f"CONGRATULATIONS player {l} YOU WIN!!!")
            c=input("DO YOU WANT TO PLAY AGAIN:(Y/N)")
            if c=='Y':
                print("The game has been restarted")
                symbol()
            else:
                break
        if(l==1):
            l=2
        else:
            l=1
        if(m=='X'):
            m='O'
        else:
            m='X'
        if(a==8):
            print("game drawn")
            c = input("DO YOU WANT TO PLAY AGAIN:(Y/N)")
            if c == 'Y':
                print("The game has been restarted")
                symbol()
        a+=1

def symbol():
    while 1:
        board=["_","_","_","_","_","_","_","_","_","_"]
        x1=['X','O']
        a=(input("Player 1 : Choose your Symbol-(X/O)")).upper()
        if a not in x1:
            print("ERROR!! Choose the correct symbol")
            continue
        else:
            if a=='X':
                b='O'
            else:
                b='X'
            print("Player 1 Symbol: "+a)
            print("Player 2 Symbol: "+b)
            break

    while 1:
        x2 = ['Y', 'N']
        c=(input("Player 1, do you want to go first?(Y/N)")).upper()
        if c not in x2:
            print("ERROR!! Choose the correct symbol")
            continue
        else:
            if c=='Y':
                print("Player 1 will go first")
                player=1
                play(board,a,player)
            else:
                print("Player 2 will go first")
                player=2
                play(board,b,player)
        break

print("*****_WELCOME to TIC TAC TOE_*****")
print("The board with the positions is as follows:")
print("1|2|3")
print("4|5|6")
print("7|8|9")
symbol()