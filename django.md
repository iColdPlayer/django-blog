Tutorials dango untuk pemula

Django sendiri adalah sebuah web framework yang termasuk mature, robust.<br>

Dan pada kesempatan kali ini kita akan mencoba Django untuk membuat sebuah aplikasi sederhana berbasis web.

Langsung saja kita mulai.

Adapun langkah-langkah yang harus diikuti di antaranya:

- Siapkan directory project kita.
    - `$ mkdir aplikasi && cd aplikasi`
- Siapkan `Virtual Environment`.
    - `python -m venv env` /  `python3 -m venv env`
- Install Django dengan perintah:
    - `pip install django`
- Startproject dengan perintah:
    - `django-admin startproject djangoApps`

Setelah  kita mengikutai langkah di atas maka kita akan mempunyai directory baru bernama `djangoApps`. `djangoApps` adalah nama project kita.

Jika kita melihat ke dalamnya maka akan mempunyai struktur folder seperti berikut:

```
aplikasi/
│
├── djangoApps/
│   ├── djangoApps/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
└── env/
```
- `aplikasi` adalah directory / folder root yang kita buat pertama kali.<br>
- `djangoApps` adalah nama project kita dan merupakan hasil dari ketika kita menjalankan perintah: `django-admin startproject djangoApps`.
- `settings.py` adalah file berupa *configurations* dari project kita. 
- `__init__.py` adalah pengenal project itu sendiri sehingga kita bisa melakukan import ke `apps` yang akan kita buat setelah ini.
- `wsgi.py` adalah file untuk configurasi server dsb.
- `manage.py` adalah file yang kita gunakan untuk menjalankan project kita.
- dan `env` adalah virtual environment yang telah kita buat sebelumnya.

Pada struktur file di atas kita mempunyai 2 folder bernama `djangoApps.` Untuk memudahkan kita dalam mengenali antara **project directory** dan **root directory** maka pindahkan file `djangoApps/djangoApps/*` ke luar folder.
Sehingga struktur folder kita akan terlihat seperti berikut:

```
aplikasi/
│
├── djangoApps/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/
│
└── manage.py
``` 
Sehingga akan mempermudah kita dalam mengenali struktur folder project yang sedang kita kerjakan.

Langkah selanjutnya kita jalankan server dengan perintah:<br>
`$ ./manage.py runserver` atau bisa juga <br>
`$ python manage.py runserver`

Maka server akan berjalan dengan notifikasi:
```
(env) icoldplayer@icoldplayer:~/Documents/django/djapps$ ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

May 15, 2019 - 17:45:52
Django version 2.2.1, using settings 'djangoApps.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Maka server telah berjalan, pada alamat: `127.0.0.0:8000` atau bisa juga menggunakan `localhost:8000`. <br>
hasilnya adalah seperti berikut ini:

[](images to)



Di sini kita telah berhasil menginstall dan membuat sebuah django project di directory `aplikasi`.


Langkah selanjutnya adalah membuat `apps` / `aplikasi` yang akan kita gunakan nantinya. <br>
Django sendiri menggunakan metode `Model`, `View`, `Templating`. <br>
Dan setiap `apps` mempunyai `model`, `views`, dan `template` tersendiri.

#### Second Steps 
Langsung saja, selanjutnya kita akan membuat sebuah `apps` bernama `HelloWorld`. <br>
Ketikkan perintah di bawah ini untuk membuat sebuah aplikasi pada project kita.

- `./manage.py startapp helloWorld` <br>
- Maka django akan otomatis membuat sebuah directory baru bernama `helloWorld.`
- Selanjutnya, setiap kali kita membuat aplikasi, maka jangan lupa untuk menginstall nya juga di `settings.py`. 
- Masuk ke `settings.py` dan ketikkan naman aplikasi kita di dalamnya.

`settings.py`:<br>
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    static,
    
    #nama aplikasi.
    'helloWorld' 
]
```
- Langkah selanjutnya cobalah masuk ke folder aplikasi kita yaitu `helloWorld`.
- Di dalam folder tersebut kita mempunyai beberapa file di antaranya:
    - `__init__.py` untuk memberitahu python agar kita dapat memperlakukan folder `helloWorld` sebagai python package.
    - `admin.py` berisi konfigurasi halaman django admin.
    - `apps.py` berisi konfigurasi untuk aplikasi kita.
    - `models.py` berisi `class series` yang digunakan oleh `Django` untuk membuat sebuah ORM / `class` yang akan diconvert ke dalam database yang kita gunakan.
    - `tests.py` untuk melakukan test terhadap aplikasi kita.
    - `views.py` berisi konfigurasi fungsi / class yang akan kita gunakan pada html template nantinya.
    
    
#### Third Step
Selanjutnya kita akan membuat sebuah `views` yang akan ditampilan ke dalam html templates dan browser.

`Views` sendiri berisi sebuah fungsi yang dapat digunakan untuk menampilkan data ke dalam templates.

`views.py`:
```python
from django.shortcuts import render

def halo_dunia(request):
    return render(request, 'halo_dunia.html')
```
- Pada baris pertama kita melakukan import sebuah `built in function` bernama `render` dari module bernama `django.shortcuts`.
- Pada baris kedua kita membuat sebuah fungsi view bernama `halo_dunia()` dan memiliki 1 argumen yaitu `request.`
- Dan pada baris ketiga, ketika fungsi tersebut dipanggil maka akan menrender sebuah html file bernama `halo_dunia.html.`
- File `halo_dunia.html` sendiri belum ada, kita akan membuatnya sebentar lagi.
- Selanjutnya kita membuat folder bernama `templates` di dalam `helloWorld apps.` dan di dalam folder `templates` kita buat 
    sebuah file bernama `halo_dunia.html.`

buatlah folder templates di dalam helloWorld folder
```
$ mkdir templates && cd templates
$ touch halo_dunia.html
```
Buatlah sebuah kerangka html sederhana:
```html
<!DOCTYPE html>
<html>
<head>
   <title>Django Site</title>
</head>
<body>
   <h1>Belajar Django Site</h1>
   <p>My first Django Site</p>
</body>
</html>
```
Pada contoh di atas kita telah membuat sebuah view function dan membuat sebuah template untuk ditampilkan kepada user/browser. Akan tetapi kita belum dapat mengaksesnya karena kita tidak tahu dimana template tersebut akan muncul.<br>

Langkah selanjutnya adalah membuat url yang akan menampilkan template yang baru saja kita buat.

Langkah selanjutnya, buatlah sebuah file bernama `urls.py` di dalam folder `helloWorld` kita.

`urls.py`:
```python
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.halo_dunia, name='halo_dunia')
]
```
- Baris pertama, kita melakukan import built in bernama `path.`
- Pada baris kedua, kita melakukan import `views` dari `helloWorld` apps yang telah kita buat sebelumnya.
- Pada baris ketiga dan empat, kita membuat sebuah `list` bernama `urlpatterns` dan membuat url untuk situs kita bernama `halo_dunia`


Langkah selanjutnya, **masuklah ke folder aplikasi**, edit file `urls.py`:
```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('halo_dunia.urls'))
]
```
Jalankan kembali server dengan perintah: ` python manage.py runserver.`

Masuk ke browser dan ketikkan alaman `127.0.0.1:8000` / `localhost:8000` maka kita akan mendapatkan tampilan seperti di bawah ini:

[](image screenshot)


Congratulations, kalian telah berhasil membuat sebuah homepage sederhana dengan Django 2.2.

What's next?

Pada tutorials selanjutnya kita akan mempelajari tentang cara integrasi template di django.



#### Conclusion: <br>

Pada sebuah web / situs, akan terdapat banyak menu dan tampilan.
Oleh karena itu, dengan metode `apps` django kita akan dengan mudah membuat sebuah aplikasi dan menggunakannya kembali di project lainnya.

Contoh:
sebuah website terdiri dari `Home`, `About`, `Blog`, `Contact`, `Account`, dll.
Dengan metode `apps` tersebut kita dapat membuatnya menjadi masing-masing `apps` yang terpisah satu dengan lainnya. 

Sehingga akan memudahkan kita dalam membangun sebuah website yang utuh dengan menggabungkannya menjadi satu dan akan mudah melakukan `debug` apabila terjadi error.

