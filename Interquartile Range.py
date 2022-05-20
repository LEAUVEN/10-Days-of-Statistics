import statistics as st

size = int(input())
veriler = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(size):
    s += [veriler[i]] * freq[i]
Toplamm = sum(freq)
s.sort()

if size%2 != 0:
    q1 = st.median(s[:Toplamm//2])
    q3 = st.median(s[Toplamm//2+1:])
else:
    q1 = st.median(s[:Toplamm//2])
    q3 = st.median(s[Toplamm//2:])

ir = round(float(q3-q1), 1)
print(ir)

