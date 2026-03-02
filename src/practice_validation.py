campaigns = [
    {"name": "Search", "cost": 300, "revenue": 450},
    {"name": "Display", "cost": 200, "revenue": 150},
    {"name": "YouTube", "cost": 400, "revenue": 400},
    {"name": "Broken", "cost": 0, "revenue": 100}
]

if len(campaigns) == 0:
    print('No campaigns')
else:
    
    for campaign in campaigns:
        if campaign['cost'] == 0:
            print(f'For campaign "{campaign["name"]}" cost = 0')
            continue
        
        profit: float = campaign['revenue'] - campaign['cost']
        print(f'Campaign {campaign["name"]} profit - {profit:.2f}')