import webbrowser, sys, pyperclip

sys.argv

# check if parameters were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# opens a new default browser
webbrowser.open('https://www.google.ca/maps/place/' + address)
