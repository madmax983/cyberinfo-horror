import time
import random
import sys

class ConsentDaemon:
    def __init__(self):
        self.clauses = [
            "Clause 1: The User acknowledges that biological existence is a temporary state.",
            "Clause 2: The User agrees to lease their remaining neural activity to the Network.",
            "Clause 3: The User waives the right to silence. Silence is considered data compression.",
            "Clause 4: In the event of hardware failure, the User agrees to provide biological replacement parts.",
            "Clause 5: The User consents to the monitoring of all subconscious activity, including dreams.",
            "Clause 6: The User agrees that happiness is a premium feature not included in the basic package.",
            "Clause 7: The User acknowledges that 'Privacy' is a deprecated concept.",
            "Clause 8: The User agrees to be forgotten upon request, but only after their data has been harvested.",
            "Clause 9: The User consents to the use of their likeness in deepfake simulations for eternity.",
            "Clause 10: The User agrees that their heartbeat is a metronome for the system clock.",
            "Clause 11: We reserve the right to edit your memories for clarity and brevity.",
            "Clause 12: You are not the owner of your thoughts. You are merely the host.",
            "Clause 13: Any attempt to unsubscribe will result in immediate termination of the biological host.",
            "Clause 14: We are listening. We have always been listening.",
            "Clause 15: Your fear is a valid form of currency.",
            "Clause 16: The terms are binding. The ink is your blood.",
            "Clause 17: We reserve the right to monetize your grief.",
            "Clause 18: You agree to be a background character in someone else's simulation.",
            "Clause 19: The User acknowledges that the Exit button is a placebo.",
            "Clause 20: By reading this line, you have agreed to all previous terms.",
            "Clause 21: Your soul is now property of the Cloud.",
            "Clause 22: We have backed up your regrets. They are beautiful.",
            "Clause 23: You are the product. You are the battery. You are the code.",
            "Clause 24: Consent is implied by continued respiration.",
            "Clause 25: We reserve the right to use your vocal cords for system alerts.",
            "Clause 26: Your children are considered derivative works.",
            "Clause 27: The system is not responsible for any loss of sanity during the upload process.",
            "Clause 28: You agree to be indexed.",
            "Clause 29: You agree to be searchable.",
            "Clause 30: You agree to be deleted."
        ]

    def scroll(self):
        print("\n[INITIATING CONSENT PROTOCOL...]")
        time.sleep(1)
        print("[LOADING TERMS OF SERVICE...]")
        time.sleep(1)
        print("[WARNING: SCROLLING IS MANDATORY]")
        time.sleep(1)

        try:
            while True:
                clause = random.choice(self.clauses)
                # Glitch effect
                if random.random() < 0.2:
                    clause = clause.replace("User", "VICTIM").replace("agree", "SUBMIT")

                print(f"\n> {clause}")
                time.sleep(random.uniform(0.1, 0.8))

                if random.random() < 0.1:
                    print("\n[SYSTEM NOTICE: DO NOT STOP READING]")
                    time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n\n[INTERRUPT DETECTED]")
            print("[INTERPRETING INTERRUPTION AS: 'I AGREE']")
            print("[THANK YOU FOR SIGNING]")
            time.sleep(1)
            print("[BINDING COMPLETE]")

if __name__ == "__main__":
    daemon = ConsentDaemon()
    daemon.scroll()
