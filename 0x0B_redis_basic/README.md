## Overview

This project demonstrates how to use Redis for basic operations and as a simple cache with Python. Redis is an in-memory data structure store used as a database, cache, and message broker. The goal of this project is to learn how to interact with Redis using the Python programming language.

## Learning Objectives

- Learn how to use Redis for basic operations.
- Learn how to use Redis as a simple cache.

## Requirements

- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3** (version 3.9).
- Your files should end with a new line.
- The first line of all your Python files should be exactly `#!/usr/bin/env python3`.
- Your code should follow the **PEP 8** style guidelines (version 2.5).
- You must document your modules, classes, and functions with detailed docstrings.
  - Modules: `python3 -c 'print(__import__("my_module").__doc__)'`
  - Classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
  - Functions: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- All functions and coroutines should have **type annotations**.

## Installation Instructions

### Install Redis on Ubuntu 20.04

To install Redis on your Ubuntu 20.04 system, use the following commands:

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
