# read the fantasy high transcripts

with open("./transcripts/fh_01_02_03_all.txt", "r") as f:
   full_text = f.read()

# split into chunks
words = full_text.split()
chunk_size = 500
overlap = 80

chunks = []
for i in range(0, len(words), chunk_size - overlap):
    chunk = " ".join(words[i:i + chunk_size])
    chunks.append(chunk)

print(f"turned Fantasy High transcripts into {len(chunks)} chunks.")
