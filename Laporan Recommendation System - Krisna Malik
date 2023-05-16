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

1. Langkah pertama yang dilakukan adalah melihat apakah ada nilai kosong pada dataset kita

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
