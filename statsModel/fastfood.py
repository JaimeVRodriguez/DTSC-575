import statsmodels.api as sm
import pandas as pd

def regression():
    df = pd.read_csv('fastfood.csv')

    X = df[['total_fat', 'sat_fat', 'cholesterol', 'sodium']]
    X = sm.add_constant(X)

    y = df.calories

    model = sm.OLS(y, X).fit()
    
    print(model.mse_total.round(2))
    print(model.rsquared.round(2))
    print(model.params.round(2))
    print(model.pvalues.round(2))

regression()