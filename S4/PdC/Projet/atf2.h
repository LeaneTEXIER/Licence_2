#define ATF_BLOCSIZE 16
#define NBLOCS 1000
#define NBLOCS_B NBLOCS/8

extern void atf_init();

extern void * atf_newbloc();

extern int atf_freebloc(void *bloc);
