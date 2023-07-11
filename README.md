# machine_learning_project
This is first machine learning projet.


## Start Machine Learnin Project.

### Software and account Requirement

1. [GitHub Account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code Ide](httos://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/git)


creating conda Environment
''''''

conda create -p venv ==3..10 -y
''''''

conda activate venv/
''''''

pip install -r requirements.txt
'''''''


To Add files to git
''''''

git add .
''''''
OR
''''''
git add <file_name>
''''''

> Note : To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
''''''
git status
''''''

To check all vesion maintained by git
''''''
git log
''''''


To create version/commit all changes by git
''''''
git commit -m "message"
''''''

To send version/changes to github
''''''
git push origin main
''''''

To check remote url
''''''
git remote -v
''''''

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = cablearora@gmail.com
2. HEROKU_API_KEY = fo1_o_647pydTU9_tfwzj6YrvWdr3cg9zkvghNNa9wNIqb0
3. HEROKU_APP_NAME = project-ml
''''''

BUILD DOCKER IMAGE
'''''''

docker build -t <image_name>:<tagname> .
''''''

> Note: Image name for docker must be lowecase

To list docker images
'''''''
docker images
'''''''


Run docker image
'''''''
docker run -p 5000:5000 -e PORT=5000 6f222dc27e70
''''''

To check running container
'''''''
docker ps
''''''

To stop Docker container
''''''
docker stop <container_id>
''''''



''''''
python setup.py install
''''''

