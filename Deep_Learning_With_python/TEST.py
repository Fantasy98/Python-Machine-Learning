from tabnanny import verbose
import tensorflow as tf


##Find your .dll file's path and add them into environment 
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

print(tf.test.gpu_device_name())
##
### pip install graphviz 
### pip install pydot_ng
