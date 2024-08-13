def aggro(GameState):
    if GameState.last_action() == None:
        return 'B'
    if GameState.last_action() == 'B':
        return 'C'
    if GameState.last_action() == 'K':
        return 'B'

def straightforward(GameState):
    if GameState.street() == 0:
        # First action
        if GameState.action_number() == 0:
            if GameState.first_die() in [1, 2, 3, 4, 5]:
                return 'K'
            if GameState.first_die() in [6]:
                return 'B'
        
        # Second action
        if GameState.action_number() == 1:
            # If checked to
            if GameState.last_action() == 'K':
                if GameState.first_die() in [1, 2, 3, 4, 5]:
                    return 'K'
                if GameState.first_die() in [6]:
                    return 'B'
            # If bet into
            if GameState.last_action() == 'B':
                if GameState.first_die() in [1]:
                    return 'F'
                if GameState.first_die() in [2, 3, 4, 5, 6]:
                    return 'C'
        
        # Third action -- Must be K-B-?
        if GameState.action_number() == 2:
            if GameState.first_die() in [1]:
                return 'F'
            if GameState.first_die() in [2, 3, 4, 5, 6]:
                return 'C'

    # First street
    if GameState.street() == 1:
        # First action
        if GameState.action_number() == 0:
            if GameState.total() in [2, 3, 4, 5, 6, 7, 8, 9]:
                return 'K'
            if GameState.total() in [10, 11, 12]:
                return 'B'
            
        # Second action
        if GameState.action_number() == 1:
            # If checked to
            if GameState.last_action() == 'K':
                if GameState.total() in [2, 3, 4, 5, 6, 7, 8, 9]:
                    return 'K'
                if GameState.total() in [10, 11, 12]:
                    return 'B'
            # If bet into
            if GameState.last_action() == 'B':
                if GameState.total() in [2, 3, 4]:
                    return 'F'
                if GameState.total() in [5, 6, 7, 8, 9, 10, 11, 12]:
                    return 'C'
        
        # Third action -- Must be K-B-?
        if GameState.action_number() == 2:
            if GameState.total() in [2, 3, 4]:
                return 'F'
            if GameState.total() in [5, 6, 7, 8, 9, 10, 11, 12]:
                return 'C'

def loosepassive(GameState):
    if GameState.last_action() == None:
        return 'K'
    if GameState.last_action() == 'B':
        return 'C'
    if GameState.last_action() == 'K':
        return 'K'

def rando(GameState):
    import random
    
    if GameState.last_action() == None:
        return random.choice(['B', 'K'])
    if GameState.last_action() == 'B':
        return random.choice(['C', 'F'])
    if GameState.last_action() == 'K':
        return random.choice(['B', 'K'])
