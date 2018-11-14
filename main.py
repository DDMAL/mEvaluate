# a tool for comparing two MEI files

from evalMei import evalMei
from pymei import documentFromFile, documentFromText
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
        mei1_text = f.read()

    mei_1 = documentFromText(mei1_text)
    # mei_2 = documentFromFile(inMei2)

    print "DONE"
