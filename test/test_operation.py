import pytest
from code.Operation import Operation

"""
Fixture to setup and teardown operation object for tests.
"""
@pytest.fixture()
def operation():
    print("\nSetting up operation object for test")
    operation = Operation()
    yield operation
    print("\nDeleting operation object as a teardown")
    del operation

"""
Class to test Operation.
"""
class TestOperation:
    """
    Method to test add method.
    """
    def test_add(self, operation):
        actual_result = operation.add(2, 3)
        assert actual_result == 5
    
    """
    Method to test multiply method.
    """
    def test_multiply(self, operation):
        actual_result = operation.multiply(2, 3)
        assert actual_result == 6
    
    """
    Method to test subtract method.
    """
    def test_subtract(self, operation):
        actual_result = operation.subtract(2, 3)
        assert actual_result == (-1)

    """
    Method to test divide method for success case.
    """
    def test_divide_success(self, operation):
        actual_result = operation.divide(6, 3)
        assert actual_result == 2
    
    """
    Method to test divide method for failure case.
    """
    def test_divide_failure(self, operation):
        actual_result = operation.divide(6, 0)   
        assert (str(actual_result) == 'division by zero') 
