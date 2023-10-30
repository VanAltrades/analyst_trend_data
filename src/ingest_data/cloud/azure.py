# import pyodbc
# import pandas as pd

# def get_azure_db_data(server, database, username, password, sql_query):
#     # Define the connection string
#     connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};User Id={username};Password={password};"

#     try:
#         # Establish a connection to the Azure SQL Database
#         conn = pyodbc.connect(connection_string)
        
#         # Execute the SQL query and fetch the results into a DataFrame
#         df = pd.read_sql_query(sql_query, conn)

#         # Close the database connection
#         conn.close()

#         return df
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#         return None

# # Example usage
# server = "your_server_name.database.windows.net"
# database = "your_database_name"
# username = "your_username"
# password = "your_password"
# sql_query = "SELECT * FROM your_table"
# result_df = get_azure_db_data(server, database, username, password, sql_query)

# if result_df is not None:
#     print(result_df)