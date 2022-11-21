
# assignment 2 ques 1
# using for loop and a sample list.
list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for j in range (1,len(list)):
    for i in range(len(list)-j):
        if list[i][1]>list[i+1][1]:
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp
for i in range(len(list)):
    print(list[i],end=' ')


# assignment 2 ques 2
#using chr builtin 
dict={}
for i in range(97,123):
    dict[chr(i)]=i
print(dict)




