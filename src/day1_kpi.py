cost: float = 300.0
clicks: int = 80
conversion: int = 7

cpc: float = cost / clicks
conversion_rate: float = conversion / clicks
cpa: float = cost / conversion

print(f"CPC: {cpc: .2f}")
print(f"CR: {conversion_rate: .2%}")
print(f"CPA: {cpa: .2f}")