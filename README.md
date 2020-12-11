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

`git clone https://github.com/EclipseEsp/50.038_CDS`

## To Run on Local Machine

1. cd cdsapp/
2. npm install
3. npm build run
    - builds a folder `/build` of the reactapp for deployment
    - ***run this command everytime you update App.js***
4. cd ../flaskapp/
5. python3 -m venv venv
    - to install virual environment so it does not affect your local machine
6. source venv/bin/activate
    - activates the virtual environment  
7. pip install -r -requirements.txt
    - installs the dependencies in requirements.txt
    - some dependencies will fail, if not necessary remove using `vim editor`
    - vim requirements.txt
        - remove the line that has error when installing
8. start *flask server* with `"flask run"` in (venv).../flaskapp
    - wait for app to deploy (take afew seconds)
    - access app with http://localhost:5000
9. **alternatively**, start with `sudo python3 app.py` if using **AWS EC2 Instance**
    - to keep app long running
    - use `nohup sudo python3 app.py &`
    - app will run in background
        - to kill the app:
            - `"pgrep python3"` to get pid
            - `"sudo kill pid"`

**Dependencies required (if requirements.txt fails eg. version not found):**

1. make sure **pip** is latest
2. install using `pip install` or `python -m pip install`
    - pip install `matplotlib`
    - pip install `numpy`
    - pip install `cmake`
    - pip install `scikit-build`
    - sudo apt-get install `python-opencv`
    - pip install `opencv-python`
    - pip install `keras` or python -m pip install `keras`
    - pip install `tensorflow` or python -m pip install `tensorflow`
    - pip install `pillow`

    *Note*: 
    
    - install `cmake` and `scikit-build` before `python-opencv`
    - project done using:
        - python 2.7.17
        - flask 1.1.2
        - nodejs v8.10.0
        - npm 6.14.8
        - cmake 3.18.4.post1
        - scikit-build 0.11.1
        - python-pip 20.3.1
        - tensorflow 2.3.1
        - keras 2.4.3
        - pillow 8.0.1



