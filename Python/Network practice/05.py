import telnetlib as tel


def to_bytes(line):
    return f"{line}".encode("utf-8")


ip_dict = {1: {'gi0/1': ['10.0.0.9', 1], 'gi0/0': ['10.0.0.1', 1]},
           5: {'gi0/0': ['10.0.0.2', 1], 'gi0/1': ['10.0.0.6', 1]},
           2: {'gi0/0': ['10.0.0.5', 1], 'gi0/1': ['10.0.0.13', 1]},
           3: {'gi0/0': ['10.0.0.10', 1], 'gi0/1': ['10.0.0.17', 0], 'gi0/2': ['188.24.0.1', -1]},
           4: {'gi0/0': ['10.0.0.14', 1], 'gi0/1': ['10.0.0.18', 0], 'gi0/2': ['13.201.255.5', -1]},
           6: {'gi0/0': ['188.24.0.2', -1], 'gi0/1': ['172.16.0.1', 0], 'gi0/2': ['172.16.0.5', 0]},
           7: {'gi0/0': ['13.201.255.6', -1], 'gi0/1': ['172.16.0.2', 0], 'gi0/2': ['172.16.0.9', 0]},
           8: {'gi0/0': ['172.16.0.6', 0], 'gi0/1': ['172.16.0.10', 0]}}


for i in range(1, 9):
    with open(f'R{i}.cfg', 'w') as f:
        f.write('\n')
        f.write('en\n')
        f.write('conf t\n')
        f.write('no ip domain-lookup\n')
        f.write("no banner exec\n")
        f.write("no banner incoming\n")
        f.write("no banner login\n")
        f.write('line con 0\n')
        f.write(' logg sync\n')
        f.write(' exit\n')
        f.write('router osp 1\n')
        f.write(f' router-id 10.{i}.{i}.{i}\n')
        f.write('int lo0\n')
        f.write(f' ip addr 10.{i}.{i}.{i} 255.255.255.255\n')
        f.write(f' ip ospf 1 area {1 if i == 1 or i == 2 or i == 5 else 0}\n')
        f.write(' exit\n')
        for iface, param in ip_dict[i].items():
            f.write(f"int {iface}\n")
            f.write(f" ip addr {param[0]} 255.255.255.252\n")
            f.write(" no shut\n")
            if param[1] != -1:
                f.write(f" ip ospf 1 area {param[1]}\n")
                f.write(f" ip ospf network point-to-point\n")
            f.write(" exit\n")
        f.write('end\n')
        f.write('wr\n')

eve_ip = "192.168.200.100"
port = 32768
for i in range(1, 9):
    with tel.Telnet(eve_ip, port+i) as telnet:
        with open(f"R{i}.cfg", 'r') as f:
            for line in f:
                telnet.write(to_bytes(line))
