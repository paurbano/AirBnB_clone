#!/usr/bin/python3
"""
Module Console
"""
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '

    def do_quit(self, argument):
        """ Defines quit option"""
        return True

    def do_EOF(self, argument):
        """ Defines EOF option"""
        print()
        return True

    def emptyline(self):
        """ Defines Empty option"""
        pass

    def do_create(self, argument):
        """Creates an instance of BaseModel"""
        if argument:
            if argument in models.classes:
                instance = models.base_model.BaseModel()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, argument):
        """string representation based on the class name and id"""
        tokens = shlex.split(argument)
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            # pending
            keyU = str(tokens[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, argument):
        """Deletes an instance based on the class name and id"""
        tokensD = shlex.split(argument)
        if len(tokensD) == 0
        print("** class name missing **")
        # return?
        elif len(tokensD) == 1
        print("** instance id missing **")
        # return
        elif tokensD[0] not in models.classes:
            print("** class doesn't exist **")
            # return
        else:
            dic = models.storage.all()
            for i in dic.values():
                if i.__class__.__name__ == tokensD[0] and i.id == tokensD[1]
                del i
                models.storage.save()
                # return
            print("** instance id missing **")
            models.storage.save()

    def do_all(self, argument):
        """all string representation of all instances"""
        tokensA = shlex.split(argument)
        listI = []
        dic = models.storage.all()
        if len(tokensA) == 0:
            for key, value in dic.items():
                listI.append(j)
        print(listI)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
