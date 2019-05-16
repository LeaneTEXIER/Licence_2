#define BLOC_END -1
#define CBL_BLOCSIZE 4
#define NBLOCS 1000

extern int cbl_init();

extern void * cbl_newbloc();

extern int cbl_freebloc(void *bloc);
