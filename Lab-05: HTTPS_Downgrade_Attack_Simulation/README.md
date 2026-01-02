# Lab-05: HTTPS Downgrade Attack Simulation

## Objective

The objective of this lab is to understand **HTTPS downgrade attacks**, where an attacker attempts to force a secure HTTPS connection to fall back to insecure HTTP. This lab demonstrates how downgrade conditions occur and why enforcing HTTPS is critical for secure web communication.

This lab focuses on:

- Understanding how HTTPS downgrade attacks work  
- Observing HTTP vs HTTPS behavior  
- Identifying downgrade indicators such as redirects and missing HSTS  
- Learning mitigation techniques that prevent downgrade attacks  

---

## Background

An **HTTPS downgrade attack** occurs when an attacker interferes with a user's attempt to establish a secure HTTPS connection and forces the connection to use HTTP instead.

Common downgrade techniques include:

- Stripping HTTPS links and redirecting users to HTTP  
- Blocking or modifying HTTPS redirects  
- Exploiting websites that do not strictly enforce HTTPS  

Once downgraded to HTTP, an attacker can:

- Read sensitive data  
- Inject malicious content  
- Perform Man-in-the-Middle (MITM) attacks easily  

---

## Tools Used

- **curl** – Inspecting HTTP/HTTPS behavior, redirects, and security headers  
- **Wireshark** – Network traffic capture and protocol-level verification  
- **Web Browser** – Real-world HTTP and HTTPS access behavior  
- **Local Network (Controlled Environment)**  

>  This lab is strictly **educational** and does **not** perform real attacks.

---

## Lab Environment

- **Victim:** Web browser and curl client  
- **Attacker (Simulation):** Traffic analysis and observation tools  
- **Network Type:** Local / Test network  

**Traffic Types Observed:**
- HTTP (Unencrypted)  
- HTTPS (Encrypted)  

---

## Attack Simulation Overview

Instead of performing a real downgrade attack, this lab **simulates HTTPS downgrade conditions** by:

1. Using `curl` to observe HTTP → HTTPS redirects  
2. Inspecting HTTPS enforcement and security headers  
3. Identifying downgrade prevention mechanisms such as HSTS  
4. Verifying traffic behavior using Wireshark  

This approach ensures safe, ethical, and realistic analysis.

---

## curl-Based Downgrade Analysis

The `curl` tool was used to analyze how websites handle HTTPS enforcement.

Key observations include:

- Automatic redirection from HTTP to HTTPS  
- Presence or absence of **Strict-Transport-Security (HSTS)** headers  
- HTTPS-only access enforcement  

Example commands used:

```bash
curl -I http://example.com
curl -I https://example.com
curl -I https://example.com | grep -i strict-transport-security
```

These results clearly demonstrate whether a site is vulnerable to downgrade attacks.

---

## Wireshark Verification

Wireshark was used to validate observations at the network level:

- HTTP traffic was visible in plaintext  
- HTTPS traffic showed TLS handshakes  
- Encrypted application data was unreadable  
- No sensitive data was exposed over HTTPS  

This confirms the effectiveness of HTTPS and TLS against downgrade and MITM attacks.

---

## Security Analysis

### Why HTTPS Downgrade Attacks Work
- Lack of HTTPS enforcement  
- No HSTS policy  
- Insecure redirects  

### Why HTTPS Downgrade Attacks Fail
- Enforced HTTPS redirects  
- HSTS prevents HTTP fallback  
- TLS encryption protects data integrity  

---

## Mitigation Techniques

- Enforce HTTPS across all endpoints  
- Enable **HSTS (HTTP Strict Transport Security)**  
- Avoid mixed-content resources  
- Validate TLS certificates  
- Use secure browser configurations  

---

## Conclusion

This lab demonstrates how HTTPS downgrade attacks exploit weak configurations and why modern web security relies on strict HTTPS enforcement. By using `curl` for policy-level analysis and Wireshark for traffic verification, this lab provides a comprehensive and realistic understanding of downgrade attacks and their prevention.

---

## Lab Status

 Completed  
 Educational simulation only  
 Safe and ethical practice 
