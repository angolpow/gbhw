#### 1
*На всех маршрутизаторах настроить динамическую маршрутизацию с помощью протокола RIP2 и DHCP сервер для динамической настройки клиентов в LAN.*

[Файл задания 1](Task4_rip.pkt)

#### 2

*Задание на расчет сетей (не в Packet Tracer).
а) разбить сеть 10.8.2.0/24 на 3 подсети, на 7, на 21. Для каждого разбиения указать адрес сети, первого узла, последнего узла и широковещательный.
б) сколько хостов будет в сети 172.16.1.0/26, в сети 10.0.0.0/18 ?
в) какой будет броадкаст адрес в сети 10.0.0.0/30, в сети 10.255.255.124/30 ?*


а)
- На 3 сети

|		|	Network	    |	Prefix|	   First	|	Last      	|	Broadcast	  |
|	-:|--:	 	      |----:|---:		      |---:		      |---:      		|
|	1	|	10.8.2.0	  | 25	|	10.8.2.1	  | 10.8.2.126	|	10.8.2.127	|
|	2	|	10.8.2.128	|	26	|	10.8.2.129	|	10.8.2.190	|	10.8.2.191	|
|	3	|	10.8.2.192	|	26	|	10.8.2.193	|	10.8.2.254	|	10.8.2.255	|

- На 7 сетей:

|	№	|	Network	    |	Prefix	|	First	  |	Last	      |	Broadcast	  |
|--:|------:		  |	--:	| ---:		    |	---:	      |---:		      |
|	1	|	10.8.2.0	  |	26	|	10.8.2.1	  |	10.8.2.62	  |	10.8.2.63	  |
|	2	|	10.8.2.64	  |	27	|	10.8.2.65	  |	10.8.2.94	  |	10.8.2.95	  |
|	3	|	10.8.2.96	  |	27	|	10.8.2.97	  |	10.8.2.126	|	10.8.2.127	|
|	4	|	10.8.2.128	|	27	|	10.8.2.129	|	10.8.2.158	|	10.8.2.159	|
|	5	|	10.8.2.160	|	27	|	10.8.2.161	|	10.8.2.190	|	10.8.2.191	|
|	6	|	10.8.2.192	|	27	|	10.8.2.193	|	10.8.2.222	|	10.8.2.223	|
|	7	|	10.8.2.224	|	27	|	10.8.2.225	|	10.8.2.254	|	10.8.2.255	|

- На 21 сеть:

| № | Network	    | Prefix| First	    | Last	      | Broadcast   |
|--:|------------:|----:|------------:|------------:|------------:|
| 1 |	10.8.2.0	  | 28	| 10.8.2.1	  | 10.8.2.14	  | 10.8.2.15   |
| 2	| 10.8.2.16 	| 28	| 10.8.2.17	  | 10.8.2.30	  | 10.8.2.31   |
|	3	|	10.8.2.32	  |	28	|	10.8.2.33	  |	10.8.2.46	  |	10.8.2.47	  |
|	4	|	10.8.2.48 	|	28	|	10.8.2.49	  |	10.8.2.62	  |	10.8.2.63	  |
|	5	|	10.8.2.64 	|	28	|	10.8.2.65	  |	10.8.2.78 	|	10.8.2.79	  |
|	6	|	10.8.2.80 	|	28	|	10.8.2.81	  |	10.8.2.94	  |	10.8.2.95	  |
|	7	|	10.8.2.96 	|	28	|	10.8.2.97	  |	10.8.2.110	|	10.8.2.111	|
|	8	|	10.8.2.112	|	28	|	10.8.2.113	|	10.8.2.126	|	10.8.2.127	|
|	9	|	10.8.2.128	|	28	|	10.8.2.129	|	10.8.2.142	|	10.8.2.143	|
|	10|	10.8.2.144	|	28	|	10.8.2.145	|	10.8.2.158	|	10.8.2.159	|
|	11|	10.8.2.160	|	28	|	10.8.2.161	|	10.8.2.174	|	10.8.2.175	|
|	12|	10.8.2.176	|	29	|	10.8.2.177	|	10.8.2.182	|	10.8.2.183	|
|	13|	10.8.2.184	|	29	|	10.8.2.185	|	10.8.2.190	|	10.8.2.191	|
|	14|	10.8.2.192	|	29	|	10.8.2.193	|	10.8.2.198	|	10.8.2.199	|
|	15|	10.8.2.200	|	29	|	10.8.2.201	|	10.8.2.206	|	10.8.2.207	|
|	16|	10.8.2.208	|	29	|	10.8.2.209	|	10.8.2.214	|	10.8.2.215	|
|	17|	10.8.2.216	|	29	|	10.8.2.217	|	10.8.2.222	|	10.8.2.223	|
|	18|	10.8.2.224	|	29	|	10.8.2.225	|	10.8.2.230	|	10.8.2.231	|
|	19|	10.8.2.232	|	29	|	10.8.2.233	|	10.8.2.238	|	10.8.2.239	|
|	20|	10.8.2.240	|	29	|	10.8.2.241	|	10.8.2.246	|	10.8.2.247	|
|	21|	10.8.2.248	|	29	|	10.8.2.249	|	10.8.2.254	|	10.8.2.255	|

б) В сети 172.16.1.0/26 62 доступных хоста (**2 в степени 6 минус бродкаст и адрес сети**). В сети 10.0.0.0/18 - 16382 (**2 в степени 14 минус бродкаст и адрес сети** или же **64*256-2**).

в) В сети 10.0.0.0/30 бродкаст 10.0.0.3, в сети 10.255.255.124/30 - 10.255.255.127.

#### 3
*Настроить OSPF маршрутизацию (основу сети взять из Task4.pkt)*

[Файл задания 2](Task4_ospf.pkt)