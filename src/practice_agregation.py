campaigns = [
    {"name": "Search", "cost": 300, "revenue": 450},
    {"name": "Display", "cost": 200, "revenue": 150},
    {"name": "YouTube", "cost": 400, "revenue": 400},
    {"name": "Broken", "cost": 0, "revenue": 100}
]

if len(campaigns) == 0:
    print('No campaigns')
else:
    profit: float = 0.0
    profit_count: int = 0

    for campaign in campaigns:
        profit = campaign['revenue'] - campaign['cost']

        if profit > 0:
            profit_count += 1
            profit += profit
        
    avg_profit: float = profit / profit_count
    print(f"Aveerage profit for {profit_count} profitable campaigns = {avg_profit:.2f}")
        
