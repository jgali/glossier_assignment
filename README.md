Two Approaches :

1) Using a custom python function ( DB credentials can be pulled from some kind of vault without hardcoding )
2) Using Distributed computing li

Using any one of the above approaches we can do 2 things 

Import raw json data into postgress staging 
1) Using python jdbc to insert data from s3 into postgress  or 
2) Postgress provides options to import data from s3 ( This is the approach we use 90% of the time ).

2) Once the data is loaded into postgress staging flatten by creating a view and then insert into consumption table 
  depending on if the data is full or deltas you can choose to truncate and load or use merge 

Approach 1 
Import data from s3 to postgress 
  1 Create a postgress function or stored procedure that takes input as 
    a) Bucket name 
    b) File prefix (Because this could be changing everyday if we choose to partition the data based on load date or other keys)
  2) Run the function , This will import the json file into a postgress table 
  3) Create a view that can flatten the json 
  4) insert data from view into consumption table ( If full load truncate and reload ,if deltas then update else insert using merge statement )
    If it is truncate and reload there you can use table swap to minimize the downtime for the consumption table or you can use materialzed view with concurrent refresh 

2) Approach 2 is using python to load the data into postgress . 
