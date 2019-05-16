#define ATF_BLOCSIZE 16
#define NBLOCS 1000

extern void atf_init();

extern void * atf_newbloc();

extern int atf_freebloc(void *bloc);
