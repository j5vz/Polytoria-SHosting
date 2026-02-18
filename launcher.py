import subprocess
import os
import sys

def main():
    base = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    # finds the first .poly file in the folder automatically
    map_file = next((f for f in os.listdir(base) if f.endswith('.poly')), None)
    # searches for the client (checks common names cuz im lazy)
    client = next((f for f in os.listdir(base) if f.lower() in ["polytoria client.exe", "polytoria.exe"]), None)

    if not client:
        print("[-] Put this in the folder with your Polytoria exe.")
        input(); return
    if not map_file:
        print("[-] No .poly / Polytoria game file found in this folder!")
        input(); return

    print(f"[+] Launching {map_file}...")
    subprocess.Popen([os.path.join(base, client), "-solo", os.path.join(base, map_file), "-randomuser"])

if __name__ == "__main__":
    main()
