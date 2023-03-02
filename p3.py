import json
with open('revenue.json') as f:
    data = json.load(f)
values = [d['valor'] for d in data if d['valor'] > 0]
lowest_revenue = min(values)
highest_revenue = max(values)
monthly_average = sum(values) / len(values)
days_above_average = len([v for v in values if v > monthly_average])
print("Lowest revenue: {}".format(lowest_revenue))
print("Highest revenue: {}".format(highest_revenue))
print("Number of days with revenue above the average: {}".format(days_above_average))
