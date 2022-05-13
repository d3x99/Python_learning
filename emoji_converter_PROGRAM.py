message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😣"
}

output = ""
for emoji in words:
    output += emojis.get(emoji, emoji) + " "
print(output)


