from random import randint
from random import seed
from random import random
from random import choice
from textwrap import indent
import string
import sys

outputFile_Header = open('junkCodefile_header.txt','w')
outputFile_Cpp = open('junkCodefile_cpp.txt','w')

numClass = 0
numClassVariable = 0
numClassMethod = 0
numFunction = 0
numVariable = 0
numForLoop = 0
numWhileLoop = 0
numBranchStatement = 0

#################################
######### Get Inputs ############
#################################
#Valid for range in 0,1,2,3,4,5,6,7,8,9,10
#isdigit is automatically False since strings are empty initially
while True:
    try:
        numClass = int(input('Input number of classes (0 < Entered value <= 10): '))
        if numClass not in range(0,11):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numClassVariable = int(input('Input number of class variables (Required: 0 < Entered value < 10): '))
        if numClassVariable not in range(0,11):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()   

while True:
    try:
        numClassMethod = int(input('Input number of class methods (Required: 0 < Entered value <= 10): '))
        if numClassMethod not in range(0,11):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numFunction = int(input('Input number of functions (0 < Entered value < 10): Default is 1: '))
        if numFunction not in range(0,11):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numVariable = int(input('Input number of variables (0 < Entered value < 5): Default is 1: '))
        if numVariable not in range(0,6):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numForLoop = int(input('Input number of for loops (0 < Entered value < 5): Default is 1: '))
        if numForLoop not in range(0,6):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numWhileLoop = int(input('Input number of while loops (0 < Entered val1ue < 5): Default is 1: '))
        if numWhileLoop not in range(0,6):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numBranchStatement  = int(input('Input number of branch statement (0 < Entered value < 5): Default is 1: '))
        if numBranchStatement not in range(0,6):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

########################################
#########Create Junk name###############
########################################
def createRandomName(num):
    result = (choice(string.ascii_letters) for intNum in range(5))
    randName = ''
    for iter in result:
        randName += iter
    randName += str(randint(0,num*100))
    return randName

###############################################################
################# Create Function Return Types ################
###############################################################
def createFunctionReturnType(num):
    returnType = ('void','float','std::string','int')
    randValue = (num * 1337) % 4
    if randValue == 1:
        return returnType[1]
    elif randValue == 2:
        return returnType[2]
    elif randValue == 3:
        return returnType[3]
    else:
        return returnType[0]

#######################################################
########### Create Function Parameters ################
#######################################################
def createFunctionParameters(num):
    parameterType = ('int','float','std::string')

    functionParameterStr = ''
    functionParameterList = []
    counter = randint(0,num)
    while counter > 0:
        randValue = (counter * 1000) % 10
        if randValue == 0:
            val = parameterType[0] + '& '
            functionParameterStr += val
            functionParameterList.append(val)
        elif randValue == 1:
            val = 'const ' + parameterType[0] + '& '
            functionParameterStr += val
            functionParameterList.append(val)
        elif randValue == 2:
            val = parameterType[0] + '* '
            functionParameterStr += val
            functionParameterList.append(val)
        elif randValue == 3:
            val = parameterType[1] + '& '
            functionParameterStr += val
            functionParameterList.append(val)
        elif randValue == 4:
            val = 'const ' + parameterType[1] + '& '
            functionParameterStr += val 
            functionParameterList.append(val)
        elif randValue == 5:
            val = parameterType[1] + '* '
            functionParameterStr += val
            functionParameterList.append(val)
        elif randValue == 6:
            val = parameterType[2] + '& '
            functionParameterStr += val
            functionParameterList.append(val)
        elif randValue == 7:
            val = 'const ' + parameterType[2] + '& '
            functionParameterStr += val
            functionParameterList.append(val)
        elif randValue == 8:
            val = parameterType[2] + '* '
            functionParameterStr += val
            functionParameterList.append(val)
        varName = createRandomName(num)
        functionParameterList.append(varName)
        functionParameterStr += varName
        if counter != 1:
            functionParameterStr += ', '
        counter -= 1
    return functionParameterStr, functionParameterList

###############################################
######## Create function prototype ############
###############################################
#returnType is random number, where return value(s) will be different based on number given
#numParameter is random number, where return value(s) will be different based on number given
#Default is 0
def createFunctionPrototype(returnType = 0, numParameter = 0):
    paramStr = createFunctionParameters(numParameter)
    functionReturnStr = createFunctionReturnType(returnType)
    functionStr = functionReturnStr + ' ' + createRandomName(randint(0,99)) + '(' + paramStr[0] + ')'
    return functionStr, paramStr, functionReturnStr   

##################################################
######## Create for loop for function ############
##################################################
def createForLoop(numForLoop, functionDefinitionStr):
    if numForLoop == 0:
        return functionDefinitionStr
    else:
        functionDefinitionStr += 'for(int i = ' + str(randint(0,99)) + '; i<100; i++) {\n\tcontinue;\n}\n' 
        return createForLoop(numForLoop-1, functionDefinitionStr)
    
####################################################
######## Create while loop for function ############
####################################################
def createWhileLoop(numWhileLoop, functionDefinitionStr):
    if numWhileLoop == 0:
        return functionDefinitionStr
    else:
        randomCountName = createRandomName(numWhileLoop)
        functionDefinitionStr += 'int count_' + randomCountName + ' = ' + str(randint(0,50)) + ';\nwhile(count_' + randomCountName + '>0) {\n\tcount_' + randomCountName + '--;\n\tcontinue;\n}\n'
        return createForLoop(numWhileLoop-1, functionDefinitionStr)

###################################################
######## Create variables for function ############
###################################################
def createVariable(numVariable, functionDefinitionStr, varTypesTuple):
    if numVariable == 0:
        return functionDefinitionStr
    else:
        functionDefinitionStr += str(varTypesTuple[randint(0,4)]) + ' ' + createRandomName(numVariable) + ';\n'   
        return createVariable(numVariable-1, functionDefinitionStr, varTypesTuple) 

###########################################################
######## Create branch statements for function ############
###########################################################
def createBranchStatement(numBranchStatement, lengthOfParameterList, parameterList, functionDefinitionStr):
    branchStatementConditionVal_Num = str(randint(0,200))
    branchstatementConditionVal_Char = choice(string.ascii_letters)
    if lengthOfParameterList == 0:
        branchStatementName = createRandomName(numBranchStatement)
        if numBranchStatement % 5 == 0:
            functionDefinitionStr += 'if(' + 'int ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(int ' + branchStatementName + ' == ' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        elif numBranchStatement % 5 == 1:
            functionDefinitionStr += 'if(' + 'float ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + '.01) {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(float ' + branchStatementName + ' == ' + str(randint(100,199)) + '.02) {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        elif numBranchStatement % 5 == 2:
            functionDefinitionStr += 'if(' + 'std::string ' + branchStatementName + ' == junkStr_' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(std::string ' + branchStatementName + ' == ' + 'junkStr_' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        elif numBranchStatement % 5 == 3:
            functionDefinitionStr += 'if(' + 'double ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + '.03) {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(double ' + branchStatementName + ' == ' + 'junkStr_' + str(randint(100,199)) + '.03) {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        elif numBranchStatement % 5 == 4:
            functionDefinitionStr += 'if(' + 'char ' + branchStatementName + ' == ' + branchStatementConditionVal_Char + ') {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(char ' + branchStatementName + ' == ' + choice(string.ascii_letters) + ') {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        functionDefinitionStr += 'else {\n\tcontinue;\n}\n'
    else:
        counter = 0
        while counter < lengthOfParameterList:
            if parameterList[counter] == 'int&' or 'const int&':
                functionDefinitionStr += 'if(' + parameterList[counter + 1] + ' == ' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                numBranchStatement_Temp = numBranchStatement
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(' + parameterList[counter + 1] + ' == ' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1    
            elif parameterList[counter] == 'int*':
                functionDefinitionStr += 'if(*' + parameterList[counter + 1] + ' == ' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                numBranchStatement_Temp = numBranchStatement
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(*' + parameterList[counter + 1] + ' == ' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1
            elif parameterList[counter] == 'float&' or 'const float&':
                functionDefinitionStr += 'if(' + parameterList[counter + 1] + ' == ' + branchStatementConditionVal_Num + '.01) {\n\tcontinue;\n}'
                numBranchStatement_Temp = numBranchStatement
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(' + parameterList[counter + 1] + ' == ' + str(randint(100,199)) + '.01) {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1
            elif parameterList[counter] == 'float*':
                functionDefinitionStr += 'if(*' + parameterList[counter + 1] + ' == ' + branchStatementConditionVal_Num + '.02) {\n\tcontinue;\n}'
                numBranchStatement_Temp = numBranchStatement
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(*' + parameterList[counter + 1] + ' == ' + str(randint(100,199)) + '.02) {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1
            elif parameterList[counter] == 'std::string&' or 'const std::string&':
                functionDefinitionStr += 'if(' + parameterList[counter + 1] + ' == junkStr_' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'  
                numBranchStatement_Temp = numBranchStatement
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(' + parameterList[counter + 1] + ' == junkStr_' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1
            elif parameterList[counter] == 'std::string*':
                functionDefinitionStr += 'if(*' + parameterList[counter + 1] + ' == junkStr_' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                numBranchStatement_Temp = numBranchStatement
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(*' + parameterList[counter + 1] + ' == junkStr_' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1
            functionDefinitionStr += 'else {\n\tcontinue;\n}\n'
            counter += 2           
            
############################################
####### Create function definition #########
############################################
#number of variable is dependent on number of parameters + random variables (numVariable) created within scope
#paramter is passed as list of parameters
def createFunctionDefinition(returnType, parameter):
    functionDefinitionStr = ''
    paramList = parameter[1]
    varTypes = ('int','float','std::string','double','char')

    functionDefinitionStr = createForLoop(numForLoop, functionDefinitionStr)
    functionDefinitionStr = createWhileLoop(numWhileLoop, functionDefinitionStr)
    createBranchStatement(numBranchStatement, len(paramList), paramList, functionDefinitionStr)
    functionDefinitionStr = createVariable(numVariable, functionDefinitionStr, varTypes)

    if returnType != 'void': #if return type is not void
        randomReturnName = createRandomName(randint(500,1000))
        functionDefinitionStr += returnType + ' ' + randomReturnName + ';\nreturn ' + randomReturnName + ';\n'

    if functionDefinitionStr == '': #Empty function definition 
        functionDefinitionStr = 'return;\n'
    
    return functionDefinitionStr

##########################################################
######## Define and create variables for class ###########
##########################################################
def defineClassVariableList(numClassVariable, classVarList):
    if numClassVariable == 0:
        return
    else:
        randomClassVariableName = createRandomName(numClassVariable)
        if numClassVariable % 3 == 0:
            outputFile_Header.write('\t\tstd::string ' + randomClassVariableName + ';\n')
            classVarList.append('std::string')
        elif numClassVariable % 3 == 1:
            outputFile_Header.write('\t\tint ' + randomClassVariableName + ';\n')
            classVarList.append('int')
        elif numClassVariable % 3 == 2:
            outputFile_Header.write('\t\tfloat ' + randomClassVariableName + ';\n') 
            classVarList.append('float')
        classVarList.append(randomClassVariableName)
        defineClassVariableList(numClassVariable-1, classVarList)

##################################################################
############ Define and create constructor for class #############
##################################################################
def returnClassConstructorAsStr(classVarList):
    classConstructor = ''
    counter = 0
    while counter < len(classVarList):
        classConstructor += classVarList[counter] + ' ' + classVarList[counter + 1]
        if counter + 2 != len(classVarList):
            classConstructor += ', '
        counter += 2
    return classConstructor  

###################################################################
############# Create accessor and setter methods ##################
###################################################################
def defineAccessorAndSetter(randomClassName, lengthOfClassVarList, classVarList, classVarListIndex):
    if classVarListIndex > lengthOfClassVarList:
        return
    else:
        randomInt = randint(0,99)
        if classVarList[classVarListIndex-1] == 'std::string':
            outputFile_Header.write('\t\tstd::string ' + 'getString_' + classVarList[classVarListIndex] + '();\n\t\tvoid setString_' + classVarList[classVarListIndex] + '(const std::string& newStr);\n')
            outputFile_Cpp.write('\tstd::string ' + 'junkClass_' + randomClassName + '::getString_' + classVarList[classVarListIndex] + '() {\n\t\treturn ' + 
                                 classVarList[classVarListIndex] + ';\n\t}\n' + '\tvoid ' + 'junkClass_' + randomClassName + '::setString_' + 
                                 classVarList[classVarListIndex] + '(const std::string& newStr) {\n\t\t' + classVarList[classVarListIndex] + 
                                 ' = newStr;\n\t}\n')       
        elif classVarList[classVarListIndex-1] == 'int':
            outputFile_Header.write('\t\tint ' + 'getInt_' + classVarList[classVarListIndex] + '();\n\t\tvoid setInt_' + classVarList[classVarListIndex] + '(int newInt);\n')
            outputFile_Cpp.write('\tint ' + 'junkClass_' + randomClassName + '::getInt_' + classVarList[classVarListIndex] + '() {\n\t\treturn ' + 
                                 classVarList[classVarListIndex] + ';\n\t}\n' + '\tvoid ' + 'junkClass_' + randomClassName + '::setInt_' + 
                                 classVarList[classVarListIndex] + '(int newInt) {\n\t\t' + classVarList[classVarListIndex] + 
                                 ' = newInt;\n\t}\n')
        elif classVarList[classVarListIndex-1] == 'float':
            outputFile_Header.write('\t\tfloat ' + 'getFloat_' + classVarList[classVarListIndex] + '();\n\t\tvoid setFloat_' + classVarList[classVarListIndex] + '(float newFloat);\n')
            outputFile_Cpp.write('\tfloat ' + 'junkClass_' + randomClassName + '::getFloat_' + classVarList[classVarListIndex] + '() {\n\t\treturn ' + 
                                 classVarList[classVarListIndex] + ';\n\t}\n' + '\tvoid ' + 'junkClass_' + randomClassName + '::setFloat_' + 
                                 classVarList[classVarListIndex] + '(float newFloat) {\n\t\t' + classVarList[classVarListIndex] + 
                                 ' = newFloat;\n\t}\n')    
        defineAccessorAndSetter(randomClassName, lengthOfClassVarList, classVarList, classVarListIndex + 2)
         
#################################################################
################## Create class methods #########################
#################################################################
def defineClassMethod(randomClassName, numClassMethod):
    if numClassMethod == 0:
        return
    else: 
        randomClassMethodName = createRandomName(numClassMethod)
        randomInt = randint(0,99)
        if numClassMethod % 4 == 0:
            outputFile_Header.write('\t\tstd::string ' + 'generateRandString_' + randomClassMethodName + '_' + str(numClassMethod) + '();\n')
            outputFile_Cpp.write('\tstd::string ' + 'junkClass_' + randomClassName + '::' + 'generateRandString_' + randomClassMethodName + '_' + str(numClassMethod) +
                                    '() {\n\t\tfor(int i = 0; i < ' + str(randomInt) + '; i++) {\n\t\t\tcontinue;\n\t\t}\n\t\tstring junkString_' + randomClassMethodName + 
                                    ' = junkStr_' + str(randomInt) + ';\n\t\treturn junkString_' + randomClassMethodName + ';\n\t}\n')    
        elif numClassMethod % 4 == 1:
            outputFile_Header.write('\t\tint ' + 'generateRandInt_' + randomClassMethodName + '_' + str(numClassMethod) + '();\n')
            outputFile_Cpp.write('\tint ' + 'junkClass_' + randomClassName + '::' + 'generateRandInt_' + randomClassMethodName + '_' + str(numClassMethod) +
                                    '() {\n\t\tfor(int i = 0; i < ' + str(randomInt) + '; i++) {\n\t\t\tcontinue;\n\t\t}\n\t\tint junkInt_' + randomClassMethodName + 
                                    ' = ' + str(randomInt) + ';\n\t\treturn junkInt_' + randomClassMethodName + ';\n\t}\n')
        elif numClassMethod % 4 == 2:
            outputFile_Header.write('\t\tfloat ' + 'generateRandFloat_' + randomClassMethodName + '_' + str(numClassMethod) + '();\n')
            outputFile_Cpp.write('\tfloat ' + 'junkClass_' + randomClassName + '::' + 'generateRandFloat_' + randomClassMethodName + '_' + str(numClassMethod) + 
                                    '() {\n\t\tfor(int i = 0; i < ' + str(randomInt) + '; i++) {\n\t\t\tcontinue;\n\t\t}\n\t\tfloat junkFloat_' + randomClassMethodName + 
                                    ' = ' + str(randomInt) + '.' + str(randint(100,200)) + ';\n\t\treturn junkFloat_' + randomClassMethodName + ';\n\t}\n')   
        defineClassMethod(randomClassName, numClassMethod-1) 
        
####################################################
############ Create and Define Class ###############
####################################################
def createClass(numClasses):
    if numClasses == 0:
        return
    else:
        #Namespace for classes
        junkClassNamspace_Name = str(randint(0,9999))
        outputFile_Header.write("namespace junkNamespace_" + junkClassNamspace_Name + " {\n")
        outputFile_Cpp.write("namespace junkNamespace_" + junkClassNamspace_Name + " {\n")

        randomClassName = createRandomName(numClasses)
        outputFile_Header.write('\tclass ' + 'junkClass_' + randomClassName + ' {\n\tprivate:\n')
        outputFile_Header.write('\t\tchar *junkCharArr_' + randomClassName + ';\n')
        outputFile_Header.write('\t\tint *junkInt_' + randomClassName + ';\n')

        ##################################################################
        ##### Create and Define Class Variables in Constructor Form ######
        ##################################################################
        classVariableList = []
        defineClassVariableList(numClassVariable, classVariableList)
        classVariableListLength = len(classVariableList)
        classConstructorStr = returnClassConstructorAsStr(classVariableList)

        outputFile_Header.write('\tpublic:\n')
        ###############################################
        ##Write prototype constructor and destructors##
        ###############################################
        explicitRandomConstructorName_Int = createRandomName(randint(50,99))
        explicitRandomConstructorName_Float = createRandomName(randint(50,99))
        outputFile_Header.write('\t\texplicit junkClass_' + randomClassName + '(int ' + explicitRandomConstructorName_Int + ');\n')
        outputFile_Header.write('\t\texplicit junkClass_' + randomClassName + '(float ' + explicitRandomConstructorName_Float + ');\n')
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '(' + classConstructorStr + ');\n') #Constructor
        outputFile_Header.write('\t\t~junkClass_' + randomClassName + '();\n') #Destructor
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '(const junkClass_' + randomClassName + '& oldJunkObj);\n') #Copy Constructor
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '(junkClass_' + randomClassName + '&& rValue);\n') #Move Constructor
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '& operator=(const junkClass_' + randomClassName + ' &toCopyAssign);\n') #Copy Assignment
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '& operator=(junkClass_' + randomClassName + '&& toMove);\n') #Move Assignment
        ######################################
        ##Define constructor and destructors##
        ######################################
        #Explicit Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(int ' + explicitRandomConstructorName_Int + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(nullptr) { }\n') 
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(float ' + explicitRandomConstructorName_Float + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(nullptr) { };\n') 
        #Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(' + classConstructorStr + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(new int(' + str(randint(0,9)) +  '))')
        if classVariableListLength != 0:
            outputFile_Cpp.write(', ')
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write(classVariableList[counter] + '(' + classVariableList[counter] + ')')
                if (counter + 2) < classVariableListLength:
                    outputFile_Cpp.write(', ')  
                counter += 2
        outputFile_Cpp.write(' { }\n')    
        #Destructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + '~junkClass_' + randomClassName + '() {\n\t\tdelete[] junkCharArr_' + randomClassName + '; junkCharArr_' + randomClassName +
                             ' = nullptr;\n\t\tdelete junkInt_' + randomClassName + '; junkInt_' + randomClassName + ' = nullptr;\n\t}\n')
        #Copy Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::junkClass_' + randomClassName + '(const junkClass_' + randomClassName + '& oldJunkObj) : junkCharArr_' + randomClassName + 
                             '(new char[1024]), junkInt_' + randomClassName + '(new int(*oldJunkObj.junkInt_' + randomClassName + '))') 
        if classVariableListLength != 0:
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write(', ' + classVariableList[counter] + '(oldJunkObj.' + classVariableList[counter] + ')')
                counter += 2 
        outputFile_Cpp.write(' {\n' + '\t\t*junkInt_' + randomClassName + ' = *oldJunkObj.junkInt_' + randomClassName + ';\n\t\tjunkCharArr_' + randomClassName + ' = new char[1024];\n\t\tstrcpy(' + 
                             'junkCharArr_' + randomClassName + ', oldJunkObj.junkCharArr_' + randomClassName + ');\n\t}\n')
        #Move Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::junkClass_' + randomClassName + '(junkClass_' + randomClassName + '&& rValue)' + ' : junkCharArr_' + randomClassName + 
                             '(rValue.junkCharArr_' + randomClassName + '), ' +
                             'junkInt_' + randomClassName + '(rValue.junkInt_' + randomClassName + ')')  
        if classVariableListLength != 0:  
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write(', ' + classVariableList[counter] + '(rValue.' + classVariableList[counter] + ')')
                counter += 2
        outputFile_Cpp.write(' {\n\t\trValue.junkCharArr_' + randomClassName + ' = nullptr;\n\t\trValue.junkInt_' + randomClassName + ' = nullptr;')
        if classVariableListLength != 0:  
            counter = 1
            while counter < classVariableListLength:
                if classVariableList[counter-1] == 'std::string':
                    outputFile_Cpp.write('\n\t\trValue.' + classVariableList[counter] + ' = "";')
                elif classVariableList[counter] == 'float':
                    outputFile_Cpp.write('\n\t\trValue.' + classVariableList[counter] + ' = 0.f;')
                elif classVariableList[counter] == 'int':
                    outputFile_Cpp.write('\n\t\trValue.' + classVariableList[counter] + ' = 0;')
                counter += 2
        outputFile_Cpp.write('\n\t}\n')
        #Copy Assignment
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '& junkClass_' + randomClassName + '::' + 'operator=(const junkClass_' + randomClassName + '& toCopyAssign) {\n' + 
                             '\t\tif(this != &toCopyAssign) {\n\t\t\tstd::swap(*junkCharArr_' + randomClassName + ', *toCopyAssign.junkCharArr_' + 
                             randomClassName + ');\n\t\t\t' + 'std::swap(*junkInt_' + randomClassName + ', *toCopyAssign.junkInt_' + randomClassName + ');\n')
        if classVariableListLength != 0:  
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write('\t\t\t' + classVariableList[counter] + ' = toCopyAssign.' + classVariableList[counter] + ';\n')
                counter += 2
        outputFile_Cpp.write('\t\t}\n\t\treturn *this;\n\t}\n')  
        #Move Assignment
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '& junkClass_' + randomClassName + '::operator=(junkClass_' + randomClassName + 
                             '&& toMove) {\n'+ '\t\tif(this != &toMove) {\n\t\t\tdelete[] junkCharArr_' + randomClassName + ';\n\t\t\tdelete junkInt_' + randomClassName + 
                             ';\n\t\t\tjunkCharArr_' + randomClassName + ' = toMove.junkCharArr_' + randomClassName + ';\n\t\t\tjunkInt_' + randomClassName + 
                             ' = toMove.junkInt_' + randomClassName + ';\n\t\ttoMove.junkCharArr_' + randomClassName +  ' = nullptr;\n\t\ttoMove.junkInt_' + randomClassName + ' = nullptr;\n')
        if classVariableListLength != 0:  
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write('\t\t\t' + classVariableList[counter] + ' = toMove.' + classVariableList[counter] + ';\n')
                counter += 2
        outputFile_Cpp.write('\t\t}\n\t\treturn *this;\n\t}\n')
        #######################################################################################
        ######################## Write and define prototype methods ###########################
        #######################################################################################
        ##################################
        ####Overload Add Operator#########
        ##################################
        outputFile_Header.write('\t\tfriend int operator+(const junkClass_' + randomClassName + '& term_1, const junkClass_' + randomClassName + '& term_2);\n')
        outputFile_Cpp.write('\tint operator+(const junkClass_' + randomClassName + '& term_1, const junkClass_' + randomClassName + '& term_2) {\n\t\treturn *term_1.junkInt_' + 
                             randomClassName + ' + *term_2.junkInt_' + randomClassName + ';\n\t}\n')
        ####################################
        ###### Accessors and setters #######
        ####################################  
        classVariableList_indexCounter = 1
        if classVariableListLength != 0:  
            defineAccessorAndSetter(randomClassName, classVariableListLength, classVariableList, classVariableList_indexCounter)
        ######################################
        ########Class Methods#################
        ######################################
        defineClassMethod(randomClassName, numClassMethod)
        outputFile_Header.write('\t\tint getJunkInt();\n')
        outputFile_Cpp.write('\tint junkClass_' + randomClassName + '::getJunkInt() {\n\t\treturn *junkInt_' + randomClassName + ';\n\t}\n')

        outputFile_Header.write("\t};\n}\n")
        outputFile_Cpp.write("};\n")

        createClass(numClasses-1)  

def createFunction(numFunction):
    if numFunction == 0:
        return
    else:
        functionPrototype, functionParamList, functionReturnType = createFunctionPrototype(numFunction, numFunction)
        outputFile_Header.write(indent(functionPrototype + ';\n','\t'))
        outputFile_Cpp.write(indent(functionPrototype,'\t') + ' {\n' + indent(createFunctionDefinition(functionReturnType,functionParamList),'\t\t') + '\n\t}\n')    
        createFunction(numFunction-1)
                                             
##########################################################################################################
################################    Write to Files  ######################################################
##########################################################################################################   
outputFile_Header.write("#ifndef OUTPUTFILE_H\n#define OUTPUTFILE_H\n#include<iostream>\n#include<string>\n\n")
outputFile_Cpp.write('#include<iostream>\n#include<string>\n#include "outputFile.h"\n\n')
createClass(numClass)

#############################
##Write prototype functions##
#############################
junkFunctionNamspace_Name = str(randint(0,9999))
outputFile_Header.write("namespace junkNamespace_" + junkFunctionNamspace_Name + " {\n")
outputFile_Cpp.write("namespace junkNamespace_" + junkFunctionNamspace_Name + " {\n")
createFunction(numFunction)

outputFile_Header.write("}\n\n#endif")
outputFile_Cpp.write("};")

outputFile_Header.close()   
outputFile_Cpp.close()
