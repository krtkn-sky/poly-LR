# Fuel Efficiency Prediction

## Dataset Description

This dataset contains information about various car models and their corresponding engine displacement (in cubic centimeters, cc), horsepower (in kilowatts, kW), and fuel efficiency (in kilometers per liter, km/l). The goal is to predict fuel efficiency based on engine displacement and horsepower.

| Car Model       | Engine Displacement (cc) | Horsepower (kW) | Fuel Efficiency (km/l) |
| --------------- | ------------------------- | --------------- | ------------------------ |
| Phantom Fury    | 1000                     | 50              | 20                      |
| Ghost Glide     | 1200                     | 55              | 21                      |
| Sapphire Storm  | 1500                     | 70              | 18                      |
| Midnight Beast  | 1800                     | 75              | 17                      |
| Thunder Strike  | 2000                     | 85              | 16                      |
| Firestorm       | 2200                     | 95              | 15                      |
| Lunar Cruiser   | 2500                     | 100             | 14                      |
| Solar Flare     | 2800                     | 110             | 13                      |
| Eclipse Blaze   | 3000                     | 120             | 12                      |
| Starblaze       | 3200                     | 130             | 11                      |
| Viper Strike    | 3500                     | 140             | 10                      |
| Shadow Serpent  | 3800                     | 150             | 9                       |
| Phantom Wraith  | 4000                     | 160             | 8                       |
| Titan Thunder   | 4200                     | 170             | 7                       |
| Dark Destroyer  | 4500                     | 180             | 6                       |

## Python Code

The Python code provided in this repository uses polynomial regression to predict fuel efficiency based on the provided dataset. The code is implemented using the scikit-learn library for machine learning.

You can tweak the `degree` parameter in the PolynomialFeatures to achieve more precise regression predictions. For instance, setting `degree=2` may yield a more accurate prediction depending on the dataset and the underlying relationship.

### Dependencies

To run the code, you will need to have the following Python libraries installed:

- NumPy
- Matplotlib
- Pandas
- scikit-learn

You can install these dependencies using pip:

```bash
pip install numpy matplotlib pandas scikit-learn

