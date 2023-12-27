import tensorflow as tf


class Model(tf.keras.models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layers.append(tf.keras.layers.InputLayer(input_shape=(2,)))
