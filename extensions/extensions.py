def main():
    file = input("File name: ").lower().strip()
    print(cmp(file))

def cmp(x):
    if ".jpg" or ".jpeg" in x:
        return "image/jgep"
    elif ".gif" in x:
        return "image/gif"
    elif ".png" in x:
        return "image/png"
    elif ".pdf" in x:
        return "application/pdf"
    elif ".txt" in x:
        return "application/txt"
    elif ".zip" in x:
        return "application/zip"
    else:
        return "application/octet-stream"

main()
