from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np
import pandas as pd




np.random.seed(42)
count = 1000

# хар-ки: вік, площа, к-сть кімнат, розташування 

age = np.random.randint(1900, 2024, count)
area = np.random.uniform(30,200, count)
rooms = np.random.randint(1,6, count)
distance = np.random.uniform(1,20, count)
#location = np.random.choice(['Центр міста', 'Село', 'Біля моря'], count)


price = (area * 1000) + (rooms * 4000) + ((2024 - age) * 500) - (distance * 2000)

data = pd.DataFrame({
    "Area": area,
    "Rooms": rooms,
    "Age": age,
    "Distance": distance,
    "Price": price
})

x = data.drop("Price", axis = 1)
y = data["Price"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state = 42)


sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


model = GradientBoostingRegressor(n_estimators = 100, random_state = 42)
model.fit(x_train, y_train)

predictions = model.predict(x_test)

new_data = pd.DataFrame({
    "Area": [73.2],
    "Rooms": [2],
    "Age": [2011],
    "Distance": [3]
})

final_data = sc.transform(new_data)
prediction = model.predict(final_data)
print(f'Прогнозована ціна квартири: ${prediction[0]}')












