class HashTableLinearProbing:
    def __init__(self, size):
        # Menentukan ukuran tabel hash yang lebih besar dari jumlah item (aman)
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Fungsi hash menggunakan modulo
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        
        # Proses Linear Probing jika terjadi tabrakan (Collision)
        while self.table[index] is not None:
            print(f"--> Tabrakan (Collision) di indeks {index} untuk key {key}.")
            print("--> Mencari sel kosong secara linier (Linear Probing)...")
            index = (index + 1) % self.size
            
            if index == original_index:
                print("Tabel Hash sudah penuh!")
                return
                
        self.table[index] = key
        print(f"Sukses memasukkan {key} ke indeks {index}\n")

    def display(self):
        print("-" * 25)
        print("Kondisi Akhir Tabel Hash:")
        print("-" * 25)
        for i in range(self.size):
            print(f"Indeks {i} : {self.table[i]}")


if __name__ == "__main__":
    print("IMPLEMENTASI HASHING DENGAN LINEAR PROBING")
    print("=" * 45)
    
    # Membuat tabel hash dengan ukuran 10
    ht = HashTableLinearProbing(10)
    
    # Memasukkan elemen tanpa tabrakan
    ht.insert(157)  # 157 % 10 = 7
    ht.insert(2001) # 2001 % 10 = 1
    ht.insert(13)   # 13 % 10 = 3
    
    # Memasukkan elemen 207 yang akan menghasilkan tabrakan dengan 157
    ht.insert(207)  # 207 % 10 = 7 (akan masuk ke linear probing)
    
    ht.display() 