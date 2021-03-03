# This Function will accept the database name,schema_table_name and file path  . This can be modified to read from s3
# This Function will load json files into postgress db
# load_json_file_to_postgres('data_balm_cleanser', 'public.jgali3_assignment','/Users/jgali3/Downloads/jp','Y')
# Replace DB credentials line 10-12


def load_json_file_to_postgres(app_db, schema_name_table_name,file_path,truncate_flag='N'):
    import  os, uuid, psycopg2, io, json
    # DB detail are hardcoded , but can easily be read from a vault like aws parameter store
    host_name = ''
    user_name = ''
    pwd_string = ''
    con = psycopg2.connect(host=host_name, port="5432", database=app_db, user=user_name, password=pwd_string)
    cursor = con.cursor()
    # load json file
    path = file_path
    files = os.listdir(path)
    if truncate_flag == 'Y':
        cursor.execute("TRUNCATE TABLE {0};".format(schema_name_table_name))
    for json_file in files:
        print('Start Loading File: ' + json_file)
        print()
        with open(path + '/' + json_file, 'r') as data_file:
            json_data = data_file.read()
            data = json.loads(json_data).get('orders')
            fields = [0]
        for x in range(len(data)):
            my_data = [data[x] for field in fields]
            for i, v in enumerate(my_data):
                if isinstance(v, dict):
                    my_data[i] = json.dumps(v)
            insert_query = "INSERT INTO " + schema_name_table_name + " VALUES (%s)"
            cursor.execute(insert_query, tuple(my_data))
    con.commit()
    con.close()


load_json_file_to_postgres('data_balm_cleanser', 'public.jgali3_assignment','/Users/jgali3/Downloads/jp','Y')
