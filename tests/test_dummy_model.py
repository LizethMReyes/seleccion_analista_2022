from pollos_petrel import get_mean_target, read_trainig_dataset


# Lee train.csv
def test_read_training_dataset():
    training_dataset = read_trainig_dataset()
    obtained_n_rows = training_dataset.shape[0]
    expected_n_rows = 1304
    assert expected_n_rows == obtained_n_rows


# Calcula promedio de target
def test_get_mean_target():
    get_mean_target()


# Lee test.csv
# Tira todas las columnas excepto id
# Agrega columna target con el promedio
# Guarda el archivo con sufijo _submission.csv
