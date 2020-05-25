def candidate(arr):
    li=[]
    for i in arr:
        li.append(arr[i])
    max_value = max(li)
    name=[]
    for i in arr:
        if arr[i]==max_value:
            name.append(i)
    print(name)

    small=name[0]
    for i in range(0, len(name)):
        if len(small)>len(name[i]):
            small=name[i]
    print(small)



dic = {"Rahul":3,"G!2m0":9,"Mayank":12,"Priyank":5,"Rishi":2,"Chandani":5,"Rani":5}
candidate(dic)
