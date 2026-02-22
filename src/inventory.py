import pandas as pd
from config import SERVICE_LEVEL

def calculate_inventory(forecast_path="data/future_forecast.csv"):
    df = pd.read_csv(forecast_path)

    avg_demand = df["prediction"].mean()
    demand_std = df["prediction"].std()

    safety_stock = demand_std * 1.65  # ~95% service level approximation
    reorder_point = avg_demand + safety_stock

    inventory_df = pd.DataFrame({
        "Average_Demand": [avg_demand],
        "Safety_Stock": [safety_stock],
        "Reorder_Point": [reorder_point]
    })

    inventory_df.to_csv("data/inventory_decisions.csv", index=False)
    print("Inventory Calculated Successfully")

if __name__ == "__main__":
    calculate_inventory()