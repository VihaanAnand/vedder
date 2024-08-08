"""
This is the vedder module, an all-purpose module importing a bunch of useful libraries and creating a bunch of useful functions.
"""

# Import libraries
from abc import *
from argparse import *
from array import *
from ast import *
from asyncio import *
from atexit import *
from base64 import *
from bdb import *
from binascii import *
from bisect import *
from builtins import *
from bz2 import *
from cProfile import *
from calendar import *
from cmath import *
from cmd import *
from code import *
from codecs import *
from codeop import *
from collections import *
from colorsys import *
from compileall import *
from concurrent import *
from configparser import *
from contextlib import *
from contextvars import *
from copy import *
from copyreg import *
from ctypes import *
from curses import *
from dataclasses import *
from datetime import *
from dbm import *
from decimal import *
from difflib import *
from dis import *
from doctest import *
from email import *
from encodings import *
from ensurepip import *
from enum import *
from errno import *
from faulthandler import *
from fcntl import *
from filecmp import *
from fileinput import *
from fnmatch import *
from fractions import *
from ftplib import *
from functools import *
from gc import *
from genericpath import *
from getopt import *
from getpass import *
from gettext import *
from glob import *
from graphlib import *
from grp import *
from gzip import *
from hashlib import *
from heapq import *
from hmac import *
from html import *
from http import *
from idlelib import *
from imaplib import *
from importlib import *
from inspect import *
from io import *
from ipaddress import *
from itertools import *
from json import *
from keyword import *
from linecache import *
from locale import *
from logging import *
from lzma import *
from mailbox import *
from marshal import *
from math import *
from mimetypes import *
from mmap import *
from modulefinder import *
from multiprocessing import *
from netrc import *
from ntpath import *
from nturl2path import *
from numbers import *
from opcode import *
from operator import *
from optparse import *
from os import *
from pathlib import *
from pdb import *
from pickle import *
from pickletools import *
from pkgutil import *
from platform import *
from plistlib import *
from poplib import *
from posix import *
from posixpath import *
from pprint import *
from profile import *
from pstats import *
from pty import *
from pwd import *
from py_compile import *
from pyclbr import *
from pydoc import *
from pydoc_data import *
from pyexpat import *
from queue import *
from quopri import *
from random import *
from re import *
from readline import *
from reprlib import *
from resource import *
from rlcompleter import *
from runpy import *
from sched import *
from secrets import *
from select import *
from selectors import *
from shelve import *
from shlex import *
from shutil import *
from signal import *
from site import *
from smtplib import *
from socket import *
from socketserver import *
from sqlite3 import *
from ssl import *
from stat import *
from statistics import *
from string import *
from stringprep import *
from struct import *
from subprocess import *
from symtable import *
from sys import *
from sysconfig import *
from syslog import *
from tabnanny import *
from tarfile import *
from tempfile import *
from termios import *
from textwrap import *
from threading import *
from time import *
from timeit import *
from tkinter import *
from token import *
from tokenize import *
from tomllib import *
from trace import *
from traceback import *
from tracemalloc import *
from tty import *
from turtle import *
from turtledemo import *
from types import *
from typing import *
from unicodedata import *
from unittest import *
from urllib.error import *
from urllib.request import *
from uuid import *
from venv import *
from warnings import *
from wave import *
from weakref import *
from webbrowser import *
from wsgiref import *
from xml import *
from xmlrpc import *
from zipapp import *
from zipfile import *
from zipimport import *
from zlib import *
from zoneinfo import *
from vh import *

# Function to generate all primes up to a maximum
def generate_primes(max):
        """
        Generates a list of all prime numbers up to max using the Sieve of Eratosthenes and returns them.

        Parameters
        max (int): The highest value to include in the list.

        Returns
        list: The list of prime numbers.

        Example
        generate_primes(100)
        Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        """
        if max <= 1:
                return []
        output = [2]
        for i in range(3, max + 1, 2):
                is_prime = True
                for j in output:
                        if i % j == 0:
                                is_prime = False
                                break
                if is_prime:
                        output.append(i)
        return output


# Function to check if a number is prime
def is_prime(num):
        """
        Check if a number is prime using the Sieve of Eratosthenes.

        Parameters
        num (int): The number to check for primality.

        Returns
        bool: The primality truth value.

        Example
        is_prime(5)
        Output: True
        """
        is_prime = True
        for j in range(2, num):
                if num % j == 0:
                        is_prime = False
                        break
        return is_prime

# Function to read from a file and return contents
def read_file(filepath):
        """
        Read from a file and return its contents.

        Parameters
        filepath (str): The path of the file to read from.

        Returns
        str: The data retrieved from the file.

        Example
        read_file("/path/to/file/goes/here/file.txt")
        Output: Contents of the file
        """
        try:
                with builtins.open(filepath, "r") as file:
                        data = file.read()
                        return data
        except Exception as error:
                return f"Error - {error}"

# Function to read from a URI and return contents
def read_uri(uri):
        """
        Read from a URI and return its contents.

        Parameters
        uri (str): The URI to read from.

        Returns
        str: The data retrieved from the URI.

        Example
        read_uri("https://www.apple.com/")
        Output: "<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xml:la..."
        """
        try:
                context = create_default_context()
                context.check_hostname = False
                context.verify_mode = CERT_NONE
                with urlopen(uri, context = context) as response:
                        data = response.read().decode("utf-8")
                        return data
        except Exception as error:
                return f"Error - {error}"

# Function to run a terminal command
def terminal_command(command):
        """
        Run a terminal/shell command and return its output.

        Parameters
        command (str): The command to run.

        Returns
        str: The output of the command.

        Example
        terminal_command("pwd")
        Output: "/Users/user/Desktop/my/path/here"
        """
        try:
                output = subprocess.check_output(command, shell = True).decode()
                return output
        except Exception as error:
                return f"Error - {error}"