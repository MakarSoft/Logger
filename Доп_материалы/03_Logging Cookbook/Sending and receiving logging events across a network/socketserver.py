# На принимающей стороне вы можете настроить приемник с помощью модуля socketserver. Вот основной рабочий пример:
#  Сначала запустите сервер, а затем клиент. На стороне клиента на консоль ничего не выводится; на стороне сервера вы должны увидеть что-то вроде:
# About to start TCP server...
# 59 root INFO Jackdaws love my big sphinx of quartz.
# 59 myapp.area1 DEBUG Quick zephyrs blow, vexing daft Jim.
# 69 myapp.area1 INFO How quickly daft jumping zebras vex.
# 69 myapp.area2 WARNING Jail zesty vixen who grabbed pay from quack.
# 69 myapp.area2 ERROR The five boxing wizards jump quickly.

# Обратите внимание, что в некоторых сценариях есть некоторые проблемы с безопасностью при использовании pickle.
# Если это влияет на вас, вы можете использовать альтернативную схему сериализации, переопределив метод makePickle()
# и реализовав там свою альтернативу, а также адаптировав приведенный выше сценарий для использования вашей альтернативной сериализации.
import pickle
import logging
import logging.handlers
import socketserver
import struct

class LogRecordStreamHandler(socketserver.StreamRequestHandler):
    """Handler for a streaming logging request.
    This basically logs the record using whatever logging policy is
    configured locally.
    """
    def handle(self):
        """
        Handle multiple requests - each expected to be a 4-byte length,
        followed by the LogRecord in pickle format. Logs the record
        according to whatever policy is configured locally.
        """
        while True:
            chunk = self.connection.recv(4)
            if len(chunk) < 4:
                break
            slen = struct.unpack('>L', chunk)[0]
            chunk = self.connection.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.connection.recv(slen - len(chunk))
            obj = self.unPickle(chunk)
            record = logging.makeLogRecord(obj)
            self.handleLogRecord(record)

    def unPickle(self, data):
        return pickle.loads(data)

    def handleLogRecord(self, record):
        # if a name is specified, we use the named logger rather than the one
        # implied by the record.
        if self.server.logname is not None:
            name = self.server.logname
        else:
            name = record.name
        logger = logging.getLogger(name)

        # N.B. EVERY record gets logged. This is because Logger.handle
        # is normally called AFTER logger-level filtering. If you want
        # to do filtering, do it at the client end to save wasting
        # cycles and network bandwidth!
        logger.handle(record)

class LogRecordSocketReceiver(socketserver.ThreadingTCPServer):
    """
    Simple TCP socket-based logging receiver suitable for testing.
    """
    allow_reuse_address = True

    def __init__(self, host='localhost',
        port=logging.handlers.DEFAULT_TCP_LOGGING_PORT,
        handler=LogRecordStreamHandler):
        socketserver.ThreadingTCPServer.__init__(self, (host, port), handler)
        self.abort = 0
        self.timeout = 1
        self.logname = None

    def serve_until_stopped(self):
        import select
        abort = 0
        while not abort:
            rd, wr, ex = select.select([self.socket.fileno()], [], [], self.timeout)
        if rd:
            self.handle_request()
        abort = self.abort

def main():
    logging.basicConfig(format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
    tcpserver = LogRecordSocketReceiver()
    print('About to start TCP server...')
    tcpserver.serve_until_stopped()

if __name__ == '__main__':
    main()