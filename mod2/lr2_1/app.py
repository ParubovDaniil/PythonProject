import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RSS_FILE = os.path.join(BASE_DIR, 'output_file.txt')

def get_summary_rss() -> str:
    with open(RSS_FILE, 'r') as f:
        lines = f.readlines()[1:]
        rss_sum = sum(int(line.split()[5]) for line in lines)
        suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']
        index = 0
        while rss_sum >= 1024 and index < len(suffixes) - 1:
            rss_sum /= 1024
            index += 1
        return f"Memory consumption: {rss_sum:.2f} {suffixes[index]}"

if __name__ == '__main__':
    result = get_summary_rss()
    print(result)