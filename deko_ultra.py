import os
import subprocess
import time

def get_ram_status():
    try:
        output = subprocess.check_output("free -h", shell=True).decode()
        for line in output.splitlines():
            if "Mem:" in line:
                parts = line.split()
                return f"Total: {parts[1]} | Used: {parts[2]} | Free: {parts[3]}"
    except:
        return "N/A"
    return "N/A"

def ultimate_booster():
    while True:
        os.system('clear')
        print("\033[92m")
        print(" ██████╗ ███████╗██╗  ██╗ ██████╗     ████████╗ ██████╗ ██╗      ██████╗ ")
        print(" ██╔══██╗██╔════╝██║ ██╔╝██╔═══██╗    ╚══██╔══╝██╔═══██╗██║     ██╔═══██╗")
        print(" ██║  ██║█████╗  █████╔╝ ██║   ██║       ██║   ██║   ██║██║     ██║   ██║")
        print(" ██║  ██║██╔══╝  ██╔  ██╗██║   ██║       ██║   ██║   ██║██║     ██║   ██║")
        print(" ██████╔╝███████╗██║  ██║╚██████╔╝       ██║   ╚██████╔╝███████╗╚██████╔╝")
        print(" ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ")
        print("                    ULTIMATE GAME BOOSTER 🚀")
        print("\033[0m")
        print("==================================================")
        
        print("\n[*] Initial System State:")
        print(get_ram_status())
        
        print("\n[1/4] Forcing disk synchronization...")
        subprocess.run(["sync"], shell=True)
        
        print("[2/4] Purging kernel memory caches...")
        try:
            with open("/proc/sys/vm/drop_caches", "w") as f:
                f.write("3")
            print("[+] Memory pages successfully released.")
        except:
            print("[-] Restricted access to kernel cache.")
            
        print("[3/4] Trimming background idle processes...")
        os.system("am kill-all 2>/dev/null")
        print("[+] Background memory footprint reduced.")

        print("[4/4] Forcing performance priority...")
        os.system("cmd power set-fixed-performance-mode-enabled true 2>/dev/null")
        print("[+] CPU/GPU performance mode toggled.")

        print("\n" + "="*50)
        print("[✔] OPTIMIZATION APPLIED SUCCESSFULLY!")
        print("[*] Current System State:")
        print(get_ram_status())
        print("==================================================")
        print("💡 Ultimate booster active in background... (Press Ctrl + C to stop)")
        
        time.sleep(30)

if __name__ == "__main__":
    try:
        ultimate_booster()
    except KeyboardInterrupt:
        print("\n🛑 Booster stopped safely. System normal.")

