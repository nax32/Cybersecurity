# Cryptography – Security Fundamentals Overview

## Overview
**Cryptography** is the practice of securing information by transforming it into a form that unauthorized parties cannot read or modify. It plays a critical role in modern cybersecurity by protecting data confidentiality, integrity, authentication, and non-repudiation.

Cryptography is the foundation of secure communication protocols such as HTTPS, TLS, VPNs, and secure authentication systems.

---

## Goals of Cryptography
Cryptography is designed to achieve four main security objectives:

### Confidentiality
- Ensures data is readable only by authorized parties
- Prevents unauthorized disclosure of sensitive information

### Integrity
- Ensures data has not been altered during transmission or storage
- Detects tampering or modification

### Authentication
- Verifies the identity of communicating parties
- Prevents impersonation attacks

### Non-Repudiation
- Prevents parties from denying their actions
- Ensures accountability (e.g., digital signatures)

---

## Core Cryptographic Concepts

### Plaintext
- Original readable data
- Example: passwords, messages, files

### Ciphertext
- Encrypted, unreadable form of data
- Produced after applying encryption

### Encryption
- Process of converting plaintext into ciphertext
- Uses cryptographic algorithms and keys

### Decryption
- Process of converting ciphertext back into plaintext
- Requires the correct cryptographic key

---

## Types of Cryptography

### Symmetric Cryptography
- Same key used for encryption and decryption
- Fast and efficient
- Used for bulk data encryption

Examples:
- AES
- DES (deprecated)

---

### Asymmetric Cryptography
- Uses a key pair:
  - Public key
  - Private key
- Slower but enables secure key exchange and authentication

Examples:
- RSA
- ECC

---

### Hash Functions
- One-way cryptographic functions
- Cannot be reversed
- Used for integrity and authentication

Examples:
- SHA-256
- SHA-3

---

## Cryptography in Network Security
Cryptography is used in:
- TLS handshakes
- HTTPS encryption
- Certificate validation
- Digital signatures
- Secure authentication systems

Modern secure systems combine **asymmetric**, **symmetric**, and **hashing** techniques to balance security and performance.

---

## Cryptography vs Encoding vs Hashing
- **Cryptography** → reversible (with key)
- **Encoding** → reversible, no security (e.g., Base64)
- **Hashing** → irreversible

Understanding this distinction is critical in security analysis.

---

## Security Perspective
- Weak cryptography leads to system compromise
- Strong algorithms can still fail due to poor implementation
- Key management is as important as algorithms

Cryptography must be applied correctly to be effective.

---

## Relation to Previous Topics
- TLS uses asymmetric cryptography for key exchange
- Symmetric cryptography secures application data
- Hashing ensures integrity and authentication
- Certificate validation relies on digital signatures

---

## Conclusion
Cryptography is the backbone of modern cybersecurity. A strong understanding of cryptographic principles is essential for analyzing secure communication protocols, defending against attacks, and designing secure systems.
