a=input('enter any string')
j=0

while((j)<len(a)):
    i=0
    while(i<=j):
        if(a[i-1]==a[j] and i!=0):                   #comparing with each element
            a=a[:j]+a[j+1:]                          #taking off the repeated value

            j=j-1
            break;
        i=i+1
    j=j+1
print(a)