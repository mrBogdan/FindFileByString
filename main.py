#!/usr/bin/env python3


import sys
import os
import time


class ArgumentsResolver:
    args = {}
    params = ['--path', '--w']

    def __init__(self, args):
        self._parseArguments(args)


    def getArgs(self):
        return self.args


    def _parseArguments(self, args):
        try:
            for value in self.params:
                indexOfParam = args.index(value)

                if args[indexOfParam + 1]:
                    self.args[value] = args[indexOfParam + 1]
                else:
                    raise ValueError
        except ValueError:
            print('Wrong params!')
            exit(1)

        print(self.args)


class Finder:
    result = []

    ignoreFolders = [
        'node_modules/',
        '.git/'
    ]

    def __init__(self, currentPath, findWord):
        start = time.time()

        self.findFiles(currentPath, findWord)

        end = time.time()

        print('Time execution: ', end - start)



    def getResult(self):
        return self.result

    def findFiles(self, currentPath, findWord):
        countIterations = 0
        for root, dirs, files in os.walk(currentPath):
            for name in files:
                fullPath = os.path.join(root, name)

                countIterations = countIterations + 1

                if checkItemsInArray(fullPath, self.ignoreFolders) and findWord in open(fullPath,
                                                                                        encoding="ISO-8859-1").read():
                    print(fullPath)

        print('Count iterations: ', countIterations)


def checkItemsInArray(path, folders):
    for f in folders:
        if f in path:
            return False

    return True


def run():
    a = ArgumentsResolver(sys.argv).getArgs()

    f = Finder(a.get('--path'), a.get('--w'))


run()
