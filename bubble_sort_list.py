def bubble_sort_descending(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

# Daftar angka yang ingin diurutkan
angka = [42, 19, 33, 8, 55]

# Memanggil fungsi bubble_sort_descending dan mencetak hasilnya
hasil = bubble_sort_descending(angka)
print(hasil)