import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("fuelData.csv")
X = data.iloc[:,1:3].values
y = data.iloc[:,3].values

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,y)

new_data = poly_reg.fit_transform([[1500,70]])
predictedFuelEff =  lin_reg2.predict(new_data)
print("Predicted Fuel Efficiecny (km/l) -> ",predictedFuelEff)

plt.scatter(X[:,0],y,color='green')
plt.plot(X[:,0],lin_reg2.predict(X_poly),color='red')
plt.title('Fuel Efficiency Prediction')
plt.xlabel('Energy displacement(cc) & Horsepower(kW)')
plt.ylabel('Fuel Efficiency(km/l)')
plt.show()

new_data_point = poly_reg.fit_transform([[1500, 70]])
predicted_fuel_efficiency = lin_reg2.predict(new_data_point)
print("Predicted Fuel Efficiency (km/l):", predicted_fuel_efficiency)
