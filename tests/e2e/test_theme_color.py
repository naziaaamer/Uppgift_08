from playwright.sync_api import Page, expect
import re

"""US8: 
As a user 
I want to change the theme color
so I can use the color options from web.

AC:
User should be able to change the theme color.
User should be able to changed color on screen. 

Test Scenario: 
Go to the web page. 
Click on Dark button. 
Web theme should be changed to dark color. """

BASE_URL = "https://lejonmanen.github.io/timer-vue/"

def test_add_note(page: Page):
    page.goto(BASE_URL)

    website = page.get_by_text("This app was written in Vue 3")
    expect(website).to_be_visible()

    dark_button = page.get_by_role("button", name="Dark")
    dark_button.click()
    page.wait_for_timeout(3000)
    expect(dark_button).to_have_class("ghost selected")

    forest_button = page.get_by_role("button", name="Forest")
    forest_button.click()
    page.wait_for_timeout(3000)
    expect(forest_button).to_have_text("Forest")