#!/usr/bin/python3
"""
This module defines the command interpreter class.
"""

import cmd
from models import storage
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Custom Console Class"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string repre. of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Del. an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all str repre. of all instances
        based or not on the class name
        """
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return

        obj_list = []
        for key in storage.all():
            if not arg or arg == key.split('.')[0]:
                obj_list.append(str(storage.all()[key]))
                print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program.
        """
        print("")
        return True

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
