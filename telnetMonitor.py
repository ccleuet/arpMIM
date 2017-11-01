from scapy.all import *

#SYNchronize 

syn=IP(dst='127.0.0.1')/TCP(dport=80)

#SYNchronize-Acknowledgment
syn_acknowledgment = sr1(syn)
	
#Acknowledge
request = IP(dst='127.0.0.1') / TCP(dport=80, sport=syn_acknowledgment[TCP].dport,seq=syn_acknowledgment[TCP].ack, ack=syn_acknowledgment[TCP].seq + 1, flags='A') / 'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n'

reply = sr1(request)

#TCP socket connection is ESTABLISHED.
			
