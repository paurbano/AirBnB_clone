#!/usr/bin/python3
""" test for console"""
import unittest
import models
import sys
from console import HBNBCommand
import os
from io import StringIO
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    """ test console"""
    def setUp(self):
        """setup"""
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        """teardown"""
        sys.stdout = self.backup

    def create(self):
        """instance"""
        return HBNBCommand()

    def test_quit(self):
        """quit exist"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """EOF"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        """all"""
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_show(self):
        """test show"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        s = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(s))

    def test_show_class_name(self):
        "test messages"
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show")
        s = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", s)

    def test_show_class_name2(self):
        """test messages"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out = StringIO()
        self.capt_out.close()


if __name__ == '__main__':
    unittest.main()
