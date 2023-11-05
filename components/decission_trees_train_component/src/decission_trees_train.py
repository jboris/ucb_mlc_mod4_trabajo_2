import argparse
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# obtener parámetros:
parser = argparse.ArgumentParser("decission_trees_train")
parser.add_argument("--train_data", type=str, help="Path to train data")
parser.add_argument("--objective", type=str, help="Objective")
parser.add_argument("--criterion", type=str, help="Criterion")
parser.add_argument("--min_samples_split", type=int, help="The minimum number of samples required to split an internal node")
parser.add_argument("--max_depth", type=int, help="The maximum depth of the tree")
parser.add_argument("--model_output", type=str, help="Path of model")

args = parser.parse_args()

lines = [
    f"Split data path: {args.train_data}",
    f"Objective: {args.objective}",
    f"Criterion: {args.criterion}",
    f"Minimum number of samples to split: {args.min_samples_split}",
    f"Maximum depth: {args.max_depth}",
    f"Model path: {args.model_output}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

data = pd.read_csv(args.train_data)
y = data[args.objective]
X = data.drop(columns=[args.objective])
model = DecisionTreeClassifier(criterion=args.criterion, min_samples_split=args.min_samples_split, max_depth=args.max_depth)
model.fit(X, y)
with open(args.model_output, 'wb') as file:
    pickle.dump(model, file)

