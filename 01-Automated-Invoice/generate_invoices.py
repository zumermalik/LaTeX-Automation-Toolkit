import os
import shutil
import subprocess

# Simulated database of customers and their specific CSV billing files
clients = [
    {"name": "Acme Corporation", "data_file": "acme_items.csv", "output": "Invoice_Acme.pdf"},
    {"name": "Globex Inc.", "data_file": "globex_items.csv", "output": "Invoice_Globex.pdf"}
]

# Note: For this to work in your repo testing, you would need to create 
# 'acme_items.csv' and 'globex_items.csv' based on the items.csv format above.

for client in clients:
    print(f"Generating invoice for {client['name']}...")
    
    # 1. Inject the customer name into a text file for LaTeX to read
    with open("current_customer.txt", "w") as f:
        f.write(client["name"])
        
    # 2. Copy the client's specific data to the generic 'items.csv' that LaTeX expects
    if os.path.exists(client["data_file"]):
        shutil.copy(client["data_file"], "items.csv")
    else:
        # Fallback to the default items.csv for testing
        print(f"  Warning: {client['data_file']} not found. Using default items.csv")

    # 3. Run pdflatex silently
    # We run it twice to ensure any layout formatting is settled
    for _ in range(2):
        subprocess.run(
            ["pdflatex", "-interaction=batchmode", "invoice.tex"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
    # 4. Rename the output PDF to the client's specific invoice name
    if os.path.exists("invoice.pdf"):
        os.rename("invoice.pdf", client["output"])
        print(f"  Success! Saved as {client['output']}")

print("All invoices generated successfully!")