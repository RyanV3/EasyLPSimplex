import math

#makes list of data for tableau
def makeDataList(splitDataList, minMaxData, varNum, constraintNum):
    for i in range(len(minMaxData)):
        minMaxData[i] = (minMaxData[i]*(-1))

    minMaxData.append(0)
    

    regDataList = minMaxData + splitDataList
    for i in range(0, len(regDataList)+constraintNum, varNum+2):
        if i == 0:
            regDataList.insert(i, 1)
        else:
            regDataList.insert(i, 0)

    count = constraintNum
    for i in range(varNum+1, len(regDataList)+(constraintNum*(constraintNum+1)), (constraintNum+varNum+2)):
        for j in range(constraintNum):
            if j == count:
              regDataList.insert(i, 1)
            else:
              regDataList.insert(i, 0)
        count = count-1

    print(regDataList)
    return regDataList

#creates matrix
def createMatrix(rowCount, colCount, dataList):
    matrix = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[colCount * i + j])

        matrix.append(rowList)

    return matrix

#transforms matrix
def matrixTrans(constraintNum, matrix):
    #find E-Variable and L-Variable
    EVarCol = matrix[0].index(min(matrix[0]))
    EVarName = 'x' + str(EVarCol)
    RHSRatios = []
    for i in range(1, constraintNum):
        RHSRatios.append((matrix[i][-1])/(matrix[i][EVarCol]))

    for i in range(RHSRatios):
        if min(RHSRatios) <= 0:
            RHSRatios.remove(min(RHSRatios))

    LVarRow = RHSRatios.index(min(RHSRatios))+1
    LVarName = 's' + str(LVarRow)

    #devide pivot row by pivot element
    for i in matrix[LVarRow]:
        matrix[LVarRow][i] = matrix[LVarRow][i]/matrix[LVarRow][EVarCol]

    #New Row = (Current row ) − (Its pivot column coeff) x ( New pivot row)
    for i in range(constraintNum+1):
        if i != LVarRow:
            for j in matrix[i]:
                matrix[i][j] = matrix[i][j] - (matrix[i][EVarCol]*matrix[LVarRow][j])

    print(matrix)
    print('entering variable=' + EVarCol)
    print('leaving variable=' + LVarRow)
    return matrix

def Main():
    constraintNum = int(input("Enter the number of constraints: "))
    varNum = int(input("Enter the number of variables the problem is defined on: "))
    minOrMax = (input("Is the objective function to be maximized or minimized?"))
    rawMinMaxData = (input("Enter the coefficients of the min/max function variables(maximize z = 5 -4 format: 5 -4): "))
    minMaxData = list(map(int, rawMinMaxData.split()))
    rawDataList = (input("Enter the coefficients of the constraints(format: 6 4 24 1 2 6 -1 1 1 0 1 2): "))
    splitDataList = list(map(int, rawDataList.split()))

    finalDataList = makeDataList(splitDataList, minMaxData, varNum, constraintNum)
    initMatrix = createMatrix((constraintNum+1), (constraintNum+varNum+2), finalDataList)

    print(initMatrix)

    for i in range(constraintNum-1):
        initMatrix = matrixTrans(constraintNum, initMatrix)


Main()