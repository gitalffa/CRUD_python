import random



if __name__ =='__main__':
    data = [random.randint(0,100) for i in range(10)]

    data.sort()
    low=0
    high=len(data)-1
    print(data)
    target=int(input('What number would you like to find?'))
    mid=(low+high)//2
    while target!=data[mid]:
        if target == data[mid]:
            print('True')
        elif target<data[mid]:
            high=mid-1
            mid=(low+high)//2
            if target == data[mid]:
                print('True')
            elif mid==0 and target!=data[mid]:
                print('False')
                break
        else:
            low=mid+1
            mid=(low+high)//2
            if target == data[mid]:
                print('True')
            elif mid==len(data)-1 and target!=data[mid]:
                print('False')
                break
