# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

### Permasalahan Bisnis

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Cakupan Proyek

Menganalisa Berbagai Faktor yang mempengaruhi attrition rate pada perusahaan tersebut dan membuat dashboard untuk memonitor faktor tersebut.
Adapun faktor-faktor yang akan dalam proyek ini adalah sebagai berikut :

1. Bagaimana distribusi usia karyawan yang mengundurkan diri? Apakah ada pola umur tertentu yang cenderung memiliki tingkat attrition rate yang lebih tinggi?
2. Apakah ada korelasi antara lama bekerja di perusahaan dengan tingkat attrition rate? Apakah karyawan yang baru bergabung atau yang telah bekerja untuk waktu yang lama cenderung memiliki tingkat attrition rate yang lebih tinggi?
3. Apakah terdapat korelasi antara performa kerja dengan tingkat attrition rate? Apakah karyawan dengan performa yang rendah cenderung memiliki tingkat attrition rate yang lebih tinggi?
4. Apakah keseimbangan antara kehidupan kerja dan pribadi ( Work life balance ) mempengaruhi tingkat attrition rate? Apakah karyawan yang merasa tidak seimbang cenderung untuk mengundurkan diri?

### Persiapan

Sumber data: [https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv)

#### Setup environment:

Jalankan perintah berikut pada Terminal/Command Prompt/PowerShell guna memanggil (pull) Docker image untuk menjalankan Metabase.

```
docker pull metabase/metabase:v0.46.4
```

Apabila proses pembuatan docker image telah selesai, Anda dapat menjalankan image tersebut menggunakan perintah berikut.

```
docker run -p 3000:3000 --name metabase metabase/metabase
```

Import metbase.db.md.db ke dalam folder metabase.db pada data container metabase yang sudah dibuat sebelumnya

## Business Dashboard

<picture>
<img src="https://i.ibb.co/10fjnkY/Employee-Dashboard.jpg">
</picture>

Pada perusahaan Jaya Jaya Maju terdapat total 1470 total karyawan yang terdaftar, dimana karyawan yang masih active ada di angka 1291 dan 179 sudah berpindah perusahaan.

Adapun beberpa faktor yang dapat dilihat dari dashboard tersebut dan harapannya dapat membantu HR dalam memantau faktor tersebut, diantaranya :

1. Performance Rating = Dalam dashboard dapat terlihat bahwa karyawan yang berpindah perusahaan memiliki performance rating terkecil yaitu 3
2. Work Life Balance = Dalam dashboard dapat terlihat bahwa karyawan yang berpindah perusahaan terbesar memiliki work life balance rating 3, dimana jika dikategorikan score rating 3 tidak terlalu buruk.
3. Age = Dalam dashboard dapat terlihat bahwa karyawan yang berpindah perusahaan terbanyak pada umur 31, diikuti oleh umur 29 dan 26, dalam kata lain bisa dikatakan bahwa karyawan muda banyak yang berpindah perusahaan dibandingkan karyawan seniornya
4. Years At Company = Dalam dashboard dapat terlihat bahwa karyawan yang berpindah perusahaan terbanyak terjadi pada tahun pertama kerja diikuti oleh tahun kedua dan ketiga. Sehingga kita dapat menilai bahwa banyak karyawan yang tidak bertahan lama pada perusahaan tersebut.

## Conclusion

Terdapat berbagai faktor fenomena karyawan berpindah perusahaan pada perusahaan jaya jaya maju :

1. Faktor usia dapat mempengaruhi karyawan berpindah perusahaan, terbanyak karyawan yang berpindah perusahaan terjadi pada usia muda yaitu dalam rentang usia 25-35.
2. Karyawan yang baru bekerja dalam perusahaan awal memiliki attrition rate lebih besar
3. Performance Rating yang rendah juga dapat mempengaruhi karyawan berpindah perusahaan, dapat dilihat pada dashboard bahwa karyawan dengan performance rating terendah (3) memiliki jumlah yang banyak.
4. Faktor work life balance tidak terlalu berpengaruh pada attrition rate perusahaan karena dapat dilihat pada dashboard bahwa karyawan yang memilik work life balance score 3 (baik) lebih banyak berpindah perusahaan.

Dalam membantu prediksi dalam proyek ini, penulis disini membangun model machine learning menggunakan K-Means Clustering (dapat dilihat pada file notebook yang sudah tertera)

Didapatkan bahwa karyawan dengan segment 1 dan 2 lebih banyak berpindah perusahaan
<picture>
<img src="https://i.ibb.co/Rbn2bnn/download.png">
</picture>

Dimana <b>karyawan dalam segment 1 yaitu karyawan dengan rentang usia 25 - 32, memiliki nilai work life balance 3, dan rentang bekerja pada perusahaan yaitu 1 - 4 tahun.</b>
Sedangkan <b>karyawan dalam segment 2 yaitu karyawan dengan rentang usia 29-35 tahun, memiliki nilai work life balance 3, dan rentang bekerja pada perusahaan 5-8 tahun.</b>

<picture>
<img src="https://i.ibb.co/s172Wwn/download-1.png">
</picture>

### Rekomendasi Action Items

Beberapa ini adalah rekomendasi aksi yang dapat dilakukan perusahaan:

1. Ciptakan lingkungan kerja yang inovatif dan kolaboratif yang memungkinkan karyawan muda untuk berkontribusi, berbagi ide, dan merasa dihargai.
2. Tawarkan fleksibilitas dalam jadwal kerja dan lokasi kerja, termasuk opsi kerja jarak jauh atau bekerja dari rumah.
3. Sediakan program pengembangan karir yang komprehensif, termasuk pelatihan teknis, pelatihan kepemimpinan, dan mentorship.
