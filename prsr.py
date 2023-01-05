import requests
import json


cpu_url = "https://grafana.mirohost.net/api/datasources/proxy/7/render?target=aliasByTags(nPercentile(scale(perSecond(seriesByTag('host%3D~smart*'%2C%20'name%3DCPU.Total.Usage.Total'))%2C%201e-7)%2C%2095)%2C%20'host')&from=-7d&until=now&format=json&maxDataPoints=10100"
cpu_resp = requests.get(cpu_url)
cpu_data = json.loads(cpu_resp.text)

mem_url = "https://grafana.mirohost.net/api/datasources/proxy/7/render?target=aliasByTags(nPercentile(seriesByTag('host%3D~smart*'%2C%20'name%3DMemory.Usage')%2C%2095)%2C%20'host')&from=-7d&until=now&format=json&maxDataPoints=1500"
mem_resp = requests.get(mem_url)
mem_data = json.loads(mem_resp.text)

disk_url = "https://grafana.mirohost.net/api/datasources/proxy/7/render?target=aliasByTags(seriesByTag('host%3D~smart*'%2C%20'name%3DDisk.Root.Usage')%2C%20'host')&from=-7d&until=now&format=json&maxDataPoints=1500"
disk_resp = requests.get(disk_url)
disk_data = json.loads(disk_resp.text)
