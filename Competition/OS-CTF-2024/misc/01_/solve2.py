import socket

# Predefined answers for the given questions
answers = {
    "What is the default port for HTTP?": "80",
    "Who invented the World Wide Web?": "Tim Berners-Lee",
    "What does DNS stand for?": "Domain Name System",
    "What is the process of converting data into a coded format called?": "Encryption",
    "What protocol is commonly used for secure communication over the internet?": "HTTPS",
    "What does SQL stand for?": "Structured Query Language",
    "What is a common type of attack that involves injecting malicious code into a website?": "SQL Injection",
    "What type of malware encrypts files and demands payment for their release?": "Ransomware",
    "What is the practice of disguising communication to appear as though it is coming from a trusted source?": "Spoofing",
    "What is a file called that contains a digital certificate?": "Certificate",
    "What term describes the attempt to gain sensitive information by disguising as a trustworthy entity?": "Phishing",
    "What is a network device that filters and monitors incoming and outgoing network traffic?": "Firewall",
    "What type of attack involves overwhelming a system with traffic to disrupt service?": "DDoS",
    "What is the primary protocol used for sending email over the internet?": "SMTP",
    "What does VPN stand for?": "Virtual Private Network",
    "What is the name of the vulnerability that allows arbitrary code execution in software?": "Buffer Overflow",
    "What is the term for a software update that fixes bugs and vulnerabilities?": "Patch",
    "What does MFA stand for in cybersecurity?": "Multi-Factor Authentication",
    "What is a tool that scans a network for open ports and services?": "Nmap",
    "What is the name of the secure file transfer protocol that uses SSH?": "SFTP",
    "What does XSS stand for in web security?": "Cross-Site Scripting"
}

def main():
    host = '34.16.207.52'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        while True:
            data = s.recv(1024).decode()
            print(data)

            if "Answer the following" in data:
                continue

            # Extract the question
            question = data.strip().split("\n")[-1]
            
            if question in answers:
                answer = answers[question]
                print(f"Question: {question}")
                print(f"Answer: {answer}")
                s.sendall((answer + "\n").encode())

            if "Final flag:" in data:
                print("FLAG found!")
                break

if __name__ == "__main__":
    main()
