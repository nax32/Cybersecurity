# Lab-08: DNS Domain Frequency Analysis (C2-style Detection)

## Objective

The objective of this lab is to analyze DNS traffic from a packet capture (PCAP) file and identify **potential Command-and-Control (C2) communication patterns** using Python.

This lab expands on basic DNS frequency analysis by incorporating:

- DNS query timestamps
- Source IP to domain relationships
- Detection of periodic (beaconing) behavior

The goal is to demonstrate how **simple Python automation** can support **real-world defensive network monitoring**.

---

## Background

Malware often relies on **DNS-based communication** to reach its Command-and-Control (C2) infrastructure. Unlike normal user-driven browsing, C2 traffic typically exhibits:

- Repeated queries to the same domain
- Regular time intervals between queries (beaconing)
- Limited domain diversity per infected host

By analyzing DNS metadata, defenders can often detect suspicious activity **even when payloads are encrypted**.

---

## Tools & Technologies Used

- **Python 3**
- **tshark** (Wireshark command-line tool)
- Python modules:
  - `subprocess`
  - `collections.Counter`
  - `collections.defaultdict`
  - `datetime`
- DNS packet capture file (`dns_real.pcap`)

---

## Lab Environment

- **Traffic Type:** DNS
- **Data Source:** Offline PCAP file
- **Analysis Mode:** Defensive / forensic
- **Network Type:** Controlled lab environment

---

## Lab Workflow

1. Load a DNS PCAP file
2. Extract DNS queries using `tshark`
3. Collect:
   - Query timestamps
   - Source IP addresses
   - Queried domain names
4. Perform frequency analysis on domains
5. Map source IPs to contacted domains
6. Analyze query timing to detect beaconing behavior
7. Flag suspicious domains for further investigation

---

## Detection Techniques Used

### 1. Domain Frequency Analysis
Identifies domains that are queried excessively, which may indicate automated or malicious behavior.

### 2. Source IP → Domain Mapping
Reveals which internal hosts are contacting which domains, helping identify compromised systems.

### 3. Beaconing Detection
Analyzes time intervals between DNS queries to detect periodic communication patterns commonly used by malware.

---

## Files Included

- `dns_analysis.py`  
  Python script that performs DNS extraction, frequency analysis, IP mapping, and beaconing detection.

- `observations.md`  
  Analysis results, findings, and defensive insights from the lab.

- `README.md`  
  Lab overview, objectives, and methodology.

---

## Ethical Notice

This lab is **strictly defensive and educational**.

- No malware is executed
- No exploitation is performed
- All analysis is passive and offline

---

## Lab Status

-  Completed
-  Defensive cybersecurity practice
-  Educational and ethical analysis
