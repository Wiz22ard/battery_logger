import json
import subprocess
import time
import csv
from datetime import datetime

last_percentage = None
while True:
    try:
        # Ambil data baterai
        r = subprocess.run(['termux-battery-status'], stdout=subprocess.PIPE)
        j = json.loads(r.stdout.decode('utf-8'))
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = j['status']
        percentage = j['percentage']
        if status == 'FULL': break

        # Simpan ke CSV
        with open('charging10.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp","temperature","voltage","current","percentage","count","status","plugged"])
            writer.writerow([
                ts,
                j.get('temperature', 'N/A'),
                j.get('voltage', 'N/A'),
                j.get('current', 'N/A'),
                percentage,
                j.get('charge_counter', 'N/A'),
                status,
                j.get('plugged', 'N/A'),
            ])

        if percentage != last_percentage:
            # Print info
            print("Timestamp:", ts)
            print("%:", percentage)
            print("Status:", status)
            print("")
            last_percentage = percentage

        time.sleep(1)

    except KeyboardInterrupt:
        print("Logging dihentikan.")
        break
    except Exception as e:
        print("Error:", e)
        time.sleep(2)
