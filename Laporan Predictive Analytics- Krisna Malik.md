# Laporan Proyek Machine Learning - Krisna Malik

## Domain Proyek
Dalam bisnis transportasi harga merupakan salah satu indikator penentu dalam pengambilan keputusan oleh calon penumpang. Sedangkan dari sisi penyedia, harga merupakan alat tawar yang digunakan untuk menarik penumpang selain dari fasilitas yang disediakan.

Penetuan harga sangat krusial bagi sebuah maskapai, jika harga yang ditawarkan terlalu rendah maka akan ada kemungkinan maskapai untuk merugi karena pendapatan lebih kecil dibanding biaya operasional dan jika harga yang ditawarkan terlalu tinggi akan berpengaruh pada pembelian tiket yang berkurang.

Oleh karena itu penentuan harga yang sesuai harus dipertimbangkan dengan matang. Salah satu cara yang dapat dilakukan adalah melihat pasar dan kompetitor yang ada.

## Business Understanding
Untuk menentukan harga yang paling sesuai, kita harus melihat semua faktor yang mungkin akan berpengaruh dalam pengambilan keputusan oleh penumpang.

### Problem Statements
- Apakah akan ada pengaruh antara harga dengan durasi perjalanan? Apakah penumpang lebih menyukai durasi perjalanan yang panjang?
- Apakah kelas pesawat akan berpengaruh langsung terhadap harga?
- Apakah jumlah transit yang lebih sedikit dapat mempengaruhi penentuan harga? Bagaimana perilaku penumpang terhadap jumlah transit dalam satu perjalanan?

### Goals
- Semakin panjang durasi perjalanan akan berpengaruh pada harga yang diberikan, karena semakin jauh perjalanan dan semakin lama durasi maka akan membutuhkan lebih banyak sumber daya. Hal ini berdampak langsung pada harga yang ditetapkan menjadi lebih tinggi. Berdasarkan data yang diperoleh, banyak penumpang yang memilih durasi perjalanan yang pendek, ini mungkin saja terjadi pada perjalanan dengan jarak yang relatif dekat.
- Kelas pesawat sangat berpengaruh pada penentuan harga, lebih tinggi kelas (seperti bisnis) akan mempunyai harga yang lebih tinggi.
- Berdasarkan data yang diperoleh, penumpang banyak memilih perjalanan dengan satu kali transit dengan rerata durasi 13 jam, rerata harga yang ditawarkan pada perjalanan ini cukup tinggi. Perjalanan dengan jumlah transit lebih banyak memakan durasi sekitar 15 juga cukup diminati, harga yang ditawarkan pada perjalanan ini tidak begitu tinggi (lebih rendah dibanding perjalanan satu kali transit). Perjalanan jarak dekat atau tanpa transit memiliki peminat yang lebih tinggi dibanding perjalanan panjang dan harga yang ditawarkan lebih murah dibanding yang lain.

## Solution statements
- Berdasarkan hasil analisis diatas kita sangat perlu memperhatikan faktor-faktor yang berpengaruh pada perilaku pengambilan keputusan oleh penumpang. Machine Learning (ML) dapat membantu dalam memprediksi harga yang tepat. Banyak model dari ML yang dapat membantu kita dalam membuat prediksi. Pada proyek ini akan digunakan Random Forest dan LSTM (Long Short Term Memory).

## Data Understanding
Dataset yang digunakan adalah dataset dari sebuah aplikasi pemesanan tiket pesawat secara online. Data dikumpulkan dalam periode 11 Februari sampai 31 Maret 2022. Mencakup data perjalanan pada 6 kota besar di India dengan total sebanyak 300261 data dan 11 fitur. Dataset bisa didapatkan melalui tautan berikut:
[Kaggle](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)

### Variabel-variabel pada Flight Price Prediction adalah sebagai berikut:
1. Airline: Nama perusahaan penerbangan. Ada 6 perusahaan pada kolom ini.
2. Flight: Kode Penerbangan
3. Source City: Kota asal. Ada 6 kota pada kolom ini.
4. Departure Time: Waktu pemberangkatan. Pada kolom ini terdapat 6 kategori seperti 'Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'.
5. Stops: Jumlah transit. Ada 3 kategori yaitu 'zero', 'one', 'two_or_more'.
6. Arrival Time: Waktu kedatangan. Pada kolom ini terdapat 6 kategori seperti 'Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'.
7. Destination City: Kota tujuan. Ada 6 kota pada kolom ini.
8. Class: Kelas pesawat. Ada 2 kategori pada kelas ini yaitu Business dan Economy
9. Duration: Waktu perjalanan dalam satuan jam.
10. Days Left: Hasil dari pengurangan waktu booking dan waktu perjalanan.
11. Price: Harga tiket.

## Data Preparation
1. Setelah mempelajari dataset yang akan digunakan, hal pertama yang perlu dilakukan adalah melihat properti dari dataset untuk mengetahui data kolom mana yang merupakan kategorikal data atau numerical data.
2. Selanjutnya kita perlu mengetahui apakah dataset kita mempunyai data yang kosong atau null-value.
3. Kita perlu mengubah nama kolom pertama dalam dataset karena kolom tersebut memiliki nama 'Unnamed: 0' yang pastinya akan berdampak pada proses analisis berikutnya.
4. Setelah nama kolom tersebut diganti menjadi 'instance' kita dapat melakukan beberapa analisis data untuk menjawab Problem Statement diatas. Seperti grouping data untuk melihat keterkaitan satu dengan yang lain.
5. Proses berikutnya adalah pemrosesan data untuk dimasukkan kedalam model, tentu saja kolom 'instance' tidak diperlukan lagi sehingga kita dapat menghapusnya dan melanjutkan proses berikutnya seperti melihat pencilan pada fitur duration.
6. Untuk mendapatkan gambaran yang lebih jelas terkait hubungan antara 'price' dengan 'duration' dan 'days_left'. Kita dapat menggunakan matriks korelasi, dari matriks tersebut dapat diambil kesimpulan bahwa fitur 'days_left' tidak mempunyai korelasi yang bagus dengan 'price'. Oleh karena itu kita dapat membuang kolom tersebut.
7. Selain itu ada kolom kategorikal yang bernama 'flights' yang berisi tentang nomor penerbangan. Kita dapat membuang kolom tersebut karena tidak akan terlalu bepengaruh pada perdiksi harga kedepannya.
8. Untuk kolom kategorikal yang tersisa, kita akan lakukan tokenisasi menggunakan One Hot Encoder agar kolom tersebut dapat dibaca oleh mesin.
9. Langkah selanjutnya adalah membagi dataset menjadi data train dan test dengan proporsi 80% dan 20%.
10. Kita perlu melakukan standarasisasi untuk data numerikal untuk mempermudah pemrosesan oleh mesin.


## Modeling
Untuk menyelesaikan masalah prediksi harga untuk sebuah tiket pesawat. Pada proyek ini menggunakan pendekatan model regresi, yaitu:
1. Random Forest
2. Long Short-Term Memory (LSTM)
### Random Forest
Random forest merupakan pengembangan dari Decission Tree yang bekerja dengan mengumpulkan beberapa decission tree menjadi sebuah 'hutan'.
Dalam proyek ini menggunakan RandomForestRegressor yang sudah disediakan oleh scikit-learn.

Parameter yang digunakan adalah:
1. n_estimators; parameter ini menyimpan nilai jumlah pohon dalam forest; pada proyek ini diisi 30
2. max_depth; parameter ini menyimpan nilai seberapa banyak daun pada setiap pohon; pada proyek ini diisi 16
3. random_state; parameter ini menyimpan nilai random untuk memilih sample di awal; pada proyek ini diisi 30
4. n_jobs; parameter ini menyimpan nilai untuk menentukan berapa banyak job yang akan dijalankan secara paralel; pada proyek ini diisi 1

### LSTM
LSTM merupakan pengembangan dari RNN (Recurrent Neural Network).
Dalam proyek ini menggunakan LSTM yang disediaakan oleh TensorFlow.

Dengan arsitektur sebagai berikut:
1. 1 Layer LSTM dengan jumlah unit 60 dan menggunakan parameter return_sequences; mengembalikan output menjadi input pada langkah berikutnya
2. 1 Layer LSTM dengan jumlah unit 60
3. 1 Layer Dense dengan jumlah unit 30; activation relu
4. 1 Layer Dense dengan jumlah unit 10; activation relu
5. 1 Layer Output

Model LSTM dilatih dengan optimizer SGD (Stochastic Gradient Descent) dengan learning rate 1.0000e-04 dan momentum=0.9, 

- SGD dipilih menjadi optimizer agar model dapat lebih cepat menemukan nilai minimum dan maksimum pada setiap iterasi
- Parameter learning rate yang kecil menyebabkan perubahan nilai minimal dan maksimal setiap iterasi tidak akan terlalu signifikan sehingga model dapat belajar dengan lebih teliti namun berdampak pada waktu yang diperlukan untuk mencapai global minimum atau maksimum akan menjadi lebih lama.
- Parameter momentum akan mengakselerasi gradient descent untuk menuju kearah yang relevan (naik atau turun)

Jika kedua model tersebut dibandingkan berdasarkan nilai MSE (Mean Squared Error), keduanya relatif mirip karena pada proses train nilai MSE Random Forest lebih kecil namun pada proses test nilai MSE LSTM lebih kecil.

Setelah melakukan beberapa pengujian Random Forest lebih baik dalam memprediksi harga dibandingkan dengan LSTM; prediksi yang dihasilkan oleh Random Forest tidak terlalu jauh berbeda dengan nilai asli.

## Evaluation
Matriks evaluasi yang digunakan pada proyek ini adalah MSE karena MSE menghitung rata-rata dari selisih kuadrat antara nilai prediksi dan nilai aktual. Sehingga kita dapat mengetahui seberapa dekat atau jauhnya prediksi yang dihasilkan oleh model terhadap nialai aslinya.

Nilai MSE dari kedua model sebagai berikut:

|         | Random Forest | LSTM         |
|---------|---------------|--------------|
| Train   |13889.868149   | 33929.76252  |
| Testing |101280.963817  | 78429.225214 |

Dari hasil MSE diatas, nilai MSE dari kedua model ini masih cukup besar berada pada rentang nilai 33929 sampai 13889 tentu saja hal ini mengindikasikan bahwa model yang dibuat masih belum begitu baik.


Hasil prediksi kedua model adalah sebagai berikut

|     | Nilai Asli | Random Forest | LSTM    |
|-----|------------|---------------|---------|
| 1   | 42457      | 46424.4       | 47157.4 |
| 2   | 3354       | 3979.1        | 6691.9  |
| 3   | 8253       | 9949.5        | 7108.4  |

Jika dilihar dari hasil prediksi yang dilakukan, model Random Forest cukup mendekati nilai asli walaupun masih berada diatas niali asli.