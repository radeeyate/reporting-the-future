import matplotlib.pyplot as plt
import csv

# math is hard. some of these might be inconsistent, but I tried my hardest.
totalPopulation = [20, 60, 70, 1570, 3570, 4370, 5070, 7695, 15210, 17710, 20000]
childPopulation = [0, 0, 0, 560, 1405, 2050, 2780, 4305, 8010, 9410, 10590]
novaTerraBirths = [0, 0, 5, 60, 105, 450, 890, 1515, 2160, 2060, 2350]
earthBornKids = [0, 0, 0, 500, 1300, 1600, 1800, 2600, 5360, 5860, 6750]
years = [2050, 2057, 2065, 2072, 2079, 2082, 2089, 2090, 2092, 2097, 2100]

# save to CSV file for external use
with open("population_data.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        [
            "Year",
            "Total Population",
            "Child Population",
            "Nova Terra Births",
            "Earth Born Kids",
        ]
    )
    for i in range(len(years)):
        writer.writerow(
            [
                years[i],
                totalPopulation[i],
                childPopulation[i],
                novaTerraBirths[i],
                earthBornKids[i],
            ]
        )

# plotting the population
plt.plot(years, totalPopulation, label="Total Population")
plt.plot(years, novaTerraBirths, label="Nova Terra Births")
plt.plot(years, earthBornKids, label="Children from Earth")
plt.plot(years, childPopulation, label="Total Child Population")

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Reporting the Future - Population Growth")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.legend()

plt.show()
