import re

n_barcodes = int(input())
product_group = "00"
validation_pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
for _ in range(n_barcodes):
    barcode = input()
    match = re.match(validation_pattern, barcode)
    if not match:
        print("Invalid barcode")
        continue
    digit_match = re.findall(r"\d", barcode)
    if digit_match:
        product_group = "".join(digit_match)
    print(f"Product group: {product_group}")
    product_group = "00"
