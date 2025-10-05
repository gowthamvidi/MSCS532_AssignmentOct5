# Assignment 3: Understanding Algorithm Efficiency and Scalability

This repository contains two core Python implementations and analyses:

1. **Randomized Quicksort** — Sorting algorithm with randomized pivot and performance analysis  
2. **Hash Table with Chaining** — Key-value storage using separate chaining and universal hashing  

---

## Project Structure
├── rqsort.py # Randomized Quicksort implementation
├── Understanding_Algorithm_Efficiency_and_Scalability
├── hash.py # Hash Table implementation with chaining
└── README.md # Project documentation

## How to run

- python rqsort.py

- python hash.py

## Sample Output for RandomSort:

----------------------------------------
in:  []
out: []
----------------------------------------
in:  [1]
out: [1]
----------------------------------------
in:  [2, 1]
out: [1, 2]
----------------------------------------
in:  [5, 5, 5, 5, 5]
out: [5, 5, 5, 5, 5]
----------------------------------------
in:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
out: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
----------------------------------------
in:  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
out: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
----------------------------------------
in:  [3, 3, 2, 1, 2, 2, 3, 0, -1]
out: [-1, 0, 1, 2, 2, 2, 3, 3, 3]
----------------------------------------

## Sample Output for Hashtable:
>> insert apple 10
Inserted
>> search apple
Value: 10
>> delete apple
Deleted
>> exit
