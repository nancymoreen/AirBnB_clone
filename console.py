#!/usr/bin/python3
"""
Write a program called console.py that
contains the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Custom Console Class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        handles the quit command and returns
        True to exit the program.
        """
        print()
        return True

    if __name__ == '__main__':
        """
        block ensures that the program is only executed
        when the script is run directly and not when
        imported as a module.
        """
        HBNBCommand().cmdloop()
