export PATH=$PATH:/
pytest ./test/test_cases.py --alluredir=./tests/allure
./allure-2.12.1/bin/allure generate ./tests/allure -o ./tests/allure-report --clean
