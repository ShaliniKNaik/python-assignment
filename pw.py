import pyperclip
import sys
print("Rajshekar V\n1MJ19CS127")
PASSWORDS = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "luggage": "12345",
}

if len(sys.argv) < 2:
    print("Usage: py pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("\nPassword for " + account + " copied to clipboard.")
    print("\nPassword="+pyperclip.paste()+"\n")
else:
    print("\nThere is no account named " + account+"\n")
