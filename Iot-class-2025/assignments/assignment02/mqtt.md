# Exploring MQTT QoS Levels

Experiment with QoS 0, 1, and 2.
Observe how message delivery changes based on QoS settings.

## Publisher_qos.py output

```
[15:18:57] DEBUG | Sending CONNECT (u0, p0, wr0, wq0, wf0, c1, k60) client_id=b''
Enter message to publish: [15:18:57] DEBUG | Received CONNACK (0, 0)
iot
Enter QoS level (0, 1, 2): 2
[15:19:17] DEBUG | Sending PUBLISH (d0, q2, r0, m1), 'b'test/qos/6510301042/temperature'', ... (3 bytes)
[15:19:17] PUBLISH REQUESTED | QoS=2 | Message='iot' | msgid=1
Enter message to publish: [15:19:17] DEBUG | Received PUBREC (Mid: 1)
[15:19:17] DEBUG | Sending PUBREL (Mid: 1)
[15:19:17] DEBUG | Received PUBCOMP (Mid: 1)
[15:19:17] PUBLISHED | msgid=1
```

## Subscriber_qos.py Output

```
[15:14:51] DEBUG | Sending CONNECT (u0, p0, wr0, wq0, wf0, c1, k60) client_id=b''
[15:14:51] DEBUG | Received CONNACK (0, 0)
[15:14:51] Connected with result code 0
[15:14:51] DEBUG | Sending SUBSCRIBE (d0, m1) [(b'test/qos/6510301042/#', 2)]
[15:14:51] SUBSCRIBED to test/qos/6510301042/# with QoS=2
[15:14:51] DEBUG | Received SUBACK
[15:15:52] DEBUG | Sending PINGREQ
[15:15:52] DEBUG | Received PINGRESP
[15:16:53] DEBUG | Sending PINGREQ
[15:16:53] DEBUG | Received PINGRESP
[15:17:12] DEBUG | Received PUBLISH (d0, q1, r0, m1), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:12] RECEIVED | temperature: 26.16 | QoS=1
[15:17:12] DEBUG | Sending PUBACK (Mid: 1)
[15:17:12] DEBUG | Received PUBLISH (d0, q1, r0, m2), 'test/qos/6510301042/humidity', ...  (4 bytes)      
[15:17:12] RECEIVED | humidity: 65.6 | QoS=1
[15:17:12] DEBUG | Sending PUBACK (Mid: 2)
[15:17:12] DEBUG | Received PUBLISH (d0, q1, r0, m3), 'test/qos/6510301042/pressure', ...  (7 bytes)      
[15:17:12] RECEIVED | pressure: 1019.11 | QoS=1
[15:17:12] DEBUG | Sending PUBACK (Mid: 3)
[15:17:12] DEBUG | Received PUBLISH (d0, q1, r0, m4), 'test/qos/6510301042/fan_speed', ...  (1 bytes)     
[15:17:12] RECEIVED | fan_speed: 2 | QoS=1
[15:17:12] DEBUG | Sending PUBACK (Mid: 4)
[15:17:15] DEBUG | Received PUBLISH (d0, q1, r0, m5), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:15] RECEIVED | temperature: 32.37 | QoS=1
[15:17:15] DEBUG | Sending PUBACK (Mid: 5)
[15:17:15] DEBUG | Received PUBLISH (d0, q1, r0, m6), 'test/qos/6510301042/humidity', ...  (5 bytes)      
[15:17:15] RECEIVED | humidity: 64.16 | QoS=1
[15:17:15] DEBUG | Sending PUBACK (Mid: 6)
[15:17:15] DEBUG | Received PUBLISH (d0, q1, r0, m7), 'test/qos/6510301042/pressure', ...  (7 bytes)      
[15:17:15] RECEIVED | pressure: 1000.85 | QoS=1
[15:17:15] DEBUG | Sending PUBACK (Mid: 7)
[15:17:15] DEBUG | Received PUBLISH (d0, q1, r0, m8), 'test/qos/6510301042/fan_speed', ...  (1 bytes)     
[15:17:15] RECEIVED | fan_speed: 0 | QoS=1
[15:17:15] DEBUG | Sending PUBACK (Mid: 8)
[15:17:18] DEBUG | Received PUBLISH (d0, q1, r0, m9), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:18] RECEIVED | temperature: 25.81 | QoS=1
[15:17:18] DEBUG | Sending PUBACK (Mid: 9)
[15:17:18] DEBUG | Received PUBLISH (d0, q1, r0, m10), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:18] RECEIVED | humidity: 65.06 | QoS=1
[15:17:18] DEBUG | Sending PUBACK (Mid: 10)
[15:17:18] DEBUG | Received PUBLISH (d0, q1, r0, m11), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:18] RECEIVED | pressure: 1008.94 | QoS=1
[15:17:18] DEBUG | Sending PUBACK (Mid: 11)
[15:17:18] DEBUG | Received PUBLISH (d0, q1, r0, m12), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:18] RECEIVED | fan_speed: 2 | QoS=1
[15:17:18] DEBUG | Sending PUBACK (Mid: 12)
[15:17:21] DEBUG | Received PUBLISH (d0, q1, r0, m13), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:21] RECEIVED | temperature: 29.87 | QoS=1
[15:17:21] DEBUG | Sending PUBACK (Mid: 13)
[15:17:21] DEBUG | Received PUBLISH (d0, q1, r0, m14), 'test/qos/6510301042/humidity', ...  (4 bytes)     
[15:17:21] RECEIVED | humidity: 63.5 | QoS=1
[15:17:21] DEBUG | Sending PUBACK (Mid: 14)
[15:17:21] DEBUG | Received PUBLISH (d0, q1, r0, m15), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:21] RECEIVED | pressure: 1015.05 | QoS=1
[15:17:21] DEBUG | Sending PUBACK (Mid: 15)
[15:17:21] DEBUG | Received PUBLISH (d0, q1, r0, m16), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:21] RECEIVED | fan_speed: 2 | QoS=1
[15:17:21] DEBUG | Sending PUBACK (Mid: 16)
[15:17:24] DEBUG | Received PUBLISH (d0, q1, r0, m17), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:24] RECEIVED | temperature: 31.14 | QoS=1
[15:17:24] DEBUG | Sending PUBACK (Mid: 17)
[15:17:24] DEBUG | Received PUBLISH (d0, q1, r0, m18), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:24] RECEIVED | humidity: 55.38 | QoS=1
[15:17:24] DEBUG | Sending PUBACK (Mid: 18)
[15:17:24] DEBUG | Received PUBLISH (d0, q1, r0, m19), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:24] RECEIVED | pressure: 1007.98 | QoS=1
[15:17:24] DEBUG | Sending PUBACK (Mid: 19)
[15:17:24] DEBUG | Received PUBLISH (d0, q1, r0, m20), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:24] RECEIVED | fan_speed: 0 | QoS=1
[15:17:24] DEBUG | Sending PUBACK (Mid: 20)
[15:17:27] DEBUG | Received PUBLISH (d0, q1, r0, m21), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:27] RECEIVED | temperature: 26.71 | QoS=1
[15:17:27] DEBUG | Sending PUBACK (Mid: 21)
[15:17:27] DEBUG | Received PUBLISH (d0, q1, r0, m22), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:27] RECEIVED | humidity: 46.94 | QoS=1
[15:17:27] DEBUG | Sending PUBACK (Mid: 22)
[15:17:27] DEBUG | Received PUBLISH (d0, q1, r0, m23), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:27] RECEIVED | pressure: 1011.96 | QoS=1
[15:17:27] DEBUG | Sending PUBACK (Mid: 23)
[15:17:27] DEBUG | Received PUBLISH (d0, q1, r0, m24), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:27] RECEIVED | fan_speed: 3 | QoS=1
[15:17:27] DEBUG | Sending PUBACK (Mid: 24)
[15:17:30] DEBUG | Received PUBLISH (d0, q1, r0, m25), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:30] RECEIVED | temperature: 32.95 | QoS=1
[15:17:30] DEBUG | Sending PUBACK (Mid: 25)
[15:17:30] DEBUG | Received PUBLISH (d0, q1, r0, m26), 'test/qos/6510301042/humidity', ...  (4 bytes)     
[15:17:30] RECEIVED | humidity: 54.1 | QoS=1
[15:17:30] DEBUG | Sending PUBACK (Mid: 26)
[15:17:30] DEBUG | Received PUBLISH (d0, q1, r0, m27), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:30] RECEIVED | pressure: 1014.19 | QoS=1
[15:17:30] DEBUG | Sending PUBACK (Mid: 27)
[15:17:30] DEBUG | Received PUBLISH (d0, q1, r0, m28), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:30] RECEIVED | fan_speed: 1 | QoS=1
[15:17:30] DEBUG | Sending PUBACK (Mid: 28)
[15:17:33] DEBUG | Received PUBLISH (d0, q1, r0, m29), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:33] RECEIVED | temperature: 32.77 | QoS=1
[15:17:33] DEBUG | Sending PUBACK (Mid: 29)
[15:17:33] DEBUG | Received PUBLISH (d0, q1, r0, m30), 'test/qos/6510301042/humidity', ...  (4 bytes)     
[15:17:33] RECEIVED | humidity: 47.5 | QoS=1
[15:17:33] DEBUG | Sending PUBACK (Mid: 30)
[15:17:33] DEBUG | Received PUBLISH (d0, q1, r0, m31), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:33] RECEIVED | pressure: 1002.59 | QoS=1
[15:17:33] DEBUG | Sending PUBACK (Mid: 31)
[15:17:33] DEBUG | Received PUBLISH (d0, q1, r0, m32), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:17:33] RECEIVED | fan_speed: 0 | QoS=1
[15:17:33] DEBUG | Sending PUBACK (Mid: 32)
[15:17:33] DEBUG | Received PUBLISH (d0, q1, r0, m33), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:33] RECEIVED | temperature: 28.97 | QoS=1
[15:17:33] DEBUG | Sending PUBACK (Mid: 33)
[15:17:33] DEBUG | Received PUBLISH (d0, q1, r0, m34), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:33] RECEIVED | humidity: 65.87 | QoS=1
[15:17:33] DEBUG | Sending PUBACK (Mid: 34)
[15:17:33] DEBUG | Received PUBLISH (d0, q1, r0, m35), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:33] RECEIVED | pressure: 1018.24 | QoS=1
[15:17:33] DEBUG | Sending PUBACK (Mid: 35)
[15:17:33] DEBUG | Received PUBLISH (d0, q1, r0, m36), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:33] RECEIVED | fan_speed: 0 | QoS=1
[15:17:33] DEBUG | Sending PUBACK (Mid: 36)
[15:17:36] DEBUG | Received PUBLISH (d0, q1, r0, m37), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:36] RECEIVED | temperature: 31.61 | QoS=1
[15:17:36] DEBUG | Sending PUBACK (Mid: 37)
[15:17:36] DEBUG | Received PUBLISH (d0, q1, r0, m38), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:17:36] RECEIVED | humidity: 41.42 | QoS=1
[15:17:36] DEBUG | Sending PUBACK (Mid: 38)
[15:17:36] DEBUG | Received PUBLISH (d0, q1, r0, m39), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:17:36] RECEIVED | pressure: 1012.42 | QoS=1
[15:17:36] DEBUG | Sending PUBACK (Mid: 39)
[15:17:36] DEBUG | Received PUBLISH (d0, q1, r0, m40), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:17:36] RECEIVED | fan_speed: 0 | QoS=1
[15:17:36] DEBUG | Sending PUBACK (Mid: 40)
[15:17:36] DEBUG | Received PUBLISH (d0, q1, r0, m41), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:36] RECEIVED | temperature: 29.69 | QoS=1
[15:17:36] DEBUG | Sending PUBACK (Mid: 41)
[15:17:36] DEBUG | Received PUBLISH (d0, q1, r0, m42), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:36] RECEIVED | humidity: 44.21 | QoS=1
[15:17:36] DEBUG | Sending PUBACK (Mid: 42)
[15:17:36] DEBUG | Received PUBLISH (d0, q1, r0, m43), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:36] RECEIVED | pressure: 1018.88 | QoS=1
[15:17:36] DEBUG | Sending PUBACK (Mid: 43)
[15:17:36] DEBUG | Received PUBLISH (d0, q1, r0, m44), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:36] RECEIVED | fan_speed: 2 | QoS=1
[15:17:36] DEBUG | Sending PUBACK (Mid: 44)
[15:17:39] DEBUG | Received PUBLISH (d0, q1, r0, m45), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:39] RECEIVED | temperature: 28.56 | QoS=1
[15:17:39] DEBUG | Sending PUBACK (Mid: 45)
[15:17:39] DEBUG | Received PUBLISH (d0, q1, r0, m46), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:39] RECEIVED | humidity: 66.98 | QoS=1
[15:17:39] DEBUG | Sending PUBACK (Mid: 46)
[15:17:39] DEBUG | Received PUBLISH (d0, q1, r0, m47), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:39] RECEIVED | pressure: 1001.18 | QoS=1
[15:17:39] DEBUG | Sending PUBACK (Mid: 47)
[15:17:39] DEBUG | Received PUBLISH (d0, q1, r0, m48), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:39] RECEIVED | fan_speed: 3 | QoS=1
[15:17:39] DEBUG | Sending PUBACK (Mid: 48)
[15:17:39] DEBUG | Received PUBLISH (d0, q1, r0, m49), 'test/qos/6510301042/temperature', ...  (5 bytes)  
[15:17:39] RECEIVED | temperature: 33.15 | QoS=1
[15:17:39] DEBUG | Sending PUBACK (Mid: 49)
[15:17:39] DEBUG | Received PUBLISH (d0, q1, r0, m50), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:39] RECEIVED | humidity: 49.39 | QoS=1
[15:17:39] DEBUG | Sending PUBACK (Mid: 50)
[15:17:39] DEBUG | Received PUBLISH (d0, q1, r0, m51), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:39] RECEIVED | pressure: 1011.47 | QoS=1
[15:17:39] DEBUG | Sending PUBACK (Mid: 51)
[15:17:39] DEBUG | Received PUBLISH (d0, q1, r0, m52), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:39] RECEIVED | fan_speed: 1 | QoS=1
[15:17:39] DEBUG | Sending PUBACK (Mid: 52)
[15:17:42] DEBUG | Received PUBLISH (d0, q1, r0, m53), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:42] RECEIVED | temperature: 29.14 | QoS=1
[15:17:42] DEBUG | Sending PUBACK (Mid: 53)
[15:17:42] DEBUG | Received PUBLISH (d0, q1, r0, m54), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:42] RECEIVED | humidity: 68.79 | QoS=1
[15:17:42] DEBUG | Sending PUBACK (Mid: 54)
[15:17:42] DEBUG | Received PUBLISH (d0, q1, r0, m55), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:42] RECEIVED | pressure: 1006.63 | QoS=1
[15:17:42] DEBUG | Sending PUBACK (Mid: 55)
[15:17:42] DEBUG | Received PUBLISH (d0, q1, r0, m56), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:42] RECEIVED | fan_speed: 3 | QoS=1
[15:17:42] DEBUG | Sending PUBACK (Mid: 56)
[15:17:42] DEBUG | Received PUBLISH (d0, q1, r0, m57), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:42] RECEIVED | temperature: 33.73 | QoS=1
[15:17:42] DEBUG | Sending PUBACK (Mid: 57)
[15:17:42] DEBUG | Received PUBLISH (d0, q1, r0, m58), 'test/qos/6510301042/humidity', ...  (5 bytes)     
[15:17:42] RECEIVED | humidity: 63.76 | QoS=1
[15:17:42] DEBUG | Sending PUBACK (Mid: 58)
[15:17:42] DEBUG | Received PUBLISH (d0, q1, r0, m59), 'test/qos/6510301042/pressure', ...  (7 bytes)     
[15:17:42] RECEIVED | pressure: 1011.94 | QoS=1
[15:17:42] DEBUG | Sending PUBACK (Mid: 59)
[15:17:42] DEBUG | Received PUBLISH (d0, q1, r0, m60), 'test/qos/6510301042/fan_speed', ...  (1 bytes)    
[15:17:42] RECEIVED | fan_speed: 1 | QoS=1
[15:17:42] DEBUG | Sending PUBACK (Mid: 60)
[15:17:45] DEBUG | Received PUBLISH (d0, q1, r0, m61), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:45] RECEIVED | temperature: 27.58 | QoS=1
[15:17:45] DEBUG | Sending PUBACK (Mid: 61)
[15:17:45] DEBUG | Received PUBLISH (d0, q1, r0, m62), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:17:45] RECEIVED | humidity: 53.67 | QoS=1
[15:17:45] DEBUG | Sending PUBACK (Mid: 62)
[15:17:45] DEBUG | Received PUBLISH (d0, q1, r0, m63), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:17:45] RECEIVED | pressure: 1003.93 | QoS=1
[15:17:45] DEBUG | Sending PUBACK (Mid: 63)
[15:17:45] DEBUG | Received PUBLISH (d0, q1, r0, m64), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:17:45] RECEIVED | fan_speed: 0 | QoS=1
[15:17:45] DEBUG | Sending PUBACK (Mid: 64)
[15:17:49] DEBUG | Received PUBLISH (d0, q1, r0, m65), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:49] RECEIVED | temperature: 28.17 | QoS=1
[15:17:49] DEBUG | Sending PUBACK (Mid: 65)
[15:17:49] DEBUG | Received PUBLISH (d0, q1, r0, m66), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:17:49] RECEIVED | humidity: 50.04 | QoS=1
[15:17:49] DEBUG | Sending PUBACK (Mid: 66)
[15:17:49] DEBUG | Received PUBLISH (d0, q1, r0, m67), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:17:49] RECEIVED | pressure: 1015.12 | QoS=1
[15:17:49] DEBUG | Sending PUBACK (Mid: 67)
[15:17:49] DEBUG | Received PUBLISH (d0, q1, r0, m68), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:17:49] RECEIVED | fan_speed: 1 | QoS=1
[15:17:49] DEBUG | Sending PUBACK (Mid: 68)
[15:17:52] DEBUG | Received PUBLISH (d0, q1, r0, m69), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:52] RECEIVED | temperature: 29.55 | QoS=1
[15:17:52] DEBUG | Sending PUBACK (Mid: 69)
[15:17:52] DEBUG | Received PUBLISH (d0, q1, r0, m70), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:17:52] RECEIVED | humidity: 51.41 | QoS=1
[15:17:52] DEBUG | Sending PUBACK (Mid: 70)
[15:17:52] DEBUG | Received PUBLISH (d0, q1, r0, m71), 'test/qos/6510301042/pressure', ...  (6 bytes)
[15:17:52] RECEIVED | pressure: 1019.6 | QoS=1
[15:17:52] DEBUG | Sending PUBACK (Mid: 71)
[15:17:52] DEBUG | Received PUBLISH (d0, q1, r0, m72), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:17:52] RECEIVED | fan_speed: 2 | QoS=1
[15:17:52] DEBUG | Sending PUBACK (Mid: 72)
[15:17:53] DEBUG | Sending PINGREQ
[15:17:53] DEBUG | Received PINGRESP
[15:17:55] DEBUG | Received PUBLISH (d0, q1, r0, m73), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:55] RECEIVED | temperature: 31.82 | QoS=1
[15:17:55] DEBUG | Sending PUBACK (Mid: 73)
[15:17:55] DEBUG | Received PUBLISH (d0, q1, r0, m74), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:17:55] RECEIVED | humidity: 51.19 | QoS=1
[15:17:55] DEBUG | Sending PUBACK (Mid: 74)
[15:17:55] DEBUG | Received PUBLISH (d0, q1, r0, m75), 'test/qos/6510301042/pressure', ...  (6 bytes)
[15:17:55] RECEIVED | pressure: 1006.9 | QoS=1
[15:17:55] DEBUG | Sending PUBACK (Mid: 75)
[15:17:55] DEBUG | Received PUBLISH (d0, q1, r0, m76), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:17:55] RECEIVED | fan_speed: 2 | QoS=1
[15:17:55] DEBUG | Sending PUBACK (Mid: 76)
[15:17:58] DEBUG | Received PUBLISH (d0, q1, r0, m77), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:17:58] RECEIVED | temperature: 31.06 | QoS=1
[15:17:58] DEBUG | Sending PUBACK (Mid: 77)
[15:17:58] DEBUG | Received PUBLISH (d0, q1, r0, m78), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:17:58] RECEIVED | humidity: 58.52 | QoS=1
[15:17:58] DEBUG | Sending PUBACK (Mid: 78)
[15:17:58] DEBUG | Received PUBLISH (d0, q1, r0, m79), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:17:58] RECEIVED | pressure: 1015.05 | QoS=1
[15:17:58] DEBUG | Sending PUBACK (Mid: 79)
[15:17:58] DEBUG | Received PUBLISH (d0, q1, r0, m80), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:17:58] RECEIVED | fan_speed: 3 | QoS=1
[15:17:58] DEBUG | Sending PUBACK (Mid: 80)
[15:18:01] DEBUG | Received PUBLISH (d0, q1, r0, m81), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:18:01] RECEIVED | temperature: 28.24 | QoS=1
[15:18:01] DEBUG | Sending PUBACK (Mid: 81)
[15:18:01] DEBUG | Received PUBLISH (d0, q1, r0, m82), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:18:01] RECEIVED | humidity: 56.43 | QoS=1
[15:18:01] DEBUG | Sending PUBACK (Mid: 82)
[15:18:01] DEBUG | Received PUBLISH (d0, q1, r0, m83), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:18:01] RECEIVED | pressure: 1011.01 | QoS=1
[15:18:01] DEBUG | Sending PUBACK (Mid: 83)
[15:18:01] DEBUG | Received PUBLISH (d0, q1, r0, m84), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:18:01] RECEIVED | fan_speed: 2 | QoS=1
[15:18:01] DEBUG | Sending PUBACK (Mid: 84)
[15:18:04] DEBUG | Received PUBLISH (d0, q1, r0, m85), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:18:04] RECEIVED | temperature: 34.44 | QoS=1
[15:18:04] DEBUG | Sending PUBACK (Mid: 85)
[15:18:04] DEBUG | Received PUBLISH (d0, q1, r0, m86), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:18:04] RECEIVED | humidity: 68.34 | QoS=1
[15:18:04] DEBUG | Sending PUBACK (Mid: 86)
[15:18:04] DEBUG | Received PUBLISH (d0, q1, r0, m87), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:18:04] RECEIVED | pressure: 1000.77 | QoS=1
[15:18:04] DEBUG | Sending PUBACK (Mid: 87)
[15:18:04] DEBUG | Received PUBLISH (d0, q1, r0, m88), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:18:04] RECEIVED | fan_speed: 2 | QoS=1
[15:18:04] DEBUG | Sending PUBACK (Mid: 88)
[15:18:07] DEBUG | Received PUBLISH (d0, q1, r0, m89), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:18:07] RECEIVED | temperature: 28.69 | QoS=1
[15:18:07] DEBUG | Sending PUBACK (Mid: 89)
[15:18:07] DEBUG | Received PUBLISH (d0, q1, r0, m90), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:18:07] RECEIVED | humidity: 49.98 | QoS=1
[15:18:07] DEBUG | Sending PUBACK (Mid: 90)
[15:18:07] DEBUG | Received PUBLISH (d0, q1, r0, m91), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:18:07] RECEIVED | pressure: 1010.24 | QoS=1
[15:18:07] DEBUG | Sending PUBACK (Mid: 91)
[15:18:07] DEBUG | Received PUBLISH (d0, q1, r0, m92), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:18:07] RECEIVED | fan_speed: 3 | QoS=1
[15:18:07] DEBUG | Sending PUBACK (Mid: 92)
[15:18:11] DEBUG | Received PUBLISH (d0, q1, r0, m93), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:18:11] RECEIVED | temperature: 26.58 | QoS=1
[15:18:11] DEBUG | Sending PUBACK (Mid: 93)
[15:18:11] DEBUG | Received PUBLISH (d0, q1, r0, m94), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:18:11] RECEIVED | humidity: 53.41 | QoS=1
[15:18:11] DEBUG | Sending PUBACK (Mid: 94)
[15:18:11] DEBUG | Received PUBLISH (d0, q1, r0, m95), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:18:11] RECEIVED | pressure: 1002.42 | QoS=1
[15:18:11] DEBUG | Sending PUBACK (Mid: 95)
[15:18:11] DEBUG | Received PUBLISH (d0, q1, r0, m96), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:18:11] RECEIVED | fan_speed: 3 | QoS=1
[15:18:11] DEBUG | Sending PUBACK (Mid: 96)
[15:18:13] DEBUG | Received PUBLISH (d0, q1, r0, m97), 'test/qos/6510301042/temperature', ...  (5 bytes)
[15:18:13] RECEIVED | temperature: 27.12 | QoS=1
[15:18:13] DEBUG | Sending PUBACK (Mid: 97)
[15:18:13] DEBUG | Received PUBLISH (d0, q1, r0, m98), 'test/qos/6510301042/humidity', ...  (5 bytes)
[15:18:13] RECEIVED | humidity: 64.35 | QoS=1
[15:18:13] DEBUG | Sending PUBACK (Mid: 98)
[15:18:13] DEBUG | Received PUBLISH (d0, q1, r0, m99), 'test/qos/6510301042/pressure', ...  (7 bytes)
[15:18:13] RECEIVED | pressure: 1010.01 | QoS=1
[15:18:13] DEBUG | Sending PUBACK (Mid: 99)
[15:18:13] DEBUG | Received PUBLISH (d0, q1, r0, m100), 'test/qos/6510301042/fan_speed', ...  (1 bytes)
[15:18:13] RECEIVED | fan_speed: 0 | QoS=1
[15:18:13] DEBUG | Sending PUBACK (Mid: 100)
Traceback (most recent call last):
```