LÍNULEGAR AFLEIÐUJÖFNUR
=======================

Línulegir afleiðuvirkjar
------------------------

Kennimargliðan
~~~~~~~~~~~~~~

Afleiðujafna af gerðinni

.. math:: a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=f(t),

þar sem föllin :math:`a_0,\dots,a_m,f` eru skilgreind á bili
:math:`I\subset {{\mathbb  R}}`, er sögð vera 
:hover:`línuleg,línuleg deildajafna`, því vinstri hliðin skilgreinir línulega vörpun

.. math::

  \begin{gathered}
   L:C^ m(I)\to C(I),\\
   Lu(t)=
   a_m(t)u^{(m)}(t)+a_{m-1}(t)u^{(m-1)}(t)+
   \cdots+a_1(t)u'(t)+a_0(t)u(t),\end{gathered}

ef :math:`a_0,\dots,a_m\in C(I)`. Línuleg vörpun af þessari gerð
kallast :hover:`afleiðuvirki, deildavirki`.
Við segjum að jafnan sé 
:hover:`óhliðruð,einsleitur` ef :math:`f` er
núllfallið. Annars segjum við að hún sé 
:hover:`hliðruð,misleitur`. Fyrir sérhvern punkt
:math:`t\in I` fáum við margliðu af einni breytistærð :math:`\lambda`,

.. math::

  P(t,\lambda)= a_m(t)\lambda^{m}+a_{m-1}(t)\lambda^{m-1}+\cdots+a_1(t)\lambda+a_0(t).

Þessa margliðu köllum við :hover:`kennimargliðu,kennimargliða` 
afleiðuvirkjans :math:`L`.

Afleiðuvirkinn :math:`D`
~~~~~~~~~~~~~~~~~~~~~~~~

Til þess að geta reiknað á auðveldan hátt með afleiðuvirkjum er venja að
skilgreina virkjann :math:`D` sem :math:`Du=u'` og síðan veldi
:math:`D^ k` af :math:`D` með

.. math::

  D^ 0u=u, \quad D^ 1u=u', \quad
   D^ 2u=DDu=u{{^{\prime\prime}}}, \quad \dots \quad D^ ku= D D^
   {k-1}u=u^{(k)}.

Afleiðuvirkinn :math:`L` er síðan skrifaður með formúlunni

.. math::

  P(t,D)=a_m(t)D^ m+\cdots+a_1(t)D+a_0(t).

   

Athugið að í síðasta liðnum höfum við sleppt því að skrifa
:math:`D^ 0`, en þetta á að lesa þannig að þegar virkinn :math:`L` er
látinn verka á fallið :math:`u`, er margfaldað með :math:`a_0(t)` í
síðasta liðnum.

Ef allir stuðlarnir :math:`a_j` eru fastaföll, þá segjum við að virkinn
hafi *fastastuðla* og við skrifum þá einungis
:math:`P(D)` í stað :math:`P(t,D)`. 

Þegar ekki er ljóst í formúlum með
tilliti til hvaða breytistærðar er verið að deilda, þá tilgreinum við
það með :math:`D_t`, :math:`D_x`, :math:`D_s`, …, í stað :math:`D` í
tákninu fyrir virkjann, þar sem lágvísirinn er táknið fyrir
breytistærðina. 

Línulega samantekt tveggja afleiðuvirkja :math:`P(t,D)`
og :math:`Q(t,D)` með tvinntölunum :math:`\alpha` og :math:`\beta`
táknum við með :math:`\alpha P(t,D)+\beta Q(t,D)`. Þetta er virkinn sem
skilgreindur er með formúlunni

.. math::

  \big(\alpha P(t,D) + \beta Q(t,D)\big)u=
   \alpha P(t,D)u + \beta Q(t,D)u.

Samsetningu virkjanna :math:`P(t,D)` og :math:`Q(t,D)` táknum við með
:math:`P(t,D)Q(t,D)` og er hún skilgreind með

.. math::

  \big(P(t,D)Q(t,D)\big)u=
   P(t,D)\big(Q(t,D)u\big).

Sýnt er með dæmum að almennt er
:math:`P(t,D)Q(t,D)\neq Q(t,D)P(t,D)`, með öðrum orðum, víxlreglan
gildir ekki við samsetningu afleiðuvirkja. Hins vegar gildir hún ef
virkjarnir hafa fastastuðla:

Setning
^^^^^^^

Ef :math:`P(D)` og :math:`Q(D)` eru :hover:`línulegir,línulegur` 
:hover:`afleiðuvirkjar,deildavirkjar` með fastastuðla þá er

.. math:: P(D)Q(D)=Q(D)P(D).

--------------

Nú skulum við líta á tilvist á lausnum á jaðargildisverkefnum. Í grein
6.5 skilgreindum við almennan jaðargildisvirkja með formúlunni

.. math::

  \begin{cases}
   B:C^{m-1}[a,b]\to {{\mathbb  C}}^m, \qquad Bu=(B_1u,\dots,B_mu),\\
   B_ju=\sum\limits_{l=1}^m {\alpha}_{jl}u^{(l-1)}(a)
   +{\beta}_{jl}u^{(l-1)}(b)=c_j,  &j=1,2,\dots,m.
  \end{cases}

Við höfum fullkomna lýsingu á því hvenær lausn fæst:

   

Setning
^^^^^^^

Látum :math:`I` vera opið bil sem inniheldur :math:`[a,b]`,
:math:`P(t,D)` vera línulegan afleiðuvirkja, :math:`a_m(t)\neq 0` fyrir
öll :math:`t\in I` og :math:`B` vera almennan jaðargildisvirkja. Þá eru
eftirfarandi skilyrði jafngild

\(i) Jaðargildisverkefnið :math:`P(t,D)u=f(t)`, :math:`Bu=c`, hefur
ótvírætt ákvarðaða lausn :math:`u\in C^m(I)` fyrir sérhvert
:math:`f\in C(I)` og sérhvert :math:`c\in {{\mathbb  C}}^m`.

\(ii) Jaðargildisverkefnið :math:`P(t,D)u=0`, :math:`Bu=0`, hefur
einungis núllfallið sem lausn.

\(iii) Ef :math:`u_1,\dots,u_m` er grunnur í :math:`{\cal N}(P(t,D))`, þá
er

.. math::

  \left|\begin{matrix} B_1u_1 & B_1u_2 & \cdots & B_1u_m\\
   B_2u_1 & B_2u_2 & \cdots & B_2u_m\\
   \vdots & \vdots &\ddots & \vdots \\
   B_mu_1 & B_mu_2 & \cdots & B_mu_m
   \end{matrix}\right|\neq 0.

--------------

Hugsum okkur nú að við þekkjum grunn :math:`u_1,\dots,u_m` fyrir núllrúm
virkjans :math:`P(t,D)` og eina sérlausn :math:`u_p` á
:math:`P(t,D)u=f`. Þá er lausnin :math:`u` á (i) af gerðinni
:math:`u=d_1u_1+\cdots+d_mu_m+u_p` þar sem stuðlarnir
:math:`d_1,\dots,d_m` eru lausnir jöfnuhneppisins

.. math::

  \left[\begin{matrix} B_1u_1 & B_1u_2 & \cdots & B_1u_m\\
   B_2u_1 & B_2u_2 & \cdots & B_2u_m\\
   \vdots & \vdots &\ddots & \vdots \\
   B_mu_1 & B_mu_2 & \cdots & B_mu_m
   \end{matrix}\right]
   \left[\begin{matrix} d_1\\ d_2\\ \vdots \\ d_m\end{matrix}\right]
   =\left[\begin{matrix} c_1-B_1u_p\\ c_2-B_2u_p\\ \vdots \\ c_m-B_mu_p
   \end{matrix}\right].


   

Línulegar jöfnur með fastastuðla
--------------------------------

Línulegar jöfnur með fastastuðla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við skulum nú líta á :hover:`línulega afleiðujöfnu,línuleg deildajafna`

.. math::

  P(D)u = (a_mD^m+\cdots+a_1D+a_0)u
   =f(t), \qquad t\in I,

   

þar sem við gerum ráð fyrir því að stuðlarnir :math:`a_j` í virkjanum
séu fastaföll, :math:`a_j\in {{\mathbb  C}}`, og :math:`a_m\neq 0`.
:hover:`Kennimargliðan,kennimargliða` er þá

.. math::

  P(\lambda)=a_m\lambda^m+\cdots+a_1\lambda+a_0.

   

Fyrsta viðfangsefni okkar er að finna grunn fyrir núllrúmið
:math:`{\cal N}(P(D))` og fá þannig framsetningu á 
:hover:`almennri lausn,almenn lausn` 
:hover:`óhliðruðu,misleitur` 
jöfnunnar :math:`P(D)u=0`. Við byrjum á
því að láta afleiðuvirkjana :math:`D^ k` verka á veldisvísisfallið
:math:`e^{\alpha t}`, þar sem :math:`\alpha` er einhver tvinntala. Þá
fæst

.. math::

  De^{\alpha t}=\alpha e^{\alpha t},\quad
   D^2e^{\alpha t}=\alpha^2 e^{\alpha t},\quad
   \dots , \quad 
   D^me^{\alpha t}=\alpha^m e^{\alpha t}.

Þetta gefur okkur síðan

   

.. math::

  \begin{aligned}
   P(D)e^{\alpha t}&=(a_mD^m+\cdots+a_1D+a_0)e^{\alpha t} \\
   &=(a_m{\alpha}^m+\cdots+a_1{\alpha}+a_0)e^{\alpha
   t}=P(\alpha)e^{\alpha t}.\nonumber\end{aligned}

Ef við veljum :math:`\alpha` sem eina af núllstöðvum kennimargliðunnar
:math:`P`, þá sjáum við að :math:`e^{\alpha t}` er lausn á óhliðruðu
jöfnunni. Undirstöðusetning algebrunnar gefur okkur, að við getum þáttað
margliðuna :math:`P` fullkomlega yfir tvinntölurnar og skrifað hana sem

.. math::

  P(\lambda)=a_m(\lambda-\lambda_1)^{m_1}\cdots
   (\lambda-\lambda_\ell)^{m_\ell},

   

þar sem :math:`\lambda_1,\dots,\lambda_\ell\in {{\mathbb  C}}` eru
:hover:`núllstöðvarnar,núllstöð` og
:math:`m_1,\dots,m_\ell` er 
:hover:`margfeldni` þeirra, :math:`m_1+\cdots+m_\ell=m`. Með
því að nota þessa framsetningu á kennimargliðunni getum við skrifað
afleiðuvirkjann sem

.. math::

  P(D)=a_m(D-\lambda_1)^{m_1}\cdots(D-\lambda_\ell)^{m_\ell}.

   

Við fáum nú fullkomna lýsingu á :hover:`núllrúm,kjarni` afleiðuvirkja
með fastastuðla:

Setning
^^^^^^^

Gerum ráð fyrir að :math:`P(D)` sé línulegur afleiðuvirki af stigi
:math:`m` með fastastuðla og að kennimargliðan :math:`P(\lambda)` hafi
:math:`\ell` ólíkar núllstöðvar
:math:`\lambda_1,\dots,\lambda_\ell\in {{\mathbb  C}}` með margfeldnina
:math:`m_1,\dots,m_\ell`. Þá mynda föllin

.. math::

  \begin{gathered}
   e^{\lambda_1t}, te^{\lambda_1t},\dots, t^{m_1-1}e^{\lambda_1t},\\
   e^{\lambda_2t}, te^{\lambda_2t},\dots, t^{m_2-1}e^{\lambda_2t},\\
   \quad \vdots\qquad \vdots \qquad \qquad \vdots\\
   e^{\lambda_\ell t}, te^{\lambda_\ell t},\dots, t^{m_\ell-1}e^{\lambda_\ell t},\end{gathered}

grunn í núllrúmi virkjans :math:`P(D)` og þar með má skrifa sérhvert
stak í núllrúminu sem

.. math:: q_1(t)e^{\lambda_1t}+\cdots+q_\ell(t)e^{\lambda_\ell t},

þar sem :math:`q_j` eru margliður af stigi :math:`<m_j`,
:math:`1\leq j\leq \ell`.

Euler-jöfnur
------------

Euler-jöfnur
~~~~~~~~~~~~

Afleiðujafna af gerðinni

.. math::

  P(x,D_x)u=
   a_mx^mu^{(m)}+\cdots+a_1xu{{^{\prime}}}+a_0u=0,

   

þar sem stuðlarnir :math:`a_j` eru tvinntölur, :math:`a_m\neq 0` og
:math:`u` er óþekkt fall af :math:`x`, nefnist *Euler-jafna*. 

Til þess að fá almenna lýsingu á lausnum jöfnunnar á
:math:`{{\mathbb  R}}\setminus{{\{0\}}}` dugir okkur að finna almenna
lausn á jákvæða raunásnum, því auðvelt er að sannfæra sig um að
:math:`v(x)=u(|x|)` er lausn á :math:`{{\mathbb  R}}\setminus{{\{0\}}}`
þá og því aðeins að :math:`u` sé lausn á
:math:`\{x\in {{\mathbb  R}}; x>0\}`. 

Athugið að veldið á :math:`x` í
hverjum lið er það sama og stigið á afleiðunni. Ef við stingum
:math:`u(x)=x^r` inn í afleiðuvirkjann, þá fæst

.. math::

  \begin{aligned}
   P(x,D_x)u
   &=a_mx^m r(r-1)\cdots(r-m+1)x^{r-m}
   +\cdots+a_1xrx^{r-1}+a_0x^r\\
   &=\big(a_m r(r-1)\cdots(r-m+1)+
   \cdots+a_1r+a_0\big)x^r.\end{aligned}

Þar með er :math:`u` lausn þá og því aðeins að :math:`r` sé núllstöð
:math:`m`-ta stigs margliðunnar :math:`Q`, sem skilgreind er með
formúlunni

.. math::

  Q(r)=a_m r(r-1)\cdots(r-m+1)+\cdots+a_1r+a_0.

Lítum fyrst á tilfellið að þessi jafna hafi ólíkar núllstöðvar
:math:`r_1,\dots, r_m`. Þá er auðvelt að sannfæra sig um að föllin
:math:`x^{r_1},\dots,x^{r_m}` eru línulega óháð og þar með er almenn
lausn á Euler jöfnu af gerðinni

.. math::

  u(x)=c_1x^{r_1}+\cdots+c_mx^{r_m}.

   

Nú skulum við athuga tilfellið þegar :math:`Q(r)` hefur margfaldar
núllstöðvar. Þá skilgreinum við fallið :math:`v(t)=u(e^t)` og sýnum fram
á að :math:`v` uppfylli :math:`Q(D)v=0`. Við þurfum þá að þekkja
sambandið milli afleiða fallanna :math:`u` og :math:`v`. Við höfum

.. math::

  \begin{aligned}
   u(x)&=v(\ln x),\\
   u{{^{\prime}}}(x)&=v{{^{\prime}}}(\ln x)\cdot \dfrac 1x,\\
   u{{^{\prime\prime}}}(x)&=v{{^{\prime\prime}}}(\ln x)\cdot \dfrac 1{x^2}
   -v{{^{\prime}}}(\ln x)\cdot \dfrac 1{x^2} = D(D-1)v(\ln x)\cdot \dfrac 1{x^2}.\end{aligned}

Með þrepun fæst síðan að

.. math::

  u^{(k)}(x)=D(D-1)\cdots(D-k+1)v(\ln x)\cdot \dfrac 1{x^k}.


   

Þetta gefur

.. math::

  \begin{aligned}
   P(x,D)u(x)&=\sum\limits_{k=0}^m a_kx^ku^{(k)}(x)\\
   &=\sum\limits_{k=0}^m a_kD(D-1)\cdots(D-k+1)v(\ln x)\\
   &=Q(D)v(\ln x).\end{aligned}

Þar með er :math:`u` lausn á Euler-jöfnunni þá og því aðeins að
:math:`v` sé lausn á jöfnunni :math:`Q(D)v=0`. Nú hefur virkinn
:math:`Q` fastastuðla svo við getum beitt setningu 7.2.1:

Setning
^^^^^^^

Almenn lausn Euler-jöfnunnar á jákvæða raunásnum er línuleg samatekt
fallanna

.. math::

  \begin{gathered}
   x^{r_1}, \big(\ln x \big) x^{r_1}, \dots,
   \big(\ln x\big)^{m_1-1}x^{r_1},\\
   x^{r_2}, \big(\ln x\big)x^{r_2}, \dots,
   \big(\ln x \big)^{m_2-1} x^{r_2},\\
   \vdots \qquad \qquad \qquad \vdots \qquad \qquad \qquad \vdots\\ 
   x^{r_\ell}, \big(\ln x \big)x^{r_\ell}, \dots,
   \big(\ln x\big)^{m_\ell-1} x^{r_\ell},\end{gathered}

þar sem :math:`r_1,\dots,r_\ell` eru ólíkar núllstöðvar margliðunnar
:math:`Q`, sem gefin er með 

.. math::

  Q(r)=a_m r(r-1)\cdots(r-m+1)+\cdots+a_1r+a_0

og margfeldni þeirra er
:math:`m_1,\dots,m_\ell`.

Sérlausnir
----------

Algengt er að ástandsjöfnur eðlisfræðilegra kerfa séu af gerðinni

.. math:: P(D)u=f

þar sem :math:`P(D)` er línulegur afleiðuvirki með fastastuðla og
:math:`f` er gefið fall á einhverju bili. Fallið :math:`f` stendur oft
fyrir ytra álag, örvun eða krafta, sem á kerfið verka, en lausnin er
svörun kerfisins við þessu ytra álagi. 

Til þess að skilja kerfið er
nauðsynlegt að ráða yfir fjölbreytilegum aðferðum til þess að reikna út
svörunina :math:`u` þegar ytra álagið :math:`f` er gefið. 

Í þessari grein ætlum við að líta á tilfellið að :math:`f` sé 
veldisvísisfall eða hornafall og athuga hvort hægt sé að finna sérlausn af sömu gerð. Í næstu grein munum við hins vegar fjalla um almenna aðferð til þess að finna sérlausn fyrir hvaða hægri hlið sem er. 

Við höfum séð að :math:`P(D)e^{\alpha t}=P(\alpha)e^{\alpha t}`. 
Ef :math:`\alpha` er núllstöð kennimargliðunnar :math:`P`, 
þá er veldisvísisfallið :math:`e^{\alpha t}` lausn á óhliðruðu jöfnunni. 
Ef aftur á móti :math:`P(\alpha) \neq 0`, þá er

.. math::

  P(D)u_p=e^{\alpha t} \qquad\text{ ef } \qquad 
   u_p(t)=\dfrac{e^{\alpha t}}{P(\alpha)}.

   

Ef :math:`\alpha\in {{\mathbb  R}}`, :math:`P(i\alpha)\neq 0` og
:math:`P(-i\alpha)\neq 0`, þá fáum við með því að nota jöfnur Eulers að

.. math::

  P(D)u_p=\cos \alpha t \qquad\text{ ef } \qquad 
   u_p(t)=

   

  \dfrac{e^{i\alpha t}}{2P(i\alpha)}+
   \dfrac{e^{-i\alpha t}}{2P(-i\alpha)},

og

.. math::

  P(D)u_p=\sin \alpha t \qquad\text{ ef } \qquad 
   u_p(t)=\dfrac{e^{i\alpha t}}{2iP(i\alpha)}
   -\dfrac{e^{-i\alpha t}}{2iP(-i\alpha)}.

   

Í því tilfelli að kennimargliðan hefur eingöngu rauntalnastuðla, þá
verða lausnirnar í þessum tveimur dæmum

.. math::

  u_p(t)={{\operatorname{Re\, }}}\bigg(\dfrac{e^{i{\alpha}t}}{P(i{\alpha})}\bigg), \qquad
   \text{ og } \qquad
   u_p(t)={{\operatorname{Im\, }}}\bigg(\dfrac{e^{i{\alpha}t}}{P(i{\alpha})}\bigg).

   

Ef :math:`\alpha\in {{\mathbb  R}}`, :math:`P(\alpha)\neq 0` og
:math:`P(-\alpha)\neq 0`, þá fáum við að

.. math::

  P(D)u_p=\cosh \alpha t \qquad\text{ ef }\qquad
   u_p(t)=\dfrac{e^{\alpha t}}{2P(\alpha)}+\dfrac{e^{-\alpha
   t}}{2P(-\alpha)},

   

og

.. math::

  P(D)u_p=\sinh \alpha t \qquad\text{ ef }\qquad
   u_p(t)=\dfrac{e^{\alpha t}}{2P(\alpha)}-\dfrac{e^{-\alpha
   t}}{2P(-\alpha)}.

   

Sérlausnir fundnar með virkjareikningi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við láta afleiðuvirkjann :math:`D-{\alpha}` verka á margfeldi
fallanna :math:`v` og :math:`e^{{\alpha} t}`. Við fáum þá

.. math::

  (D-\alpha)(ve^{\alpha t})
   =D(ve^{\alpha t})-\alpha ve^{\alpha t} = v{{^{\prime}}}e^{\alpha t}.


   

Af þessari formúlu fæst síðan með þrepun

.. math::

  (D-\alpha)^ m(ve^{\alpha t})= v^{(m)} e^{\alpha
   t}\qquad m\geq 1.

   

Ef við veljum nú :math:`v(t)=t^ k`, þá fáum við

.. math::

   
   (D-\alpha)^ m(t^ ke^{\alpha t})= 
   \begin{cases}
   0, &k<m,\\
   k!e^{\alpha t},& k=m,\\
   k(k-1)\cdots(k-m+1)t^{k-m}e^{\alpha t},& k>m.
   \end{cases}

Hugsum okkur nú að :math:`\alpha` sé núllstöð :math:`P` af stigi
:math:`k`. Þá er unnt að þátta margliðuna :math:`P` í
:math:`P(\lambda)=(\lambda-\alpha)^kQ(\lambda)`, þar sem
:math:`Q(\lambda)` er margliða af stigi :math:`m-k` og
:math:`Q(\alpha)\neq 0`. Samkvæmt jöfnunni hér að framan er

.. math::

  P(D)(t^ke^{\alpha t}) = Q(D)(D-\alpha)^k(t^ke^{\alpha t})=
   Q(D)(k!e^{\alpha t})=k!Q(\alpha)e^{\alpha t}.

Þetta gefur okkur að

.. math::

  P(D)u_p=e^{\alpha t} \qquad \text{ ef } \qquad
   u_p(t) = \dfrac{t^ke^{\alpha t}}{k!Q(\alpha)}.


   

Nú skulum við gera ráð fyrir því að :math:`i\alpha` sé núllstöð
:math:`P` af stigi :math:`k` og að :math:`-i\alpha` sé núllstöð
:math:`P` af stigi :math:`l`. Þá getum við þáttað :math:`P` á tvo
mismunandi vegu í

.. math::

  P(\lambda)= (\lambda-i\alpha)^kQ(\lambda), \qquad
   P(\lambda)= (\lambda+i\alpha)^lR(\lambda),

þar sem :math:`Q` og :math:`R` eru margliður af stigi :math:`m-k` og
:math:`m-l`, :math:`Q(i\alpha)\neq 0` og :math:`R(-i\alpha)\neq 0`.
Þetta gefur að

.. math::

  P(D)u_p=\cos \alpha t \qquad\text{ ef } \qquad
   u_p(t)=\dfrac{t^ke^{i\alpha t}}{2(k!)Q(i\alpha)}+
   \dfrac{t^le^{-i\alpha t}}{2(l!)R(-i\alpha)},


   

og

.. math::

  P(D)u_p=\sin \alpha t \qquad \text{ ef } \qquad
   u_p(t)=\dfrac{t^ke^{i\alpha t}}{2i(k!)Q(i\alpha)}-
   \dfrac{t^le^{-i\alpha t}}{2i(l!)R(-i\alpha)}.


   

Green-föll
----------

Green-föll
~~~~~~~~~~

Í síðustu grein skoðuðum við nokkrar einfaldar aðferðir til að finna
sérlausnir á línulegum jöfnum með fastastuðla, þar sem hægri hlið
jöfnunnar :math:`f(t)` er veldisvísisfall eða eitthvert skylt fall. Núna
ætlum við að kynna okkur almenna aðferð til þess að finna sérlausn á

.. math::

  P(t,D)u=(a_m(t)D^m+\cdots+a_1(t)D+a_0(t))u=f(t), \qquad
   t\in I,


   

þar sem :math:`I` er eitthvert bil á rauntalnaásnum, föllin :math:`a_0, \dots,a_m,f` eru í :math:`C(I)` og :math:`a_m(t)\neq 0` fyrir öll
:math:`t\in I`.

Ef :math:`\tau\in I` er einhver ótiltekinn punktur, þá segir
fylgisetning 6.7.7 að til sé ótvírætt ákvörðuð lausn í :math:`C^m(I)` á
upphafsgildisverkefninu

.. math::

  P(t,D_t)u=0, \qquad
   u(\tau)=u{{^{\prime}}}(\tau)=\cdots=u^{(m-2)}(\tau)=0, \quad 
   u^{(m-1)}(\tau)=1/a_m({\tau}).

Við táknum hana með :math:`G(t,\tau)`. Þar með ákvarðast fallið
:math:`G` af skilyrðunum

.. math::

  \begin{gathered}
   P(t,D_t)G(t,\tau)=0,  \qquad t,\tau\in I,\\
   G(\tau,\tau)=\partial_tG(\tau,\tau)=\cdots=
   \partial_t^{(m-2)}G(\tau,\tau)=0, \quad
   \partial_t^{(m-1)}G(\tau,\tau)=1/a_m({\tau}). 
  \end{gathered}

Nú tökum við :math:`a\in I` og sýnum fram á að fallið

.. math::

  u_p(t) = \int_a^ t G(t,\tau)f(\tau) \, d\tau, \qquad t\in I,

   

uppfylli jöfnuna :math:`P(t,D)u=f(t)`, :math:`t\in I`. Til þess að ráða
við þetta þurfum við að vita að fallið :math:`G(t,\tau)` sé heildanlegt
með tilliti til :math:`\tau` og jafnframt hvernig á að deilda fall sem
gefið er með svona formúlu:

   

Hjálparsetning
^^^^^^^^^^^^^^

Ef :math:`I` er bil á raunásnum, :math:`a\in I`, :math:`f\in C(I)` og
:math:`g\in C(I\times I)`, er samfellt deildanlegt fall af fyrri breytistærðinni,
þ.e. \ :math:`{\partial}_tg\in C(I\times I)`, þá er fallið :math:`h`,
sem gefið er með formúlunni

.. math:: h(t)=\int_a^ t g(t, \tau)f(\tau) \, d\tau, \qquad t\in I,

í :math:`C^ 1(I)` og afleiða þess er

.. math::

  h{{^{\prime}}}(t)=g(t,t)f(t)+\int_a^ t \partial_tg(t,\tau)f(\tau) \, d\tau,
   \qquad t\in I.

--------------

Nú skulum við ganga út frá því að
:math:`\partial_t^{j}G\in C(I\times I)` fyrir :math:`j=0,\dots,m` og
líta aftur á fallið :math:`u_p` sem skilgreint var með 

.. math::

  u_p(t) = \int_a^ t G(t,\tau)f(\tau) \, d\tau, \qquad t\in I.

Með því að beita hjálparsetningunni, fáum við að
:math:`u_p\in C^ 1(I)` og

.. math:: u_p{{^{\prime}}}(t) = G(t,t)f(t)+\int_a^ t \partial_t G(t,\tau)f(\tau) \, d\tau.

Nú er :math:`G(t,t)=0` fyrir öll :math:`t\in I` samkvæmt fyrsta
upphafsskilyrðinu á :math:`G`, svo við fáum að :math:`u_p\in C^ 2(I)`
og

.. math::

  u_p{{^{\prime\prime}}}(t) = \partial_tG(t,t)f(t)
   +\int_a^ t \partial_t^2G(t,\tau)f(\tau) \, d\tau.

Ef :math:`m > 2` þá er :math:`\partial_tG(t,t)=0` fyrir öll
:math:`t\in I` og við getum haldið áfram að deilda fallið :math:`u_p`,
þar til við fáum að :math:`u_p\in C^ m(I)` og

.. math::

  u_p^{(m)}(t) = \partial_t^{m-1}G(t,t)f(t)+\int_a^ t
   \partial_t^mG(t,\tau)f(\tau) \, d\tau.

Nú er :math:`\partial_t^{m-1}G(t,t)=1/a_m(t)` fyrir öll
:math:`t\in I`. Við tökum saman liði og fáum

.. math::

  \begin{aligned}
   P(t,D_t)u_p(t)&=
   a_m(t)f(t)/a_m(t) +\sum\limits_{j=0}^ m
   a_j(t)\int_a^ t \partial_t^jG(t,\tau)f(\tau)\, d\tau=\\
   &=f(t)+\int_a^ t P(t,D_t)G(t,\tau)f(\tau)\, d\tau=f(t),\end{aligned}

því :math:`P(t,D_t)G(t,\tau)=0` fyrir öll :math:`\tau\in I`. Á jöfnunum
fyrir afleiður :math:`u_p` sjáum við að

.. math:: u_p(a)=u_p{{^{\prime}}}(a)=\cdots=u_p^{(m-1)}(a)=0.

Við getum því tekið saman útreikninga okkar:

Setning
^^^^^^^

Látum :math:`I` vera bil á rauntöluásnum, :math:`a\in I` og
:math:`P(t,D)` vera línulegan afleiðuvirkja

.. math::

  P(t,D)u=(a_m(t)D^m+\cdots+a_1(t)D+a_0(t))u

með samfellda stuðla og :math:`a_m(t)\neq 0` fyrir öll :math:`t\in I`. Fyrir
sérhvert :math:`f\in C(I)` er til ótvírætt ákvörðuð lausn :math:`u_p\in C^ m(I)` á upphafsgildisverkefninu

.. math::

  P(t,D)u=f(t), \qquad u(a)=u{{^{\prime}}}(a)=\cdots=u^{(m-1)}(a)=0,

   

og er hún gefin með formúlunni

   

.. math:: u_p(t) = \int_a^ t G(t,\tau)f(\tau) \, d\tau, \qquad t\in I,

þar sem :math:`G`, er lausnin á upphafsgildisverkefninu

.. math::

  \begin{gathered}
   P(t,D_t)G(t,\tau)=0,  \qquad t,\tau\in I,\\
   G(\tau,\tau)=\partial_tG(\tau,\tau)=\cdots=
   \partial_t^{(m-2)}G(\tau,\tau)=0, \quad
   \partial_t^{(m-1)}G(\tau,\tau)=1/a_m({\tau}). 
  \end{gathered}

Fallið :math:`G(t,\tau)` er :math:`m`-sinnum samfellt deildanlegt fall
af :math:`t` fyrir sérhvert :math:`\tau\in I` og
:math:`\partial_t^jG\in C(I\times I)` fyrir :math:`j=0,\dots,m`.

Skilgreining
^^^^^^^^^^^^

Fallið :math:`G(t,\tau)` í síðustu setningu kallast *Green-fall* 
virkjans :math:`P(t,D)`. Við tölum einnig um *fall Greens*.

--------------

Mjög auðvelt er að ákvarða Green-fallið fyrir línulegan afleiðuvirkja
með fastastuðla:

Fylgisetning
^^^^^^^^^^^^

Gerum ráð fyrir að :math:`P(D)=a_mD^ m+\cdots+a_1D+a_0` sé línulegur
afleiðuvirki með fastastuðla. Látum
:math:`g\in C^{\infty}({{\mathbb  R}})` vera fallið sem uppfyllir

.. math::

  P(D)g=0, \quad g(0)=g{{^{\prime}}}(0)=\cdots=g^{(m-2)}(0)=0, \quad
   g^{(m-1)}(0)=1/a_m.

   

Þá er :math:`G(t,\tau)=g(t-\tau)` Green-fall virkjans :math:`P(D)`.

Wronski-fylkið og Wronski-ákveðan
---------------------------------

Wronski-fylkið og Wronski-ákveðan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við láta :math:`G(t,\tau)` tákna Green-fallið sem lýst er í
setningu 7.5.2 og jafnframt gera ráð fyrir því að :math:`u_1,\dots, u_m`
sé grunnur í :math:`{\cal N}(P(t,D))`. Fyrst :math:`G(t,\tau)` er lausn
á óhliðruðu jöfnunni :math:`P(t,D_t)G(t,\tau)=0` fyrir sérhvert
:math:`\tau\in I`, þá getum við skrifað :math:`G(t,\tau)` sem línulega
samantekt af grunnföllunum með stuðlum sem eru háðir :math:`\tau`,

.. math:: G(t,\tau)=c_1(\tau)u_1(t)+\cdots+c_m(\tau)u_m(t), \qquad t,\tau\in I.

Stuðlaföllin :math:`c_1,\dots,c_m` ákvarðast síðan af
upphafsskilyrðunum,

.. math::

  \begin{aligned}
   G(\tau,\tau) &= c_1(\tau)u_1(\tau)+\cdots+c_m(\tau)u_m(\tau)=0,\\
   \partial_tG(\tau,\tau) &= c_1(\tau)u_1{{^{\prime}}}(\tau)+
   \cdots+c_m(\tau)u_m{{^{\prime}}}(\tau)=0,\\
   &\qquad\vdots\qquad\qquad\vdots\qquad\qquad\vdots\\
   \partial_t^{m-2}G(\tau,\tau) &= c_1(\tau)u_1^{(m-2)}(\tau)+
   \cdots+c_m(\tau)u_m^{(m-2)}(\tau)=0,\\
   \partial_t^{m-1}G(\tau,\tau) &= c_1(\tau)u_1^{(m-1)}(\tau)+
   \cdots+c_m(\tau)u_m^{(m-1)}(\tau)=1/a_m({\tau}).\end{aligned}

Á fylkjaformi verður þetta jöfnuhneppi

.. math::

  V(\tau)c(\tau)=a_m({\tau})^{-1}e_m,

   

þar sem :math:`V\in C(I,{{\mathbb  C}}^{m\times m})` er fylkjafallið

.. math::

  V(\tau)=V(u_1,\dots,u_m)(\tau)=
   \left[\begin{matrix}
   u_1(\tau)&\dots&u_m(\tau)\\
   u_1{{^{\prime}}}(\tau)&\dots&u_m{{^{\prime}}}(\tau)\\
   \vdots&\ddots&\vdots\\
   u_1^{(m-1)}(\tau)&\dots&u_m^{(m-1)}(\tau)
   \end{matrix}\right]


   

en :math:`c(\tau)=[c_1(\tau),\dots,c_m(\tau)]^t` og
:math:`e_m=[0,\dots,0,1]^t`.

Skilgreining
^^^^^^^^^^^^

Látum :math:`I` vera bil á :math:`{{\mathbb  R}}` og
:math:`u_1,\dots,u_m` vera :math:`m-1` sinnum deildanleg föll á
:math:`I`. Þá nefnist fylkjagilda fallið :math:`V=V(u_1,\dots,u_m)` *Wronski-fylki* fallanna
:math:`u_1,\dots, u_m`. Ákveða þess kallast *Wronski-ákveða* fallanna
:math:`u_1,\dots, u_m` og hana táknum við með
:math:`W=W(u_1,\dots,u_m)`.

--------------

Ef við þekkjum Wronski-ákveðuna af :math:`m` lausnum á afleiðujöfnu í
einum punkti, þá getum við reiknað hana út með því að leysa fyrsta stigs
afleiðujöfnu:

   

Setning
^^^^^^^

Látum :math:`P(t,D)=a_m(t)D^ m+\cdots+a_1(t)D+a_0(t)` vera
afleiðuvirkja með samfellda stuðla, :math:`u_1,\dots,u_m` vera lausnir á
óhliðruðu jöfnunni :math:`P(t,D)u=0` og táknum Wronski-ákveðu þeirra með
:math:`W(t)`. Þá uppfyllir :math:`W` fyrsta stigs afleiðujöfnuna

   

.. math:: a_m(t) W{{^{\prime}}}+a_{m-1}(t)W=0

og þar með gildir formúlan

.. math::

  W(t)=W(a)\exp\bigg(-\int_a^ t\dfrac{a_{m-1}(\tau)}{a_m(\tau)}\,
   d\tau\bigg) 

   

fyrir öll :math:`a` og :math:`t` á bili :math:`J` þar sem :math:`a_m`
er núllstöðvalaust.

--------------

Formúluna fyrir Wronski-ákveðuna má nota á ýmsa vegu:

Setning
^^^^^^^

Látum :math:`u_1,\dots,u_m` vera lausnir á óhliðruðu jöfnunni
:math:`P(t,D)u=0` og gerum ráð fyrir að :math:`a_m` sé núllstöðvalaust á
opnu bili :math:`J\subset I`. Þá eru eftirfarandi skilyrði jafngild:

\(i) Föllin :math:`u_1,\dots,u_m` eru línulega óháð á bilinu :math:`J`.

\(ii) :math:`W(u_1,\dots,u_m)(t)\neq 0` fyrir sérhvert :math:`t\in J`.

\(iii) :math:`W(u_1,\dots,u_m)(a)\neq 0` fyrir eitthvert :math:`a\in J`.

\(iv) Dálkvigrarnir í Wronski-fylkinu :math:`V(u_1,\dots,u_m)(t)` eru
línulega óháðir fyrir sérhvert :math:`t\in J`.

\(v) Dálkvigrarnir í Wronski-fylkinu :math:`V(u_1,\dots,u_m)(a)` eru
línulega óháðir fyrir eitthvert :math:`a\in J`.

--------------

Nú skulum við rifja það upp að :math:`n\times n` fylki :math:`A` hefur
andhverfu þá og því aðeins að :math:`\det A\neq 0`. Andhverfuna er hægt
að reikna út á ýmsa vegu, en til er formúla fyrir henni,

.. math::

  A^{[-1]}=\dfrac 1{\det A}B^ t,

   

þar sem :math:`B=(b_{jk})_{j,k=1}^ n` táknar fylgiþáttafylki
:math:`A`, sem er :math:`n\times n` fylkið með stökin

.. math::

  b_{jk}=(-1)^{j+k}\det A_{jk},

   

þar sem :math:`A_{jk}` er :math:`(n-1)\times (n-1)` fylkið, sem fæst
með því að fella niður línu númer :math:`j` og dálk númer :math:`k` í
fylkinu :math:`A`, og :math:`B^ t` er fylkið :math:`B` bylt, þar sem víxlað er á línum og dálkum í
:math:`B`. Við höfum nú bætt miklu við þekkingu okkar á Green-föllum:

   

Setning
^^^^^^^

Látum :math:`I` vera bil á :math:`{{\mathbb  R}}` og
:math:`P(t,D)=a_m(t)D^ m+\cdots+a_1(t)D+a_0(t)` vera afleiðuvirkja með
samfellda stuðla á :math:`I` og :math:`u_1,\dots,u_m` vera grunn í
:math:`{\cal N}(P(t,D))`. Green-fallið er gefið með formúlunni

.. math::

  G(t,\tau)=c_1(\tau)u_1(t)+\cdots+c_m(\tau)u_m(t), \qquad t,\tau\in I,


   

þar sem vigurinn :math:`a_m({\tau})(c_1(\tau),\dots,c_m(\tau))` myndar
aftasta dálkinn í andhverfu Wronski-fylkisins
:math:`V(u_1,\dots,u_m)(\tau)`,

.. math::

  c_j(\tau)=(-1)^{m+j} \dfrac{\det V_{mj}(u_1,\dots,u_m)(\tau)}
   {a_m({\tau})W(u_1,\dots, u_m)(\tau)},


   

þar sem :math:`V_{mj}(u_1,\dots,u_m)(\tau)` táknar
:math:`(m-1)\times (m-1)` fylkið sem fæst með því að fella niður neðstu
línuna og dálk númer :math:`j` í :math:`V(u_1,\dots,u_m)(\tau)`. Ef
:math:`f\in C(I)`, þá hefur upphafsgildisverkefnið lausnina
:math:`u_p\in C^ m(I)` sem gefin er með

.. math::

  u_p(t)=v_1(t)u_1(t)+\cdots+v_m(t)u_m(t), \qquad t\in I,

   

þar sem stuðlaföllin :math:`v_j` eru gefin með formúlunni

.. math::

  v_j(t)=\int_a^ t c_j(\tau)f(\tau) \, d\tau.

   

--------------

Við fáum nú beina formúlu fyrir Green-falli annars stigs virkja:

Fylgisetning
^^^^^^^^^^^^

Látum :math:`P(t,D)=a_2(t)D^2+a_1(t)D+a_0(t)` vera annars stigs
afleiðuvirkja á bilinu :math:`I` með samfellda stuðla og
:math:`a_2(t)\neq 0` fyrir öll :math:`t\in I`. Gerum nú ráð fyrir að
:math:`u_1` og :math:`u_2` séu línulega óháðar lausnir á óhliðruðu
jöfnunni :math:`P(t,D)u=0`. Þá er

.. math::

  G(t,\tau) 
   =a_2(\tau)^{-1}
   \left|\begin{matrix}
   u_1(\tau) & u_1(t)\\
   u_2(\tau) & u_2(t)
   \end{matrix}\right|\bigg /
   \left|\begin{matrix}
   u_1(\tau) & u_2({\tau})\\
   u_1{{^{\prime}}}(\tau) & u_2{{^{\prime}}}({\tau})
   \end{matrix}\right|.


   


