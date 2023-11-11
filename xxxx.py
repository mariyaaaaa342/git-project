d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m = 8
n = 31
np = 0
nc = 0
mp = 0
mc = 0
if n == 1:
    np = n - 2
    nc = n + 1
    mp = m - 1
    mc = m
else: n == d[2]


print(f"{str(mp).rjust(2, '0')}.{str(np).rjust(2, '0')} {str(mc).rjust(2, '0')}.{str(nc).rjust(2, '0')}")