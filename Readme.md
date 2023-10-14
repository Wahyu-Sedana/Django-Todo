## Cara menjalankan Django Todo
1. Install depedencies
```
pip install -r requirements.txt
```
2. Jalankan migrasi database
```
python manage.py migrate
```
3. Buat superuser
```
python manage.py createsuperuser
```
4. Jalankan server
```
python manage.py runserver
```
5. Buka browser di 
```
http://localhost:8000/todo
```

6. Untuk login ke admin di
```
http://localhost:8000/admin
```