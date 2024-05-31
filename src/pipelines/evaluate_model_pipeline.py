import sys
import os
import tensorflow as tf
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'components')))
from data_preprocessing_pipeline import test_ds
from model_trainer_pipeline import model

# Model Evaluation on Test Data
model_test=model.evaluate(test_ds)

# Make a directory to save the model

os.mkdir('saved_models')

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model to file
with open('saved_models/Food_ingredients_classifier.tflite', 'wb') as f:
    f.write(tflite_model)