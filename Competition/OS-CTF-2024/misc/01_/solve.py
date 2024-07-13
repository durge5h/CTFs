import socket
import requests
import re

def search_answer(question):
    # Use DuckDuckGo's Instant Answer API
    response = requests.get('https://api.duckduckgo.com/', params={
        'q': question,
        'format': 'json',
        'no_html': 1,
        'skip_disambig': 1
    })
    data = response.json()
    answer = data.get('AbstractText', '')

    # If the instant answer is not available, use related topics as a fallback
    if not answer and 'RelatedTopics' in data and data['RelatedTopics']:
        for topic in data['RelatedTopics']:
            if 'Text' in topic:
                answer = topic['Text']
                break

    return answer if answer else "I don't know"

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

            if "Try the next question." in data or "Correct!" in data:
                question = re.search(r'What .+\?', data)
                if question:
                    question = question.group(0)
                    answer = search_answer(question)
                    print(f"Question: {question}")
                    print(f"Answer: {answer}")
                    s.sendall(answer.encode() + b'\n')
            
            if "FLAG" in data:
                print("FLAG found!")
                break

if __name__ == "__main__":
    main()
