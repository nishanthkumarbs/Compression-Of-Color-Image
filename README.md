# Compression of Color Image

This project is a graphical user interface (GUI) application for compressing color images. It uses Python's Tkinter library for the GUI, PIL (Pillow) for image processing, and OS for file handling.

## Features

- **Home**: Main interface for image compression.
- **About**: Information about the application.
- **Load Image**: Load an image for compression.
- **Save Compressed Image**: Save the compressed image with user-defined dimensions and quality.

## Requirements

- Python 3.x
- Tkinter
- PIL (Pillow)
- OS module

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nishanthkumarbs/Compression-Of-Color-Image.git
    cd compression-of-color-image
    ```

2. **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```bash
    python main.py
    ```

## Usage

1. **Load an Image**: Click on the "Load Image" button and select the image you want to compress.
2. **Adjust Settings**: Enter the desired width and height, and adjust the quality using the scale.
3. **Save Compressed Image**: Click the "Save Compressed Image" button, choose the file type (JPEG or PNG), and save the image.


## Code Overview

### main.py

- **CompressionOfColorImage**: Main class for the application, handles the GUI and image compression logic.
  - `__init__`: Initializes the GUI components.
  - `create_sidebar`: Creates the sidebar menu.
  - `create_content_area`: Sets up the main content area.
  - `clear_content`: Clears the content area.
  - `load_image`: Loads an image file.
  - `show_about`: Displays information about the application.
  - `save_compressed_image`: Saves the compressed image.
  - `display_saved_image`: Displays the saved image.

### Example

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = CompressionOfColorImage(root)
    root.mainloop()
```

## Screensots
![image](https://github.com/user-attachments/assets/6476931e-91d7-48d3-bad9-38c2ae56f0bf)

## Contributing

Feel free to fork this project and submit pull requests. Any contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
