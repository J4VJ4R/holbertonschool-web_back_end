# 0x09. Unittests and Integration Tests

## Learning Objectives
   - The difference between unit and integration tests.
   -  Common testing patterns such as mocking, parametrizations and fixtures

## Tasks
### [0. Parameterize a unit test](./test_utils.py)
Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.

Decorate the method with @parametrized.expand to test the function for following inputs:
```
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
```
For each of these inputs, test with assertEqual that the function returns the expected result.

The body of the test method should not be longer than 2 lines.

### [1. Parameterize a unit test](./test_utils.py)
Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parametrized.expand):
```
nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
```
