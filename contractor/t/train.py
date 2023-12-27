import tensorflow as tf
from .model import create_or_restore_model, checkpoint_dir
from .demo import get_dataset
from tensorflow import keras
from ..config import MAX_WORKERS, MIN_WORKERS

def get_train_env():
    strategy = tf.distribute.MultiWorkerMirroredStrategy()

    with strategy.scope():
        model = create_or_restore_model()

    return model


def train():
    model = get_train_env()
    train_dataset, val_dataset, test_dataset = get_dataset()

    callbacks = [
        # This callback saves a SavedModel every epoch
        # We include the current epoch in the folder name.
        keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_dir + "/ckpt-{epoch}", save_freq="epoch"
        )
    ]
    model.fit(
        train_dataset,
        callbacks=callbacks,
        validation_data=val_dataset,
        epochs=2,
        verbose=2,
    )
