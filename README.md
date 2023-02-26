# Face-Blurring

  I build this pipeline to solve the Face Blurring   : 

## 1- First, look at a picture and find all the faces in it.

The first step in our pipeline is face detection. Obviously we need to locate the faces in a photograph before we blur them 
Second, focus on each face and be able to understand that even if a face is turned in a weird direction or in bad lighting, it is still the same person.
Third, be able to pick out unique features of the face that you can use to tell it apart from other people— like how big the eyes are, how long the face is, etc.
Finally, compare the unique features of that face to all the people you already know to determine the person’s name.


So what is Haar Cascade? It is an Object Detection Algorithm used to identify faces in an image or a real time video. 
The algorithm uses edge or line detection features proposed by Viola and Jones in their research paper
“Rapid Object Detection using a Boosted Cascade of Simple Features” published in 2001. 
The algorithm is given a lot of positive images consisting of faces, and a lot of negative images not consisting of any face to train on them.
The model created from this training is available at the OpenCV GitHub repository https://github.com/opencv/opencv/tree/master/data/haarcascades , i used this file in the my projects . 
The repository has the models stored in XML files, and can be read with the OpenCV methods. 
![image](https://user-images.githubusercontent.com/97835837/221394726-5b1f9264-2c56-41ff-b919-0f0bcd90dacf.png) 

The first contribution to the research was the introduction of the haar features shown above. These features on the image makes it easy to find out the edges or the lines in the image, or to pick areas where there is a sudden change in the intensities of the pixels.

  
## 2- Second, draw a square around the detected faces in the image .

## 3- Finally, apply Gaussian Blur 

The Gaussian blur feature is obtained by blurring (smoothing) an image using a Gaussian function to reduce the noise level . It can be considered as a nonuniform low-pass filter that preserves low spatial frequency and reduces image noise and negligible details in an image. It is typically achieved by convolving an image with a Gaussian kernel. 
