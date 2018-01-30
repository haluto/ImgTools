#!/usr/bin/python
#coding=utf-8

from imgutils import imgutil
import sys
import os
import getopt

VERSION = "v1.0.0"

#------------------------------------------------------
# usage
#------------------------------------------------------
def usage():
    print "Usage: python viewimg.py -i input_file"
    print "-i: input file, jpg, png, ..."
    print "-h: print this help message"
    print "--version: print product version and exit"


#------------------------------------------------------
# version
#------------------------------------------------------
def version():
    print VERSION


#------------------------------------------------------
# main
#------------------------------------------------------
def main():

    inputFile = ""
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:", ["version"])
    
        for op, value in opts:
            if op == "-i":
                inputFile = value
            elif op == "-h":
                usage()
                sys.exit()
            elif op == "--version":
                version()
                sys.exit()
            else:
                usage()
                sys.exit()
    except getopt.GetoptError:
        usage()
        sys.exit()
            
    if inputFile == "":
        usage()
        sys.exit()

    if not os.path.exists(inputFile):
        print inputFile + " does NOT exist!!!"
        sys.exit()
    
    imgutil.viewImage(inputFile)

if __name__ == '__main__':
    main()