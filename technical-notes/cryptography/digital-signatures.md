# Digital Signatures

## Overview

A **digital signature** is a cryptographic mechanism used to verify the **authenticity**, **integrity**, and **non-repudiation** of digital data.  
It ensures that a message or document was created by a specific sender and has not been altered during transmission.

Digital signatures are widely used in secure communications, software distribution, certificates, and legal documents.

---

## What Digital Signatures Provide

Digital signatures achieve the following security goals:

- **Authentication** – Verifies the identity of the sender  
- **Integrity** – Ensures data has not been modified  
- **Non-repudiation** – Sender cannot deny signing the data  

---

## How Digital Signatures Work (Step-by-Step)

### 1. Hashing the Message
- The sender creates a **hash** of the message using a cryptographic hash function (e.g., SHA-256).
- This produces a fixed-length message digest.

### 2. Signing the Hash
- The sender encrypts the hash using their **private key**.
- The encrypted hash becomes the **digital signature**.

### 3. Sending Data
The sender transmits:
- The **original message**
- The **digital signature**
- (Optionally) a **digital certificate**

### 4. Signature Verification
The receiver:
- Hashes the received message
- Decrypts the signature using the sender’s **public key**
- Compares both hashes

If they match, the signature is valid.

---

## Why Hashing Is Used

Digital signatures do **not** encrypt the entire message.

Instead:
- Hashing improves performance
- Ensures fixed-size input
- Protects message integrity

Only the hash is signed, not the full data.

---

## Common Digital Signature Algorithms

### RSA
- Uses asymmetric encryption
- Widely supported
- Slower than modern alternatives

### DSA (Digital Signature Algorithm)
- Designed specifically for digital signatures
- Uses discrete logarithms

### ECDSA (Elliptic Curve Digital Signature Algorithm)
- Based on elliptic curve cryptography
- Faster and more efficient
- Common in modern systems and TLS

---

## Digital Signatures vs Encryption

| Feature | Digital Signature | Encryption |
|------|-----------------|------------|
| Purpose | Authentication & integrity | Confidentiality |
| Uses private key | Yes | Yes |
| Uses public key | Yes | Yes |
| Protects message content |  No |  Yes |
| Protects message integrity |  Yes |  No |

Digital signatures **do not hide data** — they prove who sent it and that it wasn’t altered.

---

## Role of Digital Signatures in TLS and HTTPS

In secure web communication:
- Servers use **digital signatures** in certificates
- Clients verify server identity
- Prevents impersonation and MITM attacks

Digital signatures ensure trust before encryption begins.

---

## Real-World Use Cases

Digital signatures are used in:

- TLS/SSL certificates
- Software updates
- Email security (PGP, S/MIME)
- Code signing
- Blockchain and cryptocurrencies
- Legal and financial documents

---

## Security Considerations

- Compromised private keys break trust
- Weak hash functions reduce security
- Improper certificate validation enables attacks

Strong security requires:
- Secure key storage
- Trusted certificate authorities
- Modern algorithms and hash functions

---

## Relation to Other Cryptography Topics

- Hash functions ensure data integrity
- Asymmetric encryption enables signing
- Certificates bind public keys to identities
- TLS uses digital signatures for authentication
- MITM attacks exploit weak verification

---

## Conclusion

Digital signatures are a fundamental component of modern cybersecurity. They provide strong guarantees of authenticity, integrity, and non-repudiation without encrypting data. Understanding digital signatures is essential for analyzing secure communication protocols, certificate-based trust, and real-world security systems.
