# -*- coding: utf-8 -*-

def areAllDifferent(chars):
    '''Check if all chars in the given array are different'''
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            if i != j and chars[i] == chars[j]:
                return False
    return True

def findMarker(line: str, back: int):
    '''Find the marker in the given line'''
    for i in range(back, len(line)):
        if areAllDifferent(line[i-back:i]):
            return i
    return -1

def parseInput(line: str):
    '''parse the input format for one line

    separated into separate function for easier testablity
    
    Parameters
    ----------
    line : str
        The line read from the input file

    Returns
    -------
    data
        the stripped line
    '''
    return line.strip()