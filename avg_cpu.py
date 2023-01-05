from prsr import cpu_data, mem_data, disk_data
import csv


smart_info = {}

for i in mem_data:
    if "kidstaff" not in i["target"] and "smartultralite43" not in i["target"] \
        and "smartsupralite5.mirohost.net" not in i["target"] and "smart105" not in i["target"]:
        smart_info[i["target"]] = {}

for i in cpu_data:
    if "kidstaff" not in i["target"] and "smartultralite43" not in i["target"] \
        and "smartsupralite5.mirohost.net" not in i["target"] and "smart105" not in i["target"]:
        smart_info[i["target"]] = {}

for i in disk_data:
    if "kidstaff" not in i["target"] and "smartultralite43" not in i["target"] \
        and "smartsupralite5.mirohost.net" not in i["target"] and "smart105" not in i["target"]:
        smart_info[i["target"]] = {}


for i in cpu_data:
    if "kidstaff" not in i["target"] and "smartultralite43" not in i["target"] \
        and "smartsupralite5.mirohost.net" not in i["target"] and "smart105" not in i["target"]:
        try:
            smart_info[i["target"]]["cpu"] = round(sum(num[0] for num in i["datapoints"][:-1]) / len(i["datapoints"]), 2)
        except TypeError:
            continue

for i in mem_data:
    if "kidstaff" not in i["target"] and "smartultralite43" not in i["target"] \
        and "smartsupralite5.mirohost.net" not in i["target"] and "smart105" not in i["target"]:
        try:
            smart_info[i["target"]]["memory"] = round(float(i["datapoints"][-1][0] / (10 ** 9)), 2)
        except TypeError:
            continue

for i in disk_data:
    if "kidstaff" not in i["target"] and "smartultralite43" not in i["target"] \
        and "smartsupralite5.mirohost.net" not in i["target"] and "smart105" not in i["target"]:
        try:
            smart_info[i["target"]]["disk"] = round(float(i["datapoints"][-1][0] / (10 ** 9)), 2)
        except TypeError:
            continue

# print(smart_info)
servers = [[], [], [], [], []]
smarts = [[], [], [], [], []]

avg_mem = [[], [], [], [], []]
avg_cpu = [[], [], [], [], []]
avg_disk = [[], [], [], [], []]

for i in smart_info:
    if len(smart_info[i]) != 3:
        print(i, smart_info[i])

d_usage = []
c_usage = []
m_usage = []

for smart in smart_info:
    d_usage.append([smart_info[smart]["disk"], smart])
    c_usage.append([smart_info[smart]["cpu"], smart])
    m_usage.append([smart_info[smart]["memory"], smart])

d_usage.sort()
c_usage.sort()
m_usage.sort()

while len(d_usage) > 0 or len(c_usage) > 0 or len(m_usage) > 0:
    try:
        for _ in range(5):
            servers[_].append(m_usage[-1])
            smarts[_].append(m_usage[-1][1])
            avg_mem[_].append(m_usage[-1][0])
            avg_mem.reverse()
            smarts.reverse()
            m_usage.remove(m_usage[-1])
            servers.reverse()
            servers[_].append(c_usage[-1])
            smarts[_].append(c_usage[-1][1])
            avg_cpu[_].append(c_usage[-1][0])
            avg_cpu.reverse()
            smarts.reverse()
            c_usage.remove(c_usage[-1])
            servers.reverse()
            servers[_].append(d_usage[-1])
            smarts[_].append(d_usage[-1][1])
            avg_disk[_].append(d_usage[-1][0])
            avg_disk.reverse()
            smarts.reverse()
            d_usage.remove(d_usage[-1])
            servers.reverse()
    except IndexError as e:
        print(e)
        break

print("Overall:")
for s in range(5):
    print(sum(i[0] for i in servers[s]) / len(servers[s]))

print()
print("Average memory:")
for i in range(5):
    print(sum(avg_mem[i]) / len(avg_mem[i]))

print()
print("Average cpu:")
for i in range(5):
    print(sum(avg_cpu[i]) / len(avg_cpu[i]))

print()
print("Average disk:")
for i in range(5):
    print(sum(avg_disk[i]) / len(avg_disk[i]))

# for i in range(5):
#     with open(f"Smart{i}.csv", "w+", newline="") as f:
#         writer = csv.writer(f, delimiter=",", lineterminator="\n")

#         writer.writerow(smarts[i])
