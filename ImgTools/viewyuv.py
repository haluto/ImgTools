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
    print "Usage: python viewyuv.py -i input_file -x width -y height"
    print "-i: input file, jpg, png, ..."
    print "-x: width of yuv"
    print "-y: height of yuv"
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
    w = 0
    h = 0
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:x:y:", ["version"])
    
        for op, value in opts:
            if op == "-i":
                inputFile = value
            elif op == "-x":
                w = int(value)
            elif op == "-y":
                h = int(value)
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
    
    try:
        imgutil.viewYUV(inputFile, w, h)
    except imgutil.YUVWidthHeightError:
        print "Wrong width height!!!"
        sys.exit()

if __name__ == '__main__':
    main()