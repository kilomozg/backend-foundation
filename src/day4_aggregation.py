campaigns = [
    {"name": "Search", "cost": 300, "revenue": 450},
    {"name": "Display", "cost": 200, "revenue": 150},
    {"name": "YouTube", "cost": 400, "revenue": 400}
]

if len(campaigns) == 0:
    print("No campaigns")
else:
    total_profit: float = 0.0

    for campaign in campaigns:
        total_profit += campaign["revenue"] - campaign["cost"]

    average_profit: float = total_profit / len(campaigns)

    print(f"Average Profit: {average_profit:.2f}")