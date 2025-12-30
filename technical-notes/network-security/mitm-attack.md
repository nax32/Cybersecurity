# Man-in-the-Middle (MITM) Attack – Network Security Perspective

## Overview
A **Man-in-the-Middle (MITM) attack** occurs when an attacker secretly intercepts and possibly alters communication between two parties who believe they are communicating directly with each other. This attack compromises confidentiality, integrity, and sometimes authentication.

MITM attacks are especially dangerous in **unencrypted or poorly secured networks**.

---

## Objectives of a MITM Attack
An attacker performing a MITM attack may aim to:
- Steal sensitive information (credentials, cookies, tokens)
- Monitor user activity
- Modify transmitted data
- Inject malicious content
- Hijack user sessions

---

## How a MITM Attack Works (Simplified)

### Interception
The attacker positions themselves between the client and the server using techniques such as:
- ARP spoofing
- DNS spoofing
- Rogue Wi-Fi access points

The victim is unaware of the interception.

---

### Decryption / Manipulation
- If traffic is **HTTP**, data is readable in plaintext
- If traffic is **HTTPS but improperly validated**, attackers may use fake certificates
- Attacker can:
  - Read data
  - Modify requests/responses
  - Inject malicious scripts

---

### Forwarding Traffic
The attacker forwards traffic to the real destination so communication appears normal, making detection difficult.

---

## Common Types of MITM Attacks

### ARP Spoofing
- Attacker maps their MAC address to the IP of another device
- Redirects traffic through attacker’s system

### DNS Spoofing
- Victim is redirected to a malicious server
- Often used for phishing or malware delivery

### HTTPS Downgrade Attacks
- Forces HTTPS connections to fall back to HTTP
- Makes traffic readable

### Evil Twin Attack
- Fake Wi-Fi hotspot mimics a legitimate network
- Common in public places

---

## MITM Attacks in Wireshark
Using packet analysis, an attacker can:
- Read credentials in HTTP traffic
- Capture session cookies
- Observe request URLs and headers
- Modify packets in real time

 *HTTPS traffic prevents payload visibility even if packets are captured.*

---

## Role of TLS in Preventing MITM Attacks
TLS protects against MITM attacks by:
- Encrypting application data
- Verifying server identity using certificates
- Detecting tampered data via integrity checks

If certificate validation fails, browsers display security warnings.

---

## Security Indicators of a MITM Attack
- Unexpected certificate warnings
- HTTPS connection downgraded to HTTP
- Sudden redirections
- Invalid or self-signed certificates
- Repeated session logouts

---

## Prevention and Mitigation Techniques
- Always use **HTTPS**
- Enforce **HSTS (HTTP Strict Transport Security)**
- Validate TLS certificates properly
- Avoid public Wi-Fi without VPN
- Use secure DNS (DoH / DoT)
- Implement certificate pinning in applications

---

## Relation to Practical Labs
In **Lab-03 (HTTP vs HTTPS Comparison)**:
- HTTP traffic was vulnerable to MITM attacks
- HTTPS traffic remained protected due to TLS encryption

In **TLS Handshake analysis**, certificate verification was shown to be a critical defense against MITM attacks.

---

## Conclusion
MITM attacks exploit weak or unencrypted communication channels. The use of TLS, proper certificate validation, and secure network practices significantly reduces the risk of such attacks. Understanding MITM techniques is essential for detecting network threats and designing secure communication systems.
