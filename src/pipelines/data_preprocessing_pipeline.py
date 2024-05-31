import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'components')))

from data_preprocessing import load_datasets, preprocess_datasets

# Define global variables
img_height = 224
img_width = 224
batch_size = 32

# Call data preprocessing functions
val_ds, test_ds, train_ds = load_datasets(img_height, img_width, batch_size)

class_names = val_ds.class_names

# Preprocess datasets
val_ds, test_ds, train_ds = preprocess_datasets(val_ds, test_ds, train_ds)
