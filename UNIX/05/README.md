#### 1
*Произвести ручную настройку сети в Ubuntu, на каждом шаге сделать скриншоты.*

В моем случае система - CentOS, поэтому настройка будет другой.
Вариантов несколько, например:
1. Правка конфигурационного файла интерфейса в текстовом редакторе. Задано вручную.

![](5-1.PNG)

2. Утилита **nmtui**:

![](5-2.PNG)

![](5-3.PNG)

Проверяем:

![](5-4.PNG)

#### 2
*Переключить настройку сети на автоматическую через DHCP, проверить получение адреса.*

Переключаем на DHCP:

![](5-5.PNG)

При правке руками конфигурационного файла интерфейса необходимо удалить следующие строки:
**IPADDR**
**PREFIX**
**GATEWAY**
**DNS1**
**DNS2**

И изменить **BOOTPROTO** со **static** на **dhcp**.

При любом варианте после внесения изменений нужно либо перезагрузить службу **network**, либо сделать **ifdown eth0 && ifup eth0**.

![](5-6.PNG)

#### 3
*Изменить адрес DNS на 1.1.1.1 и проверить доступность интернета, например, открыв любой браузер на адрес https://geekbrains.ru.*

Проверяем работу Интернета:

![](5-7.PNG)

Меняем DNS:

![](5-8.PNG)

![](5-9.PNG)

Опять проверяем:

![](5-10.PNG)

Ничего не изменилось. Причина в том, что 1.1.1.1 - это публичный DNS. Если изменить на адрес, который не является таковым, то работать будет доступ только через ip-адреса.

#### 4
*Настроить правила iptables, чтобы из внешней сети можно было обратиться только к портам 80 и 443. Запросы на порт 8080 перенаправлять на порт 80.*

На CentOS7 обвязка для iptables - это firewalld. Для начала проверим, что открыто. Для этого нужно отдельно посмотреть список разрешенных сервисов и портов:

![](5-11.PNG)

Для того, чтобы все настройки сохранялись не только на текущую сессию, нужно добавлять **--permanent** во все команды после **firewall-cmd**. Я этого делать не буду, чтобы потом не удалять настройки.

SSH я закрывать не стал, поскольку подключен удаленно.

Открываем 80 и 443 порты, перенаправляем 8080 на 80:

![](5-12.PNG)

Проверяем с помощью модуля *SimpleHTTPServer* в python:

![](5-13.PNG)

#### 5
*Дополнительно к предыдущему заданию настроить доступ по ssh только из указанной сети.*

Поскольку я сижу по SSH, то данную настройку сделал для telnet. При появлении дополнительных ограничений (например, адрес\порт источника) необходимо создать новую зону (её нельзя добавить только в текущей сессии) для этого порта. Для проверки опять использовал *SimpleHTTPServer*:

![](5-14.PNG)

С машины из другой сети:

![](5-15.PNG)