# Student Support Center v2

## CAE Project Refactor

This repository is a **production version** of the previously developed [Cae_](https://github.com/vicct0r/Cae_) project. This version presents an optimized setup to meet the project's needs.

## Objective

The initial project used technologies such as `dj-static`, `gunicorn`, and `Heroku` to serve static and media files. However, files published this way were lost after a certain period, whenever a dyno on Heroku was restarted, resulting in the loss of all media files uploaded to the application in production.

This version of the project seeks a robust alternative for file storage using `django-heroku`, `boto3`, `django-storages`, `AWS S3`, and `Heroku`. The goal is to ensure that files are stored in an **S3 bucket** and properly displayed in the application hosted on **Heroku**.

## Technologies Used

- **Django**: Web framework used for system development.
- **AWS S3**: Storage for static and media files.
- **Heroku**: Hosting platform.
- **django-heroku**: Integration of Django with Heroku.
- **boto3**: AWS SDK for Python.
- **django-storages**: Extension to manage file storage.

## Configuration Structure

To better manage environment settings, the project was refactored to include a `settings/` directory with the following structure:


```
settings/
├── __init__.py
├── base.py
├── local.py
└── production.py
```


This organization allows efficient control of settings for both **localhost** and **production** environments.

## Contributions

### Collaboration Guidelines

For those interested in contributing to this project, it is important to note that several areas need attention. Currently, I do not have an up-to-date diagram that reflects the project architecture. However, there are several areas where improvements are welcome:

- **Bug Fixes**: Identifying and fixing backend logic issues.
- **Responsiveness**: Improving the visual presentation and user experience across different devices.
- **Performance**: Investigating and implementing ways to optimize system response times and reduce latency.

### Pull Request Instructions

If you decide to contribute to the project, please ensure that your contributions remain well-organized. It is essential to highlight:

- The main changes you made.
- If tests were included, please provide them.
- Details about the bugs you fixed and the logic behind the changes.

This approach will facilitate understanding your contributions and allow for a more efficient review process.

## Important Notice

The code is currently written in Portuguese, but I will be partially transitioning it to English to enable new contributors to participate in the project in the future.

## Notes

If this repository is active, it means that the project has been completed and is utilizing the mentioned technologies effectively. To see the application in action, you can visit the following link:

[CAE Production Application](https://sistema-cae-v5-ecab78bbbd3c.herokuapp.com/)

## Tags

**Tags**: #Django #S3 #Heroku #django-storages #boto3 #storage #academic management #web application #completed project

