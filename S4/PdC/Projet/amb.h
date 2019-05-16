#define NBLOCS 999
#define AMB_BLOCSIZE 4
#define BLOC_END -1

extern int amb_init();

extern void * amb_newbloc(unsigned int nbloc);

extern int amb_freebloc(void *bloc);
