r='\033[1;31m'
w='\033[0m'
g='\033[1;32m'
y='\033[1;33m'
blue='\033[1;34m'
cyan='\033[1;36m'
p='\033[1;35m'

import os
os.system("clear")


print("   ▄▄▄▄▀ ▄███▄   █▄▄▄▄ █▀▄▀█   ▄       ▄ ") 
print("▀▀▀ █    █▀   ▀  █  ▄▀ █ █ █    █  ▀▄   █ ")
print("    █    ██▄▄    █▀▀▌  █ ▄ █ █   █   █ ▀  ")
print("   █     █▄   ▄▀ █  █  █   █ █   █  ▄ █   ")
print("  ▀      ▀███▀     █      █  █▄ ▄█ █   ▀▄ ")
print("                  ▀      ▀    ▀▀▀   ▀     ")

print(r+"     ████▄    ▄▄▄▄▄"+w)
print(r+"     █   █   █     ▀▄"+w)
print(r+"     █   █ ▄  ▀▀▀▀▄"+w)
print(r+"     ▀████  ▀▄▄▄▄▀"+w)

print()
print()







print(f"{g}[{w}1{g}]{p} KALI_LINUX                    {r} !!!!!")
print(f"{g}[{w}2{g}]{p} UBUNTU (FOR BEGiNNER)        {r} !!!!!!!")
print(f"{g}[{w}3{g}] {p}ARCH_LINUX                  {r} !!!!!!!!!") 
print(f"{g}[{w}4{g}]{p} DEBIAN_LINUX                 {r} !!!!!!!")  
print(f"{g}[{w}5{g}]{p} KALI_NETHUNTER                {r} !!!!!")
print(f"{g}[{w}6{g}]{p} BACK_BOX                        {w} !")
print(f"{g}[{w}7{g}]{p} FEDORA                          {w} !")
print(f"{g}[{w}8{g}] {p}CENT_OS                  {y}  !-----!-----!")
print(f"{g}[{w}9{g}]{p} BLACK_ARCH               {y}  !           !")
print(f"{g}[{w}10{g}]{p} ALPINE                  {y}  !  {w}_{r}A{w}.{r}R{w}.{r}O{w}_ {y} !") 
print (f" {y}                              !           !")
print (f"    {y}                           !-----------!")


print()
print()
print()
a=int(input(g+"WHICH OS YOU WANT TO INSTALL => "+w))

if a==1:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
    
if a==2:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
if a==3:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh")
if a==4:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
if a==5:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
if a==6:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
if a==7:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
if a==8:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
if a==9:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
if a==10:
    print()
    print("CONSUME STORAGE 1GB + >> PRESS ENTER ")
    print()
    input()
    os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")

