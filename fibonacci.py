x=0
y=1
n=0
i=3
while(1==1):
    n=eval(input('Enter Number Of Terms: '))
    if n==0:
        print("Not Valid..Try Again\n")
    else:
        break
print('Here Is The Fibonacci Series: \n')
if n==1:
    print(x)
elif n==2:
    print(x,y)
else:
    print(x,y,end=' ')
    while(i<=n):
        print(x+y,end=' ')
        if i%2!=0:
            x=(x+y)
            i+=1
        else:
            y=(x+y)
            i+=1
