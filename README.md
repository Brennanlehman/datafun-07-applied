# datafun-07-applied
Project 7 ML
## Brennan Lehman
## 2/16/2024
### Machine learning project deliverables:
- Build a model
- Make predictions
- Visualize the model
- Publish your insights 

# Environment Setup 

### Start a new project repository in GitHub and then clone down to local machine. I leveraged VS Code clone functionality

### Create Virtual Environment

```shell

py -m venv .venv
.venv\Scripts\Activate
```

### Create .gitignore file
```shell
ni .gitignore
```
add .venv to .gitignore file to not be tracked in github

### Add requirements folder

```shell

ni requirements.txt
py -m pip install -r requirements.txt
```

# Install and Setup the Project

### Add dependencies

```shell

py -m pip install jupyterlab
py -m pip install numpy
py -m pip install pandas
py -m pip install pyarrow
py -m pip install matplotlib 
py -m pip install seaborn
py -m pip install scipy
```

### Freeze dependencies

```shell

py -m pip freeze > requirements.txt
```

### Git add and commit 

```shell
git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main
```

# Start Project
