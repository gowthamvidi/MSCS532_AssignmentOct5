# rqsort.py
import random
import sys
from typing import List

def quicksort_randomized(a: List[int]) -> List[int]:
    arr = list(a)  
    def _qsr(lo: int, hi: int) -> None:
        while lo < hi:
            p_idx = random.randint(lo, hi)
            pivot = arr[p_idx]

            lt, i, gt = lo, lo, hi
            while i <= gt:
                if arr[i] < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    lt += 1
                    i += 1
                elif arr[i] > pivot:
                    arr[i], arr[gt] = arr[gt], arr[i]
                    gt -= 1
                else:
                    i += 1

            left_size = lt - lo
            right_size = hi - gt
            if left_size < right_size:
                if lo < lt - 1:
                    _qsr(lo, lt - 1)
                lo = gt + 1
            else:
                if gt + 1 < hi:
                    _qsr(gt + 1, hi)
                hi = lt - 1

    _qsr(0, len(arr) - 1)
    return arr

def quicksort_randomized_2way(a: List[int]) -> List[int]:
    arr = list(a)
    def partition(lo, hi, p_idx):
        arr[p_idx], arr[hi] = arr[hi], arr[p_idx]
        pivot = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[hi] = arr[hi], arr[i+1]
        return i + 1

    def _qsr(lo, hi):
        while lo < hi:
            p_idx = random.randint(lo, hi)
            p = partition(lo, hi, p_idx)
            # smaller side first to keep stack shallow
            if (p - 1 - lo) < (hi - (p + 1)):
                if lo < p - 1:
                    _qsr(lo, p - 1)
                lo = p + 1
            else:
                if p + 1 < hi:
                    _qsr(p + 1, hi)
                hi = p - 1

    _qsr(0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    #  sorted outputs printed to the console
    tests = [
        [],
        [1],
        [2, 1],
        [5, 5, 5, 5, 5],                # duplicates
        list(range(10)),                # already sorted
        list(range(10))[::-1],          # reverse sorted
        [3, 3, 2, 1, 2, 2, 3, 0, -1],   # mixed
    ]
    for t in tests:
        print("in: ", t)
        print("out:", quicksort_randomized(t))   # <-- change to _2way if you want
        print("-" * 40)