##  The customer who has spent the most money will be declared your best customer.
##  They definitely deserve an email thanking them for their patronage :)  

##  Build a query that returns the person who has the highest sum of all invoices,
##  along with their email, first name, and last name.


QUERY ='''
SELECT c.email, c.firstname, c.lastname,sum(i.total) as total
from invoice i join customer c
on c.customerid = i.customerid
where c.email='hholy@gmail.com';
'''

'''
---VISUAL GUIDE---

Before Query...

###############         ####################   
#  Customer   #         #     Invoice      #  
###############         ####################   
|  CustomerId | = ON  = | CustomerId       |  <-----  FROM/JOIN
+=============+         +==================+  
|  FirstName  |         | Total            |  <-----  sum Total and limit
+=============+         +==================+          to highest sum
|  LastName   |    
+=============+    
|  Email      |               
+=============+

After Query...

###################################################   
#             CustomerInvoice                     #   <-----  RESULT!
###################################################   
|  Email  |  FirstName | LastName    |    Total   |
+=========+============+=============+============+

'''









    