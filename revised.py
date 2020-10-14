def Checker(enput):
    StackTemp = []
    for i in enput:
        if len(StackTemp) != 0:
            if i != StackTemp[-1][0] and StackTemp[-1][1] > 2:
                StackTemp.pop()
                if len(StackTemp) != 0:
                    if StackTemp[-1][0] == i:
                        Temp = StackTemp[-1][1]
                        StackTemp.pop()
                        StackTemp.append([i,Temp+1])
                    else:
                        StackTemp.append([i,1])
                else:
                    StackTemp.append([i,1])
            elif i != StackTemp[-1][0]:
                StackTemp.append([i, 1])
            else:
                Temp = StackTemp[-1][1]
                StackTemp.pop()
                StackTemp.append([i,Temp+1])
        else:
            StackTemp.append([i,1])

        print(StackTemp)
    finish = ''
    for i in range(0,len(StackTemp)):
        finish = finish + (StackTemp[i][0] * StackTemp[i][1])
        
    return(finish)

print(Checker('abbbaac'))


            
            
