from simplestrats import *
from advancedstrats import *
from KW import KW
import pokerish

def main():
    pokerbot = KW
    
    print('Pokerbot Gauntlet:\n')
    
    for round_num, opponent in enumerate([loosepassive, rando, straightforward, aggro]):
        print('Round {}: {} vs. {}'.format(round_num + 1, pokerbot.__name__, opponent.__name__))
        pokerish.compete(pokerbot, opponent)

if __name__ == '__main__':
    main()

