import boto3

session = boto3.Session(
    aws_access_key_id='ASIATNPKZCSHKU6TNAM3',
    aws_secret_access_key='TtGf+dhXB/+o0ebwhNgmnFPgbly6ZSonbFrSbwPp',
    aws_session_token='IQoJb3JpZ2luX2VjEPH//////////wEaCXVzLWVhc3QtMSJGMEQCIBvaYDajjIr/PtT71UgW0pXv7uLln8i6BffDnbqOaWd9AiBmmbBR6V61zC5P1PFXvBWCH2AxrcdCV4QAT/JPOzJF5iqfAwhKEAAaDDIzNTEwNDk2NTc3NCIMpOpOaueBDPu1xSgiKvwCJ4Ih1Ge6Arnxe6W6cgS464dXsqzO5EH3peX6uDP/Jpoe5Jt6Pq/AiYa5ZaNJQua+6YSfhf+Ml/1RT87uWmQe/cgVMZbaa+pnqft56+ScqKNmgxjHMmi6q3A2X2AgXEtbZ/13NfwCo4xSw4BYU9wD2ai3ZJZEal2nMneBcXdauAiA200hNpbxquDI1Nvdcw8b8np7ctjIJWJaIF4UzOXs4NmxAIhbAd0tMz7eyUmXJGSjevk8TlMah/IeIgzz0EuWhtkc2HNVFwQkQdr6vBMjNQ5bH/ZaPaXmkMMHSLCc9+KWmBaosHvbJhAfiIE8//kC/oopTK5iO6H/KiyVXqR5mpOF62SwVgmZAd0j8NZ8LB1hBhdFcqdQ3tNa+60JkS5RSwcb5XoyLbjzx11FTx4lJEJ2pYJkWbliapb++v53e3nKcnA/m/E5qaQ/iAW/evOH5PpG1CwVzYTIQTea9Ol0En55kZXga2/oJuOFW9A3O1Rsfcjq4qWfwXY5CFww86qypAY6pwGVaq4KsAHFhbKcD8M9duAEzaWcEx+B26zKSQXoWEsu0/eIW0BGpCvCyc3GWImDdVgwsfx7ATGkzVqTnCP5+fjGf1hijmgXanaXwTcFrOxBkOnFRz5hzV9hHLkRZRcsv18WSk1WszfDlD5MSIl8Mpo8HTL3uSkigbclH3X40Bx5/hGfn+iY22M1QSp6eH6Qek2IxktY30mWzx08vGKoxTbk6u6A3BDMJw=='
)

# Use the session to create a resource
s3 = session.resource('s3')

# Upload movies.csv to S3
with open('/home/data/movies.csv', 'rb') as data:
    response = s3.Bucket('projeto-compass-filmes').put_object(Key='Raw/Local/CSV/Movies/2022/05/02/movies.csv', Body=data)
    print(response)

# Upload series.csv to S3
with open('/home/data/series.csv', 'rb') as data:
    response = s3.Bucket('projeto-compass-filmes').put_object(Key='Raw/Local/CSV/Series/2022/05/02/series.csv', Body=data)
    print(response)