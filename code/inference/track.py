# track.py
import csv

def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["frame", "x", "y", "visible"])
        writer.writerows(rows)
