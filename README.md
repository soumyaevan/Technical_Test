## **Test Automation Engineer - technical task**

This automation test suit is selenium and Python test framework - Pytest

#### **Directory structure**
1. Root directory name is Technical_Test
2. Inside that there is **Config** package. Inside it there is  **config.py** file that contains
    the test data and other test related configurations
3. Then there is **Drivers** package. It contains drivers for different browser
4. Next is **Pages** package. It contains elements and actions for different pages. CareersPage class contains the elements for https://www.xeneta.com/careers page. DemoPage contains the elements of https://www.xeneta.com/demo url and CommonPage contains the elements of top and bottom bar and corresponding actions. All of these pages extends the Base Page.
5. **Reports** directory contains the html reports.
6. **Tests** directory contains the test case. Here the **conftest.py** initiates the driver. **Base.py** uses the pytest fixture which is declared in conftest. and the two main test files are **test_CareerPage** and **test_DemoPage**. These both extends the Base.
7. **requirements.txt** file contains all the python modules required to execute these tests.
8. **Technical_Test.xlsx** file contains the functional test cases for bot the test sited. Two sheets have test cases for two sites
9. **Technical_Test.pdf** file is pdf format of the functional test cases


#### **How to Execute**

1. Install Python 3.8 or later
2. Clone this repository
3. Navigate this test directory (Technical_Test)
4. Install pyhton packages from the requirements.txt file. Execute the command `pip install -r requirements.txt`
5. Chromedriver and Firefod drivers are already peresent in Drivers directory. These drivers are for mac OS. To run these tests in Mac OS you may not need to download driver if you are using latest browser. If not then downlaod the driver for the OS in which you want to run the tests and place it in Drivers directory.
6. If you put new drivers make sure you declare the path of the driver in **config.py** file under Config directory.
7. To run the test for demo page execute the following command - `pytest Tests/test_DemoPage.py -v --html=Reports/report_name.html `. this will execute the test and store the report in Reports directory.
8. Similarly to run the test for careers page execute the following command - `pytest Tests/test_CareerPage.py -v --html=Reports/careersReport.html`
9. To run all the tests together execute the following command `pytest Tests -v --html=Reports/summary.html`