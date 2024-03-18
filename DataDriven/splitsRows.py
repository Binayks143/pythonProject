import pandas as pd

# Path to the original CSV file
original_file = "C:\\Users\\SC-229-USER\\Desktop\\faraz\\bquxjob_4k.csv"

# Read the original CSV file into a pandas DataFrame
df = pd.read_csv(original_file)

# Split the DataFrame into smaller chunks
chunks = [df[i:i + 100] for i in range(0, df.shape[0], 100)]

# Save each chunk to a separate CSV file
for i, chunk in enumerate(chunks):
    chunk.to_csv(f'C:\\Users\\SC-229-USER\\Desktop\\faraz\\file_{i}.csv', index=False)
