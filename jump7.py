for a in range(1,101):
    if(a<7):
        print(a)
    elif((a%7==0)or(a%10==7)or(a//10==7)):
        continue
    else:
        print(a)
