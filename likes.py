#! /usr/bin/env python3

def likes(names):
    if len(names) > 3:
        return "{0}, {1} and {2} others like this".format(names[0],names[1],(len(names)-2))

    if len(names) == 3:
        return "{0}, {1} and {2} like this".format(names[0],names[1],names[2])

    if len(names) == 2:
        return "{0} and {1} like this".format(names[0],names[1])

    if len(names) == 1:
        return "{0} likes this".format(names[0])

    if len(names) == 0:
        return "no one likes this"
