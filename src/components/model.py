import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, GlobalAveragePooling2D, Flatten, Activation, Dropout
from keras.optimizers import Adam
from keras.applications import MobileNetV2
from data_preprocessing_pipeline import img_height, img_width, class_names

# Load MobileNetV2 as the base model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(img_width, img_height, 3))
base_model.trainable = True

# Building a Feature Extraction Model

def build_model_feature_extraction(hp):
    """
    Build a Sequential model for feature extraction using MobileNetV2 as the base model.

    Args:
    - base_model (keras.Model): The pre-trained MobileNetV2 base model.
    - data_cat (list): A list containing the class names for the dataset.
    - hp (HyperParameters): An instance of the HyperParameters class for tuning hyperparameters.

    Returns:
    - model (Sequential): A compiled Keras Sequential model for feature extraction.
    """
    # Create a Sequential model
    model = Sequential()

    # Add the base model to the Sequential model
    model.add(base_model)

    # Add the GlobalAveragePooling2D layer
    model.add(GlobalAveragePooling2D())

    # Add the Flatten layer
    model.add(Flatten())

    # Add the Dense and Activation layers
    model.add(Dense(units=512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(units=256))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(units=128))
    model.add(Activation('relu'))

    model.add(Dense(units=len(class_names)))
    model.add(Activation('softmax'))

    # Choose learning rate from a predefined list
    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=hp_learning_rate), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    return model

# Configuring Fine-Tuning for Specific Layers

def build_model_fine_tuning():
    """
    Enable fine-tuning for specific layers of the base model.

    Args:
    - base_model (keras.Model): The pre-trained MobileNetV2 base model.

    Returns:
    - None
    """
    base_model.trainable = True

    set_trainable = False

    for layer in base_model.layers:
        if layer.name == 'block_6_expand':
            set_trainable = True
        if set_trainable:
            layer.trainable = True
        else:
            layer.trainable = False