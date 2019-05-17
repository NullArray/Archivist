#!/usr/bin/env python

'''
#--ANSI Colored Formatting--#
#--Mini Library by Vector --#
#--Licensed under GNU GPL3--#
'''

_ERROR_  = "The 'text' method takes two arguments.\n"
_ERROR_ += "the first one of which is mandatory.  \n"
_ERROR_ += "Valid values are passed as string and \n"
_ERROR_ += "Include; 'green', 'red_bg' and '~' etc\n"

# Custom coloring and formatting
def text(color, text=''):
    # Colored text
    green   = "\x1b[32;01m" + text + "\x1b[39;49;00m"
    cyan    = "\x1b[33;36m" + text + "\x1b[39;49;00m"
    red     = "\x1b[31;01m" + text + "\x1b[39;49;00m"
    magenta = "\x1b[0;35m"  + text + "\x1b[39;49;00m"
    blue    = "\x1b[34m"    + text + "\x1b[39;49;00m"
    #-----------Add more colors below---------------#

    # COLOR = "[  ANSI   ]  + text + "\x1b[39;49;00m"

    # Colored Background
    green_bg   = "\e[42m" + text + "\x1b[39;49;00m"
    cyan_bg    = "\e[46m" + text + "\x1b[39;49;00m"
    red_bg     = "\e[41m" + text + "\x1b[39;49;00m"
    magenta_bg = "\e[45m" + text + "\x1b[39;49;00m"
    #-----------Add more colors below---------------#

    # COLOR = "[  ANSI   ]  + text + "\x1b[39;49;00m"

    # Colored symbols
    note   = "\x1b[32;01m[+]\x1b[39;49;00m"
    info   = "\x1b[33;36m[i]\x1b[39;49;00m"
    warn   = "\x1b[31;01m[!]\x1b[39;49;00m"
    misc   = "\x1b[0;35m[~]\x1b[39;49;00m"
    # Add more colored symbols below
    # MSG = "ANSI[*]\x1b[39;49;00m"


    if color == 'green':
        return green
    elif color == 'cyan':
        return cyan
    elif color == 'red':
        return red
    elif color == 'magenta':
	return magenta
    elif color == 'blue':
	return blue

    elif color == 'green_bg':
        return green_bg
    elif color == 'cyan_bg':
        return cyan_bg
    elif color == 'red_bg':
        return red_bg
    elif color == 'magenta_bg':
        return magenta_bg

    elif color == '+':
        return note
    elif color == 'i':
        return info
    elif color == '!':
        return warn
    elif color == '~':
        return misc
    else:
        raise BaseException(_ERROR_)
