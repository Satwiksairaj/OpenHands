# string_utils.py

def reverse_string(text: str) -> str:
    """Return the reversed string of the given text."""
    if text == '':
        return ''
    return text[::-1]
# HOW TO RUN:
# pip install -r requirements.txt
# python add_utility_function_stringutilsreversestring.py
# Then open: http://127.0.0.1:5000

    """Reverses the given string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string. If the input is empty, returns an empty string.
    """
    return text[::-1]

# HOW TO RUN:
# pip install -r requirements.txt
# python add_utility_function_stringutilsreversestring.py
# Then open: http://127.0.0.1:5000