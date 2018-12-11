# a tool for comparing two MEI files

from evalMei import evalMei
from lxml import etree as ET
import sys

def input_args():
    print "usage:\t'python file1.mei file2.mei'"
    print "\twhere file1.mei is the ground truth"
    print "\twhere file2.mei is compared to the ground truth"

if __name__ == "__main__":

    if len(sys.argv) == 3:
        (tmp, inMei1, inMei2) = sys.argv
    else:
        input_args()
        exit()

    with open(inMei1,"r") as f:
        GT = ET.fromstring(f.read())

    with open(inMei2,"r") as f:
        OG = ET.fromstring(f.read())


    mei_evaluator = evalMei()
    mei_evaluator.evaluate(GT, OG)
