#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand is a subclass of cmd.Cmd and implements the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line function that does nothing.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
