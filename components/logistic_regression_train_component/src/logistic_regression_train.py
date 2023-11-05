import argparse
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression

# obtener parámetros:
parser = argparse.ArgumentParser("logistic_regression_train")
parser.add_argument("--train_data", type=str, help="Path to train data")
parser.add_argument("--objective", type=str, help="Objective")
parser.add_argument("--model_output", type=str, help="Path of model")

args = parser.parse_args()

lines = [
    f"Split data path: {args.train_data}",
    f"Objective: {args.objective}",
    f"Model path: {args.model_output}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

data = pd.read_csv(args.train_data)
y = data[args.objective]
X = data.drop(columns=[args.objective])
model = LogisticRegression()
model.fit(X, y)
with open(args.model_output, 'wb') as file:
    pickle.dump(model, file)

