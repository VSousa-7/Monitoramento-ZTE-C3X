#!/bin/python3

# Desenvolvido por: Vinicius Sousa

import subprocess
import json
import argparse

try:

    def run_snmpwalk(ip, community, oid_base, filter_command=None):
        command = f"snmpwalk -v2c -c {community} {ip}:{porta} {oid_base} | grep -E 'gpon|OLT'"

        if filter_command:
            command += f" | {filter_command}"

        output = subprocess.check_output(command, shell=True, text=True)
        lines = output.strip().split('\n')
        results = []

        for line in lines:
            if "=" not in line:
                continue
            oid, value = line.split(" = ", 1)
            oid = oid.strip()
            value = value.split(": ")[1].strip().strip('"')
            results.append((oid, value))

        return results


    # Configurar argumentos de linha de comando
    parser = argparse.ArgumentParser(description='Script para consultar dados SNMP.')
    parser.add_argument('ip', help='Endereço IP do dispositivo SNMP')
    parser.add_argument('community', help='Comunidade SNMP')
    parser.add_argument('porta', help='Porta SNMP')
    args = parser.parse_args()

    # Configurações da consulta SNMP
    ip = args.ip  # IP do dispositivo SNMP
    community = args.community  # Comunidade SNMP
    porta = args.porta # Porta SNMP
    oid_base1 = '1.3.6.1.2.1.31.1.1.1.1'  # Primeiro OID base
    oid_base2 = '1.3.6.1.4.1.3902.1012.3.13.1.1.1'  # Segundo OID base

    # Filtro para a segunda consulta
    filter_command2 = None

    # Realizar consulta SNMP walk para o primeiro OID base
    consulta_resultado1 = run_snmpwalk(ip, community, oid_base1)

    # Realizar consulta SNMP walk para o segundo OID base
    consulta_resultado2 = run_snmpwalk(ip, community, oid_base2)

    # Extrair o ifindex da segunda consulta
    ifindex_list2 = [int(item[0].split('.')[-1]) for item in consulta_resultado2]

    # Criar lista com ifindex da segunda consulta e valores da primeira consulta
    nova_lista = [
        {"{#ID}": str(ifindex), "{#INTERFACE}": value}
        for ifindex, (_, value) in zip(ifindex_list2, consulta_resultado1)
    ]

    # Converter para JSON
    json_output = json.dumps(nova_lista, indent=4)

    # Imprimir a saída JSON
    print(json_output)
except:
    print('-> Erro ao consultar snmp!')
