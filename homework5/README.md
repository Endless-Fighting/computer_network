### 1

there are 14 paths in total.

y-x-u, y-w-u, 

y-x-v-u, y-x-w-u, y-w-v-u, y-w-x-u, y-z-w-u, 

y-w-x-v-u, y-w-v-x-u, y-x-w-v-u, y-z-w-v-u, y-z-w-x-u, 

y-z-w-x-v-u, y-z-w-v-x-u



### 2

a. from x to z, 10 paths

x-y-z, x-w-z, 

x-y-w-z, x-w-y-z, x-v-w-z, x-u-w-z, 

x-v-w-y-z, x-u-w-y-z, x-u-v-w-z, 

x-u-v-w-y-z

b. from z to u, 18 paths

z-w-u,

z-w-v-u, z-w-x-u, z-y-x-u, 

z-y-x-v-u, z-w-v-x-u, z-w-x-v-u, z-w-y-x-u, z-y-w-v-u, z-y-w-x-u, 

z-w-y-x-v-u, z-y-x-w-u, z-y-x-w-y-u, z-y-x-v-w-u, z-y-w-v-x-u, z-y-w-x-v-u, z-y-w-y-x-u, 

z-y-w-y-x-v-u

c. from z to w, 7 paths

z-w, 

z-y-w, 

z-y-x-w, 

z-y-x-v-w, z-y-x-u-w, 

z-y-x-u-v-w, z-y-x-v-u-w



### 3

| step | N'      | D(t), p(t) | D(u), p(u) | D(v), p(v) | D(w), p(w) | D(y), p(y) | D(z), p(z) |
| ---- | ------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 0    | x       | infinity   | infinity   | **3, x**   | 6, x       | 6, x       | 8, x       |
| 1    | xv      | 7, v       | **6, v**   | -          | 6, x       | 6, x       | 8, x       |
| 2    | xvu     | 7, v       | -          | -          | **6, x**   | 6, x       | 8, x       |
| 3    | xvuw    | 7, v       | -          | -          | -          | **6, x**   | 8, x       |
| 4    | xvuwy   | **7, v**   | -          | -          | -          | -          | 8, x       |
| 5    | xvuwyt  | -          | -          | -          | -          | -          | **8, x**   |
| End  | xvuwytz | 7          | 6          | 3          | 6          | 6          | 8          |



### 5

| from \ cost | u        | v        | x        | y        | z        |
| ----------- | -------- | -------- | -------- | -------- | -------- |
| v           | infinity | infinity | infinity | infinity | infinity |
| x           | infinity | infinity | infinity | infinity | infinity |
| z           | infinity | 6        | 2        | infinity | 0        |

| from \ cost | u        | v    | x    | y        | z    |
| ----------- | -------- | ---- | ---- | -------- | ---- |
| v           | 1        | 0    | 3    | infinity | 6    |
| x           | infinity | 3    | 0    | 3        | 2    |
| z           | 7        | 5    | 2    | 5        | 0    |

| from \ cost | u    | v    | x    | y    | z    |
| ----------- | ---- | ---- | ---- | ---- | ---- |
| v           | 1    | 0    | 3    | 3    | 6    |
| x           | 4    | 3    | 0    | 3    | 2    |
| z           | 6    | 5    | 2    | 5    | 0    |

| from \ cost | u    | v    | x    | y    | z    |
| ----------- | ---- | ---- | ---- | ---- | ---- |
| v           | 1    | 0    | 3    | 3    | 5    |
| x           | 4    | 3    | 0    | 3    | 2    |
| z           | 6    | 5    | 2    | 5    | 0    |



### 9

a. 

count-to-infinity problem won't occur when decreasing the cost of links since no loop will occur

b.

it's the same with decreasing the cost since the cost of two nodes that are not connected can be regarded as infinity