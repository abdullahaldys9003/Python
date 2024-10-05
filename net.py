from scapy.all import ARP, Ether, srp

def scan_network(target_ip):
    # إنشاء حزمة ARP لطلب المعلومات من الشبكة
    arp_request = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp_request

    # إرسال الحزم وانتظار الرد
    result = srp(packet, timeout=3, verbose=0)[0]

    # استخراج وتخزين معلومات الأجهزة
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

# استبدل '192.168.1.1/24' بالمدى الخاص بشبكتك
network_devices = scan_network('192.168.1.1/24')

print("الأجهزة المتصلة بالشبكة:")
for device in network_devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")