#!/usr/bin/env python3
"""Unit tests for utils module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ A class for testing utils.access_nested_map method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, mapp, path, expected):
        """Sucess testing for access_nested_map method
        """
        self.assertEqual(access_nested_map(mapp, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, mapp, path, error):
        """Testing failure of utils.access_nested_map method
        """
        with self.assertRaises(KeyError):
            try:
                access_nested_map(mapp, path)
            except KeyError as e:
                self.assertEqual(e.args[0], error)
                raise


class TestGetJson(unittest.TestCase):
    """Testing for utils.get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Tests utils.get_json with a mock object
        """
        patcher = patch("utils.requests.get")
        mock_get = patcher.start()
        mock_get.return_value.ok = payload.get("payload")
        mock_get.return_value.json.return_value = payload
        res = get_json(url)
        self.assertEqual(res, payload)
        mock_get.stop()


class TestMemoize(unittest.TestCase):
    """Testing for utils.memoize decorator
    """
    def test_memoize(self):
        """Testing for utils.memoize decorator by mocking a_method
        """
        class TestClass:
            """A class for testing
            """
            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_a:
            mock_a.return_value = True
            test = TestClass()
            test.a_property
            test.a_property
            mock_a.assert_called_once()


if __name__ == '__main__':
    unittest.main()
