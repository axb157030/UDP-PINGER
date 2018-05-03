# UDP_PingC.py

from socket import *
import sys
import time
argv = sys.argv
clientIPaddress = argv[1] 
#serverName = '10.0.0.6'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
minRTT = 0.0;
maxRTT = 0.0;
#tempRTT;
RTTAcum = 0.0;
import sys
import time
argv = sys.argv
clientIPaddress = argv[1] 
#serverName = '10.0.0.6'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
minRTT = 0.0;
maxRTT = 0.0;
#tempRTT;
RTTAcum = 0.0;
avgRTT = 0.0;
pktLost = 0.0; # number of packets lost
pktRec = 0.0 # number of packets recieved
pktLoss = 0.0; # packet loss percentage. Initially value given to make sure it stores floating numbers
seqNumTime = time.localtime()
#counter = 0;
seqNum = 1; # Sequence number intial value
clientSocket.settimeout(1)
while (seqNum <= 50): 
	message = 'reply from: ' + str(seqNum) + ' '+ str(time.asctime(seqNumTime))
	seqNumTime = time.localtime() # This will be a little off as it gets the time just before the message is sent
	RTT = time.clock() # Hold RTT of a message, which equals the amount of time since the message
	# was sent to when client recieved modified message from server. 
	# It is a little off as it is calculate a little after message is sent
	# clientSocket.sendto(message,(clientIPaddress,serverPort)) # Send ping message
	clientSocket.sendto(message,(clientIPaddress,serverPort)) # Send ping message
	
	try: 
		modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
		print(modifiedMessage, "RTT: ", RTT) # print modified message 
		if(seqNum == 1) : 
			minRTT = RTT;
		if(minRTT > RTT) :
			minRTT = RTT;
		if(maxRTT < RTT) : # The max RTT will not be greater or equal to 1 second
			maxRTT = RTT;
		RTTAcum += RTT;
		pktRec +=1
	
	except timeout:
		print 'Request time out', seqNum 
		pktLost += 1; # does a ping mean one connection that results in a timout as well?
		#clientSocket.settimeout(1)

	seqNum += 1; # Sequence number increment every successful ping
avgRTT = RTTAcum / seqNum;
pktLoss = (pktLost / seqNum) * 100
print pktRec,' Packets recieved ', pktLost, ' Packets Lost ', 'Packet Loss Rate: ', pktLoss,'%' #
print "Minimum RTT: ", minRTT, " Maximum RTT: ", maxRTT, " Average RTT: ", avgRTT

clientSocket.close()




