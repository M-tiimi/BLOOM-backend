# BLOOM-backend
## M-Team
Juulia Jokinen, Jelena Laakkonen, Veera Leppänen, Anne-Mari Mannila, Areta Santos
## Project idea
This project was created during Haaga-Helia's Software Poject II -course in fall 2021. In this project, the idea is to create an app ment for aiding user in taking care of their physical and mental health. This is done with few different functionalities. This is the backend for https://github.com/M-tiimi/BLOOM-frontend. BLOOM-backend also offers an open Machine Learning API for text sentiment analysis. 

##Machine Learning API Documentation

https://bloom-app.azurewebsites.net/ml-model/

**POST {"data":"text"}**

**Text length should be 100-422 words for the Machine Learning model.**

### Example of POST answer


![answer_mml_model](https://user-images.githubusercontent.com/70891200/144716811-f1496a26-3b32-4965-81a3-561d585f69d0.png)
