import pandas
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

if __name__ == '__main__':
    # import the data as a pandas dataframe object
    df = pandas.read_csv("sample_data.csv")

    # plot a 100 bin histogram of the "AIR_TIME" column
    plt.hist(df['AIR_TIME'], bins=100)
    plt.show()
    plt.clf()

    # get values from our "AIR_TIME" column
    transform = np.asarray(df[['AIR_TIME']].values)

    # transform values and store as "dft"
    dft = stats.boxcox(transform)[0]

    # plot the transformed data
    plt.hist(dft, bins=100, color='red')
    plt.show()
