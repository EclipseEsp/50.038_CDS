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

- `git clone https://github.com/EclipseEsp/50.038_CDS`
- `sudo apt-get install git-lfs` (pull the InceptionV3 Model stored in github using Git Large File Storage )
- `git-lfs pull`

## To Run The App 

Note: Make sure **nodejs, flask and pip** is installed ***before starting on the steps below:*** refer to **Dependencies required**. Check versions with node -v, npm -v, flask --version, pip -V, pip3 -V

1. cd cdsapp/
2. npm install
3. npm run build
    - builds a folder `/build` of the reactapp for deployment
    - ***run this command everytime you update App.js***
4. cd ../flaskapp/
5. python3 -m venv venv
    - to install virual environment so it does not affect your local machine
6. source venv/bin/activate
    - activates the virtual environment  
7. pip install -r requirements.txt
    - installs the dependencies in requirements.txt
    - some dependencies will fail, if not necessary remove using `vim editor`
    - vim requirements.txt
        - remove the line that has error when installing
8. start *flask server* with `"flask run"` (Local Machine) or `"flask run --host=0.0.0.0"` (Remote Server eg. AWS) in (venv).../flaskapp
    - wait for app to deploy (take afew seconds)
    - access app on **local machine** with http://localhost:5000 or http://127.0.0.1:5000
    - access app on **server** with https://ipaddress:5000 eg. https://100.26.152.39:5000/
9. **alternatively**, start with `sudo python3 app.py` if using **AWS EC2 Instance**
    - to keep app long running
    - use `nohup sudo python3 app.py &`
    - app will run in background
        - to kill the app:
            - `"pgrep python3"` to get pid
            - `"sudo kill <<pid>>"`

**Dependencies required (if requirements.txt fails eg. version not found):**

1. install **nodejs, flask and pip**:
    - sudo apt-get update
    - curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
    - sudo apt-get install -y nodejs
    - sudo apt install -y python3-flask
    - sudo apt-get install -y python3-pip
    - use **python3 -m pip install**
2. make sure **pip** is latest
3. install using `pip install` 
    or `python -m pip install` 
    or **`python3 -m pip install (last worked on 3/2/2021)`**

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
    
    - install `cmake` and `scikit-build` before `opencv-python`
    - project done using:
        - python 2.7.17
        - python3 3.6.9
        - pip 20.3.1
        - flask 1.1.2
        - nodejs v8.10.0
        - npm 6.14.8
        - cmake 3.18.4.post1
        - scikit-build 0.11.1
        - python-pip 20.3.1
        - tensorflow 2.3.1 (**Must be 2.3.1**, newer versions not backward compatible)
        - keras 2.4.3
        - pillow 8.0.1
    
    - Last Tested 3 Feb 2021:
        - Using **AWS EC2 Instance Ubuntu 18.04**
        - using python 2.7.17
        - using python3 3.6.9
        - without venv
        - venv has some problems to install opencv-python (import cv2 not found, conflict with default python environments)
        - check opencv version
            - for python 2.X `python2 -c 'import cv2; print cv2.__version__'`
            - for python 3.X `python3 -c 'import cv2; print(cv2.__version__)'`
        - check tensorflow version `pip list | grep tensorflow`
        - **tensorflow 2.4.1 fails, fixed with `pip install tensorflow==2.3.1`**
        - make sure pip is upgraded to at least 20.3.1 to download tensorflow 2.3.1
        - import cv2 not found - uninstall and install again, you may be using wrong:
            - pip
            - pip3
            - python
            - python3
            - python -m pip
            - python3 -m pip
    
    - Notable Troubleshooting 3 Feb 2021:
        - OpenCV errors (module not installed: reinstall or install using correct default python2 or python3)
        - Tensorflow errors (no version found: upgrade pip to latest)
        - Website not accessible, ensure `https://` is used


