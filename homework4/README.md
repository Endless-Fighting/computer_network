### 1

a. 

| destination | interface |
| ----------- | --------- |
| H3          | 3         |

b. no, since the only difference between these two kinds of traffic is the source ip address. while a forwarding table don't care about the source address.



### 2

a. no, since it's a shared bus, for each time, there can be only one packet transmitted

b. no, the system bus is also a shared bus

c. no, because they are sent over the same output port



### 3

a. (n-1)*D

b. (n-1)*D

c. 0



### 4

a.

| prefix | interface |
| ---------- | ---------- |
| 11100000 00	| 0 |
|11100000 01000000	|   1|
|1110000		|		2|
|11100001 1		|	   3|
|other		|		      3|

b.

1 matches the 5th entry to interface 3

2 matches the 3nd entry to interface 2

3 matches the 4th entry to interface 3



### 6

|destination|interface|count|
|------------|----------|-------------|
|00000000 ~ 00111111|		0	|		64|
|01000000 ~ 01011111|		1	|		32|
|01100000 ~ 10111111|		2	|		96|
|11000000 ~ 11111111|		3	|		64|