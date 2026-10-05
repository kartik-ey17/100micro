filename = input("Enter file name : ")

try:
    with open(filename , "r") as file:
        raw_lines = file.readlines()
except FileNotFoundError:
    print(f"File - {filename} , not found.")
    exit()

counts = {"INFO": 0 , "WARNING": 0 , "ERROR": 0}
log = []
errors = []
bad_count = 0
valid_lvls = {"INFO" , "WARNING" , "ERROR"}

for line in raw_lines:
    clean_line = line.strip()
    if not clean_line:
        continue
    parts = clean_line.split(" " , 3) 

    if len(parts) < 4 or parts[2] not in valid_lvls:
        bad_count += 1
        continue

    date , time_str , level , message = parts
    counts[level] += 1
    log.append({"date" : date , "time": time_str , "level": level , "message": message})

    if level == "ERROR":
        errors.append(message)

total_entry = len(log)

print("+=+=+= Log Analyzer =+=+=+\n")
print(f"File - {filename}\nTotal entries parsed: {total_entry}\n")

if bad_count > 0:
    print(f"Ignored bad lines = {bad_count}\n")
print("Log levels: \n")
for lvl , count in counts.items():
    print(f"{lvl + ':':<10} {count}")

if total_entry > 0:
    error_rate = (counts["ERROR"]/total_entry)*100
    print(f"Error rate: {error_rate}\n")

print("Errors : \n")
if errors:
    for err in errors:
        print(f" - {err}")
else:
    print("None")

search = input("Search logs (leave blank to skip) : ").strip()
if search:
    print(f"\nMatching logs for {search} : ")
    match = [l for l in log if search.lower() in l['message'].lower()]
    for entry in match:
        print(f"{entry['date']} {entry['time']} {entry['level']} {entry['message']}")
    if not match:
        print("No match")