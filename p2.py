term = int(input('How many terms? '))
n1, n2 = 0, 1
belongsToSequence = False
if term <= 0:
    print('Invalid number.')
elif term == 1:
    print(n1)
else:
    for i in range(0, term):
        print(n1, end=' ')
        if n1 == term:
            belongsToSequence = True
        nth = n1 + n2
        n1 = n2
        n2 = nth
print('\nBelongs to the sequence:', 'Yes' if belongsToSequence else 'No')
