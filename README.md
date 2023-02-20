# Automated Testing tutorial

## Setting up your python environment
### Downloads
1. We will be using anaconda to manage our python environments. Install anaconda using this [link](https://www.anaconda.com/products/distribution).
2. We will be using PyCharm for our IDE. Please download it from [here](https://www.jetbrains.com/pycharm/download/#section=windows).

### Setting up
1. Creating your anaconda environment
   1. Open Anaconda Prompt.
   2. Enter the following line of code to create the environment to be used for selenium. In this case, we will name the environment `selenium`.
   >conda create --name selenium python==3.9
   3. Press enter once you are done to create the environment.
   4. Verify if the environment `selenium` has been created by entering the following line of code in the console.
   >conda env list
   5. Once you have confirmed that the environment is created, use the following line of code to activate the environment.
   >conda activate selenium
   6. Install the following commonly used packages in your environment after activating selenium. Please run the following line by line. Ensure you are currently in the `selenium` environment.
   ![Image example of being in `selenium` environment](https://github.com/tingxiao88/Get-Start-with-Selenium/raw/main/readme_assets/conda_activate_selenium.png)
   > pip install selenium
   > 
   > pip install behave
   > 
   > pip install numpy
   > 
   > pip install pandas
   > 
   > pip install beautifulsoup4
   > 
   > pip install lxml
   > 
   > pip install requests
   > 
   > pip install jupyter
   7. Now, add the anaconda environment selenium to Pycharm. You may do this after opening a local copy of this project.
      1. Open PyCharm IDE, then head over to File > Settings.
      ![Image example of navigating to Settings](https://github.com/tingxiao88/Get-Start-with-Selenium/raw/main/readme_assets/pycharm_setting.png)
      2. Click on Project:..., then click on Python Interpreter.
      ![Image example of navigating to Python Interpreter](https://github.com/tingxiao88/Get-Start-with-Selenium/raw/main/readme_assets/pycharm_setting_2.png)
      3. When the Add Python Interpreter window is opened, click on Conda Environment. Choose `Existing environment` and, from the dropdown menu for Intepreter, select the `selenium` environment you have created earlier.
      ![Image example of selecting the correct environment](https://github.com/tingxiao88/Get-Start-with-Selenium/raw/main/readme_assets/pycharm_setting_3.png)
      4. Ensure the environment has been selected for the Python Interpreter before clicking on Apply.
      ![Image example of applying the changes](https://github.com/tingxiao88/Get-Start-with-Selenium/raw/main/readme_assets/pycharm_setting_4.png)

## Setting up chromedriver
1. Check your current Chrome browser version so that we will know which `chromedriver` to install.
   1. Open Google Chrome and click on the three dots at the top right corner of the screen. Select `Help`, followed by `About Google Chrome`.
   ![Image example of checking Google Chrome version](https://github.com/tingxiao88/Get-Start-with-Selenium/raw/main/readme_assets/chrome_version.png)
2. Download the `chromedriver` with the same version as your Google Chrome. You may download it from [here](https://chromedriver.chromium.org/downloads).
![Image example of selecting the correct `chromedriver` to install](https://github.com/tingxiao88/Get-Start-with-Selenium/raw/main/readme_assets/webdrive_download.png)
3. Unzip the contents of the download and move the `chromedriver` to your C: drive.
![Image example of setting up `chromedriver` for use](https://github.com/tingxiao88/Get-Start-with-Selenium/raw/main/readme_assets/c_drive.png)

Now we are ready to start working on our very first selenium test script!