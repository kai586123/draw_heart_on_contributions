# select any date on Wednesday
date_wednesday = '2023-11-01'
draw_index_raw = [(3, 8)]
draw_cnt = [10]

draw_index_raw.append((draw_index_raw[0][0] - 1, draw_index_raw[0][1]))
draw_index_raw.append((draw_index_raw[0][0] - 2, draw_index_raw[0][1]))
draw_index_raw.append((draw_index_raw[0][0] - 3, draw_index_raw[0][1] + 1))
draw_index_raw.append((draw_index_raw[0][0] - 3, draw_index_raw[0][1] + 2))
draw_index_raw.append((draw_index_raw[0][0] - 2, draw_index_raw[0][1] + 3))
draw_index_raw.append((draw_index_raw[0][0] - 3, draw_index_raw[0][1] + 4))
draw_index_raw.append((draw_index_raw[0][0] - 3, draw_index_raw[0][1] + 5))
draw_index_raw.append((draw_index_raw[0][0] - 2, draw_index_raw[0][1] + 6))
draw_index_raw.append((draw_index_raw[0][0] - 1, draw_index_raw[0][1] + 6))
draw_index_raw.append((draw_index_raw[0][0], draw_index_raw[0][1] + 6))
draw_index_raw.append((draw_index_raw[0][0] + 1, draw_index_raw[0][1] + 1))
draw_index_raw.append((draw_index_raw[0][0] + 2, draw_index_raw[0][1] + 2))
draw_index_raw.append((draw_index_raw[0][0] + 3, draw_index_raw[0][1] + 3))
draw_index_raw.append((draw_index_raw[0][0] + 1, draw_index_raw[0][1] + 5))
draw_index_raw.append((draw_index_raw[0][0] + 2, draw_index_raw[0][1] + 4))
for i in range(len(draw_index_raw) - 1):
    draw_cnt.append(10)

import pandas as pd
draw_index_real = [pd.to_datetime(date_wednesday)]
x0, y0 = draw_index_raw[0]
for i in range(1, len(draw_index_raw)):
    x, y = draw_index_raw[i]
    gap_days = (x - x0) + (y - y0) * 7
    draw_index_real.append(draw_index_real[0] + pd.DateOffset(days=gap_days))

to_bash_commands = []

for i, date in enumerate(draw_index_real):
    for j in range(draw_cnt[i]):
        to_bash_commands.append(f'git commit --allow-empty --date="{date.strftime("%Y-%m-%d")}" -m "draw a red heart"')

bash_cmd_str = ' && '.join(to_bash_commands)
print(bash_cmd_str)

import os
os.system(f'{bash_cmd_str}')

