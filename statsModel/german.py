import statsmodels.api as sm
import pandas as pd

def germanRegression():
    df = pd.read_csv('german_credit_data.csv')
    df.rename(columns={'Credit amount':'Credit_amount'}, inplace=True)

    y = df.Credit_amount
    X = df[['Age', 'Duration']]
    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()

    print(model.params.round(2))
    print(model.rsquared.round(2))

germanRegression()
