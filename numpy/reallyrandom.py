import numpy as np
import numpy as np
import pandas as pd
import sys

seed = np.random.seed(42)

rows = int(sys.argv[1])
columns = int(sys.argv[2])


def randDF():
    df = pd.DataFrame(np.random.randint(0, 100, size=(rows, columns)))
    print(df)

randDF()