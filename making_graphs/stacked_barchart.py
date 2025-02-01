import matplotlib.pyplot as plt
import numpy as np

species = ("A", "B", "C", "D", "E")

gender = {"male": np.array([1, 2, 3, 4, 1]), "female": np.array([5, 4, 3, 2, 1])}

width = 0.35

fix, ax = plt.subplots()
bottom = np.zeros(5)

for gender, values in gender.items():
    p = ax.bar(species, values, width, label=gender, bottom=bottom)
    bottom += values

ax.set_title("Stacked Bar Chart")
ax.legend(loc="upper right")
plt.savefig("barchart.png")
