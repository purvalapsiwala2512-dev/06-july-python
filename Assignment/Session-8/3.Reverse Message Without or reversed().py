def reverse_message(message):
    reversed_str = ""
    for char in message:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_message("WhatsApp Text"))