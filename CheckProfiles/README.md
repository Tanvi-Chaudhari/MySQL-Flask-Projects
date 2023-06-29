# Project Setup Guide

This guide will help you set up and run the project successfully. Please follow the steps below:

## Prerequisites
- [Python](https://www.python.org/downloads/) (version 3.6 or above) should be installed on your system.
- [Virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) is recommended for isolating project dependencies.

## Installation Steps

1. Clone the project repository to your local machine.

2. Open the project directory in your preferred Python editor or IDE. For example, if you are using PyCharm, make sure it is already opened in the virtual environment (venv) or install and activate the virtual environment by following these commands in the terminal:
    ```shell
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required package 'flask-mysqldb' using the following command:
    ```shell
    pip install flask-mysqldb
    ```

4. Install [phpMyAdmin](https://www.phpmyadmin.net/) on your system. You can refer to this [video tutorial](https://www.youtube.com/watch?v=jJKL-0guwa0) for assistance.

5. Set up a local development environment using a Wamp server or any other similar software. Start all the services and open phpMyAdmin. Create a new database named 'flaskapp' to be used by the project.

6. In the 'flaskapp' database, create a table named 'accounts' with the following schema:
    ```sql
    CREATE TABLE IF NOT EXISTS `accounts1` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `username` varchar(50) NOT NULL,
      `password` varchar(255) NOT NULL,
      `email` varchar(100) NOT NULL,
      `organisation` varchar(100) NOT NULL,
      `address` varchar(100) NOT NULL,
      `city` varchar(100) NOT NULL,
      `state` varchar(100) NOT NULL,
      `country` varchar(100) NOT NULL,
      `postalcode` varchar(100) NOT NULL,
      PRIMARY KEY(`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8; 
    ```
   For a better understanding of steps 5 and 6, you can watch this [video tutorial](https://www.youtube.com/watch?v=Ufb8KMikNF8).

7. To run the project, open the terminal in your editor and execute the command:
    ```shell
    flask run
    ```
   If you are using PyCharm, you can also run the `main.py` file directly.

8. Open a web browser and navigate to `http://localhost:5000` to see the project in action. The application should look similar to the screenshots below:


