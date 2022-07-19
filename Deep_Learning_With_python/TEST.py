import tensorflow as tf


##Find your .dll file's path and add them into environment 
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

##
### pip install graphviz 
### pip install pydot_ng
