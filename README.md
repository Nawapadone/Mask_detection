# Mask detection when going to public places
> The outbreak of COVID-19 causes measures to prevent transmission from person to person. everyone must stay in the house but because people who must travel to work and study, this type of work habit can adversely affect the spread of the virus. The government has measures to protect everyone by wearing a mask whenever in public.
> Because in public places there is an access inspection using CCTV This project aims to use Machine Learning to classify the Facial recognition from the face of the user to check whether the person is wearing mask on face or not.

## Model Training
> The training data was pulled from the labeled facial recognition dataset from Kaggle in the CSV format. We use the machine learning process, as the Cascade function is taught through image analysis. Which is divided into two groups which are the group of images is correct. Which is a picture of something that we want to detect In various formats But must be cut off other parts Leaving only parts of what we want And general image groups Which don't have anything that we want to detect in the picture In order to be able to detect the information In other images.
> The technique used for model training was Cascade Classifier. It is a form of Object Detection using Haar feature-based cascade classifiers is effective object detection.
> I first tried to train the model on my laptop. But it took a long time (almost 15 minutes) to even train a single epoch since it does not have a graphic card to accelerate model training.
> The method that we use to detect is divided into 4 parts, which we will start by detecting the structure of the object (face frame). When we meet, we will detect the eyes to check for that is the face and then we will detect the nose and mouth. If detected, it means that you are not wearing a mask.
> However, in actual use, there are variables regarding the suitability of image size. A part of the accuracy depends on the frame rate for image transmission to be processed from the CCTV. if sending a picture data that is too often will cause RAM to work harder.




