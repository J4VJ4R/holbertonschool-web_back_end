# 0x01. Python and Async

## Learning Objectives
  - async and await syntax
  - How to execute an async program with asyncio
  - How to run concurrent coroutines
  - How to create asyncio tasks
  - How to use the random module

## Requirements
  - A README.md file, at the root of the folder of the project, is mandatory
  - Allowed editors: vi, vim, emacs
  - All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
  - All your files should end with a new line
  - All your files must be executable
  - The length of your files will be tested using wc
  - The first line of all your files should be exactly #!/usr/bin/env python3
  - Your code should use the pycodestyle style (version 2.5.x)
  - All your functions and coroutines must be type-annotated.
  - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  - All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'

## Tasks
### [0. The basics of async](./0-basic_async_syntax.py)
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.
```
vagrant@ubuntu-bionic:/vagrant/holberton_development/curriculum-specialization-backend/0x01-Python_async_function$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

vagrant@ubuntu-bionic:/vagrant/holberton_development/curriculum-specialization-backend/0x01-Python_async_function$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```