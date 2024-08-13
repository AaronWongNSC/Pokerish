def Wong1(GameState):
    import random
    
    #random.choices(['K', 'B'], weights = (75, 25))[0]
    #print('-------------------------------------')
    #print('Street: {}'.format(GameState.street()))
    #print('Action: {}'.format(GameState.action_number()))
    #print('First Die: {}'.format(GameState.first_die()))
    #print('Second Die: {}'.format(GameState.second_die()))
    #print('Total: {}'.format(GameState.total()))
    
    # Zeroth street
    if GameState.street() == 0:
        # First action
        if GameState.action_number() == 0:
            if GameState.first_die() in [1, 2]:
                return 'K'
            if GameState.first_die() in [3, 4, 5, 6]:
                return 'B'
        
        # Second action
        if GameState.action_number() == 1:
            # If checked to
            if GameState.last_action() == 'K':
                if GameState.first_die() in [1, 2]:
                    return 'K'
                if GameState.first_die() in [3, 4, 5, 6]:
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
            if GameState.total() in [2, 3, 4, 5, 6, 7]:
                return 'K'
            if GameState.total() in [8, 9, 10, 11, 12]:
                return 'B'
            
        # Second action
        if GameState.action_number() == 1:
            # If checked to
            if GameState.last_action() == 'K':
                if GameState.total() in [2, 3, 4, 5, 6]:
                    return 'K'
                if GameState.total() in [7, 8, 9, 10, 11, 12]:
                    return 'B'
            # If bet into
            if GameState.last_action() == 'B':
                if GameState.total() in [2, 3, 4, 5]:
                    return 'F'
                if GameState.total() in [6, 7, 8, 9, 10, 11, 12]:
                    return 'C'
        
        # Third action -- Must be K-B-?
        if GameState.action_number() == 2:
            if GameState.total() in [2, 3, 4, 5]:
                return 'F'
            if GameState.total() in [6, 7, 8, 9, 10, 11, 12]:
                return 'C'
