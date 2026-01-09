
import pandas as pd
import logging

'''
CSV Headers:
    'customer_id',
    'transaction_date',
    'amount',
    'product_category',
    'store_location'
'''

chunk_size = 1000

def process_file(file_name, output_file):
    try:
        file_data = [] 
        for chunk in pd.read_csv(file_name, chunksize=chunk_size):
            file_data.append(chunk)
        df = pd.concat(file_data)
        
        df.dropna(inplace=True)
        tot_tx_per_customer = df.groupby('customer_id')['amount'].sum()
        print(tot_tx_per_customer)
        
        tot_tx_per_customer.to_csv(output_file)
        logging.info(f'Output wrote to file {output_file}')
    except FileNotFoundError:
        logging.error('Input file not found')
    except:
        logging.error('Unknown error occurred')

process_file('/Users/kalinduabeysinghe/Code/PythonProjects/coding-test/python/sample_data.csv', 'out.csv')