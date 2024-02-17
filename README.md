# MySQL CRUD Operations with Python

This repository demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations on a MySQL database using Python. It's a simple, yet powerful example of how to manipulate database records using Python scripts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- MySQL Server
- MySQL Connector Python (`mysql-connector-python` package)

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. **Clone the repository**

```sh
  git clone https://github.com/JuanCarlosGP/mysql_CRUD_python.git
    ```

2. **Set up your MySQL database**

- Make sure MySQL Server is installed and running.
- Create a database and a table that you will be using for the CRUD operations.

3. **Install the required Python packages**

```sh
pip install mysql-connector-python
    ```

4. **Configure your database connection**

- Open the `db_config.py` file and update the database configurations (host, user, password, database) to match your MySQL setup.

### Running the examples

To run the project, execute the Python scripts that correspond to the CRUD operations you wish to perform. Each script is named after the CRUD operation it demonstrates (`create.py`, `read.py`, `update.py`, `delete.py`).

## Built With

* [Python](https://www.python.org/) - The programming language used.
* [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/) - The library used to connect to MySQL.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/JuanCarlosGP/mysql_CRUD_python/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/JuanCarlosGP/mysql_CRUD_python/tags).

## Authors

* **Juan Carlos GP** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
