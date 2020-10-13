def CandyCrush(enput):
    ComparisonSTR1 = enput
    ComparisonSTR2 = ''

    def Checker(enput):
        StackTemp = []
        temp1 = 1
        for i in enput:
            temp2 = temp1
            temp1 = i
            if temp1 != temp2:
                if len(StackTemp) != 0:
                    tempX = StackTemp[len(StackTemp)-1][1]
                    if tempX > 2:
                        StackTemp.pop()
                StackTemp.append([i,1])
            elif temp1 == temp2:
                tempX = StackTemp[len(StackTemp)-1][1]
                StackTemp.pop()
                StackTemp.append([i,tempX+1])
        if StackTemp[len(StackTemp)-1][1] >2:
            StackTemp.pop()
        finish = ''
        for i in range(0,len(StackTemp)):
            finish = finish + (StackTemp[i][0] * StackTemp[i][1])

        return(finish)

    while ComparisonSTR1 != ComparisonSTR2 and len(ComparisonSTR1) != 0:
        ComparisonSTR2 = ComparisonSTR1
        ComparisonSTR1 = Checker(ComparisonSTR1)

    return(ComparisonSTR1)

print(CandyCrush('abbbaaccbbbbc'))


            
            
