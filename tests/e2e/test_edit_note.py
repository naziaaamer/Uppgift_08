from playwright.sync_api import Page, expect
import re

"""US7:
As a user 
I want to edit note text 
so I can update or make changes anytime. 

AC:
User should be able to edit note. 
User should be able to save edited changes. 

Test Scenario:
Go to the page.
Click Add note.
Verify the note input/editor appears.
Enter note text.
Click Save/Create/Add.
Verify the note appears on the screen.
Verify the displayed text is exactly what was entered.
Click on note text. 
Edit text. 
Save updated text. 
Verify edited text appears on screen. """

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

    note.locator("h3").click()
    add_text.fill("I want to add a note! update changes")
    page.wait_for_timeout(3000)
    add_text.press("Enter")
    expect(note.locator("h3")).to_have_text("I want to add a note! update changes")