import json
import subprocess
import time
import csv
from datetime import datetime

while True:
    try:
        # Ambil data baterai
        r = subprocess.run(['termux-battery-status'], stdout=subprocess.PIPE)
        j = json.loads(r.stdout.decode('utf-8'))
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Simpan ke CSV
        with open('battery_log.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                ts,
                j.get('temperature', 'N/A'),
                j.get('voltage', 'N/A'),
                j.get('current', 'N/A'),
                j.get('percentage', 'N/A'),
                j.get('charge_counter', 'N/A'),
                j.get('status', 'N/A'),
                j.get('plugged', 'N/A'),
            ])

        # Print info
        print("Timestamp:", ts)
        print("Temp:", j.get('temperature'))
        print("Volt:", j.get('voltage'))
        print("Amp:", j.get('current'))
        print("%:", j.get('percentage'))
        print("Count:", j.get('charge_counter'))
        print("Pluged:", j.get('plugged'))
        print("Status:", j.get('status'))
        print("")
        time.sleep(1)

    except KeyboardInterrupt:
        print("Logging dihentikan.")
        break
    except Exception as e:
        print("Error:", e)
        time.sleep(2)
