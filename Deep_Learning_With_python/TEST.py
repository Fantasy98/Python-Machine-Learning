

import tensorflow as tf
import torch



##Find your .dll file's path and add them into environment 
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

print(tf.test.gpu_device_name())
##
### pip install graphviz 
### pip install pydot_ng

from torch import nn

points = torch.tensor([[4.0,1.0]]).to(device='cuda')
print(points) 