# **50.038 Computational Data Science**

## *Project Demo*

**Classification** of garbage into *plastic, paper, glass, metal, cardboard using* ***InceptionV3***

<span style="display:block;">
  <img src="images/home_demo_large.gif"/>
</span>

***Team makeup:***

Jeremy Ng 1003565

Tay Kiat Hong 1003305

Yuri Kim 1002334

Daniel Teo 1003571

## Git Clone

-git clone https://github.com/EclipseEsp/50.038_CDS

## To Run on Local Machine

1. cd cdsapp/
2. npm install
3. npm build run
    - **run this everytime you update Reactjs code**
4. cd ../flaskapp/
5. python3 -m venv venv
    - to install virual environment so it does not affect your local machine
6. source venv/bin/activate
    - activates the virtual environment  
7. pip install -r -requirements.txt
    - installs the dependencies in requirements.txt
    - some dependencies will fail, if not necessary remove using `vim editor`
    - vim requirements.txt
        - remove line that has error installing
8. run app in `"flask run"` in (venv).../flaskapp
    - wait for app to deploy (afew seconds)
    - access app with http://localhost:5000
9. `alternatively`, run in `"nohup sudo python3 app.py &"` if using **AWS EC2 Instance**
    - app will run in background
10. to kill the app
    - `"pgrep python3"`
    - `"sudo kill pid"`

**Dependencies required (if requirements.txt fails eg. version not found):**

1. make sure pip is latest
2. install using pip or python -m install
    - pip intall `matplotlib`
    - pip install `numpy`
    - pip install `cmake`
    - pip install `scikit-build`
    - sudo apt-get install `python-opencv`
    - pip install `opencv-python`
    - pip install `keras` or python -m pip install `keras`
    - pip install `tensorflow` or python -m pip install `tensorflow`
    - pip install `pillow`

    *Note*: 
    - install `scikit-build` before `python-opencv`
    - using python 2.7.17
        - check with `python --version`


