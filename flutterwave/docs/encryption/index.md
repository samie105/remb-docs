---
title: "Encryption"
source: "https://developer.flutterwave.com/docs/encryption"
canonical_url: "https://developer.flutterwave.com/docs/encryption"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:30:14.472Z"
content_hash: "dcd0c0e02097f1fe3529bbc3ff23bc11d4b5f2d1b90de51dc5853a450f1cd01e"
menu_path: ["Encryption"]
section_path: []
tab_variants: ["Node.js","Java","Python"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/api-headers/index.md", "title": "Supported Request Headers"}
nav_next: {"path": "flutterwave/docs/common-errors/index.md", "title": "Errors"}
---

When making a card charge request, you **must encrypt** the card information before sending the request.

> ## 🚧
> 
> If you're using any of our official backend SDKs, you don't need to handle encryption manually. Pass your [encryption key](../environments/index.md#retrieve-test-api-credentials) to the library, and it will automatically encrypt your request payload.

When integrating with our direct charge APIs, you'll need to handle the encryption of your code to ensure data integrity. Follow these steps to encrypt your request properly:

1.  Retrieve your encryption key from the **API settings** section in your Flutterwave dashboard.
2.  Use the Advanced Encryption Standard (`AES 256`) to encrypt your request. This is extended via the following libraries:
    1.  Node.js: `node-forge`, `crypto`, `crypto-js`
    2.  Python: `pycryptodome`, `cryptography`
    3.  Java: `JCE`(from `javax.crypto`)
    4.  PHP: `openssl`, `libsodium`
3.  Add the encrypted data to your API requests.

#### Node.js

```javascript
export async function encryptAES(data: string, token: string, nonce: string): Promise<string> {
    if (nonce.length !== 12) {
        throw new Error("Nonce must be exactly 12 characters long");
    }

    const cryptoSubtle = globalThis.crypto?.subtle || require("crypto").webcrypto?.subtle;
    if (!cryptoSubtle) {
        throw new Error("Crypto API is not available in this environment.");
    }

    const decodedKeyBytes = Uint8Array.from(atob(token), c => c.charCodeAt(0));

    const key = await cryptoSubtle.importKey(
        "raw",
        decodedKeyBytes,
        { name: "AES-GCM" },
        false,
        ["encrypt"]
    );
    const iv = new TextEncoder().encode(nonce);

    const encryptedData = await cryptoSubtle.encrypt(
        {
            name: "AES-GCM",
            iv: iv,
        },
        key,
        new TextEncoder().encode(data)
    );

    return btoa(String.fromCharCode(...new Uint8Array(encryptedData)));
}
```

```java
public class EncryptionService {

    private static final String AES = "AES";
    private static final String AES_ALGORITHM = "AES/GCM/NoPadding";
    private static final int TAG_LENGTH_BIT = 128;

    static String encrypt(String plainText, String nonce, String b64EncodedKey) throws NoSuchPaddingException, NoSuchAlgorithmException, InvalidAlgorithmParameterException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {
        if (plainText.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid plainText");
        }
        if (b64EncodedKey.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid b64EncodedAESKey");
        }
        if (nonce.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid nonce");
        }

        Cipher cipher = Cipher.getInstance(AES_ALGORITHM);
        GCMParameterSpec gcmSpec = new GCMParameterSpec(TAG_LENGTH_BIT, nonce.getBytes());
        byte[] decodedKeyBytes = Base64.getDecoder().decode(b64EncodedKey);
        SecretKey key = new SecretKeySpec(decodedKeyBytes, AES);
        cipher.init(Cipher.ENCRYPT_MODE, key, gcmSpec);
        byte[] encryptedBytes = cipher.doFinal(plainText.getBytes());

        return Base64.getEncoder().encodeToString(encryptedBytes);
    }

    public static String generateNonce(int length) {
        return new Random().ints(length, 0, 62)
                .mapToObj("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"::charAt)
                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                .toString();
    }
}
```

```python
import base64
import secrets
import string
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class AESEncryptor:
    def __init__(self, encryption_key: str):
        self.aes_key = base64.b64decode(encryption_key)

    @staticmethod
    def generate_nonce(length: int = 12) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(length))

    def encrypt(self, plain_text: str, nonce: str) -> str:
        if not plain_text or not nonce:
            raise ValueError('Both plain_text and nonce are required for encryption.')

        nonce_bytes = nonce.encode()
        aes_gcm = AESGCM(self.aes_key)
        cipher_text = aes_gcm.encrypt(nonce_bytes, plain_text.encode(), None)

        return base64.b64encode(cipher_text).decode()

    def encrypt_dict(self, data: dict) -> dict:
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        nonce = self.generate_nonce()
        encrypted_data = {"nonce": nonce}

        for key, value in data.items():
            encrypted_data[key] = self.encrypt(str(value), nonce)

        return encrypted_data
```

#### Java

```javascript
export async function encryptAES(data: string, token: string, nonce: string): Promise<string> {
    if (nonce.length !== 12) {
        throw new Error("Nonce must be exactly 12 characters long");
    }

    const cryptoSubtle = globalThis.crypto?.subtle || require("crypto").webcrypto?.subtle;
    if (!cryptoSubtle) {
        throw new Error("Crypto API is not available in this environment.");
    }

    const decodedKeyBytes = Uint8Array.from(atob(token), c => c.charCodeAt(0));

    const key = await cryptoSubtle.importKey(
        "raw",
        decodedKeyBytes,
        { name: "AES-GCM" },
        false,
        ["encrypt"]
    );
    const iv = new TextEncoder().encode(nonce);

    const encryptedData = await cryptoSubtle.encrypt(
        {
            name: "AES-GCM",
            iv: iv,
        },
        key,
        new TextEncoder().encode(data)
    );

    return btoa(String.fromCharCode(...new Uint8Array(encryptedData)));
}
```

```java
public class EncryptionService {

    private static final String AES = "AES";
    private static final String AES_ALGORITHM = "AES/GCM/NoPadding";
    private static final int TAG_LENGTH_BIT = 128;

    static String encrypt(String plainText, String nonce, String b64EncodedKey) throws NoSuchPaddingException, NoSuchAlgorithmException, InvalidAlgorithmParameterException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {
        if (plainText.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid plainText");
        }
        if (b64EncodedKey.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid b64EncodedAESKey");
        }
        if (nonce.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid nonce");
        }

        Cipher cipher = Cipher.getInstance(AES_ALGORITHM);
        GCMParameterSpec gcmSpec = new GCMParameterSpec(TAG_LENGTH_BIT, nonce.getBytes());
        byte[] decodedKeyBytes = Base64.getDecoder().decode(b64EncodedKey);
        SecretKey key = new SecretKeySpec(decodedKeyBytes, AES);
        cipher.init(Cipher.ENCRYPT_MODE, key, gcmSpec);
        byte[] encryptedBytes = cipher.doFinal(plainText.getBytes());

        return Base64.getEncoder().encodeToString(encryptedBytes);
    }

    public static String generateNonce(int length) {
        return new Random().ints(length, 0, 62)
                .mapToObj("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"::charAt)
                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                .toString();
    }
}
```

```python
import base64
import secrets
import string
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class AESEncryptor:
    def __init__(self, encryption_key: str):
        self.aes_key = base64.b64decode(encryption_key)

    @staticmethod
    def generate_nonce(length: int = 12) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(length))

    def encrypt(self, plain_text: str, nonce: str) -> str:
        if not plain_text or not nonce:
            raise ValueError('Both plain_text and nonce are required for encryption.')

        nonce_bytes = nonce.encode()
        aes_gcm = AESGCM(self.aes_key)
        cipher_text = aes_gcm.encrypt(nonce_bytes, plain_text.encode(), None)

        return base64.b64encode(cipher_text).decode()

    def encrypt_dict(self, data: dict) -> dict:
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        nonce = self.generate_nonce()
        encrypted_data = {"nonce": nonce}

        for key, value in data.items():
            encrypted_data[key] = self.encrypt(str(value), nonce)

        return encrypted_data
```

#### Python

```javascript
export async function encryptAES(data: string, token: string, nonce: string): Promise<string> {
    if (nonce.length !== 12) {
        throw new Error("Nonce must be exactly 12 characters long");
    }

    const cryptoSubtle = globalThis.crypto?.subtle || require("crypto").webcrypto?.subtle;
    if (!cryptoSubtle) {
        throw new Error("Crypto API is not available in this environment.");
    }

    const decodedKeyBytes = Uint8Array.from(atob(token), c => c.charCodeAt(0));

    const key = await cryptoSubtle.importKey(
        "raw",
        decodedKeyBytes,
        { name: "AES-GCM" },
        false,
        ["encrypt"]
    );
    const iv = new TextEncoder().encode(nonce);

    const encryptedData = await cryptoSubtle.encrypt(
        {
            name: "AES-GCM",
            iv: iv,
        },
        key,
        new TextEncoder().encode(data)
    );

    return btoa(String.fromCharCode(...new Uint8Array(encryptedData)));
}
```

```java
public class EncryptionService {

    private static final String AES = "AES";
    private static final String AES_ALGORITHM = "AES/GCM/NoPadding";
    private static final int TAG_LENGTH_BIT = 128;

    static String encrypt(String plainText, String nonce, String b64EncodedKey) throws NoSuchPaddingException, NoSuchAlgorithmException, InvalidAlgorithmParameterException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {
        if (plainText.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid plainText");
        }
        if (b64EncodedKey.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid b64EncodedAESKey");
        }
        if (nonce.isEmpty()) {
            throw new IllegalArgumentException("Must provide valid nonce");
        }

        Cipher cipher = Cipher.getInstance(AES_ALGORITHM);
        GCMParameterSpec gcmSpec = new GCMParameterSpec(TAG_LENGTH_BIT, nonce.getBytes());
        byte[] decodedKeyBytes = Base64.getDecoder().decode(b64EncodedKey);
        SecretKey key = new SecretKeySpec(decodedKeyBytes, AES);
        cipher.init(Cipher.ENCRYPT_MODE, key, gcmSpec);
        byte[] encryptedBytes = cipher.doFinal(plainText.getBytes());

        return Base64.getEncoder().encodeToString(encryptedBytes);
    }

    public static String generateNonce(int length) {
        return new Random().ints(length, 0, 62)
                .mapToObj("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"::charAt)
                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                .toString();
    }
}
```

```python
import base64
import secrets
import string
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class AESEncryptor:
    def __init__(self, encryption_key: str):
        self.aes_key = base64.b64decode(encryption_key)

    @staticmethod
    def generate_nonce(length: int = 12) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(length))

    def encrypt(self, plain_text: str, nonce: str) -> str:
        if not plain_text or not nonce:
            raise ValueError('Both plain_text and nonce are required for encryption.')

        nonce_bytes = nonce.encode()
        aes_gcm = AESGCM(self.aes_key)
        cipher_text = aes_gcm.encrypt(nonce_bytes, plain_text.encode(), None)

        return base64.b64encode(cipher_text).decode()

    def encrypt_dict(self, data: dict) -> dict:
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        nonce = self.generate_nonce()
        encrypted_data = {"nonce": nonce}

        for key, value in data.items():
            encrypted_data[key] = self.encrypt(str(value), nonce)

        return encrypted_data
```

```json
{
   "amount":150,
   "currency":"NGN",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "customer":{
      "email":"kod@gmail.com"
   },
   "payment_method":{
      "type":"card",
      "card": {
        "nonce": "{{RANDOMLY_GENERATED_NONCE}}",
        "encrypted_expiry_month": "sQpvQEb7GrUCjPuEN/NmHiPl",
        "encrypted_expiry_year": "sgHNEDkJ/RmwuWWq/RymToU5",
        "encrypted_card_number": "sAE3hEDaDQ+yLzo4Py+Lx15OZjBGduHu/DcdILh3En0=",
        "encrypted_cvv": "tAUzH7Qjma7diGdi7938F/ESNA=="
      }
   }
}
```

If you send unencrypted or improperly encrypted card details in your request, we'll return a `422` error with a failed encryption error message.

```json
{
    "status": "failed",
    "error": {
        "type": "CLIENT_ENCRYPTION_ERROR",
        "code": "11100",
        "message": "Unable to decrypt encrypted fields provided",
        "validation_errors": []
    }
}
```

Updated 5 months ago

* * *
