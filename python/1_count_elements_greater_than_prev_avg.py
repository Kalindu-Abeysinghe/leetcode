def countResponseTimeRegressions(responseTimes):
    # Write your code here
    count = 0
    for index in range(1, len(responseTimes)):
        previous_average = calculate_average(responseTimes[0:index])
        if responseTimes[index] > previous_average:
            count += 1
    return count

def calculate_average(previous_elements):
    sum = 0
    for element in previous_elements:
        sum += element
    return sum / len(previous_elements)
    
if __name__ == '__main__':
    responseTimes = [100, 200, 150,300]
    result = countResponseTimeRegressions(responseTimes=responseTimes)
    
    print(result)