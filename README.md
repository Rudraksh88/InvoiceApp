# InvoiceApp

An app that creates printable invoices made using Django with APIs powered by Django REST Framework  

Here are some screenshots:

## Dashboard
This is where you can see all the generated invoices. Click on the INVOICE ID or CUSTOMER NAME to see its details

![Screenshot 2022-05-06 100721](https://user-images.githubusercontent.com/62953974/167070302-a0dca20e-f65b-4844-bee3-f94ca1f13b3e.png)

## Invoice Details
Displays details of a particular invoice. The Print Invoice button opens up the browser's print dialog.

![Screenshot 2022-05-06 101019](https://user-images.githubusercontent.com/62953974/167070480-e864942f-2bc9-4701-8601-dd9cb53efe72.png)  

![Screenshot 2022-05-06 101031](https://user-images.githubusercontent.com/62953974/167070747-8be51f0c-a9ed-4db8-a1f0-ba93b90247ae.png)

## Django Admin 
Manage and create new Invoices using this interface  

Default Admin credentials:    
Username: ```admin```  
Password: ```admin@123```  

![Screenshot 2022-05-06 101803](https://user-images.githubusercontent.com/62953974/167070882-a99ce712-7a43-466f-9a2b-3aaf3ea58300.png)

![invoiceapp-heroku herokuapp com_admin_invoiceapp_invoice_e733148d-1ab9-40ca-b836-a27e6d7dad83_change_](https://user-images.githubusercontent.com/62953974/167070926-05844c7e-a28a-408e-bed2-9565487b7fa4.png)

### Create new Invoice form

![invoiceapp-heroku herokuapp com_admin_invoiceapp_invoice_add_](https://user-images.githubusercontent.com/62953974/167070978-69e153b6-106f-44a2-8647-28763eeed0b6.png)

## API Guide
### API Endpoints
* ```/api/``` GETs list of all invoices  
* ```/api/get-invoice/{invoice_id}/``` GETs details of a specific invoice  
* ```/api/update/{invoice_id}/{item_name}/``` Updates details of a specific item of a specific invoice  
* ```/api/create/``` Creates a new invoice  

### List of all invoices

![invoiceapp-heroku herokuapp com_api_](https://user-images.githubusercontent.com/62953974/167071170-e1d9e99f-f5bb-4777-be77-0f71bbbdbc17.png)

### Invoice Details

![invoiceapp-heroku herokuapp com_api_get-invoice_a8aeb5a8-5498-40fd-9b4f-bb09a7057c71_](https://user-images.githubusercontent.com/62953974/167071476-13c3f576-a530-4d1e-8cee-b1a4d9eab01f.png)

### Update Invoice

![invoiceapp-heroku herokuapp com_api_update_a8aeb5a8-5498-40fd-9b4f-bb09a7057c71_PC%20Cabinet_](https://user-images.githubusercontent.com/62953974/167071497-6096fa4f-82a5-4927-8ec0-271dbf336f85.png)

### Create Invoice

![invoiceapp-heroku herokuapp com_api_create_](https://user-images.githubusercontent.com/62953974/167071540-77d4b2c2-1055-430d-a7b5-0be53446ce88.png)
