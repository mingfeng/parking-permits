### Parking Permits API

Backend repository for parking permits service developed by City of Helsinki.

Instructions in this README.md are written with an experienced Python developer in mind. For example, "docker-compose up" means you already know what docker and docker-compose are and you already have both installed locally. This helps to keep the README.md concise.

### Setting up local development environment with Docker

- Clone the repository

- Start the application

  ```bash
  docker-compose up
  ```

- Access development server on [localhost:8000](http://localhost:8000)

- Login to admin interface with `admin` and 🥥

- Done!

### Setting up local development environment with PyEnv and VirtualEnvWrapper

```
pyenv install -v 3.9.0
pyenv virtualenv 3.9.0 parking_permits
pyenv local parking_permits
pyenv virtualenvwrapper
```

Install packages

```
pip install -U pip pip-tools
pip-compile -U requirements.in
pip-compile -U requirements-dev.in
pip-sync requirements.txt requirements-dev.txt
```


### Managing project packages

- We use `pip-tools` to manage python packages we need
- After adding a new package to requirements(-dev).in file, compile it and re-build the Docker image so that the container would have access to the new package

  ```bash
  docker-compose up --build
  ```

### Running tests

- You can run all the tests with:
  ```bash
  docker-compose exec graphql-api pytest
  ```
- If you want to run the tests continously while developing:

  - Install [fd](https://github.com/sharkdp/fd) using `brew` or equivalent
  - Install [entr](https://github.com/eradman/entr) using `brew` or equivalent
  - Run pytest whenever a Python file changes with:

    ```bash
    fd --extension py | entr -c docker-compose exec graphql-api pytest
    ```
