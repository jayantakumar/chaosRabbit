import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("NoPertubationData",sep="\t")
print(df)
plt.plot(df["q_delivered_rate"][25:])
plt.show()