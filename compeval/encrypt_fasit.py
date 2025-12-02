from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("FASIT_KEY")
if KEY is None:
    raise RuntimeError("FASIT_KEY manglar i .env")

fernet = Fernet(KEY.encode())

with open("test_fasit.csv", "rb") as f:
    data = f.read()

encrypted = fernet.encrypt(data)

with open("test_fasit.enc", "wb") as f:
    f.write(encrypted)

print("✅ test_fasit.csv kryptert → test_fasit.enc")
