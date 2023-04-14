# InfoCasa

###### _Created on: 13/03/2023_

### Project execution 

---

#### **Prerequisites**

- Have Python 3 installed. (**Click to download [Python](https://www.python.org/downloads/)** )
- Install the virtual environment for package control of a project using the following command:

  ```
      pip install virtualenv
  ```

> The package manager is already on Windows, however on Linux you need to download it.  
> By clicking on the following link you can download [PIP](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)

- Download repositories:
  credit-backend (backend)

#### **Step 1. Creation and activation of the virtual environment**.

---

**Create the virtual environment

Access the terminal / command console and use:

        virtualenv -p python3 venv

> At the end of the command you can write any name, in this case the name venv was used.

With this command a folder is created for the virtual environment that is not included in the project with the assigned name, **_venv_** in this case, and **this way the virtual environment is established**.

**Activate the virtual environment**.

Access the folder, with the assigned name (**_venv_**), from the terminal / command console and use:

```Bash
Source bin/activate  (Linux)
Scripts/activate  (Windows)
```

> To exit use the command deactivate inside the folder (**_venv_**).

**To install the libraries inside the virtual environment**

Execute the following command:

        pip install -r requirements.txt

This command installs all the libraries from the repository into the virtual environment to run the project.

---
#### **Creation and activation of the environment via docker** 

1.- install docker [DOCKER](https://www.docker.com/)

2.- execute the command:

        docker-compose build

3.- execute the command

        docker-compose up

4.- enter redis

        docker exec -it redis-latam redis-cli

5.- set a key or obtain a value

        SET hello word
        GET hello


# NOTE
to use this project is required to install docker in the machine
