# Generated Bt Gpt


import numpy as np
import matplotlib.pyplot as plt
#  1. Basic Bar Plot


x = ['A', 'B', 'C']
y = [3, 7, 5]

plt.bar(x, y)
plt.show()

#  2. Bar Orientation

# Vertical bar: plt.bar(...)

# Horizontal bar: plt.barh(...)

plt.barh(x, y)

#  3. Bar Width & Height

# width(for bar) or height(for barh)

plt.bar(x, y, width=0.4)

#  4. Color Customization

# color: solid colors or colormap

# edgecolor: border color

# linewidth: border width

plt.bar(x, y, color='skyblue', edgecolor='black', linewidth=1.5)

#  5. Transparency

# alpha: 0 (transparent) to 1 (opaque)

plt.bar(x, y, alpha=0.7)

#  6. Hatch Patterns

#  Hatch styles like /, \, |, -, +, x, o, O, .

plt.bar(x, y, hatch='//')

#  7. Bar Alignment

# align = 'center' or align = 'edge'

plt.bar(x, y, align='edge')

#  8. Labels and Titles

plt.title("Bar Plot Example")
plt.xlabel("Category")
plt.ylabel("Values")

#  9. Error Bars

errors = [0.5, 0.2, 0.3]
plt.bar(x, y, yerr=errors, capsize=5)

#  10. Grouped(Side-by-side) Bars

labels = ['A', 'B', 'C']
group1 = [3, 7, 5]
group2 = [4, 6, 8]
x = np.arange(len(labels))
width = 0.35

plt.bar(x - width/2, group1, width, label='Group 1')
plt.bar(x + width/2, group2, width, label='Group 2')
plt.xticks(x, labels)
plt.legend()

#  11. Stacked Bars

plt.bar(x, group1, label='Group 1')
plt.bar(x, group2, bottom=group1, label='Group 2')
plt.legend()

#  12. Logarithmic Scale

plt.yscale('log')

#  13. Bar Labels(value on top of bars)

bars = plt.bar(x, y)
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height()}', ha='center', va='bottom')

#  14. Custom Tick Labels

plt.xticks(rotation=45)

#  15. Adding Grid

plt.grid(True, axis='y', linestyle='--', alpha=0.7)
