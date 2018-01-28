from random2 import randint
from random2 import seed
from random2 import random
from random2 import choice
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
    returnType = ('void','float','string','int')
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
    parameterType = ('int','float','string')

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
        branchStatementName = createRandomName(numBranchStatement_Temp)
        if numBranchStatement_Temp % 5 == 0:
            functionDefinitionStr += 'if(' + 'int ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(int ' + branchStatementName + ' == ' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        elif numBranchStatement_Temp % 5 == 1:
            functionDefinitionStr += 'if(' + 'float ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + '.01) {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(float ' + branchStatementName + ' == ' + str(randint(100,199)) + '.02) {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        elif numBranchStatement_Temp % 5 == 2:
            functionDefinitionStr += 'if(' + 'string ' + branchStatementName + ' == junkStr_' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(string ' + branchStatementName + ' == ' + 'junkStr_' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        elif numBranchStatement_Temp % 5 == 3:
            functionDefinitionStr += 'if(' + 'double ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + '.03) {\n\tcontinue;\n}'
            numBranchStatement_Temp = numBranchStatement
            while(numBranchStatement_Temp > 0):
                functionDefinitionStr += 'else if(double ' + branchStatementName + ' == ' + 'junkStr_' + str(randint(100,199)) + '.03) {\n\tcontinue;\n}'  
                numBranchStatement_Temp -= 1 
        elif numBranchStatement_Temp % 5 == 4:
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
            elif parameterList[counter] == 'string&' or 'const string&':
                functionDefinitionStr += 'if(' + parameterList[counter + 1] + ' == junkStr_' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'  
                numBranchStatement_Temp = numBranchStatement
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(' + parameterList[counter + 1] + ' == junkStr_' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1
            elif parameterList[counter] == 'string*':
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
    varTypes = ('int','float','string','double','char')

    functionDefinitionStr = createForLoop(numForLoop, functionDefinitionStr)
    functionDefinitionStr = createWhileLoop(numWhileLoop, functionDefinitionStr)
    createBranchStatement(numBranchStatement, len(paramList), paramList, functionDefinitionStr)
    functionDefinitionStr = createVariable(numVariable, functionDefinitionStr, varTypes)

    if returnType != 'void': #if return type is not void
        randomReturnName = createRandomName(randint(500,1000))
        functionDefinitionStr += returnType + ' ' + randomReturnName + ';\nreturn ' + randomReturnName

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
            classVarList.append('std::string&')
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
        if classVarList[classVarListIndex-1] == 'std::string&':
            outputFile_Header.write('\t\tstring ' + 'getString_' + classVarList[classVarListIndex] + '();\n')
            outputFile_Cpp.write('\tstring ' + 'junkClass_' + randomClassName + '::getString_' + classVarList[classVarListIndex] + '() {\n\t\treturn ' + 
                                 classVarList[classVarListIndex] + ';\n\t}\n' + '\tvoid ' + 'junkClass_' + randomClassName + '::setString_' + 
                                 classVarList[classVarListIndex] + '(const std::string& newStr) {\n\t\t' + classVarList[classVarListIndex] + 
                                 ' = newStr;\n\t}\n')       
        elif classVarList[classVarListIndex-1] == 'int':
            outputFile_Header.write('\t\tint ' + 'getInt_' + classVarList[classVarListIndex] + '();\n')
            outputFile_Cpp.write('\tint ' + 'junkClass_' + randomClassName + '::getInt_' + classVarList[classVarListIndex] + '() {\n\t\treturn ' + 
                                 classVarList[classVarListIndex] + ';\n\t}\n' + '\tvoid ' + 'junkClass_' + randomClassName + '::setInt_' + 
                                 classVarList[classVarListIndex] + '(int newInt) {\n\t\t' + classVarList[classVarListIndex] + 
                                 ' = newInt;\n\t}\n')
        elif classVarList[classVarListIndex-1] == 'float':
            outputFile_Header.write('\t\tfloat ' + 'getFloat_' + classVarList[classVarListIndex] + '();\n')
            outputFile_Cpp.write('\tfloat ' + 'junkClass_' + randomClassName + '::getFloat_' + classVarList[classVarListIndex] + '() {\n\t\treturn ' + 
                                 classVarList[classVarListIndex] + ';\n\t}\n' + '\tvoid ' + 'junkClass_' + randomClassName + '::setInt_' + 
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
            outputFile_Header.write('\t\tstring ' + str(numClassMethod) + '_generateRandString_' + randomClassMethodName + '();\n')
            outputFile_Cpp.write('\tstring ' + 'junkClass_' + randomClassName + '::' + str(numClassMethod) + '_generateRandString_' + randomClassMethodName + 
                                    '() {\n\t\tfor(int i = 0; i < ' + str(randomInt) + '; i++) {\n\t\t\tcontinue;\n\t\t}\n\t\tstring junkString_' + randomClassMethodName + 
                                    ' = junkStr_' + str(randomInt) + ';\n\t\treturn junkString_' + randomClassMethodName + ';\n\t}\n')    
        elif numClassMethod % 4 == 1:
            outputFile_Header.write('\t\tint ' + str(numClassMethod) + '_generateRandInt_' + randomClassMethodName + '();\n')
            outputFile_Cpp.write('\tint ' + 'junkClass_' + randomClassName + '::' + str(numClassMethod) + '_generateRandInt_' + randomClassMethodName + 
                                    '() {\n\t\tfor(int i = 0; i < ' + str(randomInt) + '; i++) {\n\t\t\tcontinue;\n\t\t}\n\t\tint junkInt_' + randomClassMethodName + 
                                    ' = ' + str(randomInt) + ';\n\t\treturn junkInt_' + randomClassMethodName + ';\n\t}\n')
        elif numClassMethod % 4 == 2:
            outputFile_Header.write('\t\tfloat ' + str(numClassMethod) + '_generateRandFloat_' + randomClassMethodName + '();\n')
            outputFile_Cpp.write('\tfloat ' + 'junkClass_' + randomClassName + '::' + str(numClassMethod) + '_generateRandString_' + randomClassMethodName + 
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
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '(const ' + randomClassName + '& oldJunkObj);\n') #Copy Constructor
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '( ' + randomClassName + '&& rValue)' + ' : junkCharArr_' + randomClassName + 
                                '(std::move(rValue.junkCharArr_' + randomClassName + ')), ' + 'junkInt_' + randomClassName + '(std::move(rValue.junkInt_' + randomClassName + '));\n') #Move Constructor
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '& operator=(const ' + randomClassName + '& toCopyAssign);\n') #Copy Assignment
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '& operator=(' + randomClassName + '&& toMove);\n') #Move Assignment
        ######################################
        ##Define constructor and destructors##
        ######################################
        #Explicit Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(int ' + explicitRandomConstructorName_Int + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(nullptr)\n') 
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(float ' + explicitRandomConstructorName_Float + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(nullptr)\n') 
        #Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(' + classConstructorStr + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(nullptr)')
        if classVariableListLength != 0:
            outputFile_Cpp.write(', ')
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write(classVariableList[counter] + '(' + classVariableList[counter] + ')')
                if (counter + 2) < classVariableListLength:
                    outputFile_Cpp.write(', ')  
                counter += 2
        outputFile_Cpp.write(' { };\n')    
        #Destructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + '~junkClass_' + randomClassName + '() {\n\t\tdelete[] junkCharArr_' + randomClassName + '; junkCharArr_' + randomClassName +
                             ' = nullptr;\n\t\tdelete junkInt_' + randomClassName + '; junkInt_' + randomClassName + ' = nullptr;\n\t}\n')
        #Copy Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::junkClass_' + randomClassName + '(const ' + randomClassName + '& oldJunkObj) {\n' +
                             '\t\tjunkInt_' + randomClassName + ' = new int;\n\t\t*junkInt_' + randomClassName + ' = *oldJunkObj.' + 'junkInt_' + randomClassName + 
                             ';\n\t\tjunkCharArr_' + randomClassName + ' = new char[1024];\n\t\tstd::copy(' + 'junkCharArr_' + randomClassName + ',  oldJunkObj.junkCharArr_' + 
                             randomClassName + ');\n')
        if classVariableListLength != 0:
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write('\t\t' + classVariableList[counter] + ' = oldJunkObj.' + classVariableList[counter] + ';\n')  
                counter += 2 
        outputFile_Cpp.write('\t}\n')
        #Move Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::junkClass_' + randomClassName + '(' + randomClassName + '&& rValue)' + ' : junkCharArr_' + randomClassName + 
                             '(std::move(rValue.junkCharArr_' + randomClassName + ')), ' +
                             'junkInt_' + randomClassName + '(std::move(rValue.junkInt_' + randomClassName + '))')  
        if classVariableListLength != 0:  
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write(', ' + classVariableList[counter] + '(std::move(rValue.' + classVariableList[counter] + ')')
                counter += 2
        outputFile_Cpp.write(' { }\n')
        #Copy Assignment
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '& junkClass_' + randomClassName + '::' + 'operator=(const ' + randomClassName + '& toCopyAssign) {\n' + 
                             '\t\tstd::swap(junkCharArr_' + randomClassName + ',toCopyAssign.junkCharArr_' + randomClassName + ');\n\t\t' + 'std::swap(junkInt_' + randomClassName + 
                             ',toCopyAssign.junkInt_' + randomClassName + ');\n')
        if classVariableListLength != 0:  
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write('\t\tstd::swap(' + classVariableList[counter] + ',toCopyAssign.' + classVariableList[counter] + ');\n')
                counter += 2
        outputFile_Cpp.write('\t\treturn *this;\n\t}\n')  
        #Move Assignment
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '& junkClass_' + randomClassName + '::junkClass_' + randomClassName + '& operator=(' + randomClassName + 
                             '&& toMove) {\n'+ '\t\tif(this != &toMove) {\n\t\t\tdelete junkCharArr_' + randomClassName + ';\n\t\t\tdelete junkInt_' + randomClassName + 
                             ';\n\t\t\tjunkCharArr_' + randomClassName + ' = std::move(toMove.junkCharArr_' + randomClassName + ');\n\t\t\tjunkInt_' + randomClassName + 
                             ' = std::move(toMove.junkInt_' + randomClassName + ');\n')
        if classVariableListLength != 0:  
            counter = 1
            while counter < classVariableListLength:
                outputFile_Cpp.write('\t\t\t' + classVariableList[counter] + ' = std::move(toMove.' + classVariableList[counter] + ');\n')
                counter += 2
        outputFile_Cpp.write('\t\t}\n\t\treturn *this;\n\t}\n')
        #####################################################################################
        ########################Write and define prototype methods###########################
        #####################################################################################
        ##################################
        ####Overload Add Operator#########
        ##################################
        outputFile_Header.write('\t\tfriend junkClass_' + randomClassName + ' operator+(const junkClass_' + randomClassName + '& term_1, const junkClass_' + randomClassName + '& term_2);\n')
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + ' operator+(const ' + randomClassName + '& term_1, const ' + randomClassName + '& term_2) {\n\t\tjunkClass_' + randomClassName + 
                             ' result = term_1;\n\t\tresult.junkInt_' + randomClassName + ' = term_1.junkInt_' + randomClassName + ' + term_2.junkInt_' + randomClassName + ';\n\t\treturn result;\n\t}\n')
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

        outputFile_Header.write("\t};\n}\n")
        outputFile_Cpp.write("}\n")

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
outputFile_Cpp.write("}")

outputFile_Header.close()   
outputFile_Cpp.close()