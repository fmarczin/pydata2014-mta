import numpy as np
from matplotlib import pyplot as plt 


def evaluate(pred, truth):
    mae = np.mean(np.abs(pred - truth))
    plt.plot(pred, label='prediction')
    plt.plot(truth, label='truth')
    plt.title("MAE: {:.2f}".format(mae))
    plt.legend()
    plt.show()
    return mae
