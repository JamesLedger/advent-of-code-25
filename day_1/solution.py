
def get_data(data_path):

    data = []

    with open(data_path) as f:
        for line in f:
            data.append(line)

    return data
    
# Part 2 solution
def calculate_zeros(data):
    
    print(f'Calculating number of Zeros for {len(data)} operations')

    # The status starts at 50 
    safe_status = 50
    
    zero_count = 0

    for operation in data:
        direction = operation[0]
        magnitude = int(operation[1:])

        if direction == 'L':
            safe_status = safe_status - magnitude
        if direction == 'R':
            safe_status = safe_status + magnitude

        safe_status = safe_status % 100

        if safe_status == 0:
            zero_count = zero_count + 1


    return zero_count

# Part 2 solution
def calculate_zero_passes(data):
    print(f'Calculating number of Zeros for {len(data)} operations')

    # The status starts at 50 
    safe_status = 50
    
    zero_count = 0

    for operation in data:
        direction = operation[0]
        magnitude = int(operation[1:])

        if direction == 'L':
            safe_status = safe_status - magnitude
        if direction == 'R':
            safe_status = safe_status + magnitude
        
        if safe_status > 99 or safe_status < -99:
            zero_count = zero_count + safe_status // 100

    return zero_count


def main(data_path):
    print("-- AOC Day one -- ")
    data = get_data(data_path)

    zero_count = calculate_zeros(data)
    zero_passes = calculate_zero_passes(data)

    print('--- Dial pointing at zero count ---')
    print(zero_count)

    print('--- Dial pass over zero count ---')
    print(zero_passes)

    return zero_count, zero_passes


if __name__ == "__main__":
    main('input.txt')
