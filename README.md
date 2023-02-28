# AirBnB clone - The console

The goal of the project is fully clone the AirBnB application

# Learning Objectivex

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function


## Command Interpreter

This is our first console for a web aplication mangament. 'console.py' iteracts directly with 'class FileStorage'
a class what manage 'BaseModel' and his subcalsses for serialization and deserialization.

https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230228%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230228T152226Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=862ba3ba5a08fe85a23a834069192be0299c9156fc900a51bfaa48c395029da2

### Usage

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all create destroy help  quit show update
(hbnb)
```

### Commands

- create: Create a new BaseModel instance. Ussage: Create <ClassName>

- destroy: Deletes a storaged object. Ussage: destroy <ClassName> <id>

- all: Print all instance of type <ClassName> Ussage: all <ClassName>

- show: Print the str representation of an instance. Ussage: show <ClassName> <id>

- update: Update an instance with new attributes. Ussage: update <ClassName> <id> <attribute name> <attribute value>
