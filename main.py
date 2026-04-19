def chunk_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

# Misol:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
print(chunk_list(input_list, chunk_size))
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. `input_list` ro'yxatiga berilgan elementlarni kiritib, `chunk_size` o'lchamini belgilang.
2. `chunk_list` funksiyasiga `input_list` va `chunk_size` o'lchamini kiritib, natijani chiqarib ko'ring.
