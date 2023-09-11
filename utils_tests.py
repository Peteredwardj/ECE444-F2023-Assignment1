
from utils import utils

class utils_tests:
    def __init__(self):
        self.utilsObj = utils()

    def testReversed(self,reversedTestsInput):
        for input in reversedTestsInput:
            conversionResult = self.utilsObj.reversed(input)
            if (conversionResult == reversedTestsInput[input]):
                print("✓ PASSED : Input : {} | Expected : {} | Actual : {}".format(input,reversedTestsInput[input],conversionResult))
            else:
                print("✗ FAILED : Input : {} | Expected : {} | Actual : {}".format(input,reversedTestsInput[input],conversionResult))
                return False 
        
        return True


    def testFormatter(self, formatterTestsInput):
        for input in formatterTestsInput:
            binResult, octResult = self.utilsObj.formatter(input)
            if (binResult == formatterTestsInput[input]['bin'] and octResult == formatterTestsInput[input]['oct']):
                print("✓ PASSED : Input : {} | Expected : {} , {} | Actual : {} , {}".format(input,formatterTestsInput[input]['bin'], formatterTestsInput[input]['oct'],binResult,octResult))
            else:
                print("✗ Failed : Input : {} | Expected : {} , {} | Actual : {} , {}".format(input,formatterTestsInput[input]['bin'], formatterTestsInput[input]['oct'],binResult,octResult))
                return False
        return True
        

def main():
    utilsTestObj = utils_tests()

    print("reversed() test")
    reversedTestsInput = {'stringInput' : None, 1.0: None , 123 : 321 , 321: 123} #input: expected
    testPassed = utilsTestObj.testReversed(reversedTestsInput)   
    if (testPassed):
        print("reversed() test : PASSED")
    else:
        print("reversed() test : FAILED")


    print("\nformatter() test")
    formatterTestsInput = {'stringInput': {'bin': None, 'oct': None}, 1.0: {'bin': None, 'oct': None} , 123 : {'bin': '0b1111011', 'oct': '0o173'} , 321: {'bin': '0b101000001', 'oct': '0o501'}}
    testPassed = utilsTestObj.testFormatter(formatterTestsInput)
    if (testPassed):
        print("formatter() test : PASSED")
    else:
        print("formatter() test : FAILED")


    
if __name__ == "__main__":
    main()