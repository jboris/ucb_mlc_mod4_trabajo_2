import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser("correlation")
parser.add_argument("--data", type=str, help="Path to data")
parser.add_argument("--method", type=str, help="Method of correlation")
parser.add_argument("--color_palette", type=str, help="Color palette")
parser.add_argument("--style", type=str, help="Style")
parser.add_argument("--matrix_title", type=str, help="Matrix title")
parser.add_argument("--pairplot_title", type=str, help="Pair plot title")
parser.add_argument("--matrix_output", type=str, help="Path of matrix")
parser.add_argument("--matrix_image_output", type=str, help="Path of matrix image")
parser.add_argument("--pairplot_image_output", type=str, help="Path of Pair plot image")

args = parser.parse_args()
lines = [
    f"Data path: {args.data}",
    f"Method of correlation: {args.method}",
    f"Color palette: {args.color_palette}",
    f"Style: {args.style}",
    f"Matrix title: {args.matrix_title}",
    f"Pair plot title: {args.pairplot_title}",
    f'Path of matrix: {args.matrix_output}',
    f'Path of matrix image: {args.matrix_image_output}',
    f'Path of Pair plot image: {args.pairplot_image_output}',
]

print("Parámetros: ...")
for line in lines:
    print(line)

data = pd.read_csv(args.data)
correlation_matrix = data.corr(method=args.method)
correlation_matrix.to_csv(args.matrix_output, index=False)

plt.style.use(args.style)
fig, ax = plt.subplots(figsize=(8, 8))
cax = ax.matshow(correlation_matrix, cmap=args.color_palette, vmin=-1, vmax=1)
plt.title(args.matrix_title)
plt.colorbar(cax)
ax.set_yticks(np.arange(len(correlation_matrix.columns)))
ax.set_yticklabels(correlation_matrix.columns)
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        text = ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}', ha='center', va='center', color='black')
ax.grid(False)
plt.savefig(args.matrix_image_output)

plt.style.use(args.style)
fig, axes = plt.subplots(nrows=len(data.columns), ncols=len(data.columns), figsize=(12,12))
for i, column1 in enumerate(data.columns):
    ax = axes[i, 0]
    ax.text(-0.15, 0.5, column1, rotation=90, transform=ax.transAxes, va='center', ha='center')
    ax.axis('off')
for ax in axes.flat:
    ax.set_xticks([])
    ax.set_yticks([])
for i, column1 in enumerate(data.columns):
    for j, column2 in enumerate(data.columns):
        if i == j:
            ax = axes[i, j]
            ax.hist(data[column1], color='b', edgecolor='k', linewidth=0.5)
        else:
            ax = axes[i, j]
            ax.scatter(data[column2], data[column1], marker='o', s=15, c='b', edgecolor='k', linewidth=0.5)
plt.suptitle(args.pairplot_title)
plt.tight_layout()
plt.savefig(args.pairplot_image_output)

