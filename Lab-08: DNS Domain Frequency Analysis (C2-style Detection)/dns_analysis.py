import subprocess
from collections import Counter

pcap_file = "dns_real.pcap"

print("[*] Extracting DNS queries using tshark...\n")

cmd = [
    "tshark",
    "-r", pcap_file,
    "-Y", "dns",
    "-T", "fields",
    "-e", "dns.qry.name"
]

result = subprocess.run(cmd, capture_output=True, text=True)

# Remove empty lines
domains = [d for d in result.stdout.splitlines() if d.strip()]

print(f"[*] Total DNS queries found: {len(domains)}\n")

domain_counts = Counter(domains)

print("DNS DOMAIN FREQUENCY REPORT\n")

for domain, count in domain_counts.most_common():
    if count > 10:
        print(f"[⚠️ SUSPICIOUS] {domain} → {count} queries")
    else:
        print(f"[OK] {domain} → {count} queries")
