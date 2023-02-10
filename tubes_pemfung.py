
#* FINAL
import streamlit as st

st.title('KELOMPOK 10 ')
st.subheader('Anggota Kelompok : ')
st.subheader('1. Andika Purnama Putra (21102141)')
st.subheader('2. Maria Pasya Saragih (21102136) ')
st.subheader('3. M.Reyhan Asshidiq Djajasasmita (21102126)')
st.subheader('4. Rodi Cahyawan (21102256)')
st.subheader('5. Suryani Dewi Wulandari (21102119)')
st.write("")
st.write("")

st.write("Iterator Tools adalah sekumpulan modul built-in di Python yang memungkinkan Anda untuk dapat membuat dan mengolah iterator.Iterator itu sendiri merupakan objek yang membuat kita dapat mengakses elemen dalam urutan.")
st.write("Macam-macam Iterator Tools pada Python :")
st.subheader("Infinite Iterators : ")
st.write("- count()")
st.write("- cycle()")
st.write("- repeat()")
st.subheader("Finite Iterators : ")
st.write("- accumulate()")
st.write("- chain()")
st.write("- compress()")
st.write("- combinations()")
st.write("- permutations()")
st.write("- groupby()")

st.subheader("Studi Kasus Penerapan Itertools Python ")
#! count()
st.subheader("1. COUNT")
st.write("count() adalah fungsi bawaan Python yang digunakan untuk mengembalikan umlah total elemen yang diberikan dalam sebuah string. Dimungkinkan juga untuk menentukan indeks awal dan akhir dari tempat Anda ingin memulai pencarian.")
kode_count = '''nama_mahasiswa = [
"Ahmad Tri Fathoni", "Ahmad Faitsal Hanif", "Amanda Dzunuri Elvira",
"Amanda Manopo", "Salsabilla Amanda", "Bilalos Tenggoro Angin",
"Dimas febriyanto", "Dimas Danur Dhowo Danisworo", "Satria Dimas Madeswara",
"Elang Laras Yoga", "Yoga Galih Prasojo", "Gayuh Hening Sanyuri",
"Ghilda Amalia Karimah", "Amalia Tri Rahayu", "Gina Silvi Muharina"
]

jumlah_nama_ahmad = 0
jumlah_nama_dimas = 0


for nama in nama_mahasiswa:
    if nama.count("Ahmad") > 0: 
        jumlah_nama_ahmad += 1
    if nama.count("Dimas") > 0:
        jumlah_nama_dimas+= 1

print("Jumlah Nama Ahmad :", jumlah_nama_ahmad)
print("Jumlah Nama Dimas :", jumlah_nama_dimas) '''
st.code(kode_count, language='python')
st.write("Kode ini membuat sebuah daftar nama_mahasiswa yang berisi nama-nama mahasiswa. Kemudian, kode ini menginisialisasi dua variabel, jumlah_nama_ahmad dan jumlah_nama_dimas, untuk mencatat jumlah nama dalam daftar yang berisi string ahmad & dimas. Kemudian gunakan perulangan for untuk mengiterasi.")

st.text("Output Program :")

output_count = '''Jumlah Nama Ahmad : 2
Jumlah Nama Dimas : 3 '''
st.code(output_count, language='python')



#! cycle()
st.subheader("2. CYCLE")
st.write("fungsi cycle() pada python digunakan untuk mengulangi sebuah iterable (seperti list, tuple, atau string) tanpa batas. Fungsi ini membuat objek iterable yang berulang-ulang tanpa henti. Setiap iterasi selesai, iterasi berikutnya akan dimulai dari awal, berguna jika ingin mengulangi sebuah sequence elemen.")
kode_cycle = ''' import itertools
from itertools import cycle 
iter_cycle = cycle(['a', 'd', 'j'])

for i in range(8):
    print(next(iter_cycle)) '''
st.code(kode_cycle, language='python')
st.write("iterable yang diberikan sebagai argument adalah list ['a', 'd', 'j']. Kemudian dilakukan perulangan 'for' sebanyak 8 kali untuk mengakses item. Sehingga akan menghasilkan output berikut :")


st.text("Output Program :")
output_cycle = '''a
d
j
a
d
j
a
d'''
st.code(output_cycle, language='python')

#! repeat()
st.subheader("3. REPEAT")
st.write("")
kode_repeat = ''' import itertools
from collections import Counter

data = ['Pemfung', 'Anum', 'Jarkom', 'Komas', 'Pemfung', 'Basdat', 'Komas', 'Pemfung', 'Jarkom', 'Pemfung', 'Basdat', 'Komas', 'Pemfung']

# Menghitung jumlah muncul setiap elemen/matkul dalam list
count = Counter(data)

# Mencari elemen/matkul dalam list yang muncul paling banyak
result = max(count, key=count.get)

# Menggunakan itertools.repeat() untuk membuat list baru yang berisi elemen/matkul yang muncul paling banyak
new_data = list(itertools.repeat(result, count[result]))

# Mencetak hasil
print("Matkul yang paling sering muncul:", result)
print("Data baru:", new_data) '''
st.code(kode_repeat,language='python')
st.write("Program di atas digunakan untuk mencari elemen yang paling sering muncul dalam sebuah list data. Variable 'count' diatas didefinisikan untuk menghitung jumlah disetiap elemen dalam list data. Program menggunakan fungsi 'max' dan key function 'count.get' untuk mencari elemen dalam list yang muncul paling banyak. Kemudian Fungsi 'max' akan membandingkan elemen dalam list menggunakan key function yang ditentukan, dan akan mengembalikan elemen yang memiliki nilai tertinggi. Dan mencetak hasil dari matkul yang paling banyak muncul, dan data baru dari matkul yang paling banyak muncul")

st.text("Output Program :")
output_repeat = '''Matkul yang paling sering muncul: Pemfung
Data baru: ['Pemfung', 'Pemfung', 'Pemfung', 'Pemfung', 'Pemfung']'''
st.code(output_repeat, language='python')

#! accumulate()
st.subheader("4. ACCUMULATE")
st.write("Fungsi accumulate() pada python digunakan untuk menghitung acuan atau akumulasi dari sekumpulan elemen, ini membuat objek iterable yang berisi acuan dari elemen iterable ditentukan. Misalnya, jika ingin memiliki sebuah daftar angka dan ingin menghitung acuan dari angka-angka, kita dapat menggunakan fungsi accumulate() (1, 2, 3, 4, 5), ini akan menghasilkan objek iterable dengan isi [1, 2, 3, 4, 5] dimana setiap elemen adalah acuan dari elemen sebelumnya.")
kode_accumulate = '''import itertools
# pada variabel hasil menyimpan rumus, yaitu akan mengalikan tiap elemen pada list 'data' secara berurutan
data = [2, 4, 3, 3, 2, 0]
hasil = itertools.accumulate(data, lambda a, b: a*b)
print(list(hasil))'''
st.code(kode_accumulate, language='python')

st.write("Program fungsi 'accumulate' ini membutuhkan dua argumen yakni iterable dan fungsi acuan. Fungsi acuan yakni 'lamdda a, b: a*b' fungsinya untuk mengembalikan sebuah nilai. ")
st.text("Output Program :")
output_accumulate = '''[2, 8, 24, 72, 144, 0]'''
st.code(output_accumulate, language='python')


#! chain()
st.subheader("5. CHAIN")
st.write("Fungsi chain() pada python digunakan untuk menggabungkan beberapa iterable menjadi satu iterable baru. Fungsi chain() membaca elemen-elemen dari setiap iterable secara berurutan dan menggabungkannya menjadi satu iterable baru. Jika kita ingin mengiterasi beberapa objek seperti list, tuple, atau string seolah-olah mereka adalah satu objek tunggal.")
kode_chain = '''import itertools

from itertools import chain

a = [1, 9, 4, 6, 2]

b = ['f', 'u', 'n', 'g', 's', 'i']

data = list(chain(a,b))

print(data)'''
st.code(kode_chain, language='python')
st.write("Fungsi 'chain' membutuhkan satu atau lebih iterable sebagai argumennya, dan mengembalikan sebuah iterator yang menggabungkan elemen dari semua iterable tersebut secara berurutan")

st.text("Output Program :")
output_chain = '''[1, 9, 4, 6, 2, 'f', 'u', 'n', 'g', 's', 'i']'''
st.code(output_chain, language='python')
#! compress()
st.subheader("6. COMPRESS")
st.write("Fungsi compress() pada python digunakan untuk mengiterasi elemen dari suatu iterable berdasarkan suatu kondisi. Fungsi compress() menerima dua argumen : suatu iterable dan suatu iterable boolean. Iterable Boolean ini digunakan sebagai filter dan menentukan apakah elemen dari iterable pertama harus diambil atau tidak. ")
kode_compress = '''import itertools

x = ['K','E','L', 'E', 'O', 'R', 'P', 'O', 'N', 10]
y = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1]
for i in itertools.compress(x, y) :
    print(i)'''
st.code(kode_compress, language='python')
st.write("Dalam sintaks di atas, fungsi compress dalam module itertools digunakan untuk mengambil elemen dari iterable x berdasarkan filter dalam iterable y. Iterable 'y' berisi boolean values yang menentukan apakah elemen dalam iterable 'x' harus diambil atau tidak. Jika nilai boolean pada posisi yang sama dalam iterable 'y' bernilai TRUE, maka elemen pada posisi yang sama dalam iterable 'x' diambil dan dicetak.")
st.text("Output Program :")
output_compress = '''K
L
E
P
O
N
10'''
st.code(output_compress, language='python')

#! combinations()
st.subheader("7. COMBINATIONS")
st.write("Fungsi combinations() digunakan untuk menghasilkan sebuah generator yang menyimpan kombinasi item dari sebuah koleksi iterable dengan panjang tertentu (r). Dalam hal ini, 'r' adalah parameter kedua yang diberikan ke fungsi combinations(). Fungsi ini sangat berguna ketika kita ingin menghitung semua kemungkinan kombinasi dari item dalam koleksi tertentu.")
kode_combinations = ''' import itertools

from itertools import combinations

data = [2, 6, 7, 4, 9, 12,]

data_kombinasi = combinations(data, r=2)

for index, data in enumerate(list(data_kombinasi), 1):
    print(f'kombinasi ke : {index}.{data}') '''
st.code(kode_combinations, language='python')

st.text("Output Program :")
output_combinations = '''Kombinasi ke : 1. (2, 6)
Kombinasi ke : 2. (2, 7)
Kombinasi ke : 3. (2, 4)
Kombinasi ke : 4. (6, 7)
Kombinasi ke : 5. (6, 4)
Kombinasi ke : 6. (7, 4)'''
st.code(output_combinations, language='python')

#! permutations()
st.subheader("8. PERMUTATIONS")
st.write("Fungsi permutations() adalah fungsi dalam module 'itertools' di Python yang membuat iterator yang mengandung semua permutasi unik dari iterable yang diberikan sebagai argumen.")
kode_permutations = ''' from itertools import permutations
 
data_list = [2, 4, 1]
 
data_permutasi = permutations(data_list)
 
for index, data in enumerate(list(data_permutasi), 1):
    print(f'Hasil Nomor: {index}. {data}') '''
st.code(kode_permutations, language='python')
st.write("dari contoh kasus diatas terdapat 10 permutasi bedasarkan data yang kita input dalam variabel data_list. Pertama, kita import fungsi permutation() dari modul itertools. Kemudian kita definisikan list yang akan kita hitung permutasinya. Dari kode di atas, variabel 'permutasi' akan berisi object dari 'permutations(data_list)'.")

st.text("Output Program :")
output_permutations = '''Hasil Nomor : 1. (2, 4, 1)
Hasil Nomor : 2. (2, 1, 4)
Hasil Nomor : 3. (4, 2, 1)
Hasil Nomor : 4. (4, 1, 2)
Hasil Nomor : 5. (1, 2, 4)
Hasil Nomor : 6. (1, 4, 2)'''
st.code(output_permutations, language='python')

#! groupby()
st.subheader("9. GROUPBY")
st.write("Fungsi groupby() pada Python digunakan untuk memgroupkan item-item dalam sebuah iterable berdasarkan nilai yang dikembalikan oleh sebuah fungsi array. Item-item yang memiliki nilai key yang sama akan dikelompokan bersama. Fungsi ini sangat berguna ketika kita ingin mengelompokkan angka ganjil dan genap.")

kode_groupby = ''' import itertools
  
mahasiswa = [("MK1", "Reyhan"),              
             ("MK1", "Wulan"),              
             ("MK2", "Rodi"),              
             ("MK2", "Maria"),
             ("MK2", "Andika"),]
  
group_by_mk = itertools.groupby(mahasiswa, lambda x : x[0])
  
for mk, group in group_by_mk:
    nama_mahasiswa = {mk : [nama for _, nama in group]}
    print(nama_mahasiswa) '''
    
st.code(kode_groupby, language='python')

st.text("Output Program")
output_groupby = ''' {'MK1' : ['Reyhan', 'Wulan']}
{'MK2' : ['Rodi', 'Maria', 'Andika']} '''
st.code(output_groupby, language='python')
