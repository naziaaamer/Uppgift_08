import re

from playwright.sync_api import Page, expect
import re
"""US2:

US1: As a user
I want to add a timer
So I can see timer widgets on screen.

AC:
User should be able to add the timer.
Added timer should be visible to the user.

Test Scenario:
Go to the page.
Click Add timer.
Verify the timer appears on screen."""

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


#US4 Delete timer
def test_delete_timer(page: Page):
    page.goto(BASE_URL)

    website = page.get_by_text("This app was written in Vue 3")
    expect(website).to_be_visible()

    page.get_by_role("button", name="Add timer").click()

    timer_widget = page.locator("div.widget div.timer.paused")
    expect(timer_widget).to_be_visible()
    page.wait_for_timeout(3000)
    expect(timer_widget.locator(".row.time")).to_have_text("15:00")

    timer_widget.locator("div.icon.close").click()
    page.wait_for_timeout(3000)
    expect(timer_widget).not_to_be_visible()