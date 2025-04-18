import sys
# 2fz pflfxf
def get_mean_size(lines):
    total_size = 0
    file_count = 0

    for line in lines[1:]:  # Игнорируем первую стр
        parts = line.split()
        if len(parts) > 8:  # Проверяем, что стр полн и содерж нужн данн
            try:
                size = int(parts[4])  # Размер файла в байтах
                total_size += size
                file_count += 1
            except ValueError:
                continue  # Игнорируем строки некорректные
#Проверка на 0
    if file_count == 0:
        return "No files found or sizes could not be retrieved."#Не найден файл

    mean_size = total_size / file_count
    return f"Average file size: {mean_size:.2f} bytes"#Средний размер файла в байтах

if __name__ == '__main__':
    # Читаемданные из ввода
    lines = sys.stdin.readlines()
    result = get_mean_size(lines)
    print(result)