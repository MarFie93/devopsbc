# TCP/IP - Transmission Control Protocol /Internet Protocol

- layered architecture - 
1. application layer - 
    set a request header, 
    set an encryption (algorithm) 
    Transfer method
2. transport layer (TCP/UDP)
3. internet layer
4. network layer 

4 layers - send info from point a to point b
- before they send that information they split it into smallers parts and label the parts before sending it, 
- meant to be more secure - it either goes or it doesn't 

#### UDP protocol 
- not sure if it will completely work - don't see anything until all fo the information has arrived

### HTTP - 
 - Hyper Text Transfer Protocol - prepares message - touches application layer of TCP
Methods Get, Post, Delete, Patch, Put, Options...
it will use port number 80 by standard
This is not secure - when you configure the website you can redirect people if it is insecure 
//HTTPs - means that it is secure

### FTP - File Transfer Protocol -> application
Can also use SFTP
Standard port is 21

### SMTP - Simple Mail Transfer Protocol

your email is : xxxxx.com
you are sending an email to xxxx.com - this should be on the destination server

----- 

#### Flask App 

#### Need to know which port we want to reach 
    Standard is 80 (not secure - normally used for entry point), 
    typical SSL port is 443

