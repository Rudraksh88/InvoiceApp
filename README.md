# InvoiceApp

An app that creates printable invoices made using Django with APIs powered by Django REST Framework  

Here are some screenshots:

## Dashboard
This is where you can see all the generated invoices. Click on the INVOICE ID or CUSTOMER NAME to see its details

![invoiceapp-heroku herokuapp com_](https://user-images.githubusercontent.com/62953974/167078572-e2099742-60ca-48c5-8d59-dd3cab6f3902.png)

## Invoice Details
Displays details of a particular invoice. The Print Invoice button opens up the browser's print dialog. 

![invoiceapp-heroku herokuapp com_invoice_a8aeb5a8-5498-40fd-9b4f-bb09a7057c71](https://user-images.githubusercontent.com/62953974/167078672-b0d72495-1674-4877-9491-ec6c07458b4b.png)

![Screenshot 2022-05-06 101031](https://user-images.githubusercontent.com/62953974/167079040-e5400d12-5255-4759-b8e8-bbdb81a7e8f8.png)


## Django Admin 
Manage and create new Invoices using this interface  

Default Admin credentials:    
Username: ```admin```  
Password: ```admin@123```  

![Screenshot 2022-05-06 101803](https://user-images.githubusercontent.com/62953974/167070882-a99ce712-7a43-466f-9a2b-3aaf3ea58300.png)

![invoiceapp-heroku herokuapp com_admin_invoiceapp_invoice_e733148d-1ab9-40ca-b836-a27e6d7dad83_change_](https://user-images.githubusercontent.com/62953974/167070926-05844c7e-a28a-408e-bed2-9565487b7fa4.png)

### Create new Invoice form

Currently new invoices can only be generated via the Django Admin panel or via the API.  
invoice_id and invoice_date are generated automatically when an invoice is created.  

![invoiceapp-heroku herokuapp com_admin_invoiceapp_invoice_add_](https://user-images.githubusercontent.com/62953974/167070978-69e153b6-106f-44a2-8647-28763eeed0b6.png)

## API Guide
### API Endpoints
* ```/api/``` GETs list of all invoices  
* ```/api/get-invoice/{invoice_id}/``` GETs details of a specific invoice  
* ```/api/update/{invoice_id}/{item_name}/``` Updates details of a specific item of a specific invoice  
* ```/api/create/``` Creates a new invoice  

### List of all invoices

```/api/```  

![invoiceapp-heroku herokuapp com_api_](https://user-images.githubusercontent.com/62953974/167071170-e1d9e99f-f5bb-4777-be77-0f71bbbdbc17.png)

### Invoice Details

Example:
To get the invoice details of invoice_id ```a8aeb5a8-5498-40fd-9b4f-bb09a7057c71/```  

```/api/get-invoice/a8aeb5a8-5498-40fd-9b4f-bb09a7057c71/```

![invoiceapp-heroku herokuapp com_api_get-invoice_a8aeb5a8-5498-40fd-9b4f-bb09a7057c71_](https://user-images.githubusercontent.com/62953974/167071476-13c3f576-a530-4d1e-8cee-b1a4d9eab01f.png)

### Update Invoice

Example:
To update the item "PC Cabinet" of the invoice_id ```a8aeb5a8-5498-40fd-9b4f-bb09a7057c71/```  

```/api/update/a8aeb5a8-5498-40fd-9b4f-bb09a7057c71/PC Cabinet```

Format of the PUT request body:
```
{
  "item_name": "PC Cabinet",
  "item_quantity": 1,
  "item_price": 200
}
```

![invoiceapp-heroku herokuapp com_api_update_a8aeb5a8-5498-40fd-9b4f-bb09a7057c71_PC%20Cabinet_](https://user-images.githubusercontent.com/62953974/167071497-6096fa4f-82a5-4927-8ec0-271dbf336f85.png)

### Create Invoice
Example:
Format for the POST request body to create invoice  

```/api/create/```

```
{
    "customer_name": "John Doe",
    "customer_phone": 111666,
    "customer_address": "Palo Alto, California",
    "items": [
        {
            "item_name": "PC Cabinet",
            "item_quantity": 1,
            "item_price": 200
        },
        {
            "item_name": "Motherboard",
            "item_quantity": 1,
            "item_price": 1000
        },
        {
            "item_name": "PSU",
            "item_quantity": 1,
            "item_price": 300
        }
    ]
}
```

![invoiceapp-heroku herokuapp com_api_create_](https://user-images.githubusercontent.com/62953974/167071540-77d4b2c2-1055-430d-a7b5-0be53446ce88.png)
