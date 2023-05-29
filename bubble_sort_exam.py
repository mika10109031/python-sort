def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar nilai ujian siswa
nilai_siswa = [78, 65, 90, 82, 70]

# Memanggil fungsi bubble_sort untuk mengurutkan nilai siswa
bubble_sort(nilai_siswa)

# Menampilkan daftar nilai siswa yang sudah diurutkan
print("Daftar nilai ujian siswa yang sudah diurutkan secara ascending:")
print(nilai_siswa)