# Monitoramento-ZTE-C3X
Monitoramento com intuito de monitorar OLT ZTE C3X


# Documentado por: Vinicius Sousa
# Baseado em scrits de coletas
# Data: 06/04/2025 - 22:08

# Atribua os macros no seu Zabbix
{$SNMP_COMMUNITY} -> Community-OLT (Verifique a community da sua OLT).
{$SNMP_PORTA} -> Porta-SNMP (Porta atribuida no snmp).

# Os scripts podem ser criados no seu server ou você pode clonar o diretorio e subir no server.
/usr/lib/zabbix/externalscripts/discoveryponc3x
/usr/lib/zabbix/externalscripts/discoveryc3x
/usr/lib/zabbix/externalscripts/ponzte


# Caso copiei, renomei os scripts removendo a extensão:
mv discoveryc3x.py discoveryc3x
mv discoveryponc3x.py discoveryponc3x
mv ponzte.py ponzte

# De permissão de execução:
chmod +x discoveryc3x
chmod +x discoveryponc3x
chmod +x ponzte

# Consulta direto no Banco do Zabbix (Acesse o banco de dados e crie um usuário de leitura para poder utilizar pelo Grafana:
mysql -u root -p

mysql> create user grafanazte@localhost identified by 'COLOQUE-UMA-SENHA-BOA-PRA-USAR-NO-GRAFANA';
mysql> grant SELECT on zabbix.* to grafanazte@localhost;
mysql> quit

# Após criar o usuário, vai até o Grafana, e crie um nova datasource do Mysql, informando as credenciais de database do Zabbix, e usuário e senha criadas no passo anterior.
