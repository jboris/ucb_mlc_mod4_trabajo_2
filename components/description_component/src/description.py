import argparse
import pandas as pd

# obtener parámetros:
parser = argparse.ArgumentParser("description")
parser.add_argument("--data", type=str, help="Path to data")
parser.add_argument("--info_output", type=str, help="Path of info data")
parser.add_argument("--describe_output", type=str, help="Path of describe data")

args = parser.parse_args()

lines = [
    f"Data path: {args.data}",
    f"Info data path: {args.info_output}",
    f"Describe data path: {args.describe_output}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

data = pd.read_csv(args.data)
with open(args.info_output, 'w') as file:
    data.info(buf=file)

with open(args.describe_output, 'w') as file:
    data.describe().to_string(buf=file)

