# Developer Documentation
#### Documentation for development setup, management, and contribution</h6>

This documentation is provided to aid collaborators with preparing and troubleshooting their development environment for this project. The guidelines and workflow provided here may not always be considered the best practices, but for the confines of this project, should be followed to prevent stylistic conflicts between developers.

### Setup & Management
###### Setup the development environment and necessary tools

This project makes parallel use of `pip`, `venv`, and `pipenv` for dependency management

Clone this project repository with `git` and enter the project directory
```shell
git clone https://github.com/jkmalan/mc-assistant.git && cd mf-server-python
```

Verify that the proper version of Python is installed for your user. Install and upgrade the necessary tools
```shell
pip install --user --upgrade pip pipenv setuptools
```

Create the virtual environment using `python` and the builtin `venv`
```shell
python -m venv venv
```

Activate the virtual environment shell using `pipenv`
```shell
pipenv shell
```

Install all project dependencies using `pipenv`
```shell
pipenv install
```

### Contribution
###### Guidelines and best practices for project contributions
