# Trabalho Realizado na Semana 11

## Public-Key Infrastructure (PKI) Lab

### Task 1

For this task, we needed to create our own CA certificate. For that, we ran the following command:

```
[01/12/22]seed@VM:~/.../Labsetup$ openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -keyout ca.key -out ca.crt
Generating a RSA private key
.....................++++
.............................................................++++
writing new private key to 'ca.key'
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:PT
State or Province Name (full name) [Some-State]:Porto
Locality Name (eg, city) []:Porto
Organization Name (eg, company) [Internet Widgits Pty Ltd]:FEUP
Organizational Unit Name (eg, section) []:FSI
Common Name (e.g. server FQDN or YOUR name) []:ooga
Email Address []:
```

Using the first command:
```
[01/12/22]seed@VM:~/.../Labsetup$ openssl x509 -in ca.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            1a:07:b8:33:ff:ef:46:76:28:09:8f:fe:28:ed:16:c7:93:cf:45:a0
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = PT, ST = Porto, L = Porto, O = FEUP, OU = FSI, CN = ooga
        Validity
            Not Before: Jan 12 09:04:03 2022 GMT
            Not After : Jan 10 09:04:03 2032 GMT
        Subject: C = PT, ST = Porto, L = Porto, O = FEUP, OU = FSI, CN = ooga
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (4096 bit)
                Modulus:
                    00:98:54:83:47:eb:e0:1e:62:f7:ee:0d:7f:f4:48:
                    b7:3f:bb:f2:66:10:00:9f:81:a8:b9:78:61:cd:eb:
                    c7:8a:d5:da:31:21:f5:fc:ce:28:cd:63:66:e9:f8:
                    be:c0:26:9c:32:41:b4:79:7e:d7:55:91:4e:a1:d1:
                    62:06:f1:64:67:aa:0e:a9:a8:7b:fa:0c:39:12:c3:
                    5b:1f:10:1e:3b:99:f6:f4:2f:58:a8:bb:a1:07:a4:
                    18:f3:0e:04:b9:01:e6:21:15:f1:0f:64:8d:d6:a7:
                    da:11:79:7b:2a:34:43:58:14:62:55:27:51:f6:6f:
                    34:0d:e0:c6:e8:e2:76:ff:dd:74:e1:68:01:e8:20:
                    a9:65:91:4f:a0:39:a6:b4:1e:18:76:af:78:c5:1e:
                    d7:3f:b6:78:d2:0c:c7:af:94:16:d0:61:d6:e3:16:
                    5f:3c:30:97:62:0c:f6:21:0d:e9:a2:85:02:b5:3b:
                    eb:4f:d4:39:a1:4d:6c:54:59:98:12:49:6d:09:ef:
                    59:ae:b9:9b:11:c6:13:7e:e5:c6:53:b8:04:66:f7:
                    15:24:46:49:bd:64:46:c9:79:89:b4:d6:f0:ac:78:
                    96:51:eb:3b:fa:f7:eb:0c:6e:2a:62:54:15:b6:11:
                    d8:7a:fb:08:02:23:06:13:f9:bd:33:77:99:7b:da:
                    97:5e:56:56:58:29:18:a5:3d:c6:ec:46:a6:a5:08:
                    8e:ff:bd:ad:81:95:ed:66:63:6d:10:55:27:82:76:
                    20:b6:27:93:aa:b6:71:ef:4b:1b:ac:8d:59:9f:f4:
                    c1:2b:60:f6:4b:60:d7:0d:6a:87:a9:38:60:1a:e3:
                    39:c9:62:d7:be:42:56:0f:c3:8c:38:81:f6:a8:bf:
                    9a:f5:ef:15:ad:2c:3d:e8:47:15:20:ab:5b:df:2d:
                    ad:b2:7b:c5:20:7b:92:f8:dd:71:bb:ad:36:7e:81:
                    36:55:a7:1b:da:59:de:e6:38:35:27:1d:b4:2d:78:
                    47:97:e9:19:f2:fb:5e:d3:38:66:1e:cd:be:0f:1a:
                    a8:70:5d:01:41:d3:4a:df:d4:aa:b9:5f:f2:6b:4f:
                    66:e2:94:16:00:27:f8:8f:20:91:63:3f:ca:1e:b6:
                    05:a3:18:ee:a2:3e:12:cd:b6:c2:e8:3e:ac:fe:02:
                    1d:94:66:42:03:9b:04:98:e2:b9:44:eb:5b:d3:3c:
                    b6:d2:19:c4:bb:3d:de:93:b4:af:05:3b:7c:0c:86:
                    2f:4e:b4:1f:4d:8c:86:c2:ea:f8:23:c8:c7:a2:d3:
                    19:11:a1:aa:71:0f:db:c7:86:91:99:43:de:1a:79:
                    ec:08:38:14:9b:5d:22:ef:b3:1f:59:2e:b0:f8:05:
                    0f:da:a3
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier: 
                1C:DC:D3:1D:D5:33:C2:C4:0D:EF:1F:A5:E6:F6:79:A5:4D:0A:25:A7
            X509v3 Authority Key Identifier: 
                keyid:1C:DC:D3:1D:D5:33:C2:C4:0D:EF:1F:A5:E6:F6:79:A5:4D:0A:25:A7

            X509v3 Basic Constraints: critical
                CA:TRUE
    Signature Algorithm: sha256WithRSAEncryption
         3c:be:49:68:10:fa:f4:86:80:f9:eb:25:05:c9:d4:a9:62:bb:
         cc:71:9c:e7:0c:9d:b6:36:e6:0f:13:e5:72:ff:aa:5f:0d:16:
         be:eb:8c:98:03:2b:2d:a7:8c:77:5d:37:08:30:f2:25:a5:a0:
         c9:de:67:04:a6:16:7d:67:cc:9c:18:c0:7a:27:0c:91:cc:54:
         87:aa:23:9f:ab:e0:55:5e:f2:34:9c:56:57:e4:ea:fb:ed:61:
         cf:08:87:c2:d5:d3:c0:44:3f:ec:fa:4c:08:6e:f2:eb:dc:36:
         cb:9f:f4:dc:97:f7:80:8f:ca:74:cd:81:63:cc:60:6a:f3:a8:
         16:8c:fd:c3:82:60:16:b0:49:5b:2e:ad:db:44:d5:81:ba:2f:
         eb:9c:73:b6:8c:d4:02:8b:46:8f:a7:5b:06:d5:e8:cd:dd:44:
         25:51:5d:50:15:eb:3b:07:85:73:dc:57:18:5c:2c:7e:bf:2f:
         97:5d:fc:12:39:29:9f:03:1c:52:f9:dc:ca:d6:c4:74:91:80:
         f5:33:11:76:2a:de:39:4b:8f:16:fb:74:54:40:12:f4:4c:e0:
         42:0e:87:e3:59:12:ac:d4:ec:e5:66:56:00:41:43:30:37:8a:
         c9:b1:76:35:9b:bb:7f:94:49:25:b7:20:e8:44:74:17:cc:75:
         00:4a:ac:ec:0d:eb:b1:1d:81:84:85:06:d0:77:5f:49:9e:e4:
         15:75:17:e5:65:93:59:03:c4:e0:10:6e:2b:57:17:ab:cd:d0:
         44:98:db:49:23:23:c4:d9:1e:fe:90:bd:49:8c:65:90:fd:71:
         e7:2c:de:62:53:0e:0e:10:d1:b9:47:5f:38:2a:e3:c8:a9:ec:
         5a:fc:1f:ba:47:da:86:73:f5:c8:46:47:2e:02:2d:74:02:f3:
         cd:73:ec:c6:70:90:cd:35:b2:28:d4:ce:ee:56:37:68:89:54:
         62:e7:da:e1:fc:d5:6f:22:0c:05:01:07:40:07:ab:50:23:39:
         6f:78:08:4a:2a:a1:d4:0d:2d:db:5d:ff:05:6e:71:77:81:31:
         b9:1d:f3:24:7a:5d:d6:bb:78:f2:8f:90:d4:59:aa:d2:ca:5d:
         e5:6a:21:01:76:b1:41:87:9f:fa:20:94:56:a4:80:ec:15:1e:
         6f:58:26:25:a4:fc:15:a9:d8:c8:ad:f9:8f:9c:a0:c4:ca:65:
         f2:07:e3:b7:7a:c1:6f:5e:7e:f0:59:bb:f1:c4:d8:8b:e2:10:
         74:61:95:15:8c:0e:69:8d:44:0e:d6:0c:df:24:40:5d:45:2f:
         2e:a6:90:0f:b6:12:dc:a5:a8:fc:90:da:0e:71:e6:92:e2:97:
         d8:13:1b:a0:d8:ca:e4:1a
```

Using the second command:
```
[01/12/22]seed@VM:~/.../Labsetup$ openssl rsa -in ca.key -text -noout
Enter pass phrase for ca.key:
RSA Private-Key: (4096 bit, 2 primes)
modulus:
    00:98:54:83:47:eb:e0:1e:62:f7:ee:0d:7f:f4:48:
    b7:3f:bb:f2:66:10:00:9f:81:a8:b9:78:61:cd:eb:
    c7:8a:d5:da:31:21:f5:fc:ce:28:cd:63:66:e9:f8:
    be:c0:26:9c:32:41:b4:79:7e:d7:55:91:4e:a1:d1:
    62:06:f1:64:67:aa:0e:a9:a8:7b:fa:0c:39:12:c3:
    5b:1f:10:1e:3b:99:f6:f4:2f:58:a8:bb:a1:07:a4:
    18:f3:0e:04:b9:01:e6:21:15:f1:0f:64:8d:d6:a7:
    da:11:79:7b:2a:34:43:58:14:62:55:27:51:f6:6f:
    34:0d:e0:c6:e8:e2:76:ff:dd:74:e1:68:01:e8:20:
    a9:65:91:4f:a0:39:a6:b4:1e:18:76:af:78:c5:1e:
    d7:3f:b6:78:d2:0c:c7:af:94:16:d0:61:d6:e3:16:
    5f:3c:30:97:62:0c:f6:21:0d:e9:a2:85:02:b5:3b:
    eb:4f:d4:39:a1:4d:6c:54:59:98:12:49:6d:09:ef:
    59:ae:b9:9b:11:c6:13:7e:e5:c6:53:b8:04:66:f7:
    15:24:46:49:bd:64:46:c9:79:89:b4:d6:f0:ac:78:
    96:51:eb:3b:fa:f7:eb:0c:6e:2a:62:54:15:b6:11:
    d8:7a:fb:08:02:23:06:13:f9:bd:33:77:99:7b:da:
    97:5e:56:56:58:29:18:a5:3d:c6:ec:46:a6:a5:08:
    8e:ff:bd:ad:81:95:ed:66:63:6d:10:55:27:82:76:
    20:b6:27:93:aa:b6:71:ef:4b:1b:ac:8d:59:9f:f4:
    c1:2b:60:f6:4b:60:d7:0d:6a:87:a9:38:60:1a:e3:
    39:c9:62:d7:be:42:56:0f:c3:8c:38:81:f6:a8:bf:
    9a:f5:ef:15:ad:2c:3d:e8:47:15:20:ab:5b:df:2d:
    ad:b2:7b:c5:20:7b:92:f8:dd:71:bb:ad:36:7e:81:
    36:55:a7:1b:da:59:de:e6:38:35:27:1d:b4:2d:78:
    47:97:e9:19:f2:fb:5e:d3:38:66:1e:cd:be:0f:1a:
    a8:70:5d:01:41:d3:4a:df:d4:aa:b9:5f:f2:6b:4f:
    66:e2:94:16:00:27:f8:8f:20:91:63:3f:ca:1e:b6:
    05:a3:18:ee:a2:3e:12:cd:b6:c2:e8:3e:ac:fe:02:
    1d:94:66:42:03:9b:04:98:e2:b9:44:eb:5b:d3:3c:
    b6:d2:19:c4:bb:3d:de:93:b4:af:05:3b:7c:0c:86:
    2f:4e:b4:1f:4d:8c:86:c2:ea:f8:23:c8:c7:a2:d3:
    19:11:a1:aa:71:0f:db:c7:86:91:99:43:de:1a:79:
    ec:08:38:14:9b:5d:22:ef:b3:1f:59:2e:b0:f8:05:
    0f:da:a3
publicExponent: 65537 (0x10001)
privateExponent:
    3d:e1:7f:1f:35:6b:eb:0c:2b:49:92:44:5b:79:3a:
    af:f2:6a:cb:19:4f:17:7c:f5:8c:ba:a1:88:a4:72:
    80:2c:d5:a1:45:f9:86:c4:3d:01:0a:93:61:12:c2:
    72:8e:7c:bf:51:bf:bd:e7:50:14:9b:9d:c4:d0:a9:
    30:c6:d9:11:df:9c:6b:41:5d:73:bb:89:67:dc:e2:
    64:61:08:d7:0f:79:a9:c2:9e:12:95:7e:19:fb:88:
    83:1c:3b:c0:e8:4b:93:3f:35:99:1a:31:20:75:39:
    7a:05:ce:89:db:87:4b:fd:a3:e0:91:c3:93:07:a3:
    ae:cb:94:22:40:f5:34:85:c3:18:5a:47:04:04:58:
    ac:40:f6:86:d1:44:ae:40:d7:91:47:41:19:5a:a8:
    f8:61:e8:fc:f3:62:1f:2a:5a:86:36:68:b4:01:7f:
    98:94:e8:ba:55:27:9b:4f:ea:8c:31:da:62:c3:3f:
    99:43:4e:51:ff:80:b5:57:5c:16:79:ab:88:f0:a9:
    8e:f8:29:4d:74:18:b1:61:28:4b:14:22:fd:ac:fb:
    f2:ab:77:03:2f:fc:2d:96:68:e1:84:bb:6a:64:e6:
    33:cb:0a:a7:ae:14:d7:0c:dd:bc:ea:09:93:d7:f6:
    08:27:78:1e:5e:19:f6:fd:69:e5:c1:7d:21:3a:30:
    68:ea:d6:8e:fe:fb:2b:44:bb:87:55:1a:90:88:d8:
    19:40:b8:19:09:bd:ce:fa:6a:83:d3:09:af:60:b5:
    43:11:9b:02:4b:96:7f:35:07:59:74:5b:6a:a4:bc:
    8e:c6:1e:a8:04:61:7d:31:60:73:42:f4:37:d0:7c:
    56:f1:58:bd:a1:41:9a:bb:51:fd:a8:e7:bd:2a:f8:
    ec:c1:68:28:f4:53:98:7b:ca:01:67:50:08:db:13:
    f0:fb:cf:6b:72:5f:09:84:93:a8:5e:58:09:a9:69:
    05:40:6e:c1:96:b9:d2:e1:c8:86:00:2c:7c:40:a6:
    f6:fb:bd:78:30:e8:ca:94:3d:19:f2:62:b7:ec:52:
    e2:f7:54:86:af:75:9e:a3:17:6c:81:8a:88:8b:e3:
    88:3f:71:37:13:86:f5:4e:70:9e:d8:59:c0:0a:93:
    3c:14:5a:79:75:e6:29:fa:1d:0d:fb:80:e3:5f:5f:
    c7:9c:a3:64:81:4c:3e:cc:06:fc:ed:35:bc:4b:02:
    a2:4f:ba:7f:2e:96:53:69:a4:32:af:1e:6a:1f:07:
    ad:d6:11:0f:62:63:07:19:cc:15:37:b1:ac:00:5b:
    18:81:e8:c4:6d:e5:f0:95:a1:1f:4f:77:ad:97:38:
    2b:c7:76:f9:32:f9:9e:48:09:ee:bb:fa:46:fd:0f:
    57:c9
prime1:
    00:c8:3a:4e:1b:a6:de:09:0b:33:c0:32:45:44:74:
    0a:0e:53:68:4d:56:f3:38:f9:93:57:ff:39:9b:1a:
    08:2c:76:18:05:8c:c5:5a:15:20:73:e4:8b:e5:8c:
    55:15:55:fb:c2:93:19:a9:87:ce:39:ae:f1:6d:c9:
    2c:6b:49:81:a8:85:a9:90:5d:d5:9a:78:7f:cb:18:
    7e:73:f7:b7:5e:cc:ce:5e:ee:80:22:31:50:cf:72:
    94:0c:cb:da:8c:1e:e3:50:f7:7a:fe:6b:d0:d7:28:
    04:28:0e:4c:71:4a:f2:40:d2:8b:bb:4d:25:9d:a0:
    0a:5a:68:af:2c:10:33:b4:e3:04:9c:f8:da:65:ac:
    17:13:14:8c:52:8b:bc:63:aa:51:6a:11:09:47:0c:
    34:eb:7e:d6:e4:c4:01:60:18:e9:d3:1d:3a:56:13:
    af:f2:db:da:51:0f:2b:26:e7:00:a0:98:6f:fa:d2:
    09:e1:1d:da:6c:22:af:a6:02:f4:13:07:34:89:d6:
    ac:ce:33:f2:3e:69:f3:f9:b1:78:9a:09:ca:fa:95:
    fd:c8:42:79:fb:1a:80:2b:24:d1:52:46:09:49:17:
    0c:d6:aa:9d:d1:4f:b3:70:5b:c1:95:96:6e:8c:4e:
    56:10:6d:96:b5:a2:06:62:53:55:bf:80:62:22:03:
    c5:97
prime2:
    00:c2:c2:c2:37:bb:9f:ea:c0:6e:90:7e:91:fc:32:
    8e:49:e2:1b:30:62:e7:0d:79:61:60:74:4b:06:63:
    0f:6b:25:d7:f0:17:83:8b:ab:96:57:d1:12:7b:1f:
    39:c1:11:9c:ad:af:29:86:c5:18:db:d4:91:c1:04:
    a7:2e:94:77:cb:9f:12:10:18:93:f9:73:81:49:c3:
    0e:ec:fc:cd:35:b3:36:16:3e:7b:5e:2d:fc:c1:7a:
    1c:6d:1a:b9:51:13:d4:e5:6b:e8:10:65:b1:9a:38:
    cb:5a:2f:a4:56:60:4d:0c:e6:bd:2f:c7:cf:1e:b1:
    84:b4:41:bd:fb:db:67:0c:bd:d2:e9:f6:94:6b:f4:
    ba:f6:a3:4f:d5:f5:5c:57:2e:c6:ef:7e:c3:54:8e:
    e8:e6:c2:ed:54:7e:7b:2e:14:c8:fe:be:0f:e2:06:
    36:a7:bc:82:a1:95:10:92:b2:02:0e:31:07:39:0b:
    a5:04:5d:fd:14:24:ba:e0:84:ba:53:ef:41:68:c2:
    12:fb:ba:55:ec:e9:59:77:ef:17:ff:8b:88:95:08:
    aa:ef:d0:cf:e1:84:a1:c8:8e:07:ea:07:e7:e3:4e:
    f2:2d:45:04:4e:9c:8e:22:4a:5f:69:35:ce:13:1e:
    a4:a1:08:cb:58:4f:5e:5c:9c:d4:c5:1d:b0:dd:8d:
    ac:d5
exponent1:
    73:91:8b:b1:d4:2f:c6:22:8c:1d:3c:26:d4:ea:f1:
    3e:f1:8f:7b:4c:5b:98:a0:1d:16:a6:7e:d6:72:41:
    13:80:9a:3e:e1:d0:ab:3d:14:7d:30:06:3b:59:33:
    66:dc:39:33:46:7a:82:6a:9b:72:99:f2:49:fe:da:
    bf:96:2e:db:59:42:d4:cc:04:55:63:85:c7:70:fc:
    d3:ec:c0:0f:5c:c1:24:f4:1e:4b:1e:11:d9:9a:f5:
    af:29:1e:9c:cf:db:3e:c9:89:59:3e:5b:cd:44:10:
    9a:1a:1e:af:29:a6:08:1a:3e:82:be:75:9e:b4:58:
    25:74:d4:de:e6:ff:21:42:03:50:a3:26:53:96:ef:
    be:98:96:a1:b2:7b:eb:3e:cc:3d:1f:56:2e:86:f2:
    28:97:0e:6b:fe:62:18:d8:68:65:ed:31:d5:ab:09:
    5c:70:df:62:f8:11:5d:23:ea:2d:c7:ae:a2:a4:07:
    05:c3:98:65:df:e3:68:3b:be:2b:19:76:8e:b4:b5:
    0b:53:da:57:82:0a:4b:2d:cf:41:81:b3:81:cd:7f:
    2c:ce:89:df:90:9d:37:c9:c9:73:e6:6e:c7:9c:21:
    51:ea:2a:ab:3c:88:82:aa:c3:62:96:f0:79:d5:61:
    41:9c:2f:67:e8:fc:2c:56:93:60:b4:36:70:11:a3:
    43
exponent2:
    00:b6:c0:79:ee:42:28:b4:e7:0c:d8:99:6b:f2:f2:
    9d:81:c6:a1:2c:ae:21:91:0b:2c:cc:8d:53:39:13:
    0b:0c:c7:dd:f0:74:a0:03:17:67:63:cf:d3:3f:a4:
    f5:54:ad:6a:0f:b0:25:8f:48:b3:22:d4:3c:50:9a:
    45:25:f8:3a:d0:de:da:dc:2f:b3:ea:86:ef:f2:7f:
    0e:2a:62:ad:4c:8e:75:5a:3a:17:19:30:9d:d4:0e:
    f9:4d:87:9e:0c:ee:46:ff:60:59:c9:c9:22:f6:4c:
    04:c5:03:9f:79:4d:b3:ff:3f:24:97:09:2e:d8:e6:
    4a:57:ba:b8:c2:f4:05:a6:77:18:ca:61:8e:b4:1e:
    58:b1:c6:5c:cb:b0:08:8d:e6:5e:d5:ac:65:2d:9b:
    4b:ff:fd:39:25:e7:e9:3e:3c:52:be:77:2a:00:35:
    44:63:f1:07:c3:07:55:1d:d1:db:0b:e6:05:99:09:
    cc:36:64:db:6d:63:69:d7:f3:b3:c3:be:e5:e9:9e:
    f2:a1:33:20:1d:c6:79:25:89:3d:43:95:72:fc:25:
    be:00:7a:38:16:ad:96:01:d3:04:aa:1d:f1:01:e2:
    ba:6c:b0:2e:72:75:85:09:b8:2f:ff:51:75:a5:8b:
    43:7f:b7:f8:d7:4c:e2:86:94:c3:32:93:c1:ba:a3:
    8e:61
coefficient:
    21:a7:90:ae:67:f2:5e:b2:2d:87:d8:86:e5:8c:bf:
    03:2f:7f:f2:b0:40:a5:a0:05:61:f6:cf:00:44:94:
    a9:6d:11:f4:bb:6d:f3:c3:46:44:a9:e9:00:85:82:
    b3:65:67:e2:0c:04:f2:a0:7b:8d:28:cb:81:21:40:
    22:ed:dc:3a:e8:88:95:43:4d:d7:36:4f:6b:4d:08:
    cb:04:71:b4:dd:29:8a:90:19:2c:1f:22:f5:28:fa:
    15:17:0a:e4:0f:51:d7:fe:ee:c7:d5:66:bb:6a:20:
    77:65:8b:4d:cd:9a:f5:46:d8:a1:c6:c0:bc:87:30:
    3f:e0:dc:e8:e0:67:5a:cd:4e:b0:d2:86:33:94:d0:
    80:3e:27:20:29:92:68:08:13:34:73:33:c2:a2:30:
    f2:12:a6:88:59:f7:88:85:b8:dd:50:75:c7:05:c4:
    6c:3e:87:78:db:3f:cc:95:85:4e:91:b4:75:2c:3f:
    b9:1f:9a:77:05:91:90:16:54:84:df:10:fd:ea:77:
    dc:46:fa:e3:22:81:1a:6d:66:b7:f6:ab:c0:38:0d:
    5f:76:79:a9:0e:cf:5d:4a:19:0a:41:69:33:04:d6:
    f3:bc:58:ae:1f:42:fd:ab:13:59:26:1f:ab:dd:40:
    d2:a3:e3:6a:e8:8e:3c:ab:92:46:75:98:ea:2f:3b:
    87
```

In the first command, the part that indicates that it is a CA certificate is the following:
```
X509v3 extensions:
    X509v3 Subject Key Identifier: 
        1C:DC:D3:1D:D5:33:C2:C4:0D:EF:1F:A5:E6:F6:79:A5:4D:0A:25:A7
    X509v3 Authority Key Identifier: 
        keyid:1C:DC:D3:1D:D5:33:C2:C4:0D:EF:1F:A5:E6:F6:79:A5:4D:0A:25:A7

    X509v3 Basic Constraints: critical
        CA:TRUE
```

This also shows that the certificate is self signed because the subject and the authority are the same.

The values are present in the output of the second command.

### Task 2

For this task, we want to create a certificate request. To do so, we need the follwoing command:

```
[01/12/22]seed@VM:~/.../Labsetup$ openssl req -newkey rsa:2048 -sha256 -keyout server.key -out server.csr -subj "/CN=www.bank32.com/O=Bank32 Inc./C=US" -passout pass:dees
Generating a RSA private key
................................+++++
...........+++++
writing new private key to 'server.key'
-----
```

Then, we ran the two following commands:

```
[01/12/22]seed@VM:~/.../Labsetup$ openssl req -in server.csr -text -noout
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN = www.bank32.com, O = Bank32 Inc., C = US
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:b6:b6:87:c7:0a:e7:da:8b:b7:4c:d4:af:01:cf:
                    1c:26:27:9c:0e:b5:97:64:1f:62:64:ee:73:af:25:
                    64:46:2b:23:25:9e:60:08:23:e6:9e:3c:4e:4c:c9:
                    a7:ed:9e:5d:9f:51:1f:61:4c:84:9a:65:db:49:0d:
                    bb:f8:cd:b5:13:d3:50:a3:e4:64:28:3e:1f:0f:fa:
                    de:c0:dc:d9:49:5d:51:bb:f0:79:e2:fc:89:db:39:
                    c3:6a:38:0a:4a:cb:2a:b2:6b:23:e8:53:2c:06:4a:
                    fc:ad:56:ca:80:d5:45:1f:da:5f:69:56:ea:65:28:
                    d1:bb:cc:50:db:6a:de:17:27:7e:5a:8a:2f:f3:45:
                    39:af:65:91:76:d2:53:ae:09:80:b7:ec:88:45:6f:
                    8e:cb:e1:52:80:79:0b:4d:12:70:a7:d8:82:9e:28:
                    70:b1:57:c9:f8:3f:0b:88:4c:22:81:45:54:06:82:
                    94:02:92:d9:a1:df:49:30:e1:b7:57:9d:1c:c0:69:
                    79:6f:ae:e8:4b:15:91:ed:d8:2a:bf:2e:b9:97:7a:
                    21:84:a4:2f:5e:5a:63:20:fb:c5:7b:55:78:fd:12:
                    26:7a:67:85:19:29:36:0b:e6:f1:8d:2b:b4:04:0b:
                    14:af:64:9b:e4:4c:32:9c:6a:d3:c3:30:44:0c:c0:
                    09:65
                Exponent: 65537 (0x10001)
        Attributes:
            a0:00
    Signature Algorithm: sha256WithRSAEncryption
         09:01:50:03:eb:c9:fc:c0:54:2b:f3:25:55:0c:86:e5:85:9d:
         bb:23:f2:41:79:6b:50:e4:c1:a5:70:9a:cb:f2:50:5f:c8:74:
         2a:9f:fc:e5:82:5e:67:46:e0:19:7e:86:e2:e1:7c:23:ac:02:
         1a:65:f8:7c:f1:dd:f9:bd:72:1b:34:d5:01:d8:21:6a:fb:df:
         f4:2b:97:41:2a:44:ec:b3:b3:ad:29:cf:c3:29:64:e6:a3:22:
         ef:4d:21:24:3d:53:7c:07:29:f2:5a:c6:7e:44:d5:31:fd:87:
         de:21:57:bb:7d:be:5b:67:08:56:0e:62:21:54:99:f7:0a:45:
         b7:b4:0d:e1:cb:de:61:5b:31:fd:0e:0d:56:42:cc:2e:c2:52:
         f5:e8:9c:52:f4:3d:67:5f:86:49:05:c8:c7:26:18:0c:cc:a1:
         0f:b2:fa:70:e8:87:06:d6:a0:72:db:37:c7:e4:8c:0a:36:44:
         25:05:08:c9:36:c8:ef:a0:32:42:0e:b3:e0:34:2e:f0:dc:98:
         7c:b7:4f:cc:ab:af:c4:66:8c:5e:ca:2b:a3:1d:78:fb:0b:ac:
         be:f7:b0:01:2a:9a:00:d8:56:ac:c4:90:1e:6b:d3:e2:d7:b3:
         1e:5f:3f:35:2c:3f:a6:ab:95:66:ee:a2:87:ae:bc:08:ec:3b:
         2c:2c:9d:42
```

```
[01/12/22]seed@VM:~/.../Labsetup$ openssl rsa -in server.key -text -noout
Enter pass phrase for server.key:
RSA Private-Key: (2048 bit, 2 primes)
modulus:
    00:b6:b6:87:c7:0a:e7:da:8b:b7:4c:d4:af:01:cf:
    1c:26:27:9c:0e:b5:97:64:1f:62:64:ee:73:af:25:
    64:46:2b:23:25:9e:60:08:23:e6:9e:3c:4e:4c:c9:
    a7:ed:9e:5d:9f:51:1f:61:4c:84:9a:65:db:49:0d:
    bb:f8:cd:b5:13:d3:50:a3:e4:64:28:3e:1f:0f:fa:
    de:c0:dc:d9:49:5d:51:bb:f0:79:e2:fc:89:db:39:
    c3:6a:38:0a:4a:cb:2a:b2:6b:23:e8:53:2c:06:4a:
    fc:ad:56:ca:80:d5:45:1f:da:5f:69:56:ea:65:28:
    d1:bb:cc:50:db:6a:de:17:27:7e:5a:8a:2f:f3:45:
    39:af:65:91:76:d2:53:ae:09:80:b7:ec:88:45:6f:
    8e:cb:e1:52:80:79:0b:4d:12:70:a7:d8:82:9e:28:
    70:b1:57:c9:f8:3f:0b:88:4c:22:81:45:54:06:82:
    94:02:92:d9:a1:df:49:30:e1:b7:57:9d:1c:c0:69:
    79:6f:ae:e8:4b:15:91:ed:d8:2a:bf:2e:b9:97:7a:
    21:84:a4:2f:5e:5a:63:20:fb:c5:7b:55:78:fd:12:
    26:7a:67:85:19:29:36:0b:e6:f1:8d:2b:b4:04:0b:
    14:af:64:9b:e4:4c:32:9c:6a:d3:c3:30:44:0c:c0:
    09:65
publicExponent: 65537 (0x10001)
privateExponent:
    49:6a:2c:42:58:ea:72:50:e3:54:f6:bc:5f:10:b5:
    f1:ca:c6:94:ce:78:47:1d:a9:2e:7e:f5:72:b1:a6:
    89:df:39:5f:1b:34:e0:f0:73:f0:ae:b0:93:80:0f:
    7e:95:bc:6e:90:6c:f8:6e:83:75:7a:69:d2:ff:b6:
    c0:b0:ff:0a:39:45:54:a5:27:6d:58:10:a9:1e:17:
    35:0d:48:2d:87:56:99:1a:76:0f:33:83:bc:d7:87:
    e2:7d:23:fd:8b:86:db:6b:db:60:b5:52:a2:30:ad:
    38:85:00:17:26:1a:81:43:00:45:56:4c:16:5b:81:
    72:61:15:38:24:c7:9a:2b:71:77:13:96:ba:98:c1:
    b4:38:bc:f9:e8:58:81:72:b6:de:c2:8a:75:8d:3f:
    a7:49:44:1a:e6:fc:d5:a7:af:db:0d:e7:83:a1:5f:
    72:76:b7:84:f1:83:9f:c5:58:0e:cb:9f:3e:ba:03:
    53:69:17:c8:f5:dc:10:9b:43:99:28:2f:f4:e8:af:
    5e:7b:ca:81:ea:6e:0e:fb:be:75:63:ec:cc:c9:62:
    6a:e6:65:18:8f:50:c8:d8:6f:a8:ba:2d:5b:2e:e0:
    2d:11:b5:1b:26:4b:94:96:1a:b5:c9:b4:5c:48:96:
    6b:fb:74:bf:23:aa:48:11:50:7e:b7:ad:9d:df:cc:
    81
prime1:
    00:d9:0c:d8:4e:27:48:4f:4e:37:ff:ef:e5:99:dc:
    70:73:ce:26:49:11:8e:ca:7c:2f:77:bb:f4:20:74:
    e1:28:32:71:c9:f3:ea:27:0b:58:fc:5f:2b:cf:12:
    2d:bb:27:a5:53:ea:a4:e7:b3:66:65:55:bd:fd:97:
    cc:be:97:b1:31:ea:e3:b9:8d:62:db:28:1a:62:6a:
    ec:4f:e6:e0:1f:63:0f:fb:66:f3:6c:a7:db:d2:af:
    cb:cc:dc:b2:8b:a6:69:6c:77:4f:c6:1f:d1:55:a3:
    f0:ed:8f:b9:56:d6:88:4e:dc:53:ab:93:43:66:47:
    9e:37:17:bf:f7:56:5b:a7:45
prime2:
    00:d7:80:41:af:ba:83:70:d2:05:c4:21:b3:28:f5:
    64:0b:82:37:29:60:6c:e6:fe:30:74:a8:dc:38:63:
    46:64:bb:4d:5c:9d:84:ce:c7:36:6b:b9:48:59:86:
    be:3a:ab:07:05:30:9c:00:bc:d4:67:4a:10:13:f9:
    d6:95:fe:3f:c3:ef:d5:2c:33:6c:30:ef:40:c1:00:
    61:8a:6f:99:ea:00:b6:91:98:7e:fe:dc:71:95:1d:
    de:ea:bc:4e:f8:5e:7b:95:e5:8f:3e:22:6c:4b:6e:
    cc:62:77:4b:34:29:8b:7e:f5:38:30:09:3e:ea:19:
    fc:bd:05:e3:1b:e7:8a:6b:a1
exponent1:
    00:85:3a:e1:3b:77:d9:66:f4:b8:63:1d:ba:6d:eb:
    66:0b:6f:ab:08:87:02:83:40:1f:52:fb:c8:2a:74:
    14:11:3c:85:a4:55:58:91:86:e1:a4:68:36:d7:f0:
    6c:a9:c8:f8:2e:be:85:62:c4:38:42:53:93:3f:aa:
    82:3f:2b:95:d4:f2:3d:be:94:0e:ee:3f:7b:92:95:
    d7:60:64:73:86:50:a4:6a:c9:12:fa:cb:3e:9f:e0:
    d0:d4:7b:54:0d:6c:a4:a1:b3:ca:ff:ee:5f:ec:95:
    a9:39:e9:52:f6:fe:d0:c4:b7:71:94:8b:dc:7f:57:
    ce:c2:3a:8d:d7:20:e7:39:91
exponent2:
    21:b0:1e:14:9f:7e:8e:b3:76:4d:4b:cb:5b:1a:c9:
    51:f7:40:32:4a:ad:9b:8a:9e:fe:8d:ab:27:71:75:
    7e:a7:bd:17:3e:54:95:92:94:d2:50:3b:9c:2b:31:
    2f:b0:ae:bf:43:f3:0f:36:75:a9:d3:ed:21:82:4b:
    e6:54:c1:99:1a:b3:e3:5e:02:8a:bf:cc:0a:9f:c9:
    9f:bf:84:7b:0d:33:7d:1d:2e:b5:1e:b6:ee:cd:a5:
    9c:62:65:a1:f3:fb:33:da:98:02:e9:94:ae:52:1a:
    c7:45:c8:ce:d5:b3:c5:dc:05:b5:94:ac:6e:22:33:
    dd:44:bf:55:0c:64:1a:21
coefficient:
    00:a9:f7:dc:6b:5b:51:01:af:45:55:6a:ee:51:5f:
    71:d6:0d:81:5f:fc:9b:cd:e5:73:1d:ec:d2:9a:12:
    04:ab:ad:76:4f:8a:ce:26:d9:7e:27:0e:de:d5:d5:
    6a:6d:8c:4e:d9:c5:e8:06:f0:4d:cb:a1:aa:b9:18:
    b5:4a:29:cd:9c:1f:e5:43:63:42:cb:d0:76:6b:ff:
    79:70:a6:9b:30:8c:66:b0:e3:99:cf:ba:88:65:da:
    b2:34:7f:5d:20:bb:63:46:c6:d7:3c:05:05:72:2f:
    e4:73:4d:d9:6b:aa:07:44:db:0a:ba:08:7b:f5:fd:
    50:ee:64:00:f1:e6:d9:52:30
```

After this, we added two alternative names:
```
[01/12/22]seed@VM:~/.../Labsetup$ openssl req -newkey rsa:2048 -sha256 -keyout server.key -out server.csr -subj "/CN=www.m08g05.com/O=m08g05 Inc./C=PT" -passout pass:dees -addext "subjectAltName = DNS:www.m08g05.com, DNS:www.m08g05A.com, DNS:www.m08g05B.com"
Generating a RSA private key
.........................................................................+++++
..............+++++
writing new private key to 'server.key'
-----
```

### Task 3

In this task, we need to use the CA to sign the certificate request. For that, we run the follwoing command:
```
[01/12/22]seed@VM:~/.../Labsetup$ openssl ca -config myCA_openssl.cnf -policy policy_anything -md sha256 -days 3650 -in server.csr -out server.crt -batch -cert ca.crt -keyfile ca.key
Using configuration from myCA_openssl.cnf
Enter pass phrase for ca.key:
Check that the request matches the signature
Signature ok
Certificate Details:
        Serial Number: 4097 (0x1001)
        Validity
            Not Before: Jan 12 09:58:51 2022 GMT
            Not After : Jan 10 09:58:51 2032 GMT
        Subject:
            countryName               = PT
            organizationName          = m08g05 Inc.
            commonName                = www.m08g05.com
        X509v3 extensions:
            X509v3 Basic Constraints: 
                CA:FALSE
            Netscape Comment: 
                OpenSSL Generated Certificate
            X509v3 Subject Key Identifier: 
                F8:D9:26:BA:4D:D5:57:36:41:16:A7:65:E5:65:4E:54:67:B9:6B:02
            X509v3 Authority Key Identifier: 
                keyid:1C:DC:D3:1D:D5:33:C2:C4:0D:EF:1F:A5:E6:F6:79:A5:4D:0A:25:A7

            X509v3 Subject Alternative Name: 
                DNS:www.m08g05.com, DNS:www.m08g05A.com, DNS:www.m08g05B.com
Certificate is to be certified until Jan 10 09:58:51 2032 GMT (3650 days)

Write out database with 1 new entries
Data Base Updated
```

After that, we run the following command:
```
[01/12/22]seed@VM:~/.../Labsetup$ openssl x509 -in server.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 4097 (0x1001)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = PT, ST = Porto, L = Porto, O = FEUP, OU = FSI, CN = ooga
        Validity
            Not Before: Jan 12 09:58:51 2022 GMT
            Not After : Jan 10 09:58:51 2032 GMT
        Subject: C = PT, O = m08g05 Inc., CN = www.m08g05.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:b7:88:b4:59:e9:8e:94:34:62:4f:c4:47:56:32:
                    23:db:bd:82:22:d8:d6:2e:02:07:7c:82:1a:c0:2d:
                    c8:93:9b:0b:0a:13:db:dd:6e:e3:38:95:97:a2:db:
                    a0:0a:4a:64:da:c7:b0:a5:14:80:75:58:59:2e:f6:
                    af:63:ca:3c:6c:dc:34:a4:1e:2a:13:20:7f:85:84:
                    77:0d:2c:04:2f:ef:6d:d1:47:87:93:1a:d6:69:02:
                    39:1f:15:f0:bf:1b:8e:9e:a6:48:5b:2d:66:cd:6e:
                    02:d3:07:a1:95:30:a6:75:8c:12:69:b2:95:de:fc:
                    05:5b:cf:50:67:57:64:26:dd:03:c8:b4:58:fe:13:
                    6c:7f:a7:6f:e8:8a:84:2d:13:8e:47:d8:b1:e1:47:
                    46:c6:0e:2b:15:08:80:d1:49:e8:e2:a6:19:82:70:
                    b2:32:4d:75:a6:64:79:24:e4:b1:7c:9c:18:95:0d:
                    b3:58:ff:fe:8e:df:52:67:bc:43:0b:ff:88:27:5f:
                    d4:34:b4:30:71:32:ac:c1:70:32:e6:42:89:2b:11:
                    20:25:f5:62:e8:c1:f0:a1:e0:42:be:e5:b7:cf:58:
                    d7:0f:75:b1:09:57:5f:b3:6d:87:a2:a2:f1:f6:ff:
                    2c:e3:a9:4b:56:df:87:70:ad:bc:a8:9f:e5:e3:aa:
                    ea:df
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints: 
                CA:FALSE
            Netscape Comment: 
                OpenSSL Generated Certificate
            X509v3 Subject Key Identifier: 
                F8:D9:26:BA:4D:D5:57:36:41:16:A7:65:E5:65:4E:54:67:B9:6B:02
            X509v3 Authority Key Identifier: 
                keyid:1C:DC:D3:1D:D5:33:C2:C4:0D:EF:1F:A5:E6:F6:79:A5:4D:0A:25:A7

            X509v3 Subject Alternative Name: 
                DNS:www.m08g05.com, DNS:www.m08g05A.com, DNS:www.m08g05B.com
    Signature Algorithm: sha256WithRSAEncryption
         67:d3:39:5d:a2:d7:5d:0e:c8:b0:2c:7f:75:4a:7d:2c:cb:21:
         2b:f0:7c:0d:4b:d3:10:48:21:0e:8b:74:64:91:09:51:5e:63:
         25:5e:34:4c:2a:3e:44:4b:ec:d1:72:09:60:d1:97:88:f3:cd:
         d0:b6:db:f3:9d:3f:ba:67:aa:ce:c9:0f:57:f5:55:92:83:d5:
         1a:53:cd:dd:7c:61:7a:a5:9a:7c:c9:4d:7e:da:6d:8e:e7:6b:
         cf:e5:8d:b8:0b:6a:92:2c:11:07:66:b0:22:3d:3d:fe:d3:b0:
         59:7a:d6:5c:2f:8e:44:f1:f3:d0:7a:b7:4e:54:13:3f:c0:0f:
         21:10:54:b7:60:d3:9d:18:27:12:35:a6:78:f3:4f:1c:f1:b2:
         5a:9e:0d:5d:a2:9b:e9:0f:6b:9b:9a:a5:80:d9:fa:73:17:bb:
         bb:bb:02:09:e8:59:4f:2b:23:8b:8d:56:98:7c:e8:95:39:ea:
         01:d5:32:1b:7b:f0:18:74:e2:ce:93:0d:93:86:09:e7:d5:f4:
         cf:fd:14:39:4f:93:9d:0b:92:a2:66:67:68:b4:52:75:5d:08:
         6c:32:c4:28:48:93:07:14:14:a6:c8:54:91:ee:c3:9a:95:38:
         38:46:ea:08:bf:66:a0:e3:30:bb:21:c8:46:db:93:e2:1e:8e:
         52:c2:6f:bb:62:37:15:b0:74:1c:f7:56:b2:80:2d:98:a0:28:
         d8:d9:1f:9c:dc:77:74:23:7f:8d:47:08:0f:97:09:3f:68:a8:
         c6:80:c8:b0:c3:eb:28:e8:6c:96:c2:ae:97:76:6a:ee:c4:f9:
         fb:75:cb:97:8e:22:78:0e:80:2b:05:75:d9:79:6d:cf:cd:c2:
         4e:7b:95:29:a2:29:d2:f9:ca:ca:ac:d8:a8:26:37:43:5b:77:
         6c:a7:04:0d:fd:1d:17:b0:e7:94:28:34:fa:ab:e3:c2:b4:c4:
         22:13:9c:84:ae:e4:ba:32:9e:40:27:68:e1:da:4d:57:08:5d:
         af:83:ea:f9:c2:a0:43:e7:d1:fc:a8:f7:d8:c5:83:04:9f:ac:
         96:c4:28:b7:4f:20:8f:63:84:b9:45:0d:19:ff:28:22:e5:81:
         48:04:8d:93:f8:c5:eb:eb:6b:01:ee:90:4b:1a:03:37:25:6e:
         13:f0:65:8d:8b:6e:09:8c:8f:9c:ef:53:5f:ba:32:4b:d6:7e:
         3c:e5:a1:60:42:30:99:fc:04:72:58:9a:75:95:11:97:f1:03:
         a3:65:f2:36:3f:d3:82:14:45:e0:6f:4e:80:1e:13:58:3b:db:
         98:bd:31:f3:da:9a:1e:2d:3a:1f:b9:13:a3:65:fb:5e:c1:18:
         55:43:64:36:06:dd:3e:97
```

As we can, the alternative names are included.

### Task 4

In this task, we will set up our own website.

To start of, we need to copy owr server certificates and create the configuration file for the Apache server:
```
<VirtualHost *:443> 
    DocumentRoot /var/www/m08g05
    ServerName www.m08g05.com
    ServerAlias www.m08g05A.com
    ServerAlias www.m08g05B.com
    DirectoryIndex index.html
    SSLEngine On 
    SSLCertificateFile /certs/m08g05.crt
    SSLCertificateKeyFile /certs/m08g05.key
</VirtualHost>

<VirtualHost *:80> 
    DocumentRoot /var/www/m08g05
    ServerName www.m08g05.com
    DirectoryIndex index_red.html
</VirtualHost>

# Set the following gloal entry to suppress an annoying warning message
ServerName localhost
```

After that, we needed to change the `Dockerfile` so that it loads our website and copies our configuration files.

When we try to go to the https://m08g05.com the browser gives us a warning.

To solve this, we need to add our CA to the trusted authorities of the browser. After adding it, we can successfully enter our server.

### Task 5

### Task 6

