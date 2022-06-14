# TC/IP Congestion Control: Scalable TCP

## Authors
- Emilio Popovits Blake
- Maximiliano Sapién Fernández
- Patricio Tena Zozaya
- Karen Isabel Morgado Castillo
- Rodrigo Benavente García

## Description
`Scalable_TCP.py` simulates the connection phase of TCP (through a three-way handshake) and the transfer phase of TCP with congestion, using the implemented Scalable TCP TC/IP congestion algorithm.

**Note**: `Scalable_TCP.py` only simulates the Scalable TCP TC/IP congestion algorithm, meaning that, in cases where it's Decrease Procedures would decrease the `cwnd` and `sst` values to values where TCP would instead use TCP Congestion Avoidance, it does not perform the Decrease Procedure so only Scalable TCP is simulated (as standard TCP Congestion is not implemented).

## Requirements
- Python3

## Execution
In order to run this code Python3 must be installed.

To run this code, run the following command on console:
```sh
python Scalable_TCP.py
```

If you want to see more clearly Scalable TCP's Decrease Procedures, in `Scalable_TCP.py` you can comment the following line in the `main` function (line 155):
```py
runSimulation()
```
and un-comment the following line (line 159):
```py
# runSimulation(packets = 100, a_s = 10, b_s = 0.875)
```
which increases Scalable TCP's additive increase from `0.01` (default) to `10`, making it so that the Decrease Procedure can run and decrease `cwnd` and `sst` without running into TCP Congestion Avoidance.