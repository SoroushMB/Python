import psutil
import time

update_delay = 1

def get_size(bytes):
    for unit in [' ', 'K' , 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

in_out = psutil.net_io_counters()
bytes_sent, bytes_recv = in_out.bytes_sent, in_out.bytes_recv


while True:
    time.sleep(update_delay)
    other_in_out = psutil.net_io_counters()
    up_speed, down_speed = other_in_out.bytes_sent - bytes_sent ,other_in_out.bytes_recv - bytes_recv
    print(f"Upload: {get_size(other_in_out.bytes_sent)}\nDownload: {get_size(other_in_out.bytes_recv)}\nUpload Speed: {get_size(up_speed/update_delay)}\nDownload Speed: {get_size(down_speed/update_delay)}")
    bytes_sent, bytes_recv = other_in_out.bytes_sent, other_in_out.bytes_recv