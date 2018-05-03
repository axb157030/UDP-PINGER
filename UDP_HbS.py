from socket import *
import sys
import random
argv = sys.argv
serverIPaddress = argv[1]
messageSplit = "";
words = []
checkSeq = []
lasSeq = 0
preSeq = 0
seqNum = 0
counter = 0
losMes = 1 # number of lost messeges
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
time = 1 # When equal 50 or maxTimeOuts server stops
maxTimeOuts = 50 
serverSocket.settimeout(1)
# Assign IP address and port number to socket, use port 12000

#print counter
serverSocket.bind((serverIPaddress, 12000))
with open(argv[2], "w") as f:
	while (time <= maxTimeOuts):	
		try:
			#Receive the client packet along with the address it is coming from
			message, address = serverSocket.recvfrom(1024) 
			#f.write("packet recieved from before Recv. client\ncounter: %d\n" % counter)
			#f.flush()
			if(isinstance(message, basestring)):
				messageSplit = message
				#print "message is a string"
				words = messageSplit.split()
				seqNum = int(words[2])
				#checkSeq.append(seqNum)
				preSeq = seqNum
				#print checkSeq[counter]
				#lostMes = int(checkSeq[counter]) - int(checkSeq[counter - 1])
				losMes = (preSeq -1) - lasSeq
				#f.flush()
				
			else:
				print "message is not a string"
			print 'Server received msg ', seqNum
			lasSeq = seqNum
			f.write("Server received msg\nseqNum: %d\n" % seqNum)
			f.flush()
			if(losMes > 1):
				#print "Lost ", lostMes, " messages"
				f.write("Lost losMes: %d\n" % losMes)
				f.write("messages")
				f.flush()

			
			# Capitalize the message from the client
			message = message.upper()

			# Server responds
			serverSocket.sendto(message, address)
		except timeout:
			print "Server timeout"
			f.write("Server timeout msg\n")
			f.flush()
			time += 1
		
	