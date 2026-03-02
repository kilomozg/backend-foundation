campaigns = [
    {"name": "Search", "cost": 300, "revenue": 450},
    {"name": "Display", "cost": 200, "revenue": 150},
    {"name": "YouTube", "cost": 400, "revenue": 400}
]

if len(campaigns) == 0:
    print("No campaigns")

else:
    total_cost: float = 0.0
    total_revenue: float = 0.0

    for campaign in campaigns:
        total_cost += campaign['cost']
        total_revenue += campaign['revenue']
    
    if total_cost == 0:
        print('Total cost = 0')
    else:
        roi: float = (total_revenue - total_cost) / total_cost
        print(f'ROI: {roi:.2%}')