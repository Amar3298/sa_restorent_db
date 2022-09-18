a = "TimisplayinginthehouseofTimwiththetoysofTim"
a1 = "Tim"

def secretInfo(string,terroristName):
    a = string
    a1 = terroristName
    loopa = len(a1)
    count = 0
    for i in range(len(a)):
        result = a[i:i+loopa]
        result = result.lower()
        if(result==a1.lower()):
            count+=1
    return count

print(secretInfo(a,a1))