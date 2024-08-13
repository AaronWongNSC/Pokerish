import random

class GameState:
    def __init__(self, action, dice):
        self.dice = dice
        self.action = action
    
    def total(self):
        return sum(self.dice)
    
    def last_action(self):
        if len(self.action[-1]) > 0:
            return self.action[-1][-1]
        return None
    
    def action_number(self):
        return len(self.action[-1])
    
    def street(self):
        return len(self.dice) - 1
    
    def first_die(self):
        return self.dice[0]
    
    def second_die(self):
        if len(self.dice) == 2:
            return self.dice[1]
        return None

class Pokerish:
    def __init__(self, strat0, strat1):
        self.strat = [strat0, strat1]
        self.street = 0
        self.invest = [0, 0]
        self.action = [ ]
        self.dice = [ [ random.randint(1,6) for _ in range(2) ], [ random.randint(1,6) for _ in range(2) ]]
    
    def play(self):
        for street in range(2):
            self.street = street
            self.action.append([])
            action = True
            while action:
                action = self.make_decision()
            
            if self.action[-1][-1] == 'F':
                break

        self.determine_outcome()
            
    def make_decision(self):
        # Determine whose action
        active = len(self.action[self.street]) % 2
        decision = self.strat[active](GameState(self.action, self.dice[active][:(self.street + 1)]))
        action = self.add_action(decision)
        self.validate()
        if self.action[self.street][-1] == 'F':
            return False
        return action

    def validate(self):
        if self.action[self.street][-1] not in [ 'K', 'B', 'C' ]:
            self.action[self.street][-1] = 'F'            
        if self.action[self.street][-2:] in [ ['C'], ['B', 'K'], ['B', 'B'], ['K', 'C'] ]:
            self.action[self.street][-1] = 'F'
            
    def add_action(self, decision):
        self.action[self.street].append(decision)
        if self.action[self.street][-2:] in [ ['K', 'K'], ['B', 'C'] ]:
            return False
        if self.action[self.street][-1:] == 'F':
            return False
        return True

    def summary(self):
        text = ''
        for player in range(2):
            text += 'Player {}: '.format(player) + self.strat[player].__name__ + '\n'
            text += ' '.join(str(item) for item in self.dice[player]) + '\n'
        text += ' '.join(str(item) for item in self.action) + '\n'
        text += self.winner + '\n'
        text += str(self.potsize) + '\n'
        text += ' '.join([str(item) for item in self.win]) + '\n\n'
        return text
    
    def determine_outcome(self):
        # Calculate the pot contributions
        self.invest = [1, 1]

        for street in self.action:
            for count, action in enumerate(street):
                if action in ['B', 'C']:
                    active = count % 2
                    self.invest[active] += 1

        self.potsize = sum(self.invest)
        
        # Player folded
        if self.action[-1][-1] == 'F':
            if (len(self.action[-1]) % 2) == 0:
                self.winner = 'Player Zero'
                self.win = [self.potsize - self.invest[0], -self.invest[1]]
            else:
                self.winner = 'Player One'
                self.win = [-self.invest[0], self.potsize - self.invest[1]]

            return
        
        # Showdown
        total = [ sum(dice) for dice in self.dice]
        
        if total[0] > total[1]:
            self.winner = 'Player Zero'
            self.win = [self.potsize - self.invest[0], -self.invest[1]]
        elif total[0] < total[1]:
            self.winner = 'Player One'
            self.win = [-self.invest[0], self.potsize - self.invest[1]]
        else:
            self.winner = 'Push'
            self.win = [0, 0]

def compete(player0, player1, maxorbits = 50000):
    hands = []
    winnings = [0, 0]

    for orbit in range(maxorbits):
        for count, strat in enumerate([ [player0, player1], [player1, player0]]):
            poker = Pokerish(strat[0], strat[1])
            poker.play()
            hands.append(poker)
        
            zeroth = count % 2
            first = (count + 1) % 2
            winnings[0] += hands[-1].win[zeroth]
            winnings[1] += hands[-1].win[first]
        
    print('--- FINAL RESULT ---')
    print('P1 ({}): {} \t\t P2 ({}): {}\n\n'.format(player0.__name__, winnings[0], player1.__name__, winnings[1]))
    
    return(hands, winnings)

def test(player0, player1, maxorbits = 10):
    hands, winnings = compete(player0, player1, maxorbits = maxorbits)

    with open('test_output.txt', 'w') as output:
        for count, hand in enumerate(hands):
            print('Hand {}'.format(count + 1))
            print(hand.summary())
                
            output.write('Hand {}:\n'.format(count + 1))
            output.write(hand.summary())