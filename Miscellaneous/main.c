#include <stdio.h>
#include <time.h>

int GetTime(){
    time_t rawtime;
    struct tm * timeinfo;
    
    time(&rawtime);
    timeinfo = localtime (&rawtime);
    return asctime(timeinfo);

}
int main() {
    printf("%s", GetTime());
    return 0;
}
