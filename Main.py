from operator import attrgetter
from Entities import People
from VisitingController import VisitingController
from Calculator import Calculator
import sys

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-v':
            v = VisitingController()
        elif sys.argv[1] == '-c':
            c = Calculator()

if __name__ == '__main__':
    main()
