
Mismunaaðferðir
===============

Inngangur
---------

Nú snúum við okkur að tölulegum aðferðum til þess að nálga lausnir á
upphafs- og jaðargildisverkefnum fyrir venjulegar afleiðujöfnur og
hlutafleiðujöfnur, en fram til þessa höfum við einungis fengist við
fræðilegar lausnir. Það er undantekning frekar en regla að hægt sé að
finna lausnarformúlu fyrir verkefnin, þannig að við þurfum að geta
fundið nálganir á lausnum. Það er sjálfsagt að reyna að hafa aðferðirnar
eins almennar og kostur er. Í þessum kafla fjöllum við um
:hover:`mismunaaðferðir, mismunaaðferð` og í næsta kafla
fjöllum við um :hover:`bútaaðferðir, bútaaðferð`.

Mismunaaðferðirnar hafa marga góða þann kosti og einkum þann að auðvelt
er að útfæra þær. Þær hafa hins vegar þann ókost að snúið er að útfæra
þær fyrir hlutafleiðujöfnur á öðrum svæðum en rétthyrningum.
Bútaaðferðirnar eru aftur á móti flóknari í útfærslu, en hafa þann kost
að hægt er að útfærða þær á alls kyns svæðum í planinu.

Við lítum fyrst á jaðargildisverkefni fyrir almenna annars stigs
afleiðujöfnu á bili :math:`[a,b]` með raungildum stuðlum
:math:`a_0,a_1,a_2\in C[a,b]`,

.. math::

  \begin{cases}
       Lu=a_2u''+a_1u'+a_0u=f,& \text{ á } ]a,b[\\
   B_1u=\alpha_1u(a)-\beta_1u'(a)=\gamma_1,&(\alpha_1,\beta_1)\neq (0,0),\\
   B_2u=\alpha_2u(b)+\beta_2u'(b)=\gamma_2,&(\alpha_2,\beta_2)\neq (0,0).
     \end{cases}

og raungildri hægri hlið :math:`f`. Við munum eftir því að
tilvistarsetningarnar fyrir annars stigs jöfnur gerðu ráð fyrir því að
:math:`a_2` hefði enga núllstöð á bilinu og þess vegna er engin
takmörkun að gera ráð fyrir að :math:`a_2(x)<0` í öllum punktum
:math:`x\in [a,b]`.

Í kafla 14 umrituðum við virkjann yfir á Sturm-Liouville form,

.. math:: Lu=\varrho^{-1}\big(-(pu')'+qu\big)=f,

með

.. math::

  p=\exp\big(\int a_1(x)/a_2(x)\, dx+C\big),
   \quad q=-a_0p/a_2 \ \text { og  } \ \varrho=-p/a_2.

Afleiðujafnan :math:`Lu=f` jafngildir því :math:`-(pu')'+qu=\varrho f`.
Með því að skipta út :math:`\varrho f` fyrir :math:`f` í þessari jöfnu,
þá sjáum við að það er engin takmörkun að gera ráð fyrir að
:math:`\varrho=1` og því ætlum við að takmarka okkur við verkefnið

.. math::

  \begin{cases}
       Lu=-(pu')'+qu=-pu''-p'u'+qu=f,& \text{ á } ]a,b[\\
   B_1u=\alpha_1u(a)-\beta_1u'(a)=\gamma_1,&(\alpha_1,\beta_1)\neq (0,0),\\
   B_2u=\alpha_2u(b)+\beta_2u'(b)=\gamma_2,&(\alpha_2,\beta_2)\neq (0,0),
     \end{cases}

þar sem við gerum ráð fyrir að :math:`p\in C^1[a,b]`, :math:`p(x)>0`,
:math:`q\in C[a,b]` og :math:`q(x)\in {{\mathbb  R}}` fyrir öll
:math:`x\in [a,b]`.

Kosturinn við þessa framsetningu er að aðferðirnar alhæfast yfir á
jaðargildisverkefni fyrir hlutafleiðujöfnur af gerðinni

.. math::

  \begin{cases}
       Lu=-\nabla\cdot (p\nabla u)+qu=
   -p\nabla^2u-\nabla p\cdot \nabla u+qu=f, \qquad \text{ á } D\\
   \alpha u+\beta\dfrac{\partial u}{\partial n}
   =\gamma, \qquad  \text{á } \ \partial D,
     \end{cases}

þar sem :math:`D` svæði í planinu :math:`{{\mathbb  R}}^2`,
:math:`\partial D` táknar jaðar þess, :math:`p\in C^1(D)`,
:math:`q,f\in C(D)` eru gefin föll á :math:`D` og :math:`\alpha`,
:math:`\beta` og :math:`\gamma` eru gefin föll á jaðrinum.

Við gerum ráð fyrir að í sérhverjum punkti :math:`(x,y)` á
:math:`\partial D` sé :math:`(\alpha(x,y),\beta(x,y))\neq (0,0)`.

Athugið að í öllum punktum :math:`(x,y)` á :math:`\partial D` þar sem
:math:`\beta(x,y)=0` er gildi lausnarinnar gefið,
:math:`u(x,y)=\gamma(x,y)/\alpha(x,y)`. Munið að
:math:`\partial u/\partial n=\nabla u\cdot {\mathbf n}` og
:math:`\mathbf n` táknar ytri þvervigurinn á jaðarinn. Ef svæðið hefur
horn, þá er ytri þvervigurinn ekki vel skilgreindur þar, svo við verðum
að túlka jaðargildin þannig að jafnan gildi í öllum punktum þar sem
:math:`\beta` er núll og í öllum punktum þar sem þvervigurinn er til.

Eðlilega er miklu flóknara að fást við nálganir á hlutafleiðujöfnum á
almennum svæðum miðað við nálganir á venjulegum afleiðujöfnum á bili, en
aðferðirnar sem við fáumst við hér eins hugsaðar og bera sömu nöfn,
mismunaaðferðir.

Mismunaaðferð fyrir venjulegar afleiðujöfnur
--------------------------------------------

Mismunaaðferðir eru til í mörgum afbrigðum og við skulum lýsa
einfaldasta afbrigðinu í fyrstu umferð. Við byrjum á því að velja okkur
skiptingu

.. math:: a=x_0<x_1<x_2<\cdots <x_N=b

á bilinu :math:`[a,b]`. Einfaldast er að taka jafna skiptingu. Látum
:math:`h=(b-a)/N` tákna lengd hlutbilanna. Þá er :math:`x_j=a+jh`,
:math:`j=0,\dots,N`, og þar með :math:`x_{j-1}=x_j-h` og
:math:`x_{j+1}=x_j+h`.

Í punktunum :math:`x_j` uppfyllir lausnin :math:`u` á (:ref:`Link title <eq:21.1.0>`)
jöfnurnar

.. math::

  \begin{cases}
   \alpha_1u(x_0)-\beta_1u'(x_0)=\gamma_1,\\
   a_2(x_j)u''(x_j)+a_1(x_j)u'(x_j)+a_0(x_j)u(x_j)=f(x_j), \qquad
   j=1,\dots,N-1,\\
   \alpha_2u(x_N)+\beta_2u'(x_N)=\gamma_2.
   \end{cases}

Til einföldunar skrifum við :math:`u_j=u(x_j)` og :math:`f_j=f(x_j)`.
Við ætlum nú að setja fram :math:`(N+1)\times (N+1)` línulegt
jöfnuhneppi :math:`A {\mathbf c}={\mathbf b}` fyrir nálgunargildi þar
sem hnit lausnarinnar :math:`\mathbf c` eru nálgunargildi
:math:`c_j\approx u_j`. Hugmyndin er nú að skipta út gildunum á
afleiðunum :math:`u'(x_j)` og :math:`u''(x_j)` fyrir mismunakvóta í
þessum jöfnum, stinga síðan :math:`c_j` inn í mismunakvótana og setja
fram línulegt jöfnuhneppi sem nálgunargildin eiga að uppfylla.

Mismunajafna í vinstri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í endapunktinum :math:`a=x_0` notum við nálgum við afleiðu með
mismunakvóta

.. math:: u'(x)\approx \dfrac{u(x+h)-u(x)}h,

skiptum á afleiðunni og mismunakvótanum í fyrstu jöfnu
(:ref:`Link title <eq:21.1.00>`)

.. math:: \alpha_1u_0-\beta_1\dfrac{u_1-u_0}h\approx \gamma_1

og stingum að lokum inn :math:`c_0` og :math:`c_1` inn í hana í stað
:math:`u_0` og :math:`u_1` til þess að fá mismunajöfnu

.. math:: \alpha_1c_0-\beta_1\dfrac{c_1-c_0}h= \gamma_1.

Mismunajafna í innri punktum bilsins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í innri punktum bilsins :math:`x_j`, :math:`j=1,\dots,N-1`, nálgum við
afleiður með miðsettum mismunakvótum

.. math::

  u'(x)\approx \dfrac{u(x+h)-u(x-h)}{2h} \qquad \text{ og } \qquad 
   u''(x)\approx \dfrac{u(x-h)-2u(x)+u(x+h)}{h^2},

skiptum á afleiðum og mismunakvótum í miðjöfnu (:ref:`Link title <eq:21.1.00>`)

.. math::

  a_2(x_j)\dfrac{u_{j-1}-2u_j+u_{j+1}}{h^2}+a_1(x_j)
   \dfrac{u_{j+1}-u_{j-1}}{2h}+a_0(x_j)u_j\approx f_j,

og stingum inn :math:`c_{j-1}`, :math:`c_j` og :math:`c_{j+1}` fyrir
:math:`u_{j-1}`, :math:`u_j` og :math:`u_{j+1}` til þess að fá jöfnur
fyrir nálgunargildin

.. math::

  a_2(x_j)\dfrac{c_{j-1}-2c_j+c_{j+1}}{h^2}+a_1(x_j)
   \dfrac{c_{j+1}-c_{j-1}}{2h}+a_0(x_j)c_j=f_j.

Mismunajafna í hægri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í hægri endapunktinum :math:`b=x_N` notum við nálgunarformúluna

.. math:: u'(x)\approx \dfrac{u(x)-u(x-h)}h,

skiptum á afleiðu og mismunakvóta í síðustu jöfnu (:ref:`Link title <eq:21.1.00>`)

.. math:: \alpha_2u_N+\beta_2\dfrac{u_N-u_{N-1}}h\approx \gamma_2

og stingum síðan inn :math:`c_{N-1}` og :math:`c_N` fyrir
:math:`u_{N-1}` og :math:`u_N` til þess að fá nálgunarjöfnuna

.. math:: \alpha_2c_N+\beta_2\dfrac{c_N-c_{N-1}}h = \gamma_2.

Hneppið
~~~~~~~

Nú drögum við nálgunarjöfnurnar saman í eitt línulegt
:math:`(N+1)\times(N+1)` hneppi,

.. math::

  \begin{cases}
   \alpha_1c_0-\beta_1\dfrac{c_1-c_0}h= \gamma_1,\\
   a_2(x_j)\dfrac{c_{j-1}-2c_j+c_{j+1}}{h^2}+a_1(x_j)
   \dfrac{c_{j+1}-c_{j-1}}{2h}+a_0(x_j)c_j=f_j,\\
   \alpha_2c_N+\beta_2\dfrac{c_N-c_{N-1}}h = \gamma_2.
         \end{cases}

Það er betra að skoða þetta hneppi eftir að búið er að raða breytunum í
rétta röð,

.. math::

  \begin{cases}
   \big(\alpha_1+\tfrac {\beta_1}h\big)c_0
   -\tfrac {\beta_1}h c_1= \gamma_1,\\
   \big(\tfrac{a_2(x_j)}{h^2}-\tfrac{a_1(x_j)}{2h}\big) c_{j-1}
   +\big(-\tfrac{2a_2(x_j)}{h^2}+a_0(x_j)\big)c_j
   +\big(\tfrac{a_2(x_j)}{h^2}+\tfrac{a_1(x_j)}{2h}\big) c_{j+1} =f_j,\\
   -\tfrac{\beta_2}h c_{N-1}+\big(\alpha_2+\tfrac{\beta_2}h \big) c_N = \gamma_2,
         \end{cases}

þar sem :math:`j=1,\dots,N-1` í miðjöfnunni.

Það er auðvelt að búa til forrit sem les inn öll gögnin sem gefin eru í
jaðargildisverkefninu (:ref:`Link title <eq:21.1.0>`) auk tölunnar :math:`N` og
reiknar út nálgunargildin. Fyrstu dæmin í dæmakaflanum fjalla um þetta
viðfangsefni.

Það er fróðlegt að glöggva sig á útleiðslunni með því að fara í gegnum
hana í ákveðnu dæmi:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Reiknum út nálgunargildi fyrir jaðargildisverkefnið

.. math::

  \begin{cases}
     -(1+x)u''-u'+2u=
   -((1+x)u')'+2u=f, \quad \text{á } ]0,1[,\\
   u(0)=1, \qquad u(1)+u'(1)=0, 
   \end{cases}

í punktunum :math:`\tfrac 13`, :math:`\tfrac 23` og :math:`1`.

*Lausn:*   Skiptingin er :math:`x_0=0`, :math:`x_1=\tfrac 13`,
:math:`x_2=\tfrac 23` og :math:`x_3=1` og billengdin
:math:`h=\tfrac 13`. Við getum að sjálfsögðu stungið viðeigandi gildum
inn í jöfnuhneppið hér fyrir framan, en það er bæði einfaldara og
lærdómsríkara að leiða jöfnurnar út.

**Punktur** :math:`x_0=0` **:** Hér er gildið á :math:`u` gefið,
:math:`u(0)=1`. Nálgunarjafnan segir ekkert meira en að nálgunargildið á
að vera rétta gildið,

.. math:: c_0=1.

**Punktur** :math:`x_1=\tfrac 13` **:**   Við setjum mismunakvótana inn
fyrir afleiðurnar og fáum

.. math::

  -(1+x_1)\dfrac{u_0-2u_1+u_2}{h^2}
   -\dfrac{u_2-u_0}{2h}+2u_1\approx f_1.

Nú gerum við jöfnu úr þessu sem nálgunargildin eiga að uppfylla,

.. math::

  -(1+\tfrac 13)\dfrac{c_0-2c_1+c_2}{(\tfrac 13 )^2}
   -\dfrac{c_2-c_0}{2\cdot \tfrac 13}+2c_1=\tfrac 13
   \quad \Leftrightarrow \quad
   -\tfrac{21}2c_0+26 c_1-\tfrac{27}2c_2=\tfrac 13.

**Punktur** :math:`x_2=\tfrac 23` **:** Við endurtökum þessa reikninga en
hækkum númerið um 1 á öllum liðum

.. math::

  -(1+x_2)\dfrac{u_1-2u_2+u_3}{h^2}
   -\dfrac{u_3-u_1}{2h}+2u_2\approx f_2.

Tilsvarandi jafna fyrir nálgunargildin er því

.. math::

  -(1+\tfrac 23)\dfrac{c_1-2c_2+c_3}{(\tfrac 13 )^2}
   -\dfrac{c_3-c_1}{2\cdot \tfrac 13}+2c_2=\tfrac 23
   \quad \Leftrightarrow \quad
   -\tfrac{27}2c_1+32 c_2-\tfrac{33}2c_2=\tfrac 23.

**Punktur** :math:`x_3=1` **:**   Nú líkjum við eftir jaðarskilyrðinu

.. math:: u_3+\cfrac{u_3-u_2}{h}\approx 0.

Jafnan fyrir nálgunargildin er

.. math::

  c_3+\dfrac{c_3-c_2}{\tfrac 13}=0 
   \quad \Leftrightarrow \quad 
   -3c_2+4c_3=0.

Nú eru allar jöfnurnar komnar og við setjum þær fram á fylkjaformi
:math:`A{\mathbf c} ={\mathbf b}`,

.. math::

  \left[\begin{matrix}
   1& 0 & 0 & 0\\ -\tfrac{21}2 & 26 & -\tfrac{27}2 & 0\\
   0& -\tfrac{27}2& 32 & -\tfrac{33}2\\
   0& 0& -3& 4    
     \end{matrix}\right]
   \left[\begin{matrix}c_0 \\ c_1\\ c_2 \\ c_3\end{matrix}\right]
   =
   \left[\begin{matrix} 1 \\ \tfrac 13 \\ \tfrac 23  \\ 0\end{matrix}\right]

Niðurstaðan er :math:`c_0=1.0000`, :math:`c_1=0.6756`,
:math:`c_2=0.4987` og :math:`c_3=0.3740`.

.. end-toggle::

Skekkjumat
~~~~~~~~~~

Áður en við segjum skilið við þetta jöfnuhneppi, þá skulum við leggja
mat á stigið í nálgunarformúlunum sem við höfum notað Það gerum við með
því að taka fall :math:`\varphi\in C^4(I)` á bili :math:`I` sem
inniheldur punktinn og nota formúlu Taylors, sem segir að

.. math::

  \begin{aligned}
   \varphi(x+h)&=\varphi(x)+\varphi'(x)h+\tfrac 12 \varphi''(x)h^2
   +\tfrac 16 \varphi'''(x)h^3+\tfrac 1{24}\varphi^{(4)}(\xi)h^4,\\
   \varphi(x-h)&=\varphi(x)-\varphi'(x)h+\tfrac 12 \varphi''(x)h^2
   -\tfrac 16 \varphi'''(x)h^3+\tfrac 1{24}\varphi^{(4)}(\eta) h^4.\end{aligned}

þar sem :math:`\xi` er á milli :math:`x` og :math:`x+h` og :math:`\eta`
er á milli :math:`x` og :math:`x-h`. Skekkjurnar í nálgununum sem við
höfum notað eru

.. math::

  \begin{aligned}
     \varphi'(x)&-\dfrac{\varphi(x+h)-\varphi(x)}h
   =-\tfrac 12 \varphi''(x)h
   -\tfrac 16 \varphi'''(x)h^2-\tfrac 1{24}\varphi^{(4)}(\xi)h^3,\\
     \varphi'(x)&-\dfrac{\varphi(x)-\varphi(x-h)}h
   =\tfrac 12 \varphi''(x)h
   -\tfrac 16 \varphi'''(x)h^2+\tfrac 1{24}\varphi^{(4)}(\eta)h^3,\\
     \varphi'(x)&-\dfrac{\varphi(x+h)-\varphi(x-h)}{2h}
   =-\tfrac 1{12}\varphi'''(x)h^2-\tfrac 1{48}
   \big(\varphi^{(4)}(\xi)-\varphi^{(4)}(\eta)\big) h^3,\\
     \varphi''(x)&-\dfrac{\varphi(x-h)-2\varphi(x)+\varphi(x+h)}{h^2}
   =-\tfrac 1{24}
   \big(\varphi^{(4)}(\xi)+\varphi^{(4)}(\eta)\big) h^2.\end{aligned}

Hér sjáum við að fyrstu tvær formúlurnar gefa okkur skekkju af fyrsta
stigi í :math:`h`, sem þýðir að hægt er að meta skekkjuna minni en
:math:`Ch` ar sem :math:`C` er fasti, en hinar gefa okkur skekkju af
öðru stigi sem þýðir að hægt er að meta skekkjuna með :math:`Ch^2`, sem
er að sjálfsögðu miklu betra.

Þegar við leiðum út nálgunarjöfnur fyrir jaðargildisverkefni, þá reynum
við að haga því þannig að allar nálganir sem við gerum séu af sama
stigi. Í þessu fyrsta afbrigði er þessu ekki þannig háttað, því við
notuðum aðeins fyrsta stigs nálgun í jaðarskilyrðunum en annars stigs
nálgun á afleiðunum í innri punktum. Næst ætlum við að bæta úr þessu.

Heildun yfir hlutbil
--------------------

Það eru margar leiðir til þess að setja fram nálgunarjöfnuhneppi fyrir
jaðargildisverkefnið okkar. Nú ætlum við að kynna til sögunnar aðra
aðferð fyrir sama verkefni, en nota Sturm-Liouville-gerð þess,

.. math::

  \begin{cases}
       Lu=-(pu')'+qu=f,& \text{á } ]a,b[\\
   \alpha_1u(a)-\beta_1u'(a)=\gamma_1,\\
   \alpha_2u(b)+\beta_2u'(b)=\gamma_2.
     \end{cases}

Ef :math:`[c,d]\subset [a,b]` er hlutbil og við heildum alla liði
afleiðujöfnunnar :math:`Lu=f` yfir þetta bil, þá fáum við jöfnuna

.. math::

  p(c)u'(c)-p(d)u'(d)
   +\int_c^d q(x)u(x)\, dx=\int_c^d f(x)\, dx.

Nú ætlum við að setja fram nálgunarjöfnu fyrir þessa jöfnu með því að
skipta út afleiðunum fyrir mismunakvóta og heildunum fyrir nálganir
byggðar á einu fallgildi í :math:`[c,d]`.

Við gerum áfram ráð fyrir að skiptingin á bilinu sé jöfn
:math:`x_j=a+jh`, látum
:math:`m_j=\tfrac 12 (x_j+x_{j+1})=x_j+\tfrac 12 h` tákna miðpunkta
hlutbilanna :math:`j=0,1,2,\dots,N-1` og til einföldunar setjum við
:math:`u_j=u(x_j)`, :math:`f_j=f(x_j)`, :math:`p_j=p(x_j)`,
:math:`p(m_j)=p_{j+\frac 12}` og :math:`q_j=q(x_j)` fyrir öll :math:`j`.
Athugið að við skrifum :math:`1\frac 12=\frac 32`,
:math:`2\frac 12=\frac 52` o.s.frv..

Mismunajafna í vinstri endapunkti bilsins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við nýtum okkur að :math:`u` er lausn á afleiðujöfnunnar og heildum alla
liði hennar yfir bilið :math:`[x_0,m_0]`,

.. math::

  p(x_0)u'(x_0)-p(m_0)u'(m_0)
   +\int_{x_0}^{m_0} qu\, dx=\int_{x_0}^{m_0} f\, dx,

leysum síðan :math:`u'(x_0)=u'(a)` út úr þessari jöfnu

.. math::

  u'(x_0)=\dfrac 1{p(x_0)}\bigg(p(m_0)u'(m_0)
   -\int_{x_0}^{m_0}q(x)u(x)\, dx
   +\int_{x_0}^{m_0}f(x)\, dx\bigg)

og setjum inn í jaðarskilyrðið í :math:`x_0`. Það gefur okkur jöfnuna

.. math::

  \alpha_1u(x_0)-\dfrac {\beta_1}{p(x_0)}\bigg(
   p(m_0)u'(m_0)-\int_{x_0}^{m_0}qu\, dx+\int_{x_0}^{m_0}f\,
   dx\bigg)=\gamma_1.

Nú er :math:`m_0-x_0=\frac 12 h`, svo við fáum nálgunarjöfnu með því að
skipta á afleiðu og mismunakvóta og nálga heildin með margfeldi af
billengd og gildi í vinstri endapunkti hlutbilsins,

.. math::

  \alpha_1u_0-\dfrac {\beta_1}{p_0}\bigg(
   p_{\frac 12}\dfrac{u_1-u_0}{h}
   -\tfrac 12 h q_0u_0+ \tfrac 12 hf_0\bigg)\approx \gamma_1.

Næst setjum við inn nálgunargildin :math:`c_0` og :math:`c_1` í stað
:math:`u_0` og :math:`u_1` og búum til nálgunarjöfnu

.. math::

  \alpha_1 c_0-\dfrac {\beta_1}{p_0}\bigg(
   p_{\frac 12}\dfrac{c_1-c_0}{h}
   -\tfrac 12 h q_0c_0+\tfrac 12 hf_0\bigg)=\gamma_1.

Mismunajöfnur í innri punktum skiptingarinnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tökum nú :math:`j=1,\dots,N-1`. Þá er :math:`x_j` miðpunktur bilsins
:math:`[m_{j-1},m_j]`, sem hefur lengdina :math:`h` og
(:ref:`Link title <eq:21.2.3>`) gefur

.. math::

  p(m_{j-1})u'(m_{j-1})-p(m_j)u'(m_j)+\int_{m_{j-1}}^{m_j}q(x)u(x)\, dx
   =\int_{m_{j-1}}^{m_j}f(x)\, dx.

Við nálgum afleiðugildin með mismunakvótum

.. math::

  u'(m_j)\approx \dfrac{u_{j+1}-u_j}h \qquad \text{ og } \qquad
   u'(m_{j-1})\approx \dfrac{u_j-u_{j-1}}h,

heildin með miðpunktsnálgun

.. math::

  \int_{m_{j-1}}^{m_j}q(x)u(x)\, dx \approx hq_ju_j
   \qquad \text{ og } \qquad
   \int_{m_{j-1}}^{m_j}f(x)\, dx \approx hf_j

og búum til nálgunarjöfnu með því að skipta út afleiðugildunum fyrir
mismunakvótana og heildunum fyrir miðpunktsnálganirnar,

.. math::

  p_{j-\frac 12}\dfrac{u_j-u_{j-1}}h
   -p_{j+\frac 12}\dfrac{u_{j+1}-u_j}h
   +hq_ju_j\approx hf_j.

Við breytum þessari nálgunarjöfnu í venjulega jöfnu með því að setja
inn nálgunargildin :math:`c_{j-1}`, :math:`c_j` og :math:`c_{j+1}` fyrir
réttu fallgildin :math:`u_{j-1}`, :math:`u_j` og :math:`u_{j+1}` og
deila öllum liðum með :math:`h`

.. math::

  p_{j-\frac 12}\dfrac{c_{j}-c_{j-1}}{h^2}
   -p_{j+\frac 12}\dfrac{c_{j+1}-c_j}{h^2}
   +q_jc_j= f_j.

Mismunajafna í hægri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú þurfum við að finna nálgunarjöfnu fyrir jaðarskilyrðið í punktinum
:math:`b=x_N`,

.. math:: \alpha_2u(x_N)+\beta_2u'(x_N)=\gamma_2.

Við heildum alla liði afleiðujöfnunnar yfir bilið :math:`[m_{N-1},x_N]`
og fáum

.. math::

  -p(x_N)u'(x_N)+p(m_{N-1})u'(m_{N-1})+\int_{m_{N-1}}^{x_N} q(x)u(x)\, dx
   =\int_{m_{N-1}}^{x_N} f(x)\, dx,

leysum :math:`u'(x_N)` út úr þessari jöfnu

.. math::

  u'(x_N)=\dfrac 1{p(x_N)}\bigg(p(m_{N-1})u'(x_{N-1})
   +\int_{x_{N-1}}^{x_N}q(x)u(x)\, dx-
   \int_{x_{N-1}}^{x_N}f(x)\, dx\bigg)

og stingum inn í jaðarskilyrðið

.. math::

  \alpha_2u(x_N)+\dfrac {\beta_2}{p(x_N)}\bigg(
   p(m_{N-1})u'(m_{N-1})+\int_{m_{N-1}}^{x_N}qu\, dx
   - \int_{m_{N-1}}^{x_N} f\, dx\bigg)=\gamma_2.

Síðan skiptum við á afleiðu og mismunakvóta og nálgum heildin með
margfeldi af billengd og gildi í hægri endapunkti hlutbilsins,

.. math::

  \alpha_2u_N+\dfrac {\beta_2}{p_N}\bigg(
   p_{N-\frac 12}\dfrac{u_N-u_{N-1}}{h}+\tfrac 12h
   q_Nu_N -\tfrac 12h f_N\bigg)\approx\gamma_2.

Við setjum að lokum :math:`c_{N-1}` og :math:`c_N` í stað
:math:`u_{N-1}` og :math:`u_N` og erum þá komin með síðustu jöfnuna
fyrir nálgunargildin

.. math::

  \alpha_2c_N+\dfrac {\beta_2}{p_N}\bigg(
   p_{N-\frac 12}\dfrac{c_N-c_{N-1}}{h}+\tfrac 12h
   q_Nc_N -\tfrac 12 h f_N\bigg)=\gamma_2.

Nálgunarjöfnuhneppið
~~~~~~~~~~~~~~~~~~~~

Línulega jöfnuhneppið fyrir nálgunargildin, sem við leiddum út hér að
framan er

.. math::

  \begin{cases}
       \alpha_1 c_0-\dfrac {\beta_1}{p_0}\bigg(
   p_{\frac 12}\dfrac{c_1-c_0}{h}
   -\tfrac 12 h q_0c_0+\tfrac 12 hf_0\bigg)=\gamma_1.
   \\
   p_{j-\frac 12}\dfrac{c_{j}-c_{j-1}}{h^2}
   -p_{j+\frac 12}\dfrac{c_{j+1}-c_j}{h^2}
   +
   q_jc_j= f_j.  
   \\
   \alpha_2c_N+\dfrac {\beta_2}{p_N}\bigg(
   p_{N-\frac 12}\dfrac{c_N-c_{N-1}}{h}+\tfrac 12h
   q_Nc_N -\tfrac 12 h f_N\bigg)=\gamma_2.  
     \end{cases}

Nú röðum við óþekktu stærðunum í rétta röð og fáum
:math:`(N+1)\times (N+1)` línulegt jöfnuheppi fyrir gildin :math:`c_j`,

.. math::

  \begin{cases}
     \bigg(\alpha_1+\dfrac{\beta_1}{p_0}
   \bigg(\dfrac{p_{\frac 12}}h+\tfrac 12 hq_0\bigg)\bigg)c_0
   -\dfrac{\beta_1p_{\frac 12}}{p_0h}c_1
   =\gamma_1+\tfrac 12 \dfrac{\beta_1hf_0}{p_0},
   \\
   -\dfrac{p_{j-\frac 12}}{h^2} c_{j-1}
   +\bigg(\dfrac{p_{j-\frac 12}+p_{j+\frac 12}}{h^2}+q_j\bigg) c_j
   -\dfrac{p_{j+\frac 12}}{h^2} c_{j+1}  =f_j, 
   \\
   -\dfrac{\beta_2p_{N-\frac 12}}{p_Nh}c_{N-1}+
   \bigg(\alpha_2+\dfrac{\beta_2}{p_N}\bigg(\dfrac{p_{N-\frac 12}}{h}+\tfrac
   12 h q_N\bigg)\bigg)c_N
   =\gamma_2+\tfrac 12\dfrac{\beta_2h}{p_N}f_N.
         \end{cases}

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Reiknum út nálgunargildi fyrir jaðargildisverkefnið

.. math::

  \begin{cases}
     -(1+x)u''-u'+2u=
   -((1+x)u')'+2u=f, \quad \text{á } ]0,1[,\\
   u(0)=1, \qquad u(1)+u'(1)=0, 
   \end{cases}

í punktunum :math:`\tfrac 13`, :math:`\tfrac 23` og :math:`1` með því
að beita heildun yfir hlutbil.

*Lausn:*   Þetta er endurtekning á sýnidæmi :ref:`Link title <sy:21.2.1>`. Skiptingin
er :math:`x_0=0`, :math:`x_1=\tfrac 13`, :math:`x_2=\tfrac 23` og
:math:`x_3=1` og billengdin :math:`h=\tfrac 13`. Miðpunktarnir eru
:math:`m_0=\tfrac 16`, :math:`m_1=\tfrac 12` og :math:`m_2=\tfrac 56`.
Við förum líkt að og í úrlausn okkar á sýnidæmi :ref:`Link title <sy:21.2.1>` og
útfærum heildunina yfir hlutbilin.

**Punktur** :math:`x_0=0` **:**   Hér er gildið á :math:`u` gefið og
nálgunarjafnan er :math:`c_0=1`.

**Punktur** :math:`x_1=\tfrac 13` **:**   Heildum yfir hlutbilið
:math:`[\tfrac 16,\tfrac   12]`,

.. math::

   \begin{aligned}
   &-\bigg[(1+x)u'(x)\bigg]_{m_0}^{m_1}+
   2\int_{m_0}^{m_1}u(x)\, dx\\
   &=\tfrac 76 u'(\tfrac 16)-\tfrac 32 u'(\tfrac 12)
   +
   2\int_{\tfrac 16}^{\tfrac 12}u(x)\, dx
   =\int_{\tfrac 16}^{\tfrac 12}x\,
   dx=\tfrac 19.
   \end{aligned}

Við skiptum út afleiðum fyrir mismunakvóta og miðpunktsnálgun fyrir
heildið í þessari jöfnu,

.. math::

  \tfrac 76 \dfrac{u_1-u_0}{h}-\tfrac 32 \dfrac{u_2-u_1}{h}
   +2h u_1\approx \tfrac 19,

búum til nálgunarjöfnur og deilum að lokum öllum liðum með
:math:`h=\tfrac 13`

.. math::

  \tfrac 76 \dfrac{c_1-c_0}{\tfrac 13}-\tfrac 32 \dfrac{c_2-c_1}{\tfrac 13}
   +2\cdot \tfrac 13 c_1 = \tfrac 19
   \quad \Leftrightarrow \quad
   -\tfrac{21}2c_0+26 c_1-\tfrac{27}2c_2=\tfrac 13.

**Punktur** :math:`x_2=\tfrac 23` **:**   Við heildum yfir hlutbilið
:math:`[\tfrac 12,\tfrac 56]` og endurtökum reikningana, en það þýðir
hækkum á númerinu um 1 á öllum liðum

.. math::

   \begin{aligned}
  &-\bigg[(1+x)u'(x)\bigg]_{m_1}^{m_2}+
   2\int_{m_1}^{m_2}u(x)\, dx\\
   &=\tfrac 32 u'(\tfrac 12)-\tfrac {11}6 u'(\tfrac 56)
   +
   2\int_{\tfrac 12}^{\tfrac 56}u(x)\, dx
   =\int_{\tfrac 12}^{\tfrac 56}x\, dx=\tfrac 29.
   \end{aligned}

Við skiptum út afleiðum fyrir mismunakvóta og miðpunktsnálgun fyrir
heildið

.. math::

  \tfrac 32 \dfrac{u_2-u_1}{h}-\tfrac {11}6 \dfrac{u_3-u_2}{h}
   +2h u_2\approx \tfrac 29.

Nú setjum við nálgunargildin í stað réttu gildanna, deilum einnig öllum
liðum með :math:`h=\tfrac 13` og búum til nálgunarjöfnur

.. math::

  \tfrac 32 \dfrac{c_2-c_1}{\tfrac 13}-\tfrac {11}6 \dfrac{c_3-c_2}{\tfrac 13}
   +2\cdot \tfrac 13 c_2 = \tfrac 29
   \quad \Leftrightarrow \quad
   -\tfrac{27}2c_1+32 c_2-\tfrac{33}2c_3=\tfrac 23.

**Punktur** :math:`x_3=1` **:**   Við heildum yfir hlutbilið
:math:`[\tfrac 56,1]` og fáum

.. math::

   \begin{aligned}
  &-\bigg[(1+x)u'(x)\bigg]_{m_2}^{x_3}+
   2\int_{m_2}^{x_3}u(x)\, dx\\
   &=\tfrac {11}6 u'(\tfrac 56)-2u'(1)
   +
   2\int_{\tfrac 56}^{1}u(x)\, dx
   =\int_{\tfrac 56}^{1}x\, dx=\tfrac 16 \cdot \tfrac
   {11}{12}=\tfrac{11}{72}.
   \end{aligned}

Í útleiðslunni hér að framan, leystum við :math:`u'(1)` úr úr þessari
jöfnu og stungum inn í jöfnuna fyrir jaðargildin. Við getum eins snúið
því við leyst :math:`u'(1)=-u(1)=-u_3` út úr jaðargildunum og stungið
inn í þessa jöfnu. Það gefur

.. math:: \tfrac {11}6\dfrac{u_3-u_2}h+2u_3+2\cdot \tfrac 16 u_3\approx \tfrac{11}{72}.

Þetta gefur okkur síðustu nálgunarjöfnuna og við deilum í alla liði
hennar með :math:`h=\tfrac 13`

.. math::

  \tfrac {11}6\dfrac{c_3-c_2}{\tfrac 13}+
   2c_3+\tfrac 13 c_3 = \tfrac{11}{72}
   \quad \Leftrightarrow \quad
   -\tfrac{33}2c_2+\tfrac{47}2 c_3=\tfrac{11}{24}.

Þrjár fyrstu línur jöfnuhneppisins :math:`A{\mathbf c} ={\mathbf b}`
eru þær sömu og í jöfnuhneppinu í :ref:`Link title <sy:22.2.1>`,

.. math::

  \left[\begin{matrix}
   1& 0 & 0 & 0\\ -\tfrac{21}2 & 26 & -\tfrac{27}2 & 0\\
   0& -\tfrac{27}2& 32 & -\tfrac{33}2\\
   0& 0& -\tfrac{33}2& \tfrac {47}2    
     \end{matrix}\right]
   \left[\begin{matrix}c_0 \\ c_1\\ c_2 \\ c_3\end{matrix}\right]
   =
   \left[\begin{matrix} 1 \\ \tfrac 13 \\ \tfrac 23  \\ \tfrac {11}{24}
   \end{matrix}\right]

Niðurstaðan er :math:`c_0=1.0000`, :math:`c_1=0.7119`,
:math:`c_2=0.5192` og :math:`c_3=0.3840`.

.. end-toggle::

Nálgunarjöfnur fyrir almennar skiptingar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í útleiðslu okkar hér að framan gerðum við ráð fyrir að skiptingin væri
jöfn. Ef við höfum almenna skiptingu, látum :math:`h_j=x_{j+1}-x_j`
tákna lengdina á hlutbilinu :math:`[x_j,x_{j+1}]` og heildum yfir
hlutbil eins og hér að framan, þá fáum við nýtt jöfnuhneppi fyrir
nálgunargildin,

.. math::

  \begin{cases}
     \bigg(\alpha_1+\dfrac{\beta_1}{p_0}
   \bigg(\dfrac{p_{\frac 12}}{h_0}+\tfrac 12 h_0q_0\bigg)\bigg)c_0
   -\dfrac{\beta_1p_{\frac 12}}{p_0h_0}c_1
   =\gamma_1+\tfrac 12 \dfrac{\beta_1h_0f_0}{p_0},
   \\
   -\dfrac{2p_{j-\frac 12}}{(h_{j-1}+h_j)h_j} c_{j-1}
   +\bigg(
   \dfrac{2p_{j-\frac 12}}{(h_{j-1}+h_j)h_{j-1}}+
   \dfrac{2p_{j+\frac 12}}{(h_{j-1}+h_j)h_j}+q_j\bigg) c_j
   -\dfrac{2p_{j+\frac 12}}{(h_{j-1}+h_j)h_j} c_{j+1}
   =f_j,\\
   -\dfrac{\beta_2p_{N-\frac 12}}{p_Nh_{N-1}}c_{N-1}+
   \bigg(\alpha_2+\dfrac{\beta_2}{p_N}\bigg(\dfrac{p_{N-\frac 12}}{h_{N-1}}
   +\tfrac 12 h_{N-1} q_N\bigg)\bigg)c_N
   =\gamma_2+\tfrac 12\dfrac{\beta_2h_{N-1}}{p_N}f_N.    
     \end{cases}

Línuleg brúun og þúfugrunnföll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar nálgunargildin :math:`c_j\approx u_j` hafa verið ákvörðuð út frá
mismunajöfnunum, er eðlilegt að nota línulega brúun á milli þeirra til
þess að finna fall :math:`v` sem nálgar :math:`u` í öllum punktum
bilsins :math:`[a,b]`

Þess vegna skilgreinum við *nálgunarfall* :math:`v\in C[a,b]`, sem tekur
gildið :math:`c_j` í punktinum :math:`x_j` og er þannig að graf þess á
bilinu :math:`[x_j,x_{j+1}]` er línustrik. Þá er auðvelt að sjá að

.. math:: v=c_0\varphi_0+\cdots+c_N\varphi_N,

Þar sem :math:`\big(\varphi_j\big)_{j=0}^N` tákna *þúfugrunnföllin* sem
skiptingin :math:`\big(x_j\big)_{j=0}^N` skilgreinir, en
:math:`\varphi_j` er samfellda fallið sem tekur gildið :math:`1` í
:math:`x_j`, tekur gildið :math:`0` í öllum hinum skiptingarpunktunum og
hefur graf sem er línustrik á sérhverju hlutbilanna
:math:`[x_j,x_{j+1}]`, :math:`j=0,\dots,N-1`. Við getum skrifað upp
formúlur fyrir föllunum :math:`\varphi_j` og afleiðum þeirra,

.. math::

  \begin{aligned}
   \varphi_0(x)&=\begin{cases} \tfrac{x_1-x}{h_0}, &x\in [x_0,x_1],\\
   0, &\text{annars},
   \end{cases} &
   \varphi'_0(x)&=\begin{cases} \tfrac{-1}{h_0}, &x\in ]x_0,x_1[,\\
   0, &x\in {{\mathbb  R}}\setminus [x_0,x_1],
   \end{cases} 
   \nonumber
   \\
   \varphi_j(x)&=\begin{cases} \tfrac{x-x_{j-1}}{h_{j-1}}, &x\in [x_{j-1},x_j],\\
   \tfrac{x_{j+1}-x}{h_j}, &x\in [x_j,x_{j+1}],\\
   0, &\text{annars}.
   \end{cases}&
   \varphi'_j(x)&=\begin{cases} \tfrac{1}{h_{j-1}}, &x\in ]x_{j-1},x_j[,\\
   \tfrac{-1}{h_j}, &x\in [x_j,x_{j+1}],\\
   0, &x\in {{\mathbb  R}}\setminus [x_{j-1},x_{j+1}].
   \end{cases}
  \\
   \varphi_m(x)&=\begin{cases} \tfrac{x-x_{m-1}}{h_{m-1}}, &x\in [x_{m-1},x_m],\\
   0, &\text{annars}. \nonumber
   \end{cases}&
   \varphi'_m(x)&=\begin{cases} \tfrac{1}{h_{m-1}}, &x\in [x_{m-1},x_m],\\
   0, &\text{annars}. \nonumber
   \end{cases}\end{aligned}

Staðarskekkjur í mismunasamböndum
---------------------------------

Lítum nú aftur á jafna skiptingu á :math:`[a,b]` með billengd
:math:`h=(b-a)/N`,

.. math::

  a=x_0<x_1<\cdots<x_N=b, \quad x_j=x_0+jh,  \quad 
   m_j=x_j+\tfrac 12 h.

Í þessum punktum uppfyllir lausnin :math:`u` á jaðargildisverkefninu
jöfnuhneppið

.. math::

  \begin{cases}
       B_1u=\alpha_1u_0-\beta_1u'(x_0)=\gamma_1\\
   Lu(x_j)=-p(x_j)u''(x_j)-p'(x_j)u'(x_j)+q_ju_j=f_j,\\
   B_2u=\alpha_2u_N+\beta_2u'(x_N)=\gamma_2,
     \end{cases}

þar sem :math:`j=1,\dots,N-1`. Samkvæmt (:ref:`Link title <eq:21.3.1a>`) uppfyllir
nálgunarlausnin

.. math:: v(x)=\sum_{j=0}^Nc_j\varphi_j(x)=c_0\varphi_0(x)+\cdots+c_N\varphi_N(x),

jöfnuhneppið

.. math::

  \begin{cases}
   M_0v=\alpha_1 v(x_0)-\dfrac {\beta_1}{p_0}\bigg(
   p_{\frac 12}\dfrac{v(x_1)-v(x_0)}{h}
   -\tfrac 12 h q_0v(x_0)+\dfrac 12 hf_0\bigg)=\gamma_1,
   \\
   M_jv=
   -p_{j+\frac 12}\dfrac{v(x_{j+1})-v(x_j)} {h^2}
   +p_{j-\frac 12}\dfrac{v(x_{j})-v(x_{j-1})} {h^2}
   + q_jv(x_j)=f_j,
   \\
   M_Nv=
   \alpha_2v(x_N)+\dfrac {\beta_2}{p_N}\bigg(
   p_{N-\frac 12}\dfrac{v(x_N)-v(x_{N-1})}{h}+\tfrac 12h
   q_Nv(x_N) -\tfrac 12h f_N\bigg)=\gamma_2,
     \end{cases}

þar sem :math:`j=1,\dots,N-1`. Athugið að við getum reiknað út
:math:`M_0\varphi,\dots,M_n\varphi` fyrir hvaða
:math:`\varphi\in C[a,b]` sem er og þá sérstaklega lausnina :math:`u` á
jaðargildisverkefninu. Við köllum :math:`M_j` *mismunavirkja*
(e. *difference operator*) vegna þess að :math:`M_j` er vörpun sem
úthlutar falli :math:`\varphi` gildi :math:`M_j\varphi` sem er
skilgreint út frá mismunakvótum fallsins :math:`\varphi`. Til þess að
kanna samræmið milli jöfnuhneppanna (:ref:`Link title <eq:21.3.7>`) og
(:ref:`Link title <eq:21.3.8>`) stingum við :math:`u(x)` í stað :math:`v(x)` inn í
síðara jöfnuhneppið og tökum mismuninn,

.. math::

  S_0u=B_1u-M_0u, \quad
   S_ju=Lu(x_j)-M_ju, \ j=1,\dots,N-1, \qquad 
   S_Nu=B_2u-M_Nu.

Þessar stærðir nefnast *staðarskekkjur* (e. *local truncation error*)
*mismunavirkjanna* :math:`M_j` í punktunum :math:`x_j`. Við segjum að
mismunasamböndin :math:`M_0u,\dots,M_Nu` *samræmist*
jaðargildisverkefninu (:ref:`Link title <eq:21.1.1>`) ef allar staðarskekkjurnar
:math:`S_ju` stefna á :math:`0` þegar fínleiki skiptingarinnar :math:`h`
stefnir á :math:`0`. Þetta þýðir að fyrir sérhvert :math:`\varepsilon>0`
er til :math:`\delta>0` þannig að

.. math::

  |S_ju|<\varepsilon, \qquad \text{ fyrir öll } j=0,\dots,N \quad\text{
     og } \quad h=(b-a)/N<\delta.

Setning Taylors
~~~~~~~~~~~~~~~

Áður en við hefjum glímuna við að meta staðarskekkjur í
mismunasamböndum, skulum við rifja upp setningu Taylors sem er helsta
tólið sem við höfum til þess að gera staðbundnar nálganir á föllum. Hún
segir að fyrir sérhvert fall :math:`\varphi\in C^m(I)`, þar sem
:math:`I` er bil og sérhvern punkt :math:`x\in I`, gildir

.. math::

  \varphi(x+h)=\varphi(x)+\varphi'(x)h+\tfrac 1{2}\varphi''(x)h^2+
   \cdots+\tfrac 1{m!} \varphi^{(m)}(x)h^m+\varepsilon_m(x,h)

þar sem skekkjan :math:`\varepsilon_m(x,h)` í nálgun á
:math:`\varphi(x+h)` með Taylor-margliðu :math:`\varphi` í hægri hlið
jöfnunnar uppfyllir

.. math:: \dfrac{\varepsilon_m(x,h)}{h^m}\to 0, \qquad h\to 0.

Ef :math:`\varphi\in C^{m+1}(I)`, þá er til punktur :math:`\xi` milli
:math:`x` og :math:`x+h` þannig að

.. math:: \varepsilon_m(x,h)=\tfrac 1{(m+1)!} \varphi^{(m+1)}(\xi){h^{m+1}}

og við fáum betra mat,

.. math:: |\varepsilon_m(x,h)|\leq C h^{m+1},

með :math:`C\geq \max_{t\in I}\tfrac 1{(m+1)!}|\varphi^{(m+1)}(t)|`.

Stig og óvera
~~~~~~~~~~~~~

Við þurfum oft að meta stærðir :math:`\chi(h)` og viljum gefa til kynna
hversu hratt þær stefna á :math:`0` ef :math:`h` stefnir á :math:`0`. Þá
er eðlilegt að bera :math:`\chi(h)` saman við veldi :math:`h^k` með
veldisvísinn :math:`k\in {{\mathbb  R}}_+`, (:math:`k\geq 0`). Við
segjum að :math:`\chi(h)` sé af *stigi* :math:`k` eða :math:`k` *-ta
stigi* eða að :math:`\chi(h)` sé *stórt o af* :math:`h^k` og táknum það
með :math:`\chi(h)=O(h^k)`, ef til eru fastar :math:`C>0` og
:math:`c>0`, þannig að

.. math:: |\chi(h)|\leq C h^k, \qquad h\in ]0,c].

Við segjum að :math:`\chi(h)` sé *óvera af* :math:`h^k` eða að
:math:`\chi(h)` sé *lítið o af* :math:`h^k` og táknum það
:math:`\chi(h)=o(h^k)`, ef

.. math:: \dfrac{\chi(h)}{h^k} \to 0, \qquad h\to 0.

Ef :math:`0\leq j<k` og :math:`\chi(h)=O(h^k)` (eða
:math:`\chi(h)=o(h^k))`, þá er :math:`\chi(h)/h^j=O(h^{k-j})` (eða
:math:`\chi(h)/h^j=o(h^{k-j})`).

Ef við stillum upp jöfnum

.. math::

  \chi(h)=O(1), \ 
   \chi(h)=o(1), \ 
   \chi(h)=O(h), \ 
   \chi(h)=o(h), \ 
   \chi(h)=O(h^2), \ 
   \chi(h)=o(h^2),\dots.

og lítum á þær sem skekkjumat, þá fer matið á :math:`\chi(h)` sem við
lesum út úr þessum jöfnum batnandi þegar við lesum línuna frá vinstri
til hægri.

Sem dæmi er eðlilegt að taka Taylor-nálgunina sem við nefndum hér að
framan, en setning Taylors segir að

.. math::

  \varepsilon_m(x,h)=o(h^m) \ \ 
   \text{ ef } \  \varphi\in C^m[a,b] \quad 
   \text{ og } \quad 
   \varepsilon_m(x,h)=O(h^{m+1}) \ \  
   \text{ ef } \  \varphi\in C^{m+1}[a,b].

Hugsum okkur að við séum með tvö föll :math:`\chi_1` og :math:`\chi_2`
og að við höfum skekkjumatið :math:`\chi_1(h)=O(h^{k_1})` og
:math:`\chi_2(h)=O(h^{k_2})`. Þá er

.. math:: |\chi_1(h)\chi_2(h)|\leq C_1h^{k_1}C_2h^{k_2}=C_1C_2h^{k_1+k_2}

sem segir okkur að :math:`\chi_1(h)\chi_2(h)=h^{k_1+k_2}`. Fyrir
summuna höfum við hins vegar

.. math::

  |\chi_1(h)+\chi_2(h)|\leq C_1h^{k_1}+C_2h^{k_2}\leq
   (C_1+C_2)h^{\min\{k_1,k_2\}},
   \qquad   h\leq 1,

og það segir okkur að
:math:`\chi_1(h)+\chi_2(h)=O(h^{\min\{k_1,k_2\}})`.

Athugið að þegar skrifað er :math:`\chi_1(h)=\chi_2(h)+O(h^k)`, þá er
átt við að nálgunin á :math:`\chi_1(h)` með :math:`\chi_2(h)` hafi
skekkju af stigi :math:`k`, sem jafngildir því að segja að
:math:`\chi_1(h)-\chi_2(h)=O(h^k)`.

Mat á staðarskekkju
~~~~~~~~~~~~~~~~~~~

Þegar við metum staðarskekkju í mismunasamböndunum, þá skrifum við
punktana :math:`x_{j-1}=x_j-h` og :math:`x_{j+1}=x_j+h` og lítum á
:math:`S_ju` sem fall af :math:`h`. Síðan viljum við finna hæsta
mögulega veldi á :math:`k` þannig að :math:`S_ju(h)=O(h^k)` eða
:math:`S_ju(h)=o(h^k)`.

Staðarskekkja í vinstri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við lítum nú á vinstri endapunktinn :math:`x_0=a` og könnum
staðarskekkju nálgunarlausnarinnar í honum. Til einföldunar skulum við
skrifa :math:`x` í stað :math:`x_0`,

.. math::

  \begin{aligned}
   S_0u(h)
   &= \alpha_1u(x)-\beta_1 u'(x) \\
   &-\alpha_1 u(x)+\dfrac {\beta_1}{p(x)}\bigg(
   p(x+\tfrac 12 h)\dfrac{u(x+h)-u(x)}{h}
   -\tfrac 12 h q(x)u(x)+\tfrac 12 hf(x)\bigg)\\
   &=-\dfrac {\beta_1}{p(x)}\bigg(p(x)u'(x)
   -p(x+\tfrac 12 h)\dfrac{u(x+h)-u(x)}{h}
   +\tfrac 12 h q(x)u(x)-\tfrac 12 hf(x)\bigg)\\\end{aligned}

Samkvæmt forsendu er :math:`p\in C^1[a,b]` og af því leiðir að
:math:`u\in C^2[a,b]`. Af Taylor-setningunni leiðir því að

.. math::

  \begin{aligned}
     p(x+\tfrac 12 h)&=p(x)+\tfrac 12 hp'(x)+o(h)\\
   \dfrac{u(x+h)-u(x)}{h}&=
   u'(x)+\tfrac 12 hu''(x)+o(h).\end{aligned}

Nú margföldum við saman alla liði og fáum

.. math::

  \begin{aligned}
   p(x+\tfrac 12 h)\dfrac{u(x+h)-u(x)}h 
   &=\big(p(x)+\tfrac 12 hp'(x)+o(h)\big)
   \big(u'(x)+\tfrac 12 hu''(x)+o(h)\big)\\
   &=p(x)u'(x)+\tfrac 12 h\big(p(x)u''(x)+p'(x)u'(x)\big)
   +o(h).\end{aligned}

Með því að setja þessar nálganir inn í formúluna hér að framan og
notfæra okkur að :math:`u` uppfyllir afleiðujöfnuna í punktinum
:math:`x` fáum við

.. math::

  \begin{gathered}
   S_0u(h)=
   -\dfrac {\beta_1h}{2p(x)}\bigg(
   -p(x)u''(x)-p'(x)u'(x)
   +q(x)u(x)-f(x)\bigg)+o(h)=o(h).\end{gathered}

Annar en síðri möguleiki á nálgun jaðarskilyrðisins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú er tækifæri til þess að útskýra hvers vegna við völdum ekki nálgunina

.. math:: \alpha_1u_0-\beta_1\dfrac{u_1-u_0}h\approx \gamma_1,

en hún gefur af sér mismunajöfnuna

.. math:: \widetilde M_0v=\alpha_1v(x_0)-\beta_1\dfrac{v(x_1)-v(x_0)}h=\gamma_1,

og staðarskekkjuna (hér er :math:`x=x_0`),

.. math::

  \begin{gathered}
   \widetilde S_0u(h)=B_1u-\widetilde M_0u
   =-\beta_1\bigg(
   u'(x)-\dfrac{u(x+h)-u(x)}h\bigg)
   =\beta_1\big(-\tfrac 12 hu''(x)+o(h)\big)=O(h).\end{gathered}

Fyrri nálgunaraðferðin er betri því hún hefur staðarskekkju
:math:`S_0u(h)=o(h)`, sem er betra mat en :math:`O(h)`.

Staðarskekkja í innri punktum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tökum nú innri punkt í skiptingunni :math:`x_j` með
:math:`j=1,\dots,N-1`. Fyrir hann er

.. math::

  \begin{aligned}
     S_ju(h)=&Lu(x_j)-M_ju\\
   =&-p(x_j)u''(x_j)-p'(x_j)u'(x_j)\\
   &+p(m_j)\dfrac{u(x_j+h)-u(x_j)}{h^2}
   +p(m_{j-1})\dfrac{u(x_j-h)-u(x_j)}{h^2}\end{aligned}

Nú þurfum við fjórar Taylor-liðanir. Til einföldunar setjum við
:math:`x` í stað :math:`x_j` og fáum

.. math::

  \begin{aligned}
     p(m_j)&=p(x+\tfrac 12 h)=p(x)+\tfrac 12 p'(x)h+o(h),\\
     p(m_{j-1})&=p(x-\tfrac 12 h)=p(x)-\tfrac 12 p'(x)h+o(h),\\
   \dfrac{u(x+h)-u(x)}{h^2}&=
   \dfrac 1h u'(x)+\tfrac 12 u''(x)+o(1),\\
   \dfrac{u(x-h)-u(x)}{h^2}&=
   -\dfrac 1h u'(x)+\tfrac 12 u''(x)+o(1),\\\end{aligned}

Þetta gefur

.. math::

  \begin{aligned}
   p(m_j)&\dfrac{u(x+h)-u(x)}{h^2}
   +p(m_{j-1})\dfrac{u(x-h)-u(x)}{h^2} \\
   &=\big(p(x)+\tfrac 12 p'(x)h+o(h)\big)
   \big(\dfrac 1h u'(x)+\tfrac 12 u''(x)+o(1)\big)  \\
   &+\big(p(x)-\tfrac 12 p'(x)h+o(h)\big)
   \big(-\dfrac 1h u'(x)+\tfrac 12 u''(x)+o(1)\big)\\
   &=p(x)u''(x)+p'(x)u'(x)+o(1)\end{aligned}

Af þessu leiðir að

.. math:: S_ju(h)=o(1)\to 0, \qquad h\to 0.

Þetta segir okkur að það er samræmi milli afleiðujöfnunnar og
mismunajöfnunnar í punktinum :math:`x_j`.

Staðarskekkja í innri punktum með betri forsendum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar við fengumst við veldaraðalausnir á afleiðujöfnum, þá sáum við að
lausn :math:`u` á jöfnunni :math:`Lu=f` er gefin með veldaröð í grennd
um sérhvern punkt, ef föllin :math:`p`, :math:`q` og :math:`f` eru gefin
með veldaröðum í grennd um sérhvern punkt. Fallið :math:`u` er þá
óendanlega oft deildanlegt og við getum tekið eins marga liði í
Taylor-nálgun og við viljum. Setjum til einföldunar :math:`x` í stað
:math:`x_j` og lítum aftur á Taylor-liðanir okkar,

.. math::

  \begin{aligned}
     p(m_j)&=p(x+\tfrac 12 h)=p(x)+\tfrac 12 p'(x)h+O(h^2),\\
     p(m_{j-1})&=p(x-\tfrac 12 h)=p(x)-\tfrac 12 p'(x)h+O(h^2),\\
   \dfrac{u(x+h)-u(x)}{h^2}&=
   \dfrac 1h u'(x)+\tfrac 12 u''(x)+\tfrac 16 u'''(x)h+O(h^2),\\
   \dfrac{u(x-h)-u(x)}{h^2}&=
   -\dfrac 1h u'(x)+\tfrac 12 u''(x)-\tfrac 16 u'''(x)h+O(h^2).\\\end{aligned}

Við fáum nú endurbót á reikningi okkar hér að framan því þriðja stigs
afleiðan fellur út

.. math::

  \begin{aligned}
   p(m_j)&\dfrac{u(x+h)-u(x)}{h^2}
   +p(m_{j-1})\dfrac{u(x-h)-u(x)}{h^2} \\
   &=\big(p(x)+\tfrac 12 p'(x)h+O(h^2)\big)
   \big(\dfrac 1h u'(x)+\tfrac 12 u''(x)+\tfrac 16 u'''(x)h+O(h^2)\big)  \\
   &+\big(p(x)-\tfrac 12 p'(x)h+O(h^2)\big)
   \big(-\dfrac 1h u'(x)+\tfrac 12 u''(x)-\tfrac 16 u'''(x)h+O(h^2)\big)\\
   &=p(x)u''(x)+p'(x)u'(x)+O(h^2)\end{aligned}

Af þessu leiðir að skekkjumatið verður miklu betra,

.. math:: S_ju(h)=O(h^2).

miðað við :math:`S_ju(h)=o(1)` sem fæst þegar aðeins má gera ráð fyrir
að :math:`p\in C^1[a,b]` og :math:`u\in C^2[a,b]`. Athugið að við getum
ekki fengið skekkumat með hærra stigi en :math:`2`, þótt við tækjum
fleiri liðið því fjórða stigs liðurinn hverfur ekki eins og þriðja stigs
liðurinn gerir hér.

Staðarskekkja í hægri endapunkti :math:`x_N=b`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú gefum við okkur aftur að :math:`p\in C^1[a,b]` og
:math:`u\in C^2[a,b]` og lítum á hægri endapunkt :math:`x_N=b`. Til
einföldunar skrifum við :math:`x` í stað :math:`x_N`. Þá er

.. math::

  S_Nu(h)=-\dfrac{\beta_2}{p(x)}
   \bigg(-p(x)u'(x)-p(x-\tfrac 12 h)\dfrac{u(x-h)-u(x)}h+\tfrac 12 h
   q(x)u(x) -\tfrac 12 h f(x)\bigg)

Með Taylor-liðun fáum við

.. math::

  \begin{aligned}
     p(x-\tfrac 12 h)
   \dfrac{u(x-h)-u(x)}h 
   &=\big(p(x)-\tfrac 12 h p'(x)+o(h)\big)
   \big(-u'(x)+\tfrac 12 hu''(x)+o(h)\big)\\
   &=-p(x)u'(x)+\tfrac 12 h\big(p(x) u''(x)+p'(x)u'(x)\big)+o(h)\end{aligned}

Við smeygjum hægri hliðinni inn í jöfnuna hér að framan, notfærum okkur
að :math:`u` er lausn á afleiðujöfnunni og fáum

.. math::

  S_Nu(h)=-\dfrac{\beta_2h}{2p(x)}
   \bigg(-p(x) u''(x)-p'(x)u'(x)+q(x)u(x)-f(x)\bigg)+o(h)
   =o(h).

Ef við getum rökstutt að :math:`p\in C^2[a,b]` og
:math:`u\in C^3[a,b]`, eins og í tilfellinu þegar :math:`p`, :math:`q`
og :math:`f` eru gefin með veldaröðum í grennd um sérhvern punkt, þá
höfum við betri Taylor-nálganir

.. math::

  \begin{aligned}
     p(x-\tfrac 12 h)
   \dfrac{u(x-h)-u(x)}h 
   &=\big(p(x)-\tfrac 12 h p'(x)+O(h^2)\big)
   \big(-u'(x)+\tfrac 12 hu''(x)+O(h^2)\big)\\
   &=-p(x)u'(x)+\tfrac 12 h\big(p(x) u''(x)+p'(x)u'(x)\big)+O(h^2).\end{aligned}

Það gefur skekkjumatið :math:`S_Nu(h)=O(h^2)` sem bætir
:math:`o(h)`-matið hér að framan.

Samantekt á mismunaaðferð með heildun yfir hlutbil
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum nú farið í gegnum útfærslu á mismunaaðferð með heildun yfir
hlutbil til þess að finna nálgun á lausn :math:`u(x)` á
(:ref:`Link title <eq:21.1.1>`). Við reiknum út nálgunarfall
:math:`v=c_0\varphi_0+\cdots+c_N\varphi_N`, þar sem
:math:`\varphi_0,\dots,\varphi_N` eru þúfugrunnföll fyrir skiptingu
:math:`a=x_0<x_1<\cdots<x_N=b` á bilinu :math:`[a,b]`, sem má velja
hvernig sem er, og stuðlarnir :math:`c_j` eru lausn á ákveðnu línulegu
jöfnuhneppi, sem við leiddum út frá afleiðujöfnunni og jaðarskilyrðunum.
Útleiðslan miðast við að við fengjum góða nálgun á :math:`u(x_j)` með
:math:`c_j`. Þetta gerðum við með því að heilda jöfnuna sem lausnin
:math:`u` uppfyllir yfir bil milli miðpunkta bilanna sitt hvorum megin
við :math:`x_j`, skipta út afleiðum fyrir mismunakvóta og heildum fyrir
eins punkts nálganir og bjuggum þannig til nálgunarjöfnuhneppi. Við
höfum ekki sannað að nálgunarlausnin :math:`v(x)` stefni á :math:`u(x)`
ef fínleiki skiptingarinnar stefnir á :math:`0`, en við höfum sýnt að
það er samræmi milli :math:`u` og :math:`v` í þeim skilningi að
staðarskekkjurnar mismunasambandanna sem úrlausnin byggir á stefna allar
á :math:`0`.

Mismunaaðferð fyrir hlutafleiðujöfnur
-------------------------------------

Nú tökum við fyrir jaðargildisverkefnið (:ref:`Link title <eq:21.1.3>`) og leiðum út
nálgunarjöfnur í punktum í rétthyrndu neti í plani. Við köllum aðferðina
*heildun yfir hlutsvæði*, en hún er alhæfing á heildun yfir hlutbil sem
við sáum hér fyrr í kaflanum. Það er ákveðin hagræðing í því til þess að
byrja með að skipta jaðrinum í tvö sundurlæg mengi :math:`\partial D=\partial_1D\cup \partial_2 D`, þar sem

.. math::

  \partial_1D=\{(x,y)\in \partial D\,;\, \beta(x,y)=0\}
   \qquad \text{ og } \qquad 
   \partial_2D=\{(x,y)\in \partial D\,;\, \beta(x,y)\neq 0\}.

Í punktum :math:`(x,y)\in \partial_1D` eru gildi lausnarinnar gefin
:math:`u(x,y)=\gamma(x,y)/\alpha(x,y)`, svo við getum eins skipt út
:math:`\gamma` fyrir :math:`\gamma/\alpha` á þessum hluta jaðarsins. Við
skulum því gera ráð fyrir að jaðargildisverkefnið sé

.. math::

  \begin{cases}
       Lu=-\nabla\cdot (p\nabla u)+qu=f, \quad &\text{á } D\\
   u=\gamma,\quad &\text{á } \ \partial_1 D,\\
   \alpha u+\beta\dfrac{\partial u}{\partial n}
   =\gamma, \quad  &\text{á } \ \partial_2 D,
     \end{cases}

Ef :math:`\partial_1D=\partial D`, þá erum við með *Dirichlet
jaðarskilyrði*, sem þýðir að lausnin er þekkt á öllum jaðrinum.

Net
~~~

Hugsum okkur að svæðið :math:`D` sé innihaldið í rétthyrningnum

.. math:: R=\{(x,y)\,;\, a\leq x\leq b, c\leq y\leq d\}.

Tökum nú :math:`h>0` og lítum á rétthyrnda netið með möskvastærðina
:math:`h` gegnum hornpunktinn :math:`(a,c)`, en það hefur hnútpunktana

.. math:: x=a+mh \qquad \text{ og } \qquad y=c+nh, \qquad m,n\in {{\mathbb  Z}}.

Línurnar gegnum hnútpunktana eru stikaðar með

.. math::

  {{\mathbb  R}}\ni t\mapsto (a+mh,t) \qquad \text{ og } \qquad 
   {{\mathbb  R}}\ni s\mapsto (s,c+nh).

Línurnar skera :math:`\overline D =D\cup\partial D` í punktum
:math:`(x_j,y_j)`, :math:`j=1,\dots,M`, sem er raðað þannig að punktar
númer :math:`1` til :math:`N\leq M` eru í :math:`D\cup \partial_2 D`,
þar sem fallgildi :math:`u` eru óþekkt, en :math:`(x_j,y_j)` fyrir
:math:`j=N+1,\dots,M` eru þá punktarnir í :math:`\partial_1 D`, þar sem
fallgildi :math:`u` eru þekkt.

.. figure:: ./myndir/fig2201.svg
    :align: center
    :alt: Svæðið :math:`D`. Teiknið inn netið og merkið punktana :math:`(x_j,y_j)`!

    Mynd: Svæðið :math:`D`. Teiknið inn netið og merkið punktana :math:`(x_j,y_j)`!

Heildun yfir hlutsvæði
~~~~~~~~~~~~~~~~~~~~~~

Sundurleitnisetningin, sem einnig er nefnd Gauss-setning, segir að

.. math::

  \iint_\Omega\nabla\cdot  {\mathbf  V} \, dA
   =\int_{\partial \Omega} {\mathbf V} \cdot {\mathbf  n}\, ds,

fyrir sérhvert samfellt deildanlegt vigursvið :math:`\mathbf V` sem
skilgreint er í grennd um :math:`\overline \Omega`. Gera þarf ráð fyrir
að jaðarinn :math:`\partial\Omega` hafi samfelldan ytri þvervigur alls
staðar nema í endanlega mörgum punktum. Sundurleitnisetningin gildir
þannig á öllum þríhyrningum og ferhyrningum, en það eru svæðin sem við
heildum einkum yfir. Hér táknar :math:`dA=dxdy` flatarmálsfrymið í
:math:`{{\mathbb  R}}^2` og :math:`ds` bogalengdarfrymið á jaðrinum
:math:`\partial \Omega`.

Í sértilfellinu :math:`{\mathbf V}=p\nabla u` er

.. math::

  \nabla\cdot \big( p \nabla u\big)=
   \dfrac{\partial}{\partial x}\bigg(p\dfrac{\partial u}{\partial x}\bigg)
   +\dfrac{\partial}{\partial y}\bigg(p\dfrac{\partial u}{\partial y}\bigg)

og þá gildir

.. math::

  \iint_\Omega \nabla\cdot\big(p\nabla u\big) \, dxdy
   =\int_{\partial\Omega} p\dfrac{\partial u}{\partial n}\, ds

um sérhvert tvisvar samfellt deildanlegt fall :math:`u`. Lausn
hlutafleiðujöfnunnar uppfyllir því

.. math::

  -\int_{\partial\Omega } p\dfrac{\partial u}{\partial n}\, ds
   +\iint_\Omega qu\, dxdy =\iint_\Omega f\, dxdy

ef við gerum ráð fyrir að :math:`\Omega\subset D`.

Nú skiptum við svæðinu :math:`D` skipulega í hlutsvæði og notum þessi
heildi til þess að leiða út nálgunarjöfnur fyrir gildi lausnarinnar
:math:`u(x_j,y_j)` í punktunum :math:`(x_j,y_j)`. Tilsvarandi
nálgunargildi táknum við með :math:`c_j`, :math:`j=1,\dots,N` og við
setjum

.. math:: c_j=u(x_j,y_j)=\gamma(x_j,y_j)=\gamma_j, \qquad j=N+1,\dots,M,

í punktunum þar sem gildi lausnarinnar eru gefin.

Nálgunarjafna í innri punkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./myndir/fig2201a.svg
    :align: center
    :alt: Innri punktur

    Mynd: Innri punktur

Gerum nú ráð fyrir að :math:`(x_j,y_j)` sé innri punktur í :math:`D` og
að grannar hans eftir netlínunum séu allir hnútpunktar í netinu. Látum
:math:`\Omega_j` vera ferninginn með miðju í :math:`(x_j,y_j)` og
kantlengdina :math:`h`. Látum granna :math:`(x_j,y_j)` eftir netlínunum
vera :math:`(x_l,y_l)`, :math:`(x_r,y_r)`, :math:`(x_s,y_s)` og
:math:`(x_t,y_t)`, eins og myndin sýnir, :math:`m_{j,k}` vera miðpunkt
striksins milli :math:`(x_j,y_j)` og :math:`(x_k,y_k)` og
:math:`S_{j,k}` vera þann kant á :math:`\Omega_j` sem næstur er
:math:`(x_k,y_k)` fyrir :math:`k=l,r,s,t`. Þá er

.. math::

  \int_{\partial \Omega_j} p\dfrac{\partial u}{\partial n}\, ds
   =\sum_{k=l,r,s,t} \int_{S_{j,k}} p\dfrac{\partial u}{\partial n}\, ds.

Heildið yfir strikið :math:`S_{j,k}` er nálgað með margfeldi af gildi
heildisstofnsins í miðpunkti striksins og lengd þess,

.. math::

  \int_{S_{j,k}}p\dfrac{\partial u}{\partial n} \, ds
   \approx p(m_{j,k})\dfrac{\partial u}{\partial n}(m_{j,k}) h
   \approx p(m_{j,k})\dfrac{u(x_k,y_k)-u(x_j,y_j)}{h} h.

Flatarheildin í jöfnu (:ref:`Link title <eq:21.5.2>`) með :math:`\Omega_j` í
hlutverki :math:`\Omega` eru nálguð með miðpunktsreglu þannig að gildi
heildisins er nálgað með margfeldi af gildi heildisstofnsins í
miðpunktinum :math:`(x_j,y_j)` og flatarmáli :math:`\Omega_j`,

.. math::

  \iint_{\Omega_j}q u \, dxdy \approx q(x_j,y_j)u(x_j,y_j)\,  h^2
   \quad \text{ og } \quad
   \iint_{\Omega_j}f \, dxdy \approx f(x_j,y_j)\,  h^2.

Til styttingar á formúlunum setjum við nú :math:`u_k=u(x_k,y_k)`,
:math:`q_k=q(x_k,y_k)`, :math:`f_k=f(x_k,y_k)` og
:math:`p_{j,k}=p(m_{j,k})`. Nálgunarjafnan fyrir (:ref:`Link title <eq:21.5.2>`) með
:math:`\Omega=\Omega_j` verður því

.. math::

  -p_{j,l}(u_l-u_j)
   -p_{j,r}(u_r-u_j)
   -p_{j,s}(u_s-u_j)
   -p_{j,t}(u_t-u_j)
   +q_ju_jh^2\approx f_jh^2.

Nú deilum við öllum liðum með :math:`h^2`, setjum við nálgunargildin
:math:`c_k` inn í stað :math:`u_k` fyrir :math:`k=j,l,r,s,t` og setjum
þetta samband fram með línulegri jöfnu sem nálgunargildin eiga að
uppfylla,

.. math::

  \begin{gathered}
   \big(h^{-2}\big({p_{j,l}+p_{j,r}+p_{j,s}+p_{j,t}}\big)+q_j\big)c_j
   \\
   -h^{-2}p_{j,l}c_l
   -h^{-2}p_{j,r}c_r
   -h^{-2}p_{j,s}c_s
   -h^{-2}p_{j,t}c_t
   =f_j.\end{gathered}

Í tilfellinu þegar :math:`p` er fasti, segjum :math:`p=1`, þá fáum við
einfaldari jöfnu

.. math::

  \big(4{h^{-2}}+q_j\big)c_j\\
   -{h^{-2}}c_l
   -{h^{-2}}c_r
   -{h^{-2}}c_s
   -{h^{-2}}c_t
   =f_j.

Punktuppsprettur
~~~~~~~~~~~~~~~~

Í útleiðslunni hér að framan gerum við alltaf ráð fyrir að :math:`f` sé
samfellt fall á :math:`\overline D=D\cup \partial D`. Aðferðin sem við
notum, heildun yfir hlutsvæði, leyfir okkur að bæta punktuppsprettum
:math:`\sum_{s=1}^\mu Q_s\delta_{P_s}` við fallið :math:`f` og líta á
hægri hliðina í hlutafleiðujöfnunni sem
:math:`f+\sum_{s=1}^\mu Q_s\delta_{P_s}`. Hér er
:math:`\delta_{P_s}(x,y)` Dirac-fall í punktinum
:math:`P_s=(\xi_s,\eta_s)`. Við gerum ráð fyrir að þetta séu ólíkir
punktar og að skipting okkar í hlutsvæði sé það fín að í mesta lagi einn
punktur :math:`P_s` geti verið í hverjum rétthyrningi :math:`\Omega_j`.
Í kafla 20 eru Dirac-föllin útskýrð sem veik markgildi af föllum, en það
eina sem við þurfum að vita um þau í þessu samhengi er að

.. math::

  \iint_\Omega \delta_{P_s}(x,y)\, dxdy=
   \begin{cases}
     1,&P_s\in \Omega,\\ 0,&P_s\not\in \Omega.
   \end{cases}

Þegar verið er að útfæra aðferðina með þessu afbrigði af hægri hlið er
athugað hvort einhver punktanna :math:`P_s` liggur í :math:`\Omega_j`.
Ef :math:`P_t` gerir það, þá er

.. math::

  \iint_{\Omega_j}\big(f+\sum_{s=1}^\mu Q_s\delta_{P_s}(x,y)\big) \,
   dxdy  \approx f(x_j,y_j)\,  h^2+Q_t.

Síðan er jafnan stöðluð með því að deila með :math:`h^2` og þá kemur
:math:`b_j=f(x_j,y_j)+Q_t/h^2` í hægri hlið nálgunarjöfnunnar. Í
forritum fyrir aðferðina á rétthyrningi er best að framkvæma þessa
aðgerð í blálokin þegar allt annað í nálgunarjöfnuhneppinu hefur verið
reiknað.

Dirichlet verkefni á rétthyrningi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum nú á :math:`D=\{(x,y)\,;\, 0<x<1, 0<y<1\}` og Dirichlet verkefnið

.. math::

  \begin{cases}
     -\nabla^2u+qu=f,&\text{í } D,\\
   u(x,y)=\gamma(x,y),& (x,y)\in \partial D,
   \end{cases}

Athugið að þetta er tilfellið :math:`p=1`. Ákvörðum línulegt
jöfnuhneppi með mismunaaðferð fyrir gildi lausnarinnar í punktunum
:math:`(\tfrac 13,\tfrac 13)`, :math:`(\tfrac 23,\tfrac 13)`,
:math:`(\tfrac 13,\tfrac 23)`, :math:`(\tfrac 23,\tfrac 23)`.

*Lausn:*  Við númerum þessa punkta í sömu röð :math:`(x_j,y_j)` með
:math:`j=1,2,3,4` og númerum aðra punkta netsins :math:`(x_j,y_j)` með
:math:`j=5,6,\dots,16` eins og myndin sýnir

.. figure:: ./myndir/fig2202.svg
    :align: center
    :alt: Dirichlet-verkefni, númering á punktum og skipting í hlutsvæði

    Mynd: Dirichlet-verkefni, númering á punktum og skipting í hlutsvæði

Nálgunargildin í þeim síðarnefndu eru réttu gildin á jaðrinum,
:math:`c_j=\gamma(x_j,y_j)=\gamma_j`, :math:`j=5,6,\dots,16` og
:math:`h^{-2}=9`. Samkvæmt jöfnu (:ref:`Link title <eq:21.5.4>`) eru jöfnurnar fjórar

.. math::

  \begin{aligned}
     (36+q_1)c_1-9c_2-9c_3-9c_6-9c_9&=f_1,\\
     (36+q_2)c_2-9c_1-9c_4-9c_7-9c_{10}&=f_2,\\
     (36+q_3)c_3-9c_1-9c_4-9c_{11}-9c_{14}&=f_3,\\
     (36+q_4)c_4-9c_2-9c_3-9c_{12}-9c_{15}&=f_4.\\\end{aligned}

Við fáum nálgunargildin með því að leysa jafngilt hneppi,

.. math::

  \left[  \begin{matrix}
   36+q_1&-9&-9& 0\\
   -9&36+q_2&0&-9\\    
   -9&0&36+q_3&-9\\
   0&-9&-9&36+q_4\\
     \end{matrix}\right]
   \left[
     \begin{matrix}
      c_1\\c_2\\c_3\\c_4 
     \end{matrix}
   \right]
   =\left[
     \begin{matrix}
   f_1+9\gamma_6+9\gamma_9,\\
   f_2+9\gamma_7+9\gamma_{10},\\
   f_3+9\gamma_{11}+9\gamma_{14},\\
   f_4+9\gamma_{12}+9\gamma_{15}.\\
     \end{matrix}
   \right].

.. end-toggle::

Blandað jaðarskilyrði
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./myndir/fig2203.svg
    :align: center
    :alt: Jaðarpunktur

    Mynd: Jaðarpunktur

Látum nú :math:`(x_j,y_j)\in \partial_2 D` vera jaðarpunkt, þar sem við
höfum blandað jaðarskilyrði og gerum ráð fyrir að strikið :math:`S_j`
milli miðpunktanna :math:`m_{j,s}` og :math:`m_{j,t}` liggi allt í
:math:`\partial_2 D`. Við táknum strikin milli :math:`(x_j,y_j)` og
hinna punktanna með :math:`S_{j,l}`, :math:`S_{j,s}` og :math:`S_{j,t}`.
Þá er

.. math::

  \int_{\partial \Omega_j} p\dfrac{\partial u}{\partial n}\, ds
   =\sum_{k=l,s,t} \int_{S_{j,k}} p\dfrac{\partial u}{\partial n}\, ds
   +\int_{S_{j}} p\dfrac{\partial u}{\partial n}\, ds.

Nálgunin á vegheildinu á vinstri kantinum verður sú sama og áður,

.. math::

  \int_{S_{j,l}} p\dfrac{\partial u}{\partial n} \, ds
   \approx p_{j,l}\dfrac {u_l-u_j} h h

Efri og neðri kantarnir á :math:`\Omega_j` hafa lengdina
:math:`\tfrac 12 h`, svo nálganir á heildunum yfir þá verða

.. math::

  \int_{S_{j,s}} p\dfrac{\partial u}{\partial n} \, ds
   \approx p_{j,s}\dfrac{u_s-u_j}h\tfrac 12 h 
   \qquad \text{ og }  \qquad 
   \int_{S_{j,t}} p\dfrac{\partial u}{\partial n} \, ds
   \approx p_{j,t}\dfrac{u_t-u_j}h\tfrac 12 h.

Í punktinum :math:`(x_j,y_j)` höfum við jaðarskilyrði

.. math::

  -\dfrac{\partial u}{\partial n}(x_j,y_j)
   =\dfrac{\alpha(x_j,y_j)u(x_j,y_j)-\gamma(x_j,y_j)}{\beta(x_j,y_j)}
   =\dfrac{\alpha_ju_j-\gamma_{j}}{\beta_{j}},

sem gefur nálgunina

.. math::

  -\int_{S_{j}} p\dfrac{\partial u}{\partial n} \, ds
   \approx
   p_j\dfrac{\alpha_ju_j-\gamma_j}{\beta_j} h.

Flatarmál :math:`\Omega_j` er :math:`\tfrac 12 h^2`. Nú er
:math:`(x_j,y_j)` ekki miðpunktur :math:`\Omega_j` heldur jaðarpunktur,
en það breytir því ekki að eðlilegt er að nálga flatarheildin í
(:ref:`Link title <eq:21.5.2>`) fyrir :math:`\Omega=\Omega_j` með

.. math::

  \iint_{\Omega_j} q u\, dxdy
   \approx q_ju_j \tfrac 12 h^2
   \quad \text{ og } \quad
   \iint_{\Omega_j} f\, dxdy
   \approx f_j \tfrac 12 h^2.

Nú röðum við þessu saman í nálgunarjöfnu fyrir (:ref:`Link title <eq:21.5.2>`) með
:math:`\Omega_j` í hlutverki :math:`\Omega`,

.. math::

  -p_{j,l}(u_l-u_j)-\tfrac 12p_{j,s}(u_s-u_j)-\tfrac 12p_{j,t}(u_t-u_j)
   +p_j\dfrac{\alpha_ju_j-\gamma_j}{\beta_j} h
   +\tfrac 12 h^2 q_ju_j\approx \tfrac 12 h^2 f_j.

Nú skiptum við út :math:`u_k` í staðinn fyrir :math:`c_k` fyrir
:math:`k=j,l,s,t`, deilum öllum liðum með :math:`\tfrac 12 h^2` og fáum
jöfnu fyrir nálgunargildin

.. math::

  -2h^{-2}p_{j,l}(c_l-c_j)-h^{-2}p_{j,s}(c_s-c_j)-h^{-2}p_{j,t}(c_t-c_j)
   +2h^{-1}p_j\dfrac{\alpha_jc_j-\gamma_j}{\beta_j}
   +q_jc_j = f_j.

Að lokum tökum við saman liðina í jöfnuna

.. math::

  \begin{gathered}
    \label{eq:21.5.5}
   \big(2h^{-2}p_{j,l}+h^{-2}p_{j,s}+h^{-2}p_{j,t}
   +2h^{-1}p_j\tfrac{\alpha_j}{\beta_j}+q_j\big)c_j
   \\
   -2h^{-2}p_{j,l}c_l-h^{-2}p_{j,s}c_s-h^{-2}p_{j,t}c_t
   =f_j+2h^{-1}p_j\tfrac{\gamma_j}{\beta_j}.\end{gathered}

Það er þess virði að skrifa sérstaklega upp tilfellið þegar
:math:`p=1`,

.. math::

  \big(4h^{-2}
   +q_j+2h^{-1}\tfrac{\alpha_j}{\beta_j}\big)c_j
   -2h^{-2}c_l-h^{-2}c_s-h^{-2}c_t
   =f_j+2h^{-1}\tfrac{\gamma_j}{\beta_j}

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Breytum nú jaðargildisverkefninu í sýnidæmi :ref:`Link title <sy:22.2.1>` þannig að
við höfum blandað jaðarskilyrði á hægri kantinum,

.. math::

  \begin{cases}
     -\nabla^2u+qu=f,&\text{í } D,\\
   u(x,y)=\gamma(x,y),& (x,y)\in \partial_1 D,\\
   \alpha(x,y)u(x,y)+\dfrac{\partial u}{\partial n}(x,y)
   =\gamma(x,y),& (x,y)\in \partial_2 D,
   \end{cases}

Þar sem :math:`\partial_1D` er sammengi þriggja kanta á rétthyrningnum
:math:`D`, þar sem :math:`y=0`, :math:`x=0` og :math:`y=1`, og
:math:`\partial_2D` er hægri kanturinn þar sem :math:`x=1`. Ákvörðum
línulegt jöfnuhneppi með mismunaaðferð fyrir gildi lausnarinnar í
:math:`(\tfrac 13,\tfrac 13)`, :math:`(\tfrac 23,\tfrac 13)`,
:math:`(1,\tfrac 13)`, :math:`(\tfrac 13,\tfrac 23)`,
:math:`(\tfrac 23,\tfrac 23)` og :math:`(1,\tfrac 23)`.

.. figure:: ./myndir/fig2204.svg
    :align: center
    :alt: Blandað jaðarskilyrði á hægri kanti, númering á punktum og skipting í hlutsvæði

    Mynd: Blandað jaðarskilyrði á hægri kanti, númering á punktum og skipting í hlutsvæði

*Lausn:*  Hér erum við aðeins að einfalda okkur lífið með því að setja
:math:`\beta=1` á :math:`\partial_2D`. Við erum með 6 punkta
:math:`(x_j,y_j)` með :math:`j=1,2,\dots,6`, þar sem gildin eru óþekkt.
Nálgunargildin í hinum punktunum :math:`(x_j,y_j)` með
:math:`j=7,8,\dots,16` eru gefin

.. math:: c_j=u(x_j,y_j)=\gamma(x_j,y_j)=\gamma_j, \qquad j=7,8,\dots,16.

Við fylgjum jöfnu (:ref:`Link title <eq:21.5.4>`) fyrir punkta númer
:math:`j=1,2,4,5` en jöfnu (:ref:`Link title <eq:21.5.6>`) fyrir punkta
:math:`j=3,6`. Þá er línulega jöfnuhneppið

.. math::

  \begin{aligned}
     (36+q_1)c_1-9c_2-9c_4-9c_8-9c_{11}&=f_1,\\
     (36+q_2)c_2-9c_1-9c_3-9c_5-9c_{9}&=f_2,\\
     (36+q_3+6\alpha_3)c_3-18c_2-9c_6-9c_{10}&=f_3+6\gamma_3,\\
     (36+q_4)c_4-9c_1-9c_5-9c_{12}-9c_{14}&=f_4.\\
     (36+q_5)c_5-9c_2-9c_4-9c_{6}-9c_{15}&=f_5.\\
     (36+q_6+6\alpha_6)c_6-9c_3-18c_{5}-9c_{16}&=f_6+6\gamma_6.\\\end{aligned}

Við fáum nálgunargildin með því að leysa jafngilt hneppi,

.. math::

  \begin{gathered}
   \left[  \begin{matrix}
   36+q_1&-9&0&-9& 0& 0\\
   -9&36+q_2&-9&0&-9&0\\    
   0&-18&36+q_3+6\alpha_3&0&0&-9\\
   -9&0&0&36+q_4&-9&0\\
   0&-9&0&-9&36+q_5&-9\\
   0&0&-9&0&-18&36+q_6+6\alpha_6\\
     \end{matrix}\right]
   \left[
     \begin{matrix}
      c_1\\c_2\\c_3\\c_4 \\ c_5 \\ c_6
     \end{matrix}
   \right]\\
   =\left[
     \begin{matrix}
   f_1+9\gamma_8+9\gamma_{11}\\
   f_2+9\gamma_{9}\\
   f_3+9\gamma_{10}+6\gamma_3\\
   f_4+9\gamma_{12}+9\gamma_{14}\\
   f_5+9\gamma_{15}\\
   f_6+9\gamma_{16}+6\gamma_6\\
     \end{matrix}
   \right].\end{gathered}

.. end-toggle::

Mismunaaðferðin hentar lang best þegar hlutafleiðujafnan er leyst á
rétthyrningi og allir punktarnir :math:`(x_j,y_j)`,
:math:`j=1,2,\dots,M`, eru hnútpunktar netsins. Það er alveg
vandræðalaust að setja upp nálgunarjöfnuhneppi á svæðum sem hafa aðra
lögun, til dæmis á marghyrningum.

Jaðargildisverkefni á þríhyrningi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Breytum nú svæðinu í sýnidæmi :ref:`Link title <sy:22.2.2>` í þríhyrning,

.. math:: D=\{(x,y)\,;\, 0<y<1-x\}

og setjum blandað jaðarskilyrði á langhliðina. Þá er :math:`\partial_1D`
sammengi skammhliða þríhyrningsins og :math:`\partial_2D` er langhliðin,

.. math::

  \begin{cases}
     -\nabla^2u+qu=f,&\text{í } D,\\
   u(x,y)=\gamma(x,y),& (x,y)\in \partial_1 D,\\
   \alpha(x,y)u(x,y)+\dfrac{\partial u}{\partial n}(x,y)
   =\gamma(x,y),& (x,y)\in \partial_2 D,
   \end{cases}

Nú ætlum við að setja upp nálgunarjöfnuhneppi fyrir þrjá punkta
:math:`(\tfrac 13,\tfrac 13)`, :math:`(\tfrac 23,\tfrac 13)` og
:math:`(\tfrac 13,\tfrac 23)`.

.. figure:: ./myndir/fig2205.svg
    :align: center
    :alt: Jaðargildisverkefni á þríhyrningi, númering á punktum og skipting í hlutsvæði

    Mynd: Jaðargildisverkefni á þríhyrningi, númering á punktum og skipting í hlutsvæði

*Lausn:* Myndin sýnir uppröðun punktanna og hlutsvæðin sem við notum við
að leiða út jöfnurnar. Við setjum :math:`c_j=\gamma(x_j,y_j)=\gamma_j`,
:math:`j=4,\dots,10`. Fyrsti punkturinn er innri punktur og við vitum
hvernig nálgunarjafnan sem svarar til hans er leidd út,

.. math:: (36+q_1)c_1-9c_2-9c_3=f_1+9\gamma_5+9\gamma_8.

Fyrir :math:`j=2,3` er lengd skástriksins :math:`S_j` í
:math:`\partial\Omega_j` jöfn :math:`\sqrt 2\, h` og jaðarskilyrðið er

.. math::

  -\dfrac{\partial u}{\partial n}(x_j,y_j)=
   \alpha(x_j,y_j)u(x_j,y_j)-\gamma(x_j,y_j)
   =\alpha_ju_j-\gamma_j,

og því gefur miðpunktsnálgun á heildinu yfir :math:`S_j`

.. math::

  -\int_{S_j} p\dfrac{\partial u}{\partial n}\, ds
   \approx \big(\alpha_ju_j-\gamma_j\big) \sqrt 2 \, h.

Flatarmál þríhyrninganna :math:`\Omega_j` er :math:`\tfrac 12 h^2` og
því er eðlilegt að nálga flatarheildin

.. math::

  \iint_{\Omega_j} qu\, dxdy \approx q_ju_j\tfrac 12 h^2
   \qquad \text{ og } \qquad 
   \iint_{\Omega_j} f\, dxdy \approx f_j\tfrac 12 h^2

Eftir að hafa deilt öllum liðum í nálgunarjöfnunum með
:math:`\tfrac 12 h^2` og sett :math:`c_j` í stað :math:`u_j` fáum við

.. math::

  \begin{aligned}
     2\sqrt 2 h^{-1}\big(\alpha_2c_2-\gamma_2  \big)
   -2h^{-2}(c_1-c_2)-2h^{-2}(c_6-c_2)+q_2c_2=f_2,\\
     2\sqrt 2 h^{-1}\big(\alpha_3c_3-\gamma_3  \big)
   -2h^{-2}(c_1-c_3)-2h^{-2}(c_9-c_3)+q_3c_3=f_3.\end{aligned}

Nú setjum við inn :math:`h=\tfrac 13` og röðum liðunum jöfnuhneppi sem
við setjum

.. math::

  \left[  \begin{matrix}
   36+q_1&-9&-9\\
   -18&36+q_2+6\sqrt 2 \alpha_2&0\\    
   -18& 0&36+q_3+6\sqrt 2  \alpha_3\\
     \end{matrix}\right]
   \left[
     \begin{matrix}
      c_1\\c_2\\c_3
     \end{matrix}
   \right]\\
   =\left[
     \begin{matrix}
   f_1+9\gamma_5+9\gamma_8\\
   f_2+18\gamma_6+6\sqrt 2\gamma_2\\
   f_3+18\gamma_{9}+6\sqrt 2\gamma_3\\
     \end{matrix}
   \right].

.. end-toggle::

Almenn mismunaaðferð á rétthyrningi
-----------------------------------

Við látum nú :math:`D = \  ]a,b[\times ]c,d[ \  = \{(x,y)\, ;\, a<x<b, c<y<d\}` tákna rétthyrning í planinu
:math:`{{\mathbb  R}}^2` með hliðar samsíða ásunum. Við ætlum að líta á
almennt jaðargildisverkefni

.. math::

  \begin{cases}
     -\nabla\cdot\big(p\nabla u\big)+qu=f, &\text{í } D,\\
   \alpha  u + \beta \dfrac{\partial u}{\partial n} = \gamma,&
   \text{á } \partial D,
     \end{cases}

hugsa okkur að föllin :math:`\alpha`, :math:`\beta` og :math:`\gamma`
séu gefin á öllum jaðrinum, þannig að í þeim felist bæði
Dirichlet-jaðarskilyrði og blönduð jaðarskilyrði. Við gerum því ráð
fyrir að í jaðarpunktum :math:`(x,y)`, þar sem :math:`\beta(x,y)=0`
gildi :math:`\alpha(x,y)\neq 0` og að þar með sé gildið
:math:`u(x,y)=\gamma(x,y)/\alpha(x,y)`.

Á hornunum er ytri þvervigurinn :math:`\mathbf n` ekki skilgreindur. Þar
má leyfa föllunum :math:`\alpha`, :math:`\beta` og :math:`\gamma` að
vera ósamfelldum. Til þess að nálga vegheildi yfir tvö línustrik sem
liggja að hornunum þá tökum við bara gildi á :math:`\alpha`,
:math:`\beta` og :math:`\gamma` í miðpunktum strikanna sitt hvorum
megin.

Við verðum að velja tölurnar :math:`a,b,c` og :math:`d` þannig að hægt
sé að skipta :math:`D` í reglulegt net með kantlengdina :math:`h`. Þetta
þýðir að :math:`N=(b-a)/h` og :math:`M=(d-c)/h` verði heilar tölur. Til
þess að leysa þetta verkefni verðum við að hafa þrjú hnitakerfi í
kollinum samtímis og við verðum að hafa rithátt yfir þau öll:

(1) **Hnit netpunkta í** :math:`(x,y)`-**plani:**   Við erum bundin af því
að matlab leyfir okkur ekki að númera stök vigra frá :math:`0`, svo við
skulum láta :math:`\ell=N+1` tákna fjölda punkta í hverri línu og
skilgreina skiptinguna :math:`a=x_1<x_2<\cdots<x_\ell=b`, þannig að
:math:`x_j=a+(j-1)h`, :math:`j=1,\dots,\ell`. Ef við látum :math:`m=M+1`
tákna fjölda lína þá er skiptingin :math:`c=y_1<y_2<\cdots<y_m=d` með
:math:`y_k=c+(k-1)h`, :math:`k=1,\dots,m`. Heildarfjöldi netpunkta er
:math:`n=\ell\cdot m=(N+1)(M+1)`.

(2) **Tvívíð númering netpunkta** :math:`(j,k)` **:**  Hér eru :math:`j` og
:math:`k` heiltölur með :math:`1\leq j\leq \ell` og
:math:`1\leq k\leq m`.

(3) **Einföld númering netpunkta** :math:`i` **:**   Við setjum einfalda
númeringu á alla punkta netsins þannig að tvívíða númerið :math:`(j,k)`
gefi :math:`i=j+(k-1)\ell`, þ.e.a.s. við númerum punktana eftir láréttu
línunum frá vinstri til hægri, byrjum neðst og förum upp. Öfugt, ef
gefin er talan :math:`i`, þá þurfum við að geta reiknað út
:math:`(j,k)`. Ef :math:`\ell=N+1` gengur upp í :math:`i`, þá er
:math:`j=\ell` og :math:`k=i/\ell`. Ef hins vegar :math:`\ell` gengur
ekki upp í :math:`i` þá er :math:`j` afgangurinn af :math:`i` eftir
deilingu með :math:`\ell`, :math:`j= i\mod \ell`, og
:math:`k=1+\lfloor i/\ell\rfloor`, þar sem :math:`\lfloor t \rfloor` er
stærsta heiltala :math:`\leq t`. Ég mæli með því að þið notið matlab
skipanirnar floor, sem gefur heiltöluhlutann af rauntölu og mod sem
gefur afgang við heiltöludeilingu, til þess að búa til fall fyrir þennan
útreikning, því þið þurfið oft á honum að halda.

Uppbygging forrits
~~~~~~~~~~~~~~~~~~

Veigmesti hluti forrits til þess að finna nálgun á (:ref:`Link title <eq:21.6.1>`) er
úrreikningur á :math:`n\times n` jöfnuhneppi
:math:`A{\mathbf c}={\mathbf b}` þar sem stakið :math:`c_i` í
lausnarvigrinum :math:`{\mathbf c}` er nálgunargildi fyrir
:math:`u(x_j,y_k)`. Það er margt sem þarf að skoða:

Innri punktar:
^^^^^^^^^^^^^^

Lítum fyrst á punkt :math:`(x_j,y_j)` í netinu með númerið :math:`i` þar
sem :math:`1<j<\ell` og :math:`1<k<m`. Einu stökin í :math:`A` í línu
:math:`i` sem eru frábrugðin :math:`0` eru fimm talsins
:math:`a_{i,i-\ell}`, :math:`a_{i,i-1}`, :math:`a_{i,i+1}`,
:math:`a_{i,i+\ell}` og :math:`a_{i,i}` og gildi þeirra eru lesin út úr
jöfnu (:ref:`Link title <eq:21.5.5>`). Í hægri hliðinni stendur
:math:`b_i=f_i=f(x_j,y_k)`.

.. figure:: ./myndir/fig2201b.svg
    :align: center
    :alt: Innri punktur

    Mynd: Innri punktur


Innri punktar á jöðrum:
^^^^^^^^^^^^^^^^^^^^^^^


Við lítum nú á punktana á jaðrinum
:math:`\partial D` sem eru ekki hornpunktar, segjum að við tökum punkt á
hægri jaðri eins og myndin sýnir. Ef :math:`\beta(x_j,y_k)=0`, þá er
fallsjaðarskilyrði og jafnan í punktinum :math:`i` verður

.. math:: c_i=\gamma(x_j,y_k)/\alpha(x_j,y_k).

Eina stakið í línu :math:`i` í :math:`A` sem er frábrugðið :math:`0` er
:math:`a_{i,i}=1` og í hægri hliðinni stendur
:math:`b_i=\gamma(x_j,y_k)/\alpha(x_j,y_k).` Ef hins vegar
:math:`\beta(x_j,y_k))\neq 0`, þá er það jafna (:ref:`Link title <eq:21.5.5>`) sem
gildir með (:math:`\alpha_2=\alpha`, :math:`\beta_2=\beta` og
:math:`\gamma_2=\gamma`). Eins er farið að við punktana á hinum
köntunum.

.. figure:: ./myndir/fig2203b.svg
    :align: center
    :alt: Innri punktur á jaðri

    Mynd: Innri punktur á jaðri

Hornpunktar:
^^^^^^^^^^^^

Byrja þarf á því að athuga hvort
:math:`\beta(x_j,y_k) = 0` til þess að sjá út hvort fallgildið er gefið
í punktinum. Ef svo er þá eru stuðlarnir settir inn í fylkið eins og í
síðasta lið. Ef hins vegar :math:`\beta(x_j,y_k)\neq 0`, þá þarf að
skrifa upp mismunajöfnur og taka tillit til þess að þarna geta föllin
:math:`\alpha`, :math:`\beta` og :math:`\gamma` verið ósamfelld. Gerið
grein fyrir því hvernig jöfnurnar eru leiddar út í öllum fjórum
hornpunktunum með skýringarmyndum.

Punktuppsprettur:
^^^^^^^^^^^^^^^^^

Við viljum leyfa að hægri hlið jöfnunnar hafi
punktuppsprettur í nokkrum punktum. Það gerum við með því að skipta á
:math:`f` og :math:`f+\sum_{s=1}^\mu Q_s \delta_{(\xi_s,\eta_s)}`, þar
sem :math:`\delta_{(\xi_s,\eta_s)}` táknar Dirac-delta-fall í punktinum
:math:`(\xi_s,\eta_s)`. Allir þessir punktar þurfa að vera innri
netpunktar, segjum :math:`(x_j,y_k)`. Ef númer hans er :math:`i`, þá á
að setja :math:`b_i=f(x_j,y_k)+h^{-2}Q_s`.

Gefin gildi í einstaka netpunktum:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Auðvelt er að lausnina til þess
að taka ákveðin gildi í nokkrum völdum innri punktum í rétthyrningnum
:math:`R`. Segjum að við höfum einhverja punkta :math:`(z_s,w_s)`,
:math:`s=1,\dots,\mu` og að við viljum að fallið :math:`u` takið gildið
:math:`U_s` í næsta netpunkti við :math:`(z_s,w_s)`. Segjum að hann sé
:math:`(x_j,y_k)` og að númerið sé :math:`i`. Þá setjum við öll stökin í
línu :math:`i` í :math:`A` jöfn :math:`0` nema :math:`a_{i,i}=1`. Í
hægri hliðina setjum við :math:`b_i=U_s`.

Útreikningur á lausn:
^^^^^^^^^^^^^^^^^^^^^

Þegar fylkið :math:`A` hefur verið reiknað út
er rétt að gefa skipununa sparse í Matlab til þess að nýta sér að fylkið
er rýrt (e. *sparse*) og flýta fyrir úrlausn jöfnuhneppisins:
S=sparse(A); c=S\ :math:`\backslash`\ b; Það þarf að ganga á
nágunargildin :math:`i` finna númeringuna :math:`(j,k)` og stinga
nálgunarlausninni inn í fylkið :math:`W` þannig að :math:`W_{jk}=c_i`.
Hér lýkur úrlausnarferlinu.

Teikning á nálgunarlausn:
^^^^^^^^^^^^^^^^^^^^^^^^^

Graf lausninarinnar er teiknað með
surf(x,y,W’) og jafnhæðarlínur hennar með contour(x,y,W’) (Athugið að
hér hefur fylkinu verið bylt til þess að teikningarnar komi rétt út í
:math:`xy`-hnitunum.)

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Lítum á fjögur jaðargildisverkefni af gerðinni (:ref:`Link title <eq:21.1.1>`):

**a)** :math:`[a,b]=[0,1]`, :math:`p(x)=1+x`, :math:`q(x)=x`,
:math:`f(x)=(x+1)(\tfrac 12 x^2+\tfrac 12 x -2)`,
:math:`u(a)=\tfrac 12`, :math:`u'(b)=2`.

**b)** :math:`[a,b]=[-1,1]`, :math:`p(x)=1+e^{-x}`, :math:`q(x)=1+x`,
:math:`f(x)=xe^x`, :math:`u(a)-u'(a)=0`, :math:`u'(b)=e`.

**c)**  :math:`[a,b]=[1,2]`, :math:`p(x)=x`, :math:`q(x)=1/x`,
:math:`f(x)=-2`, :math:`u'(a)=0`, :math:`u(b)-2u'(b)=-2`.

**d)**  :math:`[a,b]=[1,2]`, :math:`p(x)=1/x`, :math:`q(x)=x`,
:math:`f(x)=0`, :math:`u(a)=1/\sqrt e`, :math:`u(b)+2u'(b)=0`.

Staðfestið að jafnan :math:`Lu=-(pu')'+qu=f` sé uppfyllt á :math:`[a,b]`
fyrir gefnu föllin :math:`p`, :math:`q`, :math:`f` og að jaðarskilyrðin
séu uppfyllt í tilfellunum:

**a)** :math:`u(x)=\tfrac 12(1+x)^2`,   **b)** :math:`u(x)=e^x`,  
**c)** :math:`u(x)=x\ln x-x`,   **d)** :math:`u(x)=e^{-\frac 12 x^2}`.

Dæmi
^^^^

**abcd)** Útfærið mismunaaðferðina í grein 21.2 fyrir dæmi **1abcd)**
með :math:`N=3`, og finnið hámarksskekkjuna
:math:`\max_{j=0,\dots,N}|u(x_j)-c_j|`.

Dæmi
^^^^

**abcd)** Útfærið mismunaaðferðina í grein 21.3, heildun yfir hlutbil,
fyrir dæmi **1abcd)** með :math:`N=3`, og finnð hámarksskekkjuna
:math:`\max_{j=0,\dots,N}|u(x_j)-c_j|`.

Dæmi
^^^^

Búið til Matlab forrit sem les inn öll gögnin í jaðargildisverkefninu
(:ref:`Link title <eq:21.1.0>`) ásamt tölunni :math:`N` og ákvarðar nálgunarlausn
samkvæmt jöfnu (:ref:`Link title <eq:21.2.1b>`).

| **abcd)** Prófið forritið á jaðargildisverkefnið í dæmi **1abcd)**
  fyrir :math:`N=2,4,8,16`.
| (i) Teiknið upp nálgunina og réttu lausnina.
| (ii) Reiknið út hámarksskekkjuna
  :math:`\max_{j=0,\dots,N}|u(x_j)-c_j|` fyrir :math:`N=2,4,8,16`.
| (iii) Ef hámarksskekkjan er :math:`O(h)`, þá á að helmingast hún ef
  :math:`N` tvöfaldast. Gerist það?

Dæmi
^^^^

Búið til Matlab forrit sem les inn öll gögnin í jaðargildisverkefninu
(:ref:`Link title <eq:21.1.1>`) ásamt tölunni :math:`N` og ákvarðar nálgunarlausn
samkvæmt jöfnu (:ref:`Link title <eq:21.2.9>`).

| **abcd)** Prófið forritið á jaðargildisverkefnið í dæmi **1abcd)**
  fyrir :math:`N=2,4,8,16`.
| (i) Teiknið upp nálgunina og réttu lausnina.
| (ii) Reiknið út hámarksskekkjuna
  :math:`\max_{j=0,\dots,N}|u(x_j)-c_j|` fyrir :math:`N=2,4,8,16`.
| (iii) Ef hámarksskekkjan er :math:`O(h^2)`, þá á fjórðungast hún
  nokkurn veginn ef :math:`N` tvöfaldast. Gerist það?

Dæmi
^^^^

Látum :math:`\chi` vera fall á :math:`]0,\delta[`, :math:`\delta>0`,
:math:`0<j<k`. Sýnið:

\(i)  Ef :math:`\chi(h)=O(h^k)`, þá er :math:`\chi(h)=o(h^j)`.

\(ii) Ef :math:`\chi(h)=O(h^k)`, þá er :math:`\chi(h)/h^j=O(h^{k-j})`.

\(iii)  Ef :math:`\chi(h)=o(h^k)`, þá er :math:`\chi(h)/h^j=o(h^{k-j})`.

Dæmi
^^^^

Látum :math:`\chi_1` og :math:`\chi_2` vera föll á :math:`]0,\delta[`,
:math:`\delta>0`, :math:`k_1>0` og :math:`k_2>0`. Sýnið:

\(i)  Ef :math:`\chi_1(h)=o(h^{k_1})` og :math:`\chi_2(h)=O(h^{k_2})`, þá
er :math:`\chi_1(h)\chi_2(h)=o(h^{k_1+k_2})`.

\(ii)  Ef :math:`\chi_1(h)=o(h^{k_1})` og :math:`\chi_2(h)=o(h^{k_2})`,
þá er :math:`\chi_1(h)+\chi_2(h)=o(h^{\min\{k_1,k_2\}})`.

Dæmi
^^^^

Sýnið: Ef :math:`p\in C^2[a,b]` og :math:`u\in C^3[a,b]`, þá er
:math:`S_0u=O(h^2)`.

Dæmi
^^^^

Sýnið síðan að ekki fáist betri staðarskekkja en :math:`S_ju(h)=O(h^2)`,
þótt við gefum okkur að :math:`p\in C^3[a,b]` og :math:`u\in C^5[a,b]`
og liðum þessi föll í Taylor-liðanir

.. math::

  \begin{aligned}
     u(x+h)&=u(x)+u'(x)h+\tfrac 12 u''(x)h^2+\tfrac 16 u'''(x)h^3+
   \tfrac 1{24}u^{(iv)}(x)h^4+O(h^5),\\
     p(x+h)&=p(x)+p'(x)h+\tfrac 12 p''(x)h^2+O(h^3).\end{aligned}

Dæmi
^^^^

Látum :math:`D=\{(x,y) \,;\, a<x<b, c<y<d\}` og lítum á
Dirichlet-verkefnið

.. math::

  \begin{cases}
    -\nabla\cdot\big(p\nabla u\big)+qu=f& \text{á } D,\\
   u=\gamma,&  \text{á } \partial D.
   \end{cases}

**a)**  :math:`a=c=0`, :math:`b=d=1`, :math:`p=1`, :math:`q=0`,
:math:`f=0`, :math:`\gamma(0,y)=y/(1+y^2)`,
:math:`\gamma(1,y)=y/(4+y^2)`, :math:`\gamma(x,0)=0` og
:math:`\gamma(x,1)=1/(2+2x+x^2)`.

**b)**  :math:`a=c=0`, :math:`b=d=1`, :math:`p=1`, :math:`q=0`,
:math:`f=x^2+y^2`, :math:`\gamma(0,y)=\gamma(x,0)=0`,
:math:`\gamma(1,y)=-\tfrac 12y^2` og :math:`\gamma(x,1)=-\tfrac 12 x^2`.

**c)**  :math:`a=1` :math:`b=2`, :math:`c=0`, :math:`d=1`, :math:`p=1`,
:math:`q=0`, :math:`f=0`, :math:`\gamma(1,y)=\ln(y^2+1)`,
:math:`\gamma(2,y)=\ln(y^2+4)`, :math:`\gamma(x,0)=2\ln x` og
:math:`\gamma(x,1)=\ln(x^2+1)`.

**d)**   :math:`a=c=-1`, :math:`b=d=1`, :math:`p=1`, :math:`q=-52`,
:math:`f=0`, :math:`\gamma(-1,y)=\cos(6y-4)`,
:math:`\gamma(1,y)=\cos(6y+4)`, :math:`\gamma(x,-1)=\cos(4x-6)` og
:math:`\gamma(x,1)=\cos(4x+6)`.

Staðfestið að fallið :math:`u` sé lausnir verkefnisins: **a)**
:math:`u(x,y)=\tfrac y{(x+1)^2+y^2}`, **b)**
:math:`u(x,y)=-\tfrac 12(xy)^2`, **c)** :math:`u(x,y)=\ln(x^2+y^2)`,
**d)** :math:`u(x,y)=\cos(4x+6y)`.

Dæmi
^^^^

**abcd)** Lítum á Dirichlet-verkefnin í síðasta dæmi.

\(i) Beitið aðferðinni heildun yfir hlutbil til þess að leiða út
nálgunarjöfnur fyrir nálgunargildi :math:`c_1,\dots,c_4` í fjórum innri
punktum rétthyrningsins, eins og gert er í grein 21.5.

\(ii) Leysið jöfnurnar og berið nálgunina saman við réttu lausnina.

Dæmi
^^^^

Búið til Matlab-forrit sem les inn gögnin sem gefin eru í almenna
Dirichlet-verkefninu í dæmi 10 ásamt kantlengdinni :math:`h` og
skilar út nálgunarlausn. Athugið að talan :math:`h` þarf að vera valin
þannig að hún sé sameiginleg billengd í skiptingum á bilunum
:math:`[a,b]` og :math:`[c,d]`. Hér er átt við að það þarf að sjá til
þess að til séu náttúrlegar tölur :math:`m` og :math:`n` þannig að
:math:`h=(b-a)/m =(d-c)/n`.

**abcd)** Prófið forritið á gögnunum í næst síðasta dæmi. Notið réttu
lausnirnar til þess að reikna út hámarksskekkju með :math:`m=n=3`.

Dæmi
^^^^

Notið forritið úr síðasta dæmi til þess að kanna hvort skekkjan í
reikningunum í síðasta dæmi er :math:`O(h^2)` með því að keyra nokkrar
keyrslur og helminga kantlengdina í hvert skipti.

Dæmi
^^^^

**abcd)** (i) Sýnið að föllin :math:`u(x,y)` í dæmi 10 séu lausnir á
jaðargildisverkefnunum.

\(ii) Lesið út hvernig föllin :math:`\alpha`, :math:`\beta` og
:math:`\gamma` eru skilgreind í hverju tilfelli fyrir sig.

**a)** 
:math:`\begin{cases}
\nabla^2 u=0, \quad \text{á } D=\{(x,y)\,;\, 0<x<1,0<y<1\},\\ 
u(x,0)=0, \quad 2 u(x,1)+(x^2+2x+2)\partial_yu(x,1)=1,&0<x<1,\\
u(0,y)=\tfrac y{y^2+1}, \quad 
\partial_xu(1,y)=-\tfrac{4y}{(y^2+4)^2},& 0<y<1.
\end{cases}`

**b)** 
:math:`\begin{cases}
-\nabla^2 u=x^2+y^2, \quad \text{á } D=\{(x,y)\,;\, 0<x<1,0<y<1\},\\ 
\partial_yu(x,0)=0, \quad -2u(x,1)+\partial_yu(x,1)=0,&0<x<1,\\
u(0,y)=0, \quad u(1,y)=-\tfrac 12 y^2,& 0<y<1.
\end{cases}`

**c)** 
:math:`\begin{cases}
\nabla^2 u=0, \quad \text{á } D=\{(x,y)\,;\, 1<x<2,0<y<1\},\\ 
\partial_yu(x,0)=0, \quad u(x,1)=\ln(x^2+1), &1<x<2,\\
\partial_xu(1,y)=\tfrac y{y^2+1}, \quad 
u(2,y)=\ln(y^2+4),& 0<y<1.
\end{cases}`

**d)** 
:math:`\begin{cases}
-\nabla^2 u-52u=0, \quad \text{á } D=\{(x,y)\,;\, -1<x<1,-1<y<1\},\\ 
\partial_yu(x,-1)=-6\sin(4x-6), \quad u(x,1)=\cos(4x+6), &-1<x<1,\\
u(-1,y)=\cos(6y-4), \quad 
u(1,y)=\cos(6x+4),& -1<y<1.
\end{cases}`

Dæmi
^^^^

\(i) Beitið heildun yfir hlutbil til þess leiða út nálgunarjöfnuhneppi
fyrir jaðargildisverkefnin sem gefin eru í síðasta dæmi í punktunum sem
gefnir eru.

\(ii) Reiknið út nálgunargildin og berið þau saman við rétta lausn.

**a)**  :math:`(\tfrac 12,\tfrac 12)`, :math:`(1,\tfrac 12)`,
:math:`(\tfrac 12,1)` og :math:`(1,1)`.

**b)**  :math:`(\tfrac 12,0)`, :math:`(\tfrac 12,\tfrac 12)` og
:math:`(\tfrac 12,1)`.

**c)**  :math:`(1,0)`, :math:`(\tfrac 32,0)`, :math:`(1,\tfrac 12)` og
:math:`(\tfrac 32,\tfrac 12)`.

**d)**  :math:`(-\tfrac 13,-1)`, :math:`(\tfrac 13,-1)`,
:math:`(-\tfrac 13,\tfrac 13)`, :math:`(\tfrac 13,\tfrac 13)`,
:math:`(-\tfrac 13,1)` og :math:`(\tfrac 13,1)`.

Dæmi
^^^^

Við lítum á þríhyrningssvæðið :math:`D=\{(x,y) \,;\, 0<y<1-x, 0<x<1 \}`
og eftirfarandi jaðargildisverkefni á því:

.. math::   \begin{cases}
    -\nabla^2u+u=1,&\text{á } D,\\
  u(x,0)=1-x,&0<x<1,\\
  u(0,y)=1-y,&0<y<1,\\
  (1+x) u(x,1-x)+\dfrac{\partial u}{\partial n}(x,1-x)=xy,&
  0<x<1.
  \end{cases}

.. figure:: ./myndir/fig2207.svg
    :align: center
    :alt: Skipting á þríhyrningasvæði

    Mynd: Skipting á þríhyrningasvæði

\(i) Veljið punkta :math:`(x_1,y_1),\dots,(x_{10},y_{10})` og hlutsvæði :math:`\Omega_1`, :math:`\Omega_2` og :math:`\Omega_3` eins og sýnt eru á myndinni.
Leiðið út :math:`3\times 3` jöfnuhneppi fyrir
:math:`c_1\approx u(x_1,y_1)`, :math:`c_2\approx u(x_2,y_2)` og
:math:`c_3\approx u(x_3,y_3)` með mismunaaðferð sem 
byggir á heildun yfir hlutsvæðin þrjú.

\(ii) Reiknið út nálgunargildin.
