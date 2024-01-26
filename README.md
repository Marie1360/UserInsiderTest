This is Python UserInsider Test Project  
Instruction to build project and run tests:  
1. Download and install Python 3.10.11  
2. Install latest version of Node.js  
3. Clone and open project with PyCharm and select interpreter (Python 3.10)  
4. Open terminal and run following commands:  
         pip install selenium  
         pip install pytest  
         pip install allure-pytest  
6. To run tests use command:  
         pytest tests/test_userinsider.py  

Instruction to create Allure Report  
1. Open terminal and run following commands:  
         npm install -g allure-commandline --save-dev  
         pytest tests/test_userinsider.py  --alluredir=reportallure  
         allure serve reportallure  
2. Allure Report should be opened!  
![image](https://github.com/Marie1360/UserInsiderTest/assets/61519117/29b99ace-8fc4-417f-a425-fb22d00faeeb)

