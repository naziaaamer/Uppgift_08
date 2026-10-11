from playwright.sync_api import Page, expect
import re

"""US6:
As a user
I want to start, stop, reset the timer
so I can use all the functionality of timer widget

AC:
User should be able to add timer widget.
User should be able to start the timer.
User should be able to pause the timer.
User should be able to reset the timer.

Test Scenario:
Go to the web page.
Add timer widget.
Start timer. 
Pause timer. 
Reset timer. 
"""

BASE_URL = "https://lejonmanen.github.io/timer-vue/"

def test_add_timer(page: Page):
    page.goto(BASE_URL)

    website = page.get_by_text(re.compile("This app was written in Vue 3"))
    expect(website).to_be_visible()

    page.get_by_role("button", name="Add timer").click()

    timer_widget = page.locator("div.widget div.timer.paused")
    expect(timer_widget).to_be_visible()
    page.wait_for_timeout(3000)
    expect(timer_widget.locator(".row.time")).to_have_text("15:00")

    start_button = page.get_by_role("button", name="Start")
    pause_button = page.get_by_role("button", name="Pause")
    reset_button = page.get_by_role("button", name="Reset")

    start_button.click()
    expect(pause_button).to_be_visible()

    pause_button.click()
    expect(start_button).to_be_visible()

    reset_button.click()
    expect(timer_widget.locator(".row.time")).to_have_text("15:00")