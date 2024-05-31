import os
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.utils import image_dataset_from_directory
from keras.applications.mobilenet_v2 import preprocess_input

def load_datasets(img_height=224, img_width=224, batch_size=32):
    """
    Load image datasets from directories and preprocess them.

    Args:
        img_height (int): Height of the images (default is 224).
        img_width (int): Width of the images (default is 224).
        batch_size (int): Batch size for loading datasets (default is 32).

    Returns:
        val_ds (tf.data.Dataset): Validation dataset.
        test_ds (tf.data.Dataset): Test dataset.
        train_ds (tf.data.Dataset): Training dataset.
    """
    # Dataset for validation
    val_ds = image_dataset_from_directory(
        directory=os.path.join('E:/Learnings/CookingApp/Experiment/components/converted_img', 'valid'),
        image_size=(img_height, img_width),
        batch_size=batch_size,
        labels='inferred',
        label_mode='int',
    )

    # Dataset for testing
    test_ds = image_dataset_from_directory(
        directory=os.path.join('E:/Learnings/CookingApp/Experiment/components/converted_img', 'test'),
        image_size=(img_height, img_width),
        batch_size=batch_size,
        labels='inferred',
        label_mode='int',
    )

    # Dataset for training
    train_ds = image_dataset_from_directory(
        directory=os.path.join('E:/Learnings/CookingApp/Experiment/components/converted_img', 'train'),
        image_size=(img_height, img_width),
        batch_size=batch_size,
        labels='inferred',
        label_mode='int',
    )

    return val_ds, test_ds, train_ds


def preprocess_datasets(*datasets):
    """
    Preprocess image datasets.

    Args:
        *datasets (tf.data.Dataset): Variable number of datasets.

    Returns:
        Preprocessed datasets
    """
    preprocessed_datasets = []
    for ds in datasets:
        preprocessed_ds = ds.map(lambda x, y: (preprocess_input(x), y))
        preprocessed_datasets.append(preprocessed_ds)
    return preprocessed_datasets
