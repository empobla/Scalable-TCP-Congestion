<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Portfolio][moreinfo-shield]][moreinfo-url]
[![Contributors][contributors-shield]][contributors-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">TC/IP Congestion Control: Scalable TCP</h3>

  <p align="center">
    A simulation of the connection phase of TCP (through a three-way handshake) and the transfer phase of TCP with congestion, using the implemented Scalable TCP TC/IP congestion algorithm.
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

`Scalable_TCP.py` simulates the connection phase of TCP (through a three-way handshake) and the transfer phase of TCP with congestion, using the implemented Scalable TCP TC/IP congestion algorithm.

**Note**: `Scalable_TCP.py` only simulates the Scalable TCP TC/IP congestion algorithm, meaning that, in cases where it's Decrease Procedures would decrease the `cwnd` and `sst` values to values where TCP would instead use TCP Congestion Avoidance, it does not perform the Decrease Procedure so only Scalable TCP is simulated (as standard TCP Congestion is not implemented).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/empobla/Scalable-TCP-Congestion.git
   ```
2. Run the script
   ```sh
   python Scalable_TCP.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

When the script is run, it will firstly simulate a three-way handshake:

```sh
[SOURCE] Sending SYN to receiver...
[SOURCE] Received SYN+ACK from receiver
[SOURCE] Sending ACK to receiver...
[RECEIVER] Received ACK from source
[SOURCE] Connection Established
[RECEIVER] Connection Established
```

After establishing the connection through the three-way handshake, it will proceed to simulate the use of Scalable TCP for 100 packets. The program will output to the console the simulation as follows:

```sh
[SOURCE] Using Scalable TCP for packets 100-80 with a low-window threshold of 16
[SOURCE] Timed Out: Setting Slow Start Threshold to 20
[SOURCE] Timed Out: Setting Congestion Window to 20

[SOURCE] Using Scalable TCP for packets 100-80 with a low-window threshold of 16
[SOURCE] Successfully sent packets 100-80
[SOURCE] Increasing congestion window threshold from 20 to 20.01

[SOURCE] Using Scalable TCP for packets 80-60 with a low-window threshold of 16
[SOURCE] Packet loss recieved on packets 80-60
[SOURCE] Decreasing congestion window threshold from 20.01 to 17.51
[SOURCE] Setting slow start threshold to 17.51

[SOURCE] Using Scalable TCP for packets 80-63 with a low-window threshold of 16
[SOURCE] Successfully sent packets 80-63
[SOURCE] Increasing congestion window threshold from 17.51 to 17.52

[SOURCE] Using Scalable TCP for packets 63-46 with a low-window threshold of 16
[SOURCE] Successfully sent packets 63-46
[SOURCE] Increasing congestion window threshold from 17.52 to 17.53

[SOURCE] Using Scalable TCP for packets 46-29 with a low-window threshold of 16
[SOURCE] Successfully sent packets 46-29
[SOURCE] Increasing congestion window threshold from 17.53 to 17.54

[SOURCE] Using Scalable TCP for packets 29-12 with a low-window threshold of 16
[SOURCE] Successfully sent packets 29-12
[SOURCE] Increasing congestion window threshold from 17.54 to 17.55

[SOURCE] Using Scalable TCP for packets 12-0 with a low-window threshold of 16
[SOURCE] Successfully sent packets 12-0
[SOURCE] Increasing congestion window threshold from 17.55 to 17.56
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

This project is property of Emilio Popovits Blake, Maximiliano Sapién Fernández, Patricio Tena Zozaya, Karen Isabel Morgado Castillo, and Rodrigo Benavente García. All rights are reserved. Modification or redistribution of this code must have _explicit_ consent from any owner.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Emilio Popovits Blake - [Contact](https://emilioppv.com/contact)

Maximiliano Sapien Fernández - [Github](https://github.com/Maxsafer)

Patricio Tena Zozaya - [Github](https://github.com/tenapato)

Karen Isabel Morgado Castillo - [Github](https://github.com/Karenisabelmor)

Rodrigo Benavente García - [Github](https://github.com/Rodbena)

Project Link: [https://github.com/empobla/Scalable-TCP-Congestion](https://github.com/empobla/Scalable-TCP-Congestion)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Study of Proposed Internet Congestion Control Mechanisms](https://www.nist.gov/system/files/documents/itl/antd/P9-SP-500-282-Chapter5.pdf)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/empobla/Scalable-TCP-Congestion.svg?style=for-the-badge
[contributors-url]: https://github.com/empobla/Scalable-TCP-Congestion/graphs/contributors
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/emilio-popovits

[Python]: https://img.shields.io/badge/python-3776ab?style=for-the-badge&logo=python&logoColor=ffdc52
[Python-url]: https://www.python.org/

[moreinfo-url]: https://emilioppv.com/projects#tcip-scalable-tcp
[moreinfo-shield]: https://img.shields.io/badge/more%20info-1b1f24?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAApVBMVEUbHyQbHyQbHyRnam2sra+vsbKys7Wsrq+goqQwNDgaHyQaIilbXWGChIZMT1OYmpwYQFoaICYXRF8WUHQZLjwvMzdwcnaztLZ1d3pcX2IaICUXTG0WUHMXS2sXSGcWT3MaKjcpLTFVWFyFh4lTVllvcnWpqqwYOEwZM0QXTW4XTnAaJS8lKS3IycoYPlYaIyt4e36rra60tba5urutr7BQU1cAAAB8HBV3AAAAAnRSTlOR/KrCyFQAAAABYktHRDZHv4jRAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5wEZCiUZVutNzgAAAGpJREFUCNdjYGBkggNGBmQeiM+EAjC5zCwsrGzsHJwQLhc3ExMPLxMfP5OAIBODkLCIqBi/uASHpJS0jCyDnLyCopIyh4qqmrqGphYDk5Q2WLGOrh63PsgoA0NDI2NDE1PsFqFw0RyJ6gUAuK4HVipJCoQAAAAuelRYdGRhdGU6Y3JlYXRlAAAImTMyMDLWNTDUNTINMTSwMja3MjLVNjCwMjAAAEFRBQlQZi6pAAAALnpUWHRkYXRlOm1vZGlmeQAACJkzMjAy1jUw1DUyDTE0sDI2tzIy1TYwsDIwAABBUQUJeVmGIQAAAABJRU5ErkJggg==