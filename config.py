OPENAI_API_KEY="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"

class config:
    def __init__(self, text):
        self.key = text

    def get_API_KEY(self):
        return self.key

    def set_API_KEY(self,text):
        self.key = (str(text))
        return self.key
    
