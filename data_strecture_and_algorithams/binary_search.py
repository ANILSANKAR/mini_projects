from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

cards = list(range(1,101))

tests = []
test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

def locate_card(cards, query):
    lo = 0
    hi = len(cards) - 1
    
    count = 1
    
    while lo <= hi:
        mid = ((lo + hi) // 2) 
        midcard = cards[mid]
        
        print(f'COUNT:{count};   lo:{lo};  hi:{hi};  mid:{mid};  midCard:{midcard};   query:{query}')
        
        if midcard == query:
            return mid
        elif midcard < query:
            lo = mid + 1
        elif midcard > query:
             hi = mid - 1
        count += 1
    return -1
    
#result = locate_card(**test['input']) == test['output']
#print (result)
#evaluate_test_cases(locate_card, tests)
evaluate_test_case(locate_card, tests[8])
    