def parse_instance_counter(path):
    instance_counter = [[] for _ in range(80)]

    with open(path, 'r') as file:
        for row in file:
            pairs = [pair.strip().split() for pair in row.split(",") if pair.strip()]
        