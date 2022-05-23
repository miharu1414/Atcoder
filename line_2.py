import sys


def amount(size):
    if size == 'S':
        return 300
    elif size == 'M':
        return 500
    else:
        return 700

def standard_main(argv):
    # 1行目
    x = int(input())

    # 2行目
    if x != 1:
        n,m,s,t = map(int,input().split())
    ## 応用実装用の入力
    else:
        n,m,s,t,k = map(int,input().split())

    # 3行目
    drink_name = list(map(str,input().split()))
    drink_judge = set(drink_name)

    # 4行目以降
    query = []
    try:
        while True:
            Q = input()
            query.append(Q)
    except EOFError:
        pass
    
    drink =[]
    num =[]
    size =[]
    time =[]

    Num_judge = set()


    use= 1
    left = s
    que = []
    # 処理
    left_que = []
    i = 0
    while 1:

        
                      
        if len(query) <= i:
            break

        while not "complete" in query[i]:
            use = 0
            que.append(query[i])
            i+=1
        sagyo = []
        i+= 1
        
      
      
        if len(left_que) == 0:
            Num, Drink ,Size, Time = que[0].split()
            del que[0]

            if Drink not in drink_judge:
                print(f"ERROR: item named {Drink} does not exist.")

            elif Num in Num_judge:
                print("ERROR: reference number duplicates.")
            else:
                ml = amount(Size)
                Num_judge.add(Num)
                sagyou =[Num]
                print(f"make: 1 {Drink} {ml}")
            left_que = que
            continue

        else:
            que = left_que + que
            for j in range(len(que)):
                Num, Drink ,Size, Time = que[j].split()

                if Drink not in drink_judge:
                    print(f"ERROR: item named {Drink} does not exist.")

                elif Num in Num_judge:
                    print("ERROR: reference number duplicates.")

                elif len(sagyou) == 0:
                    left = s - amount(Size)
                    Num_judge.add(Num)
                    name_drink = drink
                    sagyou = [Num]

                elif len(sagyou) != 0 and Drink == name_drink and left>=amount(Size):
                    left -= amount(Size)
                    Num_judge.add(Num)
                    sagyou.append(Num)

                else:
                    left_que.append(que[j])
            ml = s - left
            print(print(f"make: 1 {name_drink} {ml}"))
        print("serve to:",*sagyo)
        

if __name__ == '__main__':
    standard_main(sys.argv[1:])

