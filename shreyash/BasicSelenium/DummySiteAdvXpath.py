##reference from first name to target trvel details(fromcity):

>>//input[@id="firstname"]//following::input[@id="fromcity"]      #Followwing Method

####reference first name to target Date of Birth:

>>//input[@id="firstname"]//following::input[@id="birthday"]      #Following Method

##reference first name to target Email Radio Button:

>>//input[@id="firstname"]//following::input[@id="eamil"]        #Following Method

##reference first name to Billing Name:

>>//input[@id="firstname"]//following::input[@id="billing_name"] #Following Method

##reference first name to Billing Details:

>>//input[@id="firstname"]//following::h2[text()='Billing Details']   #Following Method

##reference first name to Street Address 2:

>>//input[@id="firstname"]//following::input[@id="street_address2"]    #Following Method

######################################
###### Preceding Method Xpath ########
######################################

## Reference first Name and target "Pasenger details" title:

>>//input[@id="firstname"]//preceding::h2[text()='Passenger Details']

##Reference passenger details to target "car booking and return date" radio button:

>>//h2[text()='Passenger Details']//preceding::span[text()='Cab booking and return date - $600 ']

## reference date of birth to target "Last Name" field:

>>//input[@id="birthday"]//preceding::input[@id='firstname'][1]

##reference Visa Delivery date to Target "Delivery Option" field:

>>//input[@id="visadate"]//preceding::h2[text()='Delivery Option']

######################################
######## Following Sibling ###########
######################################

>>//div[@align="left"]/ul/li[3]//following-sibling::li[1]

>>//div[@align="left"]/ul/li[3]//following-sibling::li[2]

>>//div[@align="left"]/ul/li[1]//following-sibling::li[1]

>>//div[@align="left"]/ul/li[1]//following-sibling::li[2]

>>//div[@align="left"]/ul/li[1]//following-sibling::li[3]


#####################################
####### Following Preceding #########
#####################################

>>