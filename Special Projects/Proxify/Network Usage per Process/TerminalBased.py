from scapy.all import *
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd

all_mac_addresses = {iface.mac for iface in ifaces.values()}
connection2pid = {}
pid2traffic = defaultdict(lambda:[0,0])
global_dframe = None
is_program_running = True