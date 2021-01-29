#
# fashion-mnist TensorFlow 2.4
#
# Platform        CPU                   OS               TF            Elapsed Time (Seconds)
#
# MacbookPro      1.4GHz Quad-Core i5  11.1              2.4.1         14.4
# MacbookPro      1.4GHz Quad-Core i5  11.1              2.4.0-rc0     19.2
# binder.org      1GhZ Xeon Gold 6140  Debian-Buster     2.4.1         167
# google-collab                                          2.4.0         36

#import libraries
import tensorflow as tf
import time

#
# MacOS 11.1 TensorFlow build
#
# Select CPU device. Available options are 'cpu', 'gpu', and 'any'.
# from tensorflow.python.compiler.mlcompute import mlcompute
# mlcompute.set_mlc_device(device_name='any')
#

#download fashion mnist dataset
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_set_count = len(train_labels)
test_set_count = len(test_labels)

#setup start time
t0 = time.time()

#normalize images
train_images = train_images / 255.0
test_images = test_images / 255.0

#create ML model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

#compile ML model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#train ML model
model.fit(train_images, train_labels, epochs=10)

#evaluate ML model on test set
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

#setup stop time
t1 = time.time()
total_time = t1-t0

#print results
print('\n')
print('TensorFlow Version: {0}'.format(tf.__version__))
print(f'Training set contained {train_set_count} images')
print(f'Testing set contained {test_set_count} images')
print(f'Model achieved {test_acc:.2f} testing accuracy')
print(f'Training and testing took {total_time:.2f} seconds')

