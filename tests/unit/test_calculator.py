"""
Unit Tests for Calculator
Tests basic arithmetic operations with input validation.
"""

import pytest
from src.calculator import add, divide, subtract, multiply


class TestBasicOperations:
    """Test basic arithmetic operations."""

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6


class TestMultiplyDivide:
    """Test multiplication and division operations."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5
        assert divide(20, 4) == 5

    def test_divide_by_zero(self):
        """Test division by zero."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)


class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""

    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)

        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide(10, "2")