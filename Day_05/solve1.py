#!/usr/bin/env python3
# -*- coding: utf-8 -*-

FILENAME = 'input.txt'

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
        data structure as hashmap with the needed valus
    '''
    l = line.strip()

    if len(l) == 0:
        return { "type": "separator"}
    if l[0] == '1' or l[0] == '[':
        # use the orginial line, not the stripped one
        return { "type": "stack", "line": line}
    s = l.split(" ")
    return { "type": "move", "from": int(s[3]), "to": int(s[5]), "howmany": int(s[1])}

def buildInitialStack(stackdata):
    '''build the initial stack'''
    # find highest stack number
    stack_numbering = stackdata[-1].split(" ")
    number_of_stacks = int(stack_numbering[-2]) # -1 is the new line char
    stacks = []
    for stackindex in range(number_of_stacks):
        stacks.append([])

    print("we have %d stacks" % number_of_stacks)
    for lineindex in range(len(stackdata) - 2, -1, -1):
        for stackindex in range(number_of_stacks):
            strpos = stackindex * 4 + 1
            if len(stackdata[lineindex]) > strpos and stackdata[lineindex][strpos] != ' ':
                stacks[stackindex].append(stackdata[lineindex][strpos])
    
    return stacks


if __name__ == "__main__":
    # read the lines of the file
    with open(FILENAME) as f:
        stacks = []
        stackdata = []
        for line in f:
            # parse data input
            data = parseInput(line)
            if data["type"] == "stack":
                stackdata.append(data["line"])
            if data["type"] == "separator":
                stacks = buildInitialStack(stackdata)
            if data["type"] == "move":
                for i in range(data["howmany"]):
                    # pop last element
                    crate = stacks[data["from"]-1].pop(-1)
                    stacks[data["to"]-1].append(crate)

        # build result
        result = ''
        for s in stacks:
            result = result + s[-1]
        print("The top elements of the stack are %s" % result)