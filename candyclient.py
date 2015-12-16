import socket

class MySocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def recv_timeout(the_socket,timeout=2):
		#make socket non blocking
		the_socket.setblocking(0)
		 
		#total data partwise in an array
		total_data=[];
		data='';
		 
		#beginning time
		begin=time.time()
		while 1:
			#if you got some data, then break after timeout
			if total_data and time.time()-begin > timeout:
				break
			 
			#if you got no data at all, wait a little longer, twice the timeout
			elif time.time()-begin > timeout*2:
				break
			 
			#recv something
			try:
				data = the_socket.recv(8192)
				if data:
					total_data.append(data)
					#change the beginning time for measurement
					begin=time.time()
				else:
					#sleep for sometime to indicate a gap
					time.sleep(0.1)
			except:
				pass
		 
		#join all parts to make final string
		return ''.join(total_data)
		
clientsocket = MySocket()
clientsocket.connect('10.230.22.60', 8000)
clientsocket.send('2:MM-MM-MM-MM-MM-MM:A1')
clientsocket.send('1:MM-MM-MM-MM-MM-MM:' + raw_input('Enter slot: '))
clientsocket.send('3:MM-MM-MM-MM-MM-MM:A1')
clientsocket.sock.close()