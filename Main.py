from operator import attrgetter
from Entities import People
from VisitingController import VisitingController
from Calculator import Calculator
import sys

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-v':
            v = VisitingController(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == '-c':
            c = Calculator(sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()
