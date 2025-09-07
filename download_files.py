import requests
import os
import argparse

def download_files(base_url, filename_prefix, start_seq, end_seq, filename_suffix, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert start_seq and end_seq to integers for iteration
    start_seq_int = int(start_seq)
    end_seq_int = int(end_seq)

    # Determine the length of the sequence numbers
    seq_length = len(start_seq)

    for i in range(start_seq_int, end_seq_int + 1):
        # Generate the filename with leading zeros if necessary
        seq_str = str(i).zfill(seq_length)
        filename = f"{filename_prefix}{seq_str}{filename_suffix}"
        file_url = f"{base_url}/{filename}"
        output_path = os.path.join(output_dir, filename)

        try:
            response = requests.get(file_url)
            response.raise_for_status()  # Check if the request was successful

            with open(output_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {filename}: {e}")

if __name__ == "__main__":
    
    #parser = argparse.ArgumentParser(description="Download multiple files from a website.")
    #parser.add_argument("base_url", help="The base URL of the files to download.")
    #parser.add_argument("filename_prefix", help="The prefix of the filenames (can be empty).")
    #parser.add_argument("start_seq", help="The start sequence number (as a string).")
    #parser.add_argument("end_seq", help="The end sequence number (as a string).")
    #parser.add_argument("filename_suffix", help="The suffix of the filenames.")
    #parser.add_argument("output_dir", help="The directory to save the downloaded files.")

    #args = parser.parse_args()

#    download_files(args.base_url, args.filename_prefix, args.start_seq, args.end_seq, args.filename_suffix, args.output_dir)
    download_files("http://www.9610.com/qinhan/yyb/", "", "001", "041", ".jpg", "D:\My Pictures\calligraphy\乙瑛碑")

# Usage: python download_files.py http://example.com file_ 1 10 .txt output
#base_url="http://www.9610.com/qinhan/yyb/" start_seq="001" end_seq="047" filename_suffix=".jpg" output_dir="D:\My Pictures\calligraphy\yiyingbei"