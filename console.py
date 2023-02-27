#!/usr/bin/python3
"""This is my terminal module"""
import cmd, json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """AirBnB clone terminal"""
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_EOF(self, arg):
        """Exit the terminal, equal as quit command."""
        print()
        quit()

    def do_quit(self, arg):
        """Exit the terminal, equal as EOF command."""
        quit()

    def do_create(self, arg):
        """Create a new BaseModel instance."""
        if arg != "BaseModel":
            if arg == "":
                print("** class name missing **")
            else:
                print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """
        Print the str representation of an instance.
        USE: show <ClassName> <id>

        """
        arg = arg.split()

        if len(arg) == 1:
            print("** instance id missing **")
            return

        elif len(arg) < 2:
            print("** class name missing **")
            return

        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        obj = storage.all().get(f"{arg[0]}.{arg[1]}")

        if obj != None:
            print(obj)
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """
        Deletes a storaged object.
        USE: destroy <ClassName> <id>>
        """
        arg = arg.split()

        if len(arg) == 1:
            print("** instance id missing **")
            return

        elif len(arg) < 2:
            print("** class name missing **")
            return

        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        try:
            storage.all().pop(f"{arg[0]}.{arg[1]}")
            storage.save()

        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """
        Print all instances of type <ClassName>.
        USE: all <ClassName>
        """
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        else:
            search = storage.all()
            list_all = []
            for key, values in search.items():
                x = key.split('.')
                if x[0] == arg:
                    list_all.append(str(values))
            print(list_all)

    def do_update(self, arg):
        """
        Update an instance with new attributes.
        USE: update <ClassName> <id> <attribute name> <attribute value>
        """
        arg_list = arg.split()

        if len(arg_list) < 1:
            print("** class name missing **")
            return

        elif len(arg_list) < 2:
            print("** instance id missing **")
            return

        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(arg_list) < 3:
            print("** attribute name missing **")
            return

        elif len(arg_list) < 4:
            print("** value missing **")
            return

        try:
            a_object = storage.all().get(f"{arg_list[0]}.{arg_list[1]}")
            setattr(a_object, arg_list[2], arg_list[3])
            storage.save()

        except AttributeError:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
