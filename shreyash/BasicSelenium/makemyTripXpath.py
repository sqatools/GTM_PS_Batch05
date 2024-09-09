##MakeMyTripLogo
>>//*[@alt='Make My Trip']    #Xpath without tagname

##Bokking section >> "Hotels"
>> //span[text()='Hotels']     #Xpath without text

##For "ForexCard and Currency
>>//span[contains(@class,'darkGreyText') and text()="Forex Card & Currency"]  #Xpath and or condition

##For Trains
>>//span[contains(@class,'darkGreyText') and text()="Trains"]                #Xpath and or condition

For busses
>>//span[contains(@class,'darkGreyText') and text()="Buses"]                #Xpath and conditions


##Flight Booking "one way round"/ "Multicity"/ "RoundTrip"
>>//*[@class="tabsCircle appendRight5"][1]  #Xpath without tag name
>>(//*[@class="tabsCircle appendRight5"])[3] #Xpath without tag name

>>(//*[@class="tabsCircle appendRight5"])[2] #Xpath without tag name

##Special Fare Container

>>//div[@class="specialFareContainer relative makeFlex centerContainer"] #relative Xpath

>for "select special fare"----------------ask doubt

#For radion button in special fare contain
# For regular/Student/Senoir citizen

>>(//input[@type='radio'])[1]      #used indexing method
>>(//input[@type='radio'])[2]
>>(//input[@type='radio'])[3]

##For Search Tab
>> //a[@class="primaryBtn font24 latoBold widgetSearchBtn "]  #Relative Xpath

##For "explore more"
>>//span[@class="choosFrom__header--text defaultCursor"]    #relative Xpath

##for "Offers"
>>//h2[@class="fontFamilyHeading allCardsHeader"]      #relative Xpath

##for offer section "view all" optons
>>//span[text()="View All"]                            #Xpath with textname

##for "All offers"
>>//a[@class="makeFlex hrtlCenter column darkGreyText"]  #relative Xpath

##For"Bank Offers"
>>//a[@id="superOffersTab_BANK_OFFERS"]                  #relative Xpath

##For "Flights"
>>//a[@id="superOffersTab_FLIGHTS"]                  # relative Xpath

##For Grab 25% flat off"
>>//p[@data-cy="superOfferPtl0"]                     #relative Xpath

##For "Terms and Conditions"
>>(//span[contains(@class,'darkGreyText font12 latoRegular') and text()="T&C's Apply"])[1]  #and condition with indexing
       ### doubt needs to ask

##For "from city"
>>//input[@id="fromCity"]                           #Relative Xpaath

##For "to city"
>>//input[@id="toCity"]                            #relative Xpath

##For "Departure"
>> //span[text()="Departure"]                      #Xpath with texyname

## For "Retur"
>>//span[text()="Return"]                          #Xpath with textname

##For "Trevaellers and cars"
>> //span[text()="Travellers & Class"]            #xpath with textname

##In right corner "For IN|ENG|INR"
>> //span[@class="latoBold capText font11"]         #Relative Xpath

##For login and create account"
>>//li[@data-cy="account"]                           #relattive Xpath

