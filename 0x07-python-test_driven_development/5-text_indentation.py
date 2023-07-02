#!/usr/bin/python3
"""text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after '.', '?', and ':'.

    Args:
        text (string): The text to be print.
    Raises:
        TypeError: If type of text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    a = 0
    while a < len(text) and text[a] == ' ':
        a += 1

    while a < len(text):
        print(text[a], end="")
        if text[a] == "\n" or text[a] in ".?:":
            if text[a] in ".?:":
                print("\n")
            a += 1
            while a < len(text) and text[a] == ' ':
                a += 1
            continue
        a += 1
