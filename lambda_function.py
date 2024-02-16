from utils import read_csv, send_email
import pandas as pd

csv_file_path = 'data.csv'  # Replace 'data.csv' with the path to your CSV file

###############################################################################
#            Using CSV Reader- LEAST RECOMMENDED                              #
#            Reasons-                                                         #
#                    1. Slow read                                             #
#                    2. Data Filtering becomes complex                        #
###############################################################################

csv_handler = read_csv.CSVHandler(csv_file_path)
print(csv_handler.csv_header())

# Define your filter condition,
# e.g., filter rows where the value in the current_version column is 
# not equal to update_to_version column)
def condition(row, value=None):
    # Change the index and condition as per your requirement
    # TO-DO: Design to make it easier.
    return row[3] != row[4]

# Apply the filter
filtered_data = csv_handler.filter_data(condition)

# Print the filtered data
for row in filtered_data:
    print("Result from CSV Reader Started")
    print(row)
    print("Result from CSV Reader Finished")


###############################################################################
#            Using CSV TO Pandas Dataframe- RECOMMENDED                       #
#            Reasons-                                                         #
#                    1. Read Efficient for heavy files                        #
#                    2. Data Filtering becomes super easy                     #
#                    3. Easy to Debug with data visualisation                 #
###############################################################################
    

def csv_to_dataframe(csv_file_path):
    try:
        # Read CSV file into pandas DataFrame
        df = pd.read_csv(csv_file_path)
        return df
    except FileNotFoundError:
        print(f"CSV file '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None

# Convert CSV to DataFrame

def lambda_handler(event, context):
    df = csv_to_dataframe(csv_file_path)

    if df is not None:
        print("DataFrame created successfully:")
        print(df[df['team']=='pintu_k_dada'])
        print("DataFrame filterred Results Finished")
    
    return(df)


# # Example usage:
# smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server
# smtp_port = 587  # Replace with your SMTP port
# sender_email = 'setup_a_service_account@company.com'  # Replace with your email address
# sender_password = ''  # Replace with your email password
# email_sender = EmailSender(smtp_server, smtp_port, sender_email, sender_password)

# receiver_email = 'avengers@company.com'  # Replace with recipient email address
# subject = 'Test Email'
# body = 'This is a test email sent from Python.'

# email_sender.send_email(receiver_email, subject, body)