# AirBnB clone - The console

The goal of the project is to deploy on server a simple copy of the AirBnB website. Starting from the console

## Command Interpreter

With the class "Cmd" from the package "cmd" we can use a simple framework for writing line-oriented command interpreters.


## Usage

For start it you can use in interactive mode

```
$ ./console.py
```
or for non-interactive mode

```
$ echo "help" | ./console.py
```
### Examples
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
#### and
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
