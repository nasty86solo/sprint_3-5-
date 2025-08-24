import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *



class TestCheckChapterBread:
#переходы к разделам (Булки)
    def test_check_chapter_bread(self, start_from_login_page):
        driver = start_from_login_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sause)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread)).click()
        
        new_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.active_section))
        assert new_element.is_displayed()
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.active_section))
        assert 'Булки' in active_tab.text

class TestCheckChapterSauce:
#переходы к разделам (Соусы)
    def test_check_chapter_sauce(self, start_from_login_page):
        driver = start_from_login_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_sause)).click()
                
        new_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.active_section))
        assert new_element.is_displayed()
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.active_section))
        assert 'Соусы' in active_tab.text
    
class TestCheckChapterFillings:
#переходы к разделам (Начинки)
    def test_check_chapter_fillings(self, start_from_login_page):
        driver = start_from_login_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_fillings)).click()
                
        new_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.active_section))
        assert new_element.is_displayed()
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.active_section))
        assert 'Начинки' in active_tab.text