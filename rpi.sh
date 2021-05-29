#!/bin/bash
ssh pi@`for ((i=1; i<=29; i++));do arp -a 192.168.0.$i; done | grep "<pi mac address lowercase and colons>" | awk '{print $2}' | sed -e 's/(//' -e 's/)//'`
