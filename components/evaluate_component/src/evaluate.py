import argparse
import pandas as pd
from io import StringIO
from sklearn.metrics import classification_report

# obtener parámetros:
parser = argparse.ArgumentParser("evaluate")
parser.add_argument("--test_data", type=str, help="Test data path")
parser.add_argument("--predict_data", type=str, help="Predict data path")
parser.add_argument("--objective", type=str, help="Objective")
parser.add_argument("--target_name", type=str, help="Target name")
parser.add_argument("--report_output", type=str, help="Report data path")

args = parser.parse_args()

lines = [
    f"Test data path: {args.test_data}",
    f"Predict data path: {args.predict_data}",
    f"Objective: {args.objective}",
    f"Target name: {args.target_name}",
    f"Report data path: {args.report_output}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

test = pd.read_csv(args.test_data)[args.objective]
predict = pd.read_csv(args.predict_data)
target_names=['Not ' + args.target_name, args.target_name]
report = classification_report(test, predict, target_names=target_names)
df_report = pd.read_csv(StringIO(report), sep="\\s+")
df_report.to_csv(args.report_output)

