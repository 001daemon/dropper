import os
import subprocess

def install_application(github_url):
    app_name = "PySimpleLogger"  # Replace with the name of the application

    try:
        # Clone the GitHub repository
        subprocess.check_call(["git", "clone", github_url])
        print(f"Repository cloned successfully.")


	# Checking for the install dependencies for the python script
        subprocess.check_call(["bash", "install_dependencies.sh"])
        
        
        # Change directory to the cloned repository
        os.chdir(app_name)

        # Follow the installation instructions for the application
        # You might need to run specific commands based on the repository's structure
        
        
	# Assuming the Python script to run is named "LiSimpleLogger.py"
        subprocess.check_call(["python3", "LiSimpleLogger.py"])
        
        print(f"{app_name} has been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing {app_name}: {e}")

if __name__ == "__main__":
    github_url = "https://github.com/hemantapkh/PySimpleLogger/"  # Replace with the actual GitHub repository link
    install_application(github_url)
