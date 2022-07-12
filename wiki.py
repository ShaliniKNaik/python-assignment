import pyperclip
text = pyperclip.paste()
print("Shalini K Naik\n1MJ20CS413")
print("original text:")
print(text)

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
print("\nText after adding bullets:")
print(pyperclip.paste())
