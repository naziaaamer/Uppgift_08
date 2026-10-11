from playwright.sync_api import Page, expect
#import re

"""
US1: As a user
I want to add a note
So I can add note texts and see it on screen.

AC:
User should be able to add/create the note.
Added note should be visible to the user.

Test Scenario:
Go to the page.
Click Add note.
Verify the note input/editor appears.
Enter note text.
Click Save/Create/Add.
Verify the note appears on the screen.
Verify the displayed text is exactly what was entered.
"""


BASE_URL = "https://lejonmanen.github.io/timer-vue/"

def test_add_note(page: Page):
    page.goto(BASE_URL)

    website = page.get_by_text("This app was written in Vue 3")
    expect(website).to_be_visible()

    page.get_by_role("button", name="Add note").click()

    note = page.locator("div.widget div.note")
    note.locator("h3").click()


    add_text = page.get_by_placeholder("Description")
    add_text.fill("I want to add a note")
    add_text.press("Enter")
    expect(note.locator("h3")).to_have_text("I want to add a note")

#US3
def test_delete_note(page: Page):
    page.goto(BASE_URL)

    website = page.get_by_text("This app was written in Vue 3")
    expect(website).to_be_visible()

    page.get_by_role("button", name="Add note").click()

    note = page.locator("div.widget div.note")
    note.locator("h3").click()

    add_text = page.get_by_placeholder("Description")
    add_text.fill("I want to add a note")
    add_text.press("Enter")
    page.wait_for_timeout(3000)
    expect(note.locator("h3")).to_have_text("I want to add a note")

    icon_close = page.locator("div.icon.close ")
    expect(icon_close).to_be_visible()
    icon_close.click()
    page.wait_for_timeout(3000)
    expect(note).not_to_be_visible()