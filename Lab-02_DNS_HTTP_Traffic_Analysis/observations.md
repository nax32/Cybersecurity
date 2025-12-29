# Observations – DNS & HTTP Traffic Analysis

## Capture Summary
- A short packet capture was performed while browsing standard websites.
- Traffic was analyzed using Wireshark with protocol-based filters.
- The focus was on **DNS resolution** and **HTTP communication**.

---

## DNS Traffic Observations
- DNS queries were observed when a domain name was accessed in the browser.
- The client sent DNS queries to a DNS server over **UDP port 53**.
- DNS responses contained the resolved IP addresses for the requested domains.
- DNS traffic was transmitted in **plaintext**, making queried domain names visible.

**Security Insight:**  
Unencrypted DNS traffic can expose browsing behavior and can be monitored or manipulated by attackers.

---

## HTTP Traffic Observations
- HTTP requests were observed over **TCP port 80**.
- Common HTTP methods such as **GET** were visible in the captured packets.
- Requested URLs and resource paths were readable in plaintext.
- Server responses included status codes and content-related headers.

**Security Insight:**  
HTTP traffic is not encrypted, which allows attackers to:
- Inspect transmitted data
- Perform man-in-the-middle (MITM) attacks
- Potentially steal sensitive information

---

## Comparison with Secure Protocols
- Unlike **HTTPS**, HTTP does not provide encryption.
- Data transmitted over HTTP can be intercepted and modified.
- This highlights the importance of using **HTTPS** and encrypted DNS (DoH / DoT).

---

## General Findings
- Network traffic analysis reveals how everyday internet activities generate multiple protocol interactions.
- Even simple browsing produces DNS and HTTP packets that expose valuable information.
- Proper filtering in Wireshark makes protocol analysis efficient and clear.

---

## Conclusion
This lab demonstrates how DNS and HTTP traffic can be captured and analyzed using Wireshark. The observations clearly show the security risks associated with unencrypted protocols and reinforce the importance of encrypted communication in modern networks.
