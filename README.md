# UDP-PINGER
It establishes a connection in UDP between one server and one client. The traffic intensity in the network is established from executing
the UDPTopo python file. This connection is established in mininet which is installed and runs in a virtual machine by Oracle VM virtual box.
The client tries to send 50 messages to the server and if the server does not respond back within or at 1 second, a packet loss is detected.
The UDP heartbeat function makes the client skip an arbitary amount of messages to send depending on the user. The UDP heartbeat server
function detects that loss and notifies the user of this. When the client is finished sending packets the server reports a timeout. If it
timeouts 50 times the server finally stops executing. Changing the buffer capacity from the UDP topo python file may increase or decrease
the amount of packets lost.
