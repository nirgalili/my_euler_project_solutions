from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv = Service("C:/Users/nirga/Downloads/chromedriver_win32/chromedriver.exe")


driver = webdriver.Chrome(service=serv)

url = "https://projecteuler.net/problem=13"

driver.get(url)

numbers = driver.find_element(By.CLASS_NAME, "monospace")

numbers = numbers.text
# print(numbers)


driver.quit()

numbers_list = numbers.split("\n")
# print(numbers_list)

list_sum = 0
for i in numbers_list:
    list_sum += int(i)

# print(list_sum)
list_sum_str = str(list_sum)

first_10_digits_str = ""
for i in range(10):
    first_10_digits_str += f"{list_sum_str[i]}"

first_10_digits_int = int(first_10_digits_str)
print(first_10_digits_int)




