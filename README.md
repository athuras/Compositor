Compositor
==========

Morphologically optimal ASCII art generator (with unicode support!).
Instead of matching glyphs based on area, match based on some cost function of bitmap overlays.

Currently, Compositor supports rendering arbitrary image files (whatever can be opened by PIL) as either an arbitrarily high quality bitmap rendering, or as 'traditional' text characters.

[Demo](http://nbviewer.ipython.org/github/athuras/Compositor/blob/master/Demo.ipynb)

Here is a relatively low-res version of the Python (TM) logo, that blip in the upper right is a trademark, in case anybody was wondering.


           .~~==~~_                                              `8
         ,z*\"zooooo!\\                                      ~    {!8                                <~; ;
         {o`oooooz!!!                                     S!    {!8                                  K*x
     .<xxxxxxxxx!!!!!;ww>          ~m,*=m.   .m      xm  m*!nm  {!8.<mom.     <^*\\m..    .:^f*n~
    Aoooooooo!!!!!!!!{WWWW,      ;!}    \\!e  :!      z!   S!    {!J*`  *!^  /!/   `8!   !3   `\\!z
    ooooooo!!!!!!!!j\"@WWWWW      ;!}     z!  :!      z!   S!    {!8     !o  !b      !z  !B     !!
    oooooj(wwwwwwwwWWWWWWWW      ;!}     x!' :!      z!   S!    {!8     !o '!D      !!  !B     !!
    zo!!!QWWWWWWWWWWWWWWWW*      ;!}     !!  ;!:     z!   S!    {!8     !o  U!     .!*  !B     !!
    .x!!!QWWWWWWWWWWWWWWWW       ;!Gz>=n!J`   !!z>=mjj!   '!^~  {!8     !o   x!=~~^y:   !B     !!
         {WWWWWwwwwww            ;!}  `          `   x!       `                 `
         <WWWWWWW/ VW            ;!}                _!/
          ^WWWWWWWWW`            :j}             ^fx~
        ,,>~<wwwwwwy~,,                          `
     <@@@@@@@@%%%%@@@@@@@%
      **@@@@%%@@@%%@@@@@*`

Alternatively:
    Compositor text -u http://img4.wikia.nocookie.net/__cb20130517001619/p__/protagonist/images/f/f1/Bastila-shan.png --scale=3 --sharpness=1.4 --kmedian=5 --font_size=16


                                                      >r1ii`Y\
                                           \%%%%%%Xv/HH!!HHHHH\x?%%%%%%%%%%%%%%%%%%%%%%%%%%{
                                           \%%%%%W AHHHHHHHHHHHi`8%%%%%%%%%%%%%%%%%%%%%%%%%}
                                           \%%%%%} HHH!gww6!HHHB 8%%%%%%%%%%%%%%%%%%%%%%%%%}
                                           \%%%%%w (H<WW8@W!HHHB `*****%%%%%%%%%%%%W%%%%%%%}
                                           \%%%%%W XWWWWWW4HH!vy      \@%%%%%%%%%Wx<%%%%%%%}
                                           \%%%%%%Ay\WWWWW!H!jY     x8%%%%%%%%%%6^8%%%%%%%%}
                                           \%%%%%%@.`*WWW&HH!K     >@%%%%%%%%%Wx<%%%%%%%%%%}
                                           \%%%%%%? 1H!*WWiHiY\  xw%W%%%%%%%%6(8%%%%%%%%%%%}
                                           \%%%%%%  iH{{{!HHHHH`===Y9WWW%%%Wy%%%%%%%%%%%%%%}
                                           \%%Wx?`>4HiiH{{HHHHHHHHHH!!{%W%6(8%%%%%%%%%%%%%%}
                                           `*\)?fHHHHHH!!{HHHHHHHHH!!zWWWV%%%%%%%%%%%%%%%%%}
                                             A!iHHHH!HHHi!HHHHHHH!!5zW@^(A%%%%%%%%%%%%%%%%%}
                                             iHHHHHHHHHHHi!HHHHH!{zW@WyY%W%%%%%%%%/*%%%%%%%}
                                            }HHHHHH!{!HHHHHHHH!{}WW@^(A@%%W%%%%%@x {%%%%%%%}
                                            8>jHHHH<Wy!HHHHH!!{zW@W/<@WWzWW%%%%*`  {%%%%%%%}
                                           <WWWW:H!WWW(HHH!!{:WW@^6W@Wz{!WW%%@y    {%%%%%%%}
                                           WWWWW{j'yWWW!HH!{zW@W/x@@Wz{!i56W/^     {%%%%%%%}
                                          yWWWW{5)/AV6{..!}WW@^?A@W6z{{HHi8^       {%%%%%%%}
                                         YW%W@*})vWWWW%%%WW@W/\@WW*:{{!HHH}        {%%%%%%%}
                                        `1**x?i`/%WWWW%WWW@)/X@Wx{{}i!!HHH}        {%%%%%%%}
                                        \WW&!!5)WWWA{.WWWW/>@@W!iiiHH{!!!H3        {%%%%%%%}
                                        /%@z!!RWWWW.:WW@v/X@Wz!iHHHHHi!!!HHV       {%%%%%%%}
                                         *!HHH9WW*{zW@x/)@@W:{iHHHHHHHiiiHU        {%%%%%%%}
                                          HHHB8W4!xW@^xX@W*{!iHHHHHHHHHHHHB        {%%%%%%%}
                                          HHHR84H!:WWwWWz!!iiHHHHHHHHHHHHHH  ,,,,,,v%%%%%%%}
                                          HHHk(HHH{:WWWW!iHHHHHHHHHHHHHHHHH \%%%%%%%%%%%%%%}
                                          vHHH?9.z!!****HHHHHHHHHHHHHHHHHjH; %%%%%%%%%%%%%%}
    ____________________________________  vyWWW!^!!!!iHHHHHHHHHHHHHHHHHHHW@P ^%%%%%%%%%%%%%}
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%x/WWWW!{.!!HHHHHHHHHHHH!!HHHHHHH8Wi^ y%%%%%%%%%%%%{
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%WW6W*!HxWW.!HHHHHHHHHH!}:!HHHHH,>{HH
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%WWW{1gH!5WWW:!HHHHHHHHH{z6{HHHHKV!!!!(
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%WW:)WW!(WWWWz{HHHHHHHHH5WW{HHHHx;Hi{)
    %%%%%%%V                 W%%%%%%%%%W*WWWWW{3WWWW:!HHHHHHHHH:@W{!HHHk^^*?`
    %%%%%%%X               x%%%%%%%%%%/v<%8%WW{3VWWW:!HHHHHHHHiW@W:!HHH*
    %%%%%%%X             /W%%%%%%%%%W\XW%%%%WW{3WV@Wz{HHHHHHHHHX@@W{HHH*
    %%%%%%%X            y@%%%%%%%%%/y<%%%%%%8W{W^9@WW{HHHHHHHi!@@@W{!HH)
    %%%%%%%X          <<%%%%%%%%%@)XX%%%%%%%WW{(  W@W{HHHHHHHH WW@W6!HH^
    %%%%%%%X         y%%%%%%%%%%W/y%%%%%%%%%W6{( `8WW6!HHHHHH[ ;W@@W!HH
    %%%%%%%X       x<%%%%%%%%%@^(X%%%%%%%%%%^ {   8WWwiHHHHHHR  WWWW{HH
    %%%%%%%X      ;@%%%%%%%%%Wx\W%%%%%%%%%%%  z   8WW{HHH,jjHR  XWWW6!Hv
    %%%%%%%X     x%%%%%%%%%%*/X%%%%%%%%%%%%%  x   8@*iHHiX      /%WW:!HfV
    %%%%%%%X   xA%%%%%%%%%@)\@%%%%%%%%%@%%%%y w   WW:!HHH?`      XWW{HHi!Y
    %%%%%%%X  v@%%%%%%%%%/x<%%%%%%%%%%^`X%%%@.Xy  WW:!HHHi`       Wz{!HHH!Y
    %%%%%%%X<X%%%%%%%%%@)(8%%%%%%%%%@/  X%%%%X` , ^Wz{HHHH}       :{{!HHHH{`
    %%%%%%%@@%%%%%%%%%W/X%%%%%%%%%%^`   X%%%%%%%%w yiiHHHH!        {{!!HHH!V
    %%%%%%%%%%%%%%%%%((W%%%%%%%%%@?     X%%%%%%%%@ 7!HHHHH!        ViiHHHH!;
    %%%%%%%%%%%%%%%Wx/%%%%%%%%%%x       X%%%%%%%%%6?{HHHHH!        `HHHHHH!A
    %%%%%%%%%%%%%%/KW%%%%%%%%%@(        X%%%%%%%%%X \HHHHH}         \!HHHHHR
    %%%%%%%%%%%%Wvx%%%%%%%%%%x          X%%%%%%%%%X /!HHHH}         \v!HHHHB
    %%%%%%%%%%%//W%%%%%%%%%@^           X%%%%%%%%%X  8!HHH}          V{HHHH>`
    %%%%%%%%%@)yW%%%%%%%%%W             X%%%%%%%%%X  \!HHH}           V!HHHH
    %%%%%%%%W/W%%%%%%%%%@(              X%%%%%%%%%X  )6!HH\           )i!HHH
    %%%%%%%^yW%%%%%%%%%W/               X%%%%%%%%%X vW*!!HH            H!{{{})
    %%%%%%%W%%%%%%%%%%Wyyyyyyyyyyyyyyyyy@%%%%%%%@*>V'HHiiH"            HH*Wzii\
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(`4iHHHH!;             HHHW!HHHi\
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ^iHHHHHt^             ` ,*W&!HHH
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@(`"""""``                ` ",HHHP
