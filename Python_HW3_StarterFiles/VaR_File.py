import numpy as np

def VaR(r, confidence, principal=1):

    percentile = np.percentile(r, (1-confidence)*100)

    out = abs(percentile) * principal

    return out
