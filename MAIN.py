import os
import tkinter as tk
from tkinter import ttk, messagebox
from subprocess import call


# Function to download the package using pip
def download_package():
    package_name = package_dropdown.get()
    download_path = os.path.join(os.getcwd(), "Base Downloads", package_name)
    os.makedirs(download_path, exist_ok=True)
    call(["pip", "download", package_name, "-d", download_path])
    messagebox.showinfo("Download", f"{package_name} downloaded successfully.")


# Function to install the package using pip
def install_package():
    package_name = package_dropdown.get()
    download_path = os.path.join(os.getcwd(), "Base Downloads", package_name)

    # Check if the base packages are installed
    base_packages = ["setuptools", "wheel"]
    for base_package in base_packages:
        call(["pip", "show", base_package])
        if call(["pip", "show", base_package]) != 0:
            call(["pip", "install", base_package])

    if not os.path.exists(download_path):
        download_package()
    else:
        messagebox.showinfo("Install", f"Installing {package_name}...")
        call(["pip", "install", "--no-index", "--find-links", download_path, package_name])
        messagebox.showinfo("Install", f"{package_name} installed successfully.")


# Create the main window
root = tk.Tk()
root.title("Package Installer/Downloader")
root.geometry("300x250")

# Configure style for larger text
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

# Create and place the package dropdown and buttons
package_label = ttk.Label(root, text="Select package:")
package_label.pack()

base_downloads_path = os.path.join(os.getcwd(), "Base Downloads")
package_folders = [folder for folder in os.listdir(base_downloads_path) if
                   os.path.isdir(os.path.join(base_downloads_path, folder))]

package_dropdown = ttk.Combobox(root, values=package_folders)
package_dropdown.pack()

download_button = ttk.Button(root, text="Download", command=download_package)
download_button.pack()

install_button = ttk.Button(root, text="Install", command=install_package)
install_button.pack()

root.mainloop()
