# Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os

DATA_DIR = './data'

# Load data
trainpath = os.path.join(DATA_DIR, 'train.csv')
train = pd.read_csv(trainpath)
testpath = os.path.join(DATA_DIR, 'test.csv')
test = pd.read_csv(testpath)

# Pre-Processing
