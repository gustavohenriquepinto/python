import pandas as pd

people = pd.DataFrame({
    'name': ['Gustavo', 'Henrique', 'Ana'],
    'age': [19, 23, 5],
    'is_programmer': [True, False, False],    
})

people = people.rename(columns={
    'name':'first_name',
    'age':'years_old',
})

print(people.columns)

people.columns = ['NAME', 'AGE', 'PROGRAMMER']

print(people.columns)
