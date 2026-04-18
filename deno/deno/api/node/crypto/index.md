---
title: "crypto - Node documentation"
source: "https://docs.deno.com/api/node/crypto/"
canonical_url: "https://docs.deno.com/api/node/crypto/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:25.598Z"
content_hash: "d10eacaf1ea94d2670c99e93c0b14dca2e2e143f269017c3f19413f7194848d1"
menu_path: ["crypto - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/console/index.md", "title": "console - Node documentation"}
nav_next: {"path": "deno/deno/api/node/dgram/index.md", "title": "dgram - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:crypto";
```

The `node:crypto` module provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

```js
const { createHmac } = await import('node:crypto');

const secret = 'abcdefg';
const hash = createHmac('sha256', secret)
               .update('I love cupcakes')
               .digest('hex');
console.log(hash);
// Prints:
//   c0fa1bc00531bd78ef38c628449c5102aeabd49b5dc3a2a516ea6ea959d6658e
```

### Classes [#](#Classes)

c

[Certificate](.././crypto/~/Certificate "Certificate")

No documentation available

*   [exportChallenge](.././crypto/~/Certificate#method_exportchallenge_0)
*   [exportPublicKey](.././crypto/~/Certificate#method_exportpublickey_0)
*   [verifySpkac](.././crypto/~/Certificate#method_verifyspkac_0)

c

[Cipher](.././crypto/~/Cipher "Cipher")

Instances of the `Cipher` class are used to encrypt data. The class can be used in one of two ways:

*   [final](.././crypto/~/Cipher#method_final_0)
*   [setAutoPadding](.././crypto/~/Cipher#method_setautopadding_0)
*   [update](.././crypto/~/Cipher#method_update_0)

c

[Decipher](.././crypto/~/Decipher "Decipher")

Instances of the `Decipher` class are used to decrypt data. The class can be used in one of two ways:

*   [final](.././crypto/~/Decipher#method_final_0)
*   [setAutoPadding](.././crypto/~/Decipher#method_setautopadding_0)
*   [update](.././crypto/~/Decipher#method_update_0)

c

[DiffieHellman](.././crypto/~/DiffieHellman "DiffieHellman")

The `DiffieHellman` class is a utility for creating Diffie-Hellman key exchanges.

*   [computeSecret](.././crypto/~/DiffieHellman#method_computesecret_0)
*   [generateKeys](.././crypto/~/DiffieHellman#method_generatekeys_0)
*   [getGenerator](.././crypto/~/DiffieHellman#method_getgenerator_0)
*   [getPrime](.././crypto/~/DiffieHellman#method_getprime_0)
*   [getPrivateKey](.././crypto/~/DiffieHellman#method_getprivatekey_0)
*   [getPublicKey](.././crypto/~/DiffieHellman#method_getpublickey_0)
*   [setPrivateKey](.././crypto/~/DiffieHellman#method_setprivatekey_0)
*   [setPublicKey](.././crypto/~/DiffieHellman#method_setpublickey_0)
*   [verifyError](.././crypto/~/DiffieHellman#property_verifyerror)

c

[ECDH](.././crypto/~/ECDH "ECDH")

No documentation available

*   [computeSecret](.././crypto/~/ECDH#method_computesecret_0)
*   [convertKey](.././crypto/~/ECDH#method_convertkey_0)
*   [generateKeys](.././crypto/~/ECDH#method_generatekeys_0)
*   [getPrivateKey](.././crypto/~/ECDH#method_getprivatekey_0)
*   [getPublicKey](.././crypto/~/ECDH#method_getpublickey_0)
*   [setPrivateKey](.././crypto/~/ECDH#method_setprivatekey_0)

c

[Hash](.././crypto/~/Hash "Hash")

The `Hash` class is a utility for creating hash digests of data. It can be used in one of two ways:

*   [copy](.././crypto/~/Hash#method_copy_0)
*   [digest](.././crypto/~/Hash#method_digest_0)
*   [update](.././crypto/~/Hash#method_update_0)

c

[KeyObject](.././crypto/~/KeyObject "KeyObject")

No documentation available

*   [asymmetricKeyDetails](.././crypto/~/KeyObject#property_asymmetrickeydetails)
*   [asymmetricKeyType](.././crypto/~/KeyObject#property_asymmetrickeytype)
*   [equals](.././crypto/~/KeyObject#method_equals_0)
*   [export](.././crypto/~/KeyObject#method_export_0)
*   [from](.././crypto/~/KeyObject#method_from_0)
*   [symmetricKeySize](.././crypto/~/KeyObject#property_symmetrickeysize)
*   [toCryptoKey](.././crypto/~/KeyObject#method_tocryptokey_0)
*   [type](.././crypto/~/KeyObject#property_type)

c

[Sign](.././crypto/~/Sign "Sign")

No documentation available

*   [sign](.././crypto/~/Sign#method_sign_0)
*   [update](.././crypto/~/Sign#method_update_0)

c

[Verify](.././crypto/~/Verify "Verify")

The `Verify` class is a utility for verifying signatures. It can be used in one of two ways:

*   [update](.././crypto/~/Verify#method_update_0)
*   [verify](.././crypto/~/Verify#method_verify_0)

c

[X509Certificate](.././crypto/~/X509Certificate "X509Certificate")

Encapsulates an X509 certificate and provides read-only access to its information.

*   [ca](.././crypto/~/X509Certificate#property_ca)
*   [checkEmail](.././crypto/~/X509Certificate#method_checkemail_0)
*   [checkHost](.././crypto/~/X509Certificate#method_checkhost_0)
*   [checkIP](.././crypto/~/X509Certificate#method_checkip_0)
*   [checkIssued](.././crypto/~/X509Certificate#method_checkissued_0)
*   [checkPrivateKey](.././crypto/~/X509Certificate#method_checkprivatekey_0)
*   [fingerprint](.././crypto/~/X509Certificate#property_fingerprint)
*   [fingerprint256](.././crypto/~/X509Certificate#property_fingerprint256)
*   [fingerprint512](.././crypto/~/X509Certificate#property_fingerprint512)
*   [infoAccess](.././crypto/~/X509Certificate#property_infoaccess)
*   [issuer](.././crypto/~/X509Certificate#property_issuer)
*   [issuerCertificate](.././crypto/~/X509Certificate#property_issuercertificate)
*   [keyUsage](.././crypto/~/X509Certificate#property_keyusage)
*   [publicKey](.././crypto/~/X509Certificate#property_publickey)
*   [raw](.././crypto/~/X509Certificate#property_raw)
*   [serialNumber](.././crypto/~/X509Certificate#property_serialnumber)
*   [subject](.././crypto/~/X509Certificate#property_subject)
*   [subjectAltName](.././crypto/~/X509Certificate#property_subjectaltname)
*   [toJSON](.././crypto/~/X509Certificate#method_tojson_0)
*   [toLegacyObject](.././crypto/~/X509Certificate#method_tolegacyobject_0)
*   [toString](.././crypto/~/X509Certificate#method_tostring_0)
*   [validFrom](.././crypto/~/X509Certificate#property_validfrom)
*   [validFromDate](.././crypto/~/X509Certificate#property_validfromdate)
*   [validTo](.././crypto/~/X509Certificate#property_validto)
*   [validToDate](.././crypto/~/X509Certificate#property_validtodate)
*   [verify](.././crypto/~/X509Certificate#method_verify_0)

c

[Hmac](.././crypto/~/Hmac "Hmac")

The `Hmac` class is a utility for creating cryptographic HMAC digests. It can be used in one of two ways:

*   [digest](.././crypto/~/Hmac#method_digest_0)
*   [update](.././crypto/~/Hmac#method_update_0)

### Functions [#](#Functions)

f

[checkPrime](.././crypto/~/checkPrime "checkPrime")

Checks the primality of the `candidate`.

f

[checkPrimeSync](.././crypto/~/checkPrimeSync "checkPrimeSync")

Checks the primality of the `candidate`.

f

[createCipheriv](.././crypto/~/createCipheriv "createCipheriv")

Creates and returns a `Cipher` object, with the given `algorithm`, `key` and initialization vector (`iv`).

f

[createDecipheriv](.././crypto/~/createDecipheriv "createDecipheriv")

Creates and returns a `Decipher` object that uses the given `algorithm`, `key` and initialization vector (`iv`).

f

[createDiffieHellman](.././crypto/~/createDiffieHellman "createDiffieHellman")

Creates a `DiffieHellman` key exchange object using the supplied `prime` and an optional specific `generator`.

f

[createDiffieHellmanGroup](.././crypto/~/createDiffieHellmanGroup "createDiffieHellmanGroup")

An alias for [getDiffieHellman](.././crypto/~/getDiffieHellman)

f

[createECDH](.././crypto/~/createECDH "createECDH")

Creates an Elliptic Curve Diffie-Hellman (`ECDH`) key exchange object using a predefined curve specified by the `curveName` string. Use [getCurves](.././crypto/~/getCurves) to obtain a list of available curve names. On recent OpenSSL releases, `openssl ecparam -list_curves` will also display the name and description of each available elliptic curve.

f

[createHash](.././crypto/~/createHash "createHash")

Creates and returns a `Hash` object that can be used to generate hash digests using the given `algorithm`. Optional `options` argument controls stream behavior. For XOF hash functions such as `'shake256'`, the `outputLength` option can be used to specify the desired output length in bytes.

f

[createHmac](.././crypto/~/createHmac "createHmac")

Creates and returns an `Hmac` object that uses the given `algorithm` and `key`. Optional `options` argument controls stream behavior.

f

[createPrivateKey](.././crypto/~/createPrivateKey "createPrivateKey")

Creates and returns a new key object containing a private key. If `key` is a string or `Buffer`, `format` is assumed to be `'pem'`; otherwise, `key` must be an object with the properties described above.

f

[createPublicKey](.././crypto/~/createPublicKey "createPublicKey")

Creates and returns a new key object containing a public key. If `key` is a string or `Buffer`, `format` is assumed to be `'pem'`; if `key` is a `KeyObject` with type `'private'`, the public key is derived from the given private key; otherwise, `key` must be an object with the properties described above.

f

[createSecretKey](.././crypto/~/createSecretKey "createSecretKey")

Creates and returns a new key object containing a secret key for symmetric encryption or `Hmac`.

f

[createSign](.././crypto/~/createSign "createSign")

Creates and returns a `Sign` object that uses the given `algorithm`. Use [getHashes](.././crypto/~/getHashes) to obtain the names of the available digest algorithms. Optional `options` argument controls the `stream.Writable` behavior.

f

[createVerify](.././crypto/~/createVerify "createVerify")

Creates and returns a `Verify` object that uses the given algorithm. Use [getHashes](.././crypto/~/getHashes) to obtain an array of names of the available signing algorithms. Optional `options` argument controls the `stream.Writable` behavior.

f

[diffieHellman](.././crypto/~/diffieHellman "diffieHellman")

Computes the Diffie-Hellman secret based on a `privateKey` and a `publicKey`. Both keys must have the same `asymmetricKeyType`, which must be one of `'dh'` (for Diffie-Hellman), `'ec'` (for ECDH), `'x448'`, or `'x25519'` (for ECDH-ES).

f

[generateKey](.././crypto/~/generateKey "generateKey")

Asynchronously generates a new random secret key of the given `length`. The `type` will determine which validations will be performed on the `length`.

f

[generateKeyPair](.././crypto/~/generateKeyPair "generateKeyPair")

No documentation available

f

[generateKeyPairSync](.././crypto/~/generateKeyPairSync "generateKeyPairSync")

Generates a new asymmetric key pair of the given `type`. RSA, RSA-PSS, DSA, EC, Ed25519, Ed448, X25519, X448, and DH are currently supported.

f

[generateKeySync](.././crypto/~/generateKeySync "generateKeySync")

Synchronously generates a new random secret key of the given `length`. The `type` will determine which validations will be performed on the `length`.

f

[generatePrime](.././crypto/~/generatePrime "generatePrime")

No documentation available

f

[generatePrimeSync](.././crypto/~/generatePrimeSync "generatePrimeSync")

Generates a pseudorandom prime of `size` bits.

f

[getCipherInfo](.././crypto/~/getCipherInfo "getCipherInfo")

Returns information about a given cipher.

f

[getCiphers](.././crypto/~/getCiphers "getCiphers")

No documentation available

f

[getCurves](.././crypto/~/getCurves "getCurves")

No documentation available

f

[getDiffieHellman](.././crypto/~/getDiffieHellman "getDiffieHellman")

Creates a predefined `DiffieHellmanGroup` key exchange object. The supported groups are listed in the documentation for `DiffieHellmanGroup`.

f

[getFips](.././crypto/~/getFips "getFips")

No documentation available

f

[getHashes](.././crypto/~/getHashes "getHashes")

No documentation available

f

[getRandomValues](.././crypto/~/getRandomValues "getRandomValues")

A convenient alias for webcrypto.getRandomValues. This implementation is not compliant with the Web Crypto spec, to write web-compatible code use webcrypto.getRandomValues instead.

f

[hash](.././crypto/~/hash "hash")

A utility for creating one-shot hash digests of data. It can be faster than the object-based `crypto.createHash()` when hashing a smaller amount of data (<= 5MB) that's readily available. If the data can be big or if it is streamed, it's still recommended to use `crypto.createHash()` instead. The `algorithm` is dependent on the available algorithms supported by the version of OpenSSL on the platform. Examples are `'sha256'`, `'sha512'`, etc. On recent releases of OpenSSL, `openssl list -digest-algorithms` will display the available digest algorithms.

f

[hkdf](.././crypto/~/hkdf "hkdf")

HKDF is a simple key derivation function defined in RFC 5869. The given `ikm`, `salt` and `info` are used with the `digest` to derive a key of `keylen` bytes.

f

[hkdfSync](.././crypto/~/hkdfSync "hkdfSync")

Provides a synchronous HKDF key derivation function as defined in RFC 5869. The given `ikm`, `salt` and `info` are used with the `digest` to derive a key of `keylen` bytes.

f

[pbkdf2](.././crypto/~/pbkdf2 "pbkdf2")

Provides an asynchronous Password-Based Key Derivation Function 2 (PBKDF2) implementation. A selected HMAC digest algorithm specified by `digest` is applied to derive a key of the requested byte length (`keylen`) from the `password`, `salt` and `iterations`.

f

[pbkdf2Sync](.././crypto/~/pbkdf2Sync "pbkdf2Sync")

Provides a synchronous Password-Based Key Derivation Function 2 (PBKDF2) implementation. A selected HMAC digest algorithm specified by `digest` is applied to derive a key of the requested byte length (`keylen`) from the `password`, `salt` and `iterations`.

f

[privateDecrypt](.././crypto/~/privateDecrypt "privateDecrypt")

Decrypts `buffer` with `privateKey`. `buffer` was previously encrypted using the corresponding public key, for example using [publicEncrypt](.././crypto/~/publicEncrypt).

f

[privateEncrypt](.././crypto/~/privateEncrypt "privateEncrypt")

Encrypts `buffer` with `privateKey`. The returned data can be decrypted using the corresponding public key, for example using [publicDecrypt](.././crypto/~/publicDecrypt).

f

[pseudoRandomBytes](.././crypto/~/pseudoRandomBytes "pseudoRandomBytes")

No documentation available

f

[publicDecrypt](.././crypto/~/publicDecrypt "publicDecrypt")

No documentation available

f

[publicEncrypt](.././crypto/~/publicEncrypt "publicEncrypt")

Encrypts the content of `buffer` with `key` and returns a new `Buffer` with encrypted content. The returned data can be decrypted using the corresponding private key, for example using [privateDecrypt](.././crypto/~/privateDecrypt).

f

[randomBytes](.././crypto/~/randomBytes "randomBytes")

Generates cryptographically strong pseudorandom data. The `size` argument is a number indicating the number of bytes to generate.

f

[randomFill](.././crypto/~/randomFill "randomFill")

This function is similar to [randomBytes](.././crypto/~/randomBytes) but requires the first argument to be a `Buffer` that will be filled. It also requires that a callback is passed in.

f

[randomFillSync](.././crypto/~/randomFillSync "randomFillSync")

Synchronous version of [randomFill](.././crypto/~/randomFill).

f

[randomInt](.././crypto/~/randomInt "randomInt")

Return a random integer `n` such that `min <= n < max`. This implementation avoids [modulo bias](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Modulo_bias).

f

[randomUUID](.././crypto/~/randomUUID "randomUUID")

Generates a random [RFC 4122](https://www.rfc-editor.org/rfc/rfc4122.txt) version 4 UUID. The UUID is generated using a cryptographic pseudorandom number generator.

f

[scrypt](.././crypto/~/scrypt "scrypt")

Provides an asynchronous [scrypt](https://en.wikipedia.org/wiki/Scrypt) implementation. Scrypt is a password-based key derivation function that is designed to be expensive computationally and memory-wise in order to make brute-force attacks unrewarding.

f

[scryptSync](.././crypto/~/scryptSync "scryptSync")

Provides a synchronous [scrypt](https://en.wikipedia.org/wiki/Scrypt) implementation. Scrypt is a password-based key derivation function that is designed to be expensive computationally and memory-wise in order to make brute-force attacks unrewarding.

f

[secureHeapUsed](.././crypto/~/secureHeapUsed "secureHeapUsed")

No documentation available

f

[setEngine](.././crypto/~/setEngine "setEngine")

No documentation available

f

[setFips](.././crypto/~/setFips "setFips")

Enables the FIPS compliant crypto provider in a FIPS-enabled Node.js build. Throws an error if FIPS mode is not available.

f

[sign](.././crypto/~/sign "sign")

Calculates and returns the signature for `data` using the given private key and algorithm. If `algorithm` is `null` or `undefined`, then the algorithm is dependent upon the key type (especially Ed25519 and Ed448).

f

[timingSafeEqual](.././crypto/~/timingSafeEqual "timingSafeEqual")

This function compares the underlying bytes that represent the given `ArrayBuffer`, `TypedArray`, or `DataView` instances using a constant-time algorithm.

f

[verify](.././crypto/~/verify "verify")

Verifies the given signature for `data` using the given key and algorithm. If `algorithm` is `null` or `undefined`, then the algorithm is dependent upon the key type (especially Ed25519 and Ed448).

### Interfaces [#](#Interfaces)

I

[AsymmetricKeyDetails](.././crypto/~/AsymmetricKeyDetails "AsymmetricKeyDetails")

No documentation available

*   [divisorLength](.././crypto/~/AsymmetricKeyDetails#property_divisorlength)
*   [hashAlgorithm](.././crypto/~/AsymmetricKeyDetails#property_hashalgorithm)
*   [mgf1HashAlgorithm](.././crypto/~/AsymmetricKeyDetails#property_mgf1hashalgorithm)
*   [modulusLength](.././crypto/~/AsymmetricKeyDetails#property_moduluslength)
*   [namedCurve](.././crypto/~/AsymmetricKeyDetails#property_namedcurve)
*   [publicExponent](.././crypto/~/AsymmetricKeyDetails#property_publicexponent)
*   [saltLength](.././crypto/~/AsymmetricKeyDetails#property_saltlength)

I

[BasePrivateKeyEncodingOptions](.././crypto/~/BasePrivateKeyEncodingOptions "BasePrivateKeyEncodingOptions")

No documentation available

*   [cipher](.././crypto/~/BasePrivateKeyEncodingOptions#property_cipher)
*   [format](.././crypto/~/BasePrivateKeyEncodingOptions#property_format)
*   [passphrase](.././crypto/~/BasePrivateKeyEncodingOptions#property_passphrase)

I

[CheckPrimeOptions](.././crypto/~/CheckPrimeOptions "CheckPrimeOptions")

No documentation available

*   [checks](.././crypto/~/CheckPrimeOptions#property_checks)

I

[CipherCCM](.././crypto/~/CipherCCM "CipherCCM")

No documentation available

*   [getAuthTag](.././crypto/~/CipherCCM#method_getauthtag_0)
*   [setAAD](.././crypto/~/CipherCCM#method_setaad_0)

I

[CipherCCMOptions](.././crypto/~/CipherCCMOptions "CipherCCMOptions")

No documentation available

*   [authTagLength](.././crypto/~/CipherCCMOptions#property_authtaglength)

I

[CipherChaCha20Poly1305](.././crypto/~/CipherChaCha20Poly1305 "CipherChaCha20Poly1305")

No documentation available

*   [getAuthTag](.././crypto/~/CipherChaCha20Poly1305#method_getauthtag_0)
*   [setAAD](.././crypto/~/CipherChaCha20Poly1305#method_setaad_0)

I

[CipherChaCha20Poly1305Options](.././crypto/~/CipherChaCha20Poly1305Options "CipherChaCha20Poly1305Options")

No documentation available

*   [authTagLength](.././crypto/~/CipherChaCha20Poly1305Options#property_authtaglength)

I

[CipherGCM](.././crypto/~/CipherGCM "CipherGCM")

No documentation available

*   [getAuthTag](.././crypto/~/CipherGCM#method_getauthtag_0)
*   [setAAD](.././crypto/~/CipherGCM#method_setaad_0)

I

[CipherGCMOptions](.././crypto/~/CipherGCMOptions "CipherGCMOptions")

No documentation available

*   [authTagLength](.././crypto/~/CipherGCMOptions#property_authtaglength)

I

[CipherInfo](.././crypto/~/CipherInfo "CipherInfo")

No documentation available

*   [blockSize](.././crypto/~/CipherInfo#property_blocksize)
*   [ivLength](.././crypto/~/CipherInfo#property_ivlength)
*   [keyLength](.././crypto/~/CipherInfo#property_keylength)
*   [mode](.././crypto/~/CipherInfo#property_mode)
*   [name](.././crypto/~/CipherInfo#property_name)
*   [nid](.././crypto/~/CipherInfo#property_nid)

I

[CipherInfoOptions](.././crypto/~/CipherInfoOptions "CipherInfoOptions")

No documentation available

*   [ivLength](.././crypto/~/CipherInfoOptions#property_ivlength)
*   [keyLength](.././crypto/~/CipherInfoOptions#property_keylength)

I

[CipherOCB](.././crypto/~/CipherOCB "CipherOCB")

No documentation available

*   [getAuthTag](.././crypto/~/CipherOCB#method_getauthtag_0)
*   [setAAD](.././crypto/~/CipherOCB#method_setaad_0)

I

[CipherOCBOptions](.././crypto/~/CipherOCBOptions "CipherOCBOptions")

No documentation available

*   [authTagLength](.././crypto/~/CipherOCBOptions#property_authtaglength)

I

[DecipherCCM](.././crypto/~/DecipherCCM "DecipherCCM")

No documentation available

*   [setAAD](.././crypto/~/DecipherCCM#method_setaad_0)
*   [setAuthTag](.././crypto/~/DecipherCCM#method_setauthtag_0)

I

[DecipherChaCha20Poly1305](.././crypto/~/DecipherChaCha20Poly1305 "DecipherChaCha20Poly1305")

No documentation available

*   [setAAD](.././crypto/~/DecipherChaCha20Poly1305#method_setaad_0)
*   [setAuthTag](.././crypto/~/DecipherChaCha20Poly1305#method_setauthtag_0)

I

[DecipherGCM](.././crypto/~/DecipherGCM "DecipherGCM")

No documentation available

*   [setAAD](.././crypto/~/DecipherGCM#method_setaad_0)
*   [setAuthTag](.././crypto/~/DecipherGCM#method_setauthtag_0)

I

[DecipherOCB](.././crypto/~/DecipherOCB "DecipherOCB")

No documentation available

*   [setAAD](.././crypto/~/DecipherOCB#method_setaad_0)
*   [setAuthTag](.././crypto/~/DecipherOCB#method_setauthtag_0)

I

[DiffieHellmanGroupConstructor](.././crypto/~/DiffieHellmanGroupConstructor "DiffieHellmanGroupConstructor")

No documentation available

*   [prototype](.././crypto/~/DiffieHellmanGroupConstructor#property_prototype)

I

[DSAKeyPairKeyObjectOptions](.././crypto/~/DSAKeyPairKeyObjectOptions "DSAKeyPairKeyObjectOptions")

No documentation available

*   [divisorLength](.././crypto/~/DSAKeyPairKeyObjectOptions#property_divisorlength)
*   [modulusLength](.././crypto/~/DSAKeyPairKeyObjectOptions#property_moduluslength)

I

[DSAKeyPairOptions](.././crypto/~/DSAKeyPairOptions "DSAKeyPairOptions")

No documentation available

*   [divisorLength](.././crypto/~/DSAKeyPairOptions#property_divisorlength)
*   [modulusLength](.././crypto/~/DSAKeyPairOptions#property_moduluslength)
*   [privateKeyEncoding](.././crypto/~/DSAKeyPairOptions#property_privatekeyencoding)
*   [publicKeyEncoding](.././crypto/~/DSAKeyPairOptions#property_publickeyencoding)

I

[ECKeyPairKeyObjectOptions](.././crypto/~/ECKeyPairKeyObjectOptions "ECKeyPairKeyObjectOptions")

No documentation available

*   [namedCurve](.././crypto/~/ECKeyPairKeyObjectOptions#property_namedcurve)
*   [paramEncoding](.././crypto/~/ECKeyPairKeyObjectOptions#property_paramencoding)

I

[ECKeyPairOptions](.././crypto/~/ECKeyPairOptions "ECKeyPairOptions")

No documentation available

*   [privateKeyEncoding](.././crypto/~/ECKeyPairOptions#property_privatekeyencoding)
*   [publicKeyEncoding](.././crypto/~/ECKeyPairOptions#property_publickeyencoding)

I

[ED25519KeyPairKeyObjectOptions](.././crypto/~/ED25519KeyPairKeyObjectOptions "ED25519KeyPairKeyObjectOptions")

No documentation available

I

[ED25519KeyPairOptions](.././crypto/~/ED25519KeyPairOptions "ED25519KeyPairOptions")

No documentation available

*   [privateKeyEncoding](.././crypto/~/ED25519KeyPairOptions#property_privatekeyencoding)
*   [publicKeyEncoding](.././crypto/~/ED25519KeyPairOptions#property_publickeyencoding)

I

[ED448KeyPairKeyObjectOptions](.././crypto/~/ED448KeyPairKeyObjectOptions "ED448KeyPairKeyObjectOptions")

No documentation available

I

[ED448KeyPairOptions](.././crypto/~/ED448KeyPairOptions "ED448KeyPairOptions")

No documentation available

*   [privateKeyEncoding](.././crypto/~/ED448KeyPairOptions#property_privatekeyencoding)
*   [publicKeyEncoding](.././crypto/~/ED448KeyPairOptions#property_publickeyencoding)

I

[GeneratePrimeOptions](.././crypto/~/GeneratePrimeOptions "GeneratePrimeOptions")

No documentation available

*   [add](.././crypto/~/GeneratePrimeOptions#property_add)
*   [bigint](.././crypto/~/GeneratePrimeOptions#property_bigint)
*   [rem](.././crypto/~/GeneratePrimeOptions#property_rem)
*   [safe](.././crypto/~/GeneratePrimeOptions#property_safe)

I

[GeneratePrimeOptionsArrayBuffer](.././crypto/~/GeneratePrimeOptionsArrayBuffer "GeneratePrimeOptionsArrayBuffer")

No documentation available

*   [bigint](.././crypto/~/GeneratePrimeOptionsArrayBuffer#property_bigint)

I

[GeneratePrimeOptionsBigInt](.././crypto/~/GeneratePrimeOptionsBigInt "GeneratePrimeOptionsBigInt")

No documentation available

*   [bigint](.././crypto/~/GeneratePrimeOptionsBigInt#property_bigint)

I

[HashOptions](.././crypto/~/HashOptions "HashOptions")

No documentation available

*   [outputLength](.././crypto/~/HashOptions#property_outputlength)

I

[JsonWebKey](.././crypto/~/JsonWebKey "JsonWebKey")

No documentation available

*   [crv](.././crypto/~/JsonWebKey#property_crv)
*   [d](.././crypto/~/JsonWebKey#property_d)
*   [dp](.././crypto/~/JsonWebKey#property_dp)
*   [dq](.././crypto/~/JsonWebKey#property_dq)
*   [e](.././crypto/~/JsonWebKey#property_e)
*   [k](.././crypto/~/JsonWebKey#property_k)
*   [kty](.././crypto/~/JsonWebKey#property_kty)
*   [n](.././crypto/~/JsonWebKey#property_n)
*   [p](.././crypto/~/JsonWebKey#property_p)
*   [q](.././crypto/~/JsonWebKey#property_q)
*   [qi](.././crypto/~/JsonWebKey#property_qi)
*   [x](.././crypto/~/JsonWebKey#property_x)
*   [y](.././crypto/~/JsonWebKey#property_y)

I

[JsonWebKeyInput](.././crypto/~/JsonWebKeyInput "JsonWebKeyInput")

No documentation available

*   [format](.././crypto/~/JsonWebKeyInput#property_format)
*   [key](.././crypto/~/JsonWebKeyInput#property_key)

I

[JwkKeyExportOptions](.././crypto/~/JwkKeyExportOptions "JwkKeyExportOptions")

No documentation available

*   [format](.././crypto/~/JwkKeyExportOptions#property_format)

I

[KeyExportOptions](.././crypto/~/KeyExportOptions "KeyExportOptions")

No documentation available

*   [cipher](.././crypto/~/KeyExportOptions#property_cipher)
*   [format](.././crypto/~/KeyExportOptions#property_format)
*   [passphrase](.././crypto/~/KeyExportOptions#property_passphrase)
*   [type](.././crypto/~/KeyExportOptions#property_type)

I

[KeyPairKeyObjectResult](.././crypto/~/KeyPairKeyObjectResult "KeyPairKeyObjectResult")

No documentation available

*   [privateKey](.././crypto/~/KeyPairKeyObjectResult#property_privatekey)
*   [publicKey](.././crypto/~/KeyPairKeyObjectResult#property_publickey)

I

[KeyPairSyncResult](.././crypto/~/KeyPairSyncResult "KeyPairSyncResult")

No documentation available

*   [privateKey](.././crypto/~/KeyPairSyncResult#property_privatekey)
*   [publicKey](.././crypto/~/KeyPairSyncResult#property_publickey)

I

[PrivateKeyInput](.././crypto/~/PrivateKeyInput "PrivateKeyInput")

No documentation available

*   [encoding](.././crypto/~/PrivateKeyInput#property_encoding)
*   [format](.././crypto/~/PrivateKeyInput#property_format)
*   [key](.././crypto/~/PrivateKeyInput#property_key)
*   [passphrase](.././crypto/~/PrivateKeyInput#property_passphrase)
*   [type](.././crypto/~/PrivateKeyInput#property_type)

I

[PublicKeyInput](.././crypto/~/PublicKeyInput "PublicKeyInput")

No documentation available

*   [encoding](.././crypto/~/PublicKeyInput#property_encoding)
*   [format](.././crypto/~/PublicKeyInput#property_format)
*   [key](.././crypto/~/PublicKeyInput#property_key)
*   [type](.././crypto/~/PublicKeyInput#property_type)

I

[RandomUUIDOptions](.././crypto/~/RandomUUIDOptions "RandomUUIDOptions")

No documentation available

*   [disableEntropyCache](.././crypto/~/RandomUUIDOptions#property_disableentropycache)

I

[RSAKeyPairKeyObjectOptions](.././crypto/~/RSAKeyPairKeyObjectOptions "RSAKeyPairKeyObjectOptions")

No documentation available

*   [modulusLength](.././crypto/~/RSAKeyPairKeyObjectOptions#property_moduluslength)
*   [publicExponent](.././crypto/~/RSAKeyPairKeyObjectOptions#property_publicexponent)

I

[RSAKeyPairOptions](.././crypto/~/RSAKeyPairOptions "RSAKeyPairOptions")

No documentation available

*   [modulusLength](.././crypto/~/RSAKeyPairOptions#property_moduluslength)
*   [privateKeyEncoding](.././crypto/~/RSAKeyPairOptions#property_privatekeyencoding)
*   [publicExponent](.././crypto/~/RSAKeyPairOptions#property_publicexponent)
*   [publicKeyEncoding](.././crypto/~/RSAKeyPairOptions#property_publickeyencoding)

I

[RsaPrivateKey](.././crypto/~/RsaPrivateKey "RsaPrivateKey")

No documentation available

*   [key](.././crypto/~/RsaPrivateKey#property_key)
*   [oaepHash](.././crypto/~/RsaPrivateKey#property_oaephash)
*   [oaepLabel](.././crypto/~/RsaPrivateKey#property_oaeplabel)
*   [padding](.././crypto/~/RsaPrivateKey#property_padding)
*   [passphrase](.././crypto/~/RsaPrivateKey#property_passphrase)

I

[RSAPSSKeyPairKeyObjectOptions](.././crypto/~/RSAPSSKeyPairKeyObjectOptions "RSAPSSKeyPairKeyObjectOptions")

No documentation available

*   [hashAlgorithm](.././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_hashalgorithm)
*   [mgf1HashAlgorithm](.././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_mgf1hashalgorithm)
*   [modulusLength](.././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_moduluslength)
*   [publicExponent](.././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_publicexponent)
*   [saltLength](.././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_saltlength)

I

[RSAPSSKeyPairOptions](.././crypto/~/RSAPSSKeyPairOptions "RSAPSSKeyPairOptions")

No documentation available

*   [hashAlgorithm](.././crypto/~/RSAPSSKeyPairOptions#property_hashalgorithm)
*   [mgf1HashAlgorithm](.././crypto/~/RSAPSSKeyPairOptions#property_mgf1hashalgorithm)
*   [modulusLength](.././crypto/~/RSAPSSKeyPairOptions#property_moduluslength)
*   [privateKeyEncoding](.././crypto/~/RSAPSSKeyPairOptions#property_privatekeyencoding)
*   [publicExponent](.././crypto/~/RSAPSSKeyPairOptions#property_publicexponent)
*   [publicKeyEncoding](.././crypto/~/RSAPSSKeyPairOptions#property_publickeyencoding)
*   [saltLength](.././crypto/~/RSAPSSKeyPairOptions#property_saltlength)

I

[RsaPublicKey](.././crypto/~/RsaPublicKey "RsaPublicKey")

No documentation available

*   [key](.././crypto/~/RsaPublicKey#property_key)
*   [padding](.././crypto/~/RsaPublicKey#property_padding)

I

[ScryptOptions](.././crypto/~/ScryptOptions "ScryptOptions")

No documentation available

*   [N](.././crypto/~/ScryptOptions#property_n)
*   [blockSize](.././crypto/~/ScryptOptions#property_blocksize)
*   [cost](.././crypto/~/ScryptOptions#property_cost)
*   [maxmem](.././crypto/~/ScryptOptions#property_maxmem)
*   [p](.././crypto/~/ScryptOptions#property_p)
*   [parallelization](.././crypto/~/ScryptOptions#property_parallelization)
*   [r](.././crypto/~/ScryptOptions#property_r)

I

[SecureHeapUsage](.././crypto/~/SecureHeapUsage "SecureHeapUsage")

No documentation available

*   [min](.././crypto/~/SecureHeapUsage#property_min)
*   [total](.././crypto/~/SecureHeapUsage#property_total)
*   [used](.././crypto/~/SecureHeapUsage#property_used)
*   [utilization](.././crypto/~/SecureHeapUsage#property_utilization)

I

[SigningOptions](.././crypto/~/SigningOptions "SigningOptions")

No documentation available

*   [dsaEncoding](.././crypto/~/SigningOptions#property_dsaencoding)
*   [padding](.././crypto/~/SigningOptions#property_padding)
*   [saltLength](.././crypto/~/SigningOptions#property_saltlength)

I

[SignJsonWebKeyInput](.././crypto/~/SignJsonWebKeyInput "SignJsonWebKeyInput")

No documentation available

I

[SignKeyObjectInput](.././crypto/~/SignKeyObjectInput "SignKeyObjectInput")

No documentation available

*   [key](.././crypto/~/SignKeyObjectInput#property_key)

I

[SignPrivateKeyInput](.././crypto/~/SignPrivateKeyInput "SignPrivateKeyInput")

No documentation available

I

[VerifyJsonWebKeyInput](.././crypto/~/VerifyJsonWebKeyInput "VerifyJsonWebKeyInput")

No documentation available

I

[VerifyKeyObjectInput](.././crypto/~/VerifyKeyObjectInput "VerifyKeyObjectInput")

No documentation available

*   [key](.././crypto/~/VerifyKeyObjectInput#property_key)

I

[VerifyPublicKeyInput](.././crypto/~/VerifyPublicKeyInput "VerifyPublicKeyInput")

No documentation available

I

[webcrypto.AesCbcParams](.././crypto/~/webcrypto.AesCbcParams "webcrypto.AesCbcParams")

No documentation available

*   [iv](.././crypto/~/webcrypto.AesCbcParams#property_iv)

I

[webcrypto.AesCtrParams](.././crypto/~/webcrypto.AesCtrParams "webcrypto.AesCtrParams")

No documentation available

*   [counter](.././crypto/~/webcrypto.AesCtrParams#property_counter)
*   [length](.././crypto/~/webcrypto.AesCtrParams#property_length)

I

[webcrypto.AesDerivedKeyParams](.././crypto/~/webcrypto.AesDerivedKeyParams "webcrypto.AesDerivedKeyParams")

No documentation available

*   [length](.././crypto/~/webcrypto.AesDerivedKeyParams#property_length)

I

[webcrypto.AesGcmParams](.././crypto/~/webcrypto.AesGcmParams "webcrypto.AesGcmParams")

No documentation available

*   [additionalData](.././crypto/~/webcrypto.AesGcmParams#property_additionaldata)
*   [iv](.././crypto/~/webcrypto.AesGcmParams#property_iv)
*   [tagLength](.././crypto/~/webcrypto.AesGcmParams#property_taglength)

I

[webcrypto.AesKeyAlgorithm](.././crypto/~/webcrypto.AesKeyAlgorithm "webcrypto.AesKeyAlgorithm")

No documentation available

*   [length](.././crypto/~/webcrypto.AesKeyAlgorithm#property_length)

I

[webcrypto.AesKeyGenParams](.././crypto/~/webcrypto.AesKeyGenParams "webcrypto.AesKeyGenParams")

No documentation available

*   [length](.././crypto/~/webcrypto.AesKeyGenParams#property_length)

I

[webcrypto.Algorithm](.././crypto/~/webcrypto.Algorithm "webcrypto.Algorithm")

No documentation available

*   [name](.././crypto/~/webcrypto.Algorithm#property_name)

I

[webcrypto.Crypto](.././crypto/~/webcrypto.Crypto "webcrypto.Crypto")

Importing the `webcrypto` object (`import { webcrypto } from 'node:crypto'`) gives an instance of the `Crypto` class. `Crypto` is a singleton that provides access to the remainder of the crypto API.

*   [CryptoKey](.././crypto/~/webcrypto.Crypto#property_cryptokey)
*   [getRandomValues](.././crypto/~/webcrypto.Crypto#method_getrandomvalues_0)
*   [randomUUID](.././crypto/~/webcrypto.Crypto#method_randomuuid_0)
*   [subtle](.././crypto/~/webcrypto.Crypto#property_subtle)

I

[webcrypto.CryptoKey](.././crypto/~/webcrypto.CryptoKey "webcrypto.CryptoKey")

No documentation available

*   [algorithm](.././crypto/~/webcrypto.CryptoKey#property_algorithm)
*   [extractable](.././crypto/~/webcrypto.CryptoKey#property_extractable)
*   [type](.././crypto/~/webcrypto.CryptoKey#property_type)
*   [usages](.././crypto/~/webcrypto.CryptoKey#property_usages)

I

[webcrypto.CryptoKeyConstructor](.././crypto/~/webcrypto.CryptoKeyConstructor "webcrypto.CryptoKeyConstructor")

No documentation available

*   [length](.././crypto/~/webcrypto.CryptoKeyConstructor#property_length)
*   [name](.././crypto/~/webcrypto.CryptoKeyConstructor#property_name)
*   [prototype](.././crypto/~/webcrypto.CryptoKeyConstructor#property_prototype)

I

[webcrypto.CryptoKeyPair](.././crypto/~/webcrypto.CryptoKeyPair "webcrypto.CryptoKeyPair")

The `CryptoKeyPair` is a simple dictionary object with `publicKey` and `privateKey` properties, representing an asymmetric key pair.

*   [privateKey](.././crypto/~/webcrypto.CryptoKeyPair#property_privatekey)
*   [publicKey](.././crypto/~/webcrypto.CryptoKeyPair#property_publickey)

I

[webcrypto.EcdhKeyDeriveParams](.././crypto/~/webcrypto.EcdhKeyDeriveParams "webcrypto.EcdhKeyDeriveParams")

No documentation available

*   [public](.././crypto/~/webcrypto.EcdhKeyDeriveParams#property_public)

I

[webcrypto.EcdsaParams](.././crypto/~/webcrypto.EcdsaParams "webcrypto.EcdsaParams")

No documentation available

*   [hash](.././crypto/~/webcrypto.EcdsaParams#property_hash)

I

[webcrypto.EcKeyAlgorithm](.././crypto/~/webcrypto.EcKeyAlgorithm "webcrypto.EcKeyAlgorithm")

No documentation available

*   [namedCurve](.././crypto/~/webcrypto.EcKeyAlgorithm#property_namedcurve)

I

[webcrypto.EcKeyGenParams](.././crypto/~/webcrypto.EcKeyGenParams "webcrypto.EcKeyGenParams")

No documentation available

*   [namedCurve](.././crypto/~/webcrypto.EcKeyGenParams#property_namedcurve)

I

[webcrypto.EcKeyImportParams](.././crypto/~/webcrypto.EcKeyImportParams "webcrypto.EcKeyImportParams")

No documentation available

*   [namedCurve](.././crypto/~/webcrypto.EcKeyImportParams#property_namedcurve)

I

[webcrypto.Ed448Params](.././crypto/~/webcrypto.Ed448Params "webcrypto.Ed448Params")

No documentation available

*   [context](.././crypto/~/webcrypto.Ed448Params#property_context)

I

[webcrypto.HkdfParams](.././crypto/~/webcrypto.HkdfParams "webcrypto.HkdfParams")

No documentation available

*   [hash](.././crypto/~/webcrypto.HkdfParams#property_hash)
*   [info](.././crypto/~/webcrypto.HkdfParams#property_info)
*   [salt](.././crypto/~/webcrypto.HkdfParams#property_salt)

I

[webcrypto.HmacImportParams](.././crypto/~/webcrypto.HmacImportParams "webcrypto.HmacImportParams")

No documentation available

*   [hash](.././crypto/~/webcrypto.HmacImportParams#property_hash)
*   [length](.././crypto/~/webcrypto.HmacImportParams#property_length)

I

[webcrypto.HmacKeyAlgorithm](.././crypto/~/webcrypto.HmacKeyAlgorithm "webcrypto.HmacKeyAlgorithm")

No documentation available

*   [hash](.././crypto/~/webcrypto.HmacKeyAlgorithm#property_hash)
*   [length](.././crypto/~/webcrypto.HmacKeyAlgorithm#property_length)

I

[webcrypto.HmacKeyGenParams](.././crypto/~/webcrypto.HmacKeyGenParams "webcrypto.HmacKeyGenParams")

No documentation available

*   [hash](.././crypto/~/webcrypto.HmacKeyGenParams#property_hash)
*   [length](.././crypto/~/webcrypto.HmacKeyGenParams#property_length)

I

[webcrypto.JsonWebKey](.././crypto/~/webcrypto.JsonWebKey "webcrypto.JsonWebKey")

No documentation available

*   [alg](.././crypto/~/webcrypto.JsonWebKey#property_alg)
*   [crv](.././crypto/~/webcrypto.JsonWebKey#property_crv)
*   [d](.././crypto/~/webcrypto.JsonWebKey#property_d)
*   [dp](.././crypto/~/webcrypto.JsonWebKey#property_dp)
*   [dq](.././crypto/~/webcrypto.JsonWebKey#property_dq)
*   [e](.././crypto/~/webcrypto.JsonWebKey#property_e)
*   [ext](.././crypto/~/webcrypto.JsonWebKey#property_ext)
*   [k](.././crypto/~/webcrypto.JsonWebKey#property_k)
*   [key\_ops](.././crypto/~/webcrypto.JsonWebKey#property_key_ops)
*   [kty](.././crypto/~/webcrypto.JsonWebKey#property_kty)
*   [n](.././crypto/~/webcrypto.JsonWebKey#property_n)
*   [oth](.././crypto/~/webcrypto.JsonWebKey#property_oth)
*   [p](.././crypto/~/webcrypto.JsonWebKey#property_p)
*   [q](.././crypto/~/webcrypto.JsonWebKey#property_q)
*   [qi](.././crypto/~/webcrypto.JsonWebKey#property_qi)
*   [use](.././crypto/~/webcrypto.JsonWebKey#property_use)
*   [x](.././crypto/~/webcrypto.JsonWebKey#property_x)
*   [y](.././crypto/~/webcrypto.JsonWebKey#property_y)

I

[webcrypto.KeyAlgorithm](.././crypto/~/webcrypto.KeyAlgorithm "webcrypto.KeyAlgorithm")

No documentation available

*   [name](.././crypto/~/webcrypto.KeyAlgorithm#property_name)

I

[webcrypto.Pbkdf2Params](.././crypto/~/webcrypto.Pbkdf2Params "webcrypto.Pbkdf2Params")

No documentation available

*   [hash](.././crypto/~/webcrypto.Pbkdf2Params#property_hash)
*   [iterations](.././crypto/~/webcrypto.Pbkdf2Params#property_iterations)
*   [salt](.././crypto/~/webcrypto.Pbkdf2Params#property_salt)

I

[webcrypto.RsaHashedImportParams](.././crypto/~/webcrypto.RsaHashedImportParams "webcrypto.RsaHashedImportParams")

No documentation available

*   [hash](.././crypto/~/webcrypto.RsaHashedImportParams#property_hash)

I

[webcrypto.RsaHashedKeyAlgorithm](.././crypto/~/webcrypto.RsaHashedKeyAlgorithm "webcrypto.RsaHashedKeyAlgorithm")

No documentation available

*   [hash](.././crypto/~/webcrypto.RsaHashedKeyAlgorithm#property_hash)

I

[webcrypto.RsaHashedKeyGenParams](.././crypto/~/webcrypto.RsaHashedKeyGenParams "webcrypto.RsaHashedKeyGenParams")

No documentation available

*   [hash](.././crypto/~/webcrypto.RsaHashedKeyGenParams#property_hash)

I

[webcrypto.RsaKeyAlgorithm](.././crypto/~/webcrypto.RsaKeyAlgorithm "webcrypto.RsaKeyAlgorithm")

No documentation available

*   [modulusLength](.././crypto/~/webcrypto.RsaKeyAlgorithm#property_moduluslength)
*   [publicExponent](.././crypto/~/webcrypto.RsaKeyAlgorithm#property_publicexponent)

I

[webcrypto.RsaKeyGenParams](.././crypto/~/webcrypto.RsaKeyGenParams "webcrypto.RsaKeyGenParams")

No documentation available

*   [modulusLength](.././crypto/~/webcrypto.RsaKeyGenParams#property_moduluslength)
*   [publicExponent](.././crypto/~/webcrypto.RsaKeyGenParams#property_publicexponent)

I

[webcrypto.RsaOaepParams](.././crypto/~/webcrypto.RsaOaepParams "webcrypto.RsaOaepParams")

No documentation available

*   [label](.././crypto/~/webcrypto.RsaOaepParams#property_label)

I

[webcrypto.RsaOtherPrimesInfo](.././crypto/~/webcrypto.RsaOtherPrimesInfo "webcrypto.RsaOtherPrimesInfo")

No documentation available

*   [d](.././crypto/~/webcrypto.RsaOtherPrimesInfo#property_d)
*   [r](.././crypto/~/webcrypto.RsaOtherPrimesInfo#property_r)
*   [t](.././crypto/~/webcrypto.RsaOtherPrimesInfo#property_t)

I

[webcrypto.RsaPssParams](.././crypto/~/webcrypto.RsaPssParams "webcrypto.RsaPssParams")

No documentation available

*   [saltLength](.././crypto/~/webcrypto.RsaPssParams#property_saltlength)

I

[webcrypto.SubtleCrypto](.././crypto/~/webcrypto.SubtleCrypto "webcrypto.SubtleCrypto")

No documentation available

*   [decrypt](.././crypto/~/webcrypto.SubtleCrypto#method_decrypt_0)
*   [deriveBits](.././crypto/~/webcrypto.SubtleCrypto#method_derivebits_0)
*   [deriveKey](.././crypto/~/webcrypto.SubtleCrypto#method_derivekey_0)
*   [digest](.././crypto/~/webcrypto.SubtleCrypto#method_digest_0)
*   [encrypt](.././crypto/~/webcrypto.SubtleCrypto#method_encrypt_0)
*   [exportKey](.././crypto/~/webcrypto.SubtleCrypto#method_exportkey_0)
*   [generateKey](.././crypto/~/webcrypto.SubtleCrypto#method_generatekey_0)
*   [importKey](.././crypto/~/webcrypto.SubtleCrypto#method_importkey_0)
*   [sign](.././crypto/~/webcrypto.SubtleCrypto#method_sign_0)
*   [unwrapKey](.././crypto/~/webcrypto.SubtleCrypto#method_unwrapkey_0)
*   [verify](.././crypto/~/webcrypto.SubtleCrypto#method_verify_0)
*   [wrapKey](.././crypto/~/webcrypto.SubtleCrypto#method_wrapkey_0)

I

[X25519KeyPairKeyObjectOptions](.././crypto/~/X25519KeyPairKeyObjectOptions "X25519KeyPairKeyObjectOptions")

No documentation available

I

[X25519KeyPairOptions](.././crypto/~/X25519KeyPairOptions "X25519KeyPairOptions")

No documentation available

*   [privateKeyEncoding](.././crypto/~/X25519KeyPairOptions#property_privatekeyencoding)
*   [publicKeyEncoding](.././crypto/~/X25519KeyPairOptions#property_publickeyencoding)

I

[X448KeyPairKeyObjectOptions](.././crypto/~/X448KeyPairKeyObjectOptions "X448KeyPairKeyObjectOptions")

No documentation available

I

[X448KeyPairOptions](.././crypto/~/X448KeyPairOptions "X448KeyPairOptions")

No documentation available

*   [privateKeyEncoding](.././crypto/~/X448KeyPairOptions#property_privatekeyencoding)
*   [publicKeyEncoding](.././crypto/~/X448KeyPairOptions#property_publickeyencoding)

I

[X509CheckOptions](.././crypto/~/X509CheckOptions "X509CheckOptions")

No documentation available

*   [multiLabelWildcards](.././crypto/~/X509CheckOptions#property_multilabelwildcards)
*   [partialWildcards](.././crypto/~/X509CheckOptions#property_partialwildcards)
*   [singleLabelSubdomains](.././crypto/~/X509CheckOptions#property_singlelabelsubdomains)
*   [subject](.././crypto/~/X509CheckOptions#property_subject)
*   [wildcards](.././crypto/~/X509CheckOptions#property_wildcards)

### Namespaces [#](#Namespaces)

N

[constants](.././crypto/~/constants "constants")

No documentation available

### Type Aliases [#](<#Type Aliases>)

T

[BinaryLike](.././crypto/~/BinaryLike "BinaryLike")

No documentation available

T

[BinaryToTextEncoding](.././crypto/~/BinaryToTextEncoding "BinaryToTextEncoding")

No documentation available

T

[CharacterEncoding](.././crypto/~/CharacterEncoding "CharacterEncoding")

No documentation available

T

[CipherCCMTypes](.././crypto/~/CipherCCMTypes "CipherCCMTypes")

No documentation available

T

[CipherChaCha20Poly1305Types](.././crypto/~/CipherChaCha20Poly1305Types "CipherChaCha20Poly1305Types")

No documentation available

T

[CipherGCMTypes](.././crypto/~/CipherGCMTypes "CipherGCMTypes")

No documentation available

T

[CipherKey](.././crypto/~/CipherKey "CipherKey")

No documentation available

T

[CipherMode](.././crypto/~/CipherMode "CipherMode")

No documentation available

T

[CipherOCBTypes](.././crypto/~/CipherOCBTypes "CipherOCBTypes")

No documentation available

T

[DSAEncoding](.././crypto/~/DSAEncoding "DSAEncoding")

No documentation available

T

[ECDHKeyFormat](.././crypto/~/ECDHKeyFormat "ECDHKeyFormat")

No documentation available

T

[Encoding](.././crypto/~/Encoding "Encoding")

No documentation available

T

[KeyFormat](.././crypto/~/KeyFormat "KeyFormat")

No documentation available

T

[KeyLike](.././crypto/~/KeyLike "KeyLike")

No documentation available

T

[KeyObjectType](.././crypto/~/KeyObjectType "KeyObjectType")

No documentation available

T

[KeyType](.././crypto/~/KeyType "KeyType")

No documentation available

T

[LargeNumberLike](.././crypto/~/LargeNumberLike "LargeNumberLike")

No documentation available

T

[LegacyCharacterEncoding](.././crypto/~/LegacyCharacterEncoding "LegacyCharacterEncoding")

No documentation available

T

[UUID](.././crypto/~/UUID "UUID")

No documentation available

T

[webcrypto.AlgorithmIdentifier](.././crypto/~/webcrypto.AlgorithmIdentifier "webcrypto.AlgorithmIdentifier")

No documentation available

T

[webcrypto.BigInteger](.././crypto/~/webcrypto.BigInteger "webcrypto.BigInteger")

No documentation available

T

[webcrypto.BufferSource](.././crypto/~/webcrypto.BufferSource "webcrypto.BufferSource")

No documentation available

T

[webcrypto.HashAlgorithmIdentifier](.././crypto/~/webcrypto.HashAlgorithmIdentifier "webcrypto.HashAlgorithmIdentifier")

No documentation available

T

[webcrypto.KeyFormat](.././crypto/~/webcrypto.KeyFormat "webcrypto.KeyFormat")

No documentation available

T

[webcrypto.KeyType](.././crypto/~/webcrypto.KeyType "webcrypto.KeyType")

No documentation available

T

[webcrypto.KeyUsage](.././crypto/~/webcrypto.KeyUsage "webcrypto.KeyUsage")

No documentation available

T

[webcrypto.NamedCurve](.././crypto/~/webcrypto.NamedCurve "webcrypto.NamedCurve")

No documentation available

### Variables [#](#Variables)

v

[constants.defaultCipherList](.././crypto/~/constants.defaultCipherList "constants.defaultCipherList")

Specifies the active default cipher list used by the current Node.js process (colon-separated values).

v

[constants.defaultCoreCipherList](.././crypto/~/constants.defaultCoreCipherList "constants.defaultCoreCipherList")

Specifies the built-in default cipher list used by Node.js (colon-separated values).

v

[constants.DH\_CHECK\_P\_NOT\_PRIME](.././crypto/~/constants.DH_CHECK_P_NOT_PRIME "constants.DH_CHECK_P_NOT_PRIME")

No documentation available

v

[constants.DH\_CHECK\_P\_NOT\_SAFE\_PRIME](.././crypto/~/constants.DH_CHECK_P_NOT_SAFE_PRIME "constants.DH_CHECK_P_NOT_SAFE_PRIME")

No documentation available

v

[constants.DH\_NOT\_SUITABLE\_GENERATOR](.././crypto/~/constants.DH_NOT_SUITABLE_GENERATOR "constants.DH_NOT_SUITABLE_GENERATOR")

No documentation available

v

[constants.DH\_UNABLE\_TO\_CHECK\_GENERATOR](.././crypto/~/constants.DH_UNABLE_TO_CHECK_GENERATOR "constants.DH_UNABLE_TO_CHECK_GENERATOR")

No documentation available

v

[constants.ENGINE\_METHOD\_ALL](.././crypto/~/constants.ENGINE_METHOD_ALL "constants.ENGINE_METHOD_ALL")

No documentation available

v

[constants.ENGINE\_METHOD\_CIPHERS](.././crypto/~/constants.ENGINE_METHOD_CIPHERS "constants.ENGINE_METHOD_CIPHERS")

No documentation available

v

[constants.ENGINE\_METHOD\_DH](.././crypto/~/constants.ENGINE_METHOD_DH "constants.ENGINE_METHOD_DH")

No documentation available

v

[constants.ENGINE\_METHOD\_DIGESTS](.././crypto/~/constants.ENGINE_METHOD_DIGESTS "constants.ENGINE_METHOD_DIGESTS")

No documentation available

v

[constants.ENGINE\_METHOD\_DSA](.././crypto/~/constants.ENGINE_METHOD_DSA "constants.ENGINE_METHOD_DSA")

No documentation available

v

[constants.ENGINE\_METHOD\_EC](.././crypto/~/constants.ENGINE_METHOD_EC "constants.ENGINE_METHOD_EC")

No documentation available

v

[constants.ENGINE\_METHOD\_NONE](.././crypto/~/constants.ENGINE_METHOD_NONE "constants.ENGINE_METHOD_NONE")

No documentation available

v

[constants.ENGINE\_METHOD\_PKEY\_ASN1\_METHS](.././crypto/~/constants.ENGINE_METHOD_PKEY_ASN1_METHS "constants.ENGINE_METHOD_PKEY_ASN1_METHS")

No documentation available

v

[constants.ENGINE\_METHOD\_PKEY\_METHS](.././crypto/~/constants.ENGINE_METHOD_PKEY_METHS "constants.ENGINE_METHOD_PKEY_METHS")

No documentation available

v

[constants.ENGINE\_METHOD\_RAND](.././crypto/~/constants.ENGINE_METHOD_RAND "constants.ENGINE_METHOD_RAND")

No documentation available

v

[constants.ENGINE\_METHOD\_RSA](.././crypto/~/constants.ENGINE_METHOD_RSA "constants.ENGINE_METHOD_RSA")

No documentation available

v

[constants.OPENSSL\_VERSION\_NUMBER](.././crypto/~/constants.OPENSSL_VERSION_NUMBER "constants.OPENSSL_VERSION_NUMBER")

No documentation available

v

[constants.POINT\_CONVERSION\_COMPRESSED](.././crypto/~/constants.POINT_CONVERSION_COMPRESSED "constants.POINT_CONVERSION_COMPRESSED")

No documentation available

v

[constants.POINT\_CONVERSION\_HYBRID](.././crypto/~/constants.POINT_CONVERSION_HYBRID "constants.POINT_CONVERSION_HYBRID")

No documentation available

v

[constants.POINT\_CONVERSION\_UNCOMPRESSED](.././crypto/~/constants.POINT_CONVERSION_UNCOMPRESSED "constants.POINT_CONVERSION_UNCOMPRESSED")

No documentation available

v

[constants.RSA\_NO\_PADDING](.././crypto/~/constants.RSA_NO_PADDING "constants.RSA_NO_PADDING")

No documentation available

v

[constants.RSA\_PKCS1\_OAEP\_PADDING](.././crypto/~/constants.RSA_PKCS1_OAEP_PADDING "constants.RSA_PKCS1_OAEP_PADDING")

No documentation available

v

[constants.RSA\_PKCS1\_PADDING](.././crypto/~/constants.RSA_PKCS1_PADDING "constants.RSA_PKCS1_PADDING")

No documentation available

v

[constants.RSA\_PKCS1\_PSS\_PADDING](.././crypto/~/constants.RSA_PKCS1_PSS_PADDING "constants.RSA_PKCS1_PSS_PADDING")

No documentation available

v

[constants.RSA\_PSS\_SALTLEN\_AUTO](.././crypto/~/constants.RSA_PSS_SALTLEN_AUTO "constants.RSA_PSS_SALTLEN_AUTO")

Causes the salt length for RSA\_PKCS1\_PSS\_PADDING to be determined automatically when verifying a signature.

v

[constants.RSA\_PSS\_SALTLEN\_DIGEST](.././crypto/~/constants.RSA_PSS_SALTLEN_DIGEST "constants.RSA_PSS_SALTLEN_DIGEST")

Sets the salt length for RSA\_PKCS1\_PSS\_PADDING to the digest size when signing or verifying.

v

[constants.RSA\_PSS\_SALTLEN\_MAX\_SIGN](.././crypto/~/constants.RSA_PSS_SALTLEN_MAX_SIGN "constants.RSA_PSS_SALTLEN_MAX_SIGN")

Sets the salt length for RSA\_PKCS1\_PSS\_PADDING to the maximum permissible value when signing data.

v

[constants.RSA\_SSLV23\_PADDING](.././crypto/~/constants.RSA_SSLV23_PADDING "constants.RSA_SSLV23_PADDING")

No documentation available

v

[constants.RSA\_X931\_PADDING](.././crypto/~/constants.RSA_X931_PADDING "constants.RSA_X931_PADDING")

No documentation available

v

[constants.SSL\_OP\_ALL](.././crypto/~/constants.SSL_OP_ALL "constants.SSL_OP_ALL")

Applies multiple bug workarounds within OpenSSL. See [https://www.openssl.org/docs/man1.0.2/ssl/SSL\_CTX\_set\_options.html](https://www.openssl.org/docs/man1.0.2/ssl/SSL_CTX_set_options.html) for detail.

v

[constants.SSL\_OP\_ALLOW\_NO\_DHE\_KEX](.././crypto/~/constants.SSL_OP_ALLOW_NO_DHE_KEX "constants.SSL_OP_ALLOW_NO_DHE_KEX")

Instructs OpenSSL to allow a non-\[EC\]DHE-based key exchange mode for TLS v1.3

v

[constants.SSL\_OP\_ALLOW\_UNSAFE\_LEGACY\_RENEGOTIATION](.././crypto/~/constants.SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION "constants.SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION")

Allows legacy insecure renegotiation between OpenSSL and unpatched clients or servers. See [https://www.openssl.org/docs/man1.0.2/ssl/SSL\_CTX\_set\_options.html](https://www.openssl.org/docs/man1.0.2/ssl/SSL_CTX_set_options.html).

v

[constants.SSL\_OP\_CIPHER\_SERVER\_PREFERENCE](.././crypto/~/constants.SSL_OP_CIPHER_SERVER_PREFERENCE "constants.SSL_OP_CIPHER_SERVER_PREFERENCE")

Attempts to use the server's preferences instead of the client's when selecting a cipher. See [https://www.openssl.org/docs/man1.0.2/ssl/SSL\_CTX\_set\_options.html](https://www.openssl.org/docs/man1.0.2/ssl/SSL_CTX_set_options.html).

v

[constants.SSL\_OP\_CISCO\_ANYCONNECT](.././crypto/~/constants.SSL_OP_CISCO_ANYCONNECT "constants.SSL_OP_CISCO_ANYCONNECT")

Instructs OpenSSL to use Cisco's version identifier of DTLS\_BAD\_VER.

v

[constants.SSL\_OP\_COOKIE\_EXCHANGE](.././crypto/~/constants.SSL_OP_COOKIE_EXCHANGE "constants.SSL_OP_COOKIE_EXCHANGE")

Instructs OpenSSL to turn on cookie exchange.

v

[constants.SSL\_OP\_CRYPTOPRO\_TLSEXT\_BUG](.././crypto/~/constants.SSL_OP_CRYPTOPRO_TLSEXT_BUG "constants.SSL_OP_CRYPTOPRO_TLSEXT_BUG")

Instructs OpenSSL to add server-hello extension from an early version of the cryptopro draft.

v

[constants.SSL\_OP\_DONT\_INSERT\_EMPTY\_FRAGMENTS](.././crypto/~/constants.SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS "constants.SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS")

Instructs OpenSSL to disable a SSL 3.0/TLS 1.0 vulnerability workaround added in OpenSSL 0.9.6d.

v

[constants.SSL\_OP\_LEGACY\_SERVER\_CONNECT](.././crypto/~/constants.SSL_OP_LEGACY_SERVER_CONNECT "constants.SSL_OP_LEGACY_SERVER_CONNECT")

Allows initial connection to servers that do not support RI.

v

[constants.SSL\_OP\_NO\_COMPRESSION](.././crypto/~/constants.SSL_OP_NO_COMPRESSION "constants.SSL_OP_NO_COMPRESSION")

Instructs OpenSSL to disable support for SSL/TLS compression.

v

[constants.SSL\_OP\_NO\_ENCRYPT\_THEN\_MAC](.././crypto/~/constants.SSL_OP_NO_ENCRYPT_THEN_MAC "constants.SSL_OP_NO_ENCRYPT_THEN_MAC")

Instructs OpenSSL to disable encrypt-then-MAC.

v

[constants.SSL\_OP\_NO\_QUERY\_MTU](.././crypto/~/constants.SSL_OP_NO_QUERY_MTU "constants.SSL_OP_NO_QUERY_MTU")

No documentation available

v

[constants.SSL\_OP\_NO\_RENEGOTIATION](.././crypto/~/constants.SSL_OP_NO_RENEGOTIATION "constants.SSL_OP_NO_RENEGOTIATION")

Instructs OpenSSL to disable renegotiation.

v

[constants.SSL\_OP\_NO\_SESSION\_RESUMPTION\_ON\_RENEGOTIATION](.././crypto/~/constants.SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION "constants.SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION")

Instructs OpenSSL to always start a new session when performing renegotiation.

v

[constants.SSL\_OP\_NO\_SSLv2](.././crypto/~/constants.SSL_OP_NO_SSLv2 "constants.SSL_OP_NO_SSLv2")

Instructs OpenSSL to turn off SSL v2

v

[constants.SSL\_OP\_NO\_SSLv3](.././crypto/~/constants.SSL_OP_NO_SSLv3 "constants.SSL_OP_NO_SSLv3")

Instructs OpenSSL to turn off SSL v3

v

[constants.SSL\_OP\_NO\_TICKET](.././crypto/~/constants.SSL_OP_NO_TICKET "constants.SSL_OP_NO_TICKET")

Instructs OpenSSL to disable use of RFC4507bis tickets.

v

[constants.SSL\_OP\_NO\_TLSv1](.././crypto/~/constants.SSL_OP_NO_TLSv1 "constants.SSL_OP_NO_TLSv1")

Instructs OpenSSL to turn off TLS v1

v

[constants.SSL\_OP\_NO\_TLSv1\_1](.././crypto/~/constants.SSL_OP_NO_TLSv1_1 "constants.SSL_OP_NO_TLSv1_1")

Instructs OpenSSL to turn off TLS v1.1

v

[constants.SSL\_OP\_NO\_TLSv1\_2](.././crypto/~/constants.SSL_OP_NO_TLSv1_2 "constants.SSL_OP_NO_TLSv1_2")

Instructs OpenSSL to turn off TLS v1.2

v

[constants.SSL\_OP\_NO\_TLSv1\_3](.././crypto/~/constants.SSL_OP_NO_TLSv1_3 "constants.SSL_OP_NO_TLSv1_3")

Instructs OpenSSL to turn off TLS v1.3

v

[constants.SSL\_OP\_PRIORITIZE\_CHACHA](.././crypto/~/constants.SSL_OP_PRIORITIZE_CHACHA "constants.SSL_OP_PRIORITIZE_CHACHA")

Instructs OpenSSL server to prioritize ChaCha20-Poly1305 when the client does. This option has no effect if `SSL_OP_CIPHER_SERVER_PREFERENCE` is not enabled.

v

[constants.SSL\_OP\_TLS\_ROLLBACK\_BUG](.././crypto/~/constants.SSL_OP_TLS_ROLLBACK_BUG "constants.SSL_OP_TLS_ROLLBACK_BUG")

Instructs OpenSSL to disable version rollback attack detection.

v

[crypto](.././crypto/~/crypto "crypto")

No documentation available

T

v

[DiffieHellmanGroup](.././crypto/~/DiffieHellmanGroup "DiffieHellmanGroup")

No documentation available

v

[subtle](.././crypto/~/subtle "subtle")

A convenient alias for `crypto.webcrypto.subtle`.

N

v

[webcrypto](.././crypto/~/webcrypto "webcrypto")

No documentation available

v

[fips](.././crypto/~/fips "fips")

No documentation available

