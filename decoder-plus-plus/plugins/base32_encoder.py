from core.plugin.plugin import EncoderPlugin

class Plugin(EncoderPlugin):

    def __init__(self, context):
        # Name, Author, Dependencies
        super().__init__('BASE32', "Thomas Engel", ["base64"])

    def run(self, text):
        import base64
        return base64.b32encode(text.encode('utf-8', errors='surrogateescape')).decode('utf-8', errors='surrogateescape')
