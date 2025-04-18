import sys

def decrypt(encryption: str) -> str:
    stack = []
    i = 0
    n = len(encryption)
    while i < n:
        if encryption[i] == '.':
            if i + 1 < n and encryption[i + 1] == '.':
                # Две точки - удаляем предыдущий символ
                if stack:
                    stack.pop()
                i += 2  # Пропускаем обе точки
            else:
                # Одна точка - просто пропускаем
                i += 1
        else:
            stack.append(encryption[i])
            i += 1
    return ''.join(stack)

if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decrypt(data)
    print(decryption, end='')