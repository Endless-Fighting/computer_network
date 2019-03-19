### 1

suppose the port of A and B are *a* and *b* respectively

a. a 23

b. b 23

c. 23 a

d. 23 b

e. yes

f. it's impossible if they are the same host



### 2

for the segment to host A

source port is 80

des port is 26145

source IP is the IP of host B

des IP is the IP of host A



for the first segment to host C

source port is 80

des port is 7532

source IP is the IP of host B

des IP is the IP of host C



for the second segment to host C

source port is 80

des port is 26145

source IP is the IP of host B

des IP is the IP of host C



### 3

the complement is computed as follows:

  01010011

+01100110

---

  10111001

+01110100

---

  00101110

by using the complement, the receiver only need to add all the words and the check sum together. if the sum contain any 0, there must be an error.

if only one bit is wrong, it can certainly be detected, but if even number of errors happen, it can be uncertain



### 4

a. 00111110

b. 10111111

c. 01011100 -> 11011100

​    01100101 -> 11100101



### 40

a. [1, 6] and [23, 26]

b. [6, 16] and [17, 22]

c. 3 duplicate ACK

d. timeout

e. 32, because the slow start stops at 32

f. 42/2 = 21

g. 29/2 = 14

h. 1+2+4+8+16+32 = 63 segments 

​     63 + 32 > 70, thus the 70th segment is sent in the 7th round

i. window size = 7, threshold = 4

j. window size = 1, threshold = 21

k.  from 17th to 22nd round, 1+2+4+8+16+21 = 52 packets

