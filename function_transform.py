import numpy as np
from sklearn.preprocessing import MinMaxScaler

def transform_list(mylist):
  
    listdsl = [1, 0, 0]
    listfb = [0, 1, 0]
    listno = [0, 0, 1]
    listmonthtomonth = [1, 0, 0]
    listoneyear = [0, 1, 0]
    listtwoyear = [0, 0, 1]
    listbta = [1, 0, 0, 0]
    listcca = [0, 1, 0, 0]
    listec = [0, 0, 1, 0]
    listmc = [0, 0, 0, 1]

    # Mapping of values to lists
    value_to_list = {
        'DSL': listdsl,
        'Fiber optic': listfb,
        'No': listno,
        'Month-to-month': listmonthtomonth,
        'One year': listoneyear,
        'Two year': listtwoyear,
        'Bank transfer (automatic)': listbta,
        'Credit card (automatic)': listcca,
        'Electronic check': listec,
        'Mailed check': listmc
    }

    
    index = 16
    value = mylist[index]
    new_list = value_to_list.get(value, [])
    result_list = mylist[:index] + new_list + mylist[index + 1:]

   
    index = 19
    value = result_list[index]
    new_list1 = value_to_list.get(value, [])
    final_list = result_list[:index] + new_list1 + result_list[index + 1:]

  
    index = 22
    value = final_list[index]
    new_list2 = value_to_list.get(value, [])
    last_list = final_list[:index] + new_list2 + final_list[index + 1:]


    mapping = {
        'Male': 0,
        'Female': 1,
        'Yes': 1,
        'No': 0,
        'No phone service': 0
    }


    last_last_list = [mapping.get(item, item) for item in last_list]

 
    last_last_list[1] = int(last_last_list[1])

   
    converted_list = [float(item) if isinstance(item, str) and item.replace('.', '', 1).isdigit() else item for item in last_last_list]
    print(converted_list)
    # Scaling indices 4, 14, 15
    indices_to_scale = [4, 14, 15]
    scaler = MinMaxScaler()

    # Extract values to scale
    values_to_scale = np.array([converted_list[i] for i in indices_to_scale]).reshape(-1, 1)

    # Apply MinMaxScaler
    scaled_values = scaler.fit_transform(values_to_scale)

   
    for i, idx in enumerate(indices_to_scale):
        converted_list[idx] = scaled_values[i, 0]

    return converted_list

# # Example usage
# mylist3 = ['Male', '0', 'No', 'No', '34', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', '56.95', '1889.5', 'Fiber optic', 'Month-to-month', 'Credit card (automatic)']
# result = transform_list(mylist3)
# print(result)
