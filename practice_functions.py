#!/usr/bin/python

# This function censors a given word out of a block of given text.
# practice with join/split string manipulation


def censor(text, word):
    l = text.split()
    result = " "
    for i in range(0, len(l)):
        if l[i] == word:
            l[i] = "*" * len(word)
    result = result.join(l)
    print result


censor("hey hey hey hey", "hey")


# This function finds the median of a list of numbers
def median(n):
    n = sorted(n)
    if len(n) % 2 != 0:
        return n[len(n)/2]
    else:
        return float(n[len(n) / 2] + n[len(n) / 2 - 1]) / 2.0
