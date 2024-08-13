def pure(GameState):
    # Zeroth street
    if GameState.street() == 0:
        # Zeroth action
        if GameState.action_number() == 0:
            if GameState.first_die() in [1, 2, 3, 4, 5, 6]:
                return 'K'
            if GameState.first_die() in []:
                return 'B'
        
        # First action
        if GameState.action_number() == 1:
            # If checked to
            if GameState.last_action() == 'K':
                if GameState.first_die() in [1, 2, 3, 4, 5, 6]:
                    return 'K'
                if GameState.first_die() in []:
                    return 'B'
            # If bet into
            if GameState.last_action() == 'B':
                if GameState.first_die() in [1, 2, 3, 4, 5, 6]:
                    return 'F'
                if GameState.first_die() in []:
                    return 'C'
        
        # Second action -- Must be K-B-?
        if GameState.action_number() == 2:
            if GameState.first_die() in [1, 2, 3, 4, 5, 6]:
                return 'F'
            if GameState.first_die() in []:
                return 'C'

    # First street
    if GameState.street() == 1:
        # Zeroth action
        if GameState.action_number() == 0:
            if GameState.total() in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                return 'K'
            if GameState.total() in []:
                return 'B'
            
        # First action
        if GameState.action_number() == 1:
            # If checked to
            if GameState.last_action() == 'K':
                if GameState.total() in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                    return 'K'
                if GameState.total() in []:
                    return 'B'
            # If bet into
            if GameState.last_action() == 'B':
                if GameState.total() in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                    return 'F'
                if GameState.total() in []:
                    return 'C'
        
        # Second action -- Must be K-B-?
        if GameState.action_number() == 2:
            if GameState.total() in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                return 'F'
            if GameState.total() in []:
                return 'C'


def prob(GameState):
    import random
    
    probs = [
        # Slot 0 - 0th street, 0th action: check, bet
        [
            [100, 0], # 1
            [100, 0], # 2
            [100, 0], # 3
            [0, 100], # 4
            [0, 100], # 5
            [0, 100]  # 6
        ],
        # Slot 1 - 0th street, 1st action, checked to: check, bet
        [
            [100, 0], # 1
            [100, 0], # 2
            [100, 0], # 3
            [0, 100], # 4
            [0, 100], # 5
            [0, 100]  # 6
        ],
        # Slot 2 - 0th street, 1st action, bet into to: fold, call
        [
            [100, 0], # 1
            [100, 0], # 2
            [100, 0], # 3
            [0, 100], # 4
            [0, 100], # 5
            [0, 100]  # 6
        ],
        # Slot 3 - 0th street, 2st action, K-B-?: fold, call
        [
            [100, 0], # 1
            [100, 0], # 2
            [100, 0], # 3
            [0, 100], # 4
            [0, 100], # 5
            [0, 100]  # 6
        ],
        # Slot 4 - 1st street, 0th action: check, bet
        [
            [100, 0], # 2
            [100, 0], # 3
            [100, 0], # 4
            [100, 0], # 5
            [100, 0], # 6
            [100, 0], # 7
            [0, 100], # 8
            [0, 100], # 9
            [0, 100], # 10
            [0, 100], # 11
            [0, 100]  # 12
        ],
        # Slot 4 - 1st street, 1st action, checked to: check, bet
        [
            [100, 0], # 2
            [100, 0], # 3
            [100, 0], # 4
            [100, 0], # 5
            [100, 0], # 6
            [100, 0], # 7
            [0, 100], # 8
            [0, 100], # 9
            [0, 100], # 10
            [0, 100], # 11
            [0, 100]  # 12
        ],
        # Slot 5 - 1st street, 1st action, bet into: fold, call
        [
            [100, 0], # 2
            [100, 0], # 3
            [100, 0], # 4
            [100, 0], # 5
            [100, 0], # 6
            [100, 0], # 7
            [0, 100], # 8
            [0, 100], # 9
            [0, 100], # 10
            [0, 100], # 11
            [0, 100]  # 12
        ],
        # Slot 6 - 1st street, 2nd action, K-B-?: fold, call
        [
            [100, 0], # 2
            [100, 0], # 3
            [100, 0], # 4
            [100, 0], # 5
            [100, 0], # 6
            [100, 0], # 7
            [0, 100], # 8
            [0, 100], # 9
            [0, 100], # 10
            [0, 100], # 11
            [0, 100]  # 12
        ],
        ]
    
    # Zeroth street
    if GameState.street() == 0:
        # First action
        if GameState.action_number() == 0:
            return random.choices(['K', 'B'], weights = (probs[0][GameState.first_die() - 1][0], probs[0][GameState.first_die() - 1][1]))[0]
        
        # Second action
        if GameState.action_number() == 1:
            # If checked to
            if GameState.last_action() == 'K':
                return random.choices(['K', 'B'], weights = (probs[1][GameState.first_die() - 1][0], probs[1][GameState.first_die() - 1][1]))[0]
            
            # If bet into
            if GameState.last_action() == 'B':
                return random.choices(['F', 'C'], weights = (probs[2][GameState.first_die() - 1][0], probs[2][GameState.first_die() - 1][1]))[0]
        
        # Third action -- Must be K-B-?
        if GameState.action_number() == 2:
            return random.choices(['F', 'C'], weights = (probs[3][GameState.first_die() - 1][0], probs[3][GameState.first_die() - 1][1]))[0]

    # First street
    if GameState.street() == 1:
        # First action
        if GameState.action_number() == 0:
            return random.choices(['K', 'B'], weights = (probs[4][GameState.first_die() - 2][0], probs[4][GameState.first_die() - 2][1]))[0]
            
        # Second action
        if GameState.action_number() == 1:
            # If checked to
            if GameState.last_action() == 'K':
                return random.choices(['K', 'B'], weights = (probs[5][GameState.first_die() - 2][0], probs[4][GameState.first_die() - 2][1]))[0]
            # If bet into
            if GameState.last_action() == 'B':
                return random.choices(['F', 'C'], weights = (probs[5][GameState.first_die() - 2][0], probs[5][GameState.first_die() - 2][1]))[0]
        
        # Third action -- Must be K-B-?
        if GameState.action_number() == 2:
            return random.choices(['F', 'C'], weights = (probs[6][GameState.first_die() - 2][0], probs[6][GameState.first_die() - 2][1]))[0]
