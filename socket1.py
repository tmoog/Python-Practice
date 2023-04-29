import socket

def assignment_12_1():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    
    #Change this url
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    response = ''

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        line = (data.decode())
        response += line
    
    response = response.splitlines()
    
    status, headers, body = separate_status_headers_and_body(response)
    
    print('Status:')
    print(status)
    
    print('Headers:')
    print(*headers, sep="\n")
    
    print('\nData:')
    print(*body, sep="\n")


    mysock.close()

def separate_status_headers_and_body(response):
    headers = []
    rest = []

    for line in response:
        if ":" in line:
            headers.append(line)
        else:
            rest.append(line)
    status = rest[0]
    body = rest[2:]

    return status, headers, body


if __name__ == "__main__":    
    assignment_12_1()
