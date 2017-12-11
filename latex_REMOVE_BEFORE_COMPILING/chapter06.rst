UNDIRSTÖÐUATRIÐI UM AFLEIÐUJÖFNUR
=================================

Skilgreiningar á nokkrum hugtökum
---------------------------------

Venjulegar afleiðujöfnur
~~~~~~~~~~~~~~~~~~~~~~~~

*Afleiðujafna*:hover:`afleiðujafna` er jafna sem lýsir sambandi milli
fallgilda óþekkts falls og gilda á einstökum afleiðum þess. Ef óþekkta
fallið er háð einni breytistærð, þá kallast jafnan *venjuleg
afleiðujafna, :hover:`afleiðujafna!venjuleg`:hover:‘venjuleg
afleiðujafna‘* en ef það er háð fleiri en einni breytistærð, þá kallast
hún *hlutafleiðujafna*:hover:`hlutafleiðujafna`. Venjulega afleiðujöfnu
er alltaf hægt að umrita yfir í jafngilda jöfnu af gerðinni

.. math::

  F(t,u,u',u{{^{\prime\prime}}},\dots,u^{(m)})=0 
þar sem við hugsum okkur að :math:`t` sé breytistærð, sem tekur gildi í
einhverju hlutmengi :math:`A` af :math:`{{\mathbb  R}}` og að :math:`u`
sé óþekkt fall sem skilgreint er á :math:`A` og tekur gildi í
:math:`{{\mathbb  R}}`, :math:`{{\mathbb  C}}` eða jafnvel
:math:`{{\mathbb  R}}^m`. Úrlausn jöfnunnar felst í því að finna opið
bil :math:`I\subset A` og öll föll :math:`u` þannig að vigurinn

.. math::

  (t,u(t),u{{^{\prime}}}(t),\dots,u^{(m)}(t))
sé í skilgreiningarmengi fallsins :math:`F` og uppfylli jöfnuna

.. math::

  F(t,u(t),u'(t),u{{^{\prime\prime}}}(t),\dots,u^{(m)}(t))=0,
    \qquad t\in I.
Við segjum þá að fallið :math:`u` sé lausn á jöfnunni (:ref:`Link title <1.1.1>`).
*Stig:hover:`stig`*:hover:`afleiðujafna!stig`
afleiðujöfnu:hover:`stig!afleiðujöfnu` er hæsta stig á afleiðu, sem
kemur fyrir í jöfnunni. Við segjum að :math:`m`-ta stigs afleiðujafnan
(:ref:`Link title <1.1.1>`) sé á
*staðalformi:hover:`staðalform`*:hover:`afleiðujafna!staðalform` þegar
hún hefur verið umrituð yfir í jafngilda jöfnu af taginu

.. math::

  u^{(m)}=G(t,u,u',\dots,u^{(m-1)}).
Línulegar afleiðujöfnur
~~~~~~~~~~~~~~~~~~~~~~~

Afleiðujafna af gerðinni

.. math::

  a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=f(t),

þar sem föllin :math:`a_0,\dots,a_m,f` eru skilgreind á bili
:math:`I\subset {{\mathbb  R}}`, er sögð vera
*línuleg*:hover:`afleiðujafna!línuleg`. Ástæðan fyrir nafngiftinni er,
að vinstri hliðin skilgreinir línulega vörpun

.. math::

  \begin{gathered}
   L:C^ m(I)\to C(I),\\
   Lu(t)=
   a_m(t)u^{(m)}(t)+a_{m-1}(t)u^{(m-1)}(t)+
   \cdots+a_1(t)u'(t)+a_0(t)u(t),\end{gathered}

ef :math:`a_0,\dots,a_m\in C(I)`. Hér táknar :math:`C^m(I)` línulegt
rúm allra :math:`m` sinnum samfellt deildanlegra falla á :math:`I` og
:math:`C(I)` táknar rúm allra samfelldra falla á :math:`I`. Við segjum
að línulega jafna sé
*óhliðruð:hover:`afleiðujafna!óhliðruð`*:hover:`óhliðraður` ef :math:`f`
er núllfallið. Annars segjum við að hún sé
*hliðruð:hover:`afleiðujafna!hliðruð`*:hover:`hliðraður`.

Hlutafleiðujöfnur
~~~~~~~~~~~~~~~~~

Erfitt er að lýsa hlutafleiðujöfnum með almennum hætti eins, en sem dæmi
um hlutafleiðujöfnur getum við tekið

.. math::

  \begin{aligned}
   {2}
   &\partial_xu+i\partial_yu=0,& \qquad
   &\text{({\it
   Cauchy--Riemann--jafna:hover:`Cauchy--Riemann!jafna`
   :hover:`jafna!Cauchy--Riemann`})},\\
   &\partial_x^ 2u+\partial_y^ 2u=0,&\qquad
   &\text{({\it Laplace--jafna:hover:`Laplace!jafna`:hover:`jafna!Laplace`})},\\
   &\partial_tu-\kappa(\partial_x^ 2u+\partial_y^ 2u+\partial_z^
   2u)=f(x,y,z,t),& \qquad
   &\text{({\it varmaleiðnijafna:hover:`varmaleiðnijafna`})},\\
   &\partial_t^2u-c^2(\partial_x^ 2u+\partial_y^ 2u+\partial_z^
   2u)=f(x,y,z,t),& \qquad
   &\text{({\it bylgjujafna:hover:`bylgjujafna`})}.\end{aligned}

Tilvist og ótvíræðni lausna
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Það eru margvíslegar spurningar sem menn leita svara við þegar
afleiðujöfnur eru leystar. Eðlilega fjallar fyrsta spurningin um tilvist
á lausn. Ef henni er svarað játandi er eðlilegt að spyrja næst með hvaða
skilyrðum lausn sé ótvírætt ákvörðuð og síðan hvernig ákvarða megi
lausnir og finna nálganir á þeim. Til þess að útskýra þetta skulum við
líta á einföldustu afleiðujöfnu sem hugsast getur

.. math:: u'=0.

Við vitum að öll fastaföll, :math:`u(t)=c`, :math:`t\in{{\mathbb  R}}`,
uppfylla þessa jöfnu og að sérhver lausn er fastafall. Spurningunni um
tilvist er því svarað játandi, en spurningunni um ótvíræðni er svarað
neitandi, því við höfum óendanlega margar lausnir. Lítum á aðeins
flóknara dæmi, nefnilega jöfnuna

.. _1.1.6:

.. math:: u'=f,

þar sem við hugsum okkur að fallið :math:`f` sé samfellt á bilinu
:math:`I\subset {{\mathbb  R}}`. Undirstöðusetning stærðfræðigreiningarinnar segir okkur
að sérhvert stofnfall :math:`f` sé lausn. Jafnframt vitum við að
mismunur tveggja stofnfalla er fastafall og því er sérhver lausn af
gerðinni

.. math::

  u(t)=b+\int_a^ t f(\tau) \, d\tau, \qquad t,a\in I.
Ef við setjum nú það skilyrði að lausnin eigi að taka ákveðið gildi
:math:`b` í punktinum :math:`a\in I`,

.. math::

  u'=f(t), \qquad u(a)=b,
þá gefur undirstöðusetning stærðfræðigreiningarinnar að til er ótvírætt
ákvörðuð lausn og hún er sett fram með formúlunni hér að framan.

Fyrsta stigs jöfnur
-------------------

Línulegar jöfnur
~~~~~~~~~~~~~~~~

Fyrsta stigs línuleg afleiðujafna er af gerðinni

.. math::

  a_1(t)u'+a_0(t)u=f(t).
:hover:`afleiðujafna!línuleg fyrsta stigs` :hover:‘línuleg fyrsta stigs
afleiðujafna‘ Við skulum rifja upp aðferðina til að leysa þessa jöfnu í
því tilfelli að stuðlarnir eru samfelld föll á einhverju bili :math:`I`
og að :math:`a_1(t)\neq 0` fyrir öll :math:`t\in I`. Með því að deila í gegnum jöfnuna með
:math:`a_1(t)`, þá getum við gert ráð fyrir því að :math:`a_1` sé
fastafallið :math:`1` og við ætlum því að leysa

.. math:: u'+a_0(t)u=f(t).

Aðferðin gengur út á að skilgreina :math:`A` sem eitthvert stofnfall
:math:`a_0`,

.. math:: A(t)=c+\int_a^t a_0({\tau})\, d{\tau}, \qquad t,a\in I,

og athuga að ef :math:`u` er lausn, þá gildir

.. math:: \dfrac d{dt} (e^{A(t)}u(t))=e^{A(t)}(u'(t)+a_0(t)u(t))=e^{A(t)}f(t).

Af þessari jöfnu leiðir síðan að

.. math:: e^{A(t)}u=C+\int_a^t e^{A({\tau})}f({\tau}) \, d{\tau},

og þar með fæst almenna lausnarformúlan

.. math:: u(t)=e^{-A(t)}(C+\int_a^t e^{A({\tau})}f({\tau}) \, d{\tau}),

þar sem :math:`C` er einhver fasti. Þessi útreikningur okkar sýnir að
sérhver lausn á jöfnunni hlýtur að vera af þessari gerð. Nú er hins
vegar lauflétt að sýna að þetta er lausn, með því að stinga þessari
formúlu inn í afleiðujöfnuna. Verkefnið

.. math:: u'+a_0(t)u=f(t), \qquad u(a)=b,

hefur ótvírætt ákvarðaða lausn og hún er fundin með því að velja
stofnfallið :math:`A` þannig að :math:`A(a)=0` og :math:`C=b`,

.. math::

  u(t)=e^{-A(t)}(b+\int_a^ t e^{A(\tau)}f(\tau) \, d\tau), 
  \qquad A(t)=\int_a^ t a_0(\tau) \, d\tau.

Aðskiljanlegar jöfnur
~~~~~~~~~~~~~~~~~~~~~

Við segjum að fyrsta stigs afleiðujafna :math:`u'=f(t,u)` sé
*aðskiljanleg*:hover:`afleiðujafna!aðskiljanleg` ef hægt er að rita
fallið :math:`f` sem kvóta af gerðinni :math:`f(t,x)=g(t)/h(x)`. Til
þess að leysa jöfnuna, þá skrifum við hana sem :math:`h(u)u'=g(t)` og
heildum síðan

.. math:: \int h(u(t))u'(t) \, dt = c+\int g(t)\, dt,

þar sem :math:`c` er heildunarfasti. Ef við viljum síðan leysa
verkefnið

.. math:: u'=f(t,u), \qquad u(a)=b,

þá veljum við stofnfall :math:`H` fyrir :math:`h` og heildum

.. math::

  H(u(t))-H(b)= \int_b^{u(t)} h(x) \, dx =
  \int_a^ t h(u({\tau}))u'({\tau}) \, d{\tau} = 
   \int_a^ t g(\tau) \, d\tau.

Ef til er grennd um punktinn :math:`b` þar sem fallið :math:`H` hefur
andhverfu, þá getum við skrifað lausnina sem

.. math::

  u(t) = H^{[-1]}\left( H(b)+G(t)\right), \qquad G(t)=\int_a^ t
   g(\tau)\, d\tau. 
Í útreikningum á venjulegum dæmum borgar sig yfirleitt ekki að reikna
út formúlu fyrir :math:`H^ {[-1]}` og stinga síðan gildinu
:math:`H(b)+G(t)` inn í þá formúlu eins og lýst er hér. Þess í stað er
betra að leysa :math:`u(t)` úr jöfnunni :math:`H(u(t))-H(b)=G(t)`.

.. _grein1.3:

Afleiðujöfnuhneppi
------------------

*Afleiðujöfnuhneppi*:hover:`afleiðujöfnuhneppi` er safn af jöfnum sem
lýsa sambandi milli gilda óþekktra falla og gilda á einstökum afleiðum
þeirra. Ef óþekktu föllin eru háð einni breytistærð, þá kallast það
*venjulegt:hover:`afleiðujöfnuhneppi!venjulegt` afleiðujöfnuhneppi*, en
það kallast *hlutafleiðujöfnuhneppi*:hover:`hlutafleiðujöfnuhneppi` ef
þau eru háð fleiri en einni breytistærð. Venjulegt afleiðujöfnuhneppi er
alltaf hægt að umrita yfir í jöfnur af gerðinni

.. math::

  F_j(t,u_1,\dots,u_k,u_1{{^{\prime}}},\dots,u_k{{^{\prime}}},\dots,
   u_1^{(m)},\dots,u_k^{(m)})=0, \qquad j=1,\dots,l,

þar sem :math:`t` táknar breytistærðina, :math:`u_1,\dots,u_k` eru
óþekktu föllin og föllin :math:`F_1,\dots,F_l` taka gildi í
:math:`{{\mathbb  R}}` eða :math:`{{\mathbb  C}}`. Til þess að einfalda
ritháttinn, þá skilgreinum við vigurgildu föllin
:math:`u=(u_1,\dots,u_k)` og :math:`F=(F_1,\dots,F_l)`. Þá eru jöfnurnar
jafngildar vigurjöfnunni :math:`F(t,u,u{{^{\prime}}},\dots,u^{(m)})=0`
sem hefur sama útlit.

Staðalform hneppa
~~~~~~~~~~~~~~~~~

Við segjum að hneppið sé á
*staðalformi*:hover:`staðalform`:hover:`afleiðujöfnuhneppi!staðalform` ,
ef fjöldi jafna og fjöldi óþekktra falla er sá sami og það er af
gerðinni

.. math:: u^{(m)}=G(t,u,u{{^{\prime}}},\dots,u^{(m-1)}).

Mikilvægustu hneppin sem við fáumst við eru fyrsta stigs venjuleg
afleiðujöfnuhneppi á staðalformi

.. math:: u{{^{\prime}}}=G(t,u).

Ef við skrifum upp hnitaföllin fyrir þetta hneppi, þá fáum við
jöfnurnar

.. math::

  \begin{aligned}
   u_1{{^{\prime}}}&= G_1(t, u_1,\dots, u_m),\\
   u_2{{^{\prime}}}&= G_2(t, u_1,\dots, u_m),\\
   &\quad \vdots\\
   u_m{{^{\prime}}}&= G_m(t, u_1,\dots, u_m),\end{aligned}

þar sem :math:`G_j:\Omega\to{{\mathbb  R}}`,
:math:`\Omega\subset {{\mathbb  R}}\times{{\mathbb  R}}^m` eða
:math:`G_j:\Omega\to{{\mathbb  C}}`,
:math:`\Omega\subset {{\mathbb  R}}\times{{\mathbb  C}}^m` eftir því
hvort við viljum að lausnin taki rauntölugildi eða tvinntölugildi.
Föllin :math:`u=(u_1,\dots,u_m)` og :math:`G=(G_1,\dots,G_m)` taka gildi
í vigurrúminu :math:`{{\mathbb  R}}^ m` eða
:math:`{{\mathbb  C}}^ m`, eftir því hvort við hugsum okkur að
lausnirnar eigi að taka rauntölugildi eða tvinntölugildi.

Línuleg afleiðujöfnuhneppi
~~~~~~~~~~~~~~~~~~~~~~~~~~

Við segjum að fyrsta stigs jöfnuhneppi sé
*línulegt*:hover:`afleiðujöfnuhneppi!línulegt` ef fallið :math:`G` er af
gerðinni

.. math:: G(t,x)=A(t)x+f(t),

þar sem :math:`A(t)` er :math:`m\times m` fylki og :math:`f(t)` er
:math:`m`–vigur. Ef við skrifum upp hnitin þá verður hneppið

.. math::

  \begin{aligned}
   u_1{{^{\prime}}}&=a_{11}(t)u_1+\cdots+a_{1m}(t)u_m+f_1(t),\\
   u_2{{^{\prime}}}&=a_{21}(t)u_1+\cdots+a_{2m}(t)u_m+f_2(t),\\
   &\qquad \qquad \vdots\qquad \qquad \qquad \qquad \vdots\\
   u_m{{^{\prime}}}&=a_{m1}(t)u_1+\cdots+a_{mm}(t)u_m+f_m(t).\end{aligned}

Hér eru föllin :math:`a_{jk}(t)` stökin í fylkinu :math:`A(t)`. Við
segjum að hneppið sé *óhliðrað*:hover:`afleiðujöfnuhneppi!óhliðrað` ef
:math:`f` er núllfallið og við segjum að það sé
*hliðrað*:hover:`afleiðujöfnuhneppi!hliðrað` annars.

Jöfnur af hærri stigum og jafngild hneppi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum nú á venjulega :math:`m`–ta stigs afleiðujöfnu á staðalformi

.. _1.3.2:

.. math:: v^{(m)}=G(t,v,v{{^{\prime}}},\dots,v^{(m-1)}).

Ef við skilgreinum vigurfallið :math:`u=(u_1,\dots,u_m)` með

.. math:: u_1=v, \quad u_2=v{{^{\prime}}},\dots, \quad  u_m=v^{(m-1)},

þá uppfyllir :math:`u` jöfnuhneppið

.. math::

  u_1{{^{\prime}}}= u_2, \quad
   u_2{{^{\prime}}}= u_3, \quad\dots \quad
   u_{m-1}{{^{\prime}}}= u_m, \quad
   u_m{{^{\prime}}}=G(t, u_1,\dots,u_m). 

Jafnan og jöfnuhneppið eru jafngild í þeim skilningi að sérhver lausn
:math:`v` á gefur lausn :math:`u=(v,v{{^{\prime}}},\dots,v^{(m-1)})`
á hneppinu og sérhver lausn :math:`u` á hneppinu gefur lausnina
:math:`v=u_1` á jöfnunni. Þessi einfalda staðreynd er mikilvæg, því
einfalt reynist að sanna tilvist á lausnum á fyrsta stigs jöfnuhneppum á
staðalformi. Þá niðurstöðu er síðan hægt að nota til að sanna tilvist á
lausnum á jöfnum af stigi stærra en :math:`1`.

Línulega afleiðujafnan

.. math:: a_m(t)v^{(m)}+\cdots+a_1(t)v{{^{\prime}}}+ a_0(t)v=g(t)

er greinilega jafngild línulega hneppinu

.. _1.3.4:

.. math::

  \begin{gathered}
   u_1{{^{\prime}}}= u_2,\qquad  u_2{{^{\prime}}}= u_3, \qquad \dots, \quad
   u_{m-1}{{^{\prime}}}= u_m\\
   u_m{{^{\prime}}}=-(a_0(t)/a_m(t))u_1-\cdots-(a_{m-1}(t)/a_m(t))u_m+g(t)/a_m(t),\nonumber \end{gathered}

ef :math:`a_m(t)\neq 0` fyrir öll :math:`t\in I`. Fylkið :math:`A` og
vigurinn :math:`f` verða þá

.. math::

  A=\left[\begin{matrix}
   0&1&\dots&0\\
   0&0&\dots&0\\
   \vdots&\vdots&\ddots&\vdots\\
   0&0&\dots&1\\
   -a_0/a_m&-a_1/a_m&\dots&-a_{m-1}/a_m
   \end{matrix}\right],
   \qquad
   f=\left[\begin{matrix}
   0\\
   0\\
   \vdots\\
   0\\
   g/a_m
  \end{matrix}\right].

Upphafsgildisverkefni:hover:`upphafsgildisverkefni`
---------------------------------------------------

Oft hafa menn áhuga á að finna lausnir á afleiðujöfnum og
afleiðujöfnuhneppum sem uppfylla einhverja ákveðna eiginleika.
*Upphafsgildisverkefni* snúast um að leysa afleiðujöfnuhneppi með því
hliðarskilyrði að lausnin og einhverjar afleiður hennar taki fyrirfram
gefin gildi í ákveðnum punkti. Upphafsgildisverkefni fyrir fyrsta stigs
hneppi af staðalformi er til dæmis verkefnið

.. math::

  u{{^{\prime}}}=f(t,u), \quad t\in I, \qquad u(a)=b.

Hér er átt við að finna eigi lausn :math:`u=(u_1,\dots,u_m)` á jöfnunni
á bilinu :math:`I`, sem tekur gildið :math:`b=(b_1,\dots,b_m)` í
punktinum :math:`a\in I`. Upphafsgildisverkefni fyrir :math:`m`-ta stigs
línulega jöfnu er af gerðinni

.. math::

  \begin{cases} a_m(t)v^{(m)}+\cdots+a_1(t)v{{^{\prime}}}+a_0(t)v=g(t), & t\in I,\\
   v(a)=b_0, \quad v{{^{\prime}}}(a)=b_1, \quad \dots \quad  v^{(m-1)}(a)=b_{m-1}.&
   \end{cases}

Ef :math:`a_m(t)\neq 0` fyrir öll :math:`t\in I`, þá getum við deilt í
gegnum jöfnuna með :math:`a_m(t)` og umskrifað hana síðan yfir í
jafngilt :math:`m\times m` línulegt jöfnuhneppi með óþekkta vigurfallið
:math:`u=(v,v{{^{\prime}}},\dots,v^{(m-1)})`.

Jaðargildisverkefni
-------------------

*Jaðargildisverkefni*:hover:`jaðargildisverkefni` snúast um að leysa
jöfnu

.. math:: u^{(m)}=f(t,u,u{{^{\prime}}},\dots,u^{(m-1)})

af stigi :math:`m` á takmörkuðu bili :math:`I=[a,b]` með skilyrðum á

.. math::

  u(a), \ u'(a),\dots,  \ u^{(m-1)}(a)\qquad \text{ og } 
   \qquad  u(b), \ u(b),\dots, \ u^{(m-1)}(b).

Þessi skilyrði eru venjulega sett fram þannig að ákveðnar línulegar
samantektir af þessum fallgildum eigi að taka fyrirfram gefin gildi.
Fyrir annars stigs jöfnu geta
*jaðarskilyrðin*:hover:`jaðargildisskilyrði` til dæmis verið

.. math:: u(a)=0, \qquad u{{^{\prime}}}(b)=0.

*Lotubundin*:hover:`jaðargildisskilyrði!lotubundin` jaðarskilyrði eru
af gerðinni

.. math:: u(a)=u(b), \qquad u{{^{\prime}}}(a)=u{{^{\prime}}}(b).

Almenn línuleg jaðarskilyrði fyrir annars stigs jöfnu eru

.. math::

  \begin{aligned}
   B_1u&={\alpha}_{11}u(a)+{\alpha}_{12}u{{^{\prime}}}(a)
       +{\beta}_{11}u(b)+{\beta}_{12}u{{^{\prime}}}(b)=c_1\\
   B_2u&={\alpha}_{21}u(a)+{\alpha}_{22}u{{^{\prime}}}(a)
       +{\beta}_{21}u(b)+{\beta}_{22}u{{^{\prime}}}(b)=c_2,\end{aligned}

þar sem stuðlarnir :math:`{\alpha}_{jk}`, :math:`{\beta}_{jk}`,
:math:`c_{j}` eru gefnir fyrir :math:`j,k=1,2`. Almenn línuleg
jaðarskilyrði fyrir :math:`m`-ta stigs jöfnu eru af gerðinni

.. math::

  B_ju=\sum\limits_{l=1}^m \big({\alpha}_{jl}u^{(l-1)}(a)
   +{\beta}_{jl}u^{(l-1)}(b)\big)=c_j, \qquad j=1,2,\dots,m.

Við lítum á :math:`B_j` sem línulega vörpun
:math:`C^{m-1}[a,b]\to {{\mathbb  C}}` og skilgreinum
*jaðargildisvirkja:hover:`jaðargildisvirki`:hover:`virki`*:hover:`virki!jaðargildis`
:math:`B:C^{m-1}[a,b]\to {{\mathbb  C}}^m` með formúlunni
:math:`Bu=(B_1u,\dots,B_mu)`. Almennt jaðargildisverkefni fyrir
:math:`m`-ta stigs línulega jöfnu er að leysa

.. math::

  \begin{cases}
   a_m(t)u^{(m)}+\cdots+a_1(t)u{{^{\prime}}}+a_0(t)u=f(t),  &t\in ]a,b[\\
   Bu=c, \qquad B_ju=\sum\limits_{l=1}^m \big({\alpha}_{jl}u^{(l-1)}(a)
   +{\beta}_{jl}u^{(l-1)}(b)\big), 
  \end{cases}

fyrir gefið fall :math:`f\in C[a,b]` og gefinn vigur
:math:`c\in {{\mathbb  C}}^m`. Athugið að upphafsskilyrðin í
(:ref:`Link title <1.4.2>`) eru dæmi um almenn línuleg jaðarskilyrði, þar sem við
setjum :math:`{\beta}_{jl}=0` fyrir öll :math:`j` og :math:`l`,
:math:`{\alpha}_{jl}=1` ef :math:`j=l` og :math:`{\alpha}_{jl}=0` ef
:math:`j\neq l`. Ef bilið :math:`I` er ótakmarkað geta verið skilyrði á
markgildin

.. math::

  \lim_{x\to\pm\infty}u(x), \qquad 
   \lim_{x\to \pm\infty}u{{^{\prime}}}(x),\quad \dots

eftir því sem við á. Þessi skilyrði geta verið sams konar línulegar
samantektir og við höfum verið að lýsa.

Tilvist og ótvíræðni lausna á afleiðujöfnum
-------------------------------------------

Í þessari grein ætlum við að fjalla um tilvist á lausn á
upphafsgildisverkefninu

.. math::

  u{{^{\prime}}}=f(t,u),  \qquad u(a)=b,
þar sem fallið :math:`f\in C(\Omega,{{\mathbb  R}}^m)` er skilgreint á
einhverju hlutmengi :math:`\Omega` í
:math:`{{\mathbb  R}}\times {{\mathbb  R}}^m`, :math:`a` er gefin
rauntala, :math:`b` er gefinn vigur og :math:`(a,b)\in \Omega`.
Tilfellið að :math:`f` taki gildi í tvinntölurúminu
:math:`{{\mathbb  C}}^m` og að :math:`\Omega` sé hlutmengi í
:math:`{{\mathbb  R}}\times {{\mathbb  C}}^m` fæst síðan með því að líta
á :math:`{{\mathbb  C}}^m` sem vigurrúmið :math:`{{\mathbb  R}}^{2m}`.
Ef við ætlumst til þess að lausnin :math:`u` hafi samfellda afleiðu, þá
þurfum við auðvitað að gera ráð fyrir því að fallið :math:`f` sé
samfellt.

Setning
^^^^^^^

(*Peano:hover:`Peano`*:hover:`setning!Peano`).   Gerum ráð fyrir að
:math:`\Omega` sé grennd um punktinn :math:`(a,b)\in {{\mathbb  R}}\times{{\mathbb  R}}^m` og að
:math:`f\in C(\Omega,{{\mathbb  R}}^m)`. Þá er til opið bil :math:`I`
sem inniheldur punktinn :math:`a` og fall
:math:`u:I\to {{\mathbb  R}}^m`, þannig að :math:`(t,u(t))\in \Omega`,
:math:`u{{^{\prime}}}(t)=f(t,u(t))` fyrir öll :math:`t\in I` og
:math:`u(a)=b`.

Setning Peano er of erfið til þess að við getum átt við að sanna hana
hér, en fróðlegt er að vita hvað hún segir. Við munum hins vegar sanna
tvær tilvistarsetningar, sem kenndar eru við Picard. Í þeim gefum við
okkur meiri forsendur um fallið :math:`f`, en að það sé bara samfellt,
og þær tryggja að lausnin verði ótvírætt ákvörðuð. Setning Peano segir
okkur einungis að til sé lausn en hún segir ekkert um það hvort lausnin
er ótvírætt ákvörðuð.

.. _syn1.7.2:

Sýnidæmi
^^^^^^^^

Athugum upphafsgildisverkefnið :math:`u{{^{\prime}}}=3u^{2/3}`,
:math:`u(0)=0`. Fyrir

sérhvert :math:`\alpha>0` fáum við lausnina :math:`u_\alpha`, sem
skilgreind er með

.. math::

  u_\alpha(t)=\begin{cases}
   (t+\alpha)^3, &t<-\alpha,\\
   0, &-\alpha\leq t<\alpha,\\
   (t-\alpha)^3, &\alpha\leq t.
   \end{cases}

Þetta dæmi sýnir okkur að til þess að fá ótvírætt ákvarðaða lausn
þurfum við að setja einhver strangari skilyrði á :math:`f` en
samfelldni.

Skilgreining
^^^^^^^^^^^^

(*Lipschitz–skilyrði*).   Látum :math:`f:\Omega\to{{\mathbb  R}}^m` vera
fall, þar sem :math:`\Omega\subset {{\mathbb  R}}\times {{\mathbb  R}}^m` og :math:`A\subset \Omega`. Ef til er fasti :math:`C`
þannig að

.. math::

  |f(t,x)-f(t,y)|\leq C|x-y|,\qquad (t,x), (t,y)\in
    A,
þá segjum við að :math:`f` uppfylli
*Lipschitz–skilyrði*:hover:`Lipschitz–skilyrði` í menginu :math:`A`.

.. _syn1.7.4:

Sýnidæmi
^^^^^^^^

(i) Ef jöfnuhneppið er línulegt, :math:`f(t,x)=A(t)x+g(t)`,
:math:`A\in C(I,{{\mathbb  C}}^{m\times m})` og
:math:`g\in C(I,{{\mathbb  C}}^m)`, þá uppfyllir :math:`f`
Lipschitz–skilyrði í :math:`J\times {{\mathbb  C}}^m` fyrir sérhvert
lokað og takmarkað hlutbil :math:`J\subset I`. Þetta sést á því að

.. math::

  |f(t,x)-f(t,y)|=|A(t)(x-y)|
   \leq \sum\limits_{j,k=1}^m |a_{jk}(t)||x-y|\leq C|x-y|,

þar sem :math:`C=\sup\sum\limits_{j,k=1}^m |a_{jk}(t)|` og efra markið
er tekið yfir öll :math:`t\in J`.

(ii) Látum :math:`f\in C^{1}(\Omega,{{\mathbb  R}}^m)` og gerum ráð
fyrir að :math:`\Omega` sé þannig að fyrir sérhvert par af punktum
:math:`(t,x), (t,y)` í :math:`\Omega` liggi línustrikið milli þeirra í
:math:`\Omega`. Línustrikið samanstendur af öllum punktum
:math:`(t,\tau x+(1-\tau)y)`, :math:`\tau\in [0,1]`. Látum nú :math:`A`
vera lokað og takmarkað hlutmengi af :math:`\Omega`, sem hefur þann
eiginleika að fyrir sérhvert par af punktum :math:`(t,x), (t,y)` í
:math:`A` liggur línustrikið á milli þeirra í :math:`A`. Þá er

.. math::

  \begin{aligned}
   |f(t,x)-f(t,y)|&=|\int_0^ 1\dfrac d{d\tau}f(t,(1-\tau)y+\tau x) \,
   d\tau|\\
   &=|\int_0^ 1 \sum\limits_{j=1}^ m
   \partial_{x_j}f(t,(1-\tau)y+\tau x)
   (x_j-y_j) \, d\tau|\\
   &\leq \sup\limits_{(\tau,\xi)\in A} 
   \sum\limits_{j=1}^ m |\partial_{x_j}f(\tau,\xi)||x-y|,\end{aligned}

og þar með uppfyllir :math:`f` Lipschitz–skilyrði í :math:`A`.

(iii) Lítum nú á fallið :math:`f(t,x)=x^ 2`, með
:math:`\Omega={{\mathbb  R}}\times {{\mathbb  R}}`. Það uppfyllir

.. math:: |f(t,x)-f(t,y)|=|x+y||x-y|,

en þetta gefur okkur að :math:`f` uppfylli ekki Lipschitz–skilyrði í
:math:`\Omega`, því þátturinn :math:`x+y` er ekki takmarkaður. Ef við
látum hins vegar :math:`[\alpha,\beta]` vera takmarkað bil og veljum
:math:`A={{\mathbb  R}}\times [\alpha,\beta]`, þá uppfyllir fallið
:math:`f` Lipschitz–skilyrði í :math:`A` og við getum valið fastann
:math:`C` sem :math:`C=2(|\alpha|+|\beta|)`.

(iv) Fallið :math:`f(t,x)=3x^{2/3}`, í sýnidæmi :ref:`Link title <syn1.7.2>`, er
samfellt, en uppfyllir ekki Lipschitz–skilyrði í neinni grennd um
:math:`0`, því :math:`|f(t,x)-f(t,0)|=x^{2/3}=x^{-1/3}|x-0|` og
:math:`x^{-1/3}\to \infty` ef :math:`x\to 0`.

Nú kemur í ljós að Lipschitz–skilyrði tryggir að lausnin verður ótvírætt
ákvörðuð:

.. _set1.7.5:

Setning
^^^^^^^

(*Picard; víðfeðm útgáfa*).
 :hover:`Picard–setningin`:hover:`setning!Picard` Látum
:math:`I\subset {{\mathbb  R}}` vera opið bil, :math:`a\in I`,
:math:`b\in {{\mathbb  R}}^ m`,
:math:`f\in C(I\times {{\mathbb  R}}^ m,{{\mathbb  R}}^ m)` og gerum
ráð fyrir að :math:`f` uppfylli Lipschitz–skilyrði í
:math:`J\times {{\mathbb  R}}^ m` fyrir sérhvert lokað og takmarkað
hlutbil :math:`J` í :math:`I`. Þá er til ótvírætt ákvörðuð lausn
:math:`u\in C^ 1(I,{{\mathbb  R}}^ m)` á upphafsgildisverkefninu

.. math:: u{{^{\prime}}}=f(t,u), \qquad u(a)=b.

Þessi setning er önnur tveggja tilvistarsetninga sem við sönnum í næstu
grein. Eins og fram hefur komið kallast hún venjulega *víðfeðm* útgáfa
af tilvistarsetningu fyrir fyrsta stigs hneppi. Ástæðan fyrir
nafngiftinni er, að við fáum lausn á bili sem inniheldur öll
:math:`t`–gildi þar sem hægri hlið jöfnunnar er skilgreind. Tökum nú
fyrir tvær mikilvægustu afleiðingar setningarinnar. Í sýnidæmi
:ref:`Link title <syn1.7.4>` sáum við að forsendurnar í setningu :ref:`Link title <set1.7.5>` eru
uppfylltar fyrir línuleg jöfnuhneppi með samfellda stuðla. Við lítum á
vigurrúmið :math:`{{\mathbb  C}}^m` yfir tvinntölurnar sem :math:`2m`
víða rúmið :math:`{{\mathbb  R}}^{2m}` yfir rauntölurnar og fáum:

Fylgisetning
^^^^^^^^^^^^

Látum :math:`I\subset {{\mathbb  R}}` vera opið bil, :math:`a\in I`,
:math:`b\in {{\mathbb  C}}^ m`,
:math:`A\in C(I,{{\mathbb  C}}^{m\times m})` og
:math:`f\in C(I,{{\mathbb  C}}^ m)`. Þá er til ótvírætt ákvörðuð lausn
:math:`u\in C^ 1(I,{{\mathbb  C}}^ m)` á upphafsgildisverkefninu

.. math::

  u{{^{\prime}}}=A(t)u+f(t) \qquad u(a)=b.
Með umskrift á upphafsgildisverkefni fyrir :math:`m`-ta stigs
afleiðujöfnu yfir í jafngilt hneppi fáum við:

Fylgisetning
^^^^^^^^^^^^

Látum :math:`I\subset {{\mathbb  R}}` vera opið bil, :math:`a\in I`,
:math:`b_0,\dots,b_{m-1} \in {{\mathbb  C}}`,
:math:`a_0,\dots,a_m, g\in C(I)` og :math:`a_m(t)\neq 0` fyrir öll
:math:`t\in I`. Þá er til ótvírætt ákvörðuð lausn :math:`u\in C^ m(I)`
á upphafsgildisverkefninu

.. math::

  \begin{gathered}
   a_m(t)u^ {(m)}+\cdots+a_1(t)u{{^{\prime}}}+a_0(t)u=g(t),\\
   u(a)=b_0, u{{^{\prime}}}(a)=b_1,\dots, u^{(m-1)}(a)=b_{m-1}.\end{gathered}

Nú setjum við fram aðra útgáfu sem venjulega kallast *staðbundin* útgáfa
af tilvistarsetningu fyrir fyrsta stigs hneppi:

.. _set1.7.8:

Setning
^^^^^^^

(*Picard; staðbundin útgáfa*:hover:`Picard–setningin`).
 :hover:`setning!Picard` Látum :math:`\Omega` vera opið hlutmengi í
:math:`{{\mathbb  R}}\times {{\mathbb  R}}^{m}`,
:math:`a\in {{\mathbb  R}}`, :math:`b\in {{\mathbb  R}}^ m`,
:math:`(a,b)\in \Omega` og :math:`f\in C(\Omega,{{\mathbb  R}}^ m)`.
Gerum ráð fyrir að til sé grennd :math:`U` um punktinn :math:`(a,b)`
innihaldin í :math:`\Omega` og að fallið :math:`f` uppfylli
Lipschitz–skilyrði í :math:`U`. Þá er til opið bil :math:`I` á
:math:`{{\mathbb  R}}` sem inniheldur :math:`a` og ótvírætt ákvörðuð
lausn :math:`u\in C^ 1(I, {{\mathbb  R}}^m)` á upphafsgildisverkefninu

.. math:: u{{^{\prime}}}=f(t,u), \qquad u(a)=b.

Ástæðan fyrir því að þessi setning kallast *staðbundin* útgáfa af
tilvistarsetningunni fyrir fyrsta stigs afleiðujöfnuhneppi er sú, að hún
segir okkur einungis að til sé bil :math:`I` þar sem lausnin er til. Í
sönnuninni, sem við tökum fyrir í næstu grein, kemur fram hvernig bilið
:math:`I` er háð :math:`U`, Lipschitz–fasta fallsins :math:`f` og
upphafsgildinu :math:`b`.

Sýnidæmi
^^^^^^^^

Við skulum taka eitt dæmi til þess að sjá hvernig skilgreiningarsvæði
lausnarinnar er háð upphafsgildinu :math:`b` og líta á verkefnið
:math:`u'=u^ 2`, :math:`u(a)=b`, þar sem :math:`b` er jákvæð rauntala. Lausnin er
fallið

.. math:: u(t)=\dfrac b{1-b(t-a)}, \qquad t\in I=]-\infty,a+1/b[.

Maður skyldi ætla að óreyndu, að svona einföld jafna hefði lausn, sem
skilgreind er á öllum rauntalnaásnum, en svo er greinilega ekki.
Skilgreiningarsvæðið minnkar eftir því sem upphafsgildið stækkar.
Athugið að engu að síður hefur verkefnið lausn í grennd um :math:`a`
fyrir sérhvert val á :math:`(a,b)`. Við sáum í sýnidæmi :ref:`Link title <syn1.7.4>`
(iii) uppfyllir skilyrðin í staðbundnu útgáfu Picard setningarinnar, en
ekki þeirrar víðfeðmu.

Aðferðin sem beitt er í sönnuninni á þessum setningum er kennd við
franska stærðfræðinginn Émile Picard. Eins og áður hefur verið sagt
framkvæmum við hana í smáatriðum í næstu grein. Auðvelt er að skilja
meginhugmyndina í sönnuninni á víðfeðmu útgáfunni af Picard–setningunni
og skulum við líta á hana núna.

Við athugum fyrst, að

.. math::

  u\in C^ 1(I,{{\mathbb  R}}^ m), \quad u{{^{\prime}}}=f(t,u),\quad t\in I, \quad
   u(a)=b 
er jafngilt því að

.. math::

  u\in C(I,{{\mathbb  R}}^ m),\quad 
   u(t)=b+\int_a^ t f(\tau,u(\tau))\, d\tau, \qquad t\in I.
Okkur dugir því að sanna að til sé ótvírætt ákvarðað fall :math:`u\in C(I,{{\mathbb  R}}^ m)` sem uppfyllir heildisjöfnuna (:ref:`Link title <1.7.5>`).
Tilvistin er fengin með því að skilgreina runu :math:`\{ u_n\}` af
föllum í :math:`C(I,{{\mathbb  R}}^ m)` með formúlunni

.. math::

  u_0(t)=b, \qquad 
   u_n(t)=b+\int_a^ t f(\tau,u_{n-1}(\tau))\, d\tau, \qquad t\in
   I,
og sýna síðan að þessi fallaruna sé samleitin að markfalli :math:`u`.
Ekki er nóg að sýna að runan :math:`\{u_n(t)\}` stefni á :math:`u(t)` í
sérhverjum punkti heldur þurfum við að sanna að :math:`\{u_n\}` sé
samleitin í *jöfnum mæli*:hover:`samleitni!í jöfnum mæli` á sérhverju
lokuðu og takmörkuðu hlutbili :math:`J` af :math:`I`. Að því fengnu gefa
niðurstöðurnar í grein 3.5 að markfallið :math:`u` er í
:math:`C(I,{{\mathbb  R}}^ m)`. Lipschitz skilyrðið gefur að

.. math:: |f(t,u_n(t))-f(t,u(t))|\leq C|u_n(t)-u(t)|, \qquad t\in J,

og þar með að runan :math:`f(t,u_n(t))` stefnir á markfallið
:math:`f(t,u(t))` í jöfnum mæli á :math:`J`. Þá megum við skipta á
heildi og markgildi og við fáum það sem sanna á,

.. math::

  \begin{gathered}
   u(t)= \lim\limits_{n\to +\infty} u_n(t) =
   b+\lim\limits_{n\to +\infty} \int_a^ t f(\tau,u_{n-1}(\tau)) \, d\tau =\\
   =
   b+\int_a^ t \lim\limits_{n\to +\infty} f(\tau,u_{n-1}(\tau)) \, d\tau =
   b+ \int_a^ t f(\tau,u(\tau)) \, d\tau.\end{gathered}

Tökum nú tvö dæmi, sem sýna hvers er að vænta um samleitni rununnar
:math:`\{u_n\}`.
