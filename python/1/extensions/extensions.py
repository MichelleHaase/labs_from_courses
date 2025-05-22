input = input("File name: ").strip().lower()

if input.endswith(".jpg"):
    print("image/jpeg")
elif input.endswith(".gif"):
    print("image/gif")
elif input.endswith(".jpeg"):
    print("image/jpeg")
elif input.endswith(".png"):
    print("image/png")
elif input.endswith(".pdf"):
    print("application/pdf")
elif input.endswith(".txt"):
    print("text/plain")
elif input.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
