# include < stdio . h >

3 vint main ()
5
 char ch ;
 while (( ch = getchar ())!= n )// tips 
8# ifdef CONVERT 
10
 Note by aut ：该位操作要求输入严格为 AlphNum ,
11
否则会出现严重的错误，
12
可按需加入适当的判断条件或扩展位操作逻辑。
13
**/
14
 ch =( ch |(1<<5))&~((( ch >>5&0b11)==0b11)<<5);
15
# endif 
16
 putchar ( ch );
17
18
 putchar ( ch );
19
 return 0;
20
