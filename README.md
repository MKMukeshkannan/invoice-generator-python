<h1>INVOICE GENERATOR USING PYTHON</h1>

![Invoice-generator-python](https://user-images.githubusercontent.com/119940345/206175540-da1d1119-b816-4928-a129-d6a69e78cfdf.png)
<p> <strong>An Invoicing Software</strong> that enables the user to create an invoice via
an User-friendly-Graphical User Interface <em>(using tkinter module in python) </em>. It allows the user to enter the
customer details, (like customer name, customer id, phone number), invoice
number, date of delivery, details of the products purchased by the customer
(like product id, product name, quantity and unit price of the product) and
calculate the total value of the product purchased by the customer. This software
also saves these invoices details into MySQL server for ease of management of
data.</p>
<h3>Required Applications</h3>
  <ul>
      <li> <a href="https://www.python.org/" target = "_blank">Python IDLE</a>  (any other python IDEs)</li>
      <li> <a href="https://www.mysql.com/" target = "_blank">MySQL</a></li>


  </ul>
<h3>Required Python Modules</h3>
  <ul>
    <li> <a href="https://docs.python.org/3/library/tkinter.html" target = "_blank">Tkinter</a> </li>
    <li> <a href="https://pypi.org/project/mysql-connector-python/" target = "_blank">MySQL Connector</a> </li>

  </ul>
  
<h3>DESCRIPTION</h3>
    <p>This is a simple invoice generating software using python, that can receive customer details from the user as inputs (The date must be given in <strong>YYYY/MM/DD</strong> format).
     We need to enter the product details in feilds given at the bottom of the software. The software have constraints to check whether the user is giving valid inputs (like
     Quantity and unit prices are entered in number and no feild is left empty). Now, Click <strong><a href="#insert">INSERT PRODUCT"</a></strong> buttton to insert the products into the dashboard
     we can also select the product from the dashboard and click <strong>"REMOVE PRODUCT"</strong> button to remove that product.We can see that the software 
     fills the total column automatically
     and by clicking <strong><a href = "#gst">TOTAL BUTTON</a></strong> " at the bottom the software adds all the price of inserted products and calculates GST (Goods and Service Tax as per indian tax norms) 
     of the products. <strong><a href = "#sve">"SAVE"</a></strong> Button allows the user to save all the data into the DBMS database.
     </p>
     
<h3>Room for Improvement</h3>
<p>This project has a long way to go. we can add complete inventory control feature that keeps deducts product count from inventory database as we make an invoice.
This feature will help us to maintain <em>inventory stock</em> easy.we can make the software generate the invoice in <em>pdf format</em> so that it can be printed.An feature to 
make complete sale report annually and for each customer separately and many more......</p>
     
     
     
     
     
<h3>SCREENSHOTS OF WORKING</h3>






![1](https://user-images.githubusercontent.com/119940345/206175897-d4fcf19a-42ad-4d80-9dba-66523f860ddb.png)
![2](https://user-images.githubusercontent.com/119940345/206175904-f7f7c356-8144-44bf-848c-0f4a121cc2ef.png)
![4](https://user-images.githubusercontent.com/119940345/206175905-7de29bbb-3030-4001-a761-015713d7cf08.png)




<h1 id = "insert"></h1>





![5](https://user-images.githubusercontent.com/119940345/206175909-6f6fc46f-a07f-410c-b822-befb5772cbbc.png)




<h1 id = "gst"></h1>




![6](https://user-images.githubusercontent.com/119940345/206175911-f840debb-bd09-4f36-96dc-83657f19ff18.png)
![7](https://user-images.githubusercontent.com/119940345/206175915-d30874fb-6b57-4e0b-bb31-6ea129d0cc71.png)





<h1 id = "sve"></h1>







![8](https://user-images.githubusercontent.com/119940345/206175922-6fd41871-933b-4686-99c0-21b6e4263535.png)
![9](https://user-images.githubusercontent.com/119940345/206175925-bd9c3b94-d808-495d-835a-6d5de8e6fe19.png)
![10](https://user-images.githubusercontent.com/119940345/206175926-5099e9f2-106e-41c0-9eab-24da6f74982d.png)



