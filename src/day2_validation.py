cost: float = 0
revenue: float = 450.0

profit: float = revenue - cost
roi: float = (revenue - cost) / cost

if cost == 0:
    print("Invalid cost")
elif revenue < cost:
    print("Loss")
elif revenue == cost:
    print("Break even")
elif revenue > cost:
    print("Profit")