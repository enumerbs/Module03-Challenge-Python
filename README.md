# Module03-Challenge-Python
Data Analytics Boot Camp - Module 03 - Python \
Python Challenge

---

# Results

Results for the **PyBank** and **PyPoll** components of this challenge are written to the local console and to the following text files, respectively:
- ./PyBank/analysis/financial_analysis.txt
- ./PyPoll/analysis/election_results.txt

# Implementation notes

The implementations of 'main.py' are similar in both the PyBank and PyPoll cases. In particular, they utilise:
- Coding patterns covered in this Module for file read and write operations, using features of the 'os' and 'csv' Python modules.
- A Dictionary data structure to facilitate storage and retrieval of intermediate results.
- Formatted output utilising f-string syntax.

The PyPoll 'main.py' also explored iterating over Dictionary key/value pairs, and uses a Tuple to keep track of each election candidate's individual vote count and percentage of the total votes. It then uses List Comprehension syntax to format the output of those values next to the candidate's name.

# References

The following references were used in the development of the solution for this Challenge.

## Python language
- https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/
- https://www.geeksforgeeks.org/ternary-operator-in-python/
- https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator

## Python code patterns for reading & writing files
- Coding patterns for "Reading and Writing in Python": Data Analytics Boot Camp - Module 3, Lesson 2 class notes.
- https://blog.enterprisedna.co/python-write-to-file/

## Python f-string formatting
- https://jerrynsh.com/3-useful-python-f-string-tricks-you-probably-dont-know/

## Python data structures
### Dictionary features
- https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
- https://www.freecodecamp.org/news/how-to-check-if-a-key-exists-in-a-dictionary-in-python/
- https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
### List comprehensions
- https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
### Tuple features
- https://www.w3schools.com/python/python_tuples_access.asp
