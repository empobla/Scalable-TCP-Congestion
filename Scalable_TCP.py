from random import randint
from time import sleep

def threeWayHandshake(max_retries):
    '''
    Simulates a three-way handshake between the source and receiver

    :param int max_retries: Max number of retries before the connection is dropped

    :return True if a connection was established, False if a connection was dropped
    '''

    # Send source SYN to the receiver, awaiting receiver's SYN+ACK
    retry_wait = 3  # Retry wait time, initially 3 seconds
    received_synack = False 
    for _ in range(max_retries):
        print('[SOURCE] Sending SYN to receiver...')
        received_synack = True if randint(1, 10) != 1 else False
        
        if received_synack: break
        else:
            print('[SOURCE] Did not receive SYN+ACK from receiver')
            sleep(retry_wait)
            retry_wait *= 2
    
    # If receiver's SYN+ACK was not received before the max retries limit was met, 
    # raise a connection failure
    if not received_synack: 
        print('[SOURCE] Connection Dropped')
        return False

    print('[SOURCE] Received SYN+ACK from receiver')
    
    # Send an ACK from the source to the receiver, acknowledging the receiver
    retry_wait = 3
    received_ack = False
    for _ in range(max_retries):
        print('[SOURCE] Sending ACK to receiver...')
        received_ack = True if randint(1, 10) != 1 else False
        
        if received_ack: break
        else:
            print('[RECEIVER] Did not receive ACK from source')
            sleep(retry_wait)
            retry_wait *= 2

    # If receiver did not receive source's ACK before the max retries limit was met, 
    # raise a connection failure
    if not received_ack: 
        print('[RECEIVER] Connection Dropped')
        return False

    print('[RECEIVER] Received ACK from source')

    # If three way handshake succeeded, return a successful connection so transfer 
    # phase can be initiated
    print('[SOURCE] Connection Established')
    print('[RECEIVER] Connection Established')
    return True

def runSimulation(packets = 100, additive_increase = 0.01, multiplicative_decrease = 0.875):
    '''
    Runs TCP simulation
    
    :param int packets: number of packets (default 100)
    :param float additive_increase: additive increase to use for Scalable TCP (default 0.01)
    :param float multiplicative_decrease: multiplicative decrease to use for Scalable TCP. Must be high above 0.5 and below 1 (default 0.875)

    :return void
    '''

    # Simulate a three way handshake, retrying connection until the retry limit is met.
    connection_established = threeWayHandshake(3)
    
    # If no simulated connection was established, drop connection and return.
    if not connection_established: return

    '''
    When the sst is reached, the source increases cwnd more slowly at a linear rate
    '''
    
    # Assume that cwnd (congestion window) is greater than the low-window threshold for 
    # Scalable TCP, to simulate Scalable TCP procedures
    cwnd_int = 20   # Initial congestion window in packets, set to 20 for simulation purposes
    cwnd = cwnd_int # Congestion window in packets
    sst_int = 25    # Slow start threshold to terminate initial slow start (in packets)
    sst = sst_int   # Current slow start threshold in packets

    # Initialize Scalable TCP symbols
    a_s = additive_increase        # Increase applied to cwnd by Scalable TCP on each ACK
    b_s = multiplicative_decrease  # Percentage residual congestion window applied by Scalable TCP on each loss
    lw_s = 16                      # Low-window threshold for applying Scalable TCP procedures (in packets)

    # While there are still packets to be sent
    while (packets > 0):
        # Select wether to use TCP Congestion Avoidance or Scalable TCP Congestion Avoidance
        # Will always select Scalable TCP Congestion Avoidance for simulation purposes
        use_Scalable_tcp = cwnd > lw_s

        if use_Scalable_tcp:
            print(f'\n[SOURCE] Using Scalable TCP for packets {packets}-{(packets - int(cwnd)) if packets >= int(cwnd) else 0} with a low-window threshold of {lw_s}')

            # Simulate packets received or packet lost
            ack_received = None
            rand_num = randint(1, 10)
            if rand_num == 1:
                ack_received = -1
            elif rand_num == 2:
                ack_received = 0
            else:
                ack_received = 1
            
            # Increase procedure
            # If no packets were lost, increase cwnd by Scalable TCP's fixed value
            if ack_received == 1: 
                print(f'[SOURCE] Successfully sent packets {packets}-{(packets - int(cwnd)) if packets >= int(cwnd) else 0}')
                print(f'[SOURCE] Increasing congestion window threshold from {round(cwnd, 2)} to {round(cwnd + a_s, 2)}')
                # Reduce the number of packets to be sent, simulating that packets were sent
                packets -= int(cwnd)
                cwnd += a_s
                if packets <= 0: break
                continue

            # Decrease procedure
            # If there was a loss notification, reduce the cwnd by Scalable TCP's percentage 
            # residual congestion. Also, set the slow start threshold to the new, lower cwnd 
            # to ensure the flow remains in congestion avoidance
            # 
            # In order to simulate ONLY Scalable TCP, cwnd must not go under the low-window 
            # threshold.
            if ack_received == 0: 
                print(f'[SOURCE] Packet loss recieved on packets {packets}-{(packets - int(cwnd)) if packets >= int(cwnd) else 0}')
                
                if cwnd * b_s < lw_s:
                    print(f'[SIMULATION] Decrease procedure not executed in order to ONLY simulate Scalable TCP')
                    print(f'[SIMULATION] If decrease procedure had been executed, TCP Congestion Avoidance would have run instead')
                    continue

                print(f'[SOURCE] Decreasing congestion window threshold from {round(cwnd, 2)} to {round(cwnd * b_s, 2)}')
                print(f'[SOURCE] Setting slow start threshold to {round(cwnd * b_s, 2)}')
                cwnd *= b_s
                sst = cwnd
                continue
            
            # Timeout procedure
            # Set the slow start threshold to the reduced cwnd and reset the cwnd to its 
            # initial value, meaning that Scalable TCP will reenter slow start until 
            # the cwnd passes the sst and then return to congestion avoidance
            if ack_received == -1:
                print(f'[SOURCE] Timed Out: Setting Slow Start Threshold to {max(cwnd * b_s, cwnd_int)}')
                print(f'[SOURCE] Timed Out: Setting Congestion Window to {cwnd_int}')
                cwnd *= b_s
                sst = max(cwnd, cwnd_int)
                cwnd = cwnd_int
                continue
                    
if __name__ == '__main__':  
    # Run Scalable TCP simulation with default values (from the PDF)
    runSimulation()
    
    # In order to make Scalable TCP's decrease procedure noticeable, run 
    # the simulation with the following values:
    # runSimulation(packets = 100, a_s = 10, b_s = 0.875)  