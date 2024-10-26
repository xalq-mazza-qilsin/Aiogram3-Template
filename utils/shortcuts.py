MARKDOWN_ESCAPE_CHARS = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']


def safe_markdown(_string):
    _string = str(_string)
    text = ""
    for letter in _string:
        if letter in MARKDOWN_ESCAPE_CHARS:
            text += '\{}'.format(letter)
        else:
            text += letter
    return text
