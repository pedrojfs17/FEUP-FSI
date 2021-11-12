# Trabalho Realizado na Semana 4

## CTF

### Desafio 1

After some time exploring the website, we found some important information about versions, plugins installed and the active accounts on the website:

```
Wordpress version: 5.8.1

Installed Plugins and their versions:
- WooCommerce plugin -> 5.7.1
- Booster for WooCommerce plugin -> 5.4.3

Active users:
- admin
- Orval Sanford

Exploit: https://www.exploit-db.com/exploits/50299 -> Vulnerabilidade do Booster for WooCommerce
flag{CVE-2021-34646}
flag{e78dd1ba649539b0104483b1e9c37ff0}
```

With some research on CVE databases, we found a vulnerability in the Booster for WooComerce plugin, which made it possible for an attacker to log in as any user. The CVE was `CVE-2021-34646`, with a CVSS score of 9.8 (critical).

Flag:
```
flag{CVE-2021-34646}
```

### Desafio 2

With some research on the CVE, we found an exploit, https://www.exploit-db.com/exploits/50299, that we used to easily log in as the admin user in the website. Using this script with the id 1, which is usually the admin since is the first account created on the database, it generates 3 links that can be used to log in as the admin.

After logging in, we just needed to go to http://ctf-fsi.fe.up.pt:5001/wp-admin/edit.php, and in the private file there was the flag.

Flag:
```
flag{e78dd1ba649539b0104483b1e9c37ff0}
```

---

## Environment Variable and Set-UID Program Lab

### Task 1

Output:
```
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1907,unix/VM:/tmp/.ICE-unix/1907
QT_ACCESSIBILITY=1
COLORTERM=truecolor
XDG_CONFIG_DIRS=/etc/xdg/xdg-ubuntu:/etc/xdg
XDG_MENU_PREFIX=gnome-
GNOME_DESKTOP_SESSION_ID=this-is-deprecated
GNOME_SHELL_SESSION_MODE=ubuntu
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
XMODIFIERS=@im=ibus
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
GTK_MODULES=gail:atk-bridge
PWD=/home/seed/Desktop/seed-labs/category-software/Environment_Variable_and_SetUID
LOGNAME=seed
XDG_SESSION_DESKTOP=ubuntu
XDG_SESSION_TYPE=x11
GPG_AGENT_INFO=/run/user/1000/gnupg/S.gpg-agent:0:1
XAUTHORITY=/run/user/1000/gdm/Xauthority
GJS_DEBUG_TOPICS=JS ERROR;JS LOG
WINDOWPATH=2
HOME=/home/seed
USERNAME=seed
IM_CONFIG_PHASE=1
LANG=en_US.UTF-8
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
XDG_CURRENT_DESKTOP=ubuntu:GNOME
VTE_VERSION=6003
GNOME_TERMINAL_SCREEN=/org/gnome/Terminal/screen/fbf4393d_de50_4cd9_80ca_fde7c269b52d
INVOCATION_ID=5d8488cf5ee548a5902b6ebb00c7146e
MANAGERPID=1641
GJS_DEBUG_OUTPUT=stderr
LESSCLOSE=/usr/bin/lesspipe %s %s
XDG_SESSION_CLASS=user
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=seed
GNOME_TERMINAL_SERVICE=:1.111
DISPLAY=:0
SHLVL=1
QT_IM_MODULE=ibus
XDG_RUNTIME_DIR=/run/user/1000
JOURNAL_STREAM=9:33295
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:.
GDMSESSION=ubuntu
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
OLDPWD=/home/seed/Desktop/seed-labs/category-software
_=/usr/bin/printenv
```

### Task 2

Environment variables are passed on to the children process. The output from the parent process was equal to the children's one.

### Task 3

If the `environ` is not passed in the execve call, the environment variables are not passed to the new process. Otherwise, the environment variables remain the same.

### Task 4

The output of the system call are the environment variables, which means that the system call passes the environment variables array to the execve call.

### Task 5

All the variables set in the shell process are printed in the child process.

### Task 6

Running the following command adds the current working directory to the PATH environment variable.

```bash
export PATH="/home/seed/Desktop/seed-labs/category-software/Environment_Variable_and_SetUID/Labsetup/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:."
```

With this, when the system call is made, it will look for an executable called `ls` in the folders in the PATH variable starting from the first one, which is my working directory.

After that, we created an executable with the following code:

```c
#include <zconf.h>
#include <stdio.h>
int main() {
    int a;
    a = geteuid();

    if (a == 0)
        printf("You are the root user!\n");
    else
        printf("You are not the root user!\n");
    
    return 0;
}
```

This program was compiled with the command `gcc attack.c -o ls` which created an executable called `ls` in our working directory. Running the Set-UID program which had the root privileges, it will make a call to the `/bin/dash` which will then look for a `ls`, our executable, and will execute it. This `/bin/dash` has the countermeasure to avoid this kind of attacks, so it will run our executable with the user permissions and the output will be "You are not the root user!". Running the command given, to create a symbolic link from `/bin/sh` to `/bin/zsh`, and running the executable again, the new call will run our `ls` and the output will be "You are the root user!", showing that there is a vulnerability that is easily exploited by changing the PATH environment variable. 

