# Gradient Descent Statistical Data Analysis

## Project Overview

This project presents a Python-based statistical data analysis using datasets covering the period from 2010 to 2021.

The project focuses on analyzing demographic and socio-economic data, creating visualizations, and applying a gradient descent-based statistical model to study the relationship between input and output variables.

## Objectives

- Analyze datasets from 2010–2021.
- Perform statistical and numerical analysis using Python.
- Apply the gradient descent optimization technique.
- Study patterns and trends in the available data.
- Create visualizations for better understanding of the datasets.
- Compare the gradient descent result with the closed-form solution.

## Dataset

The project contains Excel datasets for the years 2010–2021.

All datasets are stored in the `Data` folder.

### Dataset Files

- table-6-2_2010.xlsx
- table-6-2_2011.xlsx
- table-6-2_2012.xlsx
- table-6-2_2013.xlsx
- table-6-2_2014.xlsx
- table-6-2_2015.xlsx
- table-6-2_2016.xlsx
- table-6-2_2017.xlsx
- table-6-2_2018.xlsx
- table-6-2_2019.xlsx
- table-6-2_2020.xlsx
- table-6-2_2021.xlsx

## Data Visualization

The project contains plots representing different aspects of the data:

1. State-wise Data Analysis
2. Population and Growth Rate
3. Economy
4. Unemployment
5. Literacy Rate

## Methodology

The project uses gradient descent as an optimization technique to fit a
simple linear model, `y = w * x + b`, where `w` is the weight (slope) and
`b` is the bias (intercept).

The model performs the following steps:

1. Standardize `x` and `y` (zero mean, unit variance) so the learning rate
   behaves consistently regardless of the raw data's scale.
2. Calculate predicted values.
3. Calculate the prediction error.
4. Calculate the squared error and Mean Squared Error (MSE).
5. Calculate the gradients with respect to `w` and `b`.
6. Update both `w` and `b` using gradient descent.
7. Repeat the process for multiple iterations.
8. Convert the learned `w` and `b` back to the original (un-standardized)
   scale.
9. Compare the final result with the closed-form (ordinary least squares)
   solution.

The weight and bias are updated using the gradient descent equations:

```
w_new = w - learning_rate × gradient_w
b_new = b - learning_rate × gradient_b
```

## Gradient Descent Model

The Python implementation uses an initial weight and bias, and a learning
rate, to iteratively minimize the Mean Squared Error between predicted and
observed values.

The model uses:

- Initial weight: `0.0`
- Initial bias: `0.0`
- Learning rate: `0.05` (applied to standardized data)
- Number of iterations: `1000`

The gradients are calculated from the prediction error together with the
input variable (for `w`) and directly from the error (for `b`).

## Results

The gradient descent algorithm is applied iteratively to reduce the error
between the predicted and observed values. Both the weight and bias
converge, and the final result is compared with the analytical closed-form
(OLS) solution to check the optimization is correct.

### Result Files

The detailed numerical results are available in the `Results` folder.

- `gradient_descent_results.txt` – Summary of the gradient descent results.
- `results.csv` – Iteration-wise results including weight, bias, MSE, and
  gradients (on the standardized scale).
- `final_result.png` – Convergence plot (MSE vs. iteration) alongside the
  fitted line plotted against the actual data.

### Gradient Descent Convergence

![Gradient Descent Convergence](Results/final_result.png)

### Numerical Results

Example output using the built-in sample dataset (values will differ when
run against a real file from `Data/`):

| Parameter               |        Value |
|--------------------------|-------------:|
| Initial Weight           |          0.0 |
| Initial Bias             |          0.0 |
| Learning Rate            |         0.05 |
| Number of Iterations     |         1000 |
| Final Weight             |   724.181818 |
| Final Bias               |  9389.200000 |
| Closed-Form Weight       |   724.181818 |
| Closed-Form Bias         |  9389.200000 |
| Weight Difference        |     0.000000 |
| Bias Difference          |     0.000000 |

The full numerical results — including the final weight, bias, MSE, and
their differences from the closed-form solution — are written to the
`Results` folder on every run.

## Technologies Used

- Python
- Microsoft Excel
- VS Code
- Git
- GitHub
- Matplotlib
- pandas / openpyxl (for reading Excel datasets, optional)

## Project Structure

```text
Gradient-Descent-Statistical-Model/
│
├── Data/
│   ├── table-6-2_2010.xlsx
│   ├── table-6-2_2011.xlsx
│   ├── table-6-2_2012.xlsx
│   ├── ...
│   └── table-6-2_2021.xlsx
│
├── Gradient-Descent-Statistical-Model.py
│
├── Results/
│   ├── gradient_descent_results.txt
│   ├── results.csv
│   └── final_result.png
│
├── plots/
│   ├── data_by_state.png
│   ├── population.png
│   ├── economy.png
│   ├── unemployment.png
│   └── literacy_rate.png
│
└── README.md
```
