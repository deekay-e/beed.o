#!/usr/bin/env python
''' console app for beedo '''
import cmd


class BeedoCommand(cmd.Cmd):
    ''' Beedo console '''
    prompt = '(beedo) '

    def do_EOF(self, arg):
        ''' exit console '''
        return True

    def emptyline(self):
        ''' overwrite the emptyline method '''
        return False

    def do_quit(self, arg):
        ''' quit command to exit the program '''
        return True


if __name__ == '__main__':
    BeedoCommand().cmdloop()
