campaigns = [
    {"name": "Search", "cost": 300, "revenue": 450},
    {"name": "Display", "cost": 200, "revenue": 150},
    {"name": "YouTube", "cost": 400, "revenue": 400}
]

for campaign in campaigns:
    profit:float = campaign['revenue'] - campaign['cost']
    if profit < 0:
        print(f'Campaign: {campaign["name"]} - Loss')
    elif profit == 0:
        print(f'Campaign: {campaign["name"]} - BREAK EVEN')
    else:
        print(f"Campaign: {campaign['name']} - Profit: {profit}")