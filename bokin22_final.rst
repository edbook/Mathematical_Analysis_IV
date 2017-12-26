
Bútaaðferðir
============

Inngangur
---------

Nú ætlum við að líta á sömu jaðargildisverkefnin og í síðasta kafla, en
kynna til sögunnar nýjar nálgunaraðferðir. Verkefnin eru annars vegar
venjuleg afleiðujafna af Sturm-Liouville-gerð með almennum
jaðarskilyrðum

.. math::

  \begin{cases}
       Lu=-(pu')'+qu=f,& \text{ á } ]a,b[,\\
   B_1u=\alpha_1u(a)-\beta_1u'(a)=\gamma_1,&(\alpha_1,\beta_1)\neq (0,0),\\
   B_2u=\alpha_2u(b)+\beta_2u'(b)=\gamma_2,&(\alpha_2,\beta_2)\neq (0,0),
     \end{cases}

og hins vegar hlutafleiðujafna í tveimur rúmvíddum af sundurleitnigerð á
svæði :math:`D\subset {{\mathbb  R}}^2` með jaðri :math:`\partial D` með
almennum jaðarskilyrðum

.. math::

  \begin{cases}
       Lu=-\nabla\cdot (p\nabla u)+qu=f, \qquad \text{ á } D,\\
   \alpha u+\beta\dfrac{\partial u}{\partial n}
   =\gamma, \qquad  \text{á } \ \partial D.
     \end{cases}

Forsendur okkar um stuðlana í virkjunum og stuðlana í jaðarskilyrðunum
eru þær sömu og í síðasta kafla.

Nálgunaraðferðin sem við ætlum að fást við er mjög almenn. Hún er kennd
við rússneskan stærðfræðing, Boris Galerkin. Það er auðveldast að lýsa
henni fyrir Dirichlet-verkefnið, þegar lausnin :math:`u(x)` í fyrra
verkefninu og :math:`u(x,y)` í seinna verkefninu er gefin á jaðrinum.
Það verður fyrsta takmark okkar og að því loknu fjöllum við um almenn
jaðarskilyrði. Aðferð Galerkins í ákveðnu sértilfelli er kölluð
bútaaðferð (e.  *finite element method*) og hana útfærum við í
smáatriðum. Þótt almenna nálgunaraðferðin beri nafn Galerkins, þá ber
þess að geta að svisslendingurinn Walther Ritz hafði áður sýnt hvernig
lágmörkunarverkefi leiði af sér jaðargildisverkefni fyrir
hlutafleiðujöfnur. Ritz er því stundum nefndur sem höfundur
aðferðarinnar.

Hlutheildun, innfeldi og tvílínulegt form
-----------------------------------------

Við ætlum nú að bera saman hlutheildun í einni og tveimur víddum. Hún
byggir á undirstöðusetningu stærðfræðigreiningarinnar og
sundurleitnisetningu Gauss. Með því að beita hlutheildun getum við sett
fram svokallaða *veika framsetningu* jaðargildisverkefnanna
(:ref:`Link title <eq:22.1.1>`) og (:ref:`Link title <eq:22.1.2>`), en Galerkin-aðferð byggir á
henni.

Um hlutheildun
~~~~~~~~~~~~~~

Látum nú :math:`V` tákna rúm allra raungildra falla :math:`\varphi` sem
eru samfelld á :math:`[a,b]` og samfellt deildanleg á köflum. Með
táknmáli okkar er

.. math:: V=\{\varphi \in C[a,b]\cap PC^1[a,b] \, ;\,  \varphi(x)\in {{\mathbb  R}}, x\in [a,b]\}.

Ef :math:`\varphi\in V`, þá gildir samkvæmt skilgreiningu að til er
skipting :math:`a=x_0<x_1<\cdots<x_N=b` á bilinu :math:`[a,b]` og föll
:math:`\chi_j\in C^1[x_j,x_{j+1}]` þannig að einskorðun :math:`\varphi`
við bilið :math:`[x_j,x_{j+1}]` er jöfn :math:`\chi_j`. Þetta þýðir að
afleiður fallsins :math:`\varphi` frá vinstri og hægri eru til í öllum
innri skiptipunktum. Athugið að fallið :math:`\varphi` er samfellt
deildanlegt í grennd um alla nema endanlega marga punkta í bilinu
:math:`[a,b]` og þessir punktar eru allir innri punktar í skiptingunni
sem tekin er. Ef afleiða :math:`\varphi` er ekki til í punkti
:math:`x_j`, þá skilgreinum við

.. math:: \varphi'(x_j)=\tfrac 12\big(\varphi'(x_j+)+\varphi'(x_j-)\big).

Með þessu verður :math:`\varphi'` heildanlegt fall á :math:`[a,b]` og
undirstöðusetningin gefur

.. math::

  \varphi(x)=\varphi(c)+\int_c^x\varphi'(t)\, dt, \qquad
   x,c\in [a,b].

Formúlan fyrir hlutheildun gildir einnig, ef við veljum tvö föll
:math:`\varphi` og :math:`\psi` í :math:`V`,

.. math::

  -\int_c^d\psi'(x)\varphi(x)\, dx
   =\int_c^d\psi(x)\varphi'(x) \, dx
   -\big[\psi(x)\varphi(x)\big]_c^d
   \qquad c,d\in [a,b].

Ef :math:`\psi=pv'`, þar sem :math:`v\in C^2[a,b]`, þá verður þessi
formúla

.. math::

  -\int_a^b(p(x)v'(x))'\varphi(x)\, dx
   =\int_a^bp(x)v'(x)\varphi'(x) \, dx
   -\big[p(x)v'(x)\varphi(x)\big]_a^b.

Sundurleitnisetning og hlutheildun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við sjá hvernig sundurleitnisetning Gauss gefur okkur formúlu
sem er hliðstæða hlutheildunar. Látum :math:`{\mathbf V=(v,w)}` vera
vigursvið af tveimur rúmbreytistærðum :math:`(x,y)` og
:math:`\varphi\in C^1({{\mathbb  R}}^2)` vera samfellt deildanlegt fall.
Þá gefur Leibniz-reglan

.. math::

  \nabla\cdot (\varphi {\mathbf V})
   =\dfrac{\partial (v\varphi)}{\partial x}
   +\dfrac{\partial (w\varphi) }{\partial y}
   =\bigg(\dfrac{\partial  v}{\partial x}
   +\dfrac{\partial  w}{\partial y}\bigg)\varphi
   +\bigg(v\dfrac{\partial  \varphi}{\partial x}
   +w\dfrac{\partial  \varphi}{\partial y}\bigg)
   =(\nabla\cdot {\mathbf V})\varphi  + {\mathbf V} \cdot \nabla  \varphi.

Í sértilfellinu :math:`{\mathbf V}= p\nabla  u` er þessi formúla

.. math::

  \nabla\cdot \big(\varphi p\nabla u\big)=
   \big(\nabla\cdot(p\nabla u)\big)\varphi
   +p\nabla u  \cdot \nabla \varphi.

Sundurleitnisetnig Gauss gefur

.. math::

  \iint_D \nabla \cdot (\varphi p\nabla u)\, dA
   =\int_{\partial D} p\dfrac{\partial u}{\partial n}\varphi \, ds

og af síðustu tveimur formúlum leiðir

.. math::

  -\iint\limits_D\nabla\cdot \big( p\nabla  u\big) \varphi \, dA=
   -\int\limits_{\partial D} p\dfrac{\partial u}{\partial n}\varphi\, ds
   +\iint\limits_D p\nabla  u\cdot \nabla  \varphi\, dA.

Þessi formúla er hliðstæða hlutheildunar í tveimur rúmvíddum.

Innfeldi
~~~~~~~~

Ef :math:`\varphi` og :math:`\psi` eru tvö raungild heildanleg föll á
bilinu :math:`[a,b]`, þá skilgreinum við innfeldi þeirra með formúlunni

.. math::

  {{\langle \varphi,\psi\rangle}}=\int_a^b \varphi(x)\psi(x)\, dx
   =\int_a^b \varphi \psi \, dx.

Ef hins vegar :math:`\varphi` og :math:`\psi` eru tvö raungild
heildanleg föll á lokuninni :math:`\overline D=D\cup \partial D`, þá
skilgreinum við innfeldi þeirra með

.. math::

  {{\langle \varphi,\psi\rangle}}=
   \iint_D \varphi(x,y)\psi(x,y)\, dxdy
   =\iint_D \varphi\psi \, dA.

Tvílínulegt form sem :math:`L` gefur af sér
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`L` táknar afleiðuvirkjann í (:ref:`Link title <eq:22.1.1>`), þá notum við
stuðlana :math:`p` og :math:`q` til þess að skilgreina *tvílínulega
formið sem* :math:`L`  *gefur af sér* með

.. math::

  {{\langle \varphi,\psi\rangle}}_L=\int_a^b\big(p\varphi' \psi'
   +q\varphi \psi\big)\, dx,
   \qquad \varphi, \psi \in V,

Ef hins vegar :math:`L` táknar hlutafleiðuvirkjann (:ref:`Link title <eq:22.1.2>`),
þá skilgreinum við á hliðstæðan máta

.. math::

  {{\langle \varphi,\psi\rangle}}_L=\iint\limits_D\big(p\, \nabla  \varphi\cdot \nabla 
   \psi +q\, \varphi\psi\big)\, dA.

Hér þurfum við að gera ráð fyrir því að fyrsta stigs hlutafleiður
:math:`\varphi` og :math:`\psi` séu skilgreindar og takmarkaðar á
:math:`D` til þess að heildin séu til.

Sambandið við jaðargildisverkefnin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú getum við tengt innfeldið og tvílínulega formið við
jaðargildisverkefnin. Látum fyrst :math:`L` vera virkjann í
(:ref:`Link title <eq:22.1.1>`) og :math:`v\in C^2[a,b]`. Hlutheildunin
(:ref:`Link title <eq:22.2.1>`) gefur okkur

.. math::

  {{\langle Lv,\varphi\rangle}}
   =
   \int_a^b\big(pv'\varphi'+qv\varphi \big) \, dx
   -\big[pv'\varphi\big]_a^b
   ={{\langle v,\varphi\rangle}}_L-\big[pv'\varphi\big]_a^b.

Í sértilfellinu þegar :math:`\varphi(a)=\varphi(b)=0` og :math:`v=u` er
lausnin á :math:`Lu=f` fáum við

.. math::

  {{\langle u,\varphi\rangle}}_L={{\langle f,\varphi\rangle}}, \qquad \varphi\in V, 
   \ \varphi(a)=\varphi(b)=0.

Nú lítum við á virkjann :math:`L` í seinna verkefninu (:ref:`Link title <eq:22.1.2>`)
og :math:`v\in C^2(\overline D)`. Þá gefur (:ref:`Link title <eq:22.2.2>`) að fyrir
sérhvert :math:`v\in C^2(\overline D)` gildir

.. math::

  \begin{aligned}
   \iint_D \big(Lv\big) \varphi\, dA 
   &=\iint_D\big( p\,  \nabla v\cdot \nabla \varphi+q v\varphi\big)  \,
   dA-\int_{\partial D}p\dfrac{\partial v}{\partial n} \varphi \, ds\\
   &={{\langle v,\varphi\rangle}}_L
   -\int_{\partial D}p\dfrac{\partial v}{\partial n} \varphi \, ds.\end{aligned}

Í sértilfellinu þegar :math:`v=u` er lausn :math:`Lu=f` og
:math:`\varphi=0` á jaðrinum :math:`\partial D` fáum við

.. math::

  {{\langle u,\varphi\rangle}}_L={{\langle f,\varphi\rangle}}, \qquad \varphi\in C^1(\overline
     D), \quad \varphi=0 \text{ á } \partial D.

Aðferð Galerkins fyrir Dirichlet-verkefnið
------------------------------------------

Nú getum við útskýrt aðferð Galerkins í því tilfelli þegar við höfum
Dirichlet-jaðarskilyrði á öllum jaðrinum.

Galerkin-aðferð í einni vídd fyrir Dirichlet-verkefni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessu sértilfelli er fyrra verkefnið jafngilt

.. math::

  \begin{cases}
       Lu=-(pu')'+qu=f,& \text{ á } ]a,b[,\\
   u(a)=\gamma_1/\alpha_1, \quad  u(b)=\gamma_2/\alpha_2.
     \end{cases}

Jafnan (:ref:`Link title <eq:22.2.4>`) nefnist *veikt framsetning* á þessu
jaðargildisverkefni. Athugið að hér gætum við einfaldað okkur lífið
aðeins með því að taka :math:`\alpha_1=\alpha_2=1`, en vegna
alhæfinganna sem á eftir koma skulum við hafa þetta svona.

Í aðferð Galerkins er byrjað á að finna eitthvert fall :math:`\psi_0(x)`
sem uppfyllir jaðarskilyrðin :math:`\psi_0(a)=\gamma_1/\alpha_1` og
:math:`\psi_0(b)=\gamma_2/\alpha_2`. Síðan eru valin línulega óháð föll
:math:`\varphi_1,\dots,\varphi_N` sem uppfylla óhliðruðu jaðarskilyrðin
í endapunktunum, :math:`\varphi_j(a)=\varphi_j(b)=0`. Nálgunarfall
:math:`v(x)` fyrir lausnina :math:`u(x)` er síðan valið af gerðinni

.. math:: v=\psi_0+c_1\varphi_1+\cdots+c_N\varphi_N,

þar sem stuðlarnir :math:`c_j` í línulegu samantektinni eiga að uppfylla

.. math:: {{\langle v,\varphi_j\rangle}}_L={{\langle f,\varphi_j\rangle}}, \qquad j=1,2,\dots,N.

Eins og áður var getið, þá segir formúla (:ref:`Link title <eq:22.2.4>`) að lausnin
:math:`u` uppfylli þessa jöfnu, með :math:`u` í hlutverki :math:`v` og
:math:`\varphi` í hlutverki :math:`\varphi_j` fyrir sérhvert fall
:math:`\varphi\in V` með :math:`\varphi(a)=\varphi(b)=0`.

Nú athugum við að (:ref:`Link title <eq:22.3.4>`) er línulegt jöfnuhneppi

.. math::

  {{\langle \psi_0,\varphi_j\rangle}}_L+\sum_{k=1}^Nc_k{{\langle \varphi_k,\varphi_j\rangle}}_L
   ={{\langle f,\varphi_j\rangle}}, \qquad j=1,\dots,N.

Við getum sett það fram á fylkjaformi :math:`A{\mathbf c}={\mathbf b}`,
þar sem :math:`A=\big(a_{jk}\big)_{j,k=1}^N` er samhverft
:math:`N\times N` fylki með

.. math::

  a_{jk}={{\langle \varphi_k,\varphi_j\rangle}}_L
   ={{\langle \varphi_j,\varphi_k\rangle}}_L, \qquad j,k=1,\dots,N.

Stuðlarnir í hægri hliðinni eru gefnir með

.. math:: b_j={{\langle f,\varphi_j\rangle}}-{{\langle \psi_0,\varphi_j\rangle}}_L, \qquad j=1,\dots,N.

Til þess að reikna út nálgunina :math:`v` þurfum við að reikna út alla
stuðla hneppisins og leysa það síðan, til þess að komast að því hver
gildin :math:`c_j` í línulegu samantektinni (:ref:`Link title <eq:22.3.3>`) eru.

Galerkin-aðferð í tveimur víddum fyrir Dirichlet-verkefni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum nú á Dirichlet-verkefnið í tveimur rúmvíddum,

.. math::

  \begin{cases}
       Lu=-\nabla\cdot (p\nabla u)+qu=f, \qquad \text{ á } D,\\
   u=\gamma/\alpha, \qquad  \text{á } \ \partial D.
     \end{cases}

Aðferð Galerkins er alveg eins fyrir þetta verkefni. Við byrjum á að
velja :math:`\psi_0(x,y)` á :math:`\overline D`, sem tekur réttu gildin
:math:`\gamma(x,y)/\alpha(x,y)` í öllum punktum
:math:`(x,y)\in \partial D`. Síðan veljum við línulega óháð föll
:math:`\varphi_1(x,y),\dots,\varphi_N(x,y)` sem eru núll á
:math:`\partial D`. Nálgunarfallið :math:`v(x,y)` fyrir lausnina
:math:`u(x,y)` er gefið með (:ref:`Link title <eq:22.3.3>`) og stuðlarnir
:math:`c_1,\dots,c_N` eru eiga að uppfylla línulega jöfnuheppið
(:ref:`Link title <eq:22.3.4>`). Jöfnuheppið :math:`A{\mathbf c} ={\mathbf b}` er alveg eins og í einvíða tilfellinu, en
skilgreiningarnar á innfeldi og tvílínulegu formi eru samkvæmt jöfnum
(:ref:`Link title <eq:22.2.2b>`) og (:ref:`Link title <eq:22.2.2d>`).

Aðferð Galerkins með almennum jaðarskilyrðum
--------------------------------------------

Nú ætlum við að halda áfram athugun okkar á jaðargildisverkefnunum
(:ref:`Link title <eq:22.1.1>`) og (:ref:`Link title <eq:22.1.2>`) og sýna hvernig aðferð
Galerkins er útfærð fyrir þau í öllum tilfellum. Fyrst þurfum við að
leiða út það sem kallað er *veik framsetning á jaðargildisverkefnunum*,
en það er formúla

.. math::

  {{\langle u,\varphi\rangle}}_{L,B}={{\langle f,\varphi\rangle}}+T_B(\varphi), \qquad
   \varphi\in V_B,

þar sem
:math:`(\psi,\varphi)\mapsto {{\langle \psi,\varphi\rangle}}_{L,B}` er
tvílínulegt form sem er bæði háð virkjanum :math:`L` og jaðarskilyrðunum
:math:`B`, :math:`\varphi\mapsto T_B(\varphi)` er línulegt form sem er
háð jaðarskilyrðunum og :math:`V_B` er rúm af föllum, sem skilgreint er
út frá jaðarskilyrðunum, þannig að öll föllin í :math:`V_B` taka gildið
:math:`0` í punktunum á jaðrinum, þar sem gildi réttu lausnarinnar eru
gefin.

Þegar veika formið liggur fyrir er auðvelt að útskýra hvernig aðferðin
er útfærð. Nálgunarlausnin :math:`v` á alltaf að taka sömu gildi og
rétta lausnin :math:`u` í þeim punktum jaðarsins þar sem réttu gildin
eru þekkt. Fyrst þarf að finna fall :math:`\psi_0` sem skilgreint er á
:math:`[a,b]` fyrir einvíða verkefnið og á :math:`\overline D` fyrir
tvívíða verkefnið sem tekur sömu gildi og rétta lausnin :math:`u` í
öllum punktum jaðarsins þar sem :math:`u` er þekkt.

Í einvíða tilfellinu er jaðarinn einungis tveir punktar :math:`a` og
:math:`b`. Ef jaðarskilyrðin segja að lausnin :math:`u(x)` sé gefin í
öðrum eða báðum endapunktum bilsins, þá skilgreinum við fall
:math:`\psi_0(x)` í :math:`V` sem tekur þessi gildi,
:math:`\psi_0(a)=\gamma_1/\alpha_1` ef :math:`\beta_1=0` og
:math:`\psi_0(b)=\gamma_2/\alpha_2` ef :math:`\beta_2=0`. Ef
:math:`\beta_1\neq 0` og :math:`\beta_2\neq 0`, þá er :math:`\psi_0`
núllfallið.

Í tvívíða tilfellinu skilgreinum við
:math:`\partial_1D=\{(x,y)\in \partial D\,;\, \beta(x,y)=0\}` og veljum okkur fall :math:`\psi_0(x,y)` á
:math:`\overline D` sem tekur sömu gildi og lausnin :math:`u(x,y)` á
:math:`\partial_1D`, :math:`\psi_0(x,y)=\gamma(x,y)/\alpha(x,y)`. Ef
:math:`\partial_1D` er tóma mengið, þá er :math:`\psi_0` núllfallið.

Þegar það er klárt hvað :math:`\psi_0` á að vera, þá veljum við föll
:math:`\varphi_1,\dots,\varphi_N\in V_B` og látum nálgunarfallið
:math:`v=\psi_0+c_1\varphi_1+\cdots+\varphi_N` uppfylla línulega
jöfnuhneppið

.. math::

  {{\langle v,\varphi_j\rangle}}_{L,B}={{\langle f,\varphi_j\rangle}}+T_B(\varphi_j), 
   \qquad j=1,\dots,N.

Alveg eins og í síðustu grein athugum við að (:ref:`Link title <eq:22.4.1a>`) er
línulegt jöfnuhneppi

.. math::

  {{\langle \psi_0,\varphi_j\rangle}}_{L,B}+\sum_{k=1}^Nc_k{{\langle \varphi_k,\varphi_j\rangle}}_{L,B}
   ={{\langle f,\varphi_j\rangle}}+T_B(\varphi_j), \qquad j=1,\dots,N.

Við getum sett það fram á fylkjaformi :math:`A{\mathbf c}={\mathbf b}`,
þar sem :math:`A=\big(a_{jk}\big)_{j,k=1}^N` er samhverft
:math:`N\times N` fylki með

.. math::

  a_{jk}={{\langle \varphi_k,\varphi_j\rangle}}_{L,B}
   ={{\langle \varphi_j,\varphi_k\rangle}}_{L,B}, \qquad j,k=1,\dots,N.

Stuðlarnir í hægri hliðinni eru gefnir með

.. math::

  b_j={{\langle f,\varphi_j\rangle}}+T_B(\varphi_j)-{{\langle \psi_0,\varphi_j\rangle}}_{L,B}, 
   \qquad j=1,\dots,N.

Til þess að reikna út nálgunina :math:`v` þurfum við að reikna út alla
stuðla hneppisins og leysa það síðan, til þess að komast að því hver
gildin :math:`c_j` í línulegu samantektinni (:ref:`Link title <eq:22.4.1a>`) eru.

Nú þurfum við að ganga skipulega á öll tilfellin í (:ref:`Link title <eq:22.1.1>`) og
(:ref:`Link title <eq:22.1.2>`) og leiða út veika framsetningu og skilgreina
:math:`{{\langle \varphi,\psi\rangle}}_{L,B}` og :math:`T_B(\varphi)`
þannig að (:ref:`Link title <eq:22.4.1>`) gildi fyrir þau öll.

Almenn jaðarskilyrði í einni vídd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við byggjum á formúlunni (:ref:`Link title <eq:22.2.3>`) sem við getum ritað

.. math::

  {{\langle u,\varphi\rangle}}_L + p(a)u'(a)\varphi(a)-p(b)u'(b)\varphi(b)
    = {{\langle f,\varphi\rangle}}, \qquad \varphi\in V.

Við þurfum að skipta jaðarskilyrðunum í fjögur tilvik.

Blönduð jaðarskilyrði í báðum endapunktum:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við lítum fyrst á verkefnið

.. math::

  \begin{cases}
   Lu=-(pu')'+qu=f, \\
   B_1u={\alpha}_1u(a)-\beta_1u'(a)=\gamma_1, \quad \beta_1\neq 0, \\ 
   B_2u=\alpha_2u(b)+{\beta}_2u'(b)=\gamma_2, \quad \beta_2\neq 0.
   \end{cases}

Jaðarskilyrðin jafngilda :math:`u'(a)=(\alpha_1u(a)-\gamma_1)/\beta_1`
og :math:`-u'(b)=(\alpha_2u(b)-\gamma_2)/\beta_2`. Við stingum þeim inn
í (:ref:`Link title <eq:22.4.2>`) og fáum

.. math::

  {{\langle u,\varphi\rangle}}_L  + 
   \dfrac {p(a)}{\beta_1}(\alpha_1u(a)-\gamma_1)\varphi(a)
   +\dfrac{p(b)}{\beta_2}(\alpha_2u(b)-\gamma_2)\varphi(b)
   ={{\langle f,\varphi\rangle}}.

Jafngild jafna

.. math::

  {{\langle u,\varphi\rangle}}_L
   +\dfrac {p(a)\alpha_1}{\beta_1}u(a)\varphi(a)
   +\dfrac{p(b)\alpha_2}{\beta_2}u(b)\varphi(b)
   ={{\langle f,\varphi\rangle}}
   +\dfrac {p(a)\gamma_1}{\beta_1}\varphi(a)
   +\dfrac{p(b)\gamma_2}{\beta_2}\varphi(b)

nefnist *veik framsetning jaðargildisverkefnisins* (:ref:`Link title <eq:22.4.3>`).
Við skilgreinum :math:`V_B=V`, tvílínulega formið með

.. math::

  {{\langle \varphi,\psi\rangle}}_{L,B}={{\langle \varphi,\psi\rangle}}_L
   +\dfrac {p(a)\alpha_1}{\beta_1}\varphi(a)\psi(a)
   +\dfrac{p(b)\alpha_2}{\beta_2}\varphi(b)\psi(b),
   \qquad \varphi,\psi\in V_B,

og línulega formið :math:`T_B` með

.. math::

  T_B(\varphi)=\dfrac {p(a)\gamma_1}{\beta_1}\varphi(a)
   +\dfrac{p(b)\gamma_2}{\beta_2}\varphi(b), \qquad \varphi \in V_B.

Fallsjaðarskilyrði í vinstri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú breytum við jaðarskilyrðunum og gerum ráð fyrir að
:math:`u\in C^2[a,b]` sé lausn á verkefninu

.. math::

  \begin{cases}
   Lu=-(pu')'+qu=f, \\
   B_1u=\alpha_1u(a)=\gamma_1,  \\ 
   B_2u=\alpha_2u(b)+{\beta}_2u'(b)=\gamma_2, \quad \beta_2\neq 0.
   \end{cases}

Við skilgreinum :math:`V_B=\{\varphi\in V\,;\, \varphi(a)=0\}`. Seinna
jaðarskilyrðið jafngildir :math:`-u'(b)=(\alpha_2u(b)-\gamma_2)/\beta_2`
og við sjáum að fyrir :math:`\varphi\in V_B` er (:ref:`Link title <eq:22.4.2>`)
jafngilt

.. math::

  {{\langle u,\varphi\rangle}}_L
   +\dfrac{p(b)\alpha_2}{\beta_2}u(b)\varphi(b)
   ={{\langle f,\varphi\rangle}}
   +\dfrac{p(b)\gamma_2}{\beta_2}\varphi(b).

Þetta er veik framsetning á (:ref:`Link title <eq:22.4.5>`). Við skilgreinum því

.. math::

  {{\langle \varphi,\psi\rangle}}_{L,B}={{\langle \varphi,\psi\rangle}}_L
   +\dfrac{p(b)\alpha_2}{\beta_2}\varphi(b)\psi(b),
   \quad \text{ og } \quad 
   T_B(\varphi)=
   \dfrac{p(b)\gamma_2}{\beta_2}\varphi(b),
   \qquad \varphi,\psi\in V_B.

Fallsjaðarskilyrði í hægri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú breytum við jaðarskilyrðinu aftur og gerum ráð fyrir að
:math:`u\in C^2[a,b]` sé lausn á

.. math::

  \begin{cases}
   Lu=-(pu')'+qu=f, \\
   B_1u={\alpha}_1u(a)-\beta_1u'(a)=\gamma_1, \quad \beta_1\neq 0 \\ 
   B_2u=\alpha_2u(b)=\gamma_2.
   \end{cases}

Við skilgreinum :math:`V_B=\{\varphi\in V \,;\, \varphi(b)=0 \}` og
athugum að fyrra jaðarskilyrðið jafngildir
:math:`u'(a)=(\alpha_1u(a)-\gamma_1)/\beta_1`. Þetta notum við í
(:ref:`Link title <eq:22.4.2>`) og fáum með sama hætti og hér að framan að

.. math::

  {{\langle u,\varphi\rangle}}_L
   +\dfrac {p(a)\alpha_1}{\beta_1}u(a)\varphi(a)
   ={{\langle f,\varphi\rangle}}
   +\dfrac {p(a)\gamma_1}{\beta_1}\varphi(a), \qquad \varphi\in V_B.

Þetta er veik framsetning jaðargildisverkefnisins (:ref:`Link title <eq:22.4.6>`).
Við skilgreinum

.. math::

  {{\langle \varphi,\psi\rangle}}_{L,B}={{\langle \varphi,\psi\rangle}}_L
   +\dfrac {p(a)\alpha_1}{\beta_1}\varphi(a)\psi(a)
   \quad \text{ og } \quad 
   T_B(\varphi)=\dfrac {p(a)\gamma_1}{\alpha_2}\varphi(a), 
   \qquad \varphi,\psi\in V_B.

Fallsjaðarskilyrði í báðum endapunktum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú erum við komin að Dirichlet-verkefninu, sem við lýstum í síðustu
grein,

.. math::

  \begin{cases}
   Lu=-(pu')'+qu=f, \\
   B_1u=\alpha_1u(a)=\gamma_1,\\ 
   B_2u=\alpha_2u(b)=\gamma_2.
   \end{cases}

Við vitum að í þessu tilfelli gildir um öll :math:`\varphi\in V` með
:math:`\varphi(a)=\varphi(b)=0` að

.. math:: {{\langle u,\varphi\rangle}}_L={{\langle f,\varphi\rangle}},

og því skilgreinum við rúmið
:math:`V_B=\{\varphi\in V \,;\, \varphi(a)=\varphi(b)=0\}`,
:math:`{{\langle \varphi,\psi\rangle}}_{L,B}={{\langle \varphi,\psi\rangle}}_L`
og :math:`T_B(\varphi)=0` fyrir öll :math:`\varphi,\psi\in V_B`.

Almenn jaðarskilyrði í tveimur víddum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú snúum við okkur að því að finna veika framsetningu á
jaðargildisverkefninu (:ref:`Link title <eq:22.1.2>`). Við höfum að
:math:`\partial_1D=\{(x,y) \,;\, \beta(x,y)=0\}`, skilgreinum
:math:`\partial_2D=\{(x,y) \,;\, \beta(x,y)\neq 0\}` og látum
:math:`V_B` tákna rúm allra falla :math:`\varphi\in C^2(\overline D)`
þannig að :math:`\varphi(x,y)=0` í öllum punktum
:math:`(x,y)\in \partial_1D`. Við höfum

.. math::

  -\dfrac{\partial u}{\partial n} =\dfrac{\alpha u-\gamma}{\beta},
   \qquad \text{ á } \ \partial_2D,

og því segir formúla (:ref:`Link title <eq:22.2.5>`) að rétta lausnin uppfylli

.. math::

  {{\langle u,\varphi\rangle}}_L+\int_{\partial_2D}\dfrac{p\alpha}\beta u\varphi\, ds
   ={{\langle f,\varphi\rangle}}+\int_{\partial_2D}\dfrac{p\gamma}\beta \varphi\, ds,
   \qquad \varphi\in V_B.

Þetta er veikt form jaðargildisverkefnisins (:ref:`Link title <eq:22.1.2>`). Nú
skilgreinum við

.. math::

  {{\langle \varphi,\psi\rangle}}_{L,B}=
   {{\langle \varphi,\psi\rangle}}_L+\int_{\partial_2D}\dfrac{p\alpha}\beta \varphi\psi\, ds
   \quad \text{ og } \quad 
   T_B(\varphi)=\int_{\partial_2D}\dfrac{p\gamma}\beta \varphi\, ds,
   \qquad \varphi,\psi\in V_B.

Með þessum rithætti er veik framsetning (:ref:`Link title <eq:22.1.1>`) og
(:ref:`Link title <eq:22.1.2>`) í öllum tilfellunum gefin með (:ref:`Link title <eq:22.4.1>`). Nú
skulum við taka fyrir tvö sýnidæmi um útleiðslu á veikri framsetningu og
nálgun með annars stigs margliðu með aðferð Galerkins.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum á jaðargildisverkefnið

.. math::

  -((1+x)u')'+x^2u=1-x, \quad x\in ]0,1[, 
   \quad u(0)-u'(0)=1, \quad u(1)=2.

Við skulum leiða út veikt form jaðargildisverkefnisins og útskýra
hvernig grunnföll eru valin þegar nálgunarlausn á að vera margliða af
stigi :math:`\leq 2`.

*Lausn*:   Í þessu verkefni er blandað jaðarskilyrði í :math:`x=0` og
fallsjaðarskilyrði í :math:`x=1`. Við eigum því að taka grunnfall
:math:`\varphi\in V`, sem uppfyllir :math:`\varphi(1)=0`, margfalda það
við :math:`Lu(x)` og hlutheilda. Þá fæst jafnan

.. math::

  \begin{aligned}
     \int_0^1(1-x)\varphi(x)\, dx&=\int_0^1Lu(x)\varphi(x)\, dx
   =\int_0^1\big(-((1+x)u'(x))'+x^2u(x)\big)\varphi(x)\, dx\\
   &=\int_0^1\big((1+x)u'(x)\varphi'(x)+x^2u(x)\varphi(x)\big)\, dx
   -\bigg[(1+x)u'(x)\varphi(x)\bigg]_0^1
   \\
   &=\int_0^1\big((1+x)u'(x)\varphi'(x)+x^2u(x)\varphi(x)\big)\, dx
   +u'(0)\varphi(0)\\
   &=\int_0^1\big((1+x)u'(x)\varphi'(x)+x^2u(x)\varphi(x)\big)\, dx
   +(u(0)-1)\varphi(0).\end{aligned}

Í síðasta liðnum notuðum við að rétta lausnin uppfyllir jaðarskilyrðið
:math:`u'(0)=u(0)-1`. Veika formið er því jafngilda jafnan

.. math::

  \int_0^1\big((1+x)u'(x)\varphi'(x)+x^2u(x)\varphi(x)\big)\, dx
   +u(0)\varphi(0)
   =\int_0^1(1-x)\varphi(x)\, dx+\varphi(0).

sem segir okkur jafnframt að :math:`{{\langle u,\varphi\rangle}}_{L,B}`
er það sem stendur vinstra megin jafnaðarmerkisins og
:math:`{{\langle f,\varphi\rangle}}+T_B(\varphi)` er það sem stendur
hægra megin.

Nálgunarfallið er annars stigs margliða :math:`v(x)` sem uppfyllir rétt
jaðarskilyrði :math:`v(1)=2`. Við getum því tekið :math:`\psi_0(x)=2` og
við þurfum að velja tvær línulega óháðar margliður af stigi
:math:`\leq 2` sem taka gildið :math:`0` í :math:`x=1`. Við veljum
:math:`\varphi_1(x)=1-x`, :math:`\varphi_2(x)=1-x^2`. Þá er
:math:`v(x)=2+c_1(1-x)+c_2(1-x^2)`, þar sem :math:`c_1` og :math:`c_2`
eru rauntölur. Línulega jöfnuhneppið sem stuðlarnir :math:`c_1` og
:math:`c_2` uppfylla er

.. math::

  \left[\begin{matrix} a_{11} & a_{12}\\
    a_{21} & a_{22}
   \end{matrix}
   \right]
   \left[\begin{matrix} c_1\\ c_2\end{matrix}
   \right]
   =
   \left[\begin{matrix} b_1\\ b_2\end{matrix}
   \right]

Þar sem

.. math::

  a_{jk}={{\langle \varphi_j,\varphi_k\rangle}}_{L,B}
   =\int_0^1\big((1+x)\varphi_j'(x)\varphi_k'(x)
   +x^2\varphi_j(x)\varphi_k(x)\big)\, dx
   +\varphi_j(0)\varphi_k(0)

og

.. math::

  \begin{aligned}
   b_{j}&={{\langle f,\varphi_j\rangle}}+T_B(\varphi_j)-{{\langle \psi_0,\varphi_j\rangle}}_{L,B}\\
   &=\int_0^1(1-x)\varphi_j(x)\, dx+\varphi_j(0)
   -2\int_0^1x^2\varphi_j(x)\, dx-2\varphi_j(0).  \end{aligned}

Nú er lesandanum eftirlátið að reikna út alla stuðlana og leysa
hneppið.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Látum :math:`D` vera opna þríhyrninginn sem afmarkast af línunum sem
hafa jöfnurnar :math:`y=0`, :math:`x=0` og :math:`x+y=1`,
:math:`D=\{(x,y)\, ;\, 0<x<1, 0<y<1-x\}` og lítum á verkefnið.

:math:`\begin{cases}
-\nabla^2 u=
-\dfrac{\partial^2 u}{\partial x^2 }-\dfrac{\partial^2 u}{\partial y^2 }=1
&\text{á } \ D,\\
u(x,0)=1-x, &0<x<1,\\
\dfrac{\partial u}{\partial n}(0,y)=1-y, &0<y<1,\\
\dfrac{\partial u}{\partial n}(x,1-x)+u(x,1-x)=0, &0<x<1.
\end{cases}`

Við skulum beita Galerkins til þess að ákvarða nálgunarlausn af gerðinni

.. math:: v(x,y)=a+bx+cy+dxy.

*Lausn:*   Jaðarinn :math:`\partial_1 D` er lárétta línustrikið
:math:`\{(x,0)\, ;\, 0\leq x\leq 1\}` og :math:`\partial_2 D` sammengi
lóðrétta striksins :math:`\{(0,y)\, ;\, 0<y\leq 1\}` og skástriksins
:math:`\{(x,1-x)\, ;\, 0\leq  x<1\}`.

Fyrst þurfum við að leiða út veikt form jaðargildisverkefnisins. Við
tökum því :math:`\varphi` sem er :math:`0` á :math:`\partial_1 D`
margföldum báðar hliðar afleiðujöfnunnar með :math:`\varphi` og heildum
síðan yfir :math:`D`. Þá fæst

.. math::

  \iint_D\nabla u\cdot \nabla \varphi \, dA
   -\int_{\partial_2 D}\dfrac{\partial u}{\partial n}\varphi \, ds
   =\iint_D \varphi \, dA.

Nú setjum við inn gildin fyrir :math:`\partial u/\partial n` á
:math:`\partial_2D` og fáum

.. math::

  \iint_D\nabla u\cdot \nabla \varphi \, dA
   -\int_0^1(1-y)\varphi(0,y)\, dy
   +\int_0^1u(x,1-x)\varphi(x,1-x)\, \sqrt 2\, dx
   =\iint_D \varphi \, dA.

Veikt form jaðargildisverkefnisins er því

.. math::

  \iint_D\nabla u\cdot \nabla \varphi \, dA
   +\int_0^1u(x,1-x)\varphi(x,1-x)\, \sqrt 2\, dx
   =\iint_D \varphi \, dA+\int_0^1(1-y)\varphi(0,y)\, dy.

Athugið að :math:`{{\langle u,\varphi\rangle}}_{L,B}` stendur vinstra
megin jafnaðarmerkisins og
:math:`{{\langle f,\varphi\rangle}}+T_B(\varphi)` stendur hægra mengin.

Nú er komið að því að skoða nálgnarfallið. Við verðum að velja
:math:`\psi_0(x,y)=1-x` sem jafngildir því að setja :math:`a=1` og
:math:`b=-1`. Hinir liðirnir :math:`cy` og :math:`dxy` eru báðir
:math:`0` á :math:`\partial_1D` og því er eðlilegt að velja grunnföllin
:math:`\varphi_1(x,y)=y` og :math:`\varphi_2(x,y)=xy`. Nálgunarlausnin
er því :math:`v(x,y)=\psi_0(x,y)+c_1\varphi_1(x,y)+c_2\varphi_2(x,y)`
þar sem stuðlarnir :math:`c_1` og :math:`c_2` eru leystir út úr
:math:`A{\mathbf c}={\mathbf b}`, þar sem

.. math::

  \begin{aligned}
   a_{jk}&=\int_0^1\int_0^{1-x}
   \bigg(\dfrac{\partial \varphi_j}{\partial x}\dfrac{\partial \varphi_k}{\partial x}
   +\dfrac{\partial \varphi_j}{\partial y}\dfrac{\partial \varphi_k}{\partial y}\bigg)\, dydx
   +\int_0^1\varphi_j(x,1-x)\varphi_k(x,1-x)\, \sqrt 2 \, dx \\
   b_j&=\int_0^1\int_0^{1-x} \varphi_j\, dydx 
   +\int_0^1(1-y)\varphi_j(0,y)\, dy\\
   &-\int_0^1\int_0^{1-x}\bigg(\dfrac{\partial \varphi_0}{\partial x}\dfrac{\partial \varphi_j}{\partial x}
   +\dfrac{\partial \varphi_0}{\partial y}\dfrac{\partial \varphi_j}{\partial y}\bigg)\, dydx 
   -\int_0^1\varphi_0(x,1-x)\varphi_j(x,1-x)\, \sqrt 2\, dx.\end{aligned}

Nú er ekkert annað í boði en reikna út öll heildin

.. math::

  \begin{aligned}
   a_{11}&=\int_0^1\int_0^{1-x}\big(0^2+1^2\big)\, dydx
   +\sqrt 2\int_0^1\big(1-x\big)^2\, dx=\tfrac 12+\tfrac{\sqrt 2}3,\\
   a_{12}=a_{21}&=\int_0^1\int_0^{1-x}\big(y\cdot 0+x\cdot 1\big)\, dydx
   +\sqrt 2\int_0^1\big(x(1-x)(1-x)\big)\, dx=\tfrac 16+\tfrac{\sqrt 2}{12},\\
   a_{22}&=\int_0^1\int_0^{1-x}\big(y^2+x^2\big)\, dydx
   +\sqrt 2\int_0^1\big(x(1-x)\big)^2\, dx=\tfrac 16+\tfrac{\sqrt 2}{30},\\
   b_{1}&=\int_0^1\int_0^{1-x}  y \, dydx
   +\int_0^1(1-y)y\, dy
   -\int_0^1\int_0^{1-x} \big((-1)\cdot 0+0\cdot 1\big) \, dydx\\
   &-\sqrt 2\int_0^1(1-x)(1-x)\, dx
   =\tfrac 13 -\tfrac{\sqrt 2}{3}\\
   b_{2}&=\int_0^1\int_0^{1-x}  xy \, dydx
   +\int_0^1(1-y)\cdot 0\, dy
   -\int_0^1\int_0^{1-x} \big((-1)\cdot y+0\cdot x\big) \, dydx \\
   &-\sqrt 2\int_0^1(1-x)x(1-x)\, dx =\tfrac 5{24} -\tfrac{\sqrt 2}{12}\\\end{aligned}

Hneppið sem við þurfum að leysa er

.. math::

  \left[\begin{matrix} \tfrac 12+\tfrac{\sqrt 2}3 
   & \tfrac 16+\tfrac{\sqrt 2}{12}\\
   \tfrac 16+\tfrac{\sqrt 2}{12} & \tfrac 16+\tfrac{\sqrt 2}{30}
   \end{matrix}\right]
   \left[\begin{matrix} c_1 \\ c_2 \end{matrix}\right]
   =\left[\begin{matrix} \tfrac 13-\tfrac{\sqrt 2}{3} \\ \tfrac
   5{24}-\tfrac{\sqrt 2}{12}  \end{matrix}\right]

Svarið er :math:`c_1=-0.4360` og :math:`c_2=1.0034` og því er
nálgunarlausnin

.. math:: v(x,y)=1-x-0.4360\cdot y+1.0034\cdot xy.

.. end-toggle::

Bútaaðferð í einni vídd
-----------------------

Við höfum nú lýst aðferð Galerkins mjög almennt, en til þess að hún
verði nothæf sem nálgunaraðferð þurfum við að velja góð grunnföll þannig
að auðvelt sé að ákvarða heildin sem koma fyrir í stuðlunum
:math:`a_{jk}` og :math:`b_j` og að úrlausn jöfnuheppisins verði
þægileg.

Lang auðveldast er að velja þúfugrunnföll á :math:`[a,b]` fyrir
ótiltekna skiptingu

.. math:: a=x_0<x_1<\cdots<x_N=b.

Munið að fyrir sérhvert :math:`j=0,\dots,N` er :math:`\varphi_j` fallið
sem tekur gildið :math:`1` í :math:`x_j`, :math:`0` í öllum öðrum
punktum skiptingarinnar og hefur graf sem er línustrik yfir sérhverju
hlutbilanna :math:`[x_j,x_{j+1}]`. (Nú þarf lesandinn að teikna sér
þrjár myndir. Sú fyrsta sýnir gröf fallanna :math:`\varphi_0` og
:math:`\varphi_1`, önnur sýnir gröf fallanna :math:`\varphi_{j-1}`,
:math:`\varphi_j` og :math:`\varphi_{j+1}` fyrir ótiltekinn innri punkt
:math:`x_j` í skiptingunni og sú þriðja sýnir gröf fallanna
:math:`\varphi_{N-1}` og :math:`\varphi_N`.) Við höfum formúlur
(:ref:`Link title <eq:21.1.18>`) fyrir :math:`\varphi_j` og :math:`\varphi'_j`, en
við getum komist að mestu af án þeirra þegar við reiknum út heildin.
Athugið að hér látum við :math:`j` hlaupa frá :math:`0` til :math:`N` en
ekki frá :math:`1` til :math:`N` eins og gert er hér að framan.

Kostirnir við þetta val á grunnföllum eru einkum tveir:

\(i) 
Ef :math:`|j-k|>1`, þá er :math:`a_{jk}=0` og því er :math:`A` sé
þríhornalínufylki. Við þurfum því í mesta lagi að reikna út þrjú stök
í hverri línu fylkisins og úrlausn línulega jöfnuhneppisins er
hraðvirk fyrir stór hneppi.

\(ii)
Auðvelt er að taka góðar nálganir á heildunum sem koma fyrir í
:math:`a_{jk}` og :math:`b_j`.

Blönduð jaðarskilyrði í báðum endapunktum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nálgunarlausnin :math:`v(x)` er af gerðinni

.. math:: v(x)=c_0\varphi_0(x)+\cdots+c_N\varphi_N(x).

þar sem :math:`{\mathbf c}=[c_0,\dots,c_N]^T` er lausn á línulegu
jöfnuhneppi :math:`A{\mathbf c}={\mathbf b}` þar sem stuðlarnir
fylkisins eru

.. math::

  a_{jk}={{\langle \varphi_j,\varphi_k\rangle}}_{L,B}
   ={{\langle \varphi_j,\varphi_k\rangle}}_L
   +\dfrac {p(a)\alpha_1}{\beta_1}\varphi_j(a)\varphi_k(a)
   +\dfrac{p(b)\alpha_2}{\beta_2}\varphi_j(b)\varphi_k(b)

og stuðlar hægri hliðarinnar eru

.. math::

  b_j={{\langle f,\varphi_j\rangle}}+T_B(\varphi_j)
   ={{\langle f,\varphi_j\rangle}}+\dfrac {p(a)\gamma_1}{\beta_1}\varphi_j(a)
   +\dfrac{p(b)\gamma_2}{\beta_2}\varphi_j(b).

Athugum nú að :math:`\varphi_0(a)=1`,
:math:`\varphi_j(a)=\varphi_j(b)=0`, fyrir :math:`j=1,\dots,N-1`, og
:math:`\varphi_N(b)=1`. Þetta segir okkur að áhrif jaðarskilyrðanna
gætir aðeins í :math:`0`-tu jöfnu og :math:`N`-tu jöfnu.

Í :math:`0`-tu línu jöfnuhneppins höfum við aðeins tvö stök frábrugðin
núlli í fylkinu og stakið í hægri hliðinni,

.. math::

  \begin{aligned}
   a_{00}&=\int_{x_0}^{x_1}\big(p(\varphi_0')^2+q\varphi_0^2\big)\, dx+
   \dfrac{p(a)\alpha_1}{\beta_1}
   \approx \dfrac{p(m_0)}{h_0}+\dfrac{h_0q(m_0)}3+\dfrac{p(a)\alpha_1}{\beta_1} 
   \\
   a_{01}&=
   \int_{x_0}^{x_1}\big(p\varphi_0'\varphi_1'+q\varphi_0\varphi_1\big)\,
   dx 
   \approx -\dfrac{p(m_0)}{h_0}+\dfrac{h_0q(m_0)}6.
   \\
   b_0&=\int_{x_0}^{x_1}f\varphi_0\, dx+\dfrac{p(a)\gamma_1}{\beta_1}
   \approx \dfrac{h_0(2f(x_0)+f(x_1))}6+\dfrac{p(a)\gamma_1}{\beta_1}.\end{aligned}

Hér höfum við nálgað fallgildin :math:`p(x)` og :math:`q(x)` á bilinu
:math:`[x_0,x_1]` með gildunum :math:`p(m_0)` og :math:`q(m_0)` í
miðpunktinum og reiknað heildin síðan nákvæmlega, en það er hægt að gera
með reglu Simpsons. Skýringin á nálgunarformúlunum sem notaðar eru til
þess að reikna stuðlana :math:`b_j` er að við nálgum fallið :math:`f`
með línulegri brúun á hverju hlutbilanna :math:`[x_j,x_{j+1}]`,

.. math::

  f(x)\approx f(x_0)\varphi_0(x)+f(x_1)\varphi_1(x)
   +\cdots+f(x_N)\varphi_N(x),

margföldum summuna með grunnföllunum og heildum síðan. Í línum
jöfnuhneppisins númer :math:`j=1,\dots,N-1` eru í mesta lagi þrjú stök í
fylkinu :math:`A` frábrugðin :math:`0` og síðan höfum við stakið í hægri
hliðinni,

.. math::

  \begin{aligned}
   a_{j,j-1}&=\int_{x_{j-1}}^{x_j}
   \big( p\varphi_{j-1}'\varphi_j'+q\varphi_{j-1}\varphi_j\big)\, dx
   \approx -\dfrac{p(m_{j-1})}{h_{j-1}}+\dfrac{h_{j-1}q(m_{j-1})}6,\\
   a_{j,j}&=\int_{x_{j-1}}^{x_{j+1}}
   \big( p(\varphi_j')^2+q \varphi_j^2\big)\, dx
   \approx \dfrac{p(m_{j-1})}{h_{j-1}}+\dfrac{p(m_j)}{h_j}
   +\dfrac{h_{j-1}q(m_{j-1})+h_jq(m_j)}3,\\
   a_{j,j+1}&=\int_{x_j}^{x_{j+1}}
   \big( p\varphi_j'\varphi_{j+1}'+q \varphi_j\varphi_{j+1}\big)\, dx
   \approx -\dfrac{p(m_j)}{h_j}
   +\dfrac{h_jq(m_j)}6,\\
   b_j&=\int_{x_{j-1}}^{x_{j+1}}f\varphi_j\, dx
   \approx \dfrac{h_{j-1}(f(x_{j-1})+2f(x_j))+h_j(2f(x_j)+f(x_{j+1}))}6.\end{aligned}

Hér höfum við nálgað fallgildin :math:`p(x)` og :math:`q(x)` á bilinu
:math:`[x_{j-1},x_j]` með gildunum :math:`p(m_{j-1})` og
:math:`q(m_{j-1})` í miðpunktinum og fallgildin á bilinu
:math:`[x_j,x_{j+1}]` með :math:`p(m_j)` og :math:`q(m_j)`. Síðan
reiknum við heildin yfir bilin nákvæmlega.

Í síðustu línunni númer :math:`N` verða tvö stök frábrugðin :math:`0` í
fylkinu og svo hægri hliðin

.. math::

  \begin{aligned}
   a_{N,N-1}&=\int_{x_{N-1}}^{x_N}
   \big( p\varphi_{N-1}'\varphi_N'+q\varphi_{N-1}\varphi_N\big)\, dx
   \approx -\dfrac{p(m_{N-1})}{h_{N-1}}+\dfrac{h_{N-1}q(m_{N-1})}6,\\
   a_{NN}&=\int_{x_{N-1}}^{x_{N}}
   \big( p\big(\varphi_N'\big)^2+q\varphi_N^2\big)\, dx
   +\dfrac{p(b)\alpha_2}{\beta_2}
   \approx \dfrac{p(m_{N-1})}{h_{N-1}}
   +\dfrac{h_{N-1}q(m_{N-1})}3+\dfrac{p(b)\alpha_2}{\beta_2},\\
   b_N&=\int_{x_{N-1}}^{x_{N}}f\varphi_N\, dx+\dfrac{p(b)\gamma_2}{\beta_2}
   \approx \dfrac{h_{N-1}(f(x_{N-1})+2f(x_N))}6+\dfrac{p(b)\gamma_2}{\beta_2}.\end{aligned}

Nákvæmnin nálguninni ræðst af stærstu billengdinni
:math:`\max_{1\leq i\leq N-1}h_i`. Auðvitað hefði mátt nálga :math:`p`,
:math:`q` og :math:`f` með einhverjum öðrum hætti í heildunum til þess
að fá meiri nákvæmni. Ef við hefðum til dæmis notað reglu Simpsons á
:math:`a_{j,j-1}`, þá hefðum við fengið

.. math::

  \begin{aligned}
   a_{j,j-1}&\approx-\dfrac{p(x_{j-1})+4p(m_{j-1})+p(x_j)} {6h_{j-1}}
   +\dfrac{h_{j-1}(q(x_{j-1})\cdot 0+4q(m_{j-1})\cdot \tfrac
    14+q(x_j)\cdot 0)}6\\
   &=-\dfrac{p(x_{j-1})+4p(m_{j-1})+p(x_j)}{6h_{j-1}}
   +\dfrac{h_{j-1}q(m_{j-1})}6.\end{aligned}

Fallsjaðarskilyrði
~~~~~~~~~~~~~~~~~~

Athugum nú aftur að :math:`\varphi_0(a)=1`,
:math:`\varphi_j(a)=\varphi_j(b)=0`, fyrir :math:`j=1,\dots,N-1`, og
:math:`\varphi_N(b)=0`. Þetta segir okkur að nálgunarfallið :math:`v`
uppfyllir :math:`v(a)=c_0` og :math:`v(b)=c_N`. Ef :math:`\beta_1=0`, þá
er :math:`u(a)=\gamma_1/\alpha_1` og við verðum að sjá til þess að
:math:`c_0= \gamma_1/\alpha_1`. Við höldum í jöfnuhneppið hér að framan
en breytum :math:`0`-tu jöfnunni, þannig að stuðlarnir verði

.. math:: a_{00}=1, \quad a_{0j}=0, \ j=1,\dots,N, \ b_0=\gamma_1/\alpha_1.

Ef :math:`\beta_2=0`, þá er :math:`u(b)=\gamma_2/\alpha_2` og við
verðum að sjá til þess að :math:`c_N= \gamma_2/\alpha_2`. Breytingin sem
við þurfum að gera á jöfnuhneppinu hér að framan er að í síðustu línunni
verður

.. math:: a_{Nj}=0, \ j=0,\dots,N-1, \quad  a_{NN}=1, \quad  \ b_N=\gamma_2/\alpha_2.

Nú er auðvelt að sannfæra sig um að við fáum rétta nálgun með aðferð í
tilfellunum þremur þegar lausnin er þekkt í öðrum eða báðum endapunktum.

Punktuppsprettur
~~~~~~~~~~~~~~~~

Við gerum alltaf ráð fyrir því að fallið :math:`f` sé samfellt, en
Galerkin aðferðin leyfir okkur að bæta við það punktuppsprettum
:math:`\sum_{k=1}^\nu Q_k\delta_{r_k}` í nokkrum ólíkum punktum
:math:`r_k` á bilinu :math:`[a,b]`. Það eina sem við þurfum að vita er
að

.. math::

  {{\langle f+\sum_{k=1}^\nu Q_k\delta_{r_k},\varphi_j\rangle}}
   ={{\langle f,\varphi_j\rangle}}
   +\sum_{k=1}^\nu Q_k\int_a^b \delta_{r_k}(x)\varphi_j(x)\, dx
   ={{\langle f,\varphi_j\rangle}}
   +\sum_{k=1}^\nu Q_k\varphi_j(r_k).

Ef við sjáum til þess að allir punktarnir séu hluti af skiptingunni,
:math:`r_k=x_{j_k}`, þá er summan alltaf núll nema þegar :math:`j` er
einn talnanna :math:`j_k` og þá er gildi summunnar jafnt :math:`Q_{k}`.

Þessi viðbót er mikilvæg og hún gefur okkur kost á meiri sveigjanleika í
aðferðinni. Í útfærslu hennar er ekkert annað gert en að hún er fyrst
útfærð fyrir samfellda fallið :math:`f` eins og lýst er hér að framan.
Síðan er framlagi punktuppsprettanna :math:`Q_k` bætt við stökin
:math:`b_{j_k}` sem áður voru reiknuð. Að lokum er jafnan
:math:`A{\mathbf c}={\mathbf b}` leyst og nálgunarlausnin :math:`v(x)`
er þar með fundin.

Bútaaðferð í tveimur víddum
---------------------------

Nú ætlum við að lýsa þeirri útfærslu á aðferð Galerkins sem algengast er
að nota við nálgun á lausnum á (:ref:`Link title <eq:22.1.2>`). Fyrst er svæðinu
:math:`\overline D` skipt í sammengi lokaðra þríhyrninga, eða öllu
heldur er :math:`\overline D` nálgað með sammengi lokaðra þríhyrninga.
Hornpunktar þríhyrninganna eru allir í :math:`\overline D` og þeir eru
númeraðir þannig að :math:`(x_j,y_j)\in D\cap \partial_2 D` fyrir
:math:`j=1,\dots,M` og :math:`(x_j,y_j)\in \partial_1 D` fyrir
:math:`j=N+1,\dots,M`.

Ritháttur fyrir þríhyrningana
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við þurfum að innleiða rithátt fyrir þríhyrningana. Við táknum þá með
:math:`T^{(m)}`, með :math:`m=1,\dots,L` og sammengi þeirra með
:math:`S`. Við viljum einnig geta tilgreint ákveðinn þríhyrning í netinu
með því að gefa upp hornpunkta hans. Ef þeir hafa númer :math:`A`,
:math:`B`, og :math:`C`, þá skrifum við :math:`T^{(m)}=T_{A,B,C}`. Hér
skiptir röð punktanna miklu máli og við gefum hana alltaf upp þannig að
farið er *rangsælis* eftir jaðri þríhyrningsins þegar punktarnir eru
taldir upp. (Því miður er bókstafurinn :math:`A` ofnotaður í þessari
grein, því hann stendur fyrir númer punkts í þríhyrningi, fylkið
:math:`A` og kemur auk þess fyrir í flatarheildunum. Við verðum bara að
lifa með þessari ónákvæmni.)

Myndin hér fyrir neðan sýnir svæði sem er sammengi rétthyrnings og
tveggja hálfskífa. Við getum lýst því sem mengi punkta með hnit sem
uppfylla ójöfnur,

.. math:: D=\{(x,y)\, ;\, -1-\sqrt{1-y^2}<x<1+\sqrt{1-y^2}, -1<y<1\}.

Það er nálgað með sammengi af lokuðum þríhyrningum sem eru 24 talsins.
Þeir eru númeraðir og eru númer þeirra eru sýnd innan sviga. Í netinu
eru 19 hornpunktar. Í punktum sem markaðir eru með opnum hring eru gildi
lausnarinnar óþekkt en í punktum sem markaðir eru með fylltri skífu eru
gildin þekkt. Hér er :math:`N=10` og :math:`M=19`. Athugið að
þríhyrningar nr. 1-16 eru allir einslaga og þríhyrningar nr. 17-24 eru
allir einslaga.

.. figure:: ./myndir/fig2206.svg
    :align: center
    :alt: Nálgun á svæði með þríhyrningum

    Mynd: Nálgun á svæði með þríhyrningum


Með rithætti okkar er

.. math::

  T^{(1)}=T_{1,4,6}=T_{4,6,1}=T_{6,1,4}, 
   \quad 
   T^{(2)}=T_{4,7,6}=T_{7,6,4}=T_{6,4,7}, 
   \quad 
   T^{(3)}=\dots.

Þríhyrningunum er lýst sem mengi

.. math::

  T_{A,B,C}=\{(x,y)=(1-s-t)(x_A,y_A)+s(x_B,y_B)+t(x_{C},y_{C})
   \,;\, s,t\in [0,1], s+t\leq 1\}.

Þríhyrninginn með hornpunktana :math:`(0,0)`, :math:`(1,0)` og
:math:`(0,1)` táknum við með :math:`E` og köllum hann
*einingarþríhyrning*,

.. math:: E=\{(s,t)\,;\, s,t\in [0,1], s+t\leq 1\}.

Athugum að við höfum gagntæka vörpun

.. math::

  \begin{aligned}
   t_{A,B,C}:E\to T_{A,B,C}, 
   \quad (s,t)&\mapsto  (1-s-t)(x_A,y_A)+s(x_B,y_B)+t(x_C,y_C)\\
   &=(x_A,y_A)+s(x_B-x_A,y_B-y_A)+t(x_C-x_A,y_C-y_A).\end{aligned}

Það er betra að lýsa þessu með fylkjamargföldun

.. math::

  \left[\begin{matrix} x \\ y  \end{matrix}\right]
   =
     \left[\begin{matrix} x_A \\ y_A  \end{matrix}\right]+
   \left[\begin{matrix}   x_B-x_A & x_C-x_A
   \\ y_B-y_A & y_C-y_A  
   \end{matrix}\right]
   \left[\begin{matrix}   s\\ t \end{matrix}\right]

Andhverfa :math:`t_{A,B,C}` er :math:`(x,y)\mapsto (s,t)`, þar sem
hnitin :math:`s` og :math:`t` eru leyst út úr jöfnuhneppinu

.. math::

  \left[\begin{matrix}   s\\ t \end{matrix}\right]
   =
   \left[\begin{matrix}   x_B-x_A & x_C-x_A
   \\ y_B-y_A & y_C-y_A 
   \end{matrix}\right]^{-1}
   \left[\begin{matrix}   x-x_A\\ y-y_A \end{matrix}\right]

Flatarmál þríhyrningsins :math:`T^{(m)}=T_{A,B,C}` er

.. math::

  |T^{(m)}|=|T_{A,B,C}|=\tfrac 12 |\det 
   \left[\begin{matrix}   x_B-x_A & x_C-x_A
   \\ y_B-y_A & y_C-y_A 
   \end{matrix}\right]|

og massamiðja hans er

.. math:: M_m=\tfrac 13\big((x_A,y_A)+(x_B,y_B)+(x_C,y_C)\big).

Við skilgreinum hliðarvigrana :math:`{\mathbf l}_A`,
:math:`{\mathbf l}_B` og :math:`{\mathbf l}_C` þannig að þeir liggi
mótlægum hliðum :math:`T_{A,B,C}` við hornpunkta númer :math:`A`,
:math:`B` og :math:`C` miðað við rangsælis umferðarstefnu eftir jaðrinum

.. math::

  {\mathbf l}_A=(x_C-x_B,y_C-y_B), \quad
   {\mathbf l}_B=(x_A-x_C,y_A-y_C) \quad \text{ og } \quad
   {\mathbf l}_C=(x_B-x_A,y_B-y_A).

Munið að snúningur um :math:`90^\circ` réttsælis er gefinn með
vörpuninni :math:`(x,y)\mapsto (y,-x)` og því eru vigrarnir

.. math::

  {\mathbf l}_A^R=(y_C-y_B,-x_C+x_B,), \quad
   {\mathbf l}_B^R=(y_A-y_C,-x_A+x_C,) \quad \text{ og } \quad
   {\mathbf l}_C^R=(y_B-y_A,-x_B+x_A,),

hornréttir á hliðarnar á móti hornunum númer :math:`A`, :math:`B` og
:math:`C` og snúa í stefnu ytri þvervigurs.

Þúfugrunnföll
~~~~~~~~~~~~~

Á sammengi þríhyrninganna :math:`S` skilgreinum við nú samfellt föll
:math:`\varphi_j`, :math:`j=1,\dots,M`, sem taka gildi á bilinu
:math:`[0,1]`, þannig að :math:`\varphi_j(x,y)=0` ef punkturinn
:math:`(x,y)` er ekki í neinum þríhyrninganna með hornpunkt númer
:math:`j`,

.. math::

  \varphi_j(x_k,y_k)=
   \begin{cases}
     1,&j=k,\\
   0,&j\neq k,
   \end{cases}

og graf fallsins :math:`\varphi_j` yfir sérhverjum þríhyrningi
:math:`T_{j,k,\ell}` er planið í :math:`{{\mathbb  R}}^3` gegnum
punktana

.. math::

  (x_j,y_j,1), \quad (x_k,y_k,0) \quad \text{ og } \quad 
   (x_\ell,y_\ell,0).

Lítum nú á allra einfaldasta tilfellið sem hægt er að hugsa sér og það
er þegar :math:`\overline D` er einingarþríhyrningurinn :math:`E` og við
veljum einn þríhyrning :math:`E` fyrir :math:`S`. Táknum með
:math:`\varphi_E` grunnfallið á :math:`E` sem tekur gildið :math:`1` í
:math:`(0,0)`. Formúlan fyrir :math:`\varphi_E` er

.. math:: \varphi_E(s,t)=1-s-t, \qquad (s,t)\in E,

því það er augljóst að graf :math:`\varphi_E` yfir :math:`E` er plan,
:math:`\varphi_E(0,0)=1` og :math:`\varphi_E(1,0)=\varphi_E(0,1)=0`.

Ef við viljum reikna út gildi fallsins :math:`\varphi_j` í punktinum
:math:`(x,y)` þá þurfum við fyrst að finna út hvort :math:`(x,y)` liggur
í einhverjum þríhyrningi :math:`T_{j,k,\ell}` sem hefur
:math:`(x_j,y_j)` fyrir hornpunkt. Ef svo er, þá gildir formúlan

.. math:: \varphi_j(x,y)=\varphi_E(t_{j,k,\ell}^{-1}(x,y)).

Jaðargildisverkefni á :math:`S`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nálgunarlausnin :math:`v(x,y)` fyrir jaðargildisverkefnið
(:ref:`Link title <eq:22.1.1>`) á að vera af gerðinni

.. math:: v(x,y)=\psi_0(x,y)+\sum_{j=1}^N c_j\varphi_j(x,y), \qquad (x,y)\in S.

þar sem fallið :math:`\psi_0(x,y)` hefur það hlutverk að nálga gefnu
jaðargildin á :math:`\partial_1D`,

.. math::

  \psi_0(x,y)=
   \sum_{k=N+1}^M \dfrac{\gamma(x_k,y_k)}{\alpha(x_k,y_k)}
   \varphi_k(x,y), \qquad (x,y)\in S.

Það tekur gildið :math:`\gamma(x_k,y_k)/\alpha(x_k,y_k)` í punktunum
:math:`(x_k,y_k)\in \partial_1D`, fyrir :math:`k=N+1,\dots,M` og brúar
línulega gildin á þeim strikum á jaðri :math:`S` sem tengja saman punkta
á :math:`\partial_1D`. Við táknum sammengi þessara línustrika með
:math:`\partial_1S` og látum :math:`\tilde \alpha`, :math:`\tilde \beta`
og :math:`\tilde \gamma` tákna föllin á :math:`\partial S` sem fást með
því að brúa gildi :math:`\alpha`, :math:`\beta` og :math:`\gamma` milli
viðeigandi endapunkta. Sammengi línustrikanna sem nálga
:math:`\partial_2D` táknum við með :math:`\partial_2S`.

Nálgunarfallið :math:`v` fyrir úrlausn á jaðargildisverkefninu
(:ref:`Link title <eq:22.1.1>`) er nálgunarfallið fyrir jaðargildisverkefni á
:math:`S`, sem lýst er með

.. math::

  \begin{cases}
   Lu=-\nabla\cdot \big( p\nabla u\big)+qu=f,
   &\text{ á innmengi } S,\\
   u(x,y)=\dfrac{\tilde \gamma(x,y)}{\tilde \alpha(x,y)}, 
   &(x,y)\in \partial_1 S,\\
   \tilde \alpha(x,y)u(x,y)+\tilde \beta(x,y)\dfrac{\partial u}{\partial n}(x,y)
   =\tilde \gamma(x,y), 
   &(x,y)\in \partial_2 S.
   \end{cases}

Athugið að við gætum þurft að stækka skilgreiningarmengi fallanna
:math:`p`, :math:`q` og :math:`f` þannig að þau nái yfir allt :math:`S`.
Nú snýst nálgun okkar á lausn verkefnisins (:ref:`Link title <eq:22.1.2>`) um að nota
þúfugrunnföllin á :math:`S` til þess að nálga lausnina á
(:ref:`Link title <eq:22.1.1a>`).

Nálgun á lausn jaðargildisverkefnisins á :math:`S`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Samkvæmt umfjöllun okkar hér að framan eigum við að leysa
:math:`A{\mathbf c}={\mathbf b}`, þar sem jafna (:ref:`Link title <eq:22.5.4>`) segir
að

.. math::

  a_{jk}=
   \iint_S\big(p\nabla \varphi_j\cdot \nabla \varphi_k
   +q\varphi_j\varphi_k\big)\, dA
   +\int_{\partial_2S}\dfrac{p\tilde \alpha}{\tilde \beta}
   \varphi_j\varphi_k\, ds\\

og

.. math::

  \begin{aligned}
     \label{eq:22.6.2}
   b_j&=\iint_S f\varphi_j\, dA
   +\int_{\partial_2 S}\dfrac{p\tilde \gamma}{\tilde \beta}
   \varphi_j\, ds \\
   &-\sum_{k=N+1}^M \dfrac{\gamma(x_k,y_k)}{\beta(x_k,y_k)}
   \bigg(\iint_{S}\big(p\nabla \varphi_j\cdot \nabla \varphi_k
   +q\varphi_j\varphi_k\big)\, dA 
   +\int_{\partial_2S}\dfrac{p\tilde \alpha}{\tilde \beta}
   \varphi_j\varphi_k\, ds
   \bigg) \nonumber \end{aligned}

Þessar formúlur fyrir :math:`a_{jk}` og :math:`b_j` eru heldur
ófrýnilegar við fyrstu sýn, en þær eru miklu auðveldari að fást við en
maður gæti haldið. Til dæmis er :math:`a_{jk}=0` ef punktur :math:`j` og
punktur :math:`k` eru ekki grannar í þríhyrninganetinu og því eru fá
stök í hverri línu fylkisins :math:`A` frábrugðin :math:`0`.

Bútun – Flatarheildin
~~~~~~~~~~~~~~~~~~~~~

Það er hyggilegt að líta á framlög bútanna :math:`T^{(m)}` hvers fyrir
sig í heildunum sem koma fyrir í formúlunum fyrir hverjum stuðli
:math:`a_{jk}` og :math:`b_j` og gera eðlilegar nálganir. Byrjum á því
að athuga að fyrra flatarheildið sem kemur fyrir formúlunni fyrir
:math:`b_j` er

.. math::

  \iint_S f\varphi_j\, dA =\sum_{(x_j,y_j)\in T^{(m)}}
   \iint_{T^{(m)}} f\varphi_j\, dA.

Hér er átt við að summan er aðeins tekin yfir þá þríhyrninga sem hafa
punkt :math:`j` fyrir hornpunkt. Rifjum upp að :math:`M_m` táknar
massamiðju þríhyrnings :math:`T^{(m)}`. Við setjum :math:`f_m=f(M_m)`,
:math:`p_m=p(M_m)` og :math:`q_m=q(M_m)`. Ef :math:`j` er einn horpunkta
:math:`T^{(m)}`, þá afmarkar graf :math:`\varphi_j` yfir :math:`T^{(m)}`
píramíta með hæð :math:`1` og því er heildi :math:`\varphi_j` yfir
:math:`T^{(m)}` jafnt :math:`\tfrac 13` af margfeldi flatarmáls
grunnflatar og hæð píramítans,

.. math:: \iint_{T^{(m)}}\varphi_j\, dA=\tfrac 13 |T^{(m)}|.

Við leyfum okkur að gera nálgunina

.. math::

  \iint_{T^{(m)}} f\varphi_j\, dA\approx f_m \iint_{T^{(m)}} \varphi_j\, dA
   =\tfrac 13 f_m|T^{(m)}|

og fáum því nálgunina

.. math::

  \iint_S f\varphi_j\, dA \approx \sum_{(x_j,y_j)\in T^{(m)}}
   \tfrac 13 f_m|T^{(m)}|.

Lítum næst á flatarheildin

.. math::

  \iint_S\big(p\nabla \varphi_j\cdot \nabla \varphi_k
   +q\varphi_j\varphi_k\big)\, dA
   =\sum_{(x_j,y_j),(x_k,y_k)\in T^{(m)}}
   \iint_{T^{(m)}}\big(p\nabla \varphi_j\cdot \nabla \varphi_k
   +q\varphi_j\varphi_k\big)\, dA

sem koma bæði fyrir í stuðlum fylkisins :math:`a_{jk}` og hægri
hliðarinnar :math:`b_j`. Hér er átt við að summan sé tekin yfir alla
þríhyrninga sem innihalda :math:`(x_j,y_j)` og :math:`(x_k,y_k)`. Þegar
:math:`j\neq k`, þá eru í mesta lagi tveir þríhyrningar sem um ræðir. Ef
:math:`j=k`, þá er átt við að summan sé tekin yfir alla þríhyrninga með
hornpunkt :math:`j`, eins og hér að framan.

Nú skulum við snúa okkur að því að nálga þessi heildi. Fyrst graf
:math:`\varphi_j` yfir :math:`T^{(m)}` er plan, þá tekur stigullinn
:math:`\nabla \varphi_j(x,y)` sama gildi í sérhverjum innri punkti í
:math:`T^{(m)}`. Fallið :math:`\varphi_j` tekur gildið :math:`0` á
hliðinni á móti punktinm :math:`j` og því er stigullinn í stefnu
vigursins :math:`{\mathbf l}_j^R`. Hæðin :math:`h_j` yfir á mótlæga hlið
er fjarlægð punkts :math:`j` yfir á hliðina og því er stefnuafleiða
fallsins :math:`\varphi_j` í stefnuna frá fótpunkti hæðarinnar í áttina
að punkti :math:`j` jöfn :math:`1/h_j`. Þetta gefur okkur formúlu fyrir
:math:`\nabla \varphi_j` á innmengi :math:`T^{(m)}`,

.. math::

  \nabla \varphi_j(x,y)
   =\dfrac {-1}{h_j}\dfrac{{\mathbf l}_j^R}{\|{\mathbf l}_j^R\|}.

Nú er :math:`|T^{(m)}|=\tfrac 12 \|{\mathbf l}_j^R\|h_j` og við höfum

.. math:: \nabla \varphi_j(x,y)=-\dfrac 1{2|T^{(m)}|}{{\mathbf l}_j^R}.

Ef :math:`j` og :math:`k` eru tveir hornpunktar :math:`T^{(m)}`, þá
gefur þessi formúla að

.. math::

  \nabla \varphi_j\cdot \nabla \varphi_k=
   \dfrac 1{4|T^{(m)}|^2}{{\mathbf l}_j^R\cdot {\mathbf l}_k^R}
   =\dfrac 1{4|T^{(m)}|^2}{{\mathbf l}_j\cdot {\mathbf l}_k}

gildir í innmengi :math:`T^{(m)}` og af henni leiðum við síðan

.. math::

  \iint_{T^{(m)}} p \nabla \varphi_j\cdot \nabla  \varphi_k\, dA
   \approx p_m 
   \iint_{T^{(m)}}  \nabla \varphi_j\cdot \nabla \varphi_k\, dA
   =\dfrac {p_m}{4|T^{(m)}|}{{\mathbf l}_j\cdot {\mathbf l}_k}.

Næst notfærum við okkur þekkta nálgunarformúlu fyrir tvöföld heildi
yfir þríhyrning sem segir að fyrir :math:`T^{(m)}=T_{A,B,C}` og samfellt
fall :math:`\psi(x,y)` á honum gildi

.. math::

  \iint_{T^{(m)}} \psi(x,y)\, dA
   \approx \tfrac 13\big(\psi_{A,B}+\psi_{B,C}+\psi_{C,A}\big)|T^{(m)}|,

þar sem :math:`\psi_{A,B}`, :math:`\psi_{B,C}` og :math:`\psi_{C,A}`
tákna gildi fallsins :math:`\psi` í miðpunktum hliðanna :math:`AB`,
:math:`BC` og :math:`CA` og að formúlan er nákvæm ef heildisstofninn
:math:`\psi` er margliða í :math:`(x,y)` af stigi :math:`\leq 2`. Af
þessu leiðir að

.. math::

  \iint_{T^{(m)}}  \varphi_j\varphi_k\, dA=
   \begin{cases}
     \tfrac 13
   \big(\tfrac 12\cdot \tfrac 12+\tfrac 12\cdot \tfrac 12+0\cdot 0\big)|T^{(m)}|
   =\tfrac 16 |T^{(m)}|,&j=k,\\
     \tfrac 13
   \big(\tfrac 12\cdot \tfrac 12+\tfrac 12\cdot 0+0\cdot \tfrac 12\big)|T^{(m)}|
   =\tfrac 1{12} |T^{(m)}|,&j\neq k.
   \end{cases}

Við notum nálgunarformúluna

.. math::

  \iint_{T^{(m)}} q\,  \varphi_j\varphi_k\, dA
   \approx
   \begin{cases}
   \tfrac 16 q_m\, |T^{(m)}|,&j=k,\\
   \tfrac 1{12} q_m\, |T^{(m)}|,&j\neq k.
   \end{cases}

Niðurstaðan er því að nálgun okkar á seinna flatarheildinu er

.. math::

  \iint_{T^{(m)}}\big(p\nabla \varphi_j\cdot \nabla \varphi_k
   +q\varphi_j\varphi_k\big)\, dA
   \approx 
   \dfrac {p_m}{4|T^{(m)}|}{{\mathbf l}_j\cdot {\mathbf l}_k}
   +\begin{cases}
   \tfrac 16 q_m\, |T^{(m)}|,&j=k,\\
   \tfrac 1{12} q_m\, |T^{(m)}|,&j\neq k.
   \end{cases}

Bútun – jaðarheildin
~~~~~~~~~~~~~~~~~~~~

Við eigum eftir að finna nálganir á vegheildunum yfir
:math:`\partial_2 S`,

.. math::

  \int_{\partial_2S}\dfrac{p\tilde \alpha}{\tilde \beta}
   \varphi_j\varphi_k\, ds
   \qquad \text{ og } \qquad 
   \int_{\partial_2 S}\dfrac{p\tilde \gamma}{\tilde \beta}
   \varphi_j\, ds.

Þá kemur regla Simpsons að góðu gagni. Munið að hún segir að

.. math::

  \int_a^b f(t)\, dt\approx \tfrac 16\big(f(a)+4f(\tfrac
   12(a+b))+f(b)\big)(b-a)

og að hún er nákvæm ef fallið :math:`f` er margliða af stigi
:math:`\leq 3`. Hugsum okkur nú að opna línustrikið milli punkta
:math:`A` og :math:`B` liggi í :math:`\partial_2S`, táknum miðpunkt þess
með :math:`m_{A,B}` og lengd þess með :math:`|S_{A,B}|`. Föllin
:math:`\varphi_A` og :math:`\varphi_B` uppfylla
:math:`\varphi_A(x_A,y_A)=\varphi_B(x_B,y_B)=1`,
:math:`\varphi_A(m_{A,B})=\varphi_B(m_{A,B})=\tfrac 12` og
:math:`\varphi_A(x_B,y_B)=\varphi_B(x_A,y_A)=0`, og því gefur regla
Simpsons okkur þrjár nálganir

.. math::

  \begin{gathered}
   \int_{S_{A,B}} \psi\, 
   \varphi_j^2\, ds
   \approx \tfrac 16\big(\psi(x_j,y_j)+ \psi(m_{A,B})\big) 
   |S_{A,B}|,  \qquad j=A,B,
   \\
   \int_{S_{A,B}} \psi\, 
   \varphi_A\varphi_B\, ds
   \approx \tfrac 16 \psi(m_{A,B}) |S_{A,B}|, \\
   \int_{S_{A,B}} \psi \, 
   \varphi_j\, ds
   \approx \tfrac 16\big(\psi(x_j,y_j)+2\psi(m_{A,B})\big) |S_{A,B}|
   \qquad j=A,B.\end{gathered}

Munið nú að á línustrikinu :math:`S_{A,B}` eru föllin
:math:`\tilde \alpha`, :math:`\tilde \beta` og :math:`\tilde \gamma`
fengin með línulegri brún á gildum fallanna :math:`\alpha`,
:math:`\beta` og :math:`\gamma` í punktum :math:`A` og :math:`B`.
Nálganir okkar verða því

.. math::

  \begin{gathered}
   \label{eq:22.6.10}
   \int_{S_{A,B}}\dfrac{p\tilde \alpha}{\tilde \beta}
   \varphi_j^2\, ds
   \approx \dfrac 16\bigg(
   p(x_j,y_j)
   \dfrac{\alpha(x_j,y_j)}
   {\beta(x_j,y_j)} 
   +p(m_{A,B})
   \dfrac{\alpha(x_A,y_A)+\alpha(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)}
   \bigg) |S_{A,B}|, \quad j=A,B. \\
   \int_{S_{A,B}}\dfrac{p\tilde \alpha}{\tilde \beta}
   \varphi_A\varphi_B\, ds
   \approx \frac 16
   p(m_{A,B}) \dfrac{\alpha(x_A,y_A)+\alpha(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)} |S_{A,B}|
   \label{eq:2.6.11}\\
   \int_{S_{A,B}}\dfrac{p\tilde \gamma}{\tilde \beta}
   \varphi_j\, ds
   \approx \dfrac 16\bigg(
   p(x_j,y_j)
   \dfrac{\gamma(x_j,y_j)}
   {\beta(x_j,y_j)} 
   +2
   p(m_{A,B})
   \dfrac{\gamma(x_A,y_A)+\gamma(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)}
   \bigg) |S_{A,B}|, \quad j=A,B.
   \label{eq:22.6.12}  \end{gathered}

Nálgun á stuðlum hneppisins :math:`A{\mathbf c}={\mathbf b}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú höfum við lýst því hvernig allir liðir í formúlunum
(:ref:`Link title <eq:22.6.1>`) og (:ref:`Link title <eq:22.6.2>`) eru nálgaðir og komið er að því
að lýsa því hvernig staðið er að reikningunum. Við byrjum á því að
núllstilla, :math:`a_{j,k}=0` og :math:`b_j=0` fyrir öll
:math:`j,k=1,\dots N`. Síðan tökum við bútana :math:`T^{(m)}` hvern á
fætur öðrum og reiknum út

.. math:: b^{(m)}=\tfrac 13 f_m|T^{(m)}|

og tölurnar í :math:`3\times 3` fylkinu

.. math::

  A^{(m)}=
     \left[\dfrac{p_m}{4|T^{(m)}|}
   \left[\begin{matrix}
   {\mathbf l}_A\cdot {\mathbf l}_A &     
   {\mathbf l}_A\cdot {\mathbf l}_B &     
   {\mathbf l}_A\cdot {\mathbf l}_C \\     
   {\mathbf l}_B\cdot {\mathbf l}_A &     
   {\mathbf l}_B\cdot {\mathbf l}_B &     
   {\mathbf l}_B\cdot {\mathbf l}_C \\     
   {\mathbf l}_C\cdot {\mathbf l}_A &     
   {\mathbf l}_C\cdot {\mathbf l}_B &     
   {\mathbf l}_C\cdot {\mathbf l}_C      
     \end{matrix}\right]
   +\dfrac{q_m|T^{(m)}|}{12}
   \left[
     \begin{matrix}
       2 & 1 & 1\\ 1&2&1\\ 1&1&2  \end{matrix}\right]
   \right]

Þessar stærðir köllum við *framlag bútsins* :math:`T^{(m)}=T_{A,B,C}`  *til
stuðla jöfnuhneppisins*. Samkvæmt (:ref:`Link title <eq:22.6.4aa>`) er
:math:`b^{(m)}` nálgunargildi okkar fyrir heildin þrjú,

.. math:: \iint_{T^{(m)}} f\varphi_j\, dA, \qquad j=A,B,C,

og samkvæmt (:ref:`Link title <eq:22.6.6a>`) eru stökin í fylkinu :math:`A^{(m)}`
nálgunargildi okkar á heildunum

.. math::

  \iint_{T^{(m)}}\big(p\nabla \varphi_j\cdot \nabla \varphi_k
   +q\varphi_j\varphi_k\big)\, dA, \qquad j,k=A,B,C.

Nú þarf að skoða gildin :math:`A`, :math:`B` og :math:`C` og bæta
:math:`b^{(m)}` og stökum fylkisins :math:`A^{(m)}` við viðeigandi
stuðla :math:`a_{j,k}` og :math:`b_j` þar sem :math:`j` og :math:`k`
einskorðast við mengið :math:`\{A,B,C\}`.

Við skoðum númerin :math:`A`, :math:`B` og :math:`C` á hornpunktunum og
uppfærum :math:`b`-gildin, :math:`b_j\leftarrow b_j+b^{(m)}`, fyrir þau
:math:`j=A,B,C` sem eru :math:`\leq N`.

Nú lítum við á fylkið :math:`A^{(m)}`.

Ef :math:`A > N`, þá gefur fyrsta línan :math:`A^{(m)}` ekkert framlag
til stuðlanna.

Ef :math:`A\leq N`, þá setjum við :math:`j=A` og uppfærum:
:math:`a_{j,j}\leftarrow a_{j,j}+A^{(m)}_{1,1}`.

Til þess að klára stökin í fyrstu línu :math:`A^{(m)}`, þá þurfum við að
skoða gildin á :math:`B` og síðan :math:`C`:

Ef :math:`B\leq N`, þá setjum við :math:`k=B` og uppfærum:
:math:`a_{j,k}\leftarrow a_{j,k}+A^{(m)}_{1,2}`.

Ef :math:`B >N`, þá setjum við :math:`k=B` og uppfærum:
:math:`b_{j}\leftarrow b_{j}-\gamma(x_k,y_k)A^{(m)}_{1,2}`.

Ef :math:`C\leq N`, þá setjum við :math:`k=C` og uppfærum:
:math:`a_{j,k}\leftarrow a_{j,k}+A^{(m)}_{1,3}`.

Ef :math:`C>N`, þá setjum við :math:`k=C` og uppfærum:
:math:`b_{j}\leftarrow b_{j}-\gamma(x_k,y_k)A^{(m)}_{1,3}`.

Nú hefur fyrsta línan í bútaframlaginu :math:`A^{(m)}` afgreidd og komið
að næstu línu. Ef :math:`B>N`, þá gefur hún ekkert framlag til
jöfnuhneppisins.

Ef :math:`B\leq N`, þá setjum við :math:`j=B` og uppfærum:
:math:`a_{j,j}\leftarrow a_{j,j}+A^{(m)}_{2,2}`.

Skoðum síðan gildin á :math:`A` og :math:`C`:

Ef :math:`A\leq N`, þá setjum við :math:`k=A` og uppfærum:
:math:`a_{j,k}\leftarrow a_{j,k}+A^{(m)}_{2,1}`.

Ef :math:`A >N`, þá setjum við :math:`k=A` og uppfærum:
:math:`b_{j}\leftarrow b_{j}-\gamma(x_k,y_k)A^{(m)}_{2,1}`.

Ef :math:`C\leq N`, þá setjum við :math:`k=C` og uppfærum:
:math:`a_{j,k}\leftarrow a_{j,k}+A^{(m)}_{2,3}`.

Ef :math:`C>N`, þá setjum við :math:`k=C` og uppfærum:
:math:`b_{j}\leftarrow b_{j}-\gamma(x_k,y_k)A^{(m)}_{2,3}`.

Nú sér lesandinn í hendi sér hvernig þriðja línan er afgreidd.

Þegar þríhyrningalistinn er á enda, þá höfum við nálgað öll
flatarheildin yfir :math:`S` sem koma fyrir í formúlunum
(:ref:`Link title <eq:22.6.1>`) og (:ref:`Link title <eq:22.6.2>`) og sett þau gildi inn í
:math:`a_{j,k}` og :math:`b_j`. Nú þurfum við að uppfæra :math:`a_{j,k}`
ogh :math:`b_j` með framlögum jaðarsins. Til þess þurfum við lista yfir
öll línustrikin í jaðrinum :math:`\partial_2S`. Hugsum okkur að
:math:`S_{A,B}` sé eitt slíkt strik.

Lítum fyrst á nálgunina

.. math::

  \int_{S_{A,B}}\dfrac{p\tilde \alpha}{\tilde \beta}
   \varphi_j^2\, ds
   \approx \dfrac 16\bigg(
   p(x_j,y_j)
   \dfrac{\alpha(x_j,y_j)}
   {\beta(x_j,y_j)} 
   +
   p(m_{A,B})
   \dfrac{\alpha(x_A,y_A)+\alpha(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)}
   )\bigg) |S_{A,B}|,

Þessi liður kemur fyrir í (:ref:`Link title <eq:22.6.1>`). Ef :math:`A\leq N`, þá
setjum við :math:`j=A` og uppfærum

.. math::

  a_{j,j}\leftarrow 
   a_{j,j}+\dfrac 16\bigg(
   p(x_j,y_j)
   \dfrac{\alpha(x_j,y_j)}
   {\beta(x_j,y_j)} 
   +
   p(m_{A,B})
   \dfrac{\alpha(x_A,y_A)+\alpha(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)}
   )\bigg) |S_{A,B}|.

Ef :math:`B\leq N`, þá setjum við :math:`j=B` og uppfærum
:math:`a_{j,j}` með sömu formúlu.

Horfum næst á liðinn

.. math::

  \int_{S_{A,B}}\dfrac{p\tilde \gamma}{\tilde \beta}
   \varphi_j\, ds
   \approx \dfrac 16\bigg(
   p(x_j,y_j)
   \dfrac{\gamma(x_j,y_j)}
   {\beta(x_j,y_j)} 
   +2
   p(m_{A,B})
   \dfrac{\gamma(x_A,y_A)+\gamma(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)}
   )\bigg) |S_{A,B}|

í formúlunni (:ref:`Link title <eq:22.6.2>`). Ef :math:`A\leq N`, þá setjum við
:math:`j=A` og uppfærum:

.. math::

  b_j\leftarrow b_j+
   \dfrac 16\bigg(
   p(x_j,y_j)
   \dfrac{\gamma(x_j,y_j)}
   {\beta(x_j,y_j)} 
   +2
   p(m_{A,B})
   \dfrac{\gamma(x_A,y_A)+\gamma(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)}
   )\bigg) |S_{A,B}|.

Ef :math:`B\leq N`, þá setjum við :math:`j=B` og uppfærum með sömu
formúlu.

Horfum að lokum á liðinn

.. math::

  \int_{S_{A,B}}\dfrac{p\tilde \alpha}{\tilde \beta}
   \varphi_A\varphi_B\, ds
   \approx \frac 16
   p(m_{A,B}) \dfrac{\alpha(x_A,y_A)+\alpha(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)} |S_{A,B}|

sem kemur bæði fyrir í (:ref:`Link title <eq:22.6.1>`) og (:ref:`Link title <eq:22.6.2>`). Ef
:math:`A\leq N` og :math:`B\leq N`, þá setjum við :math:`j=A` og
:math:`k=B` og uppfærum:

.. math::

  a_{j,k}\leftarrow a_{j,k} +\frac 16
   p(m_{A,B}) \dfrac{\alpha(x_A,y_A)+\alpha(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)} |S_{A,B}|
   \qquad \text{ og } \qquad a_{k,j}\leftarrow a_{j,k}.

Ef :math:`A\leq N` og :math:`B>N`, þá setjum við :math:`j=A` og
:math:`k=B` og uppfærum:

.. math::

  b_{j}\leftarrow b_{j} -\gamma(x_k,y_k)\cdot \frac 16
   p(m_{A,B}) \dfrac{\alpha(x_A,y_A)+\alpha(x_B,y_B)}
   {\beta(x_A,y_A)+\beta(x_B,y_B)} |S_{A,B}|

Ef hins vegar :math:`A>N` og :math:`B\leq N`, þá setjum við :math:`j=B`
og :math:`k=A` og uppfærum :math:`b_j` með þessari sömu formúlu. Ef bæði
:math:`A>N` og :math:`B>N`, þá eru báðir punktarnir á jaðrinum
:math:`\partial_1D` og strikið á milli þeirra því í :math:`\partial_1S`
en ekki í :math:`\partial_2S`.

Þegar listinn yfir strikin :math:`S_{A,B}` í jaðrinum
:math:`\partial_2S` er á enda, þá hefur nálgunarjöfnuhneppið verið
ákvarðað. Stuðlafylkið er rýrt (e. *sparse*), sem þýðir að fá stök í
hverri línu eru frábrugðin núlli. Fyrir þríhyrninganetið sem sýnt er á
myndinni hér að framan eru í mesta lagi 4 stök frábrugðin :math:`0` í
fyrstu línunni, 5 í annari línu, 4 í þriðju o.s.frv. Línuleg jöfnuhneppi
með rýrum fylkjum eru leyst með sérsniðnum reikniritum fyrir
:math:`LU`-þáttun, for- og endurinnsetningu og þau eru miklu hraðvirkari
en venjulega aðferðin fyrir Gauss-eyðingu. Upp á þetta er boðið í Matlab
og það er sjálfsagt að nýta sér það.

Þegar hneppið :math:`A{\mathbf c}={\mathbf b}` hefur verið leyst, þá
höfum við nálgunargildin :math:`c_j` í punktunum :math:`(x_j,y_j)` fyrir
:math:`j=1,\dots,N`.

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

**abcd)** Lítið á jaðargildisverkefnin dæmi 21.7.1.

\(i) Umritið verkefið yfir á veikt form.

\(ii) Setjið upp línulegt jöfnuhneppi fyrir Galerkin-aðferð til nálgunar
á lausninni :math:`u(x)` með annars stigs margliðu
:math:`v(x)=A+Bx+Cx^2`.

\(iii)Setjið upp línulegt jöfnuhneppi fyrir Galerkin-aðferð til nálgunar
á lausninni :math:`u(x)` með nálgunarfalli :math:`v(x)` sem er línuleg
samatekt þúfugrunnfalla með þriggja bila skiptingu.

Dæmi
^^^^

**abcdabcd)** Lítið á jaðargildisverkefnin dæmi 21.7.10 og 14.

\(i) Umritið verkefið yfir á veikt form.

\(ii) Setjið upp línulegt jöfnuhneppi fyrir Galerkin-aðferð til nálgunar
á lausninni :math:`u(x,y)` með annars stigs margliðu
:math:`v(x)=A+Bx+Cy+Dx^2+Exy+Fy^2`.

Dæmi
^^^^

Umritið jaðargildisverkefnið

.. math::

  \begin{cases}
   -\dfrac{\partial^2u}{\partial x^2}-\dfrac{\partial^2u}{\partial y^2}+u=0,
   &0<x<1.0, \ 0<y<0.6, \\
   u(x,0)=x, \ u(x,0.6)+\dfrac{\partial u}{\partial y}(x,0.6)=0, & 0<x<1.0,\\
   \dfrac{\partial u}{\partial x}(0,y)=y, \ u(1,y)=1, &0<y<0.6,
   \end{cases}

á veikt form og setjið upp jöfnuhneppi fyrir aðferð Galerkins með
nálgunarfall á forminu

.. math:: v(x,y)=A+Bx+Cy+Dx^2+Exy+Fy^2.

Dæmi
^^^^

Finnið veikt form jaðargildisverkefnisins

.. math::

  \begin{cases}
   -\dfrac{\partial^2u}{\partial x^2}-\dfrac{\partial^2u}{\partial y^2}=1,
   &0<x<1, \ 0<y<1, \\
   \dfrac{\partial u}{\partial y}(x,0)=0, \ \  
   \dfrac{\partial u}{\partial y}(x,1)=0, & 0<x<1,\\
   \dfrac{\partial u}{\partial x}(0,y)=0,\ \ 
   \dfrac{\partial u}{\partial x}(1,y)=2y,&0<y<1,
   \end{cases}

og ákvarðið síðan nálgunarlausnarfall á forminu :math:`A+Bxy` aðferð
Galerkins.

Dæmi
^^^^

Finnið veikt form jaðargildisverkefnisins

:math:`\begin{cases}
-\dfrac{\partial^2u}{\partial x^2}-\dfrac{\partial^2u}{\partial y^2}=x,
&0<x<1, \ 0<y<2-x, \\
u(0,y)=y, \ 0<y<2, &\dfrac{\partial u}{\partial n}(1,y)+u(1,y)=0, \ 0<y<1,  \\  
\dfrac{\partial u}{\partial n}(x,0)=-1, \ 0<x<1, 
&\dfrac{\partial u}{\partial n}(x,2-x)=0,\ 0<x<1,
\end{cases}`

og ákvarðið síðan nálgunarlausn á forminu :math:`A+Bx+Cy+Dxy` með aðferð
Galerkins.

Dæmi
^^^^

Lítum á jaðargildisverkefni á þríhyrningnum
:math:`D=\{(x,y)\in {{\mathbb  R}}^2 \,;\, 0<x<y<1\}`:

.. math::

  -\Delta u=xy \quad\text{ á } D,\quad
   \dfrac{\partial u}{\partial n}(x,x)=0,
   \quad 
   \dfrac{\partial u}{\partial n}(x,1)=x, 
   \quad 0<x<1, \quad 
   u(0,y)=y, \quad 0<y<1.

Umritið þetta verkefni yfir á veikt form og setjið síðan fram heildin
fyrir stuðlana í línulegu jöfnuhneppi til ákvörðunar á nálgunarlausn af
gerðinni :math:`v(x,y)=A+Bx+Cy+Dxy` sem byggir á aðferð Galerkins.

Dæmi
^^^^

Lítum á jaðargildisverkefni á þríhyrningnum
:math:`D=\{(x,y)\in {{\mathbb  R}}^2 \,;\, 0<y<x<1\}`:

:math:`\begin{cases}
-\Delta u=1, \ &\text{ á } D, \\
u(x,0)=x, \quad \dfrac{\partial u}{\partial n}(x,x)=\dfrac 1{\sqrt2},\ &0<x<1, \\
\dfrac{\partial u}{\partial n}(1,y)=0, \ &0<y<1.
\end{cases}`

Umritið þetta verkefni yfir á veikt form og reiknið út stuðlana í
línulegu jöfnuhneppi til ákvörðunar á nálgunarlausn af gerðinni :math:`v(x,y)=A+Bx+Cy+Dxy` sem byggir á aðferð Galerkins.

Dæmi
^^^^

Lítum á jaðargildisverkefni á svæðinu
:math:`D=\{(x,y)\in {{\mathbb  R}}^2 \,;\, 0<y<1+x, 0<x<1\}`:

.. math::

  \begin{cases}
   -\Delta u=x, \quad \text{ á } D,&\\
   \dfrac{\partial u}{\partial x}(x,1+x)-\dfrac{\partial u}{\partial
   y}(x,1+x)=0,
   \quad u(x,0)=0,&0<x<1, \\
   u(0,y)=y, \ 0<y<1, \quad \dfrac{\partial u}{\partial x}(1,y)=y^2, \
   0<y<2.&
   \end{cases}

Umritið jaðargildisverkefnið yfir á veikt form og setjið fram heildin
fyrir stuðlana í línulegu jöfnuhneppi til ákvörðunar á nálgunarlausn af
gerðinni :math:`v(x,y)=A+Bx+Cy+Dxy` sem byggir á aðferð Galerkins.
