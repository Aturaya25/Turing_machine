# Turing_machine
The program reads from standard input the program for the Turing machine in tabular form. The result of the Turing machine is displayed. If the program does not end after 100000 steps, the emulator stops without any diagnostics.
***
***input***
    
              a       b       =       _
      0     _,R,1   _,R,5   _,R,4     ,,
      1      ,R,     ,R,     ,R,2    ,L,7
      2     =,L,3   =,L,7    ,R,2    ,L,7
      3      ,L,     ,L,     ,L,     ,R,0
      4      ,N,7    ,N,7   _,R,     a,N,!
      5      ,R,     ,R,     ,R,6    ,L,7
      6     =,L,7   =,L,3    ,R,6    ,L,7
      7      ,L,     ,L,     ,L,     ,R,8
      8     _,R,    _,R,    _,R,     ,,!
      abbabab=abbabab
      
***output***

      _a_

***input***

       0     1     2     3     #     _
      0  ,R,   ,R,   ,R,   ,R,   ,R,  #,L,1
      1  ,L,   ,L,   ,L,   ,L,   ,L,   ,R,2
      2 _,R,3 _,R,5 _,R,7 _,R,8 _,R,!  ,,
      3  ,R,   ,R,   ,R,   ,R,   ,R,  0,R,4
      4  ,,    ,,    ,,    ,,    ,,   0,L,1
      5  ,R,   ,R,   ,R,   ,R,   ,R,  0,R,6
      6  ,,    ,,    ,,    ,,    ,,   1,L,1
      7  ,R,   ,R,   ,R,   ,R,   ,R,  1,R,4
      8  ,R,   ,R,   ,R,   ,R,   ,R,  1,R,6
      1203012301203012

***output***

      _01100011000110110001100011000110_
