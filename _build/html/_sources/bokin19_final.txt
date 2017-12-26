
Varmaleiðnijafnan
=================

Hitakjarninn
------------

Hitakjarninn
~~~~~~~~~~~~

Í þessum kafla ætlum við að fjalla um úrlausn á varmaleiðnijöfnunni á
öllu rúminu. Við skulum byrja á því að leiða út formúlu fyrir lausn á
einvíðu varmaleiðnijöfnunni með upphafsskilyrðum

.. math::

  \begin{cases}
   \dfrac{{\partial}u}{\partial t}
   -{\kappa}\dfrac{\partial^2u}{\partial x^2}=0, &x\in {{\mathbb  R}}, \ t>0,\\
   u(x,0)={\varphi}(x), &x\in {{\mathbb  R}},
   \end{cases}

og beita Fourier-ummyndun til þess. Við gerum ráð fyrir að :math:`u` sé
heildanlegt fall af :math:`x` fyrir fast :math:`t`, að :math:`{\varphi}`
sé heildanlegt og látum :math:`\widehat u({\xi},t)` og :math:`\widehat {\varphi}({\xi})` vera Fourier-myndir :math:`u(x,t)` og
:math:`{\varphi}(x)` með tilliti til :math:`x`. Við gefum okkur einnig
að

.. math::

  {{\cal F}}\{{\partial}_tu\}({\xi},t)=
   \int_{-\infty}^{+\infty}e^{-ix{\xi}}{\partial}_tu(x,t)\, dx
   =\partial_t \int_{-\infty}^{+\infty}e^{-ix{\xi}}u(x,t)\, dx
   ={\partial}_t\widehat u({\xi},t).

Samkvæmt setningu 6.2.3 (ix) er

.. math::

  {{\cal F}}\{{\partial}_x^2u\}({\xi},t)=
   \int_{-\infty}^{+\infty}e^{-ix{\xi}}{\partial}_x^2u(x,t)\, dx
   =(i{\xi})^2\widehat u({\xi},t)= -{\xi}^2\widehat u({\xi},t).

Við tökum nú Fourier-mynd af öllum liðunum í (:ref:`Link title <16.1.1>`) og fáum að
:math:`\widehat u` verður að uppfylla

.. math::

  \begin{cases}
   \partial_t\widehat u({\xi},t)
   +{\kappa}{\xi}^2\widehat u({\xi},t)=0, &{\xi}\in {{\mathbb  R}}, \ t>0,\\
   \widehat u({\xi},0)=\widehat {\varphi}({\xi}), &{\xi}\in {{\mathbb  R}}.
   \end{cases}

Þetta er fyrsta stigs afleiðujafna í :math:`t`, þar sem virkinn er
:math:`D_t+{\kappa}{\xi}^2`. Lausnin er því ótvírætt ákvörðuð

.. math:: \widehat u({\xi},t)=e^{-{\kappa}t{\xi}^2}\widehat {\varphi}({\xi}).

Í sýnidæmi 6.2.2 sáum við að :math:`{{\cal F}}\{e^{-x^2}\}({\xi})= \sqrt {\pi}e^{-{\xi}^2/4}`. Samkvæmt setningu 6.2.3 (iv) er

.. math::

  \begin{aligned}
   \sqrt{\dfrac a \pi} {{\cal F}}\{e^{-ax^2}\}({\xi})
   &=\sqrt{\dfrac a\pi} {{\cal F}}\{e^{-(\sqrt a x)^2}\}({\xi})\\
   &=e^{-({\xi}/\sqrt a)^2/4}=e^{-{\xi}^2/4a}.\end{aligned}

Ef við veljum :math:`a=1/4{\kappa}t` í þessari formúlu, þá sjáum við að
:math:`e^{-{\kappa}t{\xi}^2}` er Fourier-myndin af fallinu :math:`E` sem
gefið er með formúlunni

.. math::

  E(x,t)=E_t(x)=\begin{cases} \dfrac 1{\sqrt{4{\pi}{\kappa}t}}e^{-x^2/4{\kappa}t},
   &x\in {{\mathbb  R}}, \ t>0,\\
   0, &x\in {{\mathbb  R}}, \ t\leq 0.\end{cases}

Skilgreining
^^^^^^^^^^^^

Fallið :math:`E` nefnist *hitakjarni* eða *varmaleiðnikjarni*.

--------------

.. figure:: ./myndir/fig161.svg
    :align: center
    :alt: Varmaleiðnikjarninn.

    Mynd: Varmaleiðnikjarninn.

Formúlan (:ref:`Link title <16.1.3>`) segir okkur nú að
:math:`\widehat u({\xi},t)= \widehat E_t({\xi})\widehat \varphi({\xi})`, og því gefur andhverfuformúla
Fouriers og földunarreglan okkur að

.. math::

  u(x,t)=E_t\ast {\varphi}(x)=\int_{-{\infty}}^{+{\infty}}
    \dfrac 1{\sqrt{4{\pi}{\kappa}t}}e^{-(x-y)^2/4{\kappa}t}{\varphi}(y)\,
   dy, \qquad t>0.

Áður en lengra er haldið skulum við rannsaka nokkra eiginleika
hitakjarnans. Athugum fyrst að

.. math::

  \lim\limits_{t\to 0+} E_t(x) =
   \begin{cases} +{\infty}, &x=0,\\
   0, &x\neq 0,\end{cases}

og

.. math::

  \int_{-{\infty}}^{+{\infty}} E_t(x)\, dx=
   \int_{-{\infty}}^{+{\infty}}
   \dfrac 1{\sqrt{4{\pi}{\kappa}t}}e^{-x^2/4{\kappa}t}\, dx
   =\int_{-{\infty}}^{+{\infty}}
   \dfrac 1{\sqrt{\pi}}e^{-y^2}\, dy = 1.

Af (:ref:`Link title <16.1.6>`) leiðir síðan að fyrir samfelld takmörkuð föll
:math:`{\varphi}` gildir

.. math::

  \begin{aligned}
   \lim\limits_{t\to 0+} E_t\ast {\varphi}(x) 
   &=\lim\limits_{t\to 0+} 
   \int_{-{\infty}}^{+{\infty}}
   \dfrac 1{\sqrt{4{\pi}{\kappa}t}}e^{-(x-y)^2/4{\kappa}t}{\varphi}(y)\, dy
   \\
   &=\lim\limits_{t\to 0+} 
   \int_{-{\infty}}^{+{\infty}}
   \dfrac 1{\sqrt{\pi}}e^{-y^2}{\varphi}(x-\sqrt{4{\kappa}t}y)\, dy\\
   &=\int_{-{\infty}}^{+{\infty}}
   \dfrac 1{\sqrt{\pi}}e^{-y^2}\lim\limits_{t\to 0+}
   {\varphi}(x-\sqrt{4{\kappa}t}y)\, dy\\
   &={\varphi}(x)\int_{-{\infty}}^{+{\infty}}
   \dfrac 1{\sqrt{\pi}}e^{-y^2}\, dy ={\varphi}(x).\end{aligned}

Þessi formúla segir okkur að :math:`E_t` stefni á :math:`\delta_0` í
veikum skilningi ef :math:`t\to 0+`. Það er auðveldur reikningur að
sannfæra sig um að :math:`E` uppfylli varmaleiðnijöfnuna

.. math:: ({\partial}_t-{\kappa}{\partial}_x^2)E(x,t)=0, \qquad t>0,

því

.. math::

  \begin{aligned}
   {\partial}_tE(x,t)&=-\dfrac
   1{2t}E(x,t)+\dfrac{x^2}{4{\kappa}t^2}E(x,t),\\
   {\partial}_xE(x,t)&=
   -\dfrac x{2{\kappa}t}E(x,t),\\
   {\partial}_x^2E(x,t)&=
   -\dfrac 1{2{\kappa}t}E(x,t)-\dfrac x{2{\kappa}t}{\partial}_xE(x,t),\\
   &= -\dfrac 1{2{\kappa}t}E(x,t)+\dfrac {x^2}{4{\kappa}^2t^2}E(x,t).\end{aligned}

Af (:ref:`Link title <16.1.9>`) leiðir nú að fallið :math:`u` sem gefið er með
(:ref:`Link title <16.1.5>`) er lausn á varmaleiðnijöfnunni, því

.. math::

  ({\partial}_t-{\kappa}{\partial}_x^2)u(x,t)
   =\int_{-{\infty}}^{+{\infty}}
   ({\partial}_t-{\kappa}{\partial}_x^2)E(x-y,t) {\varphi}(y)\, dy=0.

Hér þarf lesandinn aðeins að staldra við og sannfæra sig um að setning
Lebesgues í viðauka C gefi að það megi taka afleiður með tilliti til
:math:`x` og :math:`t` undir földunarheildið. Niðurstaða þessara
útreikninga okkar er:

Setning
^^^^^^^

Upphafsgildisverkefnið

.. math::

  \begin{cases}
   \dfrac{{\partial}u}{\partial t}
   -{\kappa}\dfrac{\partial^2u}{\partial x^2}=0, &x\in {{\mathbb  R}}, \ t>0,\\
   u(x,0)=\lim_{t\to 0+}u(x,t)={\varphi}(x), &x\in {{\mathbb  R}},
   \end{cases}

þar sem :math:`\varphi` er gefið samfellt og takmarkað fall á
:math:`{{\mathbb  R}}`, hefur lausn :math:`u` sem gefin er með
formúlunni

.. math::

  u(x,t)=E_t\ast \varphi(x)=\int_{-\infty}^{+\infty}E_t(x-\xi)\varphi(\xi)\,
   d\xi, \qquad x\in {{\mathbb  R}}, \ t>0,

þar sem hitakjarninn er gefinn með formúlunni

.. math::

  E(x,t)=E_t(x)=H(t) \dfrac
   1{\sqrt{4{\pi}{\kappa}t}}e^{-x^2/4{\kappa}t},
   \qquad (x,t)\neq (0,0).

Hliðraða varmaleiðnijafnan
--------------------------

Hliðraða varmaleiðnijafnan
~~~~~~~~~~~~~~~~~~~~~~~~~~

Þá snúum við okkur að hliðruðu varmaleiðnijöfnunni og leysum hana með
óhliðruðu upphafsskilyrði

.. math::

  \begin{cases}
   \dfrac{{\partial}u}{\partial t}
   -{\kappa}\dfrac{\partial^2u}{\partial x^2}=f(x,t), &x\in {{\mathbb  R}}, \ t>0,\\
   u(x,0)=0, &x\in {{\mathbb  R}}.
   \end{cases}

Með því að beita Fourier-ummyndun eins og áður, þá fáum við verkefnið

.. math::

  \begin{cases}
   \partial_t\widehat u({\xi},t)
   +{\kappa}{\xi}^2\widehat u({\xi},t)=\widehat f({\xi},t), &{\xi}\in {{\mathbb  R}}, \ t>0,\\
   \widehat u({\xi},0)=0, &{\xi}\in {{\mathbb  R}}.
   \end{cases}

Þetta er fyrsta stigs hliðruð afleiðujafna í :math:`t` með óhliðruð
upphafsskilyrði. Virkinn er :math:`D_t+\kappa\xi^2` og Green-fall hans
er :math:`G_\xi(t,\tau)=e^{-\kappa(t-\tau)\xi^2}=\widehat E_{t-\tau}(\xi)`. Lausnin er því

.. math::

  \widehat u({\xi},t)=\int_0^te^{-{\kappa}(t-{\tau})x^2}\widehat
   f({\xi},t)\, d{\tau} = \int_0^t\widehat E_{t-{\tau}}({\xi})\widehat
   f({\xi},t)\, d{\tau}.

Nú beitum við andhverfuformúlu Fouriers og földunarreglunni og fáum

.. math::

  \begin{aligned}
   u(x,t)&=\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \bigg(\int_0^t\widehat E_{t-{\tau}}({\xi})\widehat
   f({\xi},{\tau})\, d{\tau} \bigg)\, d{\xi}\\
   &=\int_0^t\bigg(
   \dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
   \widehat E_{t-{\tau}}({\xi})\widehat
   f({\xi},{\tau})\, d{\xi}\bigg)\, d{\tau}\\
   &=\int_0^t \int_{-\infty}^{+\infty}
   E_{t-{\tau}}(x-y)f(y,{\tau})\, dy d{\tau}\\
   &=\int_0^t \int_{-\infty}^{+\infty}
   E(x-y,t-\tau)f(y,{\tau})\, dy d{\tau}.\end{aligned}

Ef við framlengjum skilgreiningarsvæði fallsins :math:`f` þannig að
:math:`f(x,t)=0` ef :math:`t\leq 0`, þá sjáum við að

.. math:: u(x,t)=E\ast f(x,t), \qquad t>0.

Við skulum nú taka saman útreikninga okkar:

Setning
^^^^^^^

Látum :math:`f` vera samfellt fall á opna efra hálfplaninu
:math:`\{(x,t); t>0\}`, sem er takmarkað á lokuninni
:math:`\{(x,t); t\geq 0\}` og tekur gildið :math:`0` á neðra hálfplaninu
:math:`\{(x,t); t<0\}` og látum :math:`{\varphi}` vera samfellt
takmarkað fall á :math:`{{\mathbb  R}}`. Þá hefur upphafsgildisverkefnið

.. math::

  \begin{cases}
   \dfrac{{\partial}u}{\partial t}
   -{\kappa}\dfrac{\partial^2u}{\partial x^2}=f(x,t), &x\in {{\mathbb  R}}, \ t>0,\\
   u(x,0)=\lim\limits_{t\to 0+}u(x,t)={\varphi}(x), &x\in {{\mathbb  R}},
   \end{cases}

ótvírætt ákvarðaða lausn :math:`u`, sem gefin er með formúlunni

.. math:: u(x,t)=E_t\ast {\varphi}(x)+E\ast f(x,t), \qquad x\in {{\mathbb  R}},\ t>0,

þar sem :math:`E` táknar hitakjarnann, sem skilgreindur er með
formúlunni (:ref:`Link title <16.1.13>`).

--------------

Það er einfalt að alhæfa þetta verkefni fyrir varmaleiðnijöfnuna í hvaða
rúmvídd sem er,

.. math::

  \begin{cases}
   \dfrac{{\partial}u}{\partial t}
   -{\kappa}\Delta u=f(x,t), &x\in {{\mathbb  R}}^n, \ t>0,\\
   u(x,0)=\lim\limits_{t\to 0+}u(x,t)={\varphi}(x), &x\in {{\mathbb  R}}^n,
   \end{cases}

þar sem :math:`f` er samfellt fall á
:math:`\{(x,t)\in {{\mathbb  R}}^n\times {{\mathbb  R}}; t\geq 0\}`,
:math:`{\varphi}` er samfellt fall á :math:`{{\mathbb  R}}^n` og bæði
:math:`f` og :math:`{\varphi}` eru takmörkuð. Hitakjarninn verður

.. math::

  E(x,t)=E_t(x)=H(t) \dfrac
   1{\big(4{\pi}{\kappa}t\big)^{n/2}}e^{-x^2/4{\kappa}t},
   \qquad x\in {{\mathbb  R}}^n,\ (x,t)\neq (0,0),

og lausnarformúlan alhæfist í

.. math:: u(x,t)=E_t\ast {\varphi}(x)+E\ast f(x,t), \qquad x\in {{\mathbb  R}}^n, t>0.

Við eftirlátum lesandanum að staðfesta að (:ref:`Link title <16.2.8>`) gefi lausn á
(:ref:`Link title <16.2.6>`).

Úrlausn á varmaleiðnijöfnum með Laplace-ummyndun
------------------------------------------------

Úrlausn á varmaleiðnijöfnum með Laplace-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum áður séð hvernig hægt er að beita Laplace-ummyndun til þess að
leysa bylgjujöfnuna með óhliðruðum upphafsskilyrðum og hliðruðum
jaðarskilyrðum á hálfás. Við byrjum á hliðstæðu verkefni fyrir
varmaleiðnijöfnuna:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Varmaleiðni á hálflínu

Nú tökum við varmaleiðnijöfnuna á hálflínu fyrir og leysum hana með
óhliðruðum upphafsskilyrðum og hliðruðu jaðarskilyrði,

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial t}-\kappa
   \dfrac{\partial^2 u}{\partial x^2}=0, &x>0, \ t>0,\\
   u(x,0)=0, &x>0,\\
   u(0,t)=f(t), &t>0,\\
   \lim\limits_{x\to +\infty}u(x,t)=0, & t>0.
   \end{cases}

Við látum :math:`U(x,s)` og :math:`F(s)` tákna Laplace-myndir
:math:`u(x,t)` og :math:`f(t)` með tilliti til :math:`t` eins og áður.
Við fáum þá verkefnið

.. math::

  \begin{cases}
   sU(x,s)-\kappa\partial_x^2U(x,s)=0,\\
   U(0,s)=F(s),\\
   \lim\limits_{x\to +\infty}U(x,s)=0.
   \end{cases}

Almenn lausn þessarar jöfnu er

.. math:: U(x,s)=A(s)e^{-\sqrt{s/\kappa}\, x}+B(s)e^{\sqrt{s/\kappa}\, x}.

Síðara jaðarskilyrðið gefur :math:`B(s)=0` og hið fyrra að
:math:`A(s)=F(s)`. Þar með er

.. math:: U(x,s)=e^{-\sqrt{s/\kappa}\, x}F(s).

Ef við getum fundið fall :math:`g(x,t)`, þannig að

.. math:: {{\cal L}}\{g\}(x,s)=e^{-\sqrt{s/\kappa}\, x},

þá gefur földunarreglan í setningu :ref:`Link title <set7.4.1>` okkur að

.. math:: u(x,t)=\int_0^tg(x,t-\tau)f(\tau)\, d\tau.

Í næsta sýnidæmi sýnum við fram á að

.. math::

  g(x,t)=\dfrac xtE(x,t)= \dfrac x{\sqrt{4\pi\kappa}\, t^{\frac 32}}
   e^{-x^2/4\kappa t},

þar sem :math:`E(x,t)` táknar varmaleiðnikjarnann. Svarið er því

.. math::

  u(x,t)=\dfrac x{\sqrt{4\pi\kappa}}\int_0^t
   (t-\tau)^{-\frac 32}e^{-x^2/4\kappa(t-\tau)} f({\tau})\, d\tau, 
   \qquad x>0, \ t>0.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Laplace-mynd varmaleiðnikjarnans

Við höfum

.. math::

  {{\cal L}}\{E\}(x,s)=\int_0^{+\infty}e^{-st}
   \dfrac{e^{-x^2/4\kappa t}}{\sqrt{4\pi\kappa t}}\, dt=
   \dfrac{1}{\sqrt{4\kappa s}}e^{-\sqrt{s/\kappa}\, x}.

Til þess að staðfesta þessa formúlu þá nefnum við fyrst að í grein 16.1
sýndum við fram á að :math:`E` uppfyllir

.. math::

  \begin{cases}
   \dfrac{\partial E}{\partial t}-\kappa
   \dfrac{\partial^2 E}{\partial^2 x}=0, &x>0, \ t>0,\\
   E(x,0)=0, &x>0,\\
   E(0,t)=\dfrac 1{\sqrt{4\pi\kappa t}}, &t>0,\\
   \lim\limits_{x\to +{\infty}}E(x,t)=0, &t>0.
   \end{cases}

Þetta er sértilfelli af (:ref:`Link title <16.3.1>`). Samkvæmt sýnidæmi 6.1.3 og
formúlu (3.7.6) er

.. math::

  {{\cal L}}\{E\}(0,s)=\dfrac 1{\sqrt{4\pi\kappa}}{{\cal L}}\{t^{-\frac 12}\}(s)=
   \dfrac {\Gamma(-\frac 12+1)}{\sqrt{4\pi\kappa}s^{-\frac 12+1}}=
   \dfrac {\sqrt\pi}{\sqrt{4\pi\kappa s}}=
   \dfrac {1}{\sqrt{4\kappa s}}.

Með nákvæmlega sömu röksemdafærslu og í síðasta sýnidæmi fáum við því

.. math:: {{\cal L}}\{E\}(x,s)=\dfrac {1}{\sqrt{4\kappa s}}e^{-\sqrt{s/\kappa}x}.

Nú er auðvelt að staðfesta lausnarformúluna í síðasta sýnidæmi, því

.. math::

  -2\kappa\partial_xE(x,t)=-2\kappa
   \big(-2x/4\kappa t  \big)E(x,t)=\dfrac xt E(x,t)

og

.. math::

  {{\cal L}}\{-2\kappa\partial_xE\}(x,s)
   =-2\kappa\partial_x{{\cal L}}\{E\}(x,s)
   =-2\kappa\dfrac{\partial}{\partial x}\bigg(
   \dfrac {1}{\sqrt{4\kappa s}}e^{-\sqrt{s/\kappa}\, x} \bigg)
   =e^{-\sqrt{s/\kappa}\, x}.

.. end-toggle::

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Beitið Fourier-ummyndun til þess að reikna út lausn á
upphafsgildisverkefninu:

.. math::

  \dfrac{{\partial}u}{{\partial}t}
   -{\kappa}\dfrac{{\partial}^2u}{{\partial}x^2}
   +r\dfrac{{\partial}u}{{\partial}x}=f(x,t), \qquad u(x,0)=\varphi(x).

Dæmi
^^^^

Beitið Fourier-ummyndun til þess að reikna út lausn á
upphafsgildisverkefninu:

.. math::

  \dfrac{{\partial}u}{{\partial}t}
   -{\kappa}\dfrac{{\partial}^2u}{{\partial}x^2} +au=f(x,t), 
   \qquad u(x,0)=\varphi(x).

Dæmi
^^^^

Beitið speglunaraðferð til þess að finna formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases} {\partial}_tu-{\kappa}{\partial}_x^2u=0, &x>0, \ t>0, \\
   u(x,0)=\varphi(x), &x>0,\\
   u(0,t)=0, &t>0,
   \end{cases}

þar sem :math:`\varphi` er takmarkað fall á :math:`{{\mathbb  R}}` og
sýnið fram á að hægt sé að skrifa hana sem

.. math:: u(x,t)=\int_{0}^{+{\infty}}(E_t(x-y)-E_t(x+y))\varphi(y)\, dy,

þar sem :math:`E_t` táknar hitakjarnann. Finnið einnig formúlu fyrir
lausn verkefnisins, þar sem jaðarskilyrðinu :math:`u(0,t)=0` er breytt í
:math:`{\partial}_xu(0,t)=0` og sýnið hvernig þetta heildi breytist.

Dæmi
^^^^

Beitið speglunaraðferð til þess að finna formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases} {\partial}_tu-{\kappa}{\partial}_x^2u=f(x,t), &x>0, \ t>0, \\
   u(x,0)=0, &x>0,\\
   u(0,t)=0, &t>0,
   \end{cases}

þar sem :math:`f` er takmarkað samfellt fall á
:math:`{{\mathbb  R}}\times {{\mathbb  R}}_+`.

Dæmi
^^^^

Finnið formúlu fyrir lausnina á verkefninu

.. math::

  \begin{cases} {\partial}_tu-{\kappa}{\partial}_x^2u=0, &x>0, \ t>0, \\
   u(x,0)=0, &x>0,\\
   u(0,t)=h(t), &t>0,
   \end{cases}

þar sem :math:`h` er samfellt deildanlegt á jákvæða raunásnum.

[*Leiðbeining:* Setjið :math:`v(x,t)=u(x,t)-h(t)` og sýnið að :math:`v`
sé lausn á hliðruðu varmaleiðnijöfnunni með hliðruðu upphafsskilyrði.]

Dæmi
^^^^

Beitið speglunaraðferð til þess að finna formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases} {\partial}_tu-{\kappa}{\partial}_x^2u=f(x,t), &x>0, \ t>0, \\
   u(x,0)=0, &x>0,\\
   \partial_xu(0,t)=0, &t>0,
   \end{cases}

þar sem :math:`f` er takmarkað samfellt fall á
:math:`{{\mathbb  R}}\times {{\mathbb  R}}_+`.

Dæmi
^^^^

Finnið formúlu fyrir lausnina á verkefninu

.. math::

  \begin{cases} {\partial}_tu-{\kappa}{\partial}_x^2u=0, &x>0, \ t>0, \\
   u(x,0)=0, &x>0,\\
   {\partial}_xu(0,t)=h(t), &t>0,
   \end{cases}

þar sem :math:`h` er samfellt deildanlegt á jákvæða raunásnum.

[*Leiðbeining:* Setjið :math:`v(x,t)=u(x,t)-xh(t)` og sýnið að :math:`v`
sé lausn á hliðruðu varmaleiðnijöfnunni með hliðruðu upphafsskilyrði.]

Dæmi
^^^^

Takið saman niðurstöður dæmanna 3-7 og skrifið upp lausnarformúlur fyrir
lausnir verkefnanna

.. math::

  \begin{cases} {\partial}_tu-{\kappa}{\partial}_x^2u=f(x,t), &x>0, \ t>0, \\
   u(x,0)=\varphi(x), &x>0,\\
   u(0,t)=h(t), &t>0,
   \end{cases}
   \begin{cases} {\partial}_tu-{\kappa}{\partial}_x^2u=f(x,t), &x>0, \ t>0, \\
   u(x,0)=\varphi(x), &x>0,\\
   {\partial}_xu(0,t)=h(t), &t>0,
   \end{cases}

með sömu forsendum og áður um föllin :math:`f`, :math:`\varphi` og
:math:`h`.

Dæmi
^^^^

Leysið verkefnið

.. math::

  {\partial}_tu-{\kappa}{\partial}_x^2u=0, \qquad
   u(x,0)=0, \quad u(0,t)=f(t), \qquad x>0, \ t>0.

Dæmi
^^^^

Notið niðurstöðuna úr sýnidæmi 16.3.1 til þess að sýna að

.. math::

  {{\cal L}}\{
   {{\operatorname{erfc}}}\big({\alpha}/(2\sqrt t)\big)\}(s) =
   \dfrac 1s e^{-{\alpha}\sqrt s},

þar sem :math:`{{\operatorname{erfc}}}=1-{{\operatorname{erf}}}` og
:math:`{{\operatorname{erf}}}` táknar skekkjufallið,

.. math:: {{\operatorname{erf}}}(x)=\dfrac 2{\sqrt {\pi}} \int_0^x e^{-{\xi}^2}\, d{\xi}.

Dæmi
^^^^

Varmaleiðni í stöng af lengd :math:`L`, með upphafshitastig :math:`0`,
annan endann við hitastig :math:`0` og hinn við :math:`f(t)` er lausn á
verkefninu

.. math::

  {\partial}_tu-{\kappa}{\partial}_x^2u=0, \qquad
   u(x,0)=0, \quad u(0,t)=0, \quad u(L,t)=f(t), \qquad x>0, \ t>0.

\(i) Sýnið að Laplace-mynd lausnarinnar :math:`u` með tilliti til
:math:`t` sé

.. math::

  U(x,s)=F(s)\dfrac{\sinh\big(x\sqrt{s/{\kappa}}\big)}
   {\sinh\big(L\sqrt{s/{\kappa}}\big)},

þar sem :math:`F` er Laplace-mynd :math:`f`.

\(ii) Látum :math:`v(x,t)` tákna lausn í sértifellinu þegar :math:`f` er
fastafallið :math:`1`. Sannið formúlu Duhamels,

.. math::

  u(x,t)=\dfrac{\partial}{\partial t}\bigg(
   \int_0^t v(x,t-{\tau})f({\tau})\, d{\tau}
   \bigg).

\(iii) Notið niðurstöðuna úr dæmi 2 og sömu tækni og í sýnidæmi 15.8.2
til þess að sýna að

.. math::

  v(x,t)=\sum\limits_{n=0}^{\infty}
   \bigg( {{\operatorname{erf}}}\bigg(\dfrac{(2n+1)L+x}{\sqrt{4{\kappa} t}}\bigg)-
   {{\operatorname{erf}}}\bigg(\dfrac{(2n+1)L-x}{\sqrt{4{\kappa} t}}\bigg)
    \bigg).


