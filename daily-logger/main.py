import time
import csv
import subprocess
import json
import os
from datetime import datetime

last_percentage = None
current_date = None
filename = None

while True:
    try:
        # Cek tanggal
        today = datetime.now().strftime('%Y-%m-%d')
        if today != current_date:
            current_date = today
            filename = f'battery-log-{today}.csv'
            if not os.path.exists(filename):
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        "timestamp",
                        "percentage",
                        "status"
                    ])

        # Ambil data baterai
        r = subprocess.run(['termux-battery-status'], stdout=subprocess.PIPE)
        j = json.loads(r.stdout.decode('utf-8'))
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = j['status']
        percentage = j['percentage']

        # Hanya log kalau persentase berubah
        if percentage != last_percentage:
            with open(filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    ts,
                    percentage,
                    status,
                ])

            print("Timestamp:", ts)
            print("%:", percentage)
            print("Status:", status)
            print("")
            last_percentage = percentage

        # Delay
        time.sleep(60)

    except KeyboardInterrupt:
        print("Logging dihentikan.")
        break
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
