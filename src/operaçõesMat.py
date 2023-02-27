# USAR OPERAÇÕES MATEMÁTICAS

from math import ceil, floor


seconds = 1042
display_minutes = 1042 // 60  # arredondar para baixo usando a função piso //.
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)
# 17
# 22

print(abs(39 - 16))
print(abs(16 - 39))
# 23
# 23

print(round(14.5))
# 15


round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
# 13
# 12
