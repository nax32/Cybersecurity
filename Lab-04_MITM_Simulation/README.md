# Lab-04: Man-in-the-Middle (MITM) Attack Simulation

## Objective

The objective of this lab is to simulate a **Man-in-the-Middle (MITM) attack** in a controlled environment to understand how attackers intercept network traffic and how encryption mechanisms like HTTPS and TLS protect against such attacks.

This lab demonstrates:
- How MITM attacks work
- What data is exposed during unsecured communication
- Why encrypted traffic is critical for secure networking

---

## Background

A **Man-in-the-Middle (MITM) attack** occurs when an attacker secretly intercepts and possibly alters communication between two parties who believe they are directly communicating with each other.

MITM attacks are commonly used to:
- Steal credentials
- Monitor sensitive data
- Modify transmitted information
- Bypass security mechanisms

---

## Tools Used

- **Wireshark** – Packet capture and analysis
- **Web Browser** – Generating HTTP and HTTPS traffic
- **Local Network / Test Environment** – Controlled lab setup
- *(Optional for advanced labs: ARP spoofing tools – not used here for safety)*

---

## Lab Environment

- **Victim:** Web browser accessing websites
- **Attacker (Simulation):** Packet analyzer (Wireshark)
- **Network Type:** Local network
- **Traffic Types:**
  - HTTP (Unencrypted)
  - HTTPS (Encrypted)

 **Note:** This lab is strictly educational and performed in a controlled environment.

---

## Attack Simulation Overview

Instead of performing a real attack, this lab simulates a MITM scenario by:
- Capturing live network traffic
- Observing plaintext data over HTTP
- Comparing it with encrypted HTTPS traffic
- Analyzing how TLS prevents MITM exploitation

---

## Steps Performed

### Step 1: Start Packet Capture
- Open Wireshark
- Select the active network interface
- Start capturing packets

---

### Step 2: Generate HTTP Traffic
- Visit an **HTTP website** (e.g., `http://example.com`)
- Observe traffic in Wireshark

#### Observations:
- URLs are visible
- Request methods are readable
- Headers and data appear in plaintext

---

### Step 3: Generate HTTPS Traffic
- Visit an **HTTPS website** (e.g., `https://example.com`)
- Observe traffic in Wireshark

#### Observations:
- TLS handshake is visible
- Cipher suite negotiation occurs
- Application data is encrypted and unreadable

---

### Step 4: Analyze MITM Feasibility

| Traffic Type | Data Visibility | MITM Risk |
|--------------|----------------|-----------|
| HTTP | Fully visible | High |
| HTTPS | Encrypted | Very Low |

---

## Wireshark Filters Used

```text
http
tls
tcp.port == 443
```

---

## Security Analysis

### Why MITM Works on HTTP
- No encryption
- No authentication
- No integrity protection
- Attackers can read and modify traffic easily

### Why MITM Fails on HTTPS
- TLS encrypts data
- Certificates authenticate servers
- Session keys prevent tampering
- Attackers see only encrypted payloads

---

## Relation to TLS Handshake

This lab directly relates to the **TLS Handshake**, where:
- Encryption parameters are negotiated
- Certificates are validated
- Secure session keys are established

If TLS is compromised or bypassed, MITM attacks become possible.

---

## Real-World Impact

MITM attacks are commonly seen in:
- Public Wi-Fi networks
- Rogue access points
- Compromised routers
- DNS spoofing scenarios

---

## Mitigation Techniques

- Always enforce **HTTPS**
- Use **HSTS (HTTP Strict Transport Security)**
- Validate TLS certificates
- Avoid unsecured public networks
- Use VPNs when necessary

---

## Conclusion

This lab demonstrates how Man-in-the-Middle attacks exploit unencrypted communication and why HTTPS with TLS is essential for modern network security. Understanding MITM attacks helps security professionals detect, prevent, and mitigate real-world threats effectively.

---

## Lab Status

 Completed  
 Educational simulation only  
 Safe and ethical practice
