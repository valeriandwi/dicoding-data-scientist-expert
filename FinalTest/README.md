# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis

1. **Tingkat Dropout yang Tinggi** : Jumlah siswa yang tidak menyelesaikan pendidikan atau dropout dari Jaya Jaya Institut cukup signifikan. Ini bisa berdampak negatif pada reputasi institusi dan juga mengurangi potensi pendapatan dari jumlah siswa yang lulus

2. **Resiko Kehilangan Potensi** : Setiap siswa yang dropout mewakili potensi yang hilang dalam hal kontribusi akademisi, karir, dan potensi kontribusi sosial yang bisa mereka berikan.

3. **Kebutuhan untuk Interenvensi Dini** : Institusi perlu mendeteksi siswa yang beresiko tinggi dropout secepat mungkin agar mereka dapat memberikan bimbingan khusus dan intervensi yang dibutuhkan untuk membantu siswa tersebut menyelesaikan pendidikannya.

4. **Kebutuhan Dashboard** : Dalam rangka memantau performa siswa dan mengidentifikasi siswa yang beresiko tinggi untuk dropout, diperlukan pengembangan dashboard yang dapat memberikan informasi yang relevan dan mudah dimengerti oleh pihak institusi pendidikan. Ini memungkinkan mereka untuk mengambil tindakan secara proaktif.

5. **Penyelidikan Faktor Penyebab** : Penting untuk menyelidiki faktor-faktor yang mungkin menyebabkan tingginya tingkat dropout, seperti masalah akademik, masalah keuangan, masalah pribadi, atau kurangnya dukungan sosial.

### Cakupan Proyek

Berdasarkan permasalahan bisnis yang telah diidentifikasi, cakupan proyek dapat mencakup beberapa tahapan, antara lain :

1. Data Preparation:

- Pengumpulan dan pembersihan data: Memastikan data yang diperlukan tersedia dan dalam format yang sesuai untuk analisis.
- Pemrosesan data: Melakukan transformasi dan penyatuan data jika diperlukan untuk mempersiapkannya untuk analisis.

2. Analisis Eksploratif:

- Eksplorasi data: Menganalisis distribusi variabel, korelasi antar variabel, dan pola-pola yang mungkin terdapat dalam data.
- Identifikasi faktor-faktor potensial yang berkaitan dengan dropout: Mengidentifikasi variabel-variabel yang dapat menjadi prediktor atau indikator dropout siswa.

3. Model Prediksi Dropout:

- Pengembangan model prediksi: Membangun model statistik atau machine learning untuk memprediksi kemungkinan dropout siswa berdasarkan faktor-faktor yang telah diidentifikasi.
- Evaluasi model: Mengukur kinerja model untuk memastikan akurasi dan keandalannya.

4. Intervensi dan Bimbingan:

- Pengembangan strategi intervensi: Merancang program bimbingan dan intervensi yang sesuai untuk siswa yang berisiko tinggi dropout.
- Implementasi strategi: Melaksanakan program bimbingan dan intervensi kepada siswa yang telah diidentifikasi sebagai berisiko tinggi.

5. Monitoring dan Evaluasi:

- Pengembangan dashboard: Membangun dashboard atau laporan interaktif untuk memantau performa siswa secara kontinu dan mendeteksi perubahan dalam tingkat dropout.
- Evaluasi efektivitas: Mengevaluasi efektivitas strategi intervensi dan mengidentifikasi perubahan dalam tingkat dropout.

### Persiapan

Sumber data: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv

Setup environment:

1. Jalankan perintah berikut pada Terminal/Command Prompt/PowerShell guna memanggil (pull) Docker image untuk menjalankan Metabase.

```
docker pull metabase/metabase:v0.46.4
```

2. Apabila proses pembuatan docker image telah selesai, Anda dapat menjalankan image tersebut menggunakan perintah berikut.

```
docker run -p 3000:3000 --name metabase metabase/metabase
```

3. Import metbase.db.md.db ke dalam folder metabase.db pada data container metabase yang sudah dibuat sebelumnya

## Business Dashboard

## Menjalankan Sistem Machine Learning

Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
