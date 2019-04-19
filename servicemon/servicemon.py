#!/usr/bin/env python3
# -*- coding: utf-8 :

import argparse
import datetime
import json
import os
import subprocess
import sys
import time

# Third party imports:

import psutil

# CONSTANTS:

CONFIG = '/etc/fanatique/servicemon.json'
DEBUG_TRACE = True
MEMORY_TYPES_BYTES = ['vms', 'rss', 'swap'] # Types of memory to be monitored.
MEMORY_TYPES_PERCENT = ['rss', 'swap']
ATOP_LOGFILE = '/tmp/servicemon.tmp' # Temporary file to save the atop history to.
ATOP_SAMPLES = 2 # Number of samples to get from atop history.

# Code:

def get_args():
    """Get arguments and set configuration"""

    try:
        parser = argparse.ArgumentParser(description="systemd: Service monitoring script")
        parser.add_argument("-c",
                            "--config",
                            help="Configuration file of the script.",
                            default=CONFIG,
                            type=str)
        return parser.parse_args()

    except argparse.ArgumentError:
        print("Error: Internal argument parsing error occured.", file=sys.stderr)
        sys.exit(1)

def setup():
    time_now   = datetime.datetime.now()
    time_delta = time_now - datetime.timedelta(minutes=ATOP_SAMPLES-1)
    time_begin = '{}:{}'.format(time_delta.hour, time_delta.minute)
    time_end   = '{}:{}'.format(time_now.hour, time_now.minute)

    exit_code = subprocess.call("/usr/bin/atop -P PRC,PRM,PRD -b {} -e {} -r > {}".format(
        time_begin,
        time_end,
        ATOP_LOGFILE))
    

def main():
    arguments = get_args()
    