from random2 import randint
from random2 import seed
from random2 import random
from random2 import choice
from textwrap import indent
import string
import re
import sys

outputFile_Header = open('junkCodefile_header.txt','w')
outputFile_Cpp = open('junkCodefile_cpp.txt','w')

numClass = 0
numClassVariable = 0
numClassMethod = 0
numFunction = 0
numVar = 0
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
        numClassMethod = int(input('Input number of class methods (Required: 0 < Entered value <= 10): '))
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
        numFunction = int(input('Input number of functions (0 < Entered value < 10): Default is 1: '))
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
        numVar = int(input('Input number of variables (0 < Entered value < 10): Default is 1: '))
        if numClass not in range(0,6):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numForLoop = int(input('Input number of for loops (0 < Entered value < 10): Default is 1: '))
        if numClass not in range(0,6):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numWhileLoop = int(input('Input number of while loops (0 < Entered val1ue < 10): Default is 1: '))
        if numClass not in range(0,6):
            print('Enter input with valid range.')
        else:
            break
    except(ValueError):
        print('Not valid input. Must be an integer.')
    except(EOFError, KeyboardInterrupt, SystemExit):
        sys.exit()

while True:
    try:
        numBranchStatement  = int(input('Input number of branch statement (0 < Entered value < 10): Default is 1: '))
        if numClass not in range(0,6):
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
def createFunction(returnType = 0, numParameter = 0):
    paramStr = createFunctionParameters(numParameter)
    functionReturnStr = createFunctionReturnType(returnType)
    functionStr = functionReturnStr + ' ' + createRandomName(randint(0,99)) + '(' + paramStr[0] + ')'
    return functionStr, paramStr, functionReturnStr   

############################################
####### Create function definition #########
############################################
#number of variable is dependent on number of parameters + random variables (numVar) created within scope
#paramter is passed as list of parameters
#To preserve O(n) running time, no nested for loop
def createFunctionDefinition(returnType, parameter):
    functionDefinitionStr = ''
    paramList = parameter[1]
    varTypes = ('int','float','string','double','char')

    if 0 < numForLoop <= 5:
        numForLoop_Temp = numForLoop
        while(numForLoop_Temp > 0):
            functionDefinitionStr += 'for(int i = ' + str(randint(0,99)) + '; i<100; i++) {\n\tcontinue;\n}\n'
            numForLoop_Temp -= 1
    
    if 0 < numWhileLoop <= 5:
        numWhileLoop_Temp = numWhileLoop
        while(numWhileLoop_Temp > 0):
            randomCountName = createRandomName(numWhileLoop_Temp)
            functionDefinitionStr += 'int count_' + randomCountName + ' = ' + str(randint(0,50)) + ';\nwhile(count_' + randomCountName + '>0) {\n\tcount_' + randomCountName + '--;\n\tcontinue;\n}\n'
            numWhileLoop_Temp -= 1

    if 0 < numBranchStatement <= 5:
        numBranchStatement_Temp = numBranchStatement
        branchStatementName = createRandomName(numBranchStatement_Temp)
        branchStatementConditionVal_Num = str(randint(0,200))
        branchstatementConditionVal_Char = choice(string.ascii_letters)
        if len(paramList) > 0:  #At least 1 variable in parameter (minimum length will be 2, 
                                #1 index for variable type and 1 index for variable name
            counter = 0
            while counter < len(paramList):
                if paramList[counter] == 'int&' or 'const int&':
                    functionDefinitionStr += 'if(' + paramList[counter + 1] + ' == ' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                    while(numBranchStatement_Temp > 0):
                        functionDefinitionStr += 'else if(' + paramList[counter + 1] + ' == ' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                        numBranchStatement_Temp -= 1    
                elif paramList[counter] == 'int*':
                    functionDefinitionStr += 'if(*' + paramList[counter + 1] + ' == ' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                    while(numBranchStatement_Temp > 0):
                        functionDefinitionStr += 'else if(*' + paramList[counter + 1] + ' == ' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                        numBranchStatement_Temp -= 1
                elif paramList[counter] == 'float&' or 'const float&':
                    functionDefinitionStr += 'if(' + paramList[counter + 1] + ' == ' + branchStatementConditionVal_Num + '.01) {\n\tcontinue;\n}'
                    while(numBranchStatement_Temp > 0):
                        functionDefinitionStr += 'else if(' + paramList[counter + 1] + ' == ' + str(randint(100,199)) + '.01) {\n\tcontinue;\n}'  
                        numBranchStatement_Temp -= 1
                elif paramList[counter] == 'float*':
                    functionDefinitionStr += 'if(*' + paramList[counter + 1] + ' == ' + branchStatementConditionVal_Num + '.02) {\n\tcontinue;\n}'
                    while(numBranchStatement_Temp > 0):
                        functionDefinitionStr += 'else if(*' + paramList[counter + 1] + ' == ' + str(randint(100,199)) + '.02) {\n\tcontinue;\n}'  
                        numBranchStatement_Temp -= 1
                elif paramList[counter] == 'string&' or 'const string&':
                    functionDefinitionStr += 'if(' + paramList[counter + 1] + ' == junkStr_' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                    while(numBranchStatement_Temp > 0):
                        functionDefinitionStr += 'else if(' + paramList[counter + 1] + ' == junkStr_' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                        numBranchStatement_Temp -= 1
                elif paramList[counter] == 'string*':
                    functionDefinitionStr += 'if(*' + paramList[counter + 1] + ' == junkStr_' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                    while(numBranchStatement_Temp > 0):
                        functionDefinitionStr += 'else if(*' + paramList[counter + 1] + ' == junkStr_' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                        numBranchStatement_Temp -= 1
                functionDefinitionStr += 'else {\n\tcontinue;\n}\n'
                counter += 2           

        else:   #No parameters passed into function
            if numBranchStatement_Temp % 5 == 0:
                functionDefinitionStr += 'if(' + 'int ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(int ' + branchStatementName + ' == ' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1 
            elif numBranchStatement_Temp % 5 == 1:
                functionDefinitionStr += 'if(' + 'float ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + '.01) {\n\tcontinue;\n}'
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(float ' + branchStatementName + ' == ' + str(randint(100,199)) + '.02) {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1 
            elif numBranchStatement_Temp % 5 == 1:
                functionDefinitionStr += 'if(' + 'string ' + branchStatementName + ' == junkStr_' + branchStatementConditionVal_Num + ') {\n\tcontinue;\n}'
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(string ' + branchStatementName + ' == ' + 'junkStr_' + str(randint(100,199)) + ') {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1 
            elif numBranchStatement_Temp % 5 == 1:
                functionDefinitionStr += 'if(' + 'double ' + branchStatementName + ' == ' + branchStatementConditionVal_Num + '.03) {\n\tcontinue;\n}'
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(double ' + branchStatementName + ' == ' + 'junkStr_' + str(randint(100,199)) + '.03) {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1 
            elif numBranchStatement_Temp % 5 == 1:
                functionDefinitionStr += 'if(' + 'char ' + branchStatementName + ' == ' + branchStatementConditionVal_Char + ') {\n\tcontinue;\n}'
                while(numBranchStatement_Temp > 0):
                    functionDefinitionStr += 'else if(char ' + branchStatementName + ' == ' + choice(string.ascii_letters) + ') {\n\tcontinue;\n}'  
                    numBranchStatement_Temp -= 1 
            functionDefinitionStr += 'else {\n\tcontinue;\n}\n'
    
    if 0 < numVar <= 5:
        numVar_Temp = numVar
        while(numVar_Temp > 0):
            functionDefinitionStr += str(varTypes[randint(0,4)]) + ' ' + createRandomName(numVar) + ';\n'
            numVar_Temp -= 1

    if returnType != 'void': #if return type is not void
        randomReturnName = createRandomName(randint(500,1000))
        functionDefinitionStr += returnType + ' ' + randomReturnName + ';\nreturn ' + randomReturnName

    if functionDefinitionStr == '': #Empty function definition 
        functionDefinitionStr = 'return;\n'
    
    return functionDefinitionStr

def defineNumOfClassMethods():
    #Define recursively
                                             
##########################################################################################################
################################    Write to Files  ######################################################
##########################################################################################################   
outputFile_Header.write("#ifndef OUTPUTFILE_H\n#define OUTPUTFILE_H\n#include<iostream>\n#include<string>\n\n")
outputFile_Cpp.write('#include<iostream>\n#include<string>\n#include "outputFile.h"\n\n')
#If input for num of class != 0
if 0 < numClass <= 10:
    numClass_Temp = numClass
    while(numClass_Temp > 0):
        #Namespace for classes
        junkClassNamspace_Name = str(randint(0,9999))
        outputFile_Header.write("namespace junkNamespace_" + junkClassNamspace_Name + " {\n")
        outputFile_Cpp.write("namespace junkNamespace_" + junkClassNamspace_Name + " {\n")

        randomClassName = createRandomName(numClass_Temp)
        outputFile_Header.write('\tclass ' + 'junkClass_' + randomClassName + ' {\n\tprivate:\n')
        outputFile_Header.write('\t\tchar *junkCharArr_' + randomClassName + ';\n')
        outputFile_Header.write('\t\tint *junkInt_' + randomClassName + ';\n')
        classConstructor = ''
        #If input for num of class variable != 0
        if 0 < numClassVariable <= 10:
            numClassVariable_Temp = numClassVariable
            while(numClassVariable_Temp > 0):
                randomClassVariableName = createRandomName(numClassVariable_Temp)
                if numClassVariable_Temp % 3 == 0:
                    outputFile_Header.write('\t\tstd::string ' + randomClassVariableName + ';\n')
                    if classConstructor != '':
                        classConstructor += ','
                    classConstructor += 'std::string& ' + randomClassVariableName
                elif numClassVariable_Temp % 3 == 1:
                    outputFile_Header.write('\t\tint ' + randomClassVariableName + ';\n')
                    if classConstructor != '':
                        classConstructor += ','
                    classConstructor += 'int ' + randomClassVariableName
                elif numClassVariable_Temp % 3 == 2:
                    outputFile_Header.write('\t\tfloat ' + randomClassVariableName + ';\n') 
                    if classConstructor != '':
                        classConstructor += ','
                    classConstructor += 'float ' + randomClassVariableName
                numClassVariable_Temp -= 1
        outputFile_Header.write('\tpublic:\n')
        ###############################################
        ##Write prototype constructor and destructors##
        ###############################################
        explicitRandomConstructorName = createRandomName(randint(50,99))
        outputFile_Header.write('\t\texplicit junkClass_' + randomClassName + '(int ' + explicitRandomConstructorName + ');\n')
        outputFile_Header.write('\t\texplicit junkClass_' + randomClassName + '(float ' + explicitRandomConstructorName + ');\n')
        outputFile_Header.write('\t\tjunkClass_' + randomClassName + '(' + classConstructor + ');\n') #Constructor
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
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(int ' + explicitRandomConstructorName + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(nullptr)') 
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(float ' + explicitRandomConstructorName + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(nullptr)') 
        #Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::' + 'junkClass_' + randomClassName + '(' + classConstructor + ') : junkCharArr_' + 
                             randomClassName + '(new char[1024]), junkInt_' + randomClassName + '(nullptr)')
        if classConstructor != '':
            outputFile_Cpp.write(', ')
            classParamList = re.split(',|\s+',classConstructor)
            counter = 1
            while counter < len(classParamList):
                outputFile_Cpp.write(classParamList[counter] + '(' + classParamList[counter] + ')')
                if (counter + 2) < len(classParamList):
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
                             randomClassName + ');\n\t\t')
        if classConstructor != '':
            classParamList = re.split(',|\s+',classConstructor)
            counter = 1
            while counter < len(classParamList):
                outputFile_Cpp.write(classParamList[counter] + ' = oldJunkObj.' + classParamList[counter] + ';\n')
                if (counter + 2) < len(classParamList):
                    outputFile_Cpp.write('\t\t')  
                counter += 2 
        outputFile_Cpp.write('\t}\n')
        #Move Constructor
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '::junkClass_' + randomClassName + '(' + randomClassName + '&& rValue)' + ' : junkCharArr_' + randomClassName + 
                             '(std::move(rValue.junkCharArr_' + randomClassName + ')), ' +
                             'junkInt_' + randomClassName + '(std::move(rValue.junkInt_' + randomClassName + '))')  
        if classConstructor != '':  
            classParamList = re.split(',|\s+',classConstructor)
            counter = 1
            while counter < len(classParamList):
                outputFile_Cpp.write(', ' + classParamList[counter] + '(std::move(rValue.' + classParamList[counter] + ')')
                counter += 2
        outputFile_Cpp.write(' {}\n')
        #Copy Assignment
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '& junkClass_' + randomClassName + '::' + 'operator=(const ' + randomClassName + '& toCopyAssign) {\n' + 
                             '\t\tstd::swap(junkCharArr_' + randomClassName + ',toCopyAssign.junkCharArr_' + randomClassName + ');\n\t\t' + 'std::swap(junkInt_' + randomClassName + 
                             ',toCopyAssign.junkInt_' + randomClassName + ');\n')
        if classConstructor != '':  
            classParamList = re.split(',|\s+',classConstructor)
            counter = 1
            while counter < len(classParamList):
                outputFile_Cpp.write('\t\tstd::swap(' + classParamList[counter] + ',toCopyAssign.' + classParamList[counter] + ');\n')
                counter += 2
        outputFile_Cpp.write('\t\treturn *this;\n\t}\n')  
        #Move Assignment
        outputFile_Cpp.write('\tjunkClass_' + randomClassName + '& junkClass_' + randomClassName + '::junkClass_' + randomClassName + '& operator=(' + randomClassName + 
                             '&& toMove) {\n'+ '\t\tif(this != &toMove) {\n\t\t\tdelete junkCharArr_' + randomClassName + ';\n\t\t\tdelete junkInt_' + randomClassName + 
                             ';\n\t\t\tjunkCharArr_' + randomClassName + ' = std::move(toMove.junkCharArr_' + randomClassName + ');\n\t\t\tjunkInt_' + randomClassName + 
                             ' = std::move(toMove.junkInt_' + randomClassName + ');\n')
        if classConstructor != '':  
            classParamList = re.split(',|\s+',classConstructor)
            counter = 1
            while counter < len(classParamList):
                outputFile_Cpp.write('\t\t\t' + classParamList[counter] + ' = std::move(toMove.' + classParamList[counter] + ');\n')
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
        ##################################
        ####Write accessors and setters###
        ##################################    
        if classConstructor != '':  
            classParamList = re.split(',|\s+',classConstructor)
            counter = 0
            while counter < len(classParamList):
                randomInt = randint(0,99)
                if classParamList[counter] == 'std::string&':
                    outputFile_Header.write('\t\tstring ' + 'getString_' + classParamList[counter + 1] + '();\n')
                    outputFile_Cpp.write('\tstring ' + 'junkClass_' + randomClassName + '::getString_' + classParamList[counter + 1] + '() {\n\t\treturn ' + classParamList[counter + 1] + ';\n\t}\n' + 
                                         '\tvoid ' + 'junkClass_' + randomClassName + '::setString_' + classParamList[counter + 1] + '(const std::string& newStr) {\n\t\t' + classParamList[counter + 1] + ' = newStr;\n\t}\n')       
                elif classParamList[counter] == 'int':
                    outputFile_Header.write('\t\tint ' + 'getInt_' + classParamList[counter + 1] + '();\n')
                    outputFile_Cpp.write('\tint ' + 'junkClass_' + randomClassName + '::getInt_' + classParamList[counter + 1] + '() {\n\t\treturn ' + classParamList[counter + 1] + ';\n\t}\n' +
                                         '\tvoid ' + 'junkClass_' + randomClassName + '::setInt_' + classParamList[counter + 1] + '(int newInt) {\n\t\t' + classParamList[counter + 1] + ' = newInt;\n\t}\n')
                elif classParamList[counter] == 'float':
                    outputFile_Header.write('\t\tfloat ' + 'getFloat_' + classParamList[counter + 1] + '();\n')
                    outputFile_Cpp.write('\tfloat ' + 'junkClass_' + randomClassName + '::getFloat_' + classParamList[counter + 1] + '() {\n\t\treturn ' + classParamList[counter + 1] + ';\n\t}\n' + 
                                         '\tvoid ' + 'junkClass_' + randomClassName + '::setInt_' + classParamList[counter + 1] + '(float newFloat) {\n\t\t' + classParamList[counter + 1] + ' = newFloat;\n\t}\n')
                counter += 2
        ######################################
        ########Class Methods#################
        ######################################
        #If input for num of class method != 0
        if 0 < numClassMethod <= 10:
            numClassMethod_Temp = numClassMethod
            while(numClassMethod_Temp > 0):
                randomClassMethodName = createRandomName(numClassVariable_Temp)
                if numClassMethod_Temp % 4 == 0:
                    randomInt = randint(0,99)
                    outputFile_Header.write('\t\tstring ' + str(numClassMethod_Temp) + '_generateRandString_' + randomClassMethodName + '();\n')
                    outputFile_Cpp.write('\tstring ' + 'junkClass_' + randomClassName + '::' + str(numClassMethod_Temp) + '_generateRandString_' + randomClassMethodName + 
                                         '() {\n\t\tfor(int i = 0; i < ' + str(randomInt) + '; i++) {\n\t\t\tcontinue;\n\t\t}\n\t\tstring junkString_' + randomClassMethodName + 
                                         ' = junkStr_' + str(randomInt) + ';\n\t\treturn junkString_' + randomClassMethodName + ';\n\t}\n')    
                elif numClassMethod_Temp % 4 == 1:
                    outputFile_Header.write('\t\tint ' + str(numClassMethod_Temp) + '_generateRandInt_' + randomClassMethodName + '();\n')
                    outputFile_Cpp.write('\tint ' + 'junkClass_' + randomClassName + '::' + str(numClassMethod_Temp) + '_generateRandInt_' + randomClassMethodName + 
                                         '() {\n\t\tfor(int i = 0; i < ' + str(randomInt) + '; i++) {\n\t\t\tcontinue;\n\t\t}\n\t\tint junkInt_' + randomClassMethodName + 
                                         ' = ' + str(randomInt) + ';\n\t\treturn junkInt_' + randomClassMethodName + ';\n\t}\n')
                elif numClassMethod_Temp % 4 == 2:
                    outputFile_Header.write('\t\tfloat ' + str(numClassMethod_Temp) + '_generateRandFloat_' + randomClassMethodName + '();\n')
                    outputFile_Cpp.write('\tfloat ' + 'junkClass_' + randomClassName + '::' + str(numClassMethod_Temp) + '_generateRandString_' + randomClassMethodName + 
                                         '() {\n\t\tfor(int i = 0; i < ' + str(randomInt) + '; i++) {\n\t\t\tcontinue;\n\t\t}\n\t\tfloat junkFloat_' + randomClassMethodName + 
                                         ' = ' + str(randomInt) + '.' + str(randint(100,200)) + ';\n\t\treturn junkFloat_' + randomClassMethodName + ';\n\t}\n')    
                numClassMethod_Temp -= 1
        outputFile_Header.write("\t};\n}\n")
        outputFile_Cpp.write("}\n")
        numClass_Temp -= 1

#Namespace for functions
#############################
##Write prototype functions##
#############################
junkFunctionNamspace_Name = str(randint(0,9999))
outputFile_Header.write("namespace junkNamespace_" + junkFunctionNamspace_Name + " {\n")
outputFile_Cpp.write("namespace junkNamespace_" + junkFunctionNamspace_Name + " {\n")
if 0 < numFunction <= 10:
    numFunction_Temp = numFunction
    while numFunction_Temp > 0:
        functionPrototype, functionParamList, functionReturnType = createFunction(numFunction_Temp, numFunction_Temp)
        outputFile_Header.write(indent(functionPrototype + ';\n','\t'))
        outputFile_Cpp.write(indent(functionPrototype,'\t') + ' {\n' + indent(createFunctionDefinition(functionReturnType,functionParamList),'\t\t') + '\n\t}\n')
        numFunction_Temp -= 1
outputFile_Header.write("}\n\n#endif")
outputFile_Cpp.write("}")

outputFile_Header.close()   
outputFile_Cpp.close()