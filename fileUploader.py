import os
import time
import shutil
import subprocess

# Directory paths
watch_folder = "/home/aine/Pictures/Screenshots"  #this is the folder url where the pictures are stores
uploaded_folder = "/home/aine/Pictures/Uploaded"  # this is the path which stores the uploaded pictures

# Upload URL
upload_url = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

# Monitor the folder
def monitor_and_upload():
    while True:
        try:
            # Get list of files in the folder
            files = [f for f in os.listdir(watch_folder) if os.path.isfile(os.path.join(watch_folder, f))]
            
            for file in files:
                file_path = os.path.join(watch_folder, file)
                
                # Execute the curl command
                curl_command = [
                    "curl", "-X", "POST",
                    "-F", f"imageFile=@{file_path}",
                    upload_url
                ]
                result = subprocess.run(curl_command, capture_output=True, text=True)
                
                if result.returncode == 0:  # Check if the upload was successful
                    print(f"Uploaded successfully: {file}")
                    
                    # Move the file to the uploaded folder
                    shutil.move(file_path, os.path.join(uploaded_folder, file))
                else:
                    print(f"Failed to upload {file}: {result.stderr}")
            
            # Wait for 30 seconds
            time.sleep(30)
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
   
    os.makedirs(uploaded_folder, exist_ok=True)
    
    print("Monitoring folder for new images...")
    monitor_and_upload()
