# **Behavioral Cloning** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./1.jpg "Center Image"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of a convolution neural network with 3x3 filter sizes and depths between 32 and 128 (model.py lines 18-24) 

The model includes ELU layers to introduce nonlinearity, the input layer is cropped to exclude noise from the sky and environment, and the data is normalized in the model using a Keras lambda layer. 

#### 2. Attempts to reduce overfitting in the model

I had intended to add dropout layers and augment my data after testing out my model if I had noticed that my network was overfitting on my dataset, but my network completed track 1 flawlessly, and didn't show any signs of overfitting. Because of this, I didn't feel the need to augment data and add dropout layers.

#### 3. Model parameter tuning

The model used an adam optimizer, and error was computed using Mean-Squared Error.

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I only used the center images, cropped out in the first layer. 

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

My first step was to use a convolution neural network model similar to Nvidia's paper, End to End Deep Learning for Self-Driving Cars. The model was introduced in the project hints, so I decided to use it.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my model had a similar loss when training vs. testing, so the network was able to generalize the data well.

The final step was to run the simulator to see how well the car was driving around track one. The vehicle was rather slow, and it almost veered off the track at a few sharp turns, but corrected itself eventually. At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The model architecture consisted of a convolution neural network with the following layers, layer sizes, and parameters:

Layer (type) | Output Shape | Param #   
---|---|---
cropping2d_1 (Cropping2D) | (None, 75, 320, 3) | 0         
lambda_1 (Lambda) | (None, 75, 320, 3) | 0         
conv2d_1 (Conv2D) | (None, 36, 158, 24) | 1824      
conv2d_2 (Conv2D) | (None, 16, 77, 36) | 21636     
conv2d_3 (Conv2D) | (None, 6, 37, 48) | 43248     
conv2d_4 (Conv2D) | (None, 4, 35, 64) | 27712     
conv2d_5 (Conv2D) | (None, 2, 33, 64) | 36928     
flatten_1 (Flatten) | (None, 4224) | 0         
dense_1 (Dense) | (None, 1162) | 4909450   
dense_2 (Dense) | (None, 100) | 116300    
dense_3 (Dense) | (None, 50) | 5050      
dense_4 (Dense) | (None, 10) | 510       
dense_5 (Dense) | (None, 1) | 11        


Total params: 5,162,669
Trainable params: 5,162,669
Non-trainable params: 0



#### 3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded 6 laps on track one using center lane driving, three laps going in the initial direction, and three laps in the opposite direction. This was due to the fact that there are more left turns than right turns on the track, which would make the network less likely to generalize the right turns. By going the opposite direction, we have the same number of left and right turns. Here is an example image of center lane driving:

![alt text][image1]

After the collection process, I had around 10,000 data points. I then preprocessed this data by simply adding a cropping2d layer after the Input layer. I then normalized the data using a Lambda layer.1


I finally randomly shuffled the data set and put 20% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was Z as evidenced by ... I used an adam optimizer so that manually training the learning rate wasn't necessary.
