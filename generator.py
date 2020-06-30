#File that generates the basic python program file from scratch.
#Use this to generate custom functions, variables - comments and so on.

class generator:  #Contains all the functions that create functions and stuff

    def main(self,):
        if __name__ == "__main__":
            pass

    ### Variables can have the following types as used mainly by python:
    ### Number, Decimal, Text, Array and Dictionary Types.
    ### Number - Integer
    ### Decimal - Float Value
    ### Text - String
    ### Array - List of items
    ### Dictionary - Dictionary of items basic python
    ### The other data types will be added as necessary.


    def genVariable(self,name,utility,varType): #This function generates variables
        
        varTypeFinal = self.convertVarTypes(varType)
        varName = self.varNameGenerator(name,varType)
        comment = '#' + varType + ' type used for : ' + utility

        print(varName+varTypeFinal+'\t'+comment)
        # with open('output.txt','w') as output_file:
        #     output_file.write(varName+varTypeFinal+'\t'+comment)


    def varNameGenerator(self,name,varType): #This function generates best practice variable names
        
        varName = ''
        name = name.lower()
        varType = varType.lower()
        
        if len(name) > 10:
            varName = name
        elif len(name) < 10:
            name = name.capitalize()
            varName = varType+name
        
        return(varName)


    def convertVarTypes(self, varType): #This function converts variable type from normie to python variable

        variableTypes = {"Number":"=0","Decimal":"=0.0","Text":"=''",
                         "Array":"=[]","Dictionary":"={}"}

        return(variableTypes[varType])


genObj = generator()
