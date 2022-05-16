## Calculate mean squared error between source and target images.

import numpy as np


def calc_mse(source, target, color_chart_area):
  source = np.reshape(source, [-1, 1]).astype(np.float64)
  target = np.reshape(target, [-1, 1]).astype(np.float64)
  mse = sum(np.power((source - target), 2))
  return mse / ((np.shape(source)[
    0]) - color_chart_area)
