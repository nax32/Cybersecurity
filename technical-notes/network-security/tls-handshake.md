# TLS Handshake – Network Security Perspective

## Overview
The **TLS (Transport Layer Security) handshake** is the process used to establish a secure, encrypted communication channel between a client and a server. It ensures that both parties agree on encryption methods and securely exchange cryptographic keys before transmitting application data.

---

## Purpose of the TLS Handshake
The TLS handshake is designed to provide:
- **Confidentiality** – Data cannot be read by attackers
- **Integrity** – Data cannot be altered in transit
- **Authentication** – Server identity is verified using certificates

---

## TLS Handshake Flow (Simplified)

### Client Hello
- Sent by the client (browser)
- Contains:
  - Supported TLS versions
  - List of cipher suites
  - Random client value

 *This message is visible in Wireshark.*

---

### Server Hello
- Sent by the server
- Contains:
  - Selected TLS version
  - Selected cipher suite
  - Random server value

 *This message is also visible in Wireshark.*

---

### Server Certificate
- Server sends its **digital certificate**
- Certificate includes:
  - Server public key
  - Certificate Authority (CA) signature
  - Domain information

 *Used to verify server identity.*

---

### Key Exchange
- Client generates a **pre-master secret**
- Pre-master secret is encrypted using the server’s public key
- Server decrypts it using its private key

 *This step ensures only the legitimate server can derive session keys.*

---

### Session Key Generation
- Both client and server independently generate:
  - Symmetric session keys
- Keys are derived using:
  - Client random
  - Server random
  - Pre-master secret

---

### Secure Communication Begins
- Handshake completes
- All subsequent traffic is:
  - Encrypted
  - Integrity-protected

 *In Wireshark, this appears as “Application Data”.*

---

## Why TLS Uses Both Asymmetric and Symmetric Encryption
- **Asymmetric encryption** is used during the handshake for secure key exchange
- **Symmetric encryption** is used afterward because it is faster and efficient

This hybrid approach provides both **security and performance**.

---

## TLS Handshake Visibility in Wireshark
- Handshake messages (Client Hello, Server Hello) are readable
- Cipher suites and TLS version are visible
- Application data content is **not readable**
- Payload appears encrypted after handshake completion

---

## Security Analysis
- TLS prevents:
  - Packet sniffing
  - Data tampering
  - Credential theft
- Without TLS, attackers can easily perform **Man-in-the-Middle (MITM)** attacks
- Modern security standards require TLS for all sensitive communications

---

## Relation to Practical Labs
In **Lab-03 (HTTP vs HTTPS Comparison)**, the TLS handshake was observed during HTTPS communication. Only handshake metadata was visible, while application data remained encrypted, validating the effectiveness of TLS in protecting web traffic.

---

## Conclusion
The TLS handshake is a critical security mechanism that establishes trust and encryption between a client and a server. Understanding each step of the handshake is essential for network security analysis, intrusion detection, and secure system design.
