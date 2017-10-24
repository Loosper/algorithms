#include <stdio.h>
#include <stdlib.h>

int main() {
    char *string = malloc(100000 * sizeof(char));
    char ch;
    int i;
    int valid = 1;

    for (i = 0; (ch = fgetc(stdin)) != EOF && ch != '\n'; ++i) {
        string[i] = ch;
    }

    for (int j = 0, k = i - 1; j <= k; ++j, --k) {
        if (string[j] != string[k]) {
            valid = 0;
            break;
        }
    }

    if (valid)
        printf("YES\n");
    else
        printf("NO\n");
}
