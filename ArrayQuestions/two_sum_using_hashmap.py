def twosum(arr, arr_size, sum):
    hashmap={}

    for i in range(0 , arr_size):
        temp=sum-arr[i]
        if(temp in hashmap):
            print("yes")
            return
        hashmap[arr[i]]=i
    print("no")

arr=[1,2,3,4,5,6]
n=8
twosum(arr,len(arr),n)
