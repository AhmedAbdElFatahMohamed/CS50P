name=input("File Name:").lower().strip()
if name.endswith('gif'):
    print("image/gif")
elif name.endswith('pdf'):
    print("application/pdf")
elif name.endswith('txt'):
    print("text/plain")
elif name.endswith('zip'):
    print("application/zip")
elif name.endswith('jpg') or name.endswith('jpeg'):
    print("image/jpeg")
elif name.endswith('png'):
  print("image/png")
else:
    print("application/octet-stream")