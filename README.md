<h3 align="center">
        <samp>&gt; Continued integration
        </samp>
</h3>


<p align="center"> 
  <samp>
    <br>
    「 <b>B3 - EPSI Dev FS</b> 」
    <br>
  </samp>
</p>

<br/>

![ci](ci.png)


# - Use To Code -

![PyCharms](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=fff)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)

<br/>

# - Objectives - </center>

## Set up a continuous integration pipeline for a software project

<br/>

# - Project architecture -

```php
├── venv/
│   └── ...
├── app.py
├── Dockerfile
├── Jenkinsfile
├── README.md
├── requirements.txt
└── test_app.py
```

<br/>

# - Key concepts -

## - Why choose Docker ?

+ Isolation: Each application runs in its own environment, without interfering with other applications.
+ Portability: A container can run identically on different machines, guaranteeing consistent behavior.
+ Ease of deployment: Docker makes it easy to integrate and deploy applications, thanks to Docker images.


## Why Jenkins?

+ Automation: Jenkins automates the build, test and deployment stages, reducing the risk of human error.
+ Continuous Integration (CI): Jenkins enables rapid error detection by running tests on every code change.
+ Continuous Deployment (CD): Jenkins can automate the deployment of new versions of applications.


## - Why a CI/CD pipeline?

+ Efficiency: By automating the build, test and deployment processes, developers can deliver features faster.
+ Code quality: Automated testing detects errors quickly, improving code stability.
+ Rapid feedback: Developers receive immediate feedback on the integrity of their code with every change, enabling rapid correction of problems.

<br/>

# - Installation -

## 1. Prerequisites: Install Docker and Git

## 2. Clone Project from GitHub
```
git clone https://github.com/Feareis/b3-epsidevfs-integration_continue.git
cd b3-epsidevfs-integration_continue
```

## 3. Building the Docker Image
```
docker build -t currency_converter:1.0 .
```

## 4. run the docked application
```
docker run -p 5000:5000 currency_converter:1.0
```

## 5. Configure Jenkins (if necessary)

Install Jenkins: Install Jenkins (with Docker, for example).
<br/><br/>
Configuring the pipeline : 
+ Create a new Jenkins job and link it to the GitHub repository b3-epsidevfs-integration_continue.
+ If a Jenkinsfile is already present in the repository, Jenkins will automatically execute the pipeline (build, test, deploy).
