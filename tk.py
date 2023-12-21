# libraries - pandas
import numpy as np
import pandas as pd

var1 = np.random.randn(100) * 5 + 20
var2 = np.random.randn(100) > 0

# labels
labels = ['Temp (C)', 'Ice Cream']

D = {labels[0]: var1, labels[1]: var2}

df = pd.DataFrame(data=D)

print(df)
print(df.mean())
