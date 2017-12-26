
Nálganir á lausnum upphafs- og jaðargildisverkefna fyrir hlutafleiðujöfnur
==========================================================================

Inngangur
---------

Tímaháð verkefni
----------------

Við tökum nú fyrir upphafs- og jaðargildisverkefnið

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial t}+L_xu
   =\dfrac{\partial u}{\partial t}-
   \dfrac{\partial }{\partial x}\bigg(p\dfrac{\partial u}{\partial x}\bigg)+qu=f, 
   &x\in (a,b), \quad t>0,\\
   u(a,t)=\gamma_1, \  
   \beta_1u(b,t)+\beta_2\dfrac{\partial u}{\partial x}(b,t)=\gamma_2, &t>0,\\
   u(x,0)=u_0(x), &x\in [a,b],
   \end{cases}

þar sem :math:`p` og :math:`q` eru föll á :math:`[a,b]`, en lausnin
:math:`u` og hægri hliðin :math:`f` eru föll af tveimur breytistærðum á
menginu :math:`\{(x,t)\, ;\, x\in [a,b], t\geq 0\}`. Upphafsgildin eru
gefin með falli :math:`u_0` á bilinu :math:`[a,b]`. Við hugsum okkur
:math:`x` sem rúmbreytistærð og :math:`t` sem tíma.

Við höfum valið fallsjaðarskilyrði í vinstri punkti og gefum okkur að
:math:`\beta_2\neq 0`. Auðvelt er að yfirfærða hinar gerðir
jaðarskilyrðanna sem við höfum verið að skoða yfir á þetta vandamál.

Byrjum á því að snúa þessu verkefni yfir á veikt form með því að velja
:math:`\varphi\in C^1[a,b]` og heilda yfir bilið :math:`[a,b]`. Við
festum :math:`t` og lítum á :math:`x\mapsto u(x,t)` og
:math:`x\mapsto f(x,t)` sem föll af :math:`x` í þeirri heildun.
Hlutheildun gefur okkur

.. math::

  \begin{gathered}
   \int_a^b\dfrac{\partial u}{\partial t}\varphi\, dx+
   \int_a^b
   \bigg(-\dfrac{\partial }{\partial x}\bigg(p\dfrac{\partial u}{\partial x}\bigg)+qu\bigg)\varphi
   \, dx \\
   =\int_a^b\dfrac{\partial u}{\partial t}\varphi\, dx
   -\bigg[p(x)\dfrac{\partial u}{\partial x}(x,t)\varphi(x)\bigg]_a^b+
   \int_a^b
   \bigg(p\dfrac{\partial u}{\partial x}\varphi'+qu\varphi\bigg)
   \, dx =\int_a^b f\varphi\, dx.\end{gathered}

Ef við stingum inn jaðargildunum og veljum :math:`\varphi` þannig að
:math:`\varphi(a)=0`, þá fáum við jöfnuna

.. math::

  {{\langle u'_t(\cdot,t),\varphi\rangle}}+{{\langle u(\cdot,t),\varphi\rangle}}_L
   +\dfrac{p(b)\beta_1}{\beta_2}u(b,t)\varphi(b)
   ={{\langle f(\cdot,t),\varphi\rangle}}
   +\dfrac{p(b)\gamma_2}{\beta_2}\varphi(b)

þar sem innfeldin eru þau sömu og áður,
:math:`u'_t=\partial u/\partial t` og :math:`u(\cdot,t)` táknar fallið
:math:`x\mapsto u(x,t)`, þ.e.a.s. hér er litið á :math:`u` sem fall af
:math:`x` fyrir fast :math:`t`. Þessa jöfnu getum við einnig skrifað sem

.. math::

  {{\langle u'_t(\cdot,t),\varphi\rangle}}+{{\langle u(\cdot,t),\varphi\rangle}}_{L,B}
   ={{\langle f(\cdot,t),\varphi\rangle}}+T_B(\varphi).

Nú veljum við fall :math:`\varphi_0\in PC^1[a,b]` sem uppfyllir
:math:`\varphi_0(a)=1` og síðan
:math:`\varphi_1,\dots,\varphi_N\in PC^1[a,b]` sem uppfylla óhliðraða
jaðarskilyrðið :math:`\varphi_j(a)=0`. Nálgunarfallið okkar á nú að vera
af gerðinni

.. math:: v(x,t)=\gamma_1\varphi_0(x)+c_1(t)\varphi_1(x)+\cdots+c_N(t)\varphi_N(x),

þar sem stuðlarnir :math:`c_1(t),\dots,c_N(t)` eru valdir þannig að
jöfnuhneppið

.. math::

  {{\langle v'_t(\cdot,t),\varphi_i\rangle}}+{{\langle v(\cdot,t),\varphi_i \rangle}}_{L,B}
   ={{\langle f(\cdot,t),\varphi_i\rangle}}+T_B(\varphi_i), \qquad i=1,\dots,N,

í samræmi við það sem krafist er í aðferð Galerkins. Nú stingum við inn
í formúluna fyrir :math:`v(x,t)` og fáum afleiðujöfnuhneppi sem
stuðlarnir :math:`c_j(t)` eiga að uppfylla,

.. math::

  \sum_{j=1}^Nc_j'(t){{\langle \varphi_j,\varphi_i\rangle}}
   +\gamma_1{{\langle \varphi_0,\varphi_i\rangle}}_{L,B}
   +\sum_{j=1}^N c_j(t){{\langle \varphi_j,\varphi_i\rangle}}_{L,B}
   ={{\langle f(\cdot,t),\varphi_i\rangle}}+T_B(\varphi_i).

Við getum snúið þessu hneppi yfir á fylkjaformið

.. math:: B\mathbf c'(t)=-A\mathbf c(t)+\mathbf b(t),

þar sem fylkið :math:`A=(a_{ij})` er gefið með formúlunni
(:ref:`Link title <1.38a>`) og stuðlar vigursins :math:`\mathbf b(t)` verða eins og í
formúlunni (:ref:`Link title <1.40a>`) gefnir með

.. math:: b_i(t)={{\langle f(\cdot,t),\varphi_i\rangle}}+T_B(\varphi_i)-{{\langle \varphi_0,\varphi_i\rangle}}_{L,B} \gamma_1,  \qquad i=1,\dots,N.

Fylkið :math:`B=(b_{ij})` er gefið með

.. math:: b_{ij}={{\langle \varphi_j,\varphi_i\rangle}}.

Út frá upphafsskilyrðunum krefjumst við þess að stuðlarnir uppfylli

.. math:: {{\langle v(\cdot,0),\varphi_i\rangle}}={{\langle u_0,\varphi_i\rangle}}, \qquad 1=1,\dots,N,

sem jafngildir

.. math::

  \gamma_1{{\langle \varphi_0,\varphi_i\rangle}}+\sum_{j=1}^Nc_j(0){{\langle \varphi_j,\varphi_i\rangle}}=
   {{\langle u_0,\varphi_i\rangle}}.

Þetta segir okkur einfaldlega að :math:`\mathbf c(0)` sé lausn
jöfnuhneppisins

.. math:: B\mathbf c(0)=\mathbf c_0

þar sem hnit vigursins :math:`\mathbf c_0` eru gefin með

.. math:: c_{0i}={{\langle u_0,\varphi_i\rangle}}-\gamma_1{{\langle \varphi_0,\varphi_i\rangle}}.

Við erum hér komin með upphafsgildisverkefni fyrir afleiðujöfnuhneppi

.. math::

  \mathbf c'(t)=-B^{-1}A\mathbf c(t)+B^{-1}\mathbf b(t), \qquad
   \mathbf c(0)=B^{-1}\mathbf c_0,

og við vitum að lausn þess er gefin með formúlunni

.. math::

  \mathbf c(t)=e^{-tB^{-1}A}B^{-1}\mathbf c_0+
   \int_0^t e^{-(t-\tau)B^{-1}A}B^{-1}\mathbf b(\tau)\, d\tau,

Þar sem :math:`e^X` táknar veldisvísisfylkið, sem skilgreint er fyrir
:math:`N\times N` fylkið :math:`X` með veldaröðinni

.. math:: e^X=I+X+\frac 1{2!}X^2+\frac 1{3!}X^3+\cdots

Þessi lausnarformúla er nytsamleg til fræðilegra athugana, en hún er
erfið til útreikninga, þegar :math:`N` er stór tala. Við þurfum því að
nálga gildi :math:`\mathbf c(t)` með einhverjum hætti. Við lítum á
upprunalega afleiðujöfnuhneppið

.. math::

  B\mathbf c'(t)=-A\mathbf c(t)+\mathbf b(t), \qquad
   B\mathbf c(0)=\mathbf c_0,

veljum okkur eitthvert tímaskref :math:`\Delta t` og búum til
mismunasamband

.. math::

  B\bigg(\dfrac 1{\Delta t}\big(\mathbf c(t+\Delta t)-\mathbf c(t)\big)\bigg)
   =-A\big(\theta \mathbf c(t+\Delta t)+(1-\theta)\mathbf c(t)\big)
   +\theta \mathbf b(t+\Delta t)+(1-\theta)\mathbf b(t),

þar sem :math:`\theta` er einhver tala á bilinu :math:`[0,1]`. Ef
:math:`\theta=\frac 12`, þá kallast þessi aðferð trapisuaðferð. Við
byrjum nú á því að leysa jöfnuna :math:`B\mathbf c(0)=\mathbf c_0` fyrir
upphafsgildin :math:`\mathbf c(0)`. Við :math:`k`-ta tímaskref
:math:`t=k\Delta t`, þar sem :math:`k=0,1,2,3\dots` þurfum við að leysa
jöfnuna

.. math::

  \big(B+\theta \Delta t A\big)\mathbf c(t+\Delta t)=
   \big(B-(1-\theta)\Delta t A\big)\mathbf c(t)
   +\Delta t\big(\theta \mathbf b(t+\Delta t)+(1-\theta)\mathbf b(t)\big).

Þetta er gert með því að :math:`LU`-þátta fylkið
:math:`B+\theta \Delta t A` í upphafi reikninga á ákvarða síðan
:math:`\mathbf c(t+\Delta t)` með for- og endurinnsetningu.

Nú kemur spurningin um það hvernig eðlilegast sé að velja tímaskrefið
:math:`\Delta t`. Til þess að rannsaka þess spurningu skulum við líta á
eiginvigraliðun með tilliti til eiginvigra almenna
eigingildisverkefnisins

.. math:: A\mathbf v=\lambda B\mathbf v.

Fyrir samhverf fylki :math:`A` og :math:`B` með :math:`B` jákvætt
ákvarðað, eins og við höfum hér, er alltaf til eiginvigragrunnur
:math:`\mathbf v_1,\dots,\mathbf v_N` sem er þverstaðlaður í þeim
skilningi að :math:`\mathbf v_i^TB\mathbf v_j=\delta_{ij}`, þar sem
:math:`\delta_{ij}=1` ef :math:`i=j` og :math:`\delta_{ij}=0` ef
:math:`i\neq j`. Ef :math:`C` táknar nú fylkið með dálkvigrana
:math:`\mathbf v_1,\dots,\mathbf v_N`, þá segir þetta skilyrði okkur að

.. math:: C^TBC=I.

Ef :math:`\lambda_1,\dots,\lambda_N` eru eigingildin sem svara til
:math:`\mathbf v_1,\dots,\mathbf v_N`,
þ.e.a.s. \ :math:`A\mathbf v_j=\lambda_jB\mathbf v_j` og við látum
:math:`\Lambda` tákna hornalínufylkið með þessi eigingildi á
hornalínunni þá jafngilda þessar jöfnur fylkjajöfnunni

.. math:: AC=\Lambda BC.

Nú skulum við hugsa okkur að lausnin :math:`\mathbf c(t)` sé sett fram
með eiginvigraliðun

.. math:: \mathbf c(t)=\hat c_1(t)\mathbf v_1+\cdots+\hat c_N(t)\mathbf v_N.

Þessi liðun jafngildir :math:`\mathbf c(t)=C\hat c(t)`, þar sem
:math:`\hat c(t)=[\hat c_1(t),\dots,\hat c_N(t)]^T`. Mismunajafnan okkar
(:ref:`Link title <1.92>`) er þá jafngild

.. math::

  \big(BC+\theta \Delta t AC\big)\hat c(t+\Delta t)=
   \big(BC-(1-\theta)\Delta t AC\big)\hat c(t)
   +\Delta t\big(\theta \mathbf b(t+\Delta t)+(1-\theta)\mathbf b(t)\big).

Ef við margföldum þessa jöfnu með :math:`C^T` og notfærum okkur
(:ref:`Link title <1.95>`) og (:ref:`Link title <1.96>`), þá fáum við jöfnuna

.. math::

  \big(I+\theta \Delta t \Lambda\big)\hat c(t+\Delta t)=
   \big(I-(1-\theta)\Delta t \Lambda\big)\hat c(t)
   +\Delta tC^T\big(\theta \mathbf b(t+\Delta t)+(1-\theta)\mathbf b(t)\big).

Við skilgreinum nú :math:`\hat b(t)=C^T\mathbf b(t)` og
:math:`\hat c_0=C^T\mathbf c_0` og endum þá með jöfnuna

.. math::

  \big(I+\theta \Delta t \Lambda\big)\hat c(t+\Delta t)=
   \big(I-(1-\theta)\Delta t \Lambda\big)\hat c(t)
   +\Delta t \big(\theta \hat b(t+\Delta t)+(1-\theta)\hat b(t)\big).

Athugum nú að :math:`I+\theta \Delta t \Lambda` og
:math:`I-(1-\theta)\Delta t \Lambda` eru hornalínufylki, svo þessi jafna
er jafngild

.. math::

  \hat c_i(t+\Delta t)= \dfrac{1-(1-\theta)\Delta t \lambda_i}{1+\theta \Delta t \lambda_i}\hat c_i(t)
   +\dfrac{\Delta t}{1+\theta \Delta t \lambda_i}
   \big(\theta \hat b_i(t+\Delta t)+(1-\theta)\hat b_i(t)\big),

fyrir :math:`i=1,2,\dots,N`. Lítum nú aftur á upprunalega
upphafsgildisverkefnið (:ref:`Link title <1.91>`) og setjum inn
:math:`\mathbf c(t)=C\hat c(t)`. Það breytist þá í

.. math::

  BC\hat c'(t)=-A\mathbf c(t)+\mathbf b(t)
   =-\Lambda BC\hat c(t)+\mathbf b(t).

Nú margföldum við með :math:`C^T`, notum (:ref:`Link title <1.95>`) og fáum hneppið

.. math:: \hat c'(t)=-\Lambda \hat c(t)+\hat b(t),

sem jafngildir jöfnunum

.. math:: \hat c'_i(t)=-\lambda_i \hat c_i(t)+\hat b_i(t).

Lausnin uppfyllir formúluna

.. math::

  \hat c_i(t+\Delta t)=e^{-\Delta t\lambda_i}\hat c_i(t)+
   \int_0^{\Delta t}e^{-(\Delta t-\tau)\lambda_i}\hat b_i(t+\tau)\, d\tau.

Ef við gerum nú nálgunina
:math:`\theta \hat b_i(t+\Delta t)+(1-\theta)\hat b_i(t)` á fallinu
:math:`\tau\mapsto \hat b_i(t+\tau)`, þá fáum við lausnina

.. math::

  \hat c_i(t+\Delta t)\approx e^{-\Delta t\lambda_i}\hat c_i(t)+
   \dfrac 1{\lambda_i}\big(1-e^{-\Delta t\lambda_i}\big)
   \big(\theta \hat b_i(t+\Delta t)+(1-\theta)\hat b_i(t)\big)

Nú berum við þetta saman við (:ref:`Link title <1.101>`) og sjáum að aðferð okkar
felst í því að nálga í hverju tímaskrefi

.. math::

  e^{-\Delta t\lambda_i} \qquad \text { með }  \qquad
   \dfrac{1-(1-\theta)\Delta t \lambda_i}{1+\theta \Delta t \lambda_i}

og

.. math::

  \dfrac 1{\lambda_i}\big(1-e^{-\Delta t\lambda_i}\big) \qquad \text{ með } \qquad
   \dfrac 1{\lambda_i}\bigg(1-\dfrac{1-(1-\theta)\Delta t \lambda_i}{1+\theta \Delta t \lambda_i}\bigg)
   =\dfrac{\Delta t}{1+\theta \Delta t \lambda_i}.

Það kemur í ljós að liðirnir :math:`\hat c_i(t)` í formúlunni
(:ref:`Link title <1.97>`), sem svara til minstu eigingildanna hafa mest áhrif í
lausninni :math:`\mathbf c(t)` og því er eðlilegt að tímaskrefið
:math:`\Delta t` sé valið þannig að

.. math::

  e^{-\Delta t\lambda}\approx
   \dfrac{1-(1-\theta)\Delta t \lambda}{1+\theta \Delta t \lambda},

þar sem :math:`\lambda=\min_i \lambda_i`. Einnig þarf að gæta þess að
kvótinn í hægri hliðinni uppfylli

.. math:: \bigg|\dfrac{1-(1-\theta)\Delta t \lambda_i}{1+\theta \Delta t \lambda_i}\bigg|<1

fyrir öll eigingildin :math:`\lambda_i` til þess að koma í veg fyrir að
skekkjumögnun geti átt sér stað.
