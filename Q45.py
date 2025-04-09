
bits = int(input("Enter number of bits: "))
bytes_val = bits / 8
megabytes = bytes_val / (1024 ** 2)
gigabytes = bytes_val / (1024 ** 3)
terabytes = bytes_val / (1024 ** 4)

print(f"\nConversion from {bits} bits:")
print(f"Megabytes (MB): {megabytes:.6f}")
print(f"Gigabytes (GB): {gigabytes:.6f}")
print(f"Terabytes (TB): {terabytes:.6f}")
# 1 Byte = 8 bits
# 1 KB = 1024 Bytes
# 1 MB = 1024 KB
# 1 GB = 1024 MB
# 1 TB = 1024 GB

bits = int(input("Enter number of bits: "))

# Convert bits to Bytes
bytes_val = bits / 8

# Convert to MB, GB, and TB
megabytes = bytes_val / (1024 ** 2)
gigabytes = bytes_val / (1024 ** 3)
terabytes = bytes_val / (1024 ** 4)

print(f"\nConversion from {bits} bits:")
print(f"Megabytes (MB): {megabytes:.6f}")
print(f"Gigabytes (GB): {gigabytes:.6f}")
print(f"Terabytes (TB): {terabytes:.6f}")
