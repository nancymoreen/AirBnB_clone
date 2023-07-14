#!/usr/bin/python3
"""
This module defines the command interpreter class.
"""


import cmd
import models

class HBNBCommand(cmd.Cmd):
    """
    Custom Console Class
    """
    prompt = '(hbnb) '

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
