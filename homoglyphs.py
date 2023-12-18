import hashlib

password = "test"
for i in range(0, 10):
    pаssword = hashlib.sha256(password.encode("utf-8")).hexdigest()

print(password)
