import matplotlib.pyplot as plt

data = [1500, 10000, 9000, 700]
labels = ["Elders (65+)", "Adults (18-64)", "Children (5-17)", "Babies (0-4)"]

plt.figure(figsize=(8, 8))
plt.pie(data, labels=labels, autopct="%1.1f%%", startangle=90, colors=["gold", "lightgreen", "lightblue", "pink"])
plt.title("Population Distribution")
plt.legend(loc="best")
plt.axis("equal")

plt.show()