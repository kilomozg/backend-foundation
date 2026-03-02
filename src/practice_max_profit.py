campaigns = [
    {"name": "Search", "cost": 300, "revenue": 450},
    {"name": "Display", "cost": 200, "revenue": 150},
    {"name": "YouTube", "cost": 400, "revenue": 400}
]

if len(campaigns) == 0:
    print("No campaigns")

else:
    max_profit = None
    max_campaign_name = None

    for campaign in campaigns:
        profit: float = campaign['revenue'] - campaign['cost']

        if max_profit is None:
            max_profit = profit
            max_campaign_name = campaign["name"]
        elif profit > max_profit:
            max_profit = profit
            max_campaign_name = campaign["name"]
    print(f"Most profitable campaign: {max_campaign_name} - Profit: {max_profit:.2f}")