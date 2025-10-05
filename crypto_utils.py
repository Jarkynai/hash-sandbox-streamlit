import hashlib
import bcrypt
import time
import pandas as pd


def available_algorithms():
return ["MD5", "SHA-1", "SHA-256", "SHA-512", "bcrypt"]


def compute_hash(text: str, algorithm: str, salt: str = "") -> str:
if algorithm == "MD5":
return hashlib.md5(text.encode()).hexdigest()
if algorithm == "SHA-1":
return hashlib.sha1(text.encode()).hexdigest()
if algorithm == "SHA-256":
return hashlib.sha256(text.encode()).hexdigest()
if algorithm == "SHA-512":
return hashlib.sha512(text.encode()).hexdigest()
if algorithm == "bcrypt":
if salt:
full_salt = bcrypt.gensalt()
return bcrypt.hashpw((text + salt).encode(), full_salt).decode()
else:
return bcrypt.hashpw(text.encode(), bcrypt.gensalt()).decode()
raise ValueError("Unknown algorithm")


def compare_hashes(h1: str, h2: str) -> bool:
return h1.strip() == h2.strip()


def benchmark_algorithms(text: str) -> pd.DataFrame:
results = []
for alg in available_algorithms():
start = time.time()
compute_hash(text, alg)
elapsed = time.time() - start
results.append({"algorithm": alg, "time": elapsed})
return pd.DataFrame(results)