from simplestrats import *
from basicblankstrats import *
import pokerish
from DA import DA
from LM import LM
from OH import OH
from KW import KW
from GL import GL
from HM import HM

def main():
    pokerish.compete(DA, OH)

if __name__ == '__main__':
    main()

