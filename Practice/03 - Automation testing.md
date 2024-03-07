# Practice: Testing the Browser

Now let's start the fun (coding) part! Your mission is to automate the following tests.

First rule: Create every testcase with capture and replay first, then implement with webdriver, and compare your results.
Second rule: In webdriver, try to create future-proof solutions (expect changes in webpages). Be prepared for average changes on the webpage.
Third rule: Do not use the mouse in your exercises. You should not see the cursor move around while the tests are running.

Use your prefered IDE and the following tools: java, maven, junit, selenium webdriver

- First exercise - Navigation:
    - Open the base url. Using the "Menu List" navigate to All Examples/Input Forms/Simpe Form Demo
    - Base url: https://web.archive.org/web/20180926132852/http://www.seleniumeasy.com/test/basic-first-form-demo.html
    - That's it.
    - Make sure that you click on visible menu items.

- Second exercise - Single field & Button:
    - Navigate to Simpe Form Demo. In "Single Input Field" enter a message into the field and click "Show Message" button. Validate that the message appeared.
    - Wasn't that hard, was it?

- Third exercise - Two fields & Output:
    - Navigate to Simpe Form Demo. In "Two Input Fields" enter value A and B and click the "Get Total" button. Validate that the answer is correct.
    - Does your test works even when you enter very large numbers?

- Fourth exercise - Checkbox:
    - Navigate to Checkbox Demo. In "Single Checkbox Demo" check the checkbox and validate the message.
    - Bonus if you write a test for "Multiple Checkbox Demo" and find the bug which is present on the webpage.

- Fifth exercise - Select List:
    - Navigate to Select Dropdown List. In "Select List Demo" select the current day from the dropdown and validate that it's selected.
    - Try out all the way you can select a day.

- Sixth exercise - Radio Buttons:
    - Navigate to Radio buttons Demo. In "Group Radio Buttons Demo" select a combination and click the "Get values" button. Validate the result.
    - Try to run several combinations in one test.

If you finished all of it, congratulations! You can now try to automate date pickers and tables :)


## Advanced (Optional)

- Date Picker - Bootstrap:
	- Navigate to the Bootstrap Date picker in Date Pickers demo
	- Open the "Select Date" picker and validate if 2019 January 14 was a Monday
	- Make your test configurable:
		- Make it possible to select any previous date and validate which day of the week was it e.g.: 2017 Dec 8 and 2015, Jan May 5

- Table - Sort and Search Demo
	- Navigate to the "Sort and Search" menu in the Table demo
	- Validate that the sum age of the 25 oldest employee is 1164