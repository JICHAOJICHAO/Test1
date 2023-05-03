#include <stdio.h>
#include <string.h>

int main() {
    char command[100];

    while(1) {
        printf("$ ");
        fgets(command, 100, stdin);

        command[strcspn(command, "\n")] = '\0'; // 去除末尾的换行符

        if(strcmp(command, "quit") == 0 || strcmp(command, "exit") == 0) {
            break;
        }

        printf("You entered: %s\n", command);
    }

    return 0;
}