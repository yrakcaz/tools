#! env python2.7

import re, fnmatch, os, sys

def isFunction(line):
    return re.match(r"\w+\s+\*?\w+\(.*\);", line)

def get_files(directory, pattern):
    l=[]
    for root, dirs, files in os.walk(directory):
        for name in fnmatch.filter(files, pattern):
            l.append(os.path.join(root, name))
    return l

def countCommas(l):
    count = 0
    for i in l:
        if i == ',':
            count += 1
    return count

def getFirstWord(l):
    ret = ""
    i = 0
    while i < len(l) and l[i] != ' ':
        ret += l[i]
        i += 1
    return ret

def treatFunction(l):
    ret = "/**\n"
    ret += "** @fn " + l
    ret += "** @brief\n"
    i = 0
    while i <= countCommas(l) and not "()" in l:
        ret += "** @param\n"
        i += 1
    if getFirstWord(l) != "void":
        ret += "** @return\n"
    ret += "*/\n"
    ret += l
    return ret + '\n'


def treat(f):
    newfile = ""
    fd = open(f, "r+")
    for l in fd:
        if isFunction(l):
            newfile += treatFunction(l)
        else:
            newfile += l
    fd.seek(0)
    fd.write(newfile)
    fd.truncate()
    fd.close()

def main():
    argv = sys.argv
    argc = len(argv)
    if (argc != 2):
        print(argv[0] + ": usage: argv[0] <extension>")
        print("\tExample of extension : *.h")
    else:
        files = get_files('.', argv[1])
        for f in files:
            treat(f)

main()
