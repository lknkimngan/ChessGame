import socket
import pickle
import time

class Network:
    def __init__(self):

       

        #AF_INET -> IPv4, SOCK_STREAM-> TCP socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.host = "localhost"
        self.host = '192.168.5.143'
        self.port = 5555
        self.addr = (self.host, self.port)
        self.board = self.connect()
        self.board = pickle.loads(self.board)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4096*8)
        except:
            pass

    def disconnect(self):
        self.client.close()

    def send(self, data, pick=False):
        """
        :param data: str
        :return: str
        """
        start_time = time.time()
        while time.time() - start_time < 5:
            try:
                if pick:
                    #dữ liệu mà được truyền đi thì nó sẽ được serialize
                    self.client.send(pickle.dumps(data))
                else:
                    self.client.send(str.encode(data))
                reply = self.client.recv(4096*8)
                try:
                    reply = pickle.loads(reply)
                    break
                except Exception as e:
                    print(e)

            except socket.error as e:
                print(e)

        return reply

        