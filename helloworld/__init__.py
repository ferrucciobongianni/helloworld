VALUES = {
    "italian": "Ciao Mondo",
    "english": "Hello World",
    "french": "Bonjour le monde"
}

def hello_world(lang=None):
    lang = lang or "english"
    assert lang in VALUES, "I wasn't expecting to be asked %s" % lang
    return VALUES.get(lang)
