import kagglehub
import numpy as np
import seaborn as sns
from kagglehub import KaggleDatasetAdapter


# Load cbb dataset containing data from 2013-2024
cbb_full = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "andrewsundberg/college-basketball-dataset",
    "cbb.csv",
)

cbb_full['TOURNEY'] = np.where(cbb_full['POSTSEASON'].notnull(), True, False)
cbb_full[cbb_full['TOURNEY'] == False]

#sns.heatmap(cbb_full.corr(), cmap="YlGnBu")
#sns.set_theme(rc={'figure.figsize':(10,10)})

