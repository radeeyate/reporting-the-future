import matplotlib.pyplot as plt

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
# data from https://agresearch.montana.edu/nwarc/weather/TempSumClndYr.html and others
avg_temps = [24.8, 24.4, 29.2, 42.0, 58.8, 61.4, 67.7, 67.3, 56.6, 44.3, 32.4, 25]
high_temps = [37, 42, 51, 62, 72, 81, 88, 87, 75, 64, 48, 39]
low_temps = [5, 10, 17, 28, 38, 45, 54, 53, 41, 30, 16, 11]
precipitation = [0.4, 0.6, 1.0, 1.5, 2.0, 1.5, 1.0, 1.2, 1.0, 1.2, 0.3, 0.5]

plt.plot(months, avg_temps, label="Average Temp (°F)")
plt.plot(months, high_temps, label="High Temp (°F)")
plt.plot(months, low_temps, label="Low Temp (°F)")
plt.bar(months, precipitation, label="Precipitation (in)")

plt.xlabel("Month")
plt.ylabel("Temperature (°F) / Precipitation (in)")
plt.title(
    "Reporting the Future - Montana Temperature and Precipitation (January - December 2023)"
)

plt.legend()
plt.xticks(rotation=45)

plt.grid(True)
plt.tight_layout()
plt.show()
