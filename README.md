# Aiogram New Template (aiogram 3)

### 1. Create virtual environment and install packages
Windows
```shell
python -m venv venv && venv\bin\activate && pip install -r requirements.txt
```

Linux/Mac
```shell
python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt
```

### 2. Create .env file and copy all variables from .env_example to it and customize your self (if needed)

### 3. Run app.py
Windows
```shell
python app.py
```
Linux/Mac
```shell
python3 app.py
```

# Set up Postgresql on server

### 1. Install postgresql (if needed)
```shell
sudo apt install -y postgresql postgresql-contrib
```

### 2. Log in to the postgresql shell
```shell
sudo -u postres psql
```

### 3. Create a database (in postgresql shell)
```shell
CREATE DATABASE database_name WITH template = template0 ENCODING 'UTF8' LC_CTYPE 'C' LC_COLLATE 'C';
```

### 4. Create a user (in postgresql shell)
```shell
CREATE USER user_name WITH PASSWORD 'password';
```

### 5. Set encoding (in postgresql shell)
```shell
ALTER ROLE user_name SET client_encoding TO 'utf8';
```

### 6. Restrict transactions from an unexpected db user (in postgresql shell)
```shell
ALTER ROLE user_name SET default_transaction_isolation TO 'read committed';
```

### 7. Set timezone (in postgresql shell)
```shell
ALTER ROLE user_name SET timezone TO 'UTC';
```
> **_Note:_**  If you use another timezone in your project, replace **'UTC'** with yours.

### 8. Grant the user the right to manage the db (in postgresql shell)
```shell
GRANT ALL PRIVILEGES ON DATABASE database_name TO user_name;
```

### 9. Quit postgresql (in postgresql shell)
```shell
\q
```

## If you have questions for this project, join and ask our community: https://t.me/+Wu3loL2thM8yZDMy

<p align="center">
<img style="width: 60%;" src="https://i.postimg.cc/nzykWKNd/result.gif">
</p>
