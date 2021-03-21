
import random

questions = {'strong': 'Do ye like yer drinks strong?',
            'salty': 'Do ye like it with a salty tang?',
            'bitter': 'Are ye a lubber who likes it bitter?',
            'sweet': 'Would ye like a bit of sweetness with yer poison?',
            'fruity': 'Are ye one for a fruit finish?'}
ingredients = {"strong": ["glug of rum", "slug of whisky", "splash of gin"],
               "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
               "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
               "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
               "fruity": ["slice of orange", "dash of cassis", "cherry on top"]}

print('Choice of y/n')
print(questions['strong'])
answer = input()
if answer == 'y':
    print(random.choice(ingredients['strong']))
elif answer == 'n':
    print(questions['salty'])
    answer = input()
    if answer == 'y':
        print(random.choice(ingredients['salty']))
    elif answer == 'n':
        print(questions['bitter'])
        answer = input()
        if answer == 'y':
            print(random.choice(ingredients['bitter']))
        elif answer == 'n':
            print(questions['sweet'])
            answer = input()
            if answer == 'y':
                print(random.choice(ingredients['sweet']))
            elif answer == 'n':
                print(questions['fruity'])
                answer = input()
                if answer == 'y':
                    print(random.choice(ingredients['fruity']))
                elif answer == 'n':
                    print('end')

