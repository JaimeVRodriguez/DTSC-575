import statsmodels.api as sm
import pandas as pd
import numpy as np

def bathPredit():
    df = pd.read_csv('sacramento.csv')
    df.baths2 = np.select([(df.baths == 1), df.baths > 1], [0, 1])

    y = df.baths2
    X = df[['beds', 'sqft', 'price']]
    X = sm.add_constant(X)

    model = sm.Logit(y, X).fit()

    print(model.params.round(2))
    print(model.pvalues.round(2))
    print('The smallest p-value is for sqft')

bathPredit()