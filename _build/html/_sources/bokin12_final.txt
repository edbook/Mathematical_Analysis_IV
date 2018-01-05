
Fyrsta stigs hlutafleiðujöfnur
==============================

Inngangur
---------

Þessi örstutti kafli inniheldur tvær aðferðir til úrlausnar á línulegum
fyrsta stigs jöfnum. Kennilínuaðferðin byggir á þeirri staðreynd að
lausnir á jöfnum af gerðinni
:math:`a(x,y){\partial}_xu+b(x,y){\partial}_yu=0` taka fast gildi á
ákveðnum ferlum, sem nefndir eru kennilínur og ákvarðast af stuðlunum
:math:`a` og :math:`b`. Við höfum séð hvernig hægt er að beita
Laplace-ummyndun til þess að finna lausnir á venjulegum afleiðujöfnum og
afleiðujöfnuhneppum. Hún kemur oft að góðu gangi við úrlausn á tímaháðum
hlutafleiðujöfnum með upphafsskilyrðum, þar sem hægt er að taka
Laplace-mynd með tilliti til tíma. Þá fæst oft fram venjuleg
afleiðujafna eða hlutafleiðujafna í rúmbreytistærðunum, sem auðveldara
er að leysa en upphaflegu jöfnuna.

Kennilínuaðferðin fyrir línulegar fyrsta stigs jöfnur
-----------------------------------------------------

Kennilínuaðferðin fyrir línulegar fyrsta stigs jöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Línuleg fyrsta stigs jafna af tveimur breytistærðum :math:`(x,y)` er af
gerðinni

.. math::

  a(x,y)\dfrac{\partial u}{\partial x} +
    b(x,y)\dfrac{\partial u}{\partial y} +
    c(x,y) u = f(x,y).

Byrjum á því að skoða einfalt dæmi:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Einfaldur massaflutningur

Lítum á vatnslögn með fast þversnið og hugsum okkur að vatnið í henni
renni með föstum hraða :math:`c`. Gerum einnig ráð fyrir að í vatninu sé
uppleyst efni og að styrkur þess á lengdareiningu í þversniðinu
:math:`x` við tímann :math:`t` sé gefinn með fallinu :math:`u(x,t)`,
:math:`[g/cm]`.

.. figure:: ./myndir/fig111.svg
    :align: center
    :alt: Einfaldur massaflutningur

    Mynd: Einfaldur massaflutningur

Ef við hugsum okkur að uppleysta efnið flytjist með straumnum en
dreifist ekki í vatninu, þá gildir jafnan

.. math:: u(x+ch,t+h) = u(x,t),

þ.e. efnisagnirnar sem voru í þversniðinu :math:`x` við tímann
:math:`t` eru í þversniðinu :math:`x+ct` við tímann :math:`t+h`. Þessi
jafna hefur síðan í för með sér að

.. math::

  \lim _{h \to 0} \dfrac 
    {u((x,t)+h(c,1)) - u(x,t)}h = 0,

og þar með er stefnuafleiða fallsins :math:`u` í stefnuna :math:`(c,1)`
í punktinum :math:`(x,t)` jöfn :math:`0`. Samkvæmt keðjureglunni er
þetta jafngilt því að

.. math::

  c \dfrac{\partial u}{\partial x} + 
      \dfrac{\partial u}{\partial t} = 0

gildi í sérhverjum punkti. Nú er augljóst að fall af gerðinni
:math:`u(x,t)=f(x-ct)` er lausn á þessari jöfnu. Við tímann :math:`t` er
gildi lausnarinnar :math:`u(x,t)` einfaldlega hliðrun á fallinu
:math:`f` um :math:`ct`.

.. figure:: ./myndir/fig112.svg
    :align: center
    :alt: Einvíð bylgja

    Mynd: Einvíð bylgja

.. end-toggle::

Það er auðvelt að finna lausn á fyrsta stigs línulegum jöfnum með
fastastuðla á öllu rúminu:

Setning
^^^^^^^

Fall :math:`u\in C^1({{\mathbb  R}}^2)` er lausn á jöfnunni

.. math::

  a\dfrac{\partial u}{\partial x}+
   b\dfrac{\partial u}{\partial y}=0,

þar sem :math:`(a,b)\in {{\mathbb  R}}^2` og :math:`(a,b)\neq (0,0)`, þá
og því aðeins að :math:`u` sé af gerðinni

.. math:: u(x,y)=f(bx-ay),

með :math:`f\in C^1({{\mathbb  R}})`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Gerum ráð fyrir að :math:`u\in C^1({{\mathbb  R}}^2)` sé lausn. Jafnan
segir okkur að stefnuafleiðan af :math:`u` í stefnu vigursins
:math:`(a,b)` sé :math:`0` í sérhverjum punkti og þar með er takmörkun
:math:`u` við sérhverja línu með stefnuvigurinn :math:`(a,b)` fastafall.
Slík lína hefur jöfnuna :math:`bx-ay=c` og því er :math:`u` einungis háð
breytunni :math:`c` á þessari línu. Þar með er til fall :math:`f` á
:math:`{{\mathbb  R}}` þannig að :math:`u(x,y)=f(c)` og þar með er
:math:`u(x,y)=f(bx-ay)`. Með því að setja :math:`y=0`, eða :math:`x=0` í
tilfellinu :math:`b=0`, inn í þessa jöfnu, þá sjáum við að
:math:`f\in C^1({{\mathbb  R}})`.

Ef :math:`f\in C^1({{\mathbb  R}})` og við skilgreinum :math:`u(x,y)=f(bx-ay)`,
þá fæst hlutafleiðujafnan beint af keðjureglunni.

.. end-toggle::

Lítum nú á tilfellið :math:`b\neq 0` og tökum punkt :math:`(x,y)` í
:math:`(\xi,\eta)`-plani. Línan gegnum punktinn :math:`(x,y)` með
stefnuvigurinn :math:`(a,b)` hefur jöfnuna :math:`b\xi-a\eta=bx-ay`.
Skurðpunktur hennar við :math:`\xi`-ásinn er :math:`(x-ay/b,0)`. Nú
vitum við að gildi lausnarinnar :math:`u`
er það sama í öllum punktunum á þessari línu og þar með
gildir:

Setning
^^^^^^^

Upphafsgildisverkefnið

.. math::

  \begin{cases} 
   a\dfrac{\partial u}{\partial x}+b\dfrac{\partial u}{\partial y}=0, 
   &(x,y)\in {{\mathbb  R}}^2,\\  
   u(x,0)=\varphi(x),  &x\in {{\mathbb  R}},
   \end{cases}

þar sem :math:`\varphi \in C^1({{\mathbb  R}})` er gefið fall og
:math:`b\neq 0`, hefur ótvírætt ákvarðaða lausn

.. math:: u(x,y)=\varphi(x-ay/b).

Skilgreining
^^^^^^^^^^^^

Lína sem hefur stefnuvigur samsíða :math:`(a,b)` nefnist *kennilína*
afleiðuvirkjans :math:`a\partial_x+b\partial_y`.

--------------

Hugtakið kennilínu og aðferðina, sem við höfum verið að fjalla um er
auðvelt að alhæfa yfir á jöfnu af gerðinni

.. math:: a(x,y)\dfrac{\partial u}{\partial x}+b(x,y)\dfrac{\partial u}{\partial y}=0.

Í því tilfelli að :math:`a` og :math:`b` eru fastar og við stikum
kennilínuna gegnum :math:`(x,y)` með :math:`t\mapsto (\xi(t), \eta(t))`,
þar sem :math:`\xi(t)=x+at` og :math:`\eta(t)=y+bt`, þá sjáum við að
:math:`(\xi(t),\eta(t))` er lausn á upphafsgildisverkefninu

.. math:: \xi{{^{\prime}}}(t)=a, \quad \eta{{^{\prime}}}(t)=b, \quad \xi(0)=x, \quad \eta(0)=y.

Skilgreining
^^^^^^^^^^^^

Sérhver lausn :math:`t\mapsto (\xi(t),\eta(t))` á afleiðujöfnuhneppinu

.. math:: \xi{{^{\prime}}}=a(\xi,\eta), \qquad \eta{{^{\prime}}}=b(\xi,\eta),

nefnist *kenniferill* eða *kennilína* afleiðuvirkjans

.. math:: a(x,y)\dfrac{\partial}{\partial x}+b(x,y)\dfrac{\partial}{\partial y}.

--------------

Gerum nú ráð fyrir að :math:`u` sé lausn og að
:math:`t\mapsto (\xi(t),\eta(t))` sé kenniferill. Þá gefur keðjureglan

.. math::

  \begin{aligned}
   \dfrac d{dt} \bigg(u(\xi(t), \eta(t))\bigg) &=
   \dfrac{\partial u}{\partial x}(\xi(t),\eta(t))\xi{{^{\prime}}}(t)
   +\dfrac{\partial u}{\partial y}(\xi(t),\eta(t))\eta{{^{\prime}}}(t)\\
   &=a(\xi(t),\eta(t))\dfrac{\partial u}{\partial x}(\xi(t),\eta(t))
   +b(\xi(t),\eta(t))\dfrac{\partial u}{\partial y}(\xi(t),\eta(t))=0.\end{aligned}

Þetta segir okkur að gildi lausnarinnar sé fast á sérhverjum
kenniferli. Nú skulum við líta á upphafsgildisverkefnið

.. math::

  \begin{cases} 
   a(x,y)\dfrac{\partial u}{\partial x}+b(x,y)\dfrac{\partial u}{\partial y}=0, 
   &(x,y)\in {{\mathbb  R}}^2,\\  
   u(x,0)=\varphi(x),  &x\in {{\mathbb  R}}.
   \end{cases}

Við byrjum á því að taka punkt :math:`(x,y)` í :math:`(\xi,\eta)`-plani.
Síðan leysum við verkefnið

.. math::

  \xi{{^{\prime}}}=a(\xi,\eta), \quad \eta{{^{\prime}}}=b(\xi,\eta), \quad \xi(0)=x,
   \quad \eta(0)=y.

Ef til er ótvírætt ákvörðuð lausn :math:`t\mapsto (\xi(t),\eta(t))` á
einhverju opnu bili fyrir sérhvert :math:`(x,y)` og ferillinn sker
:math:`\xi`-ásinn í nákvæmlega einum punkti :math:`(s(x,y),0)`, þá er
lausnin gefin með formúlunni

.. math:: u(x,y)=\varphi(s(x,y)).

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Leysum verkefnið

.. math::

  x\dfrac{\partial u}{\partial x}+\dfrac{\partial u}{\partial y}=0, 
   \qquad u(x,0)=\varphi(x),

þar sem :math:`\varphi` er eitthvert fall á :math:`{{\mathbb  R}}`. Við
höfum hér :math:`a(x,y)=x` og :math:`b(x,y)=1`, svo fyrir gefinn punkt
:math:`(x,y)` þurfum við að leysa

.. math:: \xi{{^{\prime}}}=\xi, \quad \eta{{^{\prime}}}=1, \quad \xi(0)=x, \quad \eta(0)=y.

Lausnin er greinilega

.. math:: \xi(t)=xe^t, \qquad \eta(t)=t+y, \qquad t\in {{\mathbb  R}},

og skurðpunkturinn við :math:`\xi`-ásinn svarar til :math:`t=-y`. Þar
með er :math:`s(x,y)=\xi(-y)=xe^{-y}` og lausnin er fundin,

.. math:: u(x,y)=\varphi(xe^{-y}).

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum einnig á verkefnið

.. math::

  \dfrac{\partial u}{\partial x}+x^2
   \dfrac{\partial u}{\partial y}=0, \qquad x\in {{\mathbb  R}}, \ y>0, \quad
   u(x,0)=\sin x, \qquad x\in  {{\mathbb  R}}.

Við ákvörðum kennilínu virkjans gegnum :math:`(x,y)` í
:math:`(\xi,\eta)`-plani. Ef hún sker :math:`\xi`-ásinn í nákvæmlega
einum punkti :math:`(s(x,y),0)`, þá er lausnin gefin með formúlunni
:math:`u(x,y)=\sin\big(s(x,y)\big)`. Kennilínan í gegnum :math:`(x,y)`
er stikuð með :math:`(\xi(t),\eta(t))`, þar sem

.. math::

  \xi{{^{\prime}}}(t)=1, \quad \eta{{^{\prime}}}(t)=\big(\xi(t)\big)^2, \quad 
   \xi(0)=x, \quad \eta(0)=y.

Með heildun fáum við

.. math::

  \xi(t)=x+t, \qquad \eta{{^{\prime}}}(t)=(x+t)^2, \qquad
   \eta(t)=y-\tfrac 13 x^3+\tfrac 13(x+t)^3.

Til þess að finna skurðpunkt kennilínunnar við :math:`\xi`-ásinn, þá
þurfum við aðeins að leysa :math:`t` út úr jöfnunni :math:`\eta(t)=0` og
stinga útkomunni inn í :math:`\xi(t)`,

.. math::

  y-\tfrac 13 x^3+\tfrac 13(x+t)^3=0, \qquad
   t=\big(x^3-3y\big)^{\frac 13}-x.

Hér á að taka þriðju rót af neikvæðri tölu þannig að út komi neikvæð
tala. Fyrir þetta gildi á :math:`t` er
:math:`\xi=\xi(t)=s(x,y)=\big(x^3-3y\big)^{\frac 13}`. Þar með er
lausnin fundin,

.. math:: u(x,y)=\sin\big(x^3-3y\big)^{\frac 13}, \qquad x\in {{\mathbb  R}}, y>0.

.. end-toggle::

Úrlausn á fyrsta stigs jöfnum með Laplace-ummyndun
--------------------------------------------------

Úrlausn á fyrsta stigs jöfnum með Laplace-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Laplace-ummyndunin er mikilvægt hjálpartæki við úrlausn á línulegum
afleiðujöfnum og þá einkum til þess að leysa upphafsgildisverkefni.
Hugsum okkur að :math:`u(x,t)` sé fall af tveimur breytistærðum og látum
:math:`U(x,s)` vera Laplace-myndina af :math:`u` með tilliti til tíma
:math:`t`,

.. math:: U(x,s)={{\cal L}}\{u(x,\cdot)\}(s)=\int_0^\infty e^{-st} u(x,t)\, dt.

Reiknireglan fyrir Laplace-mynd af afleiðum gefur okkur að

.. math::

  {{\cal L}}\{\partial_t^m u(x,\cdot)\}(s)
   =s^mU(x,s)
   -s^{m-1}u(x,0)-\cdots-s\partial_t^{m-2}u(x,0)-\partial_t^{m-1}u(x,0),

ef við gefum okkur að :math:`u` sé :math:`m` sinnum samfellt
deildanlegt með tilliti til :math:`t` fyrir fast :math:`x` og að allar
afleiður séu af veldisvísisgerð. Við gefur okkur einnig að það megi taka
allar afleiður af :math:`u` með tilliti til :math:`x` fram fyrir
Laplace-heildið,

.. math::

  {{\cal L}}\{\partial_x^ku(x,\cdot)\}(s)
   =\int_0^\infty e^{-st} \partial_x^ku(x,t)\, dt
   =\partial_x^k\int_0^\infty e^{-st} u(x,t)\, dt
   =\partial_x^kU(x,s).

Nú skulum við sjá hvernig þessum reglum er beitt til þess að leiða út
lausnarformúlur á upphafsgildisverkefnum.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Við skulum ákvarða formúlu fyrir lausn verkefnisins

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial t}+x\dfrac{\partial u}{\partial
   x}+u=f(x,t), &x>0, \ t>0,\\
   u(x,0)=u(0,t)=0, &x>0, \ t>0,
   \end{cases}

þar sem :math:`f` er fall á
:math:`{{\mathbb  R}}_+\times {{\mathbb  R}}_+`. Við látum
:math:`U(x,s)` og :math:`F(x,s)` tákna Laplace-myndir fallanna :math:`u`
og :math:`f` með tilliti til :math:`t`. Við notum upphafsskilyrðið
:math:`u(x,0)=0` og fáum þá að Laplace-ummyndun af verkefninu gefur
okkur

.. math:: sU(x,s)+x\partial_xU(x,s)+U(x,s)=F(x,s), \qquad U(0,s)=0.

Þetta er fyrsta stigs afleiðujafna í :math:`x`

.. math:: \partial_xU(x,s)+\dfrac{s+1}xU(x,s)=x^{-1}F(x,s), \qquad U(0,s)=0.

Ef við setjum :math:`a(x)=(s+1)/x`, þá er :math:`A(x)=\int_1^x a(\xi)\, d\xi=(s+1)\ln x` og :math:`e^{A(x)}=x^{s+1}`. Við höfum því jafngilda
jöfnu

.. math::

  \dfrac{\partial}{\partial x}\bigg(x^{s+1}U(x,s)\bigg)=x^{s}F(x,s),
   \qquad U(0,s)=0.

Við heildum og fáum

.. math:: x^{s+1}U(x,s)=\int_0^x\xi^{s} F({\xi},s)\, d\xi.

Þar með er Laplace-myndin fundin,

.. math::

  U(x,s)=x^{-1} \int_0^x x^{-s}{\xi}^sF({\xi},s)\, d{\xi}
   =x^{-1} \int_0^x  e^{-s\ln(x/{\xi})} F({\xi},s)\, d{\xi}.

Reikniregla fyrir Laplace-myndir segir okkur nú að

.. math::

  e^{-s\ln(x/{\xi})} F({\xi},s)=
   {{\cal L}}\{H(t-\ln(x/{\xi}))f({\xi},t-\ln(x/{\xi}))\}(s)

og þar með er lausnarformúlan fundin

.. math::

  u(x,t)=
   x^{-1} \int_0^x  H(t-\ln(x/{\xi}))f({\xi},t-\ln(x/{\xi}))\, d{\xi}.

.. end-toggle::

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Ákvarðið kennilínur virkjanna sem gefnir eru og kannið hvort
jaðargildisverkefnin

.. math::

  \begin{cases} Lu =0 &(x,y)\in {{\mathbb  R}}^2,\\ u(x,0)=\varphi(x), &x\in
   {{\mathbb  R}},\end{cases}
   \qquad \text{og} \qquad
   \begin{cases} Lu =0 &(x,y)\in {{\mathbb  R}}^2,\\ u(0,y)=\varphi(y), &y\in
   {{\mathbb  R}},\end{cases}

hafi ótvírætt ákvarðaða lausn fyrir sérhvert gefið fall
:math:`\varphi\in C^1({{\mathbb  R}})`.

a) :math:`Lu= 2{\partial}_xu+3{\partial}_yu`,

b) :math:`Lu= {\partial}_xu+y{\partial}_yu`,

c) :math:`Lu= y{\partial}_xu-x{\partial}_yu`,

d) :math:`Lu= y{\partial}_xu+x{\partial}_yu`.

Dæmi
^^^^

Sýnið að sérhver lausn :math:`u\in C^1({{\mathbb  R}}^2)` á jöfnunni
:math:`a{\partial}_xu+b{\partial}_yu+cu=0`, þar sem :math:`a\neq 0`, sé
af gerðinni :math:`u(x,y)=e^{-cx/a}f(bx-ay)`, þar sem
:math:`f\in C^1({{\mathbb  R}})`.

Dæmi
^^^^

Sýnið að almenn lausn hliðruðu jöfnunnar
:math:`a{\partial}_xu+b{\partial}_yu=f(x,y)`,
:math:`(x,y)\in {{\mathbb  R}}^2` sé gefin með formúlunni

.. math:: u(x,y)=(a^2+b^2)^{-\frac 12}\int_L f\, ds+g(bx-ay),

þar sem :math:`L` táknar línustrikið á kennilínunni gegnum
:math:`(x,y)` með endapunktana :math:`(x,y)` og skurðpunktinn við
:math:`y`-ásinn og :math:`g` er fall af einni breytistærð.

Dæmi
^^^^

Beitið Laplace-ummyndun til þess að ákvarða formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases}
   \dfrac{{\partial} u}{{\partial} t}+(x^2+1)
   \dfrac{\partial u}{{\partial} x}-u=0,
   &x>0, \ t>0,\\
   u(x,0)=0, \ u(0,t)=g(t), 
   &x>0, \ t>0,
   \end{cases}

þar sem :math:`g\in C^1({{\mathbb  R}}_+)`, :math:`g(0)=0` og
:math:`g{{^{\prime}}}(0)=0`.

Dæmi
^^^^

Beitið Laplace-ummyndun til þess að ákvarða formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial x}+x\dfrac{\partial u}{\partial t}=0,
   &x>0, \ t>0,\\
   u(x,0)=0, u(0,t)=t, 
   &x>0, \ t>0.
   \end{cases}

Dæmi
^^^^

Beitið Laplace-ummyndun til þess að ákvarða formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial x}+2x\dfrac{\partial u}{\partial t}=2x,
   &x>0, \ t>0,\\
   u(x,0)=u(0,t)=1, 
   &x>0, \ t>0.
   \end{cases}

Dæmi
^^^^

Beitið Laplace-ummyndun til þess að ákvarða formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases}
   \dfrac{\partial^2 u}{\partial x^2}+\dfrac{\partial^2 u}{\partial
   x\partial t} -2\dfrac{\partial^2 u}{\partial t^2}=0,
   &x\in {{\mathbb  R}}, \ t>0,\\
   u(x,0)=\partial_tu(x,0)=\lim_{x\to +\infty}u(x,t)=0, u(0,t)=f(t), 
   &x>0, \ t>0,
   \end{cases}

þar sem :math:`f` er gefið fall á :math:`{{\mathbb  R}}_+`.

Dæmi
^^^^

Beitið Laplace-ummyndun til þess að ákvarða formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases}
   \dfrac{\partial^2 u}{\partial x^2}-2\dfrac{\partial^2 u}{\partial
   x\partial t} + \dfrac{\partial^2 u}{\partial t^2}=0,
   &0<x<1, \ t>0,\\
   u(x,0)=\partial_tu(x,0)=0, &0<x<1,\\
   u(0,t)=0, \ u(1,t)=f(t), 
   &x>0, \ t>0,
   \end{cases}

þar sem :math:`f` er gefið fall á :math:`{{\mathbb  R}}_+`.
