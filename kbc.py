quetions=[
    ["who is prime minister of india ? ", "modi Ji", "gandu", "yogi ji", "you",1],
   
    ["who is smartest person in room ? ", "you ", "laptop", "arvind", "none",2],
    ["which is best village ? ", "toranwada", "bhatepuri", "undri", "pala",1],
    ["who is most kind hearted person ? ", "lahu", "arvind", "none", "you",1],
    ["who will be next modi ? ", "n gadakari", "A shah", "yogi ji", "none",1],
    ["who will be prime minister of india ? ", "modi Ji", "gandu", "yogi ji", "you",1],
    ["who is prime minister of india ? ", "modi Ji", "gandu", "yogi ji", "you",1]
]
levels=[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,640000]
money=0
for i in range(0,len(quetions)):
    
    quetion=quetions[i]
   
    print(f"\nfor RS.{levels[i]}")
    print(f"your quetion is {quetion[0]}")
    print(f"1.{quetion[1]}      3.{quetion[3]}")
    print(f"2.{quetion[2]}      4.{quetion[4]}")
    reply=int(input("enter your answer (1-4)or 0 to quit:\n"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==quetion[-1]):
        print(f"correct answer you have won {levels[i]}")
        if(8>=i>= 4):
            money = 10000
        elif(14>=i >= 9):
            money = 320000
        elif(i >= 14):
            money = 10000000
        else:
            money=0
    else:
        print("Wrong answer!")
        break 
print(f"you won {money}Rs")