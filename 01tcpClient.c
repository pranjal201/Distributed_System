#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>

void main(){
    //create a socket 
    int networkSocket;
    networkSocket = socket(AF_INET, SOCK_STREAM, 0);

    //specify an address for the socket
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(9002);
    server_address.sin_addr.s_addr = INADDR_ANY;

    int connectionStatus = connect(networkSocket, (struct sockaddr *) &server_address, sizeof(server_address));
    
    if(connectionStatus == -1)
        printf("\n!!!CONNECTION NOT ESTABILISHED!!!\n");
    
    //recieving data from the server
    char serverResponse [255];
    recv(networkSocket,&serverResponse ,sizeof(serverResponse),0);

    // print out the data from the server
    printf("The server sent the data: %s\n", serverResponse);


    //closing the socket/
    close(networkSocket);
}
