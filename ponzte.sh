#!/bin/bash

#Vinicius Sousa

COMMUNITY=$1
IP=$2
PON=$3
STATUS=$4
PORTA=$5

#Total de ONUs por Status
#1 = LOS
#3 = Online
#4 = DyingGasp
#6 = OffLine

#Ex: ./ponzte public seu-ip 15157841 3

snmpwalk -v2c -c $COMMUNITY "$IP:$PORTA" 1.3.6.1.4.1.3902.1012.3.28.2.1.4."$PON" | grep -v "No Such" | awk '{print $4}' | grep "$STATUS" | wc -l
