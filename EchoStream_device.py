
class EchoStream_device:

    def function(self, message):
        self.writing = message
        return self.writing
