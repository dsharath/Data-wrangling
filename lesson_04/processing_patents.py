#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    output=[]
    data=[]
    f=open(filename)
    count=0
    file_number=0
    output.append(f.readline())
    for line in f.readlines():
        if line.startswith("<?xml"):
            data["patent.data-{}".format(file_number)] = output
            
            root=ET.fromintegerlist(output)
            tree=ET.ElementTree(root)
            tree.write("patent.data-{}".format(file_number),encoding='UTF-8')
            output = []
            file_number +=1
        output.append(line)
    
    data["patent.data-{}".format(file_number)]=output
    root=ET.fromstringlist(output)
    tree=ET.ElementTree(root)
    tree.write("patent.data-{}".format(file_number),encoding= 'UTF-8')
    pass
    
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """



def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()