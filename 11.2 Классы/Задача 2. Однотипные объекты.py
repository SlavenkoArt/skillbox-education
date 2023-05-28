# class Monitor:
#     monitor_name_1 = 'Samsung'
#     monitor_matrix_1 = 'VA'
#     monitor_res_1 = 'WQHD'
#     monitor_freq_1 = 60
#
# monitor1 = Monitor()
# monitor2 = Monitor()
# monitor2.monitor_freq_1 = 144
# monitor3 = Monitor()
# monitor3.monitor_freq_1 = 70
# monitor4 = Monitor()
# monitor4.monitor_freq_1 = 60
# class Headphones:
#     headphones_name_1 = 'Sony'
#     headphones_sensitivity_1 = 108
#     headphones_micro_1 = False
#
# headphones1 = Headphones()
# headphones2 = Headphones()
# headphones2.headphones_micro_1 = True
# headphones3 = Headphones()
# headphones3.headphones_micro_1 = True

class Monitor:
    name = "Samsung"
    matrix = "VA"
    resolution = "WQHD"
    frequency = 0


class Headphones:
    name = "Sony"
    sensitivity = 108
    micro = True

monitors = [Monitor() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].frequency = number

headphones[0].micro = False

print(monitors[1].frequency)