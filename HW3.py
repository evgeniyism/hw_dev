boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys = sorted(boys)
girls = sorted(girls)
couples = zip(boys,girls)
if len(boys) == len(girls):
    print('Идеальные пары:')
    for match in couples:
        print(match[0], 'и', match[1] )
else:
    print('Количество участников неравное, кто кто-то может остаться без пары')