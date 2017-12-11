CAUCHY-SETNINGIN OG CAUCHY-FORMÚLAN
===================================

Vegheildun :hover:`heildi` :hover:`heildi!vegheildi` :hover:`vegheildun`
------------------------------------------------------------------------

Ferlar og vegir
~~~~~~~~~~~~~~~

Ferill í :math:`{{\mathbb  C}}` er myndmengi samfellds falls
:math:`\gamma:[a,b]\to {{\mathbb  C}}`, þar sem gefin er stefnan frá
*upphafspunkti :hover:`ferill!upphafspunktur` :hover:‘upphafspunktur
ferils‘* :math:`u_\gamma=\gamma(a)` til *lokapunkts
:hover:`ferill!lokapunktur`* :hover:`lokapunktur ferils`
:math:`e_\gamma=\gamma(b)` ferilsins.

Ef :math:`u_\gamma=e_\gamma`, þá segjum við að ferilinn sé *lokaður
:hover:`lokaður ferill` :hover:`ferill`* :hover:`ferill!lokaður`.

Við segjum að ferillinn sé *einfaldur :hover:`einfaldur ferill`
:hover:`ferill`* :hover:`ferill!einfaldur` ef
:math:`\gamma(t_1)\neq \gamma(t_2)` fyrir :math:`t_1\neq t_2`, með
hugsanlegri undantekningu að :math:`\gamma(a)=\gamma(b)`. Að ferillinn
sé einfaldur þýðir nákvæmlega að hann skeri ekki sjálfan sig, hugsanlega
með þeirri undantekningu að upphafs- og lokapunkturinn sé sá sami.

Þó svo að ferillinn sé myndmengi samfellda fallsins :math:`\gamma`, þá
lítum við oft svo á að ferilinn sé fallið sjálft og köllum hann þá
*stikaferil*. Stöku sinnum viljum við þó gera greinarmun á þessu tvennu
og þá notum við táknið
:math:`{{{\operatorname{mynd}(\gamma)}}}=\{\gamma(t); t\in [a,b]\}` til
að tákna ferilinn og segjum að ferillinn sé *stikaður* með
:math:`\gamma`.

.. figure:: ./myndir/fig091.svg
    :align: center
    :alt: Vegir.

   Mynd: Vegir.

Ferill sem er samfellt deildanlegur á köflum kallast *vegur
:hover:`ferill!vegur` :hover:`vegur!ferill`* :hover:`vegur`.

Þetta þýðir að til er skipting :math:`a=t_0<t_1\cdots<t_n=b` á bilinu
:math:`[a,b]` þannig að :math:`\gamma` sé samfellt deildanlegt á opnu
bilunum :math:`]t_{j-1},t_j[`, :math:`j=1,\dots, n` og að í endapunktum
:hover:`endapunktur ferils` :hover:`ferill!endapunktur` bilanna séu bæði
hægri og vinstri afleiða til,

.. math::

  \begin{gathered}
   \lim_{h\to 0+}\dfrac{\gamma(t_j+h)-\gamma(t_j)}h, \qquad
   j=0,\dots,n-1,\\ 
   \lim_{h\to 0-}\dfrac{\gamma(t_j+h)-\gamma(t_j)}h, \qquad
   j=1,\dots,n.\end{gathered}

Lengd vega
~~~~~~~~~~

Ef :math:`\gamma` er vegur, þá er unnt að skilgreina lengd hans
:hover:`lengd!vegs` :hover:`vegur!lengd` sem

.. math:: L(\gamma)=\lim \sum_{j=1}^ N |\gamma(\tau_j)-\gamma(\tau_{j-1})|,

þar sem markgildið er tekið þegar fínleiki skiptingarinnar
:math:`a=\tau_0<\tau_1<\cdots<\tau_N=b` stefnir á núll. Með því að líta
á hægri hliðina í þessari jöfnu sem Riemann-summu, þá fáum við

.. math:: L(\gamma)=\int_a^ b |\gamma{{^{\prime}}}(t)| \, dt.

Heildið er vel skilgreint, því :math:`\gamma` er samfellt deildanlegt á
köflum og því er afleiðan samfelld alls staðar nema í endanlega mörgum
punktum, en í grennd um þá punkta er :math:`\gamma{{^{\prime}}}`
takmarkað.

Heildi með tilliti til bogalengdar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`C` vera veg og :math:`f` vera samfellt fall á :math:`C`.
Við skilgreinum heildið af :math:`f` yfir :math:`C` með tilliti til
bogalengdar :hover:`bogalengd` :hover:`heildi!m.t.t. bogalengdar` sem

.. math:: \int_Cf \, ds = \int_a^ b f(\gamma(t)) |\gamma{{^{\prime}}}(t)|\, dt.

Við notum líka táknin

.. math::

  \int_\gamma f\, ds,  \quad \int_C f\, |dz| \quad \text { og }
   \quad \int_\gamma f\, |dz|

fyrir þetta heildi, ef vegurinn :math:`C` er stikaður með
:math:`\gamma`. Við sjáum að heildið er óháð stikuninni, því ef við
stikum veginn með :math:`\gamma_1=\gamma\circ h`, þar sem
:math:`h:[c,d]\to [a,b]`, þá fáum við

.. math::

  \begin{aligned}
   \int_c^ d f(\gamma_1(t)) |\gamma_1{{^{\prime}}}(t)|\, dt&=
   \int_c^ d f(\gamma(h(t))) |\gamma{{^{\prime}}}(h(t))h{{^{\prime}}}(t)|\, dt\\
   &=
   \int_a^ bf(\gamma(\tau))|\gamma{{^{\prime}}}(\tau)| \, d\tau.\end{aligned}

Á þessari sömu formúlu sjáum við að heildið er jafnframt óháð stefnunni
á veginum.

Vegheildi
~~~~~~~~~

Ef :math:`f` er skrifað sem fall af :math:`z=x+iy` og
:math:`\gamma(t)=\alpha(t)+i\beta(t)`, þá skilgreinum við heildið af
:math:`f` yfir :math:`C` með tilliti til :math:`x` sem

.. math::

  \int_C f \, dx =\int_\gamma f\, dx = \int_a^ b f(\gamma(t))
   \alpha{{^{\prime}}}(t) \, dt

og heildið af :math:`f` yfir :math:`C` með tilliti til :math:`y` sem

.. math::

  \int_C f \, dy =\int_\gamma f\, dy = \int_a^ b f(\gamma(t))
   \beta{{^{\prime}}}(t) \, dt.

Ef :math:`f` og :math:`g` eru samfelld föll á :math:`C`, þá setjum við

.. math:: \int_C f\, dx +g \, dy = \int_C f\, dx + \int_C g\, dy.

Eðlilegt er að skilgreina heildið af :math:`f` yfir veginn :math:`C`
með tilliti til :math:`z` og :math:`\bar z` með formúlunum

.. math::

  \begin{gathered}
   \int_C f\, dz =\int_\gamma f\, dz= \int_\gamma f\, dx +if\, dy =
   \int_a^bf(\gamma(t))\gamma{{^{\prime}}}(t) \, dt,\\
   \int_C f\, d\bar z =\int_\gamma f\, d\bar z= \int_\gamma
   f\, dx -if\, dy = 
   \int_a^bf(\gamma(t))\overline{\gamma{{^{\prime}}}(t)} \, dt.\end{gathered}

Við athugum nú að öll þessi heildi eru háð stefnunni á :math:`C`.

Heildi yfir öfugan veg
~~~~~~~~~~~~~~~~~~~~~~

Við skilgreinum *öfuga veginn :hover:`vegur!öfugur` :hover:‘öfugur
vegur‘* :math:`\gamma_-` við :math:`\gamma` með formúlunni

.. math:: \gamma_-(t)=\gamma(a+b-t), \qquad t\in [a,b].

Öfugi vegurinn :math:`{\gamma}_-` við :math:`{\gamma}` stikar sama
mengi og :math:`{\gamma}`, en farið er yfir mengið í öfuga stefnu,
þ.e. \ :math:`u_{\gamma_-}=e_{\gamma}` og
:math:`e_{\gamma_-}=u_{\gamma}`. Við fáum því

.. math::

  \begin{aligned}
   \int_a^ b f(\gamma_-(t))\alpha_-{{^{\prime}}}(t) \, dt &=
   \int_a^ b f(\gamma(a+b-t))(-\alpha{{^{\prime}}}(a+b-t)) \, dt \\
   &=
   -\int_a^ b f(\gamma(t))\alpha{{^{\prime}}}(t) \, dt.\end{aligned}

Þar með er

.. math:: \int_{\gamma_-}f\, dx = -\int_\gamma f\, dx,

og á sama hátt fáum við

.. math::

  \int_{\gamma_-}f\, dy = -\int_\gamma f\, dy, \quad 
   \int_{\gamma_-}f\, dz = -\int_\gamma f\, dz \quad \text{ og } \quad
   \int_{\gamma_-}f\, d\bar z = -\int_\gamma f\, d\bar z.

Mat á heildum
~~~~~~~~~~~~~

Við þurfum oft að meta heildi og notfærum okkur þá oftast formúluna

.. math::

  | \int_C f(z)\, dz| \leq \int_\gamma |f(z)|\, |dz|\leq \max_{z\in C}
   |f(z)| \int_\gamma |dz|= \max_{z\in C}|f(z)|L(C).

Heildi yfir línustrik og hringboga 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mikilvægustu vegheildin, sem við þurfum að reikna út, eru tekin yfir
hringboga :hover:`hringbogi` og línustrik :hover:`línustrik`. Við skulum
líta á stikanir á þessum ferlum. Ef :math:`\alpha` og :math:`\beta` eru
tveir punktar í :math:`{{\mathbb  C}}`, þá látum við
:math:`{{\langle\alpha,\beta\rangle}}` tákna línustrikið á milli þeirra.
Það er gefið með stikuninni

.. math::

  \gamma:[0,1]\to {{\mathbb  C}}, \qquad \gamma(t)=(1-t)\alpha+t\beta, \qquad
   \gamma{{^{\prime}}}(t)= (\beta-\alpha), \qquad t\in [0,1],

og þar með er

.. math::

  \int_{{{\langle\alpha,\beta\rangle}}} f \, dz = (\beta-\alpha)\int_0^ 1
   f((1-t)\alpha+t\beta)\, dt.

Boginn af hringnum :math:`\partial S(\alpha,r)`, sem liggur milli
horngildanna :math:`t=a` og :math:`t=b`, :math:`b-a\leq 2{\pi}`, er
stikaður með

.. math::

  \gamma:[a,b]\to {{\mathbb  C}}, \qquad
   \gamma(t)= \alpha+re^{it}, \qquad
   \gamma{{^{\prime}}}(t)= ire^{it}, \qquad t\in [a,b],

og við fáum

.. math::

  \int_\gamma f \, dz = \int_a^ b f(\alpha+re^{it})ire^{it}\, dt
   = ir \int_a^ b f(\alpha+re^{it})e^{it}\, dt.

Auðvelt er að sýna fram á, að opið mengi :math:`X` er svæði þá og því
aðeins að hægt sé að tengja sérhverja tvo punkta saman með vegi, sem
samanstendur af línustrikum. Einnig er auðvelt að sýna að alltaf sé hægt
að velja ferilinn einfaldan og strikin samsíða hnitaásunum.

Stofnföll
~~~~~~~~~

Undirstöðusetning stærðfræðigreiningarinnar gefur okkur

.. \_se:10.1.3:

Setning
^^^^^^^

Gerum ráð fyrir að :math:`X` sé opið mengi og :math:`f\in C(X)`. Ef
:math:`f` hefur stofnfall :hover:`stofnfall` :math:`F`, þ.e.a.s. ef til
er fall :math:`F\in {{\cal O}}(X)` þannig að :math:`F{{^{\prime}}}=f`
þá er

.. math:: \int_\gamma f(z)\, dz = F(e_\gamma)-F(u_\gamma)

fyrir sérhvern veg :math:`\gamma` í :math:`X`. Sérstaklega gildir

.. math:: \int_\gamma f(z)\, dz = 0

fyrir sérhvern lokaðan veg :math:`\gamma` í :math:`X`. Ef :math:`X` er
svæði og :math:`f{{^{\prime}}}(z)=0` fyrir öll :math:`z\in X`, þá er
:math:`f` fastafall.

--------------

Green-setningin
---------------

Við látum :math:`X` vera opið hlutmengi af :math:`{{\mathbb  C}}`,
:math:`\Omega` vera opið hlutmengi af :math:`X` þannig að jaðarinn
:math:`\partial\Omega` á :math:`\Omega` sé í :math:`X` og gerum ráð
fyrir að :math:`\partial\Omega` sé einfaldur lokaður vegur sem stikaður
er í *jákvæða stefnu* :hover:`jákvæð stefna` miðað við :math:`\Omega`.
Þetta þýðir að

.. math:: \partial\Omega={{{\operatorname{mynd}(\gamma)}}}=\{\gamma(t); t\in [a,b]\}

þar sem :math:`\gamma(a)=\gamma(b)`,
:math:`\gamma(t_1)\neq \gamma(t_2)` ef :math:`t_1\neq t_2`,
:math:`t_1,t_2\in ]a,b[` og í punktum þar sem :math:`\gamma` er
deildanlegt, þá liggur :math:`\Omega` á vinstri hönd ef staðið er í
:math:`\gamma(t)` og horft er í stefnu :math:`\gamma{{^{\prime}}}(t)`.

.. figure:: ./myndir/fig092.svg
    :align: center
    :alt: Stikun á jaðri

   Mynd: Stikun á jaðri

Þá segir Green-setningin að um sérhver :math:`f,g\in C^ 1(X)` gildi

.. math::

  \int_{\partial\Omega} f\, dx +g \, dy =\iint_\Omega(\partial_x
   g-\partial_y f)\, dxdy.

Þegar þessi regla hefur verið sönnuð fyrir raungild föll :math:`f` og
:math:`g`, þá er alveg ljóst að hún gildir fyrir tvinnföll einnig, því
við tökum heildin af raun- og þverhlutum fyrir hvort um sig.

Green-setningin gildir fyrir almennari svæði en þetta, nefnilega svæði
:math:`\Omega` þar sem jaðarinn :math:`\partial\Omega` samanstendur af
einföldum vegum :math:`\gamma_j:[a_j,b_j]\to {{\mathbb  C}}`,
:math:`j=1,\dots,N`, sem skerast einungis í endapunktum og hafa jákvæða
stefnu miðað við :math:`\Omega`. Þetta þýðir að

.. math::

  \partial\Omega=\bigcup\limits_{j=1}^N\operatorname{mynd} (\gamma_j)=
   \bigcup\limits_{j=1}^N \{\gamma_j(t); t\in [a_j,b_j]\},

og að í punktunum :math:`\gamma_j(t)`, þar sem vegirnir eru
deildanlegir, er :math:`\Omega` á vinstri hönd ef staðið er í
:math:`\gamma(t)` og horft er í stefnu :math:`\gamma{{^{\prime}}}(t)`.

.. figure:: ./myndir/fig093.svg
    :align: center
    :alt: Stikun á jaðri sem myndaður er úr fjórum vegum

   Mynd: Stikun á jaðri sem myndaður er úr fjórum vegum

Við skilgreinum heildið af :math:`f` með tilliti til :math:`x` og
:math:`g` með tilliti til :math:`y` yfir jaðarinn :math:`\partial\Omega`
með formúlunni

.. math::

  \int_{\partial\Omega}f\, dx + g\, dy =\sum_{j=1}^N \int_{\gamma_j}f
   \, dx + g\, dy

og Green-setningin fær þá sama form og áður

.. math::

  \int_{\partial\Omega}f\, dx+g\, dy =\iint_\Omega
   (\partial_xg-\partial_yf)\, dxdy.

Cauchy-setningin og Cauchy-formúlan
-----------------------------------

Cauchy-setningin
~~~~~~~~~~~~~~~~

Nú skulum við gera ráð fyrir því að :math:`X` sé opið hlutmengi í
:math:`{{\mathbb  C}}` og að :math:`\Omega\subset X` uppfylli forsendur
Green-setningarinnar. Við tökum :math:`f\in C^ 1(X)`,
:math:`f(z)=u(x,y)+iv(x,y)`, :math:`z=x+iy`, þar sem :math:`u` og
:math:`v` eru raun- og þverhluti :math:`f`. Þá gefur Green-setningin,

.. math::

  \begin{aligned}
   \int_{\partial\Omega} f\, dz 
   &=\int_{\partial\Omega} (u+iv)\, (dx+idy)

  
   \\
   &=\int_{\partial\Omega} u\, dx - v\, dy
   +i\int_{\partial\Omega} v\, dx + u\, dy\nonumber\\
   &=\iint_{\Omega}\big(-\partial_x v-\partial_y u\big) \, dxdy
   +i\iint_{\Omega}\big(\partial_x u-\partial_y v\big) \, dxdy\nonumber\\
   &=\iint_{\Omega}i\big(\partial_x u+i\partial_x v\big)-
   \big(\partial_y u+i\partial_y v \big) \, dxdy \nonumber\\
   &=i\iint_{\Omega}\big(\partial_x f+i\partial_y f\big) \, dxdy.
   =2i\iint_{\Omega}\partial_{\bar z} f \, dxdy.\nonumber\end{aligned}

Nú erum við komin að undirstöðusetningu tvinnfallagreiningarinnar:

Setning
^^^^^^^

(*Cauchy-setningin :hover:`Cauchy!setningin` :hover:`Cauchy`*
:hover:`setning!Cauchy`).   Látum :math:`X` vera opið hlutmengi af
:math:`{{\mathbb  C}}`, :math:`\Omega\subset X` vera opið, þannig að
:math:`\partial\Omega\subset X` og gerum ráð fyrir að
:math:`\partial\Omega` samanstandi af endanlega mörgum vegum, sem
skerast aðeins í endapunktum og hafa jákvæða stefnu miðað við
:math:`{\Omega}`. Ef :math:`f\in C^1(X)`, þá er

.. math::

  \int_{\partial\Omega}f\, dz = 
   2i\iint_{\Omega}\partial_{\bar z} f \, dxdy.


  

Ef :math:`f\in {{\cal O}}(X)`, þá er

.. math::

  \int_{\partial\Omega}f\, dz = 0.


  

--------------

Stjörnusvæði
~~~~~~~~~~~~

Á sumum tegundum svæða fáum við miklu almennari útgáfu af
Cauchy-setningunni en hér hefur verið sönnuð:

Skilgreining
^^^^^^^^^^^^

Opið mengi :math:`X` kallast *stjörnusvæði með tilliti til punktsins*
:math:`\alpha\in X`, ef línustrikið :math:`{{\langle\alpha,z\rangle}}`
er innihaldið í :math:`X` fyrir sérhvert :math:`z\in X`. Við segjum að
:math:`X` sé *stjörnusvæði* :hover:`stjörnusvæði` ef það er stjörnusvæði
með tilliti til einhvers punkts í :math:`X`.

--------------

.. figure:: ./myndir/fig094.svg
    :align: center
    :alt: Dæmi um stjörnusvæði.

   Mynd: Dæmi um stjörnusvæði.

.. \_se:10.2.3:

Setning
^^^^^^^

Ef :math:`X` er stjörnusvæði með tilliti til punktsins :math:`\alpha`,
þá hefur sérhvert :math:`f\in {{\cal O}}(X)` stofnfall, sem gefið er með
formúlunni

.. \_10.2.4a:

.. math:: F(z)=\int_{{{\langle\alpha,z\rangle}}} f(\zeta)\, d\zeta, \qquad z\in X.

og þar með gildir

.. math::

  \int_\gamma f\, dz =0


  

fyrir sérhvern lokaðan veg :math:`\gamma` í :math:`X`.

--------------

Cauchy-formúlan
~~~~~~~~~~~~~~~

Nú ætlum við að beita Cauchy setningunni á fallið
:math:`\zeta\mapsto f(\zeta)/(\zeta-z)` þar sem :math:`z` er punktur í
svæðinu :math:`\Omega`. Þá fæst:

Setning
^^^^^^^

(*Cauchy-formúlan :hover:`Cauchy!formúlan`* :hover:`Cauchy`).   Gerum
ráð fyrir sömu forsendum og í Cauchy -setningunni. Ef
:math:`f\in C^1(X)`, þá gildir um sérhvert :math:`z\in \Omega` að

.. math::

  f(z)=\dfrac 1{2 \pi i}\int_{\partial\Omega}\dfrac
   {f(\zeta)}{\zeta-z}\, d\zeta -\dfrac 1{2\pi}\iint_{\Omega}
   \dfrac{(\partial_\xi+i\partial_\eta)f(\zeta)}
   {\zeta-z}\, d\xi d\eta, 

  

þar sem breytan í heildinu er :math:`{\zeta}={\xi}+i\eta`. Ef
:math:`f\in {{\cal O}}(X)`, þá er

.. math::

  f(z)=\dfrac 1{2 \pi i}\int_{\partial\Omega}\dfrac
   {f(\zeta)}{\zeta-z}\, d\zeta.

  

--------------

Meðalgildissetning
~~~~~~~~~~~~~~~~~~

Í sértilfellinu að :math:`\Omega` sé hringskífa, þá gefur
Cauchy-formúlan:

Setning
^^^^^^^

(*Meðalgildissetning* :hover:`meðalgildissetning`).   Látum :math:`X`
vera opið mengi í :math:`{{\mathbb  C}}`, :math:`f\in {{\cal O}}(X)`, :math:`z\in X` og gerum ráð fyrir að
:math:`\overline S(z,r)\subset X`. Þá gildir

.. math:: f(z)=\dfrac 1{2\pi} \int_0^{2\pi}f(z+re^{it})\, dt.

--------------

Setningin segir okkur að meðalgildi fágaðs falls yfir jaðar hringskífu
er jafnt gildi fallsins í miðpunkti skífunnar.

Útreikningur á heildum
~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við kanna, hvernig hægt er að beita Cauchy-formúlunni til þess
að reikna út ýmis ákveðin heildi. Til undirbúnings á því hugsum við
okkur að forsendurnar í Cauchy-setningunni séu uppfylltar og að
:math:`Q(z)` sé margliða af stigi :math:`m` með einfaldar núllstöðvar
:math:`\alpha_1,\dots,\alpha_m` og að engin þeirra liggi á
:math:`\partial\Omega`. Við skrifum upp stofnbrotaliðun á
:math:`1/Q(z)`, sem við fjölluðum um í grein 1.5, og fáum

.. math::

  \dfrac 1{Q(z)} = \dfrac 1{Q{{^{\prime}}}(\alpha_1)(z-\alpha_1)}+\cdots+
   \dfrac 1{Q{{^{\prime}}}(\alpha_m)(z-\alpha_m)}.

Þá getum við liðað heildið

.. math::

  \int_{\partial\Omega}\dfrac{f(z)}{Q(z)}\, dz =
   \dfrac 1{Q{{^{\prime}}}(\alpha_1)}\int_{\partial\Omega}\dfrac{f(z)}{z-\alpha_1}\,
   dz 
   +\cdots+
   \dfrac 1{Q{{^{\prime}}}(\alpha_m)}\int_{\partial\Omega}\dfrac{f(z)}{z-\alpha_m}\,
   dz.

Ef :math:`\alpha_j\in \Omega`, þá gefur Cauchy-formúlan

.. math::

  \int_{\partial\Omega}\dfrac{f(z)}{z-\alpha_j}\,
   dz  = 2\pi i f(\alpha_j).

Ef aftur á móti :math:`\alpha_j\not\in\Omega`, þá er fallið
:math:`f(z)/(z-\alpha_j)` fágað í grennd um
:math:`\Omega\cup\partial\Omega`, svo Cauchy-setningin segir okkur að
heildi þess með tilliti til :math:`z` yfir :math:`\partial\Omega` sé
:math:`0`. Niðurstaða þessa útreiknings er því:

.. \_set10.2.6:

Setning
^^^^^^^

Gerum ráð fyrir að forsendur Cauchy-setningarinnar séu uppfylltar og að
:math:`Q` sé margliða með einfaldar núllstöðvar
:math:`\alpha_1,\dots,\alpha_m` og að engin þeirra liggi á
:math:`\partial\Omega`. Þá er

.. math::

  \int_{\partial\Omega} \dfrac{f(z)}{Q(z)} \, dz =
   2\pi i\sum_{\alpha_j\in \Omega}
   \dfrac{f(\alpha_j)}{Q{{^{\prime}}}(\alpha_j)}.


  

--------------

Heildi yfir hring
~~~~~~~~~~~~~~~~~

Látum nú :math:`R(x,y)=p(x,y)/q(x,y)` vera rætt fall af tveimur
raunbreytistærðum og gerum ráð fyrir að :math:`q(x,y)\neq 0` ef
:math:`x^ 2+y^ 2=1`. Lítum á heildið

.. math::

  \int_0^{2\pi} R(\cos\theta,\sin \theta) \, d\theta.

  

Við athugum að ef :math:`z` er á einingarhringnum og við skrifum
:math:`z=e^{i\theta}`, þá er

.. math::

  \begin{gathered}
   \cos\theta=\dfrac 12(e^{i\theta}+e^{-i\theta})
   =\dfrac12(z+\dfrac 1z)=\dfrac{z^ 2+1}{2z},

  
   \\ 
   \sin\theta=\dfrac 1{2i}(e^{i\theta}-e^{-i\theta})
   =\dfrac1{2i}(z-\dfrac 1z)=\dfrac{z^ 2-1}{2iz},

  
   \\ 
   dz=ie^{i\theta}d\theta, \qquad d\theta=\dfrac 1{iz}dz.

  \end{gathered}

Heldið sem við viljum reikna er vegheildi

.. math::

  \int_0^ {2\pi}R(\cos\theta,\sin
   \theta)\, d\theta =
   \int_{\partial S(0,1)}R\big(\dfrac{z^ 2+1}{2z},\dfrac{z^ 2-1}{2iz}\big)
   \dfrac 1{iz}\, dz.

Það er alltaf hægt að umrita heildisstofninn í síðasta heildinu yfir á
:math:`f(z)/Q(z)`, þar sem :math:`Q` er margliða. Í því tilfelli að
:math:`Q` hefur einungis einfaldar núllstöðvar, þá getum við beitt
síðustu setningu.

Heildi yfir rauntalnalínuna
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við líta á heildi af gerðinni

.. math:: \int_{-\infty}^{+\infty}\dfrac{f(x)}{Q(x)}\, dx,

þar sem :math:`f` er fágað í grennd um :math:`{{\mathbb  R}}\cup H_+`,
þar sem :math:`H_+=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z>0\}` táknar efra hálfplanið og
:math:`Q(z)` er margliða sem hefur einungis einfaldar núllstöðvar í efra
hálfplaninu og engar núllstöðvar á :math:`{{\mathbb  R}}`. Nú lítum við
á svæðið
:math:`\Omega_r=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z>0, |z|<r\}`,
sem er hálf hringskífa. Jaðar hennar samanstendur af línustrikinu
:math:`{{\langle-r,r\rangle}}` og hálfhringnum
:math:`\gamma_r(t)=re^{it}`, :math:`t\in [0,\pi]`. Ef við veljum nú
:math:`r` það stórt að allar núllstöðvar :math:`Q` í :math:`H_+` séu
innihaldnar í :math:`\Omega_r`, þá gefur síðasta setning okkur að

.. math::

  \int_{\partial\Omega_r} \dfrac {f(z)}{Q(z)}\, dz
   =\int_{-r}^ r \dfrac {f(x)}{Q(x)}\, dx +
   \int_{\gamma_r}\dfrac{f(z)}{Q(z)}\, dz = 
   2\pi i\sum_{\alpha_j\in H_+} \dfrac{f(\alpha_j)}{Q{{^{\prime}}}(\alpha_j)}.

.. figure:: ./myndir/fig096.svg
    :align: center
    :alt: Lokuð hálfskífa

   Mynd: Lokuð hálfskífa

Ef heildið yfir :math:`{\gamma}_r` stefnir á :math:`0` þegar
:math:`r\to+{\infty}`, þá fæst niðurstaðan

.. math::

  \int_{-\infty}^ {+\infty} \dfrac {f(x)}{Q(x)}\, dx=
   2\pi i\sum_{\alpha_j\in H_+} \dfrac{f(\alpha_j)}{Q{{^{\prime}}}(\alpha_j)}.

Cauchy-formúlan fyrir afleiður
------------------------------

Cauchy-formúlan fyrir afleiður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur nú að forsendur Cauchy-setningarinnar séu uppfylltar og að
:math:`\partial\Omega` sé stikað af vegunum
:math:`\gamma_j:[a_j,b_j]\to {{\mathbb  C}}`, :math:`j=1,\dots,N`. Ef
við beitum Cauchy-formúlunni og skrifum upp stikunina á heildinu, þá
fæst

.. math::

  f(x+iy)=\dfrac 1{2\pi i}\sum_{j=1}^ N \int_{a_j}^ {b_j}
   \dfrac {f(\gamma_j(t))}{\gamma_j(t)-x-iy}\gamma_j{{^{\prime}}}(t)\, dt, 
   \qquad f\in {{\cal O}}(X).

Nú er heildisstofninn óendanlega oft deildanlegt fall af :math:`(x,y)`
á :math:`\Omega`, samfelldur á köflum sem fall af :math:`t` á
:math:`[a_j,b_j]` og þar að auki fágað fall af :math:`z=x+iy`. Við megum
því deilda fallið :math:`f` með því að taka afleiður undir heildið,

.. math::

  f{{^{\prime}}}(z)=\partial_xf(z)=
   \dfrac 1{2\pi i}\sum_{j=1}^ N \int_{a_j}^ {b_j}
   \dfrac {f(\gamma_j(t))}{(\gamma_j(t)-x-iy)^ 2}\gamma_j{{^{\prime}}}(t)\, dt


  

fyrir öll :math:`z\in \Omega`. Á þessari formúlu sjáum við síðan að
:math:`f{{^{\prime}}}` er fágað fall og að við megum beita
hlutafleiðunum undir heildið og fáum að afleiðan
:math:`f{{^{\prime\prime}}}` af :math:`f{{^{\prime}}}` er

.. math::

  f{{^{\prime\prime}}}(z)=\partial_x^ 2f(z)=
   \dfrac 2{2\pi i}\sum_{j=1}^ N \int_{a_j}^ {b_j}
   \dfrac {f(\gamma_j(t))}{(\gamma_j(t)-x-iy)^ 3}\gamma_j{{^{\prime}}}(t)\, dt.


  

Með því að velja :math:`\Omega` sem opnar skífur sem þekja :math:`X`,
þá fáum við að :math:`f\in C^{\infty}(X)` og að allar afleiður af
:math:`f` eru fáguð föll. Þegar við fjölluðum um Taylor-raðir í setningu
:ref:`Link title <se:2.3.7>`, þá skilgreindum við hærri
:math:`{{\mathbb  C}}`-afleiður :math:`f^{(n)}` af :math:`f` með

.. math:: f^{(0)}=f, \qquad f^{(n)}=\big(f^{(n-1)}){{^{\prime}}}, \quad n\geq 1.

Með þrepun fáum við nú:

.. \_set10.3.1:

Setning
^^^^^^^

(*Cauchy-formúlan fyrir afleiður :hover:`Cauchy!formúlan fyrir afleiður`*
:hover:`Cauchy`).   Látum :math:`X` og :math:`\Omega` vera eins og í
Cauchy-setningunni og tökum :math:`z\in \Omega`. Þá er sérhvert
:math:`f` í :math:`{{\cal O}}(X)` óendanlega oft deildanlegt á
:math:`X`, allar hlutafleiður af :math:`f` eru fáguð föll og

.. math::

  f^{(n)}(z)=
   \dfrac {n!}{2\pi i}\int_{\partial\Omega}
   \dfrac {f(\zeta)}{(\zeta-z)^ {n+1}}\, d\zeta.


  

--------------

Cauchy-ójöfnur
~~~~~~~~~~~~~~

Með því að skrifa :math:`\Omega` sem hringskífu, þá fáum við:

Fylgisetning
^^^^^^^^^^^^

(*Cauchy-ójöfnur* :hover:`Cauchy!ójöfnur`).   :hover:`Cauchy` Ef
:math:`X` er opið hlutmengi af :math:`{{\mathbb  C}}`,
:math:`\bar S(\alpha,\varrho)\subset X`, :math:`f\in {{\cal O}}(X)` og
:math:`|f(z)|\leq M` fyrir öll :math:`z\in \partial S(\alpha,\varrho)`, þá er

.. math::

  |f^{(n)}(\alpha)|\leq
   Mn!/\varrho^ n.

--------------

Setning Morera
~~~~~~~~~~~~~~

Eftirfarandi setning er andhverfa Cauchy-setningarinnar:

Setning
^^^^^^^

(*Morera :hover:`Morera-setningin`* :hover:`setning!Morera`).   Látum
:math:`X` vera opið mengi í :math:`{{\mathbb  C}}`, :math:`f\in C(X)` og
gerum ráð fyrir að

.. math:: \int_{\partial\Omega} f\, dz =0

fyrir sérhvert þríhyrningssvæði :math:`\Omega` þannig að
:math:`\Omega\cup \partial \Omega\subset X`. Þá er :math:`f\in {{\cal O}}(X)`.

--------------

Ein áhugaverð afleiðing af Cauchy-ójöfnunum er:

Setning Liurville
~~~~~~~~~~~~~~~~~

Setning
^^^^^^^

(*Liouville :hover:`Liouville setningin`* :hover:`setning!Liouville`).  
Látum :math:`f\in {{\cal O}}({{\mathbb  C}})` og gerum ráð fyrir að
:math:`f` sé takmarkað fall. Þá er :math:`f` fasti.

--------------

Sönnun
^^^^^^

Gerum ráð fyrir að :math:`|f(z)|\leq M` fyrir öll
:math:`z\in {{\mathbb  C}}`. Látum :math:`z\in{{\mathbb  C}}` og
:math:`\varrho>0`. Ójöfnur Cauchy gefa
:math:`|f{{^{\prime}}}(z)|\leq  M/\varrho`. Við látum
:math:`\varrho\to +\infty` og fáum að :math:`f{{^{\prime}}}(z)=0`. Þar
með er :math:`f` fastafall.

--------------

Undirstöðusetning algebrunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setning
^^^^^^^

(*Undirstöðusetning algebrunnar :hover:‘undirstöðusetning
algebrunnar‘*).   Sérhver margliða af af stigi :math:`n\geq 1` með
stuðla í :math:`{{\mathbb  C}}` hefur núllstöð í :math:`{{\mathbb  C}}`.

--------------

Samleitni í jöfnum mæli
-----------------------

Í útreikningum okkar þurfum við oft að vita hvort formúlur eins og

.. math::

  \begin{gathered}
   \lim_{t\to \alpha}\lim_{n\to+\infty}f_n(t)=
   \lim_{n\to+\infty}\lim_{t\to \alpha}f_n(t),\\
   \lim_{t\to \alpha}\sum_{n=0}^\infty f_n(t)=\sum_{n=0}^\infty
   \lim_{t\to \alpha}f_n(t)\\
   \lim_{n\to\infty}\ \int_a ^ b f_n(t)  \, dt=
   \int_a ^ b \lim_{n\to\infty}\
   f_n(t) \, dt,\\
   \sum_{n=0}^{\infty}\ \int_a ^ b f_n(t)  \, dt=
   \int_a ^ b \bigg(\sum_{n=0}^{\infty}\
   f_n(t)\bigg) \, dt,\\
   \dfrac d{dt} \lim_{n\to \infty} f_n(t) =\lim_{n\to\infty}
   \dfrac d{dt} f_n(t),\\
   \dfrac d{dt} \sum_{n=0}^{\infty} f_n(t) =\sum_{n=0}^{\infty}
   \dfrac d{dt} f_n(t),\end{gathered}

gildi, þar sem :math:`\{f_n\}` er runa af föllum sem skilgreind eru á
bilinu :math:`[a,b]`. Eins getum við þurft að vita hvort markfall
samleitinnar fallarunu sé samfellt eða deildanlegt. Við ætlum nú að
fjalla almennt um skilyrði á rununa :math:`\{f_n\}` sem tryggja að
þessar formúlur gildi.

Skilgreiningar og einfaldar afleiðingar þeirra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við byrjum á því að rifja upp skilgreininguna á samleitni fallaruna.
Látum :math:`A` vera mengi og :math:`\{ f_n\}` vera runu af föllum
:math:`f_n:A\to {{\mathbb  C}}`. Við segjum að runan :math:`\{f_n\}` stefni á fallið
:math:`f`, og táknum það með

.. math::

  \lim_{n\to\infty}f_n=f \qquad \text{og} \qquad
   f_n\to f,

ef talnarunan :math:`\{f_n(a)\}` stefnir á :math:`f(a)` fyrir öll
:math:`a\in A`. Þetta þýðir að fyrir sérhvert :math:`a\in A` og sérhvert
:math:`\varepsilon>0` er til :math:`N>0` þannig að

.. math:: |f_n(a)-f(a)|<\varepsilon, \qquad \text{fyrir öll} \quad n\geq N.

Talan :math:`N` getur verið háð bæði :math:`a` og :math:`\varepsilon`,
:math:`N=N(a,\varepsilon)`. Ef hægt er að velja töluna :math:`N` *óháð*
:math:`a`, þá segjum við að fallarunan :math:`\{f_n\}` stefni á fallið
:math:`f` *í jöfnum mæli á* :math:`A`:

Skilgreining
^^^^^^^^^^^^

Látum :math:`A` vera mengi og :math:`\{f_n\}` vera runu af föllum á
:math:`A` með gildi í :math:`{{\mathbb  C}}`. Við segjum að
:math:`\{f_n\}` stefni á fallið :math:`f` *í jöfnum mæli* á :math:`A`,
ef fyrir sérhvert :math:`\varepsilon>0` er til :math:`N` þannig að
:math:``\ \|f\_n(a)-f(a)\|<, :math:`` Við segjum að :math:`\{f_n\}` sé
*samleitin í jöfnum mæli á* :math:`A`, ef til er fall :math:`f` þannig
að :math:`\{f_n\}` stefni á :math:`f` í jöfnum mæli á :math:`A`. Við
segjum að fallaröðin :math:`\sum_{k=0}^\infty f_k` sé *samleitin í
jöfnum mæli* ef runan af hlutsummum :math:`\{\sum_{k=0}^ n f_k\}` er
samleitin í jöfnum mæli. Ef fallaröðin :math:`\sum_{k=0}^\infty |f_k|`
er samleitin í jöfnum mæli á :math:`A`, þá segjum við að
:math:`\sum_{k=0}^\infty f_k` sé *alsamleitin í jöfnum mæli*
:hover:`alsamleitinn í jöfnu mæli` á menginu :math:`A`.

--------------

Í því tilfelli að :math:`f_n` og :math:`f` eru raungild föll má einnig
orða skilgreininguna svo, að fyrir sérhvert :math:`\varepsilon>0` sé til
:math:`N=N(\varepsilon)`, þannig fyrir öll :math:`n\geq N` er graf
fallsins :math:`f_n` innihaldið í menginu

.. math:: \{(a,y); a\in A, f(a)-\varepsilon<y<f(a)+\varepsilon\}.

Sýnidæmi
^^^^^^^^

Myndin sýnir runu :math:`\{f_n\}`,
:math:`f_n:{{\mathbb  R}}\to {{\mathbb  R}}`, sem stefnir á núllfallið
:math:`f`, en gerir það ekki í jöfnum mæli, því
:math:`|f_n(1/n)-f(1/n)|=1` fyrir öll :math:`n`.

.. figure:: ./myndir/figA1.svg
    :align: center
    :alt: :math:`f_n\to 0`,

*ekki*

   Mynd: :math:`f_n\to 0`, *ekki í jöfnum mæli*

--------------

Samleitnipróf Weierstrass
~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum samanburðarpróf fyrir samleitni í jöfnum mæli:

Setning
^^^^^^^

(*Weierstrass–próf*).   Gerum ráð fyrir að :math:`\sum_{k=0}^  \infty f_k` sé fallaröð á menginu :math:`A`, :math:`\sum_{k=0}^ \infty M_k` sé samleitin röð af jákvæðum rauntölum og
:math:``\ 0\|f\_k(a)\| M\_k :math:`` Þá er röðin
:math:`\sum_{k=0}^ \infty f_k` samleitin í jöfnum mæli á :math:`A`.

--------------

Setning Abels
~~~~~~~~~~~~~

Setning
^^^^^^^

(*Abel :hover:`Abel-setningin`* :hover:`setning!Abel`).   Ef
:math:`\sum_{n=0}^\infty a_nz^n` er veldaröð með samleitnigeisla
:math:`\varrho`, þá er hún samleitin í jöfnum mæli á sérhverri
hringskífu með miðju í :math:`0` og geisla :math:`r<\varrho`.

--------------

Samleitni í jöfnum mæli og samfelldni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú ætlum við að kanna formúluna

.. math::

  \lim_{t\to \alpha}\lim_{n\to+\infty}f_n(t)=

  

  \lim_{n\to+\infty}\lim_{t\to \alpha}f_n(t).

.. \_se:3.4.5:

Setning
^^^^^^^

Látum :math:`A` vera hlutmengi af :math:`{{\mathbb  R}}^ m` og
:math:`\{f_n\}` vera runu af samfelldum föllum sem stefnir á fallið
:math:`f` í jöfnum mæli á :math:`A`. Þá er :math:`f` samfellt.

--------------

Fylgisetning
^^^^^^^^^^^^

Látum :math:`A` vera hlutmengi af :math:`{{\mathbb  R}}^ m` og
:math:`\sum_{k=0}^\infty f_k` vera röð af samfelldum föllum sem er samleitin í jöfnum mæli á
:math:`A`. Þá er :math:``\ \_xa \_k=0f\_k(x) = \_k=0\_xaf\_k(x),
:math:``

--------------

Samleitni í jöfnum mæli og heildun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Næsta viðfangsefni er formúlan

.. math::

  \lim_{n\to+\infty}\int_a ^ b f_n(t)  \, dt=
   \int_a ^ b \lim_{n\to+\infty}\
   f_n(t) \, dt.

  

.. \_se:B.3.1:

Setning
^^^^^^^

Gerum ráð fyrir að :math:`\{f_n\}` sé runa af heildanlegum föllum á
:math:`[a,b]`, að :math:`f_n\to f` í jöfnum mæli á bilinu :math:`[a,b]`.
Setjum

.. math::

  g_n(x)=\int_a^ x f_n(t)\, dt, \qquad
   \text{og } \qquad g(x)=\int_a^ x f(t)\, dt.

Þá stefnir :math:`g_n` á :math:` g` í jöfnum mæli á :math:`[a,b]`.

--------------

Hliðstæða þessarar setningar fyrir raðir er:

Fylgisetning
^^^^^^^^^^^^

Gerum ráð fyrir að :math:`\{f_k\}` sé runa af heildanlegum föllum á
bilinu :math:`[a,b]` og að röðin :math:`\sum_{k=0}^ \infty f_k` sé
samleitin í jöfnum mæli á bilinu :math:`[a,b]`. Þá er

.. math::

  \int_a^ x \sum_{k=0}^ \infty f_k(t)\, dt
   = \sum_{k=0}^ \infty \int_a^ x  f_k(t)\, dt, \qquad x\in [a,b].

--------------

Með því að skipta á stærðinni :math:`(b-a)` og rúmmáli mengisins
:math:`A\subset {{\mathbb  R}}^ m` í sönnuninni á setninguni hér fyrir framan, fáum
við með sömu röksemdarfærslu:

Setning
^^^^^^^

Látum :math:`A` vera takmarkað hlutmengi í :math:`{{\mathbb  R}}^ m`
og :math:`\{f_n\}` vera runu af heildanlegum föllum á :math:`A`. Ef
:math:`f_n\to f` í jöfnum mæli á :math:`A`, þá er

.. math:: \lim\limits_{n\to +\infty} \int_A f_n(x)\, dx = \int_Af(x)\, dx.

--------------

Hliðstæðar setningar gilda einnig um vegheildi með tilliti til
bogalengdar og heildi yfir svæði með endanlegt flatarmál.

Setning
^^^^^^^

Látum :math:`X` vera opið hlutmengi í :math:`{{\mathbb  C}}` og
:math:`\{f_n\}` vera runu af samfelldum föllum á :math:`X`. Ef
:math:`f_n\to f` í jöfnum mæli á sérhverju lokuðu og takmörkuðu
hlutmengi í :math:`X` og :math:`\gamma` er vegur í :math:`X`, þá er

.. math::

  \lim\limits_{n\to +\infty} \int_\gamma f_n(z)\, dz = 
   \int_\gamma f(z)\, dz.

--------------

Samleitni í jöfnum mæli og deildun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú snúum við okkur að formúlunni

.. \_B.4.1:

.. math::

  \dfrac d{dt} \lim_{n\to \infty} f_n(t) =\lim_{n\to\infty}
   \dfrac d{dt} f_n(t).

Setning
^^^^^^^

Látum :math:`\{f_n\}` vera runu af föllum í :math:`C^ 1([a,b])`, gerum
ráð fyrir að runan :math:`\{f_n{{^{\prime}}}\}` sé samleitin í jöfnum
mæli á :math:`[a,b]` og að til sé :math:`c\in [a,b]` þannig runan
:math:`\{f_n(c)\}` sé samleitin. Þá er stefnir :math:`\{f_n\}` á fall
:math:`f\in C^ 1([a,b])` í jöfnum mæli á :math:`[a,b]` og

.. math:: f{{^{\prime}}}(x)=\lim_{n\to \infty}f_n{{^{\prime}}}(x), \qquad x\in [a,b].

--------------

Með þrepun fáum við hliðstæða setningu fyrir hærri afleiður:

Fylgisetning
^^^^^^^^^^^^

Látum :math:`\{f_n\}` vera runu af föllum í :math:`C^m([a,b])` og gerum
ráð fyrir því að runurnar :math:`\{f_n^{(k)}\}`, :math:`0\leq k\leq m`,
séu samleitnar í jöfnum mæli á :math:`[a,b]` og táknum markgildi
:math:`\{f_n\}` með :math:`f`. Þá er :math:`f\in C^m([a,b])` og

.. math:: f^{(k)}(t)=\lim_{n\to +\infty} f_n^{(k)}(t), \qquad t\in [a,b].

--------------

Raðaútgáfan ef þessari setningu er:

Fylgisetning
^^^^^^^^^^^^

Látum :math:`\sum_{n=0}^\infty f_n` vera röð með liði :math:`f_n` í
:math:`C^m([a,b])` og gerum ráð fyrir því að raðirnar
:math:`\sum_{n=0}^\infty {f_n^{(k)}}`, :math:`0\leq k\leq m`, séu
samleitnar í jöfnum mæli á :math:`[a,b]` og setjum
:math:`f=\sum_{n=0}^\infty {f_n}`. Þá er :math:`f\in C^m([a,b])` og

.. math:: f^{(k)}(t)=\sum_{n=0}^{\infty} f_n^{(k)}(t), \qquad t\in [a,b].

--------------

Runur af fáguðum föllum
~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`\{f_n\}` er runa af samfelldum föllum á opnu mengi :math:`X`,
sem er samleitin í jöfnum mæli á sérhverju lokuðu og takmörkuðu
hlutmengi af :math:`X`, þá er markfallið :math:`f` samfellt á :math:`X`.
Setning Morera gefur okkur meira ef föllin eru fáguð:

Setning
^^^^^^^

Ef :math:`\{f_n\}` er runa af fáguðum föllum á opnu hlutmengi :math:`X`
af :math:`{{\mathbb  C}}`, sem er samleitin í jöfnum mæli á sérhverju
lokuðu og takmörkuðu hlutmengi af :math:`X`, þá er markfallið :math:`f`
fágað og

.. math:: \lim_{n\to \infty} f_n'(z)=f'(z)\qquad z\in X.

--------------

Við getum eins tekið fyrir óendanlegar raðir
:math:`\sum_{n=0}^\infty f_n` af fáguðum föllum og fáum að markfallið

.. math:: f(z) = \sum_{n=0}^\infty f_n(z), \qquad z\in X,

er fágað, ef hlutsummurnar :math:`s_N(z)=\sum_{n=0}^N f_n(z)` eru
samleitnar í jöfnum mæli á sérhverju lokuðu og takmörkuðu hlutmengi af
:math:`X` og þá má reikna út :math:`f'` með því að deilda röðina lið
fyrir lið,

.. math:: f'(z) = \sum_{n=0}^\infty f_n'(z), \qquad z\in X.

Samleitnar veldaraðir
---------------------

Liðun í veldaröð
~~~~~~~~~~~~~~~~

Látum :math:`X` vera opið mengi í :math:`{{\mathbb  C}}`,
:math:`f\in {{\cal O}}(X)`, :math:`\varrho>0` vera þannig að
:math:`\overline S(\alpha,\varrho)\subset X` og
:math:`f\in{{\cal O}}(X)`. Þá gefur Cauchy-formúlan okkur

.. math::

  f(z)=\dfrac 1{2\pi i}\int_{\partial S(\alpha,\varrho)}
   \dfrac{f(\zeta)}{\zeta-z}\, d\zeta, \qquad z\in S(\alpha,\varrho).


  

Við athugum að

.. math::

  \dfrac 1{\zeta-z}=\dfrac 1{(\zeta-\alpha)-(z-\alpha)}=
   \dfrac 1{\zeta-\alpha}\cdot\dfrac 1{1-(z-\alpha)/(\zeta-\alpha)}.

Nú er :math:`|z-\alpha|/|\zeta-\alpha|<1` ef
:math:`z\in S(\alpha,\varrho)` og
:math:`\zeta\in\partial S(\alpha,\varrho)` og þar með getum við liðað
þáttinn lengst til hægri í kvótaröð og fáum

.. math::

  \dfrac 1{\zeta-z}=\dfrac 1{\zeta-\alpha}\sum_{n=0}^ \infty

  

  \dfrac{(z-\alpha)^ n}{(\zeta-\alpha)^ n}=\sum_{n=0}^ \infty
   \dfrac{(z-\alpha)^ n}{(\zeta-\alpha)^ {n+1}}.

Röðin er greinilega samleitin í jöfnum mæli fyrir öll
:math:`\zeta\in\partial S(\alpha,\varrho)` og öll :math:`z\in \bar S(\alpha,\varrho-\varepsilon)`, :math:`\varepsilon<\varrho`, og því
megum við skipta á óendalegu summunni og heildinu í (:ref:`Link title <10.4.1>`). Það
gefur

.. math::

  f(z)=\sum_{n=0}^ \infty \bigg( \dfrac 1{2\pi i}
   \int_{\partial S(\alpha,\varrho)}
   \dfrac {f(\zeta)}{(\zeta-\alpha)^{n+1}}\, d\zeta\bigg)
   (z-\alpha)^ n.

Samkvæmt Cauchy-formúlunni fyrir afleiður er

.. math::

  \dfrac 1{2\pi i}
   \int_{\partial S(\alpha,\varrho)}
   \dfrac {f(\zeta)}{(\zeta-\alpha)^{n+1}}\, d\zeta=
   \dfrac{f^{(n)}(\alpha)}{n!}.

Niðurstaða þessa útreiknings er:

Setning
^^^^^^^

:math:`X` er opið hlutmengi af :math:`{{\mathbb  C}}`,
:math:`\alpha\in X`, :math:`\overline S(\alpha,\varrho)\subset X` og
:math:`f\in {{\cal O}}(X)`, þá er unnt að setja :math:`f` fram með
samleitinni veldaröð á skífunni :math:`S(\alpha,\varrho)`,

.. math::

  f(z)=\sum_{n=0}^ \infty a_n(z-\alpha)^ n,
   \qquad z\in S(\alpha,\varrho),


  

þar sem stuðlarnir :math:`a_n` eru ótvírætt ákvarðaðir og eru gefnir
með

.. math::

  a_n=\dfrac {f^{(n)}(\alpha)}{n!}.

  

Samleitnigeisli raðarinnar er stærri en eða jafn fjarlægðinni frá
:math:`\alpha` út á jaðar :math:`X`.

--------------

Skilgreining
^^^^^^^^^^^^

Ef :math:`X` er opið hlutmengi af :math:`{{\mathbb  C}}`,
:math:`\alpha\in X` og :math:`f\in {{\cal O}}(X)`, þá kallast veldaröðin

.. math::

  \sum\limits_{n=0}^\infty \dfrac{f^{(n)}(\alpha)}{n!}(z-\alpha)^n,

  

*Taylor-röð* :hover:`Taylor-röð` fágaða fallsins :math:`f` í punktinum
:math:`\alpha`. Ef :math:`\alpha=0`, þá kallast hún *Maclaurin-röð*
:hover:`Maclaurin-röð` fágaða fallsins :math:`f`.

--------------

Núllstöðvar fágaðra falla
~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Látum :math:`X` vera opið hlutmengi í :math:`{{\mathbb  C}}`,
:math:`\alpha\in X` og :math:`f\in {{\cal O}}(X)`. Punkturinn
:math:`\alpha` nefnist *núllstöð* :hover:`núllstöð` fágaða fallsins
:math:`f` ef :math:`f(\alpha)=0` og mengið :hover:`núllstöð!mengi`
:math:`{\cal N}(f)=\{\alpha\in X; f(\alpha)=0\}` kallast *núllstöðvamengi* :hover:`núllstöðvamengi` fágaða
fallsins :math:`f`. Ef :math:`f` er ekki núllfallið í
:math:`S(\alpha,\varrho)`, þar sem :math:`\varrho>0`, þá er til minnsta
gildi :math:`m>0` á :math:`n` þannig að :math:`f^{(n)}(\alpha)\neq 0`.
Talan :math:`m` nefnist *stig* :hover:`stig` núllstöðvarinnar
:hover:`stig!núllstöðvar` :math:`\alpha`. Ef fallið :math:`f` er núll í
heilli grennd um :math:`\alpha`, þá segjum við að :math:`f` hafi
núllstöð af *óendanlegu stigi :hover:`óendanlegt stig`
:hover:`stig!óendanlegt`* :hover:`stig` í :math:`\alpha`.

--------------

Eins og fyrir margliður þá er hægt að þátta núllstöðvar úr fáguðum
föllum:

.. \_se:10.4.3:

Setning
^^^^^^^

Fall :math:`f\in {{\cal O}}(X)` hefur núllstöð af stigi :math:`m>0` í
punktinum :math:`\alpha\in X` þá og því aðeins að til sé
:math:`g\in {{\cal O}}(X)` þannig að :math:`g(\alpha)\neq 0` og

.. math::

  f(z)=(z-\alpha)^ mg(z), \qquad z\in X.


  

--------------

Samsemdarsetningin
------------------

Samsemdarsetningin
~~~~~~~~~~~~~~~~~~

Við skulum rifja það upp að *svæði* :hover:`svæði` er opið samanhangandi
mengi, en það þýðir að sérhverja tvo punkta :math:`\alpha` og
:math:`\beta` í :math:`X` er unnt að tengja saman með vegi í :math:`X`.
Ef :math:`A` er hlutmengi í :math:`{{\mathbb  C}}`, þá er punktur
:math:`\alpha\in A` sagður vera *einangraður :hover:‘einangraður
punktur‘* í :math:`A` ef til er :math:`\varepsilon>0` þannig að
:math:`A\cap S(\alpha,\varepsilon)=\{\alpha\}`. Mengi sem samanstendur
af einangruðum punktum í :math:`A` er sagt vera *dreift :hover:‘dreift
mengi‘* í :math:`A`. Athugið að þetta þýðir að ekki er til nein runa af
*ólíkum* punktum í :math:`A` sem er samleitin og hefur markgildi í
:math:`A`.

Setning
^^^^^^^

(*Samsemdarsetning I* :hover:`samsemdarsetning`).   Ef :math:`X` er
svæði í :math:`{{\mathbb  C}}`, :math:`f,g\in {{\cal O}}(X)` og til er
punktur :math:`{\alpha}` í :math:`X` þannig að
:math:`f^{(n)}({\alpha})=g^{(n)}({\alpha})` fyrir öll :math:`n\geq 0`,
þá er :math:`f(z)=g(z)` fyrir öll :math:`z\in X`.

--------------

.. figure:: ./myndir/fig0910.svg
    :align: center
    :alt: Punktar tengdir með ferli

   Mynd: Punktar tengdir með ferli

Setning
^^^^^^^

Ef :math:`X` er svæði og :math:`f\in {{\cal O}}(X)` er ekki núllfallið,
þá er núllstöðvamengi :math:`{\cal N}(f)=\{z\in X; f(z)=0\}` fallsins
:math:`f` dreift hlutmengi af :math:`X`.

--------------

Sönnun
^^^^^^

Látum :math:`\alpha` vera núllstöð fallsins :math:`f` og gerum ráð fyrir
að hún sé af stigi :math:`m>0`. Samkvæmt setningu :ref:`Link title <se:10.4.3>` er
til fall :math:`g\in {{\cal O}}(X)` þannig að
:math:`f(z)=(z-\alpha)^ mg(z)` fyrir öll :math:`z\in X` og
:math:`g(\alpha)\neq 0`. Fyrst :math:`g` er samfellt, þá er til
:math:`\varepsilon>0`, þannig að :math:`g(z)\neq 0` fyrir öll
:math:`z\in S(\alpha,\varepsilon)`. Við höfum því :math:`{\cal N}(f)\cap S^\ast (\alpha,\varepsilon)=\varnothing` og þar með er :math:`{\cal N}(f)`
dreift mengi.

--------------

Við fáum nú enn sterkari útgáfu af samsemdarsetningunni:

Setning
^^^^^^^

(*Samsemdarsetning II* :hover:`samsemdarsetning`).   Ef :math:`X` er
svæði, :math:`f,g\in {{\cal O}}(X)` og :math:`f(a_j)=g(a_j)` þar sem
:math:`\{a_j\}` er runa af ólíkum punktum, sem hefur markgildi
:math:`a\in X`, þá er :math:`f(z)=g(z)` fyrir öll :math:`z\in X`.

--------------

Samsemdarsetningin hefur mikla þýðingu. Hún segir okkur meðal annars, að
ef :math:`f` er fall sem gefið er með veldaröð á bili :math:`I` á
:math:`{{\mathbb  R}}` og hægt er að útvíkka :math:`f` yfir í fágað fall
á svæði :math:`X` í :math:`{{\mathbb  C}}` sem inniheldur :math:`I`, þá
er útvíkkunin ótvírætt ákvörðuð. Hún segir okkur einnig að
:math:`e^ z=e^{x+iy}=e^ x(\cos y+i\sin y)` sé eina mögulega fágaða
útvíkkunin á veldisvísisfallinu :math:`x\mapsto e^ x` og að höfuðgrein
lografallsins :math:`{{\operatorname{Log}}}z` sé eina mögulega fágaða
framlengingin af náttúrlega lografallinu :math:`\ln x` yfir í mengið
:math:`{{\mathbb  C}}\setminus\{x\in {{\mathbb  R}}; x\leq 0\}`.

Hágildislögmálið
----------------

Hágildislögmálið
~~~~~~~~~~~~~~~~

Eftirfarandi setning er merkilegt hjálpartæki til þess að sanna alls
konar ójöfnur fyrir :math:`|f|`, þar sem :math:`f` er fágað fall:

.. \_set10.9.1:

Setning
^^^^^^^

(*Hágildislögmál I* :hover:`hágildislögmál`).   Ef :math:`X` er svæði og
:math:`f\in {{\cal O}}(X)`, þá getur :math:`|f(z)|` ekki haft staðbundið
hágildi í :math:`X` nema :math:`f` sé fastafall.

--------------

Setning
^^^^^^^

(*Hágildislögmál II* :hover:`hágildislögmál`).   Látum :math:`X` vera
takmarkað svæði :math:`f\in {{\cal O}}(X)\cap C(\overline X)` (samfellt á lokuninni
:math:`\overline X`). Þá tekur :math:`|f(z)|` hágildi á jaðri svæðisins
:math:`\partial X`.

--------------

Vafningstölur vega
------------------

Vafningstölur vega
~~~~~~~~~~~~~~~~~~

Látum :math:`\gamma:[a,b]\to {{\mathbb  C}}` vera feril og :math:`p`
vera punkt sem liggur ekki á ferlinum. Þá er hægt að skrifa

.. math:: \gamma(t)=p+r(t)e^{i\theta(t)}, \qquad r=|\gamma(t)-p|, \qquad t\in [a,b],

þar sem fallið :math:`\theta:[a,b]\to {{\mathbb  R}}` kallast *horn
fyrir ferilinn :hover:`horn!fyrir feril`* :math:`\gamma`  *mælt frá
punktinum* :math:`p`. Fallið :math:`\gamma` er samfellt og af því leiðir
að hægt er að velja :math:`\theta` samfellt. Ef :math:`\gamma` er vegur,
þá er fallið :math:`\gamma` samfellt og samfellt deildanlegt á köflum og
af því leiðir að hægt er að velja :math:`\theta` með sömu eiginleika.
Sönnun á þessum staðreynum er alls ekki flókin, en við látum hana eiga
sig. Fallið :math:`\theta` er ekki ótvírætt ákvarðað, en mismunur á
tveimur hornum :math:`\theta` og :math:`\varphi` fyrir ferillinn
:math:`\gamma` mælt frá :math:`p` er fast heiltölumargfeldi af
:math:`2\pi`. Þetta segir okkur að mismunurinn
:math:`\theta(b)-\theta(a)` sé óháður því hvernig hornið er valið. Ef
ferillinn :math:`\gamma` er lokaður, þá er
:math:`e^{i\theta(b)}=e^{i\theta(a)}`, sem segir okkur að
:math:`\theta(b)-\theta(a)` sé heiltölumargfeldi af :math:`2\pi`.

Skilgreining
^^^^^^^^^^^^

Ef :math:`\theta` er samfellt horn fyrir ferilinn :math:`\gamma` mælt
frá punktinum :math:`p`, þá kallast talan

.. math:: \theta(b)-\theta(a)

*hornauki ferilsins :hover:`hornauki ferils`* :math:`\gamma`  *séð frá
punktinum :math:`p`.* Ef :math:`\gamma` er lokaður ferill, þá nefnist
heiltalan

.. math:: I(\gamma,p)=\dfrac 1{2\pi}(\theta(b)-\theta(a))

*vafningstala ferilsins :hover:`ferill!vafningstala`
:hover:`vafningstala ferils`* :math:`\gamma`  *með tilliti til punktsins*
:math:`p`. Við segjum að :math:`\gamma` *vefjist utan um*
:hover:`vefjast utan um` :math:`p`, ef :math:`I(\gamma,p)\neq 0`. Mengi
allra punkta :math:`p` sem liggja ekki á ferlinum og ferillinn vefst
utan um köllum við *innmengi ferilsins* :hover:`innmengi ferils`
:math:`\gamma` og við táknum það með :math:`I(\gamma)`.

--------------

.. figure:: ./myndir/fig0911.svg
    :align: center
    :alt: Hornauki

   Mynd: Hornauki

Ef :math:`\gamma` er lokaður vegur, þá höfum við formúlu fyrir
vafningstölunni:

Setning
^^^^^^^

Ef :math:`\gamma` er lokaður vegur, þá er

.. math::

  I(\gamma,p)=\dfrac 1{2\pi i}\int_\gamma \dfrac{dz}{z-p}, 
   \qquad p\in {{\mathbb  C}}\setminus {{{\operatorname{mynd}(\gamma)}}}.

--------------

Lítum nú á mengið
:math:`X={{\mathbb  C}}\setminus {{{\operatorname{mynd}(\gamma)}}}` sem
samanstendur af öllum punktum :math:`p` sem eru ekki á ferlinum. Það er
hægt að skrifa :math:`X` sem sammengi :math:`X=\cup X_i`, :math:`i\in I`
af sundurlægum svæðum :math:`X_i`, þar sem :math:`I` er eitthvert
endanlegt eða teljanlega óendanlegt mengi. Þessi mengi :math:`X_i`
kallast *samhengisþættir* :hover:`samhengisþáttur` mengisins :math:`X`.
Á sérhverjum samhengisþætti :math:`X_i` er vafningstalan fasti sem fall
af :math:`p`, því

.. math::

  X_i\ni p\mapsto I(\gamma,p) = \dfrac 1{2\pi i}\int_\gamma \dfrac
   {dz}{z-p},

er heiltölugilt fágað fall. Eitt mengjanna :math:`X_i` er ótakmarkað og
við sjáum á formúlunni að :math:`I(\gamma,p)\to 0` ef
:math:`|p|\to +\infty`. Þar með er vafningstalan jöfn :math:`0` á
ótakmarkaða samhengisþættinum.

Mjög létt er að ákvarða vafningstölur fyrir alla skikkanlega vegi. Við
tökum einn punkt í hverjum samhengisþætti í
:math:`X\setminus{{{\operatorname{mynd}(\gamma)}}}` og drögum beint
línustrik frá honum yfir í ótakmarkaða samhengisþáttinn. Gæta verður
þess að í öllum skurðpunktum línunnar og vegarins sé snertivigurinn við
veginn ekki samsíða línunni. Við merkjum alla skurðpunkta, sem eru
þannig að vegurinn sker línuna frá hægri til vinstri séð frá punktinum
:math:`p`, með tölunni :math:`1`, og við merkjum hina punktana, sem eru
þá þannig að vegurinn sker línuna frá vinstri til hægri, með tölunni
:math:`-1`.

.. figure:: ./myndir/fig0912.svg
    :align: center
    :alt: Talning á skurðpunktum

   Mynd: Talning á skurðpunktum

Við leggjum síðan saman allar tölur á sama línustriki. Summan er
vafningstala fyrir alla punkta í samhengisþættinum, sem inniheldur
upphafspunkt striksins.

.. figure:: ./myndir/fig0913.svg
    :align: center
    :alt: Í samhengisþáttunum standa vafningstölurnar.

   Mynd: Í samhengisþáttunum standa vafningstölurnar.

Einfaldlega samanhangandi svæði
-------------------------------

Við höfum séð að um stjörnusvæði :math:`X` gildir að vegheildi sérhvers
fágaðs falls :math:`f` á :math:`X` yfir sérhvern lokaðan veg er
:math:`0`. Við sönnuðum þetta með því að sýna fram á að sérhvert fágað
fall :math:`f` á stjörnusvæði hafi stofnfall. Hægt er að alhæfa þetta
yfir á almennari flokk mengja:

Skilgreining
^^^^^^^^^^^^

Opið mengi :math:`X` er sagt vera *einfaldlega samanhangandi*
:hover:`einfaldrelga samhangandi mengi` ef :math:`I(\gamma)\subset X`
fyrir sérhvern lokaðan veg :math:`\gamma` í :math:`X`.

--------------

Innmengi vegarins :math:`\gamma` samanstendur af öllum punktum :math:`p`
sem :math:`\gamma` vefst utanum, þar sem við segjum að :math:`\gamma`
vefjist utanum :math:`p` ef vafningstalan :math:`I(\gamma,p)` er
frábrugðin :math:`0`. Skilyrðið í skilgreiningunni segir því að í
einfaldlega samanhangandi mengi geti lokaðir vegir einungis vafist
utanum punkta í :math:`X` og þar með að þeir geti ekki vafist utan um
punkta í fyllimenginu :math:`{{\mathbb  C}}\setminus X`. Þetta þýðir að
mengið :math:`X` hafi engin göt. Sem dæmi má nefna að allar hringskífur
eru einfaldlega samanhangandi, en hringkragar eru það ekki.

.. figure:: ./myndir/fig0914.svg
    :align: center
    :alt: Einfaldlega og ekki einfaldlega samanhangandi svæði

   Mynd: Einfaldlega og ekki einfaldlega samanhangandi svæði

Einfaldlega samanhangandi svæði einkennast af fjölbreytilegum
eiginleikum:

Setning
^^^^^^^

Látum :math:`X` vera svæði í :math:`{{\mathbb  C}}`. Þá er eftirfarandi
jafngilt:

\(i) :math:`X` er einfaldlega samanhangandi.

\(ii) Sérhvert fágað fall á :math:`X` hefur stofnfall.

\(iii) Fyrir sérhvert :math:`f\in {{\cal O}}(X)` og sérhvern lokaðan veg
:math:`\gamma` í :math:`X` er

.. math::

  \int_\gamma f(\zeta) \, d\zeta = 0.


  

\(iv) Fyrir sérhvert :math:`f\in {{\cal O}}(X)` og sérhvern lokaðan veg
:math:`\gamma` í :math:`X` er

.. math::

  f(z)I(\gamma,z) = \dfrac 1{2\pi i}\int_\gamma \dfrac{f(\zeta)}
   {\zeta-z} \, d\zeta.


  

\(v) Sérhvert núllstöðvalaust fágað fall á :math:`X` hefur logra,
þ.e. ef :math:`f\in {{\cal O}}(X)` og :math:`{\cal N}(f)=\varnothing`,
þá er til :math:`g\in {{\cal O}}(X)` þannig að :math:`f(z)=e^{g(z)}`,
:math:`z\in X`.

\(vi) Sérhvert núllstöðvalaust fágað fall á :math:`X` hefur fágaða
:math:`n`-tu rót fyrir öll :math:`n\geq 1`, þ.e. ef
:math:`f\in {{\cal O}}(X)` og :math:`{\cal N}(f)=\varnothing`, þá er til
:math:`h\in {{\cal O}}(X)` þannig að :math:`f(z)=h(z)^n`,
:math:`z\in X`.

\(vii) Sérhvert núllstöðvalaust fágað fall á :math:`X` hefur fágaða aðra
rót.

————–
