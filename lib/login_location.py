from selenium import webdriver
import unittest
class Login():
   

   def __init__(self, driver):
      
       self.driver = driver
   
   def input_user(self, username):
       
       self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/form/div[1]/div/div/input').clear()
       self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/form/div[1]/div/div/input').send_keys(username)
   
   def input_psw(self,psw):
       
       self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/form/div[2]/div/div/input').clear()
       self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/form/div[2]/div/div/input').send_keys(psw)
       
   def click_button(self):
       
       self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/form/div[3]').click()
    
   def user_location(self):

       self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/ul/div[2]/div/div[1]/a')  
   def login(self, username, psw):
      
       self.input_user(username)
       self.input_psw(psw)
       self.click_button()