Compositor: Morphologically Optimal ASCII Art
==========

See the [PyPI description](https://pypi.python.org/pypi/Compositor/1.0.1) for a much wittier spiel.

    Usage:
        compositor text (-u IMAGE_URL | -f IMAGE_FILE ) [options]
        compositor image (-u IMAGE_URL | -f IMAGE_FILE ) OUTPUT_FILE [options]
        compositor (-h | --help | --version)

    Options:
        -h, --help                         show this help message and exit
        --version                          show version and exit
        -u IMAGE_URL, --url IMAGE_URL      Read an image from a URL as imput.
        -f IMAGE_FILE        Read an image from a file as input.
        --sharpness=<float>  preprocessing sharpness value. [default: 1]
        --kmedian=<int>      preprocessing median filter value. [default: 1]
        --scale=<int>        preprocessing resolution modification. [default: 1]
        --brightness=<int>   preprocessing gamme correction. [default: 1]
        --font_size=<int>    font rendering size, at least 20 is recommended. [default: 24]

Demo 1:
------

    $ Compositor text \
      -u http://img4.wikia.nocookie.net/__cb20130517001619/p__/protagonist/images/f/f1/Bastila-shan.png \
      --scale=2 --sharpness=1.4 --kmedian=5 --font_size=24

                           __
                      WW`=iiHH VWWWWWWWWWWW
                      WW g@WMi `**WWWWWWWWW
                      WWW WWH!  ,WWWW*<WWWW
                      WW'|!*iH_/%WWW`WWWWWW
                      `_=iH!HHH!!Q*<WWWWWWW
                      iHH!Hi!H!<W`WWWW^\WWW
                      wuHW!H!!W*<WVWW' {WWW
                     {W& g*,<W`{WziW   {WWW
                    ,**,WWWW*,W**!H    {WWW
                    ^*i@W&W`{WiiH!!!   {WWW
                     H!G6{,W*iHHHHH|   {WWW
                     H,:zWWiHHHHHHH]*WWWWWW
    wwwwwwwwwwwwwwwwy8Wzj!HHHH!!HHH@ WWWWWW
    WWWWWWWWWWWWWWWWW&gu0&!HHHz&H!.!:
    WWW`       WWWW*)WW{0&!HHH<W!! `
    WWW      ,WWWW`^WWW/VWHHHHDWzH
    WWW     ^WWWV,WWWW@  W!HH]'Wg!
    WWW   ,WWWW*<WWWWW   Wi!-  WW!
    WWW  <WWWW WWWW*WW   &Hi   `&H!
    WWWvWWWW//WWWW` {WW< *iH    z!H!
    WWWWWWW`0WWWW   {WWW;.HH     HHR
    WWWWW^/WWWW'    {WWW} HH     !HH
    WWWW`WWWWW      {WWW} gH     `!H
    WWWyWWWW(,,,,,,,8WWW'/ii      iy^
    WWWWWWWWWWWWWWWWWWW}(HHF       RUH


Demo 2 (Same Image, just bigger):
-----------------------------------

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
