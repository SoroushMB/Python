import psutil
import time
import os
import pandas as pd

update_delay = 1

def get_size(bytes):
    for unit in [' ', 'K' , 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

in_out = psutil.net_io_counters(pernic=True)
while True:
    time.sleep(update_delay)
    other_in_out = psutil.net_io_counters(pernic=True)
    data = []
    for iface, iface_in_out in in_out.items():
        up_speed, down_speed = other_in_out[iface].bytes_sent - iface_in_out.bytes_sent, other_in_out[iface].bytes_recv - iface_in_out.bytes_recv
        data.append({
            "iface" : iface,
            "Download" : get_size(other_in_out[iface].bytes_recv),
            "Upload" : get_size(other_in_out[iface].bytes_sent),
            "Download Speed" : f"{get_size(down_speed / update_delay)}/s",
            "Upload Speed" : f"{get_size(up_speed / update_delay)}/s"
        })
    in_out = other_in_out
    dframe = pd.DataFrame(data).sort_values("Download",ascending=False)
    os.system("cls") if "nt" in os.name else os.system("clear")
    print(dframe.to_string())