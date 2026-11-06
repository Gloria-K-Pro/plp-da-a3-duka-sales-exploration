import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)
n = 1000

products = {
    "Phone": 15000,
    "Laptop": 65000,
    "Headphones": 2500,
    "Tablet": 28000,
    "Charger": 1200
}

sales = pd.DataFrame({
    "order_id": range(1001, 1001 + n),
    "order_date": pd.to_datetime("2026-01-01")
    + pd.to_timedelta(rng.integers(0, 180, n), unit="D"),
    "branch": rng.choice(
        ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"],
        n,
        p=[0.4, 0.2, 0.15, 0.15, 0.1]
    ),
    "product": rng.choice(list(products), n),
    "quantity": rng.integers(1, 6, n),
    "channel": rng.choice(
        ["In-store", "Online", "Phone order"],
        n,
        p=[0.55, 0.35, 0.10]
    ),
})

sales["unit_price"] = sales["product"].map(products)

sales.to_csv("duka_sales.csv", index=False)
