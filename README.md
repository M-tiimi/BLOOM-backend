# BLOOM-backend
## M-Team
Juulia Jokinen, Jelena Laakkonen, Veera Leppänen, Anne-Mari Mannila, Areta Santos
## Project idea
This project was created during Haaga-Helia's Software Poject II -course in fall 2021. This project is the backend for https://github.com/M-tiimi/BLOOM-frontend. BLOOM-backend also offers an open Machine Learning API for text sentiment analysis.
## Built with
- [Django](https://www.djangoproject.com/)

- [Django REST framework](https://www.django-rest-framework.org/)

- [Python](https://www.python.org/)

- [Tensorflow + Keras](https://www.tensorflow.org/)



## Machine Learning REST API Documentation
The Machine Learning model is trained with 
https://raw.githubusercontent.com/jbrownlee/Datasets/master/review_polarity.tar.gz movie review data, that is comprised of 1000 positive reviews and 1000 negative reviews.

Link to API: https://bloom-app.azurewebsites.net/ml-model/

Example request from commandline: curl -d "data=I am so happy" https://bloom-app.azurewebsites.net/ml-model/


| Request  | Data format|
| ------------- | ------------- |
| POST  |  { "data": "text" }  |



**Text length should be >100 words for the Machine Learning model. If answer is <0,5 text is analyzed as negative if >0,5 text is analyzed as positive.**

### Example of POST answer


![answer_mml_model](https://user-images.githubusercontent.com/70891200/144716811-f1496a26-3b32-4965-81a3-561d585f69d0.png)


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.


