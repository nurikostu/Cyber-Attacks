from scapy.all import *

def sniffPckt(pkt):
	pkt.show()

def start_snifff():
	scapy_sniff = sniff(prn = sniffPckt,timeout=50,iface = 'eth0',stop_filter=lambda x:x.haslayer(ICMP))
	wrpcap('myfile.pcap',scapy_sniff)

def start_read():
	scapy_pcap=rdpcap("myfile.pcap")
	ip_list = []

	for pckt in scapy_pcap:
		if IP in pckt:
			if pckt[IP].src not in ip_list:
				ip_list.append(pckt[IP].src)
	
		else:
			pckt.show()
	print(ip_list)


print("""
	1: sniff
	2: read
	""")
choice=input(">> ")

if(choice=="1"):
	start_snifff()
elif(choice=="2"):
	start_read()
else:
	print("Hatalı giriş")