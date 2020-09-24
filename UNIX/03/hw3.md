#### 1
*Создать файл file1 и наполнить его произвольным содержимым.
Скопировать его в file2. Создать символическую ссылку file3 на file1.
Создать жесткую ссылку file4 на file1. Посмотреть, какие айноды у файлов.
Удалить file1. Что стало с остальными созданными файлами?
Попробовать вывести их на экран.*

    $ echo 'asldkfhaslkdfhalkshfkajshf' > file1
    $ cp file1 file2
    $ ln -s file1 file3
    $ ln file1 file4
    $ ls -li
      total 12
      68020641 -rw-rw-r--. 2 user user 27 Sep 24 11:24 file1
      68020642 -rw-rw-r--. 1 user user 27 Sep 24 11:25 file2
      68020643 lrwxrwxrwx. 1 user user  5 Sep 24 11:25 file3 -> file1
      68020641 -rw-rw-r--. 2 user user 27 Sep 24 11:24 file4
    $ rm file1
    $ ls -li
      total 8
      68020642 -rw-rw-r--. 1 user user 27 Sep 24 11:25 file2
      68020643 lrwxrwxrwx. 1 user user  5 Sep 24 11:25 file3 -> file1
      68020641 -rw-rw-r--. 1 user user 27 Sep 24 11:24 file4

После удаления file1 симлинк и хардлинк остались.

    $ cat file2
      asldkfhaslkdfhalkshfkajshf
    $ cat file3
      cat: file3: No such file or directory
    $ cat file4
      asldkfhaslkdfhalkshfkajshf

Симлинк, соответственно, ссылается на несуществующий файл и не открывается.  
***
#### 2
*Дать созданным файлам другие, произвольные имена.
Создать новую символическую ссылку. Переместить ссылки в другую директорию.*

    $ mv file2  newfile2
    $ ln -s newfile2 newlink
    $ mkdir test
    $ mv newlink test/
    $ mv file4  newfile4
    $ mv newfile4 test/
    $ cat test/newfile4
      asldkfhaslkdfhalkshfkajshf
    $ cat test/newlink
      cat: test/newlink: No such file or directory
Симлинк не работает, поскольку ссылается на текущий каталог.
Хардлинк работает.  Если создать симлинк вот так, то ссылку можно перемещать:

    $ ln -s /home/user/newfile2 newlink3
    $ mv newlink3 test/
    $ cat test/newlink3
      asldkfhaslkdfhalkshfkajshf

#### 3
*Создать два произвольных файла. Первому присвоить права на чтение,
запись для владельца и группы, только на чтение — для всех.
Второму присвоить права на чтение, запись — только для владельца.
Сделать это в численном и символьном виде.*

    $ touch testfile1 testfile2
    $ chmod ug=rw,o=r testfile1
    $ chmod u=rw,go=- testfile2
    $ ls -l
      total 0
      -rw-rw-r--. 1 user user 0 Sep 24 11:55 testfile1
      -rw-------. 1 user user 0 Sep 24 11:55 testfile2
    $ chmod 664 testfile1
    $ chmod 600 testfile2
    $ ls -l
      total 0
      -rw-rw-r--. 1 user user 0 Sep 24 11:55 testfile1
      -rw-------. 1 user user 0 Sep 24 11:55 testfile2


#### 4
*Создать пользователя, обладающего возможностью выполнять действия
от имени суперпользователя.*

В CentOS группа пользователей, имеющих право вызывать команду sudo,
называется wheel.

    $ cat /etc/group | grep wheel
      wheel:x:10:user
    $ sudo useradd newroot -g wheel
      [sudo] password for user:
    $ tail -1 /etc/passwd
      newroot:x:1001:10::/home/newroot:/bin/bash
    $ sudo passwd newroot
      Changing password for user newroot.
      New password:
      Retype new password:
      passwd: all authentication tokens updated successfully.
    $ su newroot
      Password:
    $ id
      uid=1001(newroot) gid=10(wheel) groups=10(wheel) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
    $ sudo tail /etc/shadow | cut -d: -f1
      nobody
      systemd-network
      dbus
      polkitd
      sshd
      postfix
      chrony
      user
      mysql
      newroot

#### 5
*Создать группу developer и несколько пользователей, входящих в нее.
Создать директорию для совместной работы.
Сделать так, чтобы созданные одними пользователями файлы могли
изменять другие пользователи этой группы.*

    $ sudo useradd devuser1 -g developer
    $ sudo useradd devuser2 -g developer
    $ sudo passwd devuser1
    $ sudo passwd devuser2
    $ cat /etc/group | grep dev
      developer:x:1001
    $ cat /etc/passwd | grep devuser
      devuser1:x:1002:1001::/home/devuser1:/bin/bash
      devuser2:x:1003:1001::/home/devuser2:/bin/bash
    $ sudo -i
    # cd /home/
    # mkdir devs
    # chgrp -R developer devs
    # chmod 775 devs
    # setfacl -d -m u::rwx,g::rwx,o::r-x /home/devs
    # getfacl devs
      # file: devs
      # owner: root
      # group: developer
      user::rwx
      group::rwx
      other::r-x
      default:user::rwx
      default:group::rwx
      default:other::r-x
    # su devuser1
    $ touch devs/file
    $ ls -l devs/
      total 0
      -rw-rw-r--. 1 devuser1 developer 0 Sep 24 19:07 file

#### 6
*Создать в директории для совместной работы поддиректорию для обмена файлами,
но чтобы удалять файлы могли только их создатели.*

    [root@gb-homework devs]# su devuser1
    [devuser1@gb-homework devs]$ mkdir test
    [devuser1@gb-homework devs]$ chmod +t test
    [devuser1@gb-homework devs]$ ls -l
      total 0
      -rw-rw-r--. 1 devuser1 developer 0 Sep 24 19:07 file
      drwxrwxr-t+ 2 devuser1 developer 6 Sep 24 19:17 test
    [devuser1@gb-homework devs]$ touch test/file1
    [devuser1@gb-homework devs]$ exit
    [root@gb-homework devs]# su devuser2
    [devuser2@gb-homework devs]$ echo 'sfasdf' > test/file1
    [devuser2@gb-homework devs]$ rm -f test/file1
      rm: cannot remove Б─≤test/file1Б─≥: Operation not permitted

#### 7
*Создать директорию, в которой есть несколько файлов.
Сделать так, чтобы открыть файлы можно было, только зная имя файла,
а через ls список файлов посмотреть было нельзя.*

    [root@gb-homework home]# mkdir test
    [root@gb-homework home]# ls -l
      total 0
      drwxr-xr-x. 2 root root   6 Sep 24 19:30 test
      drwx------. 4 user user 238 Sep 24 18:45 user
    [root@gb-homework home]# echo 'test' > test/file
    [root@gb-homework home]# ll test/
      total 4
      -rw-r--r--. 1 root root 5 Sep 24 19:31 file

Права на чтение файла есть у other. Уберем право чтения с каталога.

    [root@gb-homework home]# chmod o-r test/
    [root@gb-homework home]# echo 'another file' > test/file2
    [root@gb-homework home]# su user
    [user@gb-homework home]$ cd test/
    [user@gb-homework test]$ ls
      ls: cannot open directory .: Permission denied
    [user@gb-homework test]$ cat file
      test
    [user@gb-homework test]$ cat file2
      another file
