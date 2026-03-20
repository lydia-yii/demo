"""Quick sort implementation with comprehensive unit tests."""

from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """Sort a list using the quick sort algorithm."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Unit Tests
import pytest


def test_empty_list():
    assert quick_sort([]) == []


def test_single_element():
    assert quick_sort([42]) == [42]


def test_already_sorted():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates():
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


def test_negative_numbers():
    assert quick_sort([-5, 3, -2, 0, 7, -1]) == [-5, -2, -1, 0, 3, 7]
