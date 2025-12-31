# Asymmetric Encryption

## Overview

Asymmetric encryption is a cryptographic technique that uses a **pair of mathematically related keys**:

- **Public key** – shared openly  
- **Private key** – kept secret by the owner  

Data encrypted with one key can only be decrypted with the other. This approach solves the key distribution problem present in symmetric encryption and enables secure communication over untrusted networks.

Asymmetric encryption is foundational to **TLS, HTTPS, digital certificates, and secure key exchange**.

---

## How Asymmetric Encryption Works

1. A user generates a **public–private key pair**
2. The public key is shared openly
3. A sender encrypts data using the recipient’s **public key**
4. Only the recipient can decrypt the data using their **private key**

This ensures that only the intended recipient can access the encrypted information.

---

## Security Goals Achieved

Asymmetric encryption provides:

- **Confidentiality** – Only the private key holder can decrypt data  
- **Authentication** – Verifies identity using key ownership  
- **Integrity** – Prevents unauthorized data modification  
- **Non-repudiation** – Sender cannot deny their action (digital signatures)

---

## Common Asymmetric Encryption Algorithms

### RSA (Rivest–Shamir–Adleman)

- Most widely known asymmetric algorithm
- Based on the difficulty of factoring large prime numbers
- Used in:
  - TLS handshakes
  - Digital certificates
  - Secure key exchange

**Limitations:**
- Computationally expensive
- Slower than symmetric encryption
- Not suitable for large data encryption

---

### ECC (Elliptic Curve Cryptography)

- Uses elliptic curve mathematics
- Provides strong security with **smaller key sizes**
- Faster and more efficient than RSA
- Common in:
  - Modern TLS implementations
  - Mobile and IoT devices

---

## Why Asymmetric Encryption Is Slower

Asymmetric encryption:

- Uses complex mathematical operations
- Requires large key sizes
- Has higher computational overhead

Because of this, it is **not used for bulk data encryption**.

Instead, it is mainly used to:

- Exchange symmetric keys securely
- Authenticate identities
- Create digital signatures

---

## Key Management Advantages

Asymmetric encryption eliminates the need to share secret keys beforehand.

Benefits include:

- Secure communication over public networks
- No prior trust required
- Scalable for large systems
- Enables secure client–server communication

---

## Role in TLS and HTTPS

In secure web communication:

1. The server presents a **public key via a certificate**
2. The client verifies the certificate
3. Asymmetric encryption securely exchanges a **session key**
4. Symmetric encryption encrypts actual application data

This hybrid approach combines:

- **Security** from asymmetric encryption  
- **Performance** from symmetric encryption  

---

## Digital Signatures

Asymmetric encryption also enables digital signatures:

- Sender signs data using their **private key**
- Receiver verifies the signature using the **public key**
- Confirms:
  - Sender authenticity
  - Message integrity
  - Non-repudiation

Digital signatures are widely used in:
- Software updates
- Certificates
- Secure communications

---

## Security Considerations

- Private key compromise breaks security
- Weak key sizes reduce protection
- Poor certificate validation enables MITM attacks
- Strong security depends on:
  - Secure key storage
  - Trusted Certificate Authorities
  - Proper validation

---

## Relation to Other Cryptography Topics

- Symmetric encryption handles bulk data efficiently
- Asymmetric encryption secures key exchange
- TLS handshake combines both approaches
- Certificate validation ensures trust
- MITM attacks target weak key verification

---

## Conclusion

Asymmetric encryption is a critical pillar of modern cryptography. While slower than symmetric encryption, it enables secure key exchange, authentication, and trust establishment over insecure networks. Understanding asymmetric encryption is essential for analyzing TLS, HTTPS, certificates, and secure system design.
