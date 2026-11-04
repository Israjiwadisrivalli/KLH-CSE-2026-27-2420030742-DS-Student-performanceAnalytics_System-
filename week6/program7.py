import seaborn as sns
import numpy as np
data=np.random.randint(1,100,(10,10))
sns.heatmap(data,cmap='tab20',annot=True)