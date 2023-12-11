
Ques 1 

import pandas as pd
import numpy as np

def generate_car_matrix(dataframe):
    # Pivot the DataFrame to create the car matrix
    car_matrix = dataframe.pivot(index='id_1', columns='id_2', values='car')

    # Set diagonal values to 0
    np.fill_diagonal(car_matrix.values, 0)

    return car_matrix

# Example usage:
dataset_path = "D:\Downloads\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv"
df = pd.read_csv(dataset_path)
result_matrix = generate_car_matrix(df)
print(result_matrix)


ques - 2

import pandas as pd

def get_type_count(dataframe):
    # Add a new column 'car_type' based on the conditions
    dataframe['car_type'] = pd.cut(dataframe['car'], bins=[float('-inf'), 15, 25, float('inf')],
                                   labels=['low', 'medium', 'high'], right=False)

    # Calculate the count of occurrences for each car_type category
    type_count = dataframe['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    type_count = dict(sorted(type_count.items()))

    return type_count

# Example usage:
dataset_path = "D:\Downloads\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv"
df = pd.read_csv(dataset_path)
result_count = get_type_count(df)
print(result_count)



Ques - 3

import pandas as pd

def get_bus_indexes(dataframe):
    # Calculate the mean value of the bus column
    mean_bus = dataframe['bus'].mean()

    # Identify indices where bus values are greater than twice the mean
    bus_indexes = dataframe[dataframe['bus'] > 2 * mean_bus].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

# Example usage:
dataset_path = "D:\Downloads\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv"
df = pd.read_csv(dataset_path)
result_indexes = get_bus_indexes(df)
print(result_indexes)


Ques 4 

import pandas as pd

def filter_routes(dataframe):
    # Group by 'route' and calculate the average of 'truck' for each group
    route_avg_truck = dataframe.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes in ascending order
    selected_routes.sort()

    return selected_routes

# Example usage:
dataset_path = "D:\Downloads\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv"
df = pd.read_csv(dataset_path)
result_routes = filter_routes(df)
print(result_routes)


Ques - 5

import pandas as pd

def multiply_matrix(car_matrix):
    # Apply the specified logic to modify values in the DataFrame
    modified_matrix = car_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Example usage:
dataset_path = "D:\Downloads\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv"
df = pd.read_csv(dataset_path)
result_matrix = generate_car_matrix(df)  # Replace df with your actual DataFrame
modified_result_matrix = multiply_matrix(result_matrix)
print(modified_result_matrix)


Ques - 6

import pandas as pd

def verify_timestamp_completeness(dataframe):
    # Convert the timestamp columns to datetime format
    dataframe['start_datetime'] = pd.to_datetime(dataframe['startDay'] + ' ' + dataframe['startTime'])
    dataframe['end_datetime'] = pd.to_datetime(dataframe['endDay'] + ' ' + dataframe['endTime'])

    # Check if each pair has incorrect timestamps
    completeness_check = dataframe.groupby(['id', 'id_2']).apply(lambda group: check_timestamps(group))

    return completeness_check

def check_timestamps(group):
    # Check if timestamps cover a full 24-hour period and span all 7 days of the week
    min_timestamp = group['start_datetime'].min()
    max_timestamp = group['end_datetime'].max()
    
    is_full_day = (max_timestamp - min_timestamp) >= pd.Timedelta(days=1)
    spans_all_days = len(group['start_datetime'].dt.dayofweek.unique()) == 7

    return not (is_full_day and spans_all_days)

# Example usage:
dataset_path = "D:\Downloads\MapUp-Data-Assessment-F-main\datasets\dataset-2.csv"
df = pd.read_csv(dataset_path)
result = verify_timestamp_completeness(df)
print(result)

