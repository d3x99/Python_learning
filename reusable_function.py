def emoji_converter(message):
    emojis = {
        ":)": "😊",
        ":(": "😣"
    }

    output = ""
    for emoji in message.split(" "):
        output += emojis.get(emoji, emoji) + " "
    return output


x = input('>')
print(emoji_converter(x))

