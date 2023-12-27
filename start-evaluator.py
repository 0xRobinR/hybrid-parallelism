import tensorflow as tf
from contractor.t.model import create_or_restore_model, checkpoint_dir
from contractor.t.demo import get_dataset
from tensorflow import keras

def get_train_env():
    strategy = tf.distribute.MirroredStrategy()
    with strategy.scope():
        model = create_or_restore_model()

    return model


def evaluate():
    model = get_train_env()
    train_dataset, val_dataset, test_dataset = get_dataset()

    results = model.evaluate(val_dataset)
    print(results)


evaluate()
