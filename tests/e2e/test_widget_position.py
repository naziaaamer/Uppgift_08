from playwright.sync_api import Page, expect
#import re

#US5
"""As a user
I want to use arrow icon
So I can move up widgets or reposition the widgets.

AC:
User should be able to use arrow icon to change the widget position.

Test Scenario:
Go to the web page.
Add note with text.
Add timer.
Add another note with text.
click on arrow icon.
Widget should move up one position.
click on the arrow icon of the last widget.
Widget should move up only one position."""


BASE_URL = "https://lejonmanen.github.io/timer-vue/"

def test_add_note(page: Page):
    page.goto(BASE_URL)

    website = page.get_by_text("This app was written in Vue 3")
    expect(website).to_be_visible()
    #add note widget
    page.get_by_role("button", name="Add note").click()

    note = page.locator("div.widget div.note")
    note.locator("h3").click()


    add_text = page.get_by_placeholder("Description")
    add_text.fill("I want to add a note")
    add_text.press("Enter")
    expect(note.locator("h3")).to_have_text("I want to add a note")

    # add timer widget
    page.get_by_role("button", name="Add timer").click()

    timer_widget = page.locator("div.widget div.timer.paused")
    expect(timer_widget).to_be_visible()
    page.wait_for_timeout(3000)
    expect(timer_widget.locator(".row.time")).to_have_text("15:00")

    #move up the widget
    arrow_up_icon = timer_widget.locator("div.icon.up svg.svg-up-arrow")
    arrow_up_icon.click()
    expect(timer_widget).to_be_visible()
