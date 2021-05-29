#!/bin/bash
ssh pi@`for ((i=1; i<=29; i++));do arp -a 192.168.1.$i; done | grep <mac address of your pi> | awk '{print $2}' | sed -e 's/(//' -e 's/)//'`
