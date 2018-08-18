from core.plugin.plugin import DecoderPlugin

class Plugin(DecoderPlugin):

    def __init__(self, context):
        # Name, Author, Dependencies
        super().__init__('BASE16', "Thomas Engel", ["base64"])

    def run(self, text):
        import base64
        return base64.b16decode(text.encode('utf-8', errors='surrogateescape')).decode('utf-8', errors='surrogateescape')
