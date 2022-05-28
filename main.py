from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(executable_path='geckodriver')

def main():
    url = input('url: ')
    driver.get(url)
    count = int(input('count score: '))
    button = driver.find_element(By.ID, 'button_correct')
    button.click()
    for i in range(0, count):
        # time.sleep(0.1)
        x = int(driver.find_element(By.ID, 'task_x').text)
        y = int(driver.find_element(By.ID, 'task_y').text)
        op = driver.find_element(By.ID, 'task_op').text
        res = driver.find_element(By.ID, 'task_res').text
        if op == '+':
            ans = x+y
        elif op == '–':
            ans = x-y
        elif op == '/':
            ans = x/y
        elif op == '×':
            ans = x*y
        if ans == int(res):
            correct = driver.find_element(By.ID, 'button_correct')
            correct.click()
        else:
            wrong = driver.find_element(By.ID, 'button_wrong')
            wrong.click()
    time.sleep(15)
    driver.close()
    print('Finish')


if __name__ == '__main__':
    main()
