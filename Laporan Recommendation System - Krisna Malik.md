# Laporan Recommendation System - Krisna Malik

## Project Overview

Ada berbagai cara untuk melepas kepenatan, salah satunya adalah dengan menonton film atau acara yang kita sukai.
Seiring dengan berkembangnya teknologi, industri streaming juga ikut berkembang. Beberapa diantaranya mengkhususkan diri hanya menampilkan beberapa jenis tontonan. Salah satunya adalah Anime. Salah satu pertimbangan dari user untuk menentukan dimana dia akan menonton anime adalah dari segi koleksi atau kelengkapan situs tersebut.

Semakin banyak koleksi anime pada suatu situs maka kemungkinan besar banyak user yang akan mengakses situs tersebut. Namun, kendala yang akan dihadapi adalah user akan merasa kebingungan untuk mulai menonton karena terlalu banyak pilihan. Untuk mengatasi kendala tersebut, diperlukan sebuah sistem rekomendasi agar user merasa senang dan nyaman ketika menonton pada situs tersebut.


## Business Understanding

Pada sebuah situs streaming, user akan menemukan banyak anime namun belum tentu cocok dengan selera mereka. Oleh karena itu diperlukan sebuah sistem rekomendasi berdasarkan preferensi dari user

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah:
- Genre apa yang diminati user?
- Format anime seperti apa yang diminati user?
- Anime seperti apa yang disukai oleh user?

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Genre yang banyak diminati user adalah hentai, comedy dan music
- Ternyata banyak user yang lebih menyukai format anime dalam bentuk TV (ditayangkan oleh TV)
- Berdasarkan data, banyak user yang memberikan rating pada anime yang mempunyai genre Action, Fantasy. Hasil ini sangat berbeda dengan genre yang paling banyak diberikan rating oleh user.

### Solution statements
- Dari hasil analisis diatas, ada dua perbedaan yang mencolok dari rating yang diberikan oleh user untuk sebuah anime dan genre yang paling disukai. Oleh karena itu, untuk mempermudah user dalam menemukan anime yang mereka sukai diperlukan sebuah sistem rekomendasi yang dapat memberikan saran kepada user dengan tepat. Contohnya adalah dengan teknik Content-based Filtering dan Collaborative Filtering. Diharapkan dengan dua teknik tersebut user dapat merasa terbantu dalam menemukan anime yang mereka suka.

## Data Understanding
Dataset ini mempunyai dua file yaitu anime dan rating dalam bentuk csv. Isi dari file rating adalah kumpulan user_id yang sudah memberikan rating kepada sebuah anime. Pada file anime berisi deskripsi dari anime_id yang ada pada file rating. Dataset ini diperoleh dari myanimelist.net sumber dataset adalah sebagai berikut [Anime Recommendations Database - Kaggle](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database).

Variabel-variabel pada file anime adalah sebagai berikut:
- anime_id = anime id dari myanimelist.net
- name = judul anime
- genre = genre pada anime; satu anime bisa mempunyai banyak genre yang dipisahkan koma, seperti: Action,Comedy,Martial Arts,Shounen,Super Power
- type = type sebuah anime; movie, TV, OVA, etc.
- episodes = banyak episode. (1 if movie).
- rating = rata rata rating sebuah anime 1-10.
- members - member komunitas untuk anime tersebut

Variabel-variabel pada file rating adalah sebagai berikut:
- user_id = user id yang dibuat secara random.
- anime_id = anime yang telah diberikan rating.
- rating = nilai rating 1-10 (-1 jika user sudah menonton tapi tidak memberikan rating).


## Data Preparation

1. Langkah pertama yang dilakukan adalah melihat apakah ada nilai kosong pada dataset anime
2. Lalu melihat genre apa saja yang ada pada dataset tersebut, ternyata genre yang ditampilkan masih banyak dan berantakan
3. Berdasarkan hasil analisis, masih ada genre yang menggunakan spasi dan juga karakter lain, misalnya '-' oleh karena itu kita harus menghilangkannya
4. Selanjutnya adalah melihat dibaris mana saja yang mempunyai nilai null, terdapat 3 kolom yang masih mempunyai data kosong, yaitu rating, genre dan type
5. Untuk type dan genre, data yang kosong akan kita isi dengan unknown sedangkan untuk kolom rating data kosong akan kita isi dengan 0
6. Setelah data anime sudah bersih, kita akan membuat dataset baru dengan menggabungkan data anime dan rating dengan parameter 'anime_id' sehingga nanti dapat dilihat setiap user pada dataset rating memberikan rating pada aniem apa
7. Selanjutnya kita bersihkan kembali data anime_rating yang merupakan gabungan antara data anime dan rating dengan menghapus baris yang mempunyai nilai null
8. Untuk pemrosesan Content-based Filtering kita akan menghapus duplikasi yang ada pada data anime dan membuat vektor untuk setiap genre
9. Selanjutnya kita akan melihat nilai korelasi antara judul anime dan genrenya
10. Lalu kita akan menghitung cosine similarity untuk dijadikan dasar dalam Content-based Filtering dan kita lakukan pengujian apakah sudah berhasil memberikan rekomendasi yang sesuai atau belum
11. Untuk melakukan Collaborative Filtering kita memerlukan dataset rating
12. Langkah pertama adalah melakukan encoding kolom yang dibutuhkan, dalam proyek ini adalah kolom anime id dan user id
13. Setelah dilakukan encoding, kita akan menambahkan kolom hasil encoding kedalam dataset rating kita yang sebelumnya
14. Untuk mendapatkan data training dan validasi, kita perlu melakukan pengacakan pada dataset yang sudah kita buat sebelumnya lalu kita bagi menjadi 80% dan 20%
15. Model kita akan menerapkan 4 layer embedding yaitu user embedding, anime embedding, user bias dan anime bias
16. 

## Modeling

Pada proyek ini digunakan dua sistem rekomendasi, yaitu:
1. Collaborative Filtering
2. Content-based Filtering

## Collaborative Filtering
Sistem rekomendasi 
## Content-based Filtering
Sistem rekomendasi menggunakan Content-based Filtering akan sangat berguna jika dapat diaplikasikan untuk memberi rekomendasi saat user memilih atau sedang mencari sebuah anime. Karena konsep dasar dari sistem rekomendasi ini adalah melihat hubungan atau kedekatan setiap 'genre' sehingga user dapat melihat dan menentukan judul anime apa yang mirip dengan anime yang sedang dia cari atau yang dia pilih. Berikut adalah contoh hasil dari Content-based Filtering jika user mencari atau memilih anime dengan judul 'Naruto' dan genre dari Naruto adalah Action,Comedy,MartialArts,Shounen,SuperPower :
| | name| genre  
|-|-----|-----|
|1|	Naruto Soyokazeden Movie: Naruto to Mashin to ...	| Action,Comedy,MartialArts,Shounen,SuperPower |
|2|	Boruto: Naruto the Movie	| Action,Comedy,MartialArts,Shounen,SuperPower |
|3|	Naruto x UT	| Action,Comedy,MartialArts,Shounen,SuperPower |
|4|	Naruto: Shippuuden Movie 4 - The Lost Tower |	Action,Comedy,MartialArts,Shounen,SuperPower |
|5|	Naruto: Shippuuden Movie 3 - Hi no Ishi wo Tsu...	| Action,Comedy,MartialArts,Shounen,SuperPower |

Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

