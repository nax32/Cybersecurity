## Detection Signals (Defensive Perspective)

This section outlines practical indicators defenders can use to identify suspicious or automated clients based on HTTP headers and User-Agent behavior.

### Abnormal or Rare User-Agent Strings
- User-Agent values that do not match known browsers or OS patterns
- Outdated browser versions that are no longer common
- Generic or tool-based identifiers (e.g., `curl`, `python-requests`, `Go-http-client`)

**Why it matters:**  
Malware, scanners, and scripts often use default or poorly crafted User-Agents.

---

### Inconsistent Header Sets
- Missing headers typically sent by modern browsers:
  - `Accept-Language`
  - `Accept-Encoding`
  - `Sec-CH-UA*`
- Unusual ordering of headers
- Headers that contradict each other (e.g., mobile UA with desktop-only headers)

**Why it matters:**  
Legitimate browsers have stable, predictable header profiles.

---

### Header Reuse Across Many IPs
- Identical User-Agent and header combinations observed from:
  - Multiple source IPs
  - Different geographic regions
- Especially suspicious when seen over short time windows

**Why it matters:**  
Indicates automation, botnets, or shared malware tooling.

---

### High Request Rate With Static Headers
- Repeated requests using the same User-Agent and headers
- No natural variation over time
- Often combined with:
  - Uniform request intervals
  - Single request paths

**Why it matters:**  
Real browsers naturally change headers across sessions and updates.

---

### Mismatch Between TLS and HTTP Fingerprints
- Browser-like User-Agent paired with:
  - Non-browser TLS fingerprints (JA3)
  - Missing ALPN or modern cipher preferences

**Why it matters:**  
Attackers may spoof HTTP headers but fail to replicate TLS behavior accurately.

---

### Tool-Specific Header Patterns
Common indicators:
- `curl` → Minimal headers, predictable order
- `python-requests` → Fixed header structure
- Custom malware → Hardcoded User-Agent strings

**Why it matters:**  
Many tools leave identifiable fingerprints even when User-Agent is modified.

---

### Lack of Session Continuity
- No cookies set or reused
- No follow-up requests typical of real browsing
- No asset loading (CSS, JS, images)

**Why it matters:**  
Automated clients often perform single-purpose requests without full page interaction.

---

## Defensive Use Cases
These signals can be leveraged in:
- Web Application Firewalls (WAF)
- SIEM correlation rules
- Network Detection & Response (NDR)
- Threat hunting queries
- Bot and scraper detection logic

Detection should rely on **multiple weak signals combined**, not a single indicator.
