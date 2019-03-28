# Chillie-Plant-Disease-detection
Chillie Plant Disease detection using opencv and tensorflow

Download Pre Trained model from https://www.floydhub.com/shikhar10000/datasets/plantmodel/1

This code is designed to be deployed on floyd hub and make an REST end point api that takes an image  as input detects the related chilli disease , wirite its fingdings to firebase and then return the same via the same REST api


you can connect it to your firebase entering authentication information in app.py file




Working to make a version that works with firestore and can return an image with bounding boxes on the diease area  insted of just the name
