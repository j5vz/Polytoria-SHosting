import subprocess
import os
import sys

def main():
    # gets the folder where the .exe is sitting cuz yes
    dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    client = os.path.join(dir, "polytoria client.exe")
    map_file = os.path.join(dir, "place.poly")

    if not os.path.exists(client):
        print("[-] Error: Put this exe file in the same folder as your Polytoria client.")
        input("press enter to exit...")
        return

    cmd = [client, "-solo", map_file, "-randomuser"]
    
    try:
        subprocess.Popen(cmd)
        print("[+] Launching Place..")
    except Exception as e:
        print(f"[-] Failed: {e}")
    
if __name__ == "__main__":
    main()
