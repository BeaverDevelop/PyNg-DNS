# V 1.0.2, by https://github.com/BeaverDevelop

from ping3 import ping
import time

print("V 1.0.2, by https://github.com/BeaverDevelop")
time.sleep(3)

# DNS
Google = "8.8.8.8"
ControlD = "76.76.2.0"
Quad9 = "9.9.9.9"
OpenDNS = "208.67.222.222"
Cloudflare = "1.1.1.1"
AdGuard = "94.140.14.14"
ComodoSecure = "8.26.56.26"
Yandex = "77.88.8.8"

# Ping
GoogleResult = ping(Google) * 1000
ControlDresult = ping(ControlD) * 1000
Quad9Result = ping(Quad9) * 1000
OpenDNSresult = ping(OpenDNS) * 1000
CloudflareResult = ping(Cloudflare) * 1000
AdGuardResult = ping(AdGuard) * 1000
ComodoSecureResult = ping(ComodoSecure) * 1000
YandexResult = ping(Yandex) * 1000

# Result
print("\nThe DNS server ping is over. Results:\n\n")
print("Google: ", round(GoogleResult), 'ms')
print("ControlD: ", round(ControlDresult), 'ms')
print("Quad9: ", round(Quad9Result), 'ms')
print("OpenDNS: ", round(OpenDNSresult), 'ms')
print("Cloudflare: ", round(CloudflareResult), 'ms')
print("AdGuard: ", round(AdGuardResult), 'ms')
print("ComodoSecure: ", round(CloudflareResult), 'ms')
print("Yandex: ", round(YandexResult), 'ms')
print("\n\nIf 0 is somewhere, then an error occurred during ping, restart the program")

# Viewing DNS IP Addresses
see_ip = input("\nDo you want to see the IP address lists of all these DNS? (y/n) ")

# if the answer is yes
if see_ip == "y":
    print(f"\nServer ping is over.\n")
    print("Google: ", Google)
    print("ControlD: ", ControlD)
    print("Quad9: ", Quad9)
    print("OpenDNS: ", OpenDNS)
    print("Cloudflare: ", Cloudflare)
    print("AdGuard: ", AdGuard)
    print("ComodoSecure: ", ComodoSecure)
    print("Yandex: ", Yandex)
    input("\nTo close the program, press Enter")

# if the answer is no
if see_ip == "n":
    exit()
