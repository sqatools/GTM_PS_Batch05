#For Dummy Website

>>>>//h3[contains(text(),'Dumm')]  #with contain partial

>>>>//h1[text()=' Dummy Ticket Booking Website'] #with text

#For Home tab
>>>>//li/a[text()='Home']   # with text

>>>>//li/a[text()='Python Selenium']  #with text

>>>>//li/a[text()='Code Practice']   #with text

>>>>//li/a[text()='Code Practice']

>>>>//li/a[text()='Pytest Framework']  #with text



>>>>//*[text()='Choose the correct option:']   #without tagname
>>(//input[@type="radio"])[1]     #first radio button non indexing
.
.
(//input[@type="radio"])[6]      #sixtg radion button non indexing


>>>>//*[text()='Passenger Details']            #without tagname
>> (//input[@type="radio"])[6]    #used indexing with non sibling radio button
>>(//input[@type="radio"])[7]     #used indexing with non sibling radio button
>>//input[@type="date"]         #relative Xptah
>>(//*[@name="firstname"])[1]   #for first name nond indexing
>>(//*[@name="firstname"])[2]   #for last name non indexing


>>>>//*[text()=' Number of Additional Passangers'] #without tagname


>>>>//*[text()='How will you like to receive the dummy ticket(optional)'] #without tagname
>>(//input[@type="radio"])[10]   #used indexxing for non sibling element radio
>>(//input[@type="radio"])[12]   #same for other 2 radio button

>>>>//h2[text()='Delivery Option']   #with text

>>>>//h2[text()=' Travel Details ']      #with text
>>(//input[@type="radio"])[8]         #usd indexing with non sibling raio button
>>(//input[@type="radio"])[9]         #used indexing with non sibling radio button
>>//input[contains(@name,"departdate")]  #contains with input
>>//input[contains(@name,"returndate")]  #contain with input



>>>>//h2[text()='Billing Details']     #with text
>>//input[contains(@id,'billing_name')] #contains With input
>>//input[contains(@id,'billing_phone')] #contains with input
>>//input[contains(@id,'billing_phone')] #contain with input
>>//input[contains(@id,'billing_email')]  #contain with input
>>//input[contains(@id,'billing_email')]
>>//input[contains(@id,'billing_address')]   #contain with input
>>//input[contains(@name,'postcode')]        #contain with input
>>//input[contains(@name,'prefecture')]     #contain with input
>>//input[@id="street_address1"]            #contain with input
>>//input[@id="street_address2"]            #contain with input



>>>>//h2[text()='Most Visited Cities']  #with text
>>(//input[@type="checkbox"])[1]   #used indexing with non sibling radio button
.
.
>>(//input[@type="checkbox"])[7]  #used indexing with non sibling