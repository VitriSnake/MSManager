#!/usr/bin/python3
# -*- condig: utf-8 -*-

# MSManager is under GPLv3 license, if you use the program or part of the program in one of your projects via a "fork" of GitHub, you must keep this license on your project.

# Imports
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter
from colorama import init
from termcolor import colored
import requests # For if name == main
 
init()

def prompt_auto(ask, completion=[]):
    style = Style.from_dict({
    '':          'white',
    'ask': 'yellow',
    })
    message = [
        ('class:', '['),
        ('class:ask', '?'),
        ('class:', '] '),
        ('class:', ask),
    ]
    completion = WordCompleter(completion)
    text = prompt(message, style=style, completer=completion)

def info(message):
    print('[', end='')
    print(colored('i', 'yellow', attrs=['bold']), end='')
    print('] '+message)

def warning(message):
    print('[', end='')
    print(colored('!', 'yellow', attrs=['bold']), end='')
    print('] '+message)

def error(message):
    print('[', end='')
    print(colored('!', 'red', attrs=['bold']), end='')
    print('] '+message)

def fail(message):
    print('[', end='')
    print(colored('x', 'red', attrs=['bold']), end='')
    print('] '+message)

def note(message):
    print(colored(message, 'green'))

def sucess(message):
    print('[', end='')
    print(colored('i', 'green', attrs=['bold']), end='')
    print('] '+message)

if __name__ == "__main__":
    warning('This is a warning')
    info('This is an info')
    error('This is an error')
    fail('This is a fail')
    note('This is a note')
    sucess('This is a sucess')
    prompt_auto('Enter a word: ', requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').text.lower().split('\n'))