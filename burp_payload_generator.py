import random
import os


def clear_screen():
    """Clear the console screen"""
    os.system("cls" if os.name == "nt" else "clear")


def generate_numbers():
    """Generate sequential numbers from start to end"""
    print("\n=== NUMBER GENERATOR ===")
    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))
        filename = input("Enter output filename (default: numbers.txt): ").strip()

        if not filename:
            filename = "numbers.txt"

        if not filename.endswith(".txt"):
            filename += ".txt"

        if start > end:
            print("❌ Starting number must be less than or equal to ending number!")
            return

        with open(filename, "w") as f:
            for num in range(start, end + 1):
                f.write(f"{num}\n")

        count = end - start + 1
        print(f"✅ Generated {count} numbers in '{filename}'")

    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"❌ Error: {e}")


def generate_usernames():
    """Generate random usernames from predefined lists"""
    print("\n=== USERNAME GENERATOR ===")

    # Predefined username templates
    base_names = [
        "FemboyHotie",
        "Assassin",
        "PWNED",
        "Hacked",
        "Shadow",
        "Ghost",
        "Anonymous",
        "Admin",
        "Root",
        "User",
        "Guest",
        "Elite",
        "Hacker",
        "System",
        "Master",
        "Killer",
        "Sniper",
        "Ninja",
        "Warrior",
        "Legend",
        "Phantom",
        "Viper",
        "Demon",
        "Angel",
        "Dragon",
        "Phoenix",
        "Wolf",
        "Tiger",
        "Lion",
        "Eagle",
        "Falcon",
        "Raven",
        "Storm",
        "Thunder",
        "Lightning",
        "Blade",
        "Sword",
        "Bullet",
        "Cyber",
        "Digital",
        "Neon",
        "Toxic",
        "Venom",
        "Poison",
        "Death",
        "Dark",
        "Black",
        "Red",
        "Blue",
    ]

    suffixes = [
        "",
        "2000",
        "1337",
        "666",
        "420",
        "69",
        "2023",
        "2024",
        "Pro",
        "X",
        "XxX",
        "YT",
        "TV",
        "Gaming",
        "God",
        "King",
        "Lord",
        "Boss",
        "Chief",
        "Prime",
        "_",
        "123",
        "007",
    ]

    try:
        count = int(input("How many usernames to generate? "))
        filename = input("Enter output filename (default: usernames.txt): ").strip()

        if not filename:
            filename = "usernames.txt"

        if not filename.endswith(".txt"):
            filename += ".txt"

        if count <= 0:
            print("❌ Count must be greater than 0!")
            return

        usernames = []
        for _ in range(count):
            base = random.choice(base_names)
            suffix = random.choice(suffixes)
            username = f"{base}{suffix}"
            usernames.append(username)

        with open(filename, "w") as f:
            for username in usernames:
                f.write(f"{username}\n")

        print(f"✅ Generated {count} usernames in '{filename}'")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"❌ Error: {e}")


def generate_messages():
    """Generate security warning messages"""
    print("\n=== MESSAGE GENERATOR ===")

    messages = [
        "Your website has been exposed to vulnerability please contact your IT department to fix it.",
        "Your API key is exposed in the POST and GET request please fix it.",
        "Critical security vulnerability detected in your application.",
        "SQL injection vulnerability found. Immediate action required.",
        "Cross-Site Scripting (XSS) vulnerability detected on your website.",
        "Your database credentials are exposed in the source code.",
        "Insecure direct object reference found. User data at risk.",
        "Authentication bypass vulnerability discovered.",
        "Your session tokens are vulnerable to hijacking.",
        "Weak password policy detected. Strengthen immediately.",
        "File upload vulnerability allows arbitrary code execution.",
        "Server configuration exposes sensitive information.",
        "Your application is vulnerable to CSRF attacks.",
        "Outdated software components with known vulnerabilities detected.",
        "Insufficient access controls allow privilege escalation.",
        "Your API endpoints lack proper rate limiting.",
        "Sensitive data transmitted without encryption.",
        "Directory traversal vulnerability allows unauthorized file access.",
        "Command injection vulnerability found in user input.",
        "Your cookies are not properly secured with HttpOnly and Secure flags.",
        "XML External Entity (XXE) vulnerability detected.",
        "Server-Side Request Forgery (SSRF) vulnerability found.",
        "Insecure deserialization vulnerability allows remote code execution.",
        "Missing security headers expose your site to attacks.",
        "Your application is vulnerable to clickjacking attacks.",
    ]

    try:
        filename = input("Enter output filename (default: messages.txt): ").strip()

        if not filename:
            filename = "messages.txt"

        if not filename.endswith(".txt"):
            filename += ".txt"

        with open(filename, "w") as f:
            for message in messages:
                f.write(f"{message}\n")

        print(f"✅ Generated {len(messages)} messages in '{filename}'")

    except Exception as e:
        print(f"❌ Error: {e}")


def generate_event_types():
    """Generate event type payloads"""
    print("\n=== EVENT TYPE GENERATOR ===")

    event_types = [
        "vulnerabilityAlert",
        "vulnFound",
        "securityBreach",
        "dataLeak",
        "unauthorized",
        "exploitDetected",
        "xssTriggered",
        "sqlInjection",
        "adminAccess",
        "hackAttempt",
    ]

    try:
        filename = input("Enter output filename (default: event_types.txt): ").strip()

        if not filename:
            filename = "event_types.txt"

        if not filename.endswith(".txt"):
            filename += ".txt"

        with open(filename, "w") as f:
            for event_type in event_types:
                f.write(f"{event_type}\n")

        print(f"✅ Generated {len(event_types)} event types in '{filename}'")

    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """Main menu"""
    while True:
        clear_screen()
        print("╔═══════════════════════════════════════╗")
        print("║   BURP SUITE PAYLOAD GENERATOR        ║")
        print("╚═══════════════════════════════════════╝")
        print("\n[1] Generate Numbers")
        print("[2] Generate Usernames")
        print("[3] Generate Messages")
        print("[4] Generate Event Types")
        print("[5] Exit")
        print("\n" + "=" * 40)

        choice = input("\nSelect option (1-5): ").strip()

        if choice == "1":
            generate_numbers()
        elif choice == "2":
            generate_usernames()
        elif choice == "3":
            generate_messages()
        elif choice == "4":
            generate_event_types()
        elif choice == "5":
            clear_screen()
            print("\n" + "=" * 40)
            print("🔥 Thanks for using Burp Payload Generator! 🔥")
            print("=" * 40)
            print("\n👋 Goodbye! Happy hacking with Burp Suite!")
            print("🎯 Stay safe and hack responsibly!")
            print("💻 Keep testing, keep securing!")
            print("\n" + "=" * 40)
            print("✨ See you next time, hacker! ✨")
            print("=" * 40 + "\n")
            break
        else:
            print("\n❌ Invalid option! Please select 1-5.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
