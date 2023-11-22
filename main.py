import json
d=[]
with open('/home/ericgr3gory/dns_query_logs.json', 'r') as dns_log:
    dns = dns_log.read()
sites = []
dns = dns.split('\n')
for line in dns:
    j = json.loads(line)
    sites.append(j)

www_list = []
for line in sites:

    if "2023-11-21" in line['time_iso'] and "www" in line["domain"]:
        www_list.append(line["domain"])


www_list = list(set(www_list))

for www in www_list:
    print(www)
