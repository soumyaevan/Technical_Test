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