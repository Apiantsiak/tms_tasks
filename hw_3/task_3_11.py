# Enter the email address. Check domain name. In case it gmail.com, display the mailbox name.
# Otherwise, display the inscription "DOMAIN NAME is not supported".

user_email = input("Enter your email address: ")
domain_name = "gmail.com"

if domain_name in user_email:
    print(user_email)
else:
    print("DOMAIN NAME is not supported")
