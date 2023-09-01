![image](https://github.com/MainakRepositor/Dementia-Imager/assets/64016811/d80cfcdb-4822-4833-9271-1200df46d8fe)

## Our Model
Below is the summary of our CNN model which we have made using python and keras.

### Model for Covid & Pneumonia Classification

| Layer (type)                  | Output Shape             | Param #     |
|-------------------------------|--------------------------|-------------|
| conv2d (Conv2D)               | (None, 222, 222, 32)     | 896         |
| max_pooling2d (MaxPooling2D)  | (None, 111, 111, 32)     | 0           |
| conv2d_1 (Conv2D)             | (None, 109, 109, 64)     | 18496       |
| max_pooling2d_1 (MaxPooling2D)| (None, 54, 54, 64)       | 0           |
| conv2d_2 (Conv2D)             | (None, 52, 52, 128)      | 73856       |
| max_pooling2d_2 (MaxPooling2D)| (None, 26, 26, 128)      | 0           |
| flatten (Flatten)             | (None, 86528)            | 0           |
| dense (Dense)                 | (None, 128)              | 11075712    |

As you can see this is a simple Neural Network with 8 layers. (this had an accuracy of approx 0.93 on average)
Each Layer has a specific job in order to get the desired output, they are :-

- Convolutional layer (conv2d): This layer takes an input image and applies a set of 32 filters to produce 32 output feature maps. Each filter extracts a particular feature from the image. The output of this layer has a shape of (None, 222, 222, 32).

- Max pooling layer (max_pooling2d): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 111, 111, 32).

- Convolutional layer (conv2d_1): This layer applies a set of 64 filters to the output of the previous layer to produce 64 output feature maps. The output of this layer has a shape of (None, 109, 109, 64).

- Max pooling layer (max_pooling2d_1): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 54, 54, 64).

- Convolutional layer (conv2d_2): This layer applies a set of 128 filters to the output of the previous layer to produce 128 output feature maps. The output of this layer has a shape of (None, 52, 52, 128).

- Max pooling layer (max_pooling2d_2): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 26, 26, 128).

 - Flatten layer (flatten): This layer flattens the output of the previous layer into a 1D vector. The output of this layer has a shape of (None, 86528).

- Fully connected layer (dense): This layer takes the flattened vector from the previous layer and applies 128 neurons to it, producing a 128-dimensional output. The output of this layer has a shape of (None, 128).


