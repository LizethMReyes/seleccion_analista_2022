import pandas as pd


# Lee train.csv
def read_training_dataset():
    training_dataset_path = "pollos_petrel/train.csv"
    training_dataset = pd.read_csv(training_dataset_path)
    return training_dataset


# Calcula promedio de target
def get_mean_target(dataset: pd.DataFrame) -> float:
    mean_target = dataset["target"].mean()
    return mean_target


# Lee test.csv
def read_testing_dataset():
    testing_dataset_path = "pollos_petrel/test.csv"
    testing_dataset = pd.read_csv(testing_dataset_path)
    return testing_dataset


# Tira todas las columnas excepto id
def drop_all_but_id(dataset: pd.DataFrame) -> float:
    dataset_only_id = dataset[["id"]]
    return dataset_only_id


# Agrega columna target con el promedio
def add_mean_as_target(dataset):
    dataset["target"] = 0
    return dataset

# Guarda el archivo con sufijo _submission.csv
