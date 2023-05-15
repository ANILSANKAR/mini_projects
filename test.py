spam = ['apple','banana','tofu','cats
new = [ x if x != spam[-1] else f'and {x}' for x in spam ] 
s = ', '.join(new)
