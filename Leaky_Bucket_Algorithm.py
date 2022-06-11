if __name__ == '__main__':
    # initial packets in the bucket
    storage = 0
  
    # total no. of times bucket content is checked
    no_of_queries = 4

    # total no. of packets that can
    # be accommodated in the bucket
    bucket_size = 10

    # no. of packets that enters the bucket at a time
    input_pkt_size = 4

    # no. of packets that exits the bucket at a time
    output_pkt_size = 1

    for i in range(0, no_of_queries):  # space left
        size_left = bucket_size - storage
        if(input_pkt_size <= size_left):
            storage += input_pkt_size
            print(f'Buffer size = {storage} out of bucket size = {bucket_size}')
        else:
            print(f'Packet loss = {input_pkt_size - size_left}')
            # full size	
            storage=bucket_size
            print(f'Buffer size = {storage} out of bucket size = {bucket_size}')
        storage -= output_pkt_size