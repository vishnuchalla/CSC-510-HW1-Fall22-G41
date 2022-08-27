class Operation:
    def add(self, input1, input2):
        return input1 + input2

    def multiply(self, input1, input2):
        return input1 * input2

    def subtract(self, input1, input2):
        return input1 - input2

    def divide(self, input1, input2):
        try:
            output = input1 / input2
            return output
        except ZeroDivisionError as err:
            return err