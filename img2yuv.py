import imgutil as imgutil
import sys
import os
import getopt

VERSION = "v1.0.0"

#------------------------------------------------------
# usage
#------------------------------------------------------
def usage():
    print "Usage: python img2yuv.py -i input_file -o out_file"
    print "-i: input file, jpg, png, ..."
    print "-o: output file, .yuv"
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
    outputFile = ""
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["version"])
    
        for op, value in opts:
            if op == "-i":
                inputFile = value
            elif op == "-o":
                outputFile = value
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
            
    if inputFile == "" or outputFile == "":
        usage()
        sys.exit()

    if not os.path.exists(inputFile):
        print inputFile + " does NOT exist!!!"
        sys.exit()
    
    if os.path.exists(outputFile):
        os.remove(outputFile)
    
    imgutil.cvtImg2YUV(inputFile, outputFile)
    print outputFile + " generated!"


if __name__ == '__main__':
    main()