def is_valid_email(email):
    if "@" not in email:
        return False

    local_part, domain_part = email.split("@", 1)

    if not domain_part or "." not in domain_part:
        return False

    # Further checks can be added for more robustness
    if len(local_part) == 0 or len(domain_part.split(".")[0]) == 0:
        return False

    return True

def main():
    inp = input("What's your email address? ")

    if is_valid_email(inp):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
