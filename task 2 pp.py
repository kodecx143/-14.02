data=[]
x=198
while x>0:
    s=input().split("\t")
    data.append(s)
    x-=1
def rate(elem,sp):# функция, считающая рейтинг каждой песни, elem - прослушивания 1 песни, sp=data
    rate1=len(sp)
    rate2=len(sp)
    for i in range(rate1):
        if elem>sp[i][0]:
            rate2-=1
    return rate2
sp_rates=[]
def result(d1,d2):
    d1=int(d1)
    d2=int(d2)
    if d1>d2:
        return 1
    elif d2>d1:
        return -1
    return 0
def comp_dates(date1,date2):# сравнивает 2 даты по числу, месяцу и году
    d1=date1.split(".")
    d2=date2.split(".")
    for i in range(2,-1,-1):
        if result(d1[i],d2[i])!=0:
            return result(d1[i],d2[i])
    return 0
for line in data:#добавляет рейтинг i-ого элемента в список
    sp_rates.append(rate(line[0],data))
for i in range(len(data)):
    data[i][1],data[i][2]=data[i][2],data[i][1]
    data[i][0]=sp_rates[i]
sp_dates=[]
count=0
#считаем, ск-ко дат меньше и больше нашей
for i in range(len(data)):
    line=data[i]
    for j in range(len(data)):
        line1=data[j]
        if comp_dates(line[3],line1[3])==1:
            count+=1
        sp_dates.append(count)
#сортируем по кло-ву дат, меньше нашей
for i in range(len(data)):
    for j in range(i+1,len(data)):   
        if sp_dates[i]>sp_dates[j]:
            data[i],data[j]=data[j],data[i]
print(data)

            
    
    
    



