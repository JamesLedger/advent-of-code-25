
def get_data(data_path):

    data = []

    with open(data_path) as f:
        for line in f:
            data.append(line)

    return data
    
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

    print(f'safe status: {safe_status}')

    return zero_count


def main(data_path):
    print("-- AOC Day one -- ")
    data = get_data(data_path)

    zero_count = calculate_zeros(data)

    print('--- Zero Count ---')
    print(zero_count)

    return zero_count


if __name__ == "__main__":
    main('input.txt')
