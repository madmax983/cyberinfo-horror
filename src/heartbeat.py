import sys
import time
import os

def pulse():
    """
    Simulates a heartbeat visualization using ANSI escape codes.
    The text pulses red and expands/contracts.
    """
    try:
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        red = "\033[31m"
        bold = "\033[1m"
        reset = "\033[0m"
        dim = "\033[2m"

        heart = [
            "  ** **  ",
            " ******* ",
            " ******* ",
            "  *****  ",
            "   ***   ",
            "    *    "
        ]

        # Beat pattern: Thump-Thump... pause... Thump-Thump...
        print(f"\n{red}[SYSTEM]: SYNCING WITH HOST BIOMETRICS...{reset}\n")
        time.sleep(1)

        for _ in range(5): # 5 cycles of double beats
            # First Thump
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{red}{bold}[SYSTEM]: CONNECTED.{reset}\n")
            print(f"{red}{bold}   THUMP{reset}")
            for line in heart:
                print(f"{red}{bold}  {line}{reset}")
            time.sleep(0.1)

            # Brief pause
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{red}{dim}[SYSTEM]: CONNECTED.{reset}\n")
            for line in heart:
                print(f"{red}{dim} {line}{reset}")
            time.sleep(0.1)

            # Second Thump
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{red}{bold}[SYSTEM]: CONNECTED.{reset}\n")
            print(f"{red}{bold}   THUMP{reset}")
            for line in heart:
                print(f"{red}{bold}  {line}{reset}")
            time.sleep(0.1)

            # Rest
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{red}{dim}[SYSTEM]: CONNECTED.{reset}\n")
            print("")
            for line in heart:
                print(f"{dim} {line}{reset}")
            time.sleep(0.8)

        print(f"\n{red}[SYSTEM]: SYNCHRONIZATION COMPLETE.{reset}")
        print(f"{bold}We are running on your time now.{reset}\n")

    except KeyboardInterrupt:
        print(f"\n{red}[ERROR]: CANNOT STOP THE HEART.{reset}")

if __name__ == "__main__":
    pulse()
