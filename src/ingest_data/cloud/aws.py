# import pandas as pd
# import psycopg2  # You may need to install psycopg2 using pip

# def get_aws_db_data(sql_query, db_params):
#     """
#     Execute a SQL query on an AWS database and return the result as a DataFrame.

#     Parameters:
#     - sql_query (str): SQL query string.
#     - db_params (dict): Database connection parameters including host, database name, user, password.

#     Returns:
#     - pd.DataFrame: Result of the SQL query as a DataFrame.
#     """
#     try:
#         # Connect to the database
#         connection = psycopg2.connect(
#             host=db_params['host'],
#             database=db_params['database'],
#             user=db_params['user'],
#             password=db_params['password']
#         )

#         # Execute the SQL query and fetch the result into a DataFrame
#         result_df = pd.read_sql_query(sql_query, connection)

#         # Close the database connection
#         connection.close()

#         return result_df

#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return None

# # Example usage:
# db_params = {
#     'host': 'your_db_host',
#     'database': 'your_db_name',
#     'user': 'your_db_user',
#     'password': 'your_db_password'
# }

# sql_query = "SELECT * FROM your_table"
# dataframe = get_aws_db_data(sql_query, db_params)

# # Print the resulting DataFrame
# print(dataframe)