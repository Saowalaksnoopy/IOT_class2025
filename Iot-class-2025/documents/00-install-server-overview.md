# การติดตั้ง Debian สำหรับเรียน IoT, MQTT และ Kafka

## 🖥️ ความต้องการเบื้องต้น
- USB Bootable Debian 12 Bookworm
- คอมพิวเตอร์หรือ DeLL, VM ที่จะใช้ติดตั้ง
- อินเทอร์เน็ต (สำหรับอัปเดต package)
- คีย์บอร์ด, จอภาพ, เมาส์

---

## 1️⃣ การเริ่มต้นติดตั้ง Debian

### 1.1 Boot จาก USB
- เสียบ USB ที่มี Debian
- เปิดเครื่อง แล้วกดปุ่ม Boot Menu (เช่น `F12`, `ESC`, หรือ `DEL`)
- เลือก Boot จาก USB

---

## 2 การแบ่งพาร์ติชัน (Manual Partition)

### 2.1 เลือก Guided หรือ Manual
- ให้เลือก **Manual** เพื่อฝึกจัดการพาร์ติชันด้วยตนเอง

### 2.2 ตัวอย่างการแบ่งพาร์ติชัน
| พาร์ติชัน | ขนาด | ระบบไฟล์ | จุดเมาต์ |
|-----------|------|-----------|-----------|
| EFI       | 512 MB | FAT32     | /boot/efi |
| Swap      | 2 GB   | swap      | -         |
| /         | 20 GB  | ext4      | /   |

### 2.3 คำแนะนำ
- สำหรับเครื่องที่ RAM < 4GB แนะนำ swap = 2GB
- ตรวจสอบว่าใช้ GPT หรือ MBR ตาม BIOS/UEFI ของเครื่อง

---

## 3 การตั้งค่า IP Address แบบ Static

### 3.1 แก้ไขไฟล์ Netplan (สำหรับ Debian 12+ ที่ใช้ `systemd-networkd`)
```bash
sudo nano /etc/network/interfaces

auto eth0
iface eth0 inet static
    address 192.168.1.100
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 1.1.1.1 8.8.8.8

```

### 3.3 รีสตาร์ต Network
```bash
sudo systemctl restart networking
```

### 3.4 การตั้งค่า Hostname
Hostname คือชื่อของเครื่องในระบบเครือข่าย เช่น iot-node01 หรือ kafka-server

🔧 วิธีตั้งค่า

1. แก้ไขไฟล์ /etc/hostname
```bash
sudo nano /etc/hostname

ใส่ชื่อเครื่องที่ต้องการ เช่น:
iot-node01
```
2. แก้ไขไฟล์ /etc/hosts

```bash
sudo nano /etc/hosts

แก้บรรทัดที่มี 127.0.1.1 ให้เป็นชื่อที่ตั้งไว้ เช่น:
127.0.1.1   iot-node01
```

3. ใช้คำสั่งเปลี่ยน hostname (ทางเลือก)

```bash
sudo hostnamectl set-hostname iot-node01
```
4. ตรวจสอบว่าเปลี่ยนสำเร็จ:

```bash
hostname
```
5. รีบูตเครื่อง

```bash
sudo reboot
```

## 4️ ตรวจสอบการเชื่อมต่อ
```bash
ip a          # ตรวจสอบ IP
ping 8.8.8.8  # ทดสอบเชื่อมต่อ Internet
```

## 5 ตรวจสอบการติดตั้ง apt source list
```bash
sudo nano /etc/apt/sources.list
```

ใส่รายละเอียดของ source list สำหรับ package

```
deb https://deb.debian.org/debian bookworm main contrib non-free non-free-firmware
deb-src https://deb.debian.org/debian bookworm main contrib non-free non-free-firmware

deb https://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware
deb-src https://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware

deb https://deb.debian.org/debian bookworm-updates main contrib non-free non-free-firmware
deb-src https://deb.debian.org/debian bookworm-updates main contrib non-free non-free-firmware

```
## 5  แนะนำคำสั่งพื้นฐานหลังติดตั้ง
```bash
sudo apt update && sudo apt upgrade
sudo apt install net-tools curl wget git vim
```


ยอดเยี่ยมครับ! การใช้ `nmtui` (Network Manager Text User Interface) เป็นวิธีที่ **สะดวกและเหมาะสำหรับนักเรียน** ในการตั้งค่า IP แบบ Static บน Raspberry Pi โดยไม่ต้องแก้ไฟล์ด้วยมือ

---

## 🖧 การตั้งค่า IP Address บน Raspberry Pi ด้วย `nmtui`

> `nmtui` คือเครื่องมือ text UI สำหรับจัดการเครือข่าย โดยใช้ NetworkManager

### เงื่อนไข

* Raspberry Pi ต้องใช้ OS ที่ **ติดตั้ง `NetworkManager`** แล้ว (เช่น Debian ARM64, Ubuntu Server)
* หากยังไม่มี ให้ติดตั้งก่อน:

```bash
sudo apt update
sudo apt install network-manager
sudo systemctl stop dhcpcd
sudo systemctl disable dhcpcd
sudo systemctl enable NetworkManager
sudo reboot
```

---

## ขั้นตอนการใช้งาน `nmtui`

### 1. เปิดโปรแกรม

```bash
sudo nmtui
```

จะขึ้นหน้าจอแบบ Text GUI ให้เลือกด้วยปุ่มลูกศรและ Enter

---

### 2. เลือกเมนู `Edit a connection`

---

### 3. เลือก interface ที่ต้องการ (เช่น `eth0` หรือ `wlan0`) แล้วกด Enter

---

### 4. แก้ไขค่าต่อไปนี้:

* **Automatic (DHCP):** เปลี่ยนเป็น `Manual`

* **Addresses:** ใส่ IP แบบ static เช่น:

  ```
  192.168.1.50/24
  ```

* **Gateway:** เช่น:

  ```
  192.168.1.1
  ```

* **DNS Servers:** เช่น:

  ```
  1.1.1.1,8.8.8.8
  ```

* (ถ้ามี) กำหนดชื่อ connection เช่น `IoT-Static`

---

### 5. เลือก “OK” เพื่อบันทึก

---

### 6. กลับไปหน้าแรก แล้วเลือก `Activate a connection`

* เลือกชื่อ connection ที่เพิ่งแก้ แล้วกด `Deactivate` → จากนั้น `Activate` ใหม่

---

### 7. ตรวจสอบ IP ใหม่

```bash
ip a
```

---

## 📦 ติดตั้ง `nmtui` (หากยังไม่มี)

```bash
sudo apt install network-manager network-manager-gnome
```

---

## 📘 หมายเหตุสำหรับนักเรียน

> หากนักเรียนใช้ Raspberry Pi OS Lite (Debian ที่ใช้ `dhcpcd` เป็นหลัก) อาจต้อง **ปิด dhcpcd** เพื่อหลีกทางให้ NetworkManager

```bash
sudo systemctl stop dhcpcd
sudo systemctl disable dhcpcd
sudo systemctl enable NetworkManager
sudo reboot
```

---/


