##  Rock Music Lives on!  After the success of your recent email campaign,  
##  you're interested in targeting your long standing Rock Music audience!
##  You'll need to collect a list of emails containing each of your Rock Music listeners.

##  Use your query to return the email, first name, last name, and Genre of all Rock Music listeners!
##  Return you list ordered alphabetically by email address starting with A.
##  Can you find a way to deal with duplicate email addresses so no one receives multiple emails?


QUERY ='''
select Customer.Email, Customer.FirstName, Customer.LastName, Genre.Name from Customer join Invoice 
on Customer.CustomerId = Invoice.CustomerId 
join InvoiceLine on Invoice.InvoiceId = InvoiceLine.InvoiceId
join Track on InvoiceLine.TrackId = Track.TrackId
join Genre on Track.GenreId = Genre.GenreId and Genre.Name = 'Rock'
group by Customer.CustomerId
order by Customer.Email 
'''

'''
---VISUAL GUIDE---

Before query...

##############     ###############     #################     ############      ###########
#  Customer  #     #  Invoice    #     #  InvoiceLine  #     #  Track   #      #  Genre  # 
##############     ###############     #################     ############      ###########
| CustomerId | --> | CustomerId  |     |  TrackId      | --> | TrackId  |      |  Name   |
+============+     +=============+     +===============+     +==========+      +=========+
|  Email     |     |  InvoiceId  | --> |  InvoiceId    |     | GenreId  | -->  | GenreId |
+============+     +=============+     +===============+     +==========+      +=========+
|  FirstName |                                                  
+============+
|  LastName  |                                                              
+============+

After query...

###############################################
#                 CustomerGenre               #   <-----RESULT!
###############################################
|  Email  |  FirstName  |  LastName  | Genre  |
+=========+=============+============+========+
'''