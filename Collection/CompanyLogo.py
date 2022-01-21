from collections import Counter
s = input()
s_counter = Counter(sorted(s.strip())).most_common()
for i in range(3):
    print(f"{s_counter[i][0]} {s_counter[i][1]}")

