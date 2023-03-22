# Работать с файлом california_housing_train.csv,
# который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd
df = pd.read_csv(
    'https://storage.googleapis.com/mledu-datasets/california_housing_train.csv')

print(round(df[(df['population'] > 0) & (df['population'] <= 500)]
      ['median_house_value'].mean()))


# Узнать какая максимальная households в зоне минимального значения population

df = pd.read_csv(
    'https://storage.googleapis.com/mledu-datasets/california_housing_train.csv')

print(max(df[(df['population']) == min(df['population'])]['households']))
