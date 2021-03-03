 Approaches :

1) Using a custom python function ( DB credentials can be pulled from some kind of vault without hardcoding )
2) Using Distributed processing framework like spark on EMR (my choice)
3) AWS glue can be used to load the data plus it can also be used for orchestration

 

First approach is being used because this has been implemented locally on a Mac.
  1) Import the raw json data from the files to a staging table.
  2) Once the data is loaded into staging created a view to flattern the json data. 
  3) Once the data is flattened you can insert or update the data into final consumption tables(orders,users) by calling SQL.




To Do :

1) flatten  json array line_items into rows the public.jgali3_assignment_flattern_v
2) Create a function to load the data into the Target table
3) Create a materialized view for rolling up the data for better performance for visualizing

Suggeestions :

  1) You can use airflow or lambdas to orchestrate the tasks.
  2) optionally alereting can be done if the job fails. 
  3) Database objects can be migrated using jenkins \flyway(we use it in our current project.
  4) In order to achieve operational excellence a framework needs to be in place for logging, auditing, errorhandling ,metrics reporting and alerting(pager) of ETL jobs
  
