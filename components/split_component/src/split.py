import argparse
from pathlib import Path
from uuid import uuid4
from datetime import datetime
import os
from sklearn.model_selection import train_test_split
import pandas as pd

# obtener parámetros:
parser = argparse.ArgumentParser("split")
parser.add_argument("--split_data", type=str, help="Path to split data")
parser.add_argument("--split_test_rate", type=float, help="Split test rate")
parser.add_argument("--train_output", type=str, help="Path of train data")
parser.add_argument("--test_output", type=str, help="Path of test data")

args = parser.parse_args()

lines = [
    f"Split data path: {args.split_data}",
    f"Split rate: {args.split_test_rate}",
    f"Train data path: {args.train_output}",
    f"Test data path: {args.test_output}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

data = pd.read_csv(args.split_data)
train_data, test_data = train_test_split(data, test_size=args.split_test_rate, random_state=42)
train_data.to_csv(args.train_output, index=False)
test_data.to_csv(args.test_output, index=False)

