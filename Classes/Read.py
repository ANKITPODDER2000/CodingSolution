class Read:
    @staticmethod
    def readInput(inputLine = '' , inputType = str):
        inputVar = inputType(input(inputLine))
        return inputVar