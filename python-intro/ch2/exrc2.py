# Use the REPL and the arithmetic operators to extract the individual digits of 4936

>>> val = 4936
>>> ones = val % 10
>>> ones
6
>>> val = val // 10
>>> tens = val % 10
>>> tens
3
>>> val = val // 10
>>> hundreds = val % 10
>>> hundreds
9
>>> thousands = val = val // 10
>>> thousands
4