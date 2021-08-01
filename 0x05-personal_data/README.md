# 0x05. Personal data

## Learning Objectives
   - Examples of Personally Identifiable Information (PII)
   - How to implement a log filter that will obfuscate PII fields
   - How to encrypt a password and check the validity of an input password
   - How to authenticate to a database using environment variables

## Tasks
### [0. Regex-ing](./filtered_logger.py)
Write a function called filter_datum taking three required arguments: a list of strings fields, a string redaction a string message and a string separator, and returning a string.

The function should use a regex to replace ocurrences of certain field values.

For example:
```
>>> message = "name=Balou;email=balou@holberton.io;ssn=412-532-2382;password=abcdef;"
>>> filter_datum(fields=("email", "password"), redaction="***", message=message, separator=";")
"name=Balou;email=***;ssn=412-532-2382;password=***;"
```
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.

### [1.Log formatter](./filtered_logger.py)
Copy the following code into filtered_logger.py.
```
import logging


class RedactingFormatter(logging.Formatter):

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
```

Update the class to accept a list of strings fields constructor argument.

Implement the format method to filter values in incoming log records using filter_datum. Values for fields in fields should be filtered.

Expected result:
```
>>> import logging
>>> message = "name=Balou; email=balou@holberton.io; ssn=412-532-2382; password=abcdef;"
>>> log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
>>> formatter = RedactingFormatter(fields=("email", "ssn"))
>>> formatter.format(log_record)
"[HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Balou; email=***; ssn=***; password=abcdef;"
```

*DO NOT* extrapolate FORMAT manually. The format method should be less than 5 lines long.

### [2. Create logger ](./filtered.logger.py)
Use `user_data.csv` for this task

Implement a get_logger function that takes no arguments and returns a logging.Logger object.

The logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.

Create a tuple PII_FIELDS constant at the root of the module containing the fields from user_data.csv that are considered PII (in this csv, we have 5 PIIs). Use it to parameterize the formatter.
```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

import logging

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))

bob@dylan:~$
bob@dylan:~$ ./main.py
<class 'logging.Logger'>
PII_FIELDS: 5
bob@dylan:~$
```

### [3. Connect to secure database](./filtered_logger.py)
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.

In this task, you will connect to a secure holberton database to read a users table. The database is protected by a username and password that are set as environment variables on the server named PERSONAL_DATA_DB_USERNAME (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”).

The database name is stored in PERSONAL_DATA_DB_NAME.

Implement a get_db function that returns a connector to the database.
   - Use the os module to obtain credentials from the environment
   - Use the module mysql-connector-python to connect to the MySQL database (pip3 install mysql-connector-python)

```
bob@dylan:~$ cat main.sql
-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root_user@localhost IDENTIFIED BY 'root_pwd';
GRANT ALL PRIVILEGES ON root_user.* TO 'my_db'@'localhost';

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    email VARCHAR(256)
);

INSERT INTO users(email) VALUES ("bob@dylan.com");
INSERT INTO users(email) VALUES ("bib@dylan.com");

bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot_user -p my_db
Enter password: 
2
bob@dylan:~$ 
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

get_db = __import__('filtered_logger').get_db

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()

bob@dylan:~$
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root_user PERSONAL_DATA_DB_PASSWORD=root_pwd PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./main.py
2
bob@dylan:~$
```

### [4. Read and filter data](./filtered_logger.py)
Implement a main function that takes no arguments and returns nothing.

The function will obtain a database connection using get_db and use it to retrieve all rows in the users table. Format each row into the following string
```
"name=Marlene Wood; email=hwestiii@att.net; phone=(473) 401-4253; ssn=261-72-6780; password=K5?BMNv; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;"
```
then log them to the filtered logger.

Only your main function should run when the module is executed.
```
bob@dylan:~$ cat main.sql
-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root_user@localhost IDENTIFIED BY 'root_pwd';
GRANT ALL PRIVILEGES ON root_user.* TO 'my_db'@'localhost';

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    name VARCHAR(256), 
        email VARCHAR(256), 
        phone VARCHAR(16),
    ssn VARCHAR(16), 
        password VARCHAR(256),
    ip VARCHAR(64), 
        last_login TIMESTAMP,
    user_agent VARCHAR(512)
);

INSERT INTO users('name', 'email', 'phone', 'ssn', 'password', 'ip', 'last_login', 'user_agent') VALUES ("Marlene Wood","hwestiii@att.net","(473) 401-4253","261-72-6780","K5?BMNv","60ed:c396:2ff:244:bbd0:9208:26f2:93ea","2019-11-14 06:14:24","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36");
INSERT INTO users('name', 'email', 'phone', 'ssn', 'password', 'ip', 'last_login', 'user_agent') VALUES ("Belen Bailey","bcevc@yahoo.com","(539) 233-4942","203-38-5395","^3EZ~TkX","f724:c5d1:a14d:c4c5:bae2:9457:3769:1969","2019-11-14 06:16:19","Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30");

bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot_user -p my_db
Enter password: 
2
bob@dylan:~$ 
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root_user PERSONAL_DATA_DB_PASSWORD=root_pwd PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
name=Marlene Wood; email=hwestiii@att.net; phone=(473) 401-4253; ssn=261-72-6780; password=K5?BMNv; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
name=Belen Bailey; email=bcevc@yahoo.com; phone=(539) 233-4942; ssn=203-38-5395; password=^3EZ~TkX; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
bob@dylan:~$

```

### [5. Encrypting passwords](./encrypt_password.py)
User passwords should NEVER be stored in plain text in a database.

Implement a hash_password function that expects one string argument and returns a salted, hashed password, which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw).
```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password

password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))

bob@dylan:~$
bob@dylan:~$ ./main.py
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
b'$2b$12$xSAw.bxfSTAlIBglPMXeL.SJnzme3Gm0E7eOEKOVV2OhqOakyUN5m'
bob@dylan:~$
```

### [6. Check valid password](./encrypt_password.py)
Implement an is_valid function that expects a hashed_password bytes argument and password string argument and returns a boolean.

Use bcrypt to validate that the provided password matches the hashed password.
```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))

bob@dylan:~$
bob@dylan:~$ ./main.py
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
True
bob@dylan:~$

```