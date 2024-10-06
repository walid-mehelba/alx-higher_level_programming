#!/usr/bin/python3

def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':' character.
    
    Args:
        text (str): The text to be printed with specific formatting.
        
    Raises:
        TypeError: If text is not a string.
    
    Example:
        >>> text_indentation("Hello. How are you? I am fine: thank you.")
        Hello.

        How are you?

        I am fine: thank you.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    formatted_text = ""
    i = 0
    while i < len(text):
        formatted_text += text[i]
        if text[i] in {'.', '?', ':'}:
            formatted_text += "\n\n"
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1

    print(formatted_text.strip())
