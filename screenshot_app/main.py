from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.options import Options
from time import sleep
from datetime import datetime
import flet as ft


def main(page: ft.Page):
    page.title= "Screen Shoot App"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER

    link_obj = ft.TextField(label="Enter url")
    message = ft.Text("Message", size=20, color="white")



    def codeOpps(links):
        
        now = datetime.now()
        time_holder = now.strftime("%H:%M:%S")

        driver = webdriver.Safari()

        driver.get(links)

        image_title = driver.title

        sleep(3)

        image_title = time_holder + image_title + "_mycode.png"

        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)

        driver.set_window_size(S('Width'), S('Height'))

        sleep(5)
        
        screenshot = driver.find_element(By.TAG_NAME,'body').screenshot(image_title)

        if screenshot != '':

            message.value = f"Screen Shot {image_title} was taken"
            message.color = "green"
            message.size = 10

            page.update()

            return 0;
        else:


            message.value = f"Error Screen Shot {image_title} was not taken"
            message.color = "red"
            message.size = 7

            page.update()
            return 1;


    def main_logic():
        link = link_obj.value
        protocol = "https://"

        if link != "":

            if protocol in link:

                codeOpps(link)
            
            else:

                link= protocol+link

                codeOpps(link)
        
            return 0
        else:

            return 1

    def btnLogic(e):

        main_logic()
    

    startBtn = ft.ElevatedButton(text="Start", on_click=btnLogic)

    page.add(ft.Row(
        controls=[
        link_obj,startBtn,message
        ], alignment=ft.MainAxisAlignment.CENTER))
    
    page.update()
ft.app(target=main)