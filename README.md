
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Rahulmishra14/DDOS-Simulation-Tool">
    <img src="images/ddos.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Distributed Denial Of Service Attack</h3>

  <br/>
</div>


<!-- ABOUT THE PROJECT -->
# About The Project

### Project Scope

A DDoS attack targets websites and servers by disrupting network services in an attempt to exhaust an application’s resources. The perpetrators behind these attacks flood a site with errant traffic, resulting in poor website functionality or knocking it offline altogether. These types of attacks are on the rise.

DDoS attacks are wide-reaching, targeting all sorts of industries and company sizes worldwide. Certain industries, such as gaming, ecommerce, and telecommunications, are targeted more than others. DDoS attacks are some of the most common cyberthreats, and they can potentially compromise your business, online security, sales, and reputation.

* User should be able to select type of attack he/she wants to simulte.
* The attacked server/service should not be availaible after the attack.

## Project Design

### Architecture

<img src="images/DDoS Arechitecture.jpg" alt="architecture Diagram" >

> Above diagram shows how DDOS attack is simulated.

Distributed Denial of Service (DDoS) is a type of DOS attack where multiple systems, which are trojan infected, target a particular system which causes a DoS attack. 

A DDoS attack uses multiple servers and Internet connections to flood the targeted resource. A DDoS attack is one of the most powerful weapons on the cyber platform. When you come to know about a website being brought down, it generally means it has become a victim of a DDoS attack. This means that the hackers have attacked your website or PC by imposing heavy traffic. Thus, crashing the website or computer due to overloading. 

### Built With
Wrote the firewall using `python3`

### ⚙️ How to Use the Tool
1. **Enter Target**: Input the target IP address or domain name.
2. **Specify Port**: Enter a port number (1-65535).
3. **Choose Attack Type**: Select between TCP, HTTP, or HTTPS.
4. **Define Payload**: Specify the data you want to send during the attack.
5. **Set Interval**: Enter the interval (in seconds) for sending the payload.
6. **Determine Number of Threads**: Decide how many simultaneous threads you want to run.
7. **Start the Attack**: Click the **Start Attack 🚀** button to initiate the simulation.
8. **Stop the Attack**: Click the **Stop Attack 🛑** button to halt all operations.

### ⚠️ Important Notes
- **Responsible Use**: This tool is for educational purposes only. **Never** use it against unauthorized targets.
- **Learning Resource**: Use this tool to understand the impact of DDoS attacks and improve your cybersecurity skills.

## 💻 Code Breakdown
The core functionalities of the tool include:
- **GUI Setup**: Built with Tkinter for an intuitive user interface.
- **Thread Management**: Handles multiple threads to simulate simultaneous requests.
- **Input Validation**: Validates user inputs to ensure proper execution.
- **Asynchronous Flood Functions**: Implements TCP and asynchronous HTTP/HTTPS flood methods.

<div>
<a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="50px" height="21px"></a>
</div>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Ensure you have Python installed on your system along with the following packages. Install them using the following command:

```bash
pip install tkinter requests aiohttp
```

You should have the below software installed in your pc :
* python3
* and your preferred IDE or text editor


### Installation

1. Clone the repo
   git clone https://github.com/Rahulmishra14/DDOS-Simulation-Tool.git

2. Open project in IDE or text editor


<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- CONTACT -->
## Contact

> Rahul Mishra  - <rahulmishra02022001@gmail.com>

Project Link: [https://github.com/Rahulmishra14/DDOS-Simulation-Tool](https://github.com/Rahulmishra14/DDOS-Simulation-Tool)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

