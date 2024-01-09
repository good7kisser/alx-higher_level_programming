#!/usr/bin/python3
import sys

def print_stats():
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    status_count = {code: 0 for code in status_codes}
    total_size = 0
    line_count = 0

    try:
        for i, line in enumerate(sys.stdin, 1):
            split_line = line.split()
            if len(split_line) > 2:
                status_code = int(split_line[-2])
                file_size = int(split_line[-1])
                if status_code in status_codes:
                    status_count[status_code] += 1
                total_size += file_size
                line_count += 1
            if i % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_codes):
                    if status_count[code]:
                        print(f"{code}: {status_count[code]}")
    except KeyboardInterrupt:
        pass

    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_count[code]:
            print(f"{code}: {status_count[code]}")
