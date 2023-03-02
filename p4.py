revenue = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Other': 19849.53}
total = sum(revenue.values())
for state, value in revenue.items():
    percentage = (value / total) * 100
    print('{}: {:.2f}%'.format(state,percentage))