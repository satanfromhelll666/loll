def id_check():

    a = input()
    b = len(a)

    arr = []

    for i in range(0,b):
        temp = int(a[i])
        arr.append(temp)    

    #print(arr[8])

    if(b==9):
        if(arr[0]==0 and arr[1]==1 and arr[2]==1):
            if(arr[3]==0 or arr[3]==1 and arr[4]<=0 or arr[4] >=9 ):
                if(arr[5]==1 and arr[5]==2 and arr[5]==3):
                    if(arr[6]!=0 and arr[7]!=0 and arr[8]!=0):
                        print('accepted')
                        return

    print('rejected')

    
id_check()
    
