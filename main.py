brain_data = {
    "Prefrontal Cortex": [12, 15, 18, 20, 17],
    "Motor Cortex": [25, 27, 30, 28, 26],
    "Visual Cortex": [40, 38, 45, 42, 41],
    "Hippocampus": [10, 11, 13, 12, 14]
}

def average_activation(region_data):
    values = []
    for i in region_data:
        values.append(i)
    average = sum(values)/len(values)
    return(average)

def peak_activation(region_data):
    values = []
    for i in region_data:
        for j in region_data:
            if i < j:
                if i in values:
                    while i in values:
                        values.remove(i)
            if i > j:
                values.append(i)
    for k in values:
        for h in values:
            if k < h:
                if k in values:
                    while k in values:
                        values.remove(k)
            if k > h:
                values.append(k)
    return(values[0])

def summarize_region(region_name, region_data):
    return(f"Region: {region_name}\nAverage Activation: {average_activation(region_data)}\nPeak Activation: {peak_activation(region_data)}")

def most_active_region(brain_full_data):
    averages = []
    for i in brain_full_data:
        averages.append(average_activation(brain_full_data[i]))
    return(peak_activation(averages))

# print(summarize_region("PFC", brain_data["Prefrontal Cortex"]))
print(most_active_region(brain_data))
print("wefw")