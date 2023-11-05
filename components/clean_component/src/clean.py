import argparse
import pandas as pd

# obtener parámetros:
parser = argparse.ArgumentParser("clean")
parser.add_argument("--data", type=str, help="Path to data")
parser.add_argument("--method", type=str, help="Method to clean")
parser.add_argument("--clean_data_output", type=str, help="Path of clean data")

args = parser.parse_args()

lines = [
    f"Data path: {args.data}",
    f"Method to clean: {args.method}",
    f"Path of clean data: {args.clean_data_output}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

data = pd.read_csv(args.data)
if args.method == 'delete':
    data = data.dropna()
elif args.method == 'mean':
    data = data.fillna(data.mean())
data.to_csv(args.clean_data_output, index=False)

