test:
	pytest

test-allure:
	pytest --alluredir=./results/my_allure_results

serve-allure-report:
	allure serve ./results/my_allure_results