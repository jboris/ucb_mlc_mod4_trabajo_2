import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser("correlation")
parser.add_argument("--data", type=str, help="Path to data")
parser.add_argument("--method", type=str, help="Method of correlation")
parser.add_argument("--color_palette", type=str, help="Color palette")
parser.add_argument("--style", type=str, help="Style")
parser.add_argument("--matrix_title", type=str, help="Matrix title")
parser.add_argument("--diag_kind", type=str, help="Kind of plot to make")
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
    f'Kind of plot to make: {args.diag_kind}',
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

sns.set(style=args.style)
fig = plt.figure(figsize=(8, 8))
sns.heatmap(correlation_matrix, annot=True, cmap=args.color_palette, linewidths=0.5, vmin=-1, vmax=1)
plt.title(args.matrix_title)
fig.savefig(args.matrix_image_output)

plot = sns.pairplot(data, diag_kind=args.diag_kind)
plt.suptitle(args.pairplot_title)
fig = plot.fig
fig.savefig(args.pairplot_image_output) 

