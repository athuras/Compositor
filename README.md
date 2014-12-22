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

    $ Compositor text -u http://img4.wikia.nocookie.net/__cb20130517001619/p__/protagonist/images/f/f1/Bastila-shan.png --scale=2 --sharpness=1.4 --kmedian=5 --font_size=14

                                          _ _
                                 )gggg~ T_----- _ggggggggggggggggggg}
                                 rWWW& ~---------[WWWWWWWWWWWWWWWWWWW
                                 rWWW[{--,ogm:---rWWWWWWWWWWWWWWWWWWW
                                 rWWW&_gm&;[D--.`    ,CWWWWWWWVWWWWWW
                                 rWWWWw{CX{&:-:`    }WWWWWWWQ}WWWWWWW
                                 rWWWW&-"U&p.:'   ,cWWWWWWWV/WWWWWWWW
                                 rWWWW`|-:"".---_YT&WWWWWQ)WWWWWWWWWW
                                 rWWQ`).:"-:-------::NWWY/WWWWWWWWWWW
                                   2.-----::------::pUQ}CWWWWWWWWWWWW
                                  x--------::----:MUW\7WWWWWWW&WWWWWW
                                  -----,:---:--:m[UQ)d&WWWWWW* WWWWWW
                                 {Ww,--WW:--.::KUW\}WUNXWWWQ   WWWWWW
                                 &XWU:MUXg--:NUUW}d&Um:MQWY    WWWWWW
                                vWX&m"{yN"m:MUW\}&UUN:-:}-     WWWWWW
                               ,UU&k"}W&&UWWUQ)d&KDm":---      WWWWWW
                               [p.::}W$&@&WW\}&Uk:"-:::-;      WWWWWW
                               QWN:{AX&pUWW}A&K"-----::-,      WWWWWW
                                :--{{0NUW\}&UD"---------|      WWWWWW
                                ---{T-DU)A&m"-----------'  ___)WWWWWW
                                 --{--"UUU[-------------= WWWWWWWWWWW
                                ',rDkD"::"---:---------p-_LWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWw{XX&::::--------:::----[k:_QWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWW{&D":UUp.-------:N:----::-_
    WWWWWWWWWWWWWWWWWWWWWWWWWWWXKK{.MUUUm:-----.pU:--.w:::`
    WWWWWQ````````````)WWWWWWWQQGWXM}UUUm------:U&m--:_="`
    WWWWW[           gWWWWWWWV)WWWW@}[UU:----:-:U&k:-:_
    WWWWW[         }WWWWWWWWT/WWWWXw} &Um-----::[&[:-:_
    WWWWW[        gWWWWWWWV)WWWWWW{mT UUk:-----`U&U:-.
    WWWWW[      )WWWWWWWW\7WWWWWWWT"_ XXU:----= [W&m::
    WWWWW[     gWWWWWWWW)AWWWWWWW& N_ XWN-----= 'WX[::
    WWWWW[    CWWWWWWW\}WWWWWWWWW& N_ [&"--:     UXU:-:
    WWWWW[  }WWWWWWWQ}AWWWWWWWVWWW_k_ [U:--:_     Uh:-::_
    WWWWW[ gWWWWWWWV}WWWWWWW&- WWWW ` 'UN:--`     [D:--::
    WWWWWWWWWWWWWQ}AWWWWWWWV   WWWWWWW :-----     'm:---"
    WWWWWWWWWWWWV}WWWWWWWW`    WWWWWWW_[-----      :----"_
    WWWWWWWWWWW\AWWWWWWWW      WWWWWWWW :----       :---:-
    WWWWWWWWWW)WWWWWWWW`       WWWWWWWW k----       ,-----
    WWWWWWWW\/WWWWWWWQ         WWWWWWWW ':--`        m---|
    WWWWWWQ}WWWWWWWW`          WWWWWWWW {u.-.        |:--|
    WWWWWV/WWWWWWW6            WWWWWWW6,A":-=         -m::x
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*):--:-_         -"[--`_
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW ":---"            U:.---
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWU `                  -- --
