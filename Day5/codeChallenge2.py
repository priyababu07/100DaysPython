l1=[]
flag=0
limit = int(input("Enter the limit"))
for i in range(limit):
    score = int(input("Enter your score"))
    l1.append(score)


# maximum_score = max(l1)

#OR
maximum_score=0
for i in l1:
    
    if i>maximum_score:
     maximum_score=i 
print(f"The maximum score is {maximum_score}")