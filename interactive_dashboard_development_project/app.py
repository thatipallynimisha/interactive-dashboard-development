
import pandas as pd
import matplotlib.pyplot as plt

# Sample business performance dataset
df = pd.read_csv("business_data.csv")

print("\nBusiness Data:\n")
print(df)

# Total sales
total_sales = df["Sales"].sum()
avg_profit = df["Profit"].mean()

print("\n--- Dashboard Insights ---")
print(f"Total Sales: {total_sales}")
print(f"Average Profit: {avg_profit:.2f}")

# Sales Chart
plt.figure(figsize=(6,4))
plt.bar(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Performance")
plt.savefig("sales_chart.png")

# Profit Chart
plt.figure(figsize=(6,4))
plt.plot(df["Month"], df["Profit"], marker='o')
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit Trend")
plt.savefig("profit_chart.png")

print("\nCharts generated successfully:")
print("1. sales_chart.png")
print("2. profit_chart.png")

# Suggestions
print("\n--- Actionable Insights ---")
print("1. Focus on months with lower sales.")
print("2. Increase marketing during low-profit periods.")
print("3. Improve customer engagement strategies.")
print("4. Monitor monthly trends for better decisions.")
