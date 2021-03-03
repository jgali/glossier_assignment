 Approaches :

1) Using a custom python function ( DB credentials can be pulled from some kind of vault without hardcoding )
2) Using Distributed computing like spark on EMR (preferred)
3) AWS glue can be used to load the data plus it can also be used for orchestration
4) Database objects can be migrated using jenkins \flyway(we use it in our current project)

I am using approach 1 becuase i am running locally with only python on my machine
  1) import the json files to staging table without flattening
  2) Once the data is loaded into staging table you can create a view to flattern it. 
  3) Once the data is flattened you can insert or update the data into final consumption table by calling a function or stored procedure 
  4) You can use airflow or lambdas to orchestrate the tasks.
  5) optionally alereting can be done if the job fails. 




To Do :

1) flatten  json array line_items into rows the public.jgali3_assignment_flattern_v
2) Create a function to load the data into the Target table
3) Create a materialized view for rolling up the data for better performance for visualizing
