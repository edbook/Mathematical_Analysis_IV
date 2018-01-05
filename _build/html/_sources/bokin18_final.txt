
Bylgjujafnan
============

Inngangur
---------

Við höfum séð í ýmsum sýnidæmum að bylgjujafnan er ákaflega mikilvæg í
eðlisfræðinni. Í einni rúmvídd geta lausnir hennar lýst sveiflum strengs
og langsveiflum í bitum, í tveimur rúmvíddum geta lausnirnar lýst
sveiflum himnu og í þremur víddum geta lausnir hennar verið
rafsegulbylgjur, hljóðbylgjur í lofti og þrýstibylgjur í vökvum. Við
höfum fram til þessa mest fengist við að reikna út lausnir á
bylgjujöfnunni, sem eru skilgreindar á takmörkuðum svæðum í rúminu, og
beittum Fourier-röðum og eiginfallaröðum til þess. Nú ætlum við að
fjalla um formúlur sem gilda um lausnir á öllu rúminu.

Einvíða bylgjujafnan á öllu rúminu
----------------------------------

Einvíða bylgjujafnan á öllu rúminu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við tökum nú fyrir einvíðu bylgjujöfnuna,

.. math::

  \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=0,

og byrjum á því að finna almenna lausn á henni sem er skilgreind fyrir
öll :math:`x\in {{\mathbb  R}}` og öll :math:`t\in {{\mathbb  R}}`.
Aðferðin byggir á þeirri einföldu staðreynd að hægt er að þátta
hlutafleiðuvirkjann í samskeytingu tveggja línulegra fyrsta stigs virkja

.. math::

  \partial_t^2-c^2\partial_x^2=
   (\partial_t+c\partial_x)
   (\partial_t-c\partial_x)=
   (\partial_t-c\partial_x)
   (\partial_t+c\partial_x).

Við sjáum nú að sérhvert fall af gerðinni

.. math:: u(x,t)=f(x+ct)+g(x-ct),

þar sem :math:`f,g\in C^2({{\mathbb  R}})` er lausn á bylgjujöfnunni, 
því :math:`(\partial_t-c\partial_x)f(x+ct)=0` og
:math:`(\partial_t+c\partial_x)g(x-ct)=0`. Til þess að sýna fram á að
sérhver lausn sé af þessari gerð, þá skiptum við yfir í
svokölluð *kennihnit*, en það felst í því að innleiða hnit þannig að
hnitaásarnir verði kennilínur fyrsta stigs virkjanna í þáttuninni
hér að framan. Við skilgreinum

.. math:: \xi=x+ct, \qquad \eta=x-ct,

leysum síðan :math:`x` og :math:`t` út úr þessum jöfnum

.. math:: x=(\xi+\eta)/2, \qquad t=(\xi-\eta)/2c

og skilgreinum fallið
:math:`v(\xi,\eta)=u((\xi+\eta)/2,(\xi-\eta)/2c)=u(x,t)`. Keðjureglan
gefur

.. math::

  \begin{aligned}
   \partial_\xi v(\xi,\eta)&=
   \dfrac 12 \partial_x u(x,t)+\dfrac 1{2c}\partial_tu(x,t)\\
   &=\dfrac 1{2c}\big( \partial_t u(x,t)+ c\partial_xu(x,t)\big),\\
   \partial_\eta v(\xi,\eta)&=
   \dfrac 12 \partial_x u(x,t)-\dfrac 1{2c}\partial_tu(x,t)\\
   &=-\dfrac 1{2c}\big( \partial_t u(x,t)-c\partial_xu(x,t)\big).\end{aligned}

Þessi útreikningur segir okkur að
:math:`\partial_t+c\partial_x=2c\partial_\xi` og
:math:`\partial_t-c\partial_x=-2c\partial_{\eta}`. Þar með er

.. math::

  \big(\partial_t^2-c^2\partial_x^2\big)u(x,t)=
   -4c^2\partial_\xi\partial_\eta v(\xi,\eta).

Nú sjáum við að :math:`u` er lausn á bylgjujöfnunni þá og því aðeins að
:math:`\partial_\xi\partial_\eta v=0`. Þetta segir okkur að
:math:`\partial_\eta v` sé óháð :math:`\xi`,
:math:`\partial_\eta v(\xi,\eta)=h(\eta)`. Við heildum nú þessa jöfnu,

.. math:: v(\xi,\eta)=f(\xi)+\int_0^\eta h(\tau)\, d\tau=f(\xi)+g(\eta).

Hér er heildunarfastinn :math:`f(\xi)` háður :math:`\xi` og
:math:`g(\eta)` er stofnfall af :math:`h`. Með því að skipta aftur yfir
í :math:`(x,t)`-hnitin, þá fæst niðurstaðan:

Setning
^^^^^^^

Sérhver lausn :math:`u\in C^2({{\mathbb  R}}^2)` á bylgjujöfnunni
:math:`\partial_t^2u-c^2\partial_x^2u=0` er af gerðinni
:math:`u(x,t)=f(x+ct)+g(x-ct)`, þar sem
:math:`f,g\in C^2({{\mathbb  R}})`. Ef
:math:`u(x,t)=f_1(x+ct)+g_1(x-ct)` er önnur slík framsetning á
lausninni, þá er til fasti :math:`A` þannig að :math:`f_1(x)=f(x)+A` og
:math:`g_1(x)=g(x)-A`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við eigum aðeins eftir að sanna síðustu staðhæfinguna. Athugum að
:math:`\partial_xu(x,0)=f{{^{\prime}}}(x)+g{{^{\prime}}}(x)=f_1{{^{\prime}}}(x)+g_1{{^{\prime}}}(x)`
og
:math:`\partial_tu(x,0)/c=f{{^{\prime}}}(x)-g{{^{\prime}}}(x)=f_1{{^{\prime}}}(x)-g_1{{^{\prime}}}(x)`.
Út úr þessu lesum við að :math:`f_1(x)=f(x)+A` og :math:`g_1(x)=g(x)+B`
þar sem :math:`A` og :math:`B` eru heildunarfastar. Að lokum, þá gefur
jafnan :math:`u(x,0)=f_1(x)+g_1(x)=f(x)+g(x)+A+B=f(x)+g(x)` okkur að
:math:`A+B=0`.

.. end-toggle::

Lausnin :math:`u` í þessari setningu samanstendur af tveimur bylgjum,
sem hreyfast eftir :math:`x`-ásnum sem föll af tíma. Graf fallsins
:math:`x\mapsto f(x+ct)` er hliðrum á grafi fallsins :math:`f` um
:math:`-ct` og sú færsla með tíma er lýsing á bylgju, sem berst til
vinstri á ásnum með hraðanum :math:`-c`. Graf fallsins
:math:`x\mapsto g(x-ct)` er hliðrun á grafi fallsins :math:`g` um
:math:`ct` og því lítum við á það sem bylgju, sem berst til hægri á
ásnum með hraðanum :math:`c`.

Bylgjujafnan með upphafsskilyrðum
---------------------------------

Bylgjujafnan með upphafsskilyrðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við snúa okkur að upphafsgildisverkefninu

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=0, &x\in {{\mathbb  R}},\ t>0, \\
   u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x\in {{\mathbb  R}}.
   \end{cases}

Hér á að túlka upphafsgildin þannig að

.. math::

  \lim\limits_{t\to 0+}u(x,t)=\varphi(x) \qquad \text{ og } \qquad
   \lim\limits_{t\to 0+}\partial_tu(x,t)=\psi(x).

Sérhverja lausn :math:`u` á bylgjujöfnunni má rita sem
:math:`u(x,t)=f(x+ct)+g(x-ct)` og því segja upphafskilyrðin að

.. math::

  u(x,0)=f(x)+g(x)=\varphi(x), \qquad
   \partial_tu(x,0)=cf{{^{\prime}}}(x)-cg{{^{\prime}}}(x)=\psi(x).

Þessar jöfnur gefa síðan

.. math::

  f{{^{\prime}}}(x)+g{{^{\prime}}}(x)=\varphi{{^{\prime}}}(x), \qquad
   f{{^{\prime}}}(x)-g{{^{\prime}}}(x)={\psi}(x)/c.

Við leysum þær og fáum

.. math::

  f{{^{\prime}}}(x)=\dfrac 12 \varphi{{^{\prime}}}(x)+\dfrac 1{2c}\psi(x), \qquad
   g{{^{\prime}}}(x)=\dfrac 12 \varphi{{^{\prime}}}(x)-\dfrac 1{2c}\psi(x).

Að lokum fáum við með heildun

.. math::

  \begin{aligned}
   f(x)&=\dfrac 12\varphi(x)+\dfrac 1{2c}\int_0^x\psi(y)\, dy+A,\\
   g(x)&=\dfrac 12\varphi(x)-\dfrac 1{2c}\int_0^x\psi(y)\, dy+B,\end{aligned}

þar sem :math:`A` og :math:`B` eru heildunarfastar. Skilyrðið
:math:`u(x,0)=f(x)+g(x)=\varphi(x)+A+B` segir okkur að :math:`A+B=0` og
þar með er niðurstaðan fengin:

Setning
^^^^^^^

Upphafsgildisverkefnið 

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=0, &x\in {{\mathbb  R}},\ t>0, \\
   u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x\in {{\mathbb  R}}.
   \end{cases}

hefur ótvírætt ákvarðaða lausn

.. math::

  u(x,t)=\dfrac 12\big(\varphi(x+ct)+\varphi(x-ct)\big)
   +\dfrac 1{2c}\int_{x-ct}^{x+ct}\psi({\xi})\, d{\xi}.

--------------

Athugum að fyrri liðurinn í þessari lausnarformúlu er meðaltalið af gildum
fallsins :math:`{\varphi}` í punktunum :math:`x+ct` og :math:`x-ct` og
síðari liðurinn er margfeldið af :math:`t` og meðaltalinu af gildum
:math:`{\psi}` á bilinu :math:`[x-ct,x+ct]`. Heildið í formúlunni
er unnt að rita sem földun

.. math::

  \dfrac 1{2c}\int_{x-ct}^{x+ct}\psi(y)\, dy
   =\int_{-\infty}^{+\infty}E_t(x-y)\psi(y)\, dy = \big(E_t\ast \psi\big)(x),

þar sem fallið :math:`E` er skilgreint með

.. math::

  E_t(x)=E(x,t)= \begin{cases} 1/2c, &|x|\leq ct,\\ 0,
    &|x|>ct.\end{cases}

Í útreikningum okkar þurfum við ýmist að líta á :math:`E` sem fall af
tveimur breytistærðum :math:`(x,t)` eða sem fall af einni breytistærð
:math:`x` fyrir fast :math:`t`. Í fyrra tilfellinu skrifum við
:math:`E(x,t)`, en í því síðara skrifum við :math:`E_t(x)`. Við sjáum
einnig að fyrri liðurinn í hægri hlið í lausnarformúlunni er

.. math::

  \dfrac 12\big(\varphi(x+ct)+\varphi(x-ct)\big)
   =\dfrac{\partial}{\partial t}\bigg(
   \dfrac 1{2c}\int_{x-ct}^{x+ct}\varphi(y)\, dy
   \bigg) =\dfrac{\partial}{\partial t} E_t\ast \varphi(x).

Þar með er hægt að umskrifa lausnina í

.. math::

  u(x,t)=\dfrac{\partial}{\partial t}\big( E_t\ast \varphi\big)(x)+
   E_t\ast \psi(x).

.. figure:: ./myndir/fig151.svg
    :align: center
    :alt: Lausn bylgjujöfnunnar með :math:`{\psi}=0`.

    Mynd: Lausn bylgjujöfnunnar með :math:`{\psi}=0`.

Nú er tilvalið að líta aftur á upphafsgildisverkefnið hér að framan og
leiða lausnarformúlana út með því að beita Fourier-ummyndun. Athugum
fyrst að

.. math::

  \begin{aligned}
   \widehat E_t(\xi)&=\int_{-\infty}^{+\infty}e^{-ix\xi}E_t(x)\, dx
   =\dfrac 1{2c}\int_{-ct}^{ct}e^{-ix\xi}\, dx\\
   &=\dfrac 1{2c}\bigg[\dfrac{e^{-ix\xi}}{-i\xi}\bigg]_{-ct}^{ct}
   =\dfrac{\sin(ct\xi)}{c\xi}.\end{aligned}

Nú gerum við ráð fyrir því að bæði föllin :math:`\varphi` og
:math:`\psi` séu heildanleg og að lausnin :math:`u` sé heildanlegt fall
af :math:`x` fyrir fast :math:`t`. Við látum :math:`\widehat u(\xi,t)`
tákna Fourier-myndina af :math:`u` með tilliti til :math:`x` fyrir fast
:math:`t`. Við gerum einnig ráð fyrir að flytja megi afleiður af
:math:`u` með tilliti til :math:`t` fram fyrir Fourier-heildið,

.. math::

  {{\cal F}}\{\partial_t^ju\}(\xi,t)
   =\int\limits_{-\infty}^{+\infty}e^{-ix\xi}\partial_t^ju(x,t)\, dx
   =\partial_t^j\int\limits_{-\infty}^{+\infty}e^{-ix\xi}u(x,t)\, dx
   =\partial_t^j\widehat u(\xi,t).

Reikniregla (ix) fyrir Fourier-ummyndun gefur okkur

.. math::

  {{\cal F}}\{{\partial}_x^2u\}({\xi},t)
   =\int\limits_{-\infty}^{+\infty}e^{-ix\xi}\partial_x^2u(x,t)\, dx
   =(i{\xi})^2\widehat u({\xi},t)=-{\xi}^2\widehat u({\xi},t).

Ef vil tökum nú Fourier-mynd af öllum liðunum í 

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=0, &x\in {{\mathbb  R}},\ t>0, \\
   u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x\in {{\mathbb  R}},
   \end{cases}

þá
fáum við að :math:`\widehat u({\xi},t)` verður að uppfylla

.. math::

  \begin{cases}
   {\partial}_t^2\widehat u({\xi},t)+c^2{\xi}^2
   \widehat u({\xi},t)=0, &{\xi}\in {{\mathbb  R}},\ t>0,\\
   \widehat u({\xi},0)=\widehat\varphi({\xi}), \quad {\partial}_t\widehat
   u({\xi},t)=\widehat{\psi}({\xi}), &{\xi}\in {{\mathbb  R}}.
   \end{cases}

Þetta er annars stigs venjuleg afleiðujafna í :math:`t`, fyrir fast
:math:`{\xi}` með upphafsskilyrðum. Afleiðuvirkinn er
:math:`D_t^2+c^2{\xi}^2` og því er lausnin

.. math::

  \begin{aligned}
   \widehat u({\xi},t)&=
   \cos(ct{\xi})\widehat\varphi({\xi})
   +\dfrac{\sin(ct{\xi})}{c{\xi}}\widehat{\psi}({\xi}) \\
   &=\dfrac{\partial}{\partial t}\widehat E_t({\xi})\widehat\varphi({\xi})
   +\widehat E_t({\xi})\widehat {\psi}({\xi}).\end{aligned}

Nú beitum við andhverfuformúlu Fouriers og földunarreglunni (xi), og fáum sömu formúlu aftur

.. math::

  \begin{aligned}
   u(x,t) &=\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \widehat u({\xi},t)\, d{\xi}\\
   &=\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \dfrac{\partial}{\partial t}\widehat E_t({\xi})
   \widehat \varphi({\xi})\, d{\xi}
   +\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \widehat E_t({\xi})\widehat{\psi}({\xi})\, d{\xi}\\
   &=\dfrac{\partial}{\partial t}\bigg(
   \dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \widehat E_t({\xi})
   \widehat \varphi({\xi})\, d{\xi}\bigg)
   +\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \widehat E_t({\xi})\widehat{\psi}({\xi})\, d{\xi}\\
   &={\partial}_t\big(E_t\ast \varphi\big)(x)+E_t\ast {\psi}(x).\end{aligned}

Hliðraða bylgjujafnan
---------------------

Nú skulum við ákvarða lausn á hliðruðu bylgjujöfnunni með óhliðruðum
upphafsskilyrðum,

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=f(x,t), &x\in {{\mathbb  R}}, \ t>0,\\
   u(x,0)=\partial_tu(x,0)=0, &x\in {{\mathbb  R}},
   \end{cases}

og beita til þess Fourier-ummyndun. Með nákvæmlega sömu rökum og í greininni hér fyrir framan fáum við nú að

.. math::

  \begin{cases}
   {\partial}_t^2\widehat u({\xi},t)+c^2{\xi}^2
   \widehat u({\xi},t)=\widehat f({\xi},t), &{\xi}\in {{\mathbb  R}},\ t>0,\\
   \widehat u({\xi},0)={\partial}_t\widehat u({\xi},0)=0, &{\xi}\in {{\mathbb  R}}.
   \end{cases}

Green-fall afleiðuvirkjans :math:`D_t^2+c^2{\xi}^2` er
:math:`G_{\xi}(t,{\tau})=g({\xi},t-{\tau})`, þar sem
:math:`g({\xi},t)=\sin(ct{\xi})/c{\xi}=\widehat E_t({\xi})=\widehat E({\xi},t)`. Fourier-myndin er því

.. math::

  \widehat u({\xi},t)
   =\int_0^t  g({\xi},t-\tau)\widehat f({\xi},\tau)\, d{\tau}
   =\int_0^t\widehat E({\xi},t-\tau)\widehat f({\xi},\tau)\, d{\tau}

og andhverfuformúla Fouriers og földunarreglan segja okkur að

.. math::

  \begin{aligned}
   u(x,t)&
   =\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \bigg(\int_0^t \widehat E({\xi},t-\tau)\widehat f({\xi},\tau)\, d{\tau}\bigg)
   \, d{\xi}\label{15.4.3}\\
   &=\int_0^t \bigg(\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \widehat E({\xi},t-\tau)\widehat f({\xi},\tau)\, d{\xi}\bigg)
   \, d{\tau}\nonumber\\
   &=\int_0^t \int_{-\infty}^{+\infty}
   E(x-y,t-\tau)f(y,\tau)\, dy\, d{\tau}.\nonumber\end{aligned}

Földun tveggja falla :math:`F` og :math:`G` á :math:`{{\mathbb  R}}^n`
er skilgreind með heildinu

.. math::

  F\ast G({\xi})=\int_{{{\mathbb  R}}^n}
   F({\xi}-\eta)G(\eta)\, d{\eta}, \qquad {\xi}\in {{\mathbb  R}}^n.

Nú er :math:`E(x,t)=0` ef :math:`t<0` og ef við skilgreinum
:math:`f(x,t)=0` fyrir :math:`t<0`, þá fáum við formúluna

.. math:: u(x,t)= E\ast f(x,t), \qquad x\in {{\mathbb  R}}, \ t>0.

Lítum nú aftur á tvær síðustu formúlur fyrir :math:`u(x,t)` og stingum inn
skilgreiningunni á :math:`E`,

.. math::

  \begin{aligned}
   u(x,t)
   &=\int_0^t \int_{-\infty}^{+\infty} E(x-y,t-\tau)f(y,\tau)\, dy\, 
   d{\tau}\\
   &=\dfrac 1{2c} \int_0^t \int_{x-c(t-\tau)}^{x+c(t-\tau)} 
   f(y,{\tau})\, dyd{\tau}\nonumber\\
   &=\dfrac 1{2c}\iint\limits_{T(x,t)}f(y,{\tau})\, dyd{\tau},\nonumber\end{aligned}

þar sem :math:`T(x,t)` táknar þríhyrninginn í :math:`(y,{\tau})`-planinu
með hornpunktana :math:`(x,t)`, :math:`(x-ct,0)` og :math:`(x+ct,0)`.

Formúlur d’Alemberts, Poissons og Kirchhoffs
--------------------------------------------

Formúlur d’Alemberts, Poissons og Kirchhoffs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Niðurstaðan úr útreikningum okkar í síðustu tveimur greinum er mun
víðtækari en forsendur okkar sögðu til um. Við gerðum ráð fyrir því að
föllin :math:`u`, :math:`f`, :math:`{\varphi}` og :math:`{\psi}` væru
heildanleg með tilliti til :math:`x` á öllum ásnum
:math:`{{\mathbb  R}}` og gátum leitt út formúlu fyrir :math:`u`. Nú
kemur í ljós að formúlan gildir fyrir miklu stærri flokk af föllum:

Setning
^^^^^^^

(*d’Alembert-formúlan*).   Látum :math:`f` vera samfellt deildanlegt
fall á :math:`\{(x,t); t>0\}`, samfellt á :math:`\{(x,t); t\geq 0\}` og
:math:`f(x,t)=0` ef :math:`t<0`, látum :math:`{\varphi}` vera tvisvar
samfellt deildanlegt fall á :math:`{{\mathbb  R}}` og :math:`{\psi}`
vera samfellt deildanlegt á :math:`{{\mathbb  R}}`. Þá hefur
upphafsgildisverkefnið

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=f(x,t), &x\in {{\mathbb  R}}, \ t>0,\\
   u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x\in {{\mathbb  R}},
   \end{cases}

ótvírætt ákvarðaða lausn, sem gefin er með formúlunni

.. math::

  \begin{aligned}
   u(x,t)&=\dfrac 12\big(\varphi(x+ct)+\varphi(x-ct)\big)
   +\dfrac 1{2c}\int_{x-ct}^{x+ct}\psi({\xi})\, d{\xi}\nonumber\\
   &+\dfrac 1{2c}\iint\limits_{T(x,t)}f({\xi},{\tau})\, 
   d{\xi}d{\tau},\\
   &=\dfrac{{\partial}}{{\partial} t}\big(E_t\ast {\varphi}\big)(x)+
   E_t\ast {\psi}(x) + E\ast f(x,t),\nonumber\end{aligned}

þar sem fallið :math:`E` er skilgreint með

.. math::

  E_t(x)=E(x,t)= \begin{cases} 1/2c, &|x|\leq ct,\\ 0,
    &|x|>ct\end{cases}

og
:math:`T(x,t)` táknar þríhyrninginn með hornpunktana :math:`(x,t)`,
:math:`(x-ct,0)` og :math:`(x+ct,0)`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við byrjum á ótvíræðninni. Látum :math:`u_1` og :math:`u_2` vera tvær
lausnir á upphafsgildisverkefninu. Þá er mismunurinn :math:`u` lausn á óhliðruðu
jöfnunni með :math:`{\varphi}={\psi}=0`. Samkvæmt ótvíræðni lausn á bylgjujöfnunni með upphafsskilyrðum er
:math:`u` núllfallið og þar með er :math:`u_1=u_2`. Þetta segir okkur að
lausnin á upphafsgildisverkefninu er ótvírætt ákvörðuð ef við getum sýnt fram á
að fallið :math:`u(x,t)` er lausn.

Ótvíræðni lausn á bylgjujöfnunni með upphafsskilyrðum segir okkur að summan af tveimur fyrstu liðunum í
lausnarformúlunni leysi óhliðruðu jöfnuna með hliðruðum
upphafsskilyrðum. Við eigum aðeins eftir að staðfesta að tvöfalda
heildið skilgreini lausn á hliðruðu jöfnunni með óhliðruðum
upphafsskilyrðum. Þessi liður er gefinn með

.. math::

  v(x,t)=\dfrac 1{2c} \int_0^t\bigg(
    \int_{x-c(t-\tau)}^{x+c(t-\tau)} f(y,{\tau})\, dy\bigg)\, d{\tau}

og út frá þessari framsetningu er auðvelt að reikna út hlutafleiðurnar,

.. math::

  \begin{aligned}
   {\partial}_tv(x,t)&=
   \dfrac 1{2c}\int_{x-c(t-t)}^{x+c(t-t)}f(y,t)\, dy\\
   &+\dfrac 1{2c}\int_0^t\bigg(c\cdot f(x+c(t-{\tau}),{\tau}) - 
   (-c)\cdot f(x-c(t-{\tau}),{\tau})\bigg)\, d{\tau}\\
   &=\dfrac 1{2}\int_0^t\bigg(f(x+c(t-{\tau}),{\tau})+ 
   f(x-c(t-{\tau}),{\tau})\bigg)\, d{\tau},\end{aligned}

.. math::

  \begin{aligned}
   {\partial}_t^2v(x,t)&=
   \dfrac 1{2}\bigg(f(x+c(t-t),t)+ 
   f(x-c(t-t),t)\bigg)\\
   &+\dfrac 1{2}\int_0^t\bigg(c{\partial}_xf(x+c(t-{\tau}),{\tau})+ 
   (-c){\partial}_xf(x-c(t-{\tau}),{\tau})\bigg)\, d{\tau}\\
   &=f(x,t)+\dfrac c{2}\int_0^t\bigg({\partial}_xf(x+c(t-{\tau}),{\tau})- 
   {\partial}_xf(x-c(t-{\tau}),{\tau})\bigg)\, d{\tau},\end{aligned}

.. math::

  {\partial}_xv(x,t)=\dfrac 1{2c}\int_0^t
   \bigg(f(x+c(t-{\tau}),{\tau})-f(x-c(t-{\tau}),{\tau})\bigg)d{\tau},

.. math::

  {\partial}_x^2v(x,t)=\dfrac 1{2c}\int_0^t
   \bigg({\partial}_xf(x+c(t-{\tau}),{\tau})
   -{\partial}_xf(x-c(t-{\tau}),{\tau})\bigg)d{\tau}.

Af þessum formúlum sést greinilega að :math:`v` uppfyllir hliðruðu
bylgjujöfnuna með óhliðruðum upphafsskilyrðum.

.. end-toggle::

Þríhyrningurinn :math:`T(x,t)` nefnist *ákvörðunarsvæði* punktins
:math:`(x,t)`. Þessi nafngift er til komin vegna þess að gildi
lausnarinnar ákvarðast af gildum :math:`{\varphi}` í tveimur hornpunktum
þríhyrningsins, :math:`(x-ct,0)` og :math:`(x+ct,0)`, af gildum
:math:`{\psi}` á hliðinni á milli þessara punkta og gildum hægri hliðar
bylgjujöfnunnar :math:`f` á þríhyrningnum.

.. figure:: ./myndir/fig152.svg
    :align: center
    :alt: Ákvörðunarsvæði punktsins :math:`(x,t)`.

    Mynd: Ákvörðunarsvæði punktsins :math:`(x,t)`.

Ef :math:`(x_0,t_0)` er punktur í :math:`(x,t)`-planinu, þá nefnist
svæðið milli línanna :math:`x+ct=x_0+ct_0` og :math:`x-ct=x_0-ct_0` þar
sem :math:`t\geq t_0`, *áhrifasvæði* punktsins :math:`(x_0,t_0)`. Gildi
lausnarinnar :math:`u` í sérhverjum punkti :math:`(x,t)` í áhrifasvæði
punktsins :math:`(x_0,t_0)` verður þannig fyrir áhrifum af gildi
fallsins :math:`f` í punktinum :math:`(x_0,t_0)`. Ef :math:`t_0=0` og
:math:`x-ct\leq x_0 \leq x+ct=x_0`, þá verður :math:`u(x,t)` fyrir
áhrifum af gildi :math:`{\psi}` í :math:`x_0`. Ef :math:`t_0=0` og
:math:`x+ct=x_0` eða :math:`x-ct=x_0`, þá verður gildi lausnarinnar
einnig fyrir áhrifum af gildum :math:`{\varphi}` í :math:`x_0`.

.. figure:: ./myndir/fig153.svg
    :align: center
    :alt: Áhrifasvæði punktsins :math:`(x_0,t_0)`.

    Mynd: Áhrifasvæði punktsins :math:`(x_0,t_0)`.

Formúla d’Alemberts á sér hliðstæðu í tveimur og þremur rúmvíddum. Þá
lítum við á verkefnið

.. math::

  \begin{cases}
   {\partial^2_tu}-c^2\Delta u=f(x,t), &x\in {{\mathbb  R}}^n, \ t>0,\\
   u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x\in {{\mathbb  R}}^n,
   \end{cases}

þar sem við táknum hnit punktanna með :math:`x=(x_1,\dots,x_n)` og
látum :math:`\Delta` tákna Laplace-virkjann á :math:`{{\mathbb  R}}^n`.
Ef víddin :math:`n` er :math:`2`, þá hefur verkefnið ótvírætt ákvarðaða
lausn, sem gefin er með *Poisson-formúlunni*,

.. math::

  \begin{aligned}
   u(x,t)
   &=
   \dfrac{{\partial}}{{\partial} t}
   \bigg(\dfrac 1
   {2{\pi}c} \iint_{S(x,ct)} 
   \dfrac{\varphi({\xi})}
   {\sqrt{c^2t^2-|x-{\xi}|^2}}\, dA({\xi})\bigg)\nonumber\\
   &+
   \dfrac 1 {2{\pi}c} \iint_{S(x,ct)} 
   \dfrac{{\psi}({\xi})}
   {\sqrt{c^2t^2-|x-{\xi}|^2}}\, dA({\xi})\\
   &+
   \dfrac 1 {2{\pi}c} \int_0^t\iint_{S(x,c(t-{\tau}))} 
   \dfrac{f({\xi},{\tau})}
   {\sqrt{c^2(t-{\tau})^2-|x-{\xi}|^2}}\, dA({\xi})d{\tau},\nonumber\end{aligned}

þar sem :math:`S(x,r)` táknar opnu skífuna með miðju í :math:`x` og
geislann :math:`r`, :math:`|x|` táknar lengd :math:`x` og :math:`dA`
táknar flatarmálsfrymið. Ef víddin :math:`n` er :math:`3`, þá er lausnin
hins vegar gefin með *Kirchhoff-formúlunni*,

.. math::

  \begin{aligned}
   u(x,t)
   &=
   \dfrac{{\partial}}{{\partial} t}
   \bigg(\dfrac 1
   {4{\pi}c^2t} \iint_{{\partial}B(x,ct)} 
   \varphi({\xi})
   \, dS({\xi})\bigg)\nonumber\\
   &+
   \dfrac 1 {4{\pi}c^2t} \iint_{{\partial}B(x,ct)} 
   {\psi}({\xi})  dS({\xi})\\
   &+
   \dfrac 1 {4{\pi}c^2} \iiint_{B(x,ct)} 
   \dfrac{f({\xi},t-|x-{\xi}|/c)}
   {|x-{\xi}|}\, dV({\xi}),\nonumber\end{aligned}

þar sem :math:`B(x,r)` táknar kúlu með miðju í :math:`x` og geislann
:math:`r`, :math:`{\partial}B(x,r)` táknar yfirborð hennar, :math:`dS`
táknar flatarmálsfrymið á yfirborðinu og :math:`dV` táknar
rúmmálsfrymið.

.. figure:: ./myndir/fig1512.svg
    :align: center
    :alt: Ljóskeila og ákvörðunarsvæði.

    Mynd: Ljóskeila og ákvörðunarsvæði.

Ef :math:`(x,t)\in {{\mathbb  R}}^n\times {{\mathbb  R}}`, þá nefnast
mengin

.. math::

  \begin{aligned}
   V(x,t)&=\{({\xi},{\tau});  |x-{\xi}|\leq c|t-{\tau}|\},\\
   V(x,t)^+&=\{({\xi},{\tau})\in V(x,t); {\tau}\geq t\},\\
   V(x,t)^-&=\{({\xi},{\tau})\in V(x,t); {\tau}\leq t\},\end{aligned}

*ljóskeila*, *framtíðarljóskeila* og *fortíðarljóskeila* í punktinum
:math:`(x,t)` í tímarúminu. Á formúlum Poissons og Kirchhoffs sjáum við
að það er mikill eðlismunur á bylgjuútbreiðslu í tveimur og þremur
víddum. Í tveimur víddum ákvarðast lausnin :math:`u(x,t)` af gildum
:math:`f` í fortíðarljóskeilunni á tímabilinu :math:`[0,t]` og af gildum
:math:`{\varphi}` og :math:`{\psi}` í skurðplani fortíðarljóskeilunnar í
:math:`(x,t)` við planið :math:`t=0`. (Athugið að við hugsum okkur að
punktarnir :math:`x\in {{\mathbb  R}}^n` liggi í tímarúminu við tímann
:math:`t=0`.) Því er eðlilegt að skilgreina *ákvörðunarsvæði* punktsins
:math:`(x,t)` sem mengið
:math:`T(x,t)=\{({\xi},{\tau})\in V^-(x,t); 0\leq {\tau}\leq t \}` fyrir öll :math:`x\in {{\mathbb  R}}^2` og :math:`t>0`.
Í þremur rúmvíddum ákvarðast :math:`u(x,t)` af gildum :math:`f` á
yfirborði fortíðarljóskeilunnar á tímabilinu :math:`[0,t]` og af gildum
:math:`{\varphi}` og :math:`{\psi}` í skurðplani yfirborðs
fortíðarljóskeilunnar :math:`{\partial}V^-(x,t)` og plansins
:math:`t=0`. Í þremur víddum er því eðlilegt að skilgreina
ákvörðunarsvæði punktsins :math:`(x,t)`, sem mengið
:math:`T(x,t)=\{({\xi},{\tau})\in {\partial}V^-(x,t); 0\leq {\tau}\leq t \}`. *Áhrifasvæði punktsins* :math:`(x,t)` er eðlilegt að
skilgreina sem framtíðarljóskeiluna, ef rúmvíddin er :math:`2`, en
yfirborð framtíðarljóskeilunnar ef rúmvíddin er :math:`3`. Sá eiginleiki
bylgjuvirkjans í þremur víddum, að gildi lausnar á hliðruðu
bylgjujöfnunni í punkti :math:`(x,t)` skuli eingöngu ráðast af gildunum
á yfirborði fortíðarljóskeilunnar, er nefnt *lögmál Huygens*.

Yfirborðsbylgjur á vatni uppfylla tvívíða jöfnu, sem er áþekk
bylgjujöfnunni, en miklu flóknari í úrlausn. Fyrir litlar bylgjur er
hægt að gefa sér að lausnir bylgjujöfnunnar séu góð nálgun á
yfirborðsbylgjum. Ef steini er kastað í vatn í punktinum :math:`x_0` við
tímann :math:`t_0`, þá fer yfirborðsbylgja eftir vatninu og við getum
gert ráð fyrir því að frávik efnispunkts :math:`u(x,t)` í :math:`x` við
tímann :math:`t` sé gefið sem lausn á 

.. math::

  \begin{cases}
   {\partial^2_tu}-c^2\Delta u=f(x,t), &x\in {{\mathbb  R}}^n, \ t>0,\\
   u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x\in {{\mathbb  R}}^n,
   \end{cases}

þar sem
:math:`{\varphi}=0`, :math:`{\psi}=0` og :math:`f` er alls staðar
:math:`0` nema í lítilli grennd um :math:`(x_0,t_0)`. Bylgjan kemur í
punktinn :math:`x` við tímann :math:`t=|x-x_0|/c`. Poisson-formúlan
segir nú að áhrif bylgjunnar muni vara áfram í punktinum :math:`x` fyrir
öll :math:`t\geq t_0+|x-x_0|/c`.

Lítum nú á ljósgjafa í punktinum :math:`x_0\in {{\mathbb  R}}^3` sem
gefur frá sér merki sem varir örstutta stund við tímann :math:`t_0`.
Bylgjan :math:`u` sem berst frá honum er lausin á upphafsgildisverkefninu með
:math:`{\varphi}=0`, :math:`{\psi}=0` og :math:`f` er alls staðar
:math:`0` nema í lítilli grennd um :math:`(x_0,t_0)`. Nú sjáum við á
Kirchhoff-formúlunni að þegar :math:`t` er orðið það stórt að yfirborð
ljóskeilunnar í :math:`(x,t)` sker ekki svæðið þar sem :math:`f` er
frábrugðið :math:`0`, þá eru engin áhrif af ljósmerkinu í punktinum
:math:`x`. Ljósið er horfið.

Kúlubylgjur
-----------

Lausn á bylgjujöfnunni í þremur rúmvíddum, sem er einungis háð
:math:`(r,t)`, þar sem :math:`r=|x|` er lengd vigursins
:math:`x=(x_1,x_2,x_3)`, nefnist kúlubylgja. Með því að nota formúluna
fyrir Laplace-virkjann í kúluhnitum í viðauka D, fáum við að
:math:`u(r,t)` er lausn á jöfnunni

.. math::

  \dfrac{{\partial}^2u}{{\partial}t^2} -
   c^2\dfrac 1{r^2}\dfrac{{\partial}}{{\partial}r}\bigg(
   r^2\dfrac{{\partial}u}{{\partial}r}\bigg)
   =\dfrac{{\partial}^2u}{{\partial}t^2} -
   c^2\bigg(\dfrac{{\partial}^2u}{{\partial}r^2}+\dfrac
   2r\dfrac{{\partial}u}{{\partial}r}\bigg) =0.

Nú skilgreinum við fallið :math:`v(r,t)=ru(r,t)` og sjáum að

.. math::

  \dfrac{{\partial}^2v}{{\partial}t^2} -
   c^2\dfrac{{\partial}^2v}{{\partial}r^2}
   =
   r\bigg(
   \dfrac{{\partial}^2u}{{\partial}t^2} -
   c^2\bigg(\dfrac{{\partial}^2u}{{\partial}r^2}+\dfrac
   2r\dfrac{{\partial}u}{{\partial}r}\bigg)
   \bigg).

Þar með er :math:`u` kúlubylgja þá og því aðeins að :math:`v` sé lausn á
bylgjujöfnunni í einni rúmvídd.

Nú skulum við líta á bylgjujöfnuna í þremur víddum með kúlusamhverfri
hægri hlið og kúlusamhverfum upphafsgildum. Lausnin :math:`u` uppfyllir

.. math::

  \begin{cases}
   \dfrac{{\partial}^2u}{{\partial}t^2} -
   c^2\bigg(\dfrac{{\partial}^2u}{{\partial}r^2}+\dfrac
   2r\dfrac{{\partial}u}{{\partial}r}\bigg)=f(r,t), 
   &r>0, \ t>0,\\
   u(r,0)={\varphi}(r), \quad {\partial}_tu(r,0)={\psi}(r),  &r>0.
   \end{cases}

Við gerum ráð fyrir því að :math:`f` sé samfellt á
:math:`\{(r,t); r\geq 0, t\geq 0\}` og að :math:`{\varphi}` og
:math:`{\psi}` séu samfelld á :math:`\{r; r\geq 0\}`. Hliðstætt verkefni
fyrir fallið :math:`v` er þá

.. math::

  \begin{cases}
   \dfrac{{\partial}^2v}{{\partial}t^2} -
   c^2\dfrac{{\partial}^2v}{{\partial}r^2}=rf(r,t), 
   &r>0, \ t>0,\\
   v(r,0)=r{\varphi}(r), \quad {\partial}_tv(r,0)=r{\psi}(r), 
   &r\geq 0,\\
   v(0,t)=0, &t>0.
   \end{cases}

Við munum leysa þessi verkefni þegar við höfum fjallað um speglanir á
bylgjum.

Speglanir á bylgjum
-------------------

Speglanir á bylgjum
~~~~~~~~~~~~~~~~~~~

Formúla d’Alemberts lýsir lausnum einvíðu bylgjujöfnunnar á öllum
raunásnum. Með því að beita svokallaðri *speglunaraðferð* getum við
notað hana til þess að leysa bylgjujöfnuna með jaðarskilyrðum. Þetta er
auðvelt að útskýra í:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum á verkefnið

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=f(x,t), &x>0, \ t>0,\\
   u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x>0,\\
   u(0,t)=0, &t>0,
   \end{cases}

þar sem :math:`f` er gefið fall á
:math:`\{(x,t)\in {{\mathbb  R}}^2; x>0,t>0\}` og :math:`{\varphi}` og
:math:`{\psi}` eru föll á jákvæða ásnum. Við byrjum á því að framlengja
skilgreiningarsvæði :math:`f`, :math:`{\varphi}` og :math:`{\psi}`
þannig að þau verði oddstæð föll af :math:`x`,

.. math::

  \begin{cases} f_O(x,t)=f(x,t), \\ f_O(0,t)=0,\\
   f_O(x,t)=-f(-x,t),\end{cases}\quad
   \begin{cases} {\varphi}_O(x)={\varphi}(x), 
   \\ {\varphi}_O(0)=0,\\ {\varphi}_O(x)=-{\varphi}(-x),\end{cases}\quad
   \begin{cases} {\psi}_O(x)={\psi}(x), & x>0, \\ 
   {\psi}_O(0)=0, &x=0,\\ {\psi}_O(x)=-{\psi}(-x), &x<0.\end{cases}

Síðan skrifum við d’Alembert-formúluna upp

.. math::

  u(x,t)= \dfrac 12\big( {\varphi}_O(x+ct)+{\varphi}_O(x-ct)\big)
   +\dfrac 1{2c} \int_{x-ct}^{x+ct} {\psi}_O(y)\, dy
   +\dfrac 1{2c}\iint\limits_{T (x,t)}f_O(y,{\tau})\, dyd{\tau}.

Ef :math:`{\varphi}_O` er tvisvar samfellt deildanlegt,
:math:`{\psi}_O` er samfellt deildanlegt og :math:`f_O` er samfellt
deildanlegt, þá er bylgjujafnan uppfyllt með réttum upphafsskilyrðum. Í
kafla 18 munum við sjá hvernig hægt er að gefa bylgjujöfnunni merkingu,
ef föllin eru ekki tvisvar samfellt deildanleg. Nú kemur einnig í ljós
að jaðarskilyrðið er uppfyllt, því

.. math::

  \begin{aligned}
   u(0,t)&= \dfrac 12\big( {\varphi}_O(ct)+{\varphi}_O(-ct)\big)
   +\dfrac 1{2c} \int_{-ct}^{ct} {\psi}_O(y)\, dy\\
   &+\dfrac 1{2c}\int_0^t
   \int_{-c(t-{\tau})}^{c(t-{\tau})} f_O(y,{\tau})\, dy\, d{\tau},\end{aligned}

öll föllin eru oddstæð og þar með eru allir liðirnir :math:`0`.
Tilfellinu :math:`{\psi}=0` og :math:`f=0` eru auðvelt að lýsa sem
speglun á bylgjutoppi, sem kemur inn í punktinn :math:`x=0` á hraðanum
:math:`-c`, speglast þannig að hann kemur öfugur til baka og fer frá
punktinum :math:`x=0` með hraðanum :math:`c`. Af þessum eiginleika er
nafnið á lausnaraðferðinni dregið.

.. figure:: ./myndir/fig155.svg
    :align: center
    :alt: Speglun bylgju.

    Mynd: Speglun bylgju.

Ef :math:`x-ct>0`, þá nær ákvörðunarsvæði punktsins :math:`(x,t)` ekki
inn á hálfplanið :math:`\{(x,t); x\leq 0\}` og lausnarformúlan hefur sama form og áður,

.. math::

  u(x,t)= \dfrac 12\big( {\varphi}(x+ct)+{\varphi}(x-ct)\big)
   +\dfrac 1{2c} \int_{x-ct}^{x+ct} {\psi}(y)\, dy
   +\dfrac 1{2c}\iint\limits_{T(x,t)}f(y,{\tau})\, dyd{\tau}.

Ef hins vegar :math:`x-ct<0`, þá notfærum við okkur að

.. math::

  \int_{x-ct}^{ct-x}{\psi}_O(y)\, dy=0, \qquad
   \int_{x-c(t-{\tau})}^{c(t-{\tau})-x}f_O(y,{\tau})\, dy=0,

og fáum formúluna

.. math::

  u(x,t)= \dfrac 12\big( {\varphi}(x+ct)-{\varphi}(ct-x)\big)
   +\dfrac 1{2c} \int_{ct-x}^{x+ct} {\psi}(y)\, dy
   +\dfrac 1{2c}\iint\limits_{S(x,t)}f(y,{\tau})\, dyd{\tau}.

þar sem :math:`S(x,t)` táknar ferhyrninginn með hornpunktana
:math:`(x,t)`, :math:`(x+ct,0)`, :math:`(ct-x,0)` og :math:`(0,t-x/c)`.
Við getum því litið svo á að ákvörðunarsvæðið sé :math:`S(x,t)` í
tilfellinu :math:`x-ct<0`.

.. end-toggle::

.. figure:: ./myndir/fig154.svg
    :align: center
    :alt: Ákvörðunarsvæði punktsins :math:`(x,t)`, :math:`x-ct<0`.

    Mynd: Ákvörðunarsvæði punktsins :math:`(x,t)`, :math:`x-ct<0`.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Nú skulum við sjá hvernig hliðruð jaðarskilyrði eru meðhöndluð, með því
að líta á verkefnið

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=0, &x>0, \ t>0,\\
   u(x,0)=0, \quad \partial_tu(x,0)=0, &x>0,\\
   u(0,t)=g(t), &t>0,
   \end{cases}

þar sem fallið :math:`g` er skilgreint á jákvæða ásnum. Við byrjum á því
að finna fall :math:`w(x,t)`, sem uppfyllir hliðraða jaðarskilyrðið, og
skrifum :math:`u(x,t)=w(x,t)+v(x,t)`. Hér er einfaldast að setja
:math:`w(x,t)=g(t)`. Þá verður :math:`v` að vera lausn á verkefninu

.. math::

  \begin{cases}
   \dfrac{\partial^2v}{\partial t^2}
   -c^2\dfrac{\partial^2v}{\partial x^2}=-g{{^{\prime\prime}}}(t), &x>0, \ t>0,\\
   v(x,0)=-g(0), \quad \partial_tv(x,0)=-g{{^{\prime}}}(0), &x>0\\
   v(0,t)=0, &t>0,
   \end{cases}

en þetta verkefni leystum við í síðasta sýnidæmi, með
:math:`f(x,t)=-g{{^{\prime\prime}}}(t)`, :math:`{\varphi}(x)=-g(0)` og
:math:`{\psi}(x)=-g{{^{\prime}}}(0)`. Oddstæðar framlengingar á þessum
föllum eru
:math:`f_O(x,t)=-g{{^{\prime\prime}}}(t){{\operatorname{sign}}}(x)`,
:math:`{\varphi}_O(x)=-g(0){{\operatorname{sign}}}(x)`,
:math:`{\psi}_O(x)=-g{{^{\prime}}}(0){{\operatorname{sign}}}(x)`. Ef
við stingum þessum föllum inn í d’Alembert-formúluna, þá fáum við

.. math::

  \begin{aligned}
   u(x,t)&=g(t)-\dfrac{g(0)}2\big( {{\operatorname{sign}}}(x+ct)+{{\operatorname{sign}}}(x-ct)\big)
   -\dfrac {g{{^{\prime}}}(0)}{2c} \int_{x-ct}^{x+ct}{{\operatorname{sign}}}(y)\, dy\\
   &-\dfrac 1{2c}\int_0^tg{{^{\prime\prime}}}({\tau})
   \int_{x-c(t-{\tau})}^{x+c(t-{\tau})} {{\operatorname{sign}}}(y) \, dyd{\tau}.\end{aligned}

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Nú skulum við breyta verkefninu í upphafi þessarrar greinar
og setja inn
flæðisskilyrði í stað fallsjaðarskilyrðis,

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=f(x,t), &x>0, \ t>0,\\
   u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x>0,\\
   {\partial}_xu(0,t)=0, &t>0,
   \end{cases}

Nú byrjum við á því að framlengja skilgreiningarsvæði :math:`f`,
:math:`{\varphi}` og :math:`{\psi}` þannig að þau verði jafnstæð föll af
:math:`x`,

.. math::

  \begin{cases} f_J(x,t)=f(x,t), \\ f_J(x,t)=f(-x,t),\end{cases}\qquad
   \begin{cases} {\varphi}_J(x)={\varphi}(x), \\ 
   {\varphi}_J(x)={\varphi}(-x),\end{cases}\qquad
   \begin{cases} {\psi}_J(x)={\psi}(x), & x>0, \\ 
   {\psi}_J(x)={\psi}(-x), &x<0,\end{cases}

og :math:`f_J(0,t)=\lim_{x\to 0+}f(x,t)`,
:math:`{\varphi}_J(0)=\lim_{x\to 0+}{\varphi}(x)` og
:math:`{\psi}_J(0)=\lim_{x\to 0+}{\psi}(x)`. Síðan skrifum við
d’Alembert-formúluna upp

.. math::

  u(x,t)= \dfrac 12\big( {\varphi}_J(x+ct)+{\varphi}_J(x-ct)\big)
   +\dfrac 1{2c} \int_{x-ct}^{x+ct} {\psi}_J(y)\, dy
   +\dfrac 1{2c}\iint\limits_{T(x,t)}f_J(y,{\tau})\, dyd{\tau}.

Nú kemur í ljós að jaðarskilyrðið er uppfyllt, því

.. math::

  \begin{aligned}
   {\partial}_xu(0,t)&= \dfrac 12\big( {\varphi}_J{{^{\prime}}}(ct)
   +{\varphi}_J{{^{\prime}}}(-ct)\big)
   +\dfrac 1{2c}\big({\psi}_J(ct)-{\psi}_J(-ct)\big)\\
   &+\dfrac 1{2c}\int_0^t
   \big(f_J(c(t-{\tau}),{\tau})-f_J(-c(t-{\tau}),{\tau})\big)
   \, d{\tau}.\end{aligned}

Fallið :math:`{\varphi}_J{{^{\prime}}}` er oddstætt, svo það er
greinilegt að :math:`{\partial}_xu(0,t)=0`. Mynd okkar af speglun
bylgjunnar í tilfellinu :math:`{\psi}=0` og :math:`f=0` er:

.. figure:: ./myndir/fig156.svg
    :align: center
    :alt: Speglun bylgju.

    Mynd: Speglun bylgju.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Við getum einnig leyst hliðstætt verkefni og í síðasta sýnidæmi með
hliðruðum jaðarskilyrðum

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -c^2\dfrac{\partial^2u}{\partial x^2}=0, &x>0, \ t>0,\\
   u(x,0)=\partial_tu(x,0)=0, &x>0,\\
   {\partial}_xu(0,t)=g(t), &t>0.
   \end{cases}

Við byrjum á því að finna
fall :math:`w` sem uppfyllir hliðraða jaðarskilyrðið. Í þessu tilfelli
er heppilegt að velja :math:`w(x,t)=xg(t)`. Við ritum síðan lausnina á
forminu :math:`u(x,t)=w(x,t)+v(x,t)`. Þá verður :math:`v` að vera lausn
á verkefninu

.. math::

  \begin{cases}
   \dfrac{\partial^2v}{\partial t^2}
   -c^2\dfrac{\partial^2v}{\partial x^2}=-xg{{^{\prime\prime}}}(t), &x>0, \ t>0,\\
   v(x,0)=-xg(0), \quad \partial_tv(x,0)=-xg{{^{\prime}}}(0), &x>0,\\
   {\partial}_xv(0,t)=0, &t>0.
   \end{cases}

Jafnstæðar framlengingar á þessum föllum eru
:math:`f_J(x,t)=-|x|g{{^{\prime\prime}}}(t)`,
:math:`{\varphi}_J(x)=-|x|g(0)` og
:math:`{\psi}_J(x)=-|x|g{{^{\prime}}}(0)`. Því verður niðurstaðan,

.. math::

  \begin{aligned}
   u(x,t)&=xg(t)-\dfrac {g(0)}2\big(|x+ct|+|x-ct|\big)
   -\dfrac{g{{^{\prime}}}(0)}{2c}\int_{x-ct}^{x+ct} |y|\, dy\\
   &-\dfrac 1{2c}\iint_{T(x,t)} |y|g({\tau})\, dyd{\tau}.\end{aligned}

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Sveiflandi strengur; framhald

Í kaflanum um Fourier-raðir litum við á einvíðu bylgjujöfnuna og fundum formúlu
fyrir sveiflur strengs sem festur er niður í báðum endapunktum með
gefnum upphafsskilyrðum. Útslag strengsins er lausn verkefnisins

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}-
   c^2\dfrac{\partial^2u}{\partial x^2}=0, &0<x<L,\  t>0,\\
   u(x,0)=\varphi(x), \ \partial_tu(x,0)=\psi(x), &0<x<L,\\
   u(0,t)=u(L,t)=0, &t>0.
   \end{cases}

Lausnina fundum við með því að liða föllin :math:`\varphi` og
:math:`\psi` í Fourier-raðir,

.. math::

  \varphi(x)=\sum\limits_{n=1}^\infty\varphi_n\sin \big(n\pi x/L\big),
   \quad
   \psi(x)=\sum\limits_{n=1}^\infty\psi_n\sin \big(n\pi x/L\big),

og ganga út frá þeirri lausnartilgátu að :math:`u` væri af sams konar
gerð,

.. math:: u(x,t)=\sum\limits_{n=1}^\infty u_n(t)\sin \big(n\pi x/L\big).

Niðurstaðan var síðan að

.. math::

  u(x,t)=\sum\limits_{n=1}^\infty
   \bigg(\varphi_n\cos\big(n\pi ct/L\big)+
   \dfrac{\psi_n L}{n\pi c}\sin\big(n\pi ct/L\big) \bigg)
   \sin \big(n\pi x/L\big).

Upphafsgildisverkefnið er einnig hægt að leysa með speglunaraðferð.
Það er einfaldlega gert þannig að skilgreiningarsvæði fallanna
:math:`\phi` og :math:`\psi` er framlengt yfir á allan raunásinn, þannig
að út komi oddstæð :math:`2L`-lotubundin föll :math:`\varphi_O` og
:math:`\psi_O`. Síðan er d’Alembert formúlan skrifuð upp,

.. math::

  u(x,t)=\dfrac 12\big(\varphi_O(x+ct)+\varphi_O(x-ct)\big)
   +\dfrac 1{2c}\int_{x-ct}^{x+ct}\psi_O(y)\, dy,

og það er auðvelt að sannfæra sig um að þessi formúla gefi einnig
lausn. Það er líka auðvelt að sýna fram á að þessi formúla fyrir :math:`u(x,t)` leiði beint af framsetningunni með Fourier-röð.
Til þess athugum við fyrst að Fourier-raðirnar
eru :math:`2L`-lotubundin oddstæð föll á öllu
:math:`{{\mathbb  R}}` og því er

.. math::

  \varphi_O(x)=\sum\limits_{n=1}^\infty\varphi_n\sin \big(n\pi x/L\big),
   \quad
   \psi_O(x)=\sum\limits_{n=1}^\infty\psi_n\sin \big(n\pi x/L\big),
   \qquad x\in {{\mathbb  R}}.

Samlagningarformúlurnar fyrir kósínus og sínus gefa okkur

.. math::

  \begin{aligned}
   \cos\big(n\pi ct/L\big)\sin\big(n\pi x/L\big)&=
   \dfrac 12\big(\sin\big(n\pi(x+ct)/L\big)+
   \sin\big(n\pi(x-ct)/L\big)\big)\\
   \dfrac L{n\pi c}\sin\big(n\pi ct/L\big)\sin\big(n\pi x/L\big)&=
   \dfrac {-L}{2n\pi c}\big(\cos\big(n\pi(x+ct)/L\big)-
   \cos\big(n\pi(x-ct)/L\big)\big)\\
   &=\dfrac 1{2c}\int_{x-ct}^{x+ct}\sin\big(n\pi y/L\big)\, dy.\end{aligned}

Nú smeygjum við þessum formúlum inn í Fourier-röðina fyrir :math:`u(x,t)` og fáum

.. math::

  \begin{aligned}
   u(x,t)&=\sum\limits_{n=1}^\infty\varphi_n\dfrac 12
   \bigg(\sin\big(n\pi(x+ct)/L\big)+\sin\big(n\pi(x-ct)/L\big)\bigg)\\
   &+\sum\limits_{n=1}^\infty\psi_n\dfrac
   1{2c}\int_{x-ct}^{x+ct}\sin\big(n\pi y/L\big)\, dy \\
   &=\dfrac 12\bigg(\sum\limits_{n=1}^\infty\varphi_n
   \sin\big(n\pi(x+ct)/L\big)+
   \sum\limits_{n=1}^\infty\varphi_n
   \sin\big(n\pi(x-ct)/L\big)\bigg)\\
   &+\dfrac 1{2c}\int_{x-ct}^{x+ct}
   \bigg(\sum\limits_{n=1}^\infty\psi_n\sin\big(n\pi y/L\big)\bigg)\, dy\\
   &=\dfrac 12\big(\varphi_O(x+ct)+\varphi_O(x-ct)\big)
   +\dfrac 1{2c}\int_{x-ct}^{x+ct}{\psi}_O(y)\, dy.\end{aligned}

Við höfum því fengið nýja framsetningu á d’Alembert formúlunni með
Fourier-röðum.

.. end-toggle::

Úrlausn á bylgjujöfnum með Laplace-ummyndun
-------------------------------------------

Úrlausn á bylgjujöfnum með Laplace-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum nú séð hvernig hægt er að beita Fourier-ummyndun til þess að
finna formúlur fyrir lausnir á bylgjujöfnunni sem skilgreindar eru á
öllum rauntalnaásnum. Ef lausnin er gefin á hálfás, til dæmis jákvæða
tímaásnum, þá er oft snjallt að beita Laplace-ummyndun til þess að
ákvarða lausnarformúlu. Við lítum á tvö dæmi:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Bylgjujafnan á hálflínu

Við skulum ákvarða formúlu fyrir lausn bylgjujöfnunnar í einni rúmvídd á
hálflínu með óhliðruðum upphafsskilyrðum og hliðruðu jaðarskilyrði,

.. math::

  \begin{cases}
   \dfrac{\partial^2 u}{\partial t^2}-c^2
   \dfrac{\partial^2 u}{\partial x^2}=0, &x>0, \ t>0,\\
   u(x,0)=\partial_tu(x,0)=0, &x>0,\\
   u(0,t)=g(t), &t>0,\\
   \lim\limits_{x\to +\infty}u(x,t)=0, & t>0.
   \end{cases}

Við látum :math:`U(x,s)` og :math:`G(s)` tákna Laplace-myndir :math:`u`
og :math:`g` með tilliti til :math:`t`,

.. math::

  U(x,s)=\int_0^{\infty}e^{-st}u(x,t)\, dt, \qquad
   G(s)=\int_0^{\infty}e^{-st}g(t)\, dt.

Samkvæmt reiknireglunni um Laplace-myndir af afleiðum er

.. math::

  \begin{aligned}
   {{\cal L}}\{\partial_t^2u\}(x,s)&=
   \int_0^{\infty}e^{-st}\partial_t^2u(x,t)\, dt\\
   &= s^2U(x,s)-su(x,0)-\partial_tu(x,0)=s^2U(x,s).\end{aligned}

Við gerum ráð fyrir að hægt sé að taka afleiður með tilliti til
:math:`x` fram fyrir Laplace-heildið og fáum því

.. math::

  {{\cal L}}\{\partial_x^2u\}(x,s)=
   \int_0^{\infty}e^{-st}\partial_x^2u(x,t)\, dt=
   \partial_x^2\int_0^{\infty}e^{-st}u(x,t)\, dt=
   \partial_x^2U(x,s).

Eftir Laplace-ummyndun verður því upphafsgildisverkefnið að

.. math::

  \begin{cases}
   s^2U(x,s)-c^2\partial_x^2U(x,s)=0,\\
   U(0,s)=G(s),\\
   \lim\limits_{x\to +\infty}U(x,s)=0.
   \end{cases}

Hér höfum við venjulega afleiðujöfnu í :math:`x` og lausn hennar er af
gerðinni

.. math:: U(x,s)=A(s)e^{-(s/c)x}+B(s)e^{(s/c)x}.

Jaðarskilyrðið að :math:`U(x,s)\to 0` ef :math:`x\to +\infty` segir
okkur að :math:`B(s)=0` fyrir öll :math:`s>0`. Skilyrðið
:math:`U(0,s)=G(s)` segir okkur að :math:`A(s)=G(s)`. Þar með er

.. math:: U(x,s)=G(s)e^{-(s/c)x}=e^{-(x/c)s}{{\cal L}}\{g\}(s).

Nú gefur reikniregla fyrir Laplace-myndir okkur að

.. math:: U(x,s)={{\cal L}}\{H(t-x/c)g(t-x/c)\}(s),

þar sem :math:`H` táknar Heaviside-fallið. Lausnin er þar með fundin

.. math:: u(x,t)=H(t-x/c)g(t-x/c), \qquad t>0, \ x>0.

Það er auðvelt að túlka þessa formúlu. Við lítum á punktinn
:math:`(x,t)` í :math:`(\xi,\tau)`-plani. Önnur kennilína bylgjuvirkjans
í gegnum hann er gefin með jöfnunni :math:`\xi-c\tau=x-ct`. Ef hún sker
jákvæða :math:`\tau`-ásinn, þá er það í punktinum :math:`(0,t-x/c)`.
Gildið á :math:`u` í :math:`(x,t)` er jafnt gildi :math:`g` í
skurðpunktinum. Ef þessi kennilína í gegnum :math:`(x,t)` sker ekki
jákvæða :math:`\tau`-ásinn, þá er gildi :math:`u` í :math:`(x,t)` jafnt
:math:`0`.

.. figure:: ./myndir/fig157.svg
    :align: center
    :alt: Skurðpunktur kennilínu við :math:`\tau`-ás.

    Mynd: Skurðpunktur kennilínu við :math:`\tau`-ás.

Nú skulum við líta á :math:`u(x,t)` sem styrk merkis, sem berst til
hægri á :math:`x`-ásnum með hraðanum :math:`c`. Styrknum er stýrt í
punktinum :math:`x=0` þannig að :math:`u(x,t)=g(t)` er gefið fall og
stykurinn er :math:`0` í upphafi við tímann :math:`t=0`. Ef
:math:`t<x/c`, þá er tíminn of skammur til þess að merkið nái að berast
frá :math:`0` til :math:`x` og því er :math:`u(x,t)=0` í þessu tilfelli.
Ef :math:`t\geq x/c`, þá er :math:`u(x,t)=g(t-x/c)`, því það tekur tímann :math:`x/c`
fyrir merkið að berast frá :math:`0` til :math:`x`.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Bylgjujafnan á takmörkuðu bili

Við ákvörðum hér formúlu fyrir lausn bylgjujöfnunnar á takmörkuðu bili
með óhliðruðum upphafsskilyrðum og hliðruðu jaðarskilyrði í öðrum
endapunktinum,

.. math::

  \begin{cases}
   \dfrac{\partial^2 u}{\partial t^2}-c^2
   \dfrac{\partial^2 u}{\partial x^2}=0, &x>0, \ t>0,\\
   u(x,0)=\partial_tu(x,0)=0, &x>0,\\
   u(0,t)=0, \quad u(L,t)=b(t), &t>0.
   \end{cases}

Við látum :math:`U(x,s)` og :math:`B(s)` tákna Laplace-myndir fallanna
:math:`u` og :math:`b` með tilliti til :math:`t`. Á hliðstæðan hátt og í
síðasta sýnidæmi fáum við jaðargildisverkefni fyrir :math:`U(x,s)`,

.. math::

  \begin{cases}
   s^2U(x,s)-c^2\partial_x^2U(x,s)=0,\\
   U(0,s)=0, \quad U(L,s)=B(s).
   \end{cases}

Þetta er sama jafna og í síðasta sýnidæmi, en hér hentar best að setja
lausnina fram sem

.. math:: U(x,s)=C(s)\cosh\big((s/c)x\big)+D(s)\sinh\big((s/c)x\big).

Stuðlarnir :math:`C(s)` og :math:`D(s)` ákvarðast nú út frá
jaðarskilyrðunum, :math:`C(s)=0` og
:math:`D(s)=B(s)/\sinh\big((s/c)L\big)`. Þar með er

.. math:: U(x,s)=B(s)\dfrac{\sinh\big((s/c)x\big)}{\sinh\big((s/c)L\big)}.

Nú athugum við að

.. math::

  \begin{aligned}
   \dfrac{\sinh\big((s/c)x\big)}{\sinh\big((s/c)L\big)}&=
   \dfrac{e^{(s/c)x}-e^{-(s/c)x}}{e^{(s/c)L}\big(1-e^{-(2s/c)L}\big)}\\
   &=e^{-sL/c}\big(e^{sx/c}-e^{-sx/c}\big)
   \sum\limits_{n=0}^\infty e^{-s(2nL)/c}\\
   &=\sum\limits_{n=0}^\infty 
   \bigg(e^{-s((2n+1)L-x)/c}-e^{-s((2n+1)L+x)/c}\bigg).\end{aligned}

Þar með er

.. math::

  U(x,s)=\sum\limits_{n=0}^\infty 
   \bigg(e^{-s((2n+1)L-x)/c}-e^{-s((2n+1)L+x)/c}\bigg)B(s).

Nú segir reikniregla um Laplace-myndir okkur að
:math:`{{\cal L}}\{H(t-\alpha)b(t-\alpha)\}(s)=e^{-s\alpha}B(s)`. Við
beitum þessari reglu á sérhvern lið í summunni og fáum formúlu fyrir
lausnina

.. math::

  \begin{aligned}
   u(x,t)=\sum\limits_{n=0}^\infty \bigg(
   &H\big(t-((2n+1)L-x)/c\big)b\big(t-((2n+1)L-x)/c\big)\\
   -&H\big(t-((2n+1)L+x)/c\big)b\big(t-((2n+1)L+x)/c\big)\bigg).\end{aligned}

Það er auðvelt að túlka þess formúlu líkt og í síðasta sýnidæmi. Eins
og þar hugsum við okkur að :math:`u(x,t)` sé styrkur merkis, sem berst
eftir bilinu :math:`[0,L]` á :math:`x`-ásnum með hraðanum :math:`c`.
Styrknum er stýrt í punktinum :math:`x=L` þannig að :math:`u(L,t)=b(t)`
er gefið fall og í punktinum :math:`x=0` er því stýrt þannig að
:math:`u(0,t)=0`. Merkið er þá bylgja, sem berst fram og aftur eftir
bilinu :math:`[0,L]`. Í hvert skipti sem hún kemur að öðrum hvorum
endapunkti bilsins, þá speglast hún og kemur öfug til baka. Nú skulum
við rýna í lausnarformúluna og sjá hvernig hún breytist með tíma:

\(i) Ef :math:`0\leq t<(L-x)/c`, þá er

.. math:: u(x,t)=0.

Tíminn er of skammur til þess að merki nái að berast frá :math:`L` til
:math:`x`.

.. figure:: ./myndir/fig158.svg
    :align: center
    :alt: Tilvik (i)

    Mynd: Tilvik (i)

\(ii) Ef :math:`(L-x)/c\leq t<(L+x)/c`, þá er

.. math:: u(x,t)=b(t-\dfrac{L-x}c).

Merki hefur náð að berast frá :math:`L` til :math:`x`.

.. figure:: ./myndir/fig159.svg
    :align: center
    :alt: Tilvik (ii)

    Mynd: Tilvik (ii)

\(iii) Ef :math:`(L+x)/c\leq t<(3L-x)/c`, þá er

.. math:: u(x,t)=b(t-\dfrac{L-x}c)-b(t-\dfrac{L+x}c).

Hér hefur bæst við merki, sem borist hefur frá :math:`L` til :math:`0`,
þar sem það speglast, og þaðan til :math:`x`.

.. figure:: ./myndir/fig1510.svg
    :align: center
    :alt: Tilvik (iii)

    Mynd: Tilvik (iii)

\(iv) Ef :math:`(3L-x)/c\leq t <(3L+x)/c`, þá er

.. math:: u(x,t)=b(t-\dfrac{L-x}c)-b(t-\dfrac{L+x}c)+b(t-\dfrac{3L-x}c).

Hér hefur bæst við merki, sem borist hefur frá :math:`L` til :math:`0`,
til baka frá :math:`0` til :math:`L` og þaðan til :math:`x`. Í báðum
endapunktum hefur merkið speglast. Á þennan hátt fjölgar liðunum í
summunni með tímanum.

.. figure:: ./myndir/fig1511.svg
    :align: center
    :alt: Tilvik (iv)

    Mynd: Tilvik (iv)


.. end-toggle::

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Reiknið út Fourier-mynd lausnarinnar á símajöfnunni með
upphafsskilyrðum,

.. math::

  \begin{cases}
   {\partial}_x^2u={\alpha}{\partial}_t^2u+{\beta}{\partial}_tu+{\gamma}u,
   \\
   u(x,0)={\varphi}(x), \quad {\partial}_tu(x,0)={\psi}(x), &x\in {{\mathbb  R}},
   \end{cases}

þar sem við gefum okkur að :math:`{\varphi}` og :math:`{\psi}` séu
heildanleg föll á :math:`{{\mathbb  R}}`. Sýnið að í tilfellinu
:math:`{\varphi}=0` og :math:`{\gamma}=0` sé til lausnarformúla af
gerðinni

.. math:: u(x,t)=\int_{-\infty}^{+\infty} E(x-y,t){\psi}(y)\, dy,

án þess að reyna að reikna fallið :math:`E` út.

Dæmi
^^^^

Reiknið út Fourier-myndina af lausninni á upphafsgildisverkefninu:

.. math::

  \dfrac{{\partial}^2u}{{\partial}t^2}
   -c^2\dfrac{{\partial}^2u}{{\partial}x^2}
   +{\alpha}\dfrac{{\partial}u}{{\partial}t}+{\beta}u=f(x,t), 
   \qquad u(x,0)=\varphi(x),
   \quad {\partial}_tu(x,0)={\psi}(x).

Dæmi
^^^^

Beitið Fourier-ummyndun til þess að ákvarða formúlu fyrir
lausn verkefnisins

.. math::

  \begin{cases}
   \dfrac{\partial^2 u}{\partial x^2}+
   2\dfrac{\partial^2 u}{\partial x\partial y}+
   \dfrac{\partial^2 u}{\partial y^2}=f(x,y), &x\in {{\mathbb  R}}, \ y>0,\\
   u(x,0)=g(x), \quad \partial_yu(x,0)=h(x),
   \end{cases}

þar sem :math:`f`, :math:`g` og :math:`h` eru heildanleg föll af
:math:`x` á :math:`{{\mathbb  R}}`.

Dæmi
^^^^

Skrifið upp lausnarformúluna fyrir kúlubylgjur, með því að leysa
verkefnið 

.. math::

  \begin{cases}
   \dfrac{{\partial}^2u}{{\partial}t^2} -
   c^2\bigg(\dfrac{{\partial}^2u}{{\partial}r^2}+\dfrac
   2r\dfrac{{\partial}u}{{\partial}r}\bigg)=f(r,t), 
   &r>0, \ t>0,\\
   u(r,0)={\varphi}(r), \quad {\partial}_tu(r,0)={\psi}(r),  &r>0.
   \end{cases}

Dæmi
^^^^

Beitið speglunaraðferð og d’Alembert formúlunni til þess að reikna út
:math:`u(\frac 12, 2)`, þar sem :math:`u` er lausnin á bylgjujöfnunni

.. math::

  \begin{cases}
   \dfrac{\partial^2u}{\partial t^2}
   -\dfrac{\partial^2u}{\partial x^2}=0, &0<x<1,\ t>0,\\
   u(0,t)=0, \ {\partial}_xu(1,t)=0, &t>0,\\
   u(x,0)=4x(1-x), \ {\partial}_tu(x,0)=x, &0<x<1.
   \end{cases}

Dæmi
^^^^

Lítum á föllin :math:`u(x,t)` og :math:`v(x,t)`, sem eru lausnir

.. math::

  \begin{gathered}
   \begin{cases}
   {\partial}_t^2u-{\partial}_x^2u=0,&0<x<1, t>0,\\
   u(x,0)=\varphi(x), \ {\partial}_tu(x,0)=0, &0<x<1,\\
   u(0,t)=u(1,t)=0, &t>0,
   \end{cases}
   \\
   \begin{cases}
   {\partial}_t^2v-{\partial}_x^2v=0, & 0<x<1, t>0,\\
   v(x,0)=0, \ {\partial}_tv(x,0)={\psi}(x), & 0<x<1,\\
   {\partial}_xv(0,t)={\partial}_xv(1,t)=0, &t>0,
   \end{cases}\end{gathered}

þar sem :math:`\varphi` og :math:`{\psi}` eru :math:`2`-lotubundin föll,
:math:`\varphi` er oddstætt :math:`{\psi}` er jafnstætt og þau uppfylla
:math:`\varphi(x)={\psi}(x)=2x`, ef :math:`0\leq x\leq 1/2`, og
:math:`\varphi(x)={\psi}(x)=2-2x`, ef :math:`1/2\leq x\leq 1`. Beitið
d’Alembert formúlunni til þess að reikna út :math:`u(\frac 13,2)`,
:math:`u(\frac 45,2)`, :math:`v(\frac 12,3)` og :math:`v(\frac 74,3)`.

Dæmi
^^^^

(*Símajafnan*). Ef :math:`u` táknar straum eða spennu í rafstreng, til
dæmis símalínu, þá gefa Maxwell-jöfnurnar

.. math:: {\partial}_x^2u={\alpha}{\partial}_t^2u+{\beta}{\partial}_tu+{\gamma}u.

þar sem :math:`{\alpha}=LC`, :math:`{\beta}=(RC+LG)`,
:math:`{\gamma}=RG`, :math:`C` táknar rýmd strengsins á lengdareiningu,
:math:`G` táknar lekaleiðni á lengdareiningu, :math:`R` táknar viðnám á
lengdareiningu og :math:`L` táknar sjálfspan á lengdareiningu. Nú viljum
við ákvarða spennu í löngum streng, þar sem merki er gefið í öðrum
endapunktinum. Við hugsum okkur því að strengurinn sé óendanlega langur
og leysum því símajöfnuna á :math:`\{(x,t); x>0, t>0\}` með
hliðarskilyrðunum

.. math::

  u(x,0)={\partial}_tu(x,0)=0, \quad \lim_{x\to +{\infty}}u(x,t)=0, \quad
   u(0,t)=f(t).

\(i) Gefið ykkur að lausn sé til og reiknið út Laplace-mynd hennar með
tilliti til tíma.

\(ii) Reiknið út :math:`u` í sértilfellinu, þegar
:math:`{\beta}^2=4{\alpha}{\gamma}`. Sýnið að þá fáist einföld deyfð
bylgja, sem berst eftir :math:`x` ásnum. Ákvarðið hraða og
deyfingarstuðul bylgjunnar.
