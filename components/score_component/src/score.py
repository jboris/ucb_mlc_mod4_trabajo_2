import argparse
import pickle
import pandas as pd

# obtener parámetros:
parser = argparse.ArgumentParser("score")
parser.add_argument("--model", type=str, help="Path to model")
parser.add_argument("--test_data", type=str, help="Path of test data")
parser.add_argument("--objective", type=str, help="Objective")
parser.add_argument("--predict_output", type=str, help="Path of predict data")

args = parser.parse_args()

lines = [
    f"Path to model: {args.model}",
    f"Path of test data: {args.test_data}",
    f"Objective: {args.objective}",
    f"Path of predict data: {args.predict_output}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

model = pickle.load(open(args.model, "rb"))
test_data = pd.read_csv(args.test_data)
test_X = test_data.drop(columns=[args.objective])
predict = pd.DataFrame(model.predict(test_X))
predict.to_csv(args.predict_output, index=False)

