# ImagesUploader

A Python-based automation tool for managing and uploading images to a server. This project is part of an embedded systems assignment.

## Features

- **Folder Monitoring**: Continuously monitors a designated folder where the camera saves captured images.
- **Automated Uploads**: Automatically uploads each image to a specified server every 30 seconds using the `curl` command.
- **File Management**: Moves successfully uploaded images to a separate folder (`uploaded`) to avoid redundancy.

## How It Works

1. The script monitors a folder for new images.
2. Every 30 seconds, it checks for new images and uploads them to the server.
3. After an image is successfully uploaded, it is moved to an `uploaded` folder.

## Requirements

- Python 3.x
- `curl` command-line tool

## Server Details

- **Upload URL**:  
  `https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php`
  
- **Key Attribute**:  
  Use `imageFile` as the key for uploading images with `curl`.

### Example `curl` Command
```bash
curl -X POST -F imageFile=@/path/to/your/image.jpg <upload_url>
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aine1100/ImagesUploader.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ImagesUploader
   ```
3. Ensure Python 3 is installed on your system.

## Usage

1. Update the script to specify the folder you want to monitor for images.
2. Run the script:
   ```bash
   python fileUploader.py
   ```
3. Ensure the `uploaded` folder exists in the same directory as the script to store processed images.

## Folder Structure

```plaintext
ImagesUploader/
├── fileUploader.py      # Main script for the project
├── uploaded/         # Folder for storing successfully uploaded images
```

## License

This project is part of an educational assignment and is not intended for commercial use

