<!-- Adapted from: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/j-rayx/driving-backend">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Driving School Website Backend</h3>

  <p align="center">
    The <a href="http://drivng-school.netlify.com">website</a> features a course recommender that helps new customers to decide on courses that fit their needs, skill levels and budget.
    This repo contains the Python-Django code that powers the backend of the website.
    <br />
    <a href="https://github.com/j-rayx/driving-backend/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/j-rayx/driving-backend">View Demo</a>
    ·
    <a href="https://github.com/j-rayx/driving-backend/issues">Report Bug & Request Features</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With Python, Django and PostgreSQL</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Next.js]][Python-url]
* [![Django][React.js]][Django-url]
* [![PostgreSQL]][Postgres-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow these steps to get up and running with this project on your local machine.

### Prerequisites

1. [Install Python](https://www.python.org/downloads/). It comes packaged with `Pip`, a tool for managing Python libraries.
2. Install Django. You can see the [official Django installation guide](https://docs.djangoproject.com/en/4.1/topics/install/) for some background info. Django is at v4.1 at the point of revising this project docs.
*
  ```sh
  python -m pip install Django
  ```
  
2. Install and set up [Virtualenv](https://pypi.org/project/virtualenv/) for creating virtual environments.
*
  ```sh
  pip install virtualenv
  ```
3. [Download PostgreSQL](https://www.postgresql.org/download/) and install it.

4. [Download pgAdmin](https://www.pgadmin.org/download/)

5. Set up pgAdmin by following its tutorial on [desktop deployment](https://www.pgadmin.org/docs/pgadmin4/6.13/desktop_deployment.html).

6. Create a new database with the following terminal commands:
  ```
  psql postgres
  CREATE DATABASE database_name
  \connect database_name
  ```

7. Login to pgAdmin and see if the new database has been created on the dbserver.


### Installation

1. Create a virtual environment with the `virtualenv` command.

  ```sh
  virtualenv venv
  ```

2. Clone the repo
   ```sh
   git clone https://github.com/j-rayx/driving-backend.git
   ```

3. Activate your created Virtualenv virtual environment. Then, install the project dependencies in the `requirements.txt` file.

  ```
  source bin/activate
  pip install -r /path/to/requirements.txt
  ```

4. Supply your pgAdmin credentials in the `settings.py` file

  ```py
  # settings.py 
  
  DATABASES = {
    ‘default’: {
      ‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,
      ‘NAME’: env(‘DATABASE_NAME’),
      ‘USER’: env(‘DATABASE_USER’),
      ‘PASSWORD’: env(‘DATABASE_PASS’),
    }
  }

  ```

5. Run migrations for the database 
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

6. Spin off your local server and connect 

  ```sh
  python manage.py runserver
  ```


<!-- USAGE EXAMPLES -->
## Usage

Samples to show useful examples of how this project can be used. Additional screenshots, code examples and demos to be added soon. Also, links to more resources will be added.

[Setting up a cloned Django project](https://alicecampkin.medium.com/setting-up-a-forked-django-project-53d5939b7e9e)

_For more examples, please refer to the [Documentation](https://google.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- References -->

This README format was adapted from: https://github.com/othneildrew/Best-README-Template/
