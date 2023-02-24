# Running the test and report generation

## Running the test
1. Open Anaconda Prompt as an administrator.
2. Activate the environment you have created when setting up the environment. In this case, it should be `selenium`.
    ```
   conda activate selenium
   ```
3. Navigate into the folders where the `feature` files are being stored. In my case, my folder is being stored in the following directory. Please adjust as required.
    ```
   cd C:\Users\lmhen\SynologyDrive\GitHub\automated-testing-tutorial\features\test_cases
   ```
4. There are many command line arguments we can use to run our project code. The following are a few common ones I have used so far:
   1. Running a single feature file (assume my feature file is named `1_login.feature`):
   ```
   behave 1_login.feature
   ```
   2. Running the full set of feature files:
   ```
   behave
   ```
   
   3. Running the full set of feature files and generate JUNIT xml test report:
   ```
   behave --junit
   ```
   
## Generate and viewing the report
1. The report will appear in the folder where your `feature` files are. When you navigate to the folder, you will see a new folder created named `reports`. This is where your JUNIT test reports are located.
2. When you open it, you will notice it contains the test results of each feature written in XML format. It also contains information on which step failed and the reason for failure and the input values that caused the test case to fail.
