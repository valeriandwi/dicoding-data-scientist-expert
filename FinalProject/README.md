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

#### Library Installation

1. Pastikan python sudah terinstall dalam device anda, untuk mengetahuinya dapat dengan membuka Command Prompt lalu ketik perintah seperti berikut

```
python --version
```

2. Jika sudah dipastikan bahwa python sudah terinstall dalam device anda, maka sekarang pastikan pip sudah terinstall dengan ketik perintah sebagai berikut di command prompt

```
pip --version
```

3. Jika sudah terinstall anda bisa melakukan install library-library yang dibutuhkan pada proyek ini dengan mengetik perintah berikut pada command prompt

```
pip install requirements.txt
```

#### Running Streamlit

1. Pastikan semua library dan model joblib semua siap, lalu jalankan perintah berikut untuk menjalankan aplikasi prediksi pada proyek ini

```
streamlit run app.py
```

#### Running Metabase (Dashboard)

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

<picture>
<img src=https://github.com/valeriandwi/dicoding-data-scientist-expert/blob/main/FinalTest/dashboard.png?raw=true>
</picture>

Pada Jaya Jaya Institut terdapat total 4424 siswa, dimana 1421 siswa sudah dinyatakan dropout. Dimana rata-rata siswa dropout memiliki angka penggagurannya cukup besar yaitu 11.62%.

Adapun beberapa faktor yang dapat dilihat melalui dashboard yang dibuat, antara lain :

1. Debtor : siswa yang mempunyai hutang atau tunggakan. Sehingga dapat mengakibatkan siswa mengalami financial stress, kesulitan mendapatkan resources seperti buku, bahan studi, atau teknologi, dan yang terakhir yaitu siswa akan rentan terhadap mental issue yang mengakibatkan ketakutan, depresi, dan merasa kekurangan harapan.
2. Umur : Siswa dengan usia muda lebih banyak mengalami dropout.
3. Terdapat kolerasi antara Admission grade ( nilai masuk minimal pada program studi tertentu ) dan jumlah kurikulum yang diambil siswa pada semester 1 dan 2. Rata-rata siswa yang mengambil program studi yang memerlukan nilai tidak terlalu besar dan jumlah kurikulum yang kecil mengalami dropout.
4. Program studi management di kelas regular dan karyawan merupakan program studi yang memiliki jumlah siswa dropout terbanyak.
5. Siswa pada usia muda lebih memilih untuk mengambil jumlah kurikulum sedikit pada setiap semesternya
6. Tingkat lulusan : Siswa yang baru lulus tingkat akhir (SMA) lebih rentan mengalami dropout
7. GDP : Siswa yang mempunyai nilai GDP kecil lebih rentan mengalami dropout

## Menjalankan Sistem Machine Learning

Untuk menjalankan sistem prediksi yang dibangun, pengguna harus memastikan sudah memasukan data sebenarnya. Dimana data yang perlu dimasukan dibagi menjadi beberapa section yaitu :

1. Personal Information, antara lain : Gender, Marital Status, Nacionality, Father Occupation, Father Qualification, Mother Occupation, Mother Qualification
2. Application Information, antara lain : DayTime Evening Attendance, Previous Qualification, International Student, Application Mode, Course, Admission Grade, Previous Qualification Grade, Displaced, Education Special Needs
3. Financial Information, antara lain : Debtor, Scholarship Holder, Tuition Fees Up To Date
4. Student Progress, antara lain : Curricular Units 1st Sem & 2nd Sem Enrolled, Curricular Units 1st & 2nd Sem Evaluations, Curricular Units 1st Sem & 2nd Approved, Curricular Units 1st & 2nd Sem Grade, Applciation Order, Age at Enrollment, Unemployment Rate, Inflation Rate, GDP

Lalu setelah keseluruhan data yang sudah diisi, pengguna dapat melihat data yang dimasukan pada table dengan menekan bagian _View the Raw Data_ menekan Tombol _Predict_ untuk melakukan prediksi menurut data yang sudah dimasukan.

Perlu diketahui sitem prediksi yang dibangun menggunakan Gradient Boosting model.

Dimana jika sistem berhasil melakukan prediksi, maka akan mengeluarkan status seperti berikut :

1. Graduate : Siswa memiliki status lulus
2. Enrolled : Siswa yang masih aktif menjalani akademik
3. Dropout : Siswa yang sudah keluar dari kegiatan akademisi

<picture>
<img src="https://github.com/valeriandwi/dicoding-data-scientist-expert/blob/main/FinalTest/assets/prediction.png?raw=true">
</picture>

Sistem prediksi ini dapat dilihat pada link berikut :
[https://dicoding-data-scientist-expert-final.streamlit.app/](https://dicoding-data-scientist-expert-final.streamlit.app/)

## Conclusion

Terdapat berbagai faktor yang dapat mengakibatkan siswa mengalami dropout :

1. Finansial : siswa yang memiliki finansial yang buruk lebih rentan mengalami dropout. Keterlambatan dalam membayar juga dapat mengakibatkannya. Data ini dapat juga terlihat melalui nilai rata-rata keseluruhan GDP siswa yang dropout.
2. Program studi : program studi dengan jumlah siswa terbanyak lebih banyak mengalami dropout.
3. Beasiswa : walau tidak banyak berpengaruh, namun perlu diperhatikan kembali oleh instansi bahwa sasaran siswa yang mendapatkan beasiswa itu harus tepat.
4. Usia : usia muda lebih rentan mengalami dropout
5. Jumlah kurikulum : Siswa dengan jumlah kurikulum yang diambil lebih rentan mengalami dropout

Untuk mendalami dan memprediksi siswa yang rentan mengalami dropout, penulis membangun sebuah model machine learning menggunakan beberapa model dan beberapa feature data numerik yang dipakai diantaranya :

- Curricular_units_1st_sem_enrolled
- Curricular_units_1st_sem_evaluations
- Curricular_units_1st_sem_approved
- Curricular_units_1st_sem_grade
- Curricular_units_2nd_sem_enrolled
- Curricular_units_2nd_sem_evaluations
- Curricular_units_2nd_sem_approved
- Curricular_units_2nd_sem_grade
- Application_order
- Age_at_enrollment
- Unemployment_rate
- Inflation_rate
- GDP

1. Logistic Regression (accuracy : 62%)
2. Decision Tree (accuracy : 65%)
3. Random Forest (accuracy : 76%)
4. Gradient Boosting (accuracy : 91%)
5. XGBClassifier (accuracy : 90%)

Sehingga didapatkan bahwa model yang cocok untuk prediksi pada proyek ini yaitu Gradient Boosting. Dimana model tersebut menggunakan pc1_1 sebagai fitur utama dalam menghasilkan sebuah prediksi.

<picture>
<img src="https://github.com/valeriandwi/dicoding-data-scientist-expert/blob/main/FinalTest/assets/gboost_feature.png?raw=true">
</picture>

### Rekomendasi Action Items

Berdasarkan data yang sudah dianalisis, didapatkan bahwa Jaya Jaya institusi dapat melakukan beberapa aksi untuk mencegah siswa mengalami dropout : </br>

1. Analisis Kinerja Akademik: Tinjau data mengenai mata kuliah yang diambil, kehadiran di kelas, kualifikasi sebelumnya, dan nilai-nilai untuk mengevaluasi kinerja akademik siswa dan mengidentifikasi area yang memerlukan perbaikan.
2. Melakukan Pengembangan Program Dukungan: Berdasarkan data tentang kebutuhan pendidikan khusus, status keuangan, dan kualifikasi orang tua, institusi dapat mengembangkan program-program dukungan yang sesuai untuk meningkatkan kesejahteraan dan kinerja siswa.
3. Melakukan Pemantauan Pembayaran Uang Kuliah: Tinjau data tentang status keterlambatan pembayaran uang kuliah dan status utang siswa untuk memastikan ketersediaan sumber daya keuangan yang memadai bagi siswa dan menangani masalah keuangan yang mungkin mempengaruhi kelancaran pendidikan mereka.
4. Analisis Dampak Faktor Ekonomi: Tinjau data tentang tingkat pengangguran, tingkat inflasi, dan GDP untuk memahami dampak faktor ekonomi terhadap pendidikan dan kesejahteraan siswa.
5. Pengembangan Program Beasiswa: Berdasarkan data tentang penerima beasiswa, institusi dapat mengembangkan program beasiswa yang sesuai untuk mendukung siswa berprestasi dan berkebutuhan finansial.
