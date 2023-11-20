import json
d=[]
with open('/home/ericgr3gory/dns_query_logs.json', 'r') as dns_log:
    dns = dns_log.read()
safe_sites = ["google", "bing", "tiktok", "roblox", "adguard-dns.com", "microsoft", "epicgames", "spotify"]
sites = []
dns = dns.split('\n')
for line in dns:
    j = json.loads(line)
    sites.append(j['domain'])

site_set = set(sites)

print(f'list = {len(sites)}')
print(f'set = {len(site_set)}')

site_list = list(site_set)
www_list = []
for l in site_list:
    if "www" in l:
        www_list.append(l)
        print(l)

print(len(www_list))

for line in dns:
    j = json.loads(line)
    print((j['time_iso']))