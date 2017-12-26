
Dreififöll og veikar lausnir á hlutafleiðujöfnum
================================================

Inngangur
---------

Í greinum 2.8, 6.9 og 7.6 kynntumst við nokkrum undirstöðuhugtökum um
dreififöll á rauntalnalínunni :math:`{{\mathbb  R}}={{\mathbb  R}}^1`.
Auðvelt er að alhæfa þau hugtök yfir á rúmið :math:`{{\mathbb  R}}^n` í
hærri víddum. Reyndar eru dreififöllin mun mikilvægari við úrlausn á
hlutafleiðujöfnum en við úrlausn á venjulegum afleiðujöfnum. Í þessum
stutta kafla kynnumst við örlítið veikum hlutafleiðum, veikum lausnum á
hlutafleiðujöfnum og grunnlausnum á hlutafleiðujöfnum. Einnig sjáum við
eðlisfræðilega túlkun á Green-föllum fyrir Laplace-virkjann.

Veik markgildi, veikar afleiður og föll Diracs
----------------------------------------------

Veik markgildi, veikar afleiður og föll Diracs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í setningu 2.5.2 og fylgisetningu 2.5.4 sáum við að lausnin á verkefninu

.. math::

  \begin{cases}
   P(D)u=(a_mD^m+\cdots+a_1D+a_0)u=f(t),  &t\in {{\mathbb  R}},\\
   u(0)=u{{^{\prime}}}(0)=\cdots=u^{(m-1)}(0)=0,
   \end{cases}

er gefin með formúlunni

.. math:: u(t)=\int_0^t g(t-{\tau})f({\tau})\, d{\tau},

þar sem fallið :math:`g` uppfyllir :math:`P(D)g=0`,
:math:`g(0)=g{{^{\prime}}}(0)=\cdots=g^{(m-2)}(0)=0,` og
:math:`g^{(m-1)}(0)=1/a_m`. Nú skulum við athuga hvernig lausnin
breytist með :math:`f`. Látum því :math:`f_j` vera runu af samfelldum
föllum á :math:`{{\mathbb  R}}` og :math:`u_j` vera lausnina á
(:ref:`Link title <2.8.1>`), sem gefin er með (:ref:`Link title <2.8.2>`) með :math:`f_j` í
hlutverki :math:`f`. Ef :math:`f_j` stefnir á :math:`f` í jöfnum mæli á
sérhverju takmörkuðu bili á :math:`{{\mathbb  R}}`, þá fáum við með því
að skipta á heildi og markgildi að

.. math::

  \begin{aligned}
   \lim_{j\to +{\infty}}u_j(t)&=
   \lim_{j\to +{\infty}}
   \int_0^tg(t-{\tau})f_j({\tau})\, d{\tau}\\
   &=\int_0^tg(t-{\tau})\lim_{j\to +{\infty}}f_j({\tau})\, d{\tau}\\
   &=\int_0^tg(t-{\tau})f({\tau})\, d{\tau}=u(t).\end{aligned}

Það er raunar auðvelt að sannfæra sig um að :math:`u^{(k)}\to u^{(k)}` í
jöfnum mæli á sérhverju takmörkuðu bili á :math:`{{\mathbb  R}}` ef
:math:`0\leq k\leq m`.

Nú ætlum við að sjá hvað gerist ef við stingum ósamfelldu falli
:math:`f` inn í lausnarformúluna :ref:`Link title <2.8.2>`. Til þess að einfalda
útreikninga okkar þá skilgreinum við fallið :math:`E` með

.. math:: E(t)=H(t)g(t)=\begin{cases} g(t), &t\geq 0,\\ 0, &t<0,\end{cases}

þar sem :math:`H` táknar *Heaviside-fallið*

.. math:: H(t)=\begin{cases} 1, &t\geq 0,\\ 0, &t<0,\end{cases}

.. figure:: ./myndir/fig026.svg
    :align: center
    :alt: Heaviside-fallið

    Mynd: Heaviside-fallið

Í því tilfelli að :math:`f(t)=0` ef :math:`t<0`, þá er lausnarformúlan
(:ref:`Link title <2.8.2>`) ekkert annað en

.. math:: u=E\ast f,

þar sem :math:`{\varphi}\ast {\psi}` táknar *földun* tveggja falla
:math:`{\varphi}` og :math:`{\psi}`,

.. math::

  {\varphi}\ast {\psi}(x)=\int_{-{\infty}}^{+{\infty}}
   {\varphi}(x-y){\psi}(y)\, dy.

Földun er ein af undirstöðuaðgerðunum í fallafræði og hún mun oft koma
fyrir hjá okkur. Í útleiðslu okkar á lausnarformúlunni (:ref:`Link title <2.8.2>`)
gengum við út frá því að hægri hlið jöfnunnar :math:`f` væri samfellt
fall. Í margs konar útreikningum vilja menn setja inn föll sem eru
ósamfelld. Lítum á eitt slíkt dæmi:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Deyfðsveifla; framhald

Lítum nú enn einu sinni á deyfðan sveifil úr sýnidæmi 1.1.1 og látum nú
:math:`u(t)` tákna færslu hans frá jafnvægisstöðu og :math:`f(t)` tákna
summu ytri krafta sem á hann verka. *Atlag* kraftsviðsins
:math:`f` á tímabilinu :math:`[{\alpha},{\beta}]` er skilgreint sem
heildið

.. math:: \int_{\alpha}^{\beta}f(t)\, dt,

þar sem :math:`-{\infty}\leq {\alpha}\leq {\beta}\leq +{\infty}`. Við
skulum nú skilgreina kraftsvið :math:`f_{\varepsilon}` sem líkir eftir
því að sveiflinum sé komið af stað með því að slá snöggt í hann af
miklum krafti,

.. figure:: ./myndir/fig029.svg
    :align: center
    :alt: Vantar titil

    Mynd: Vantar titil

.. math::

  f_{\varepsilon}(t)=\begin{cases} 1/{\varepsilon}, &t\in [0,{\varepsilon}],\\
   0, &t\notin [0,{\varepsilon}].\end{cases}

Atlag þessa kraftsviðs er

.. math::

  \int_{-{\infty}}^{+{\infty}} f_{\varepsilon}(t)\, dt=1,
   \text{ og }
   \lim_{{\varepsilon}\to 0} f_{\varepsilon}(t)=\begin{cases} +{\infty}, &t=0,\\
   0, & t\neq 0.\end{cases}

.. math:: 

Ef :math:`u_{\varepsilon}` táknar útslag sveifilsins, þá gefur
lausnarformúlan (:ref:`Link title <2.8.5>`) okkur að

.. math::

  \begin{aligned}
   u_{\varepsilon}(t)&=E\ast f_{\varepsilon}(t)
   =\int_{-{\infty}}^{+{\infty}} E(t-{\tau})f_{\varepsilon}({\tau})\,
   d{\tau}\\
   &=\dfrac 1{\varepsilon} \int_0^{\varepsilon} E(t-{\tau})\, d{\tau}\nonumber
   =\int_0^1E(t-{\varepsilon}{\sigma})\, d{\sigma}\\
   &\to E(t), \qquad {\varepsilon}\to 0.\nonumber\end{aligned}

Nú er eðlilegt að spyrja, hvort hægt sé að taka markgildi af
kraftsviðinu :math:`f_{\varepsilon}` ef :math:`{\varepsilon}\to 0` og fá
út kraftsvið sem hefur eðlisfræðilega merkingu. Samkvæmt (:ref:`Link title <2.8.8>`)
þarf markfallið :math:`{\delta}` þá að uppfylla

.. math::

  \int_{-{\infty}}^{+{\infty}} {\delta}(t)\, dt=1,
   \qquad \text{ og } \qquad
   {\delta}(t)=\begin{cases} +{\infty}, &t=0,\\
   0, & t\neq 0.\end{cases}

Nú er okkur mikill vandi á höndum, því seinna skilyrðið skilgreinir
fall, sem hefur heildið :math:`0` og því stangast þessi tvö skilyrði á.
Til þess að komast út úr þessum vandræðum þurfum við að líta á
markgildið í (:ref:`Link title <2.8.8>`) í nýju ljósi og jafnframt að alhæfa
fallshugtakið.

.. end-toggle::

Áður en við getum alhæft fallshugtakið þurfum við að innleiða nokkur ný
hugtök. Ef :math:`{\varphi}` er samfellt fall á opnu hlutmengi :math:`X`
af :math:`{{\mathbb  R}}`, þá nefnist minnsta lokaða mengi sem
inniheldur :math:`\{x\in X; {\varphi}(x)\neq 0\}` :hover:`stoð`
fallsins :math:`{\varphi}` og hún er táknuð með
:math:`{{\text{supp}\, }}{\varphi}`. Hlutmengi af :math:`{{\mathbb  R}}`
sem er bæði lokað og takmarkað er sagt vera *þjappað*.
Við látum :math:`C_0^k(X)`, þar sem
:math:`0\leq k\leq {\infty}`, tákna mengi allra :math:`k` sinnum
samfellt deildanlegra falla á :math:`{{\mathbb  R}}` sem hafa þjappaða
stoð í :math:`X`. Þetta er línulegt hlutrúm í
:math:`C^k({{\mathbb  R}})`. Rúmið :math:`C_0^{\infty}(X)` er oft táknað
með :math:`{\cal D}(X)` og stök þess eru oft nefnd 
:hover:`prófunarföll, prófunarfall`.

Nú skulum við líta á fall :math:`f` sem er heildanlegt á sérhverju
þjöppuðu hlutmengi af :math:`X`. Það skilgreinir á eðlilegan hátt
línulega vörpun

.. math::

  u_f:C_0^{\infty}(X)\to {{\mathbb  C}}, \qquad
   u_f({\varphi})=\int_Xf(x){\varphi}(x)\, dx.

Athugið að einungis er heildað yfir þjappað hlutmengi af :math:`X`, því
sérhvert fall :math:`{\varphi}` í :math:`C_0^{\infty}(X)` er :math:`0`
alls staðar nema á þjöppuðu hlutmengi. Ef við skilgreinum margfeldið
:math:`f(x){\varphi}(x)` sem :math:`0` fyrir utan
:math:`{{\text{supp}\, }}{\varphi}`, þá breytist heildið ekki þó við
skrifum :math:`\int_{-{\infty}}^{+{\infty}}` í stað :math:`\int_X`. Það
er einmitt með því að líta á þessar línulegu varpanir, sem okkur tekst
að alhæfa fallshugtakið og þar með að gefa föllum eins og
:math:`{\delta}` í (:ref:`Link title <2.8.10>`) merkingu.

Skilgreining
^^^^^^^^^^^^

Látum :math:`X` vera opið hlutmengi af :math:`{{\mathbb  R}}`. Línuleg
vörpun

.. math:: u:C_0^{\infty}(X)\to {{\mathbb  C}}

nefnist :hover:`dreififall` á :math:`X` ef hún er samfelld
í þeim skilningi að

.. math:: u({\varphi}_j)\to u({\varphi}), \qquad j\to +{\infty},

þar sem föllin :math:`{\varphi}_j` hafa öll stoð í sama þjappaða
hlutmenginu :math:`K` í :math:`X` og
:math:`{\varphi}_j^{(k)}\to {\varphi}^{(k)}` í jöfnum mæli á
:math:`{{\mathbb  R}}` fyrir öll :math:`k=0,1,2\dots`. Mengi allra
dreififalla á :math:`X` táknum við með
:math:`{{\mathbb  D}}{{^{\prime}}}(X)`.

--------------

Þessi skilgreining kann að virðast erfið við fyrstu sýn, en í flestum
dæmum sem við tökum er auðvelt að staðfesta að (:ref:`Link title <2.8.12>`) gildi.
Þannig er línulega vörpunin :math:`u_f` í (:ref:`Link title <2.8.11>`) dreififall,
því

.. math::

  \begin{aligned}
   \lim_{j\to+{\infty}} u_f({\varphi}_j)&=
   \lim_{j\to+{\infty}} \int_{-{\infty}}^{+{\infty}} f(x){\varphi}_j(x)\, dx\\
   &=\int_{-{\infty}}^{+{\infty}} f(x)\lim_{j\to+{\infty}}{\varphi}_j(x)\, dx\\
   &=\int_{-{\infty}}^{+{\infty}} f(x){\varphi}(x)\, dx=u_f({\varphi}),\end{aligned}

því við megum skipta á heildi og markgildi, þegar við höfum samleitni í
jöfnum mæli. Athugum að tvö föll :math:`f` og :math:`g` skilgreina sama
dreififallið, :math:`u_f=u_g`, ef

.. math::

  u_f({\varphi})=\int_{-{\infty}}^{+{\infty}} f(x){\varphi}(x)\, dx
   =\int_{-{\infty}}^{+{\infty}} g(x){\varphi}(x)\, dx=u_g({\varphi}),
   \qquad {\varphi}\in C_0^{\infty}(X).

Þetta þýðir samt ekki að :math:`f(x)=g(x)` í sérhverjum punkti
:math:`x\in X`, því þessi heildi breytast ekki, þó gildum fallanna
:math:`f` og :math:`g` sé breytt í einstaka punktum.

:math:`{{\mathbb  D}}{{^{\prime}}}(X)` er greinilega línulegt rúm, þar
sem summa tveggja dreififalla :math:`u` og :math:`v` er skilgreind með

.. math:: \big(u+v\big)({\varphi})=u({\varphi})+v({\varphi}),

og margfeldi tölunnar :math:`{\alpha}\in {{\mathbb  C}}` og :math:`u`
er skilgreint með

.. math:: \big({\alpha}u\big)({\varphi})={\alpha}u({\varphi}).

Ef :math:`{\psi}\in C^{\infty}(X)`, þá skilgreinum við margfeldi
:math:`{\psi}` og :math:`u` með

.. math:: \big({\psi}u)({\varphi})=u({\psi}{\varphi}).

Þetta er eðlileg alhæfing á margföldun fallanna :math:`f` og
:math:`{\psi}`, því

.. math::

  \big({\psi}u_f\big)({\varphi})
   =u_f({\psi}{\varphi})
   =\int_{-{\infty}}^{+{\infty}}
   f(x){\psi}(x){\varphi}(x)\, dx = u_{f{\psi}}({\varphi}).

Skilgreining
^^^^^^^^^^^^

Látum :math:`a\in {{\mathbb  R}}` og skilgreinum :math:`{\delta}_a` með

.. math:: {\delta}_a({\varphi})={\varphi}(a),

þar sem :math:`{\varphi}` er samfellt í einhverri grennd um :math:`a`.
Greinilega er :math:`{\delta}_a` dreififall á sérhverju opnu mengi sem
inniheldur :math:`a` og það nefnist :math:`{\delta}`-*fall Diracs* í
punktinum :math:`a` eða *Dirac-delta-fall* í punktinum :math:`a`. Ef
:math:`a=0`, þá skrifum við aðeins :math:`{\delta}` í stað
:math:`{\delta}_0`.

--------------

Í mörgum bókum er :math:`{\delta}`-fall Diracs skilgreint, sem fallið
sem uppfyllir skilyrðin

.. math::

  \int_{-{\infty}}^{+{\infty}} {\delta}_a(t)\, dt=1,
   \qquad \text{ og } \qquad
   {\delta}_a(t)=\begin{cases} +{\infty}, &t=a,\\
   0, & t\neq a.\end{cases}

Eins og við gátum um í sýnidæmi :ref:`Link title <syn2.8.1>`, þá fá þessi skilyrði
ekki staðist saman, því síðara skilyrðið hefur í för með að heildið er
:math:`0`. Hins vegar er rétt að muna eftir þessum tveimur skilyrðum,
þegar verið er að túlka niðurstöður útreikninga með dreififöllum, þar
sem :math:`{\delta}`-föll koma fyrir.

Skilgreining
^^^^^^^^^^^^

Látum :math:`u_j` vera runu í :math:`{{\mathbb  D}}{{^{\prime}}}(X)`.
Við segjum að :math:`u_j` stefni á
:math:`u\in {{\mathbb  D}}{{^{\prime}}}(X)` og táknum það með
:math:`u_j\to u` og :math:`\lim_{j\to +{\infty}}u_j=u`, ef

.. math::

  \lim_{j\to +{\infty}} u_j({\varphi})=u({\varphi}), \qquad  {\varphi}\in
   C_0^{\infty}(X).

Ef öll dreififöllin :math:`u_j` eru af gerðinni :math:`u_{f_j}`, þar sem
:math:`f_j` eru heildanlegt á sérhverju þjöppuðu hlutmengi af :math:`X`,
þá segjum við að :math:`f_j` stefni á :math:`u` *í veikum skilningi* eða
að :math:`f_j` *stefni á* :math:`u`  *í skilningi dreififalla*. Þetta þýðir
að

.. math::

  \int_{-{\infty}}^{+{\infty}} f_j(x){\varphi}(x)\, dx \to u({\varphi}), 
   \qquad {\varphi}\in C_0^{\infty}(X),

og við táknum þessa samleitni einnig með :math:`f_j\to u` og
:math:`\lim_{j\to+{\infty}} f_j=u`.

--------------

Ef :math:`u_{\varepsilon}` eru dreififöll sem háð eru breytunni
:math:`{\varepsilon}\in {{\mathbb  R}}` þá skilgreinum við
:math:`\lim_{{\varepsilon}\to 0}u_{\varepsilon}` með hliðstæðum hætti. Sama er að segja um
:math:`\lim_{t\to +{\infty}}u_t` ef :math:`u_t` eru dreififöll sem háð
eru samfelldu breytunni :math:`t` og :math:`t` stefnir á
:math:`+{\infty}`. Það er enginn vandi að finna runur af föllum sem
stefna á :math:`{\delta}_a`:

Setning
^^^^^^^

Gerum ráð fyrir að :math:`f` sé heildanlegt fall á
:math:`{{\mathbb  R}}`, að
:math:`\int_{-{\infty}}^{+{\infty}}f(x)\, dx=1` og skilgreinum
:math:`f_{\varepsilon}(x)={\varepsilon}^{-1}f((x-a)/{\varepsilon})`. Þá
stefnir :math:`f_{\varepsilon}` á :math:`{\delta}_a` í skilningi
dreififalla ef :math:`{\varepsilon}\to 0`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við höfum

.. math::

  \begin{aligned}
   u_{f_{\varepsilon}}({\varphi})
   &=\int_{-{\infty}}^{+{\infty}} f_{\varepsilon}(x){\varphi}(x)\, dx
   =\int_{-{\infty}}^{+{\infty}} 
   {\varepsilon}^{-1}f((x-a)/{\varepsilon}){\varphi}(x)\, dx\\
   &=\int_{-{\infty}}^{+{\infty}} 
   f(y) {\varphi}(a+{\varepsilon}y)\, dy
   \to {\varphi}(a)\int_{-{\infty}}^{+{\infty}} 
   f(y)\, dy\\
   &={\varphi}(a)={\delta}_a({\varphi}).\end{aligned}

Hér eru breytuskiptin í heilduninni :math:`y=(x-a)/{\varepsilon}`,
:math:`x=a+{\varepsilon}y`, :math:`dy={\varepsilon}^{-1}dx`.
Lebesgue-setningin í viðauka C gefur okkur að það megi taka markgildi
undir heildið.

.. end-toggle::

Setning
^^^^^^^

Ef :math:`f_{\varepsilon}` er fjölskylda af föllum á
:math:`{{\mathbb  R}}`, :math:`0<{\varepsilon}<{\varepsilon}_0`, og
:math:`f_{\varepsilon}\to {\delta}` í veikum skilningi, þá gildir

.. math::

  \lim\limits_{{\varepsilon}\to 0} f_{\varepsilon}\ast {\varphi}(x)
   ={\varphi}(x), \qquad {\varphi}\in C_0^{\infty}({{\mathbb  R}}), \quad x\in {{\mathbb  R}}.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við tökum :math:`{\varphi}\in C_0^{\infty}({{\mathbb  R}})` og
skilgreinum :math:`{\psi}_x(y)={\varphi}(x-y)`. Þá gildir

.. math::

  \begin{aligned}
   f_{\varepsilon}\ast {\varphi}(x)
   &=\int_{-{\infty}}^{+{\infty}}f_{\varepsilon}(x-y){\varphi}(y)\,  dy
   =\int_{-{\infty}}^{+{\infty}}f_{\varepsilon}(y){\varphi}(x-y)\,  dy \\
   &=\int_{-{\infty}}^{+{\infty}}f_{\varepsilon}(y){\psi}_x(y)\,  dy 
   \to {\psi}_x(0)={\varphi}(x).\end{aligned}

.. end-toggle::

Setning
^^^^^^^

Ef :math:`a` er punktur í opna menginu :math:`X\subset {{\mathbb  R}}`
og :math:`{\psi}\in C^{\infty}(X)`, þá er :math:`{\psi}{\delta}_a={\psi}(a){\delta}_a`,
þ.e. aðgerðin að margfalda :math:`{\delta}_a` með fallinu :math:`{\psi}`
er sú sama og að margfalda :math:`{\delta}_a` með tvinntölunni
:math:`{\psi}(a)`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

:math:`\big({\psi}{\delta}_a\big)({\varphi})={\delta}_a({\psi}{\varphi}) ={\psi}(a){\varphi}(a)={\psi}(a){\delta}_a({\varphi})`.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Deyfð sveifla;framhald

Í sýnidæmi 2.8.1 litum við á kraftsvið sem verkaði á sveifilinn örskamma
stund. Við skulum nú líta aftur á þetta dæmi en hafa almennt kraftsvið
:math:`f` með atlag 1, :math:`f(t)=0` ef :math:`t\notin [0,1]` og
skilgreina kraftsviðið
:math:`f_{\varepsilon}(t)={\varepsilon}^{-1}f(t/{\varepsilon})`. Þá
hefur :math:`f_{\varepsilon}` atlagið :math:`1` og
:math:`f_{\varepsilon}(t)=0` ef :math:`t\notin [0,{\varepsilon}]`. Frávikið :math:`u_{\varepsilon}` frá
jafnvægisstöðunni uppfyllir

.. math::

  mu{{^{\prime\prime}}}_{\varepsilon}+cu_{\varepsilon}{{^{\prime}}}+ku_{\varepsilon}
   =f_{\varepsilon}, \qquad u_{\varepsilon}(0)=u{{^{\prime}}}_{\varepsilon}(0)=0,

og er þá gefið með földunarheildinu

.. math:: u_{\varepsilon}=E\ast f_{\varepsilon}.

Í setningu :ref:`Link title <set2.8.5>` sýndum við fram á að
:math:`f_{\varepsilon}\to {\delta}` og því er eðlilegt að túlka :math:`{\delta}` sem kraftsvið með
atlag :math:`1`, sem verkar einungis við tímann :math:`t=0`. Við fáum nú

.. math::

  \begin{aligned}
   u_{\varepsilon}(t)&=E\ast f_{\varepsilon}(t)
   =\int_{-{\infty}}^{+{\infty}} E(t-{\tau})f_{\varepsilon}({\tau})\,
   d{\tau}\\
   &=\int_0^1E(t-{\varepsilon}{\tau})f({\tau})\, d{\tau}
   \to E(t)\int_0^1 f({\tau})\, d{\tau}=E(t)\end{aligned}

og því er eðlilegt að túlka fallið :math:`E` sem svörun sveifilsins við
kraftsviðinu :math:`{\delta}`. Það er greinilegt að :math:`E` uppfyllir
óhliðruðu jöfnuna :math:`mE{{^{\prime\prime}}}+cE{{^{\prime}}}+kE=0`
á menginu :math:`{{\mathbb  R}}\setminus{{\{0\}}}`, en :math:`E` er ekki
tvisvar deildanlegt í punktinum :math:`t=0`, því

.. math::

  \lim_{t\to 0-}E{{^{\prime}}}(t)=0, \qquad
   \lim_{t\to 0+}E{{^{\prime}}}(t)=g{{^{\prime}}}(0)=1/m\neq 0.

Ef við skiptum nú á :math:`u_{\varepsilon}` og og markgildinu :math:`E`
í (:ref:`Link title <2.8.17>`) og á :math:`f_{\varepsilon}` og :math:`{\delta}`, þá
fáum við jöfnuna

.. math:: mE{{^{\prime\prime}}}+cE{{^{\prime}}}+kE={\delta}.

Þessi jafna hefði merkingu ef :math:`{\delta}` væri samfellt fall, en
til þess að gefa henni merkingu verðum við að alhæfa hugtakið afleiða.

.. end-toggle::

Látum nú :math:`f\in C^1({{\mathbb  R}})` og lítum á dreififallið
:math:`u_{f{{^{\prime}}}}`. Það uppfyllir

.. math::

  \begin{aligned}
   u_{f{{^{\prime}}}}({\varphi})&=
   \int_{-{\infty}}^{+{\infty}}
   f{{^{\prime}}}(x){\varphi}(x)\, dx\\
   &=\bigg[f(x){\varphi}(x)\bigg]_{-{\infty}}^{+{\infty}}
   -\int_{-{\infty}}^{+{\infty}} f(x){\varphi}{{^{\prime}}}(x)\, dx\\
   &=-\int_{-{\infty}}^{+{\infty}} f(x){\varphi}{{^{\prime}}}(x)\, dx
   =-u_f({\varphi}{{^{\prime}}}).\end{aligned}

Nú er ljóst að :math:`{\varphi}\mapsto -u_f({\varphi}{{^{\prime}}})`
er línuleg vörpun og að hún skilgreinir dreififall. Ef
:math:`f\in C^k({{\mathbb  R}})`, þá fáum við með ítrekaðri hlutheildun
að

.. math:: u_{f^{(k)}}({\varphi})=(-1)^ku_f({\varphi}^{(k)}).

Þessa formúlu leggjum við til grundvallar á skilgreiningu á afleiðum
dreififalla:

Skilgreining
^^^^^^^^^^^^

Látum :math:`u\in {{\mathbb  D}}{{^{\prime}}}(X)` vera dreififall á
opnu hlutmengi :math:`X` í :math:`{{\mathbb  R}}`. Þá er afleiða þess
:math:`u{{^{\prime}}}` skilgreind sem dreififallið

.. math::

  u{{^{\prime}}}({\varphi})=-u({\varphi}{{^{\prime}}}), \qquad {\varphi}\in
   C_0^{\infty}(X),

og fyrir sérhverja heiltölu :math:`k>0` skilgreinum við :math:`k`-tu
afleiðuna :math:`u^{(k)}` af :math:`u` sem dreififallið

.. math::

  u^{(k)}({\varphi})=(-1)^k u({\varphi}^{(k)}), \qquad {\varphi}\in
   C_0^{\infty}(X).

Ef :math:`u=u_f`, þar sem fallið :math:`f` er heildanlegt á sérhverju
þjöppuðu hlutmengi af :math:`X`, þá nefnist :math:`(u_f){{^{\prime}}}`
*veika afleiðan* af :math:`f` eða *afleiða*
:math:`f`  *í skilningi dreififalla* og við skrifum þá
:math:`f{{^{\prime}}}` í stað :math:`(u_f){{^{\prime}}}`, þegar ekki
er um að villast að átt er við veiku afleiðuna.

--------------

Eins og fram hefur komið, þá er veika :math:`k`-ta afleiðan af
:math:`f\in C^k(X)` ekkert annað en dreififallið sem :math:`f^{(k)}`
skilgreinir, þ.e.a.s.

.. math:: (u_f)^{(k)}=u_{f^{(k)}},

og því getum við litið á afleiður dreififalla sem alhæfingu á afleiðum
venjulegra falla.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Við skulum nú reikna út veiku afleiðuna af Heaviside-fallinu,

.. math::

  \begin{aligned}
   \big(u_H\big){{^{\prime}}}({\varphi})
   &=-\int_{-{\infty}}^{+{\infty}} H(x){\varphi}{{^{\prime}}}(x)\, dx
   =-\int_0^{+{\infty}}{\varphi}{{^{\prime}}}(x)\, dx\\
   &=-\bigg[{\varphi}(x)\bigg]_0^{+{\infty}}={\varphi}(0)={\delta}({\varphi}) \end{aligned}

Niðurstaðan er því formúlan

.. math:: H{{^{\prime}}}={\delta}.

Heaviside-fallið er deildanlegt í venjulegum skilningi og hefur
afleiðuna :math:`H{{^{\prime}}}(x)=0` í sérhverjum punkti
:math:`x\neq 0`. Í punktinum :math:`x=0` er :math:`H` ósamfellt og tekur
stökkið :math:`1` þegar farið er yfir ósamfelluna frá vinstri til hægri,
:math:`H(0+)-H(0-)=1`. Við getum því litið svo á að hallatala :math:`H`
sé :math:`+{\infty}` í þessum eina punkti, en að hún sé :math:`0` alls
staðar annars staðar. Í þessu samhengi er því eðlilegt að túlka
:math:`{\delta}` sem fallið sem uppfyllir :math:`{\delta}(x)=+{\infty}`
ef :math:`x=0` og :math:`{\delta}(x)=0` ef :math:`x\neq 0`.

.. figure:: ./myndir/fig027.svg
    :align: center
    :alt: Heaviside fallið :math:`H_a` og afleiðan :math:`{\delta}_a`

    Mynd: Heaviside fallið :math:`H_a` og afleiðan :math:`{\delta}_a`

Ef við lítum á hliðraða Heaviside-fallið :math:`H_a(x)=H(x-a)`, þá fæst
með sama hætti og hér að ofan að :math:`H{{^{\prime}}}_a={\delta}_a`.
Mjög algengt er að :math:`{\delta}_a` sé táknað með
:math:`{\delta}(x-a)` og þá er einnig algengt að graf :math:`{\delta}_a`
sé táknað með lóðréttri ör eins og sýnt er á myndinni.

.. end-toggle::

Setning
^^^^^^^

Ef :math:`u\in {{\mathbb  D}}{{^{\prime}}}(X)` og
:math:`{\psi}\in C^{\infty}(X)` þá gildir regla Leibniz

.. math:: \big({\psi}u){{^{\prime}}}={\psi}{{^{\prime}}}u+{\psi}u{{^{\prime}}}

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Ef :math:`{\varphi}\in C_0^{\infty}(X)`, þá er

.. math::

  \begin{aligned}
   \big({\psi}u\big){{^{\prime}}}({\varphi})&=-\big({\psi}u)({\varphi}{{^{\prime}}})
   =-u({\psi}{\varphi}{{^{\prime}}})=-u(({\psi}{\varphi}){{^{\prime}}}-{\psi}{{^{\prime}}}{\varphi})\\
   &=u({\psi}{{^{\prime}}}{\varphi})-u(({\psi}{\varphi}){{^{\prime}}})
   =\big({\psi}{{^{\prime}}}u\big)({\varphi})+u{{^{\prime}}}({\psi}{\varphi})\\
   &=\big({\psi}{{^{\prime}}}u\big)({\varphi})+\big({\psi}u{{^{\prime}}}\big)({\varphi})
   =\big({\psi}{{^{\prime}}}u+{\psi}u{{^{\prime}}}\big)({\varphi}).\end{aligned}

.. end-toggle::

Setning
^^^^^^^

Látum :math:`f\in PC^1(X)`, þar sem :math:`X` er opið hlutmengi í
:math:`{{\mathbb  R}}` og gerum ráð fyrir að :math:`f` sé deildanlegt
alls staðar á :math:`X` nema í punktunum :math:`a_1,a_2,\dots,a_N`.
Látum :math:`f{{^{\prime}}}(x)` vera skilgreint sem afleiðuna af
:math:`f` í punktum, þar sem :math:`f` er deildanlegt, og gerum ráð
fyrir að :math:`f{{^{\prime}}}` taki einhver önnur gildi í punktunum
:math:`a_j`. Þá er

.. math::

  \big(u_f\big){{^{\prime}}}= u_{f{{^{\prime}}}}
   + \sum_j \big(f(a_j+)-f(a_j-)\big) {\delta}_{a_j}.

Ef :math:`f\in PC^1(X)\cap C(X)`, þá er

.. math:: \big(u_f\big){{^{\prime}}}= u_{f{{^{\prime}}}}.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Látum :math:`{\varphi}\in C^{\infty}_0(X)` með
:math:`{{\text{supp}\, }}{\varphi}\subset [{\alpha},{\beta}]` og veljum bilið :math:`[{\alpha},{\beta}]` það stórt
að :math:`a_1,\dots,a_N\in [{\alpha},{\beta}]`. Samkvæmt skilgreiningu
er

.. math::

  \big(u_f\big){{^{\prime}}}({\varphi})
   =-u_f({\varphi}{{^{\prime}}})=-\int_{\alpha}^{\beta} f(x){\varphi}{{^{\prime}}}(x)\, dx

Nú þurfum við að framkvæma hlutheildun, en til þess að geta það þurfum
við að skipta :math:`[{\alpha},{\beta}]` í hlutbil, þar sem :math:`f` er
samfellt deildanlegt. Ef við setjum :math:`a_0={\alpha}` og
:math:`a_{N+1}={\beta}`, þá er

.. math::

  \begin{aligned}
   \big(u_f\big){{^{\prime}}}({\varphi})
   &=\sum\limits_{j=0}^N-\int_{a_j}^{a_{j+1}}f(x){\varphi}{{^{\prime}}}(x)\, dx\\
   &=\sum\limits_{j=0}^N
   \bigg(-\bigg[f(x){\varphi}(x)\bigg]_{a_j}^{a_{j+1}}
   +\int_{a_j}^{a_{j+1}}f{{^{\prime}}}(x){\varphi}(x)\, dx\bigg)\\
   &=\sum\limits_{j=0}^N
   \bigg(\big(f(a_j+){\varphi}(a_j)-f(a_{j+1}-){\varphi}(a_{j+1})\big)
   +\int_{a_j}^{a_{j+1}}f{{^{\prime}}}(x){\varphi}(x)\, dx\bigg)\end{aligned}

Nú notfærum við okkur að :math:`{\varphi}(a_0)={\varphi}(a_{N+1})=0` og
fáum

.. math::

  \begin{aligned}
   \big(u_f\big){{^{\prime}}}({\varphi})
   &=\sum\limits_{j=1}^N
   \big(f(a_j+)-f(a_j-)\big){\varphi}(a_j)
   +\int_{{\alpha}}^{{\beta}}f{{^{\prime}}}(x){\varphi}(x)\, dx\\
   &=\sum\limits_{j=1}^N
   \big(f(a_j+)-f(a_j-)\big){\delta}_{a_j}({\varphi})
   +u_{f{{^{\prime}}}}({\varphi}).\end{aligned}

Síðasta staðhæfingin er augljós, því :math:`f(a_j+)-f(a_j-)=0` ef
:math:`f` er samfellt í :math:`a_j`.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Fallið :math:`f(x)=|x|` er samfellt á :math:`{{\mathbb  R}}`, óendanlega
oft samfellt

.. figure:: ./myndir/fig025.svg
    :align: center
    :alt: Formerkisfallið

    Mynd: Formerkisfallið

deildanlegt á :math:`{{\mathbb  R}}\setminus {{\{0\}}}` og hefur
afleiðuna :math:`f{{^{\prime}}}(x)={{\operatorname{sign}}}(x)` ef
:math:`x\neq 0`, þar sem :math:`{{\operatorname{sign}}}` táknar
formerkisfallið

.. math:: {{\operatorname{sign}}}(x)=\begin{cases} 1, &x>0,\\ 0, &x=0,\\ -1, &x<0.\end{cases}

Fallið :math:`{{\operatorname{sign}}}` er því veika afleiðan af
:math:`f`. Nú hefur fallið :math:`{{\operatorname{sign}}}` afleiðuna
:math:`0` á :math:`{{\mathbb  R}}\setminus {{\{0\}}}` og tekur stökkið
:math:`2` í punktinum :math:`0`. Þar með er
:math:`f{{^{\prime\prime}}}=2{\delta}` í merkingu dreififalla.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Látum :math:`{\chi}_{[a,b]}` tákna kennifallið
fyrir lokaða bilið :math:`[a,b]` á :math:`{{\mathbb  R}}`,

.. math::

  {\chi}_{[a,b]}(x)=\begin{cases} 1, &x\in [a,b],\\ 0, &x\notin [a,b].
   \end{cases}

Þetta fall er óendanlega oft samfellt deildanlegt á
:math:`{{\mathbb  R}}\setminus\{a,b\}` með afleiðuna :math:`0` og tekur
stökkið :math:`1` í :math:`x=a` og :math:`-1` í :math:`b`. þar með er
veika afleiðan

.. math:: {\chi}_{[a,b]}{{^{\prime}}}={\delta}_a-{\delta}_b.

.. figure:: ./myndir/fig024.svg
    :align: center
    :alt: Kennifall bilsins :math:`[a,b]`

    Mynd: Kennifall bilsins :math:`[a,b]`

.. end-toggle::



Nú þegar við höfum skilgreint afleiður af dreififöllum, þá getum við
skilgreint afleiðuvirkjann :math:`D^k` sem úthlutar dreififallinu
:math:`u` afleiðunni :math:`u^{(k)}`, :math:`D^ku=u^{(k)}`. Í framhaldi
af því getum við síðan skilgreint línulega afleiðuvirkja

.. math::

  \begin{aligned}
   P(D)u&=\big(a_mD^m+\cdots+a_1D+a_0\big)u \\
   &=a_mu^{(m)}+\cdots+a_1u{{^{\prime}}}+a_0u\nonumber\end{aligned}

og myndað afleiðujöfnur fyrir dreififöll

.. math:: P(D)u=f,

þar sem :math:`f` er gefið dreififall. Stuðlarnir :math:`a_j` geta
staðið fyrir tvinntölur eða jafnvel föll í :math:`C^{\infty}(X)`.
Dreififallalausn er síðan :math:`u\in {{\mathbb  D}}{{^{\prime}}}(X)`
sem uppfyllir jöfnuna.

Skilgreining
^^^^^^^^^^^^

Látum :math:`P(D)` vera afleiðuvirkja með fastastuðla. Dreififall
:math:`u` sem uppfyllir jöfnuna

.. math:: P(D)u={\delta}

nefnist :hover:`grunnlausn` afleiðuvirkjans :math:`P(D)`.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: RLC-rás; framhald

Í sýnidæmi 1.1.2 sáum við að straumurinn :math:`i(t)` í lokaðri
straumrás með viðnámi :math:`R`, spólu með spanstuðul :math:`L` og þétti
með rýmd :math:`C` uppfyllir

.. math:: Li{{^{\prime\prime}}}(t)+Ri{{^{\prime}}}(t)+C^{-1}i(t)=e{{^{\prime}}}(t),

þar sem :math:`e(t)` táknar frumspennu spennugjafans. Ef við hugsum
okkur að :math:`i(t)=e(t)=0` ef :math:`t<0`, að spennan vaxi á örskömmu
tímabili :math:`[0,{\varepsilon}]` frá :math:`0` og upp í :math:`1` og
:math:`e(t)=1` ef :math:`t\geq {\varepsilon}`, þá er :math:`e` mjög
nálægt því að vera Heaviside-fallið.

.. figure:: ./myndir/fig028.svg
    :align: center
    :alt: Vantar titil

    Mynd: Vantar titil

Nú er :math:`H{{^{\prime}}}={\delta}` í veikum skilningi og því má
búast við því að straumurinn :math:`i` sé nálægt því að vera
grunnlausnin

.. math:: Lu{{^{\prime\prime}}}+Ru{{^{\prime}}}+C^{-1}u={\delta}.

.. end-toggle::

Setning
^^^^^^^

Látum :math:`P({\lambda})=a_m{\lambda}^m+\cdots+a_1{\lambda}+a_0` vera
margliðu með tvinntölustuðla og :math:`a_m\neq 0`. Látum :math:`G` tákna
Green-fall virkjans
:math:`P(D)`, :math:`G(t,{\tau})=g(t-{\tau})`, þar sem :math:`g` er
fallið sem uppfyllir :math:`P(D)g=0`,
:math:`g(0)=g{{^{\prime}}}(0)=\cdots=g^{(m-2)}(0)=0` og
:math:`g^{(m-1)}(0)=1/a_m`. Þá er fallið :math:`E=H\cdot g` grunnlausn
virkjans :math:`P(D)`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Fallið :math:`g` er óendanlega oft deildanlegt svo við getum tekið
veikar afleiður af :math:`E` sem margfeldi af :math:`g` og dreififallinu
sem :math:`H` skilgreinir. Til einföldunar skrifum við :math:`E` og
:math:`H` í stað :math:`u_E` og :math:`u_H` og tökum veikar afleiður.
Regla Leibniz og reglan :math:`{\psi}{\delta}={\psi}(0){\delta}` gefa
okkur þá

.. math::

  \begin{aligned}
   E{{^{\prime}}}&=g{{^{\prime}}}H+gH{{^{\prime}}}=g{{^{\prime}}}H+g{\delta}\\
   &=g{{^{\prime}}}H+g(0){\delta}=g{{^{\prime}}}H,\\
   E{{^{\prime\prime}}}&=g{{^{\prime\prime}}}H+g{{^{\prime}}}H{{^{\prime}}}=g{{^{\prime\prime}}}H+g{{^{\prime}}}{\delta}\\
   &=g{{^{\prime\prime}}}H+g{{^{\prime}}}(0){\delta}=g{{^{\prime\prime}}}H,\\
   &\qquad \vdots \qquad\qquad \vdots \qquad\qquad \vdots\\
   E^{(m-1)}&=g^{(m-1)} H+g^{(m-2)} H{{^{\prime}}}=g^{(m-1)} H+g^{(m-2)}{\delta}\\
   &=g^{(m-1)} H+g^{(m-2)}(0){\delta}=g^{(m-1)} H,\\
   E^{(m)}&=g^{(m)} H+g^{(m-1)} H{{^{\prime}}}=g^{(m)} H+g^{(m-1)}{\delta}\\
   &=g^{(m)} H+g^{(m-1)}(0){\delta}=g^{(m)} H+(1/a_m){\delta}.\end{aligned}

Tökum nú saman liðina

.. math::

  \begin{aligned}
   P(D)E&= \big(a_mD^m+a_{m-1}D^{m-1}+\cdots+a_1D+a_0)E\\
   &=a_m((1/a_m){\delta}+g^{(m)}H)
   +a_{m-1}g^{(m-1)}H+\cdots+a_1g{{^{\prime}}}H+a_0gH\\
   &={\delta}+\big(P(D)g\big)H={\delta}.\end{aligned}

.. end-toggle::

Í setningu 2.7.4 voru sett fram fjögur skilyrði, sem einkenna
Green-fallið fyrir jaðargildisverkefnið

.. math:: P(x,D)u=f, \qquad Bu=0.

Með samskonar útreikningum og í sönnuninni á :ref:`Link title <set2.8.17>` fáum við
að skilyrðin (i)-(iii) gefa

.. math:: P(x,D_x)G_B(x,{\xi})={\delta}_{\xi}, \qquad {\xi}\in ]a,b[,

og skilyrðið (iv) gefur síðan að :math:`G_B(x,{\xi})` sem fall af
:math:`x` er lausnin á jaðargildisverkefninu

.. math:: P(x,D)u={\delta}_{\xi}, \qquad Bu=0.

Veik markgildi og :math:`{\delta}`-föll Diracs
----------------------------------------------

Í grein 2.8 sáum við fyrst skilgreiningu og túlkun á Dirac-fallinu
:math:`{\delta}_a`. Það á sér hliðstæða skilgreiningu í hærri víddum.

Skilgreining
^^^^^^^^^^^^

Látum :math:`a\in {{\mathbb  R}}^n` og skilgreinum :math:`{\delta}_a`
með

.. math:: {\delta}_a({\varphi})={\varphi}(a),

þar sem :math:`{\varphi}` er samfellt í einhverri grennd um :math:`a`.
Við getum litið á :math:`{\delta}_a` sem línulega vörpun
:math:`C(X)\to {{\mathbb  C}}` á sérhverju opnu hlutmengi :math:`X` í
:math:`{{\mathbb  R}}^n` sem inniheldur :math:`a`. Vörpunin
:math:`{\delta}_a` nefnist :math:`{\delta}`-*fall Diracs* í punktinum
:math:`a` eða *Dirac-delta-fall* í punktinum :math:`a`. Ef :math:`a=0`,
þá skrifum við aðeins :math:`{\delta}` í stað :math:`{\delta}_0`.

--------------

Dirac-fallið :math:`{\delta}_a` er oft skilgreint í bókum, sem fallið á
:math:`{{\mathbb  R}}^n` sem uppfyllir

.. math::

  {\delta}_a(x)=
   \begin{cases} +{\infty}, &x=a,\\ 0, &x\neq a,\end{cases} \qquad \text{ og } \qquad
   \int_{{{\mathbb  R}}^n}{\delta}_a(x)\, dx=1.

Alveg eins og í einvíða tilfellinu fá þessi skilyrði ekki staðist
stærðfræðilega, því fall sem skilgreint er með fyrri formúlunni hefur
heildi jafnt :math:`0`, sem stangast á við síðara skilyrðið. Þess vegna
er :math:`{\delta}`-fall ekki fall í venjulegum skilningi og við verðum
að notast við skilgreininguna :ref:`Link title <sk18.2.1>`. Hins vegar er gott að
muna eftir skilyrðunum (:ref:`Link title <18.2.2>`) þegar verið er að framkvæma og
túlka útreikninga.

Hugtakið dreififall er skilgreint eins og í einvíða tilfellinu, en áður
en við getum sett skilgreininguna fram þurfum við að innleiða nokkur ný
hugtök. Ef :math:`{\varphi}` er samfellt fall á opnu hlutmengi :math:`X`
í :math:`{{\mathbb  R}}^n`, þá nefnist minnsta lokaða mengi sem
inniheldur :math:`\{x\in X; {\varphi}(x)\neq 0\}` *stoð* fallsins :math:`{\varphi}` og hún er táknuð
með :math:`{{\text{supp}\, }}{\varphi}`. Hlutmengi af
:math:`{{\mathbb  R}}^n` sem er bæði lokað og takmarkað er sagt vera
*þjappað*. Við látum :math:`C_0^k(X)`, þar sem :math:`0\leq k\leq {\infty}`, tákna mengi allra :math:`k` sinnum samfellt deildanlegra
falla á :math:`{{\mathbb  R}}^n` sem hafa þjappaða stoð í :math:`X`.
Þetta er línulegt hlutrúm í :math:`C^k({{\mathbb  R}}^n)`. Rúmið
:math:`C_0^{\infty}(X)` er oft táknað með :math:`{\cal D}(X)` og stök
þess eru oft nefnd *prófunarföll*.

Nú skulum við líta á fall :math:`f` sem er heildanlegt á sérhverju
þjöppuðu hlutmengi af :math:`X`. Það skilgreinir á eðlilegan hátt
línulega vörpun

.. math::

  u_f:C_0^{\infty}(X)\to {{\mathbb  C}}, \qquad
   u_f({\varphi})=\int_Xf(x){\varphi}(x)\, dx.

Athugið að einungis er heildað yfir þjappað hlutmengi af :math:`X`, því
sérhvert fall :math:`{\varphi}` í :math:`C_0^{\infty}(X)` er :math:`0`
alls staðar nema á þjöppuðu hlutmengi. Ef við skilgreinum margfeldið
:math:`f(x){\varphi}(x)` sem :math:`0` fyrir utan
:math:`{{\text{supp}\, }}{\varphi}`, þá breytist heildið ekki þó við
skrifum :math:`\int_{{{\mathbb  R}}^n}` í stað :math:`\int_X`. Nú kemur
skilgreiningin óbreytt frá einvíða tilfellinu:

Skilgreining
^^^^^^^^^^^^

Látum :math:`X` vera opið hlutmengi af :math:`{{\mathbb  R}}^n`. Línuleg
vörpun

.. math:: u:C_0^{\infty}(X)\to {{\mathbb  C}}

nefnist *dreififall* á :math:`X` ef hún er samfelld í þeim skilningi að

.. math:: u({\varphi}_j)\to u({\varphi}), \qquad j\to +{\infty},

fyrir sérhverja runu :math:`{\varphi}_j` í :math:`C_0^{\infty}(X)`, þar
sem föllin :math:`{\varphi}_j` hafa öll stoð í sama þjappaða hlutmenginu
:math:`K` í :math:`X` og um sérhvern hlutafleiðuvirkja
:math:`{\partial}^{\alpha}` gildir að
:math:`{\partial}^{\alpha}{\varphi}_j\to {\partial}^{\alpha}{\varphi}` í
jöfnum mæli á :math:`{{\mathbb  R}}^n`. Mengi allra dreififalla á
:math:`X` táknum við með :math:`{\cal D}'(X)`. Við skrifum einnig
:math:`{{\langle u,\varphi\rangle}}` í staðinn fyrir
:math:`u({\varphi})`.

--------------

Dirac-föll koma oft fyrir sem veik markgildi af föllum, þar sem hugtakið
*veik samleitni* er skilgreint eins og í einni vídd:

Skilgreining
^^^^^^^^^^^^

Látum :math:`u_j` vera runu í :math:`{\cal D}'(X)`. Við segjum að
:math:`u_j` stefni á :math:`u\in {\cal D}'(X)`, og táknum það með
:math:`u_j\to u` og :math:`\lim_{j\to +{\infty}}u_j=u`, ef

.. math::

  \lim_{j\to +{\infty}} u_j({\varphi})=u({\varphi}), \qquad  {\varphi}\in
   C_0^{\infty}(X).

Ef öll dreififöllin :math:`u_j` eru af gerðinni :math:`u_{f_j}`, þar sem
:math:`f_j` er heildanlegt á sérhverju þjöppuðu hlutmengi af :math:`X`,
þá segjum við að :math:`f_j` stefni á :math:`u` *í veikum skilningi* eða
að :math:`f_j` *stefni á* :math:`u`  *í skilningi dreififalla*. Þetta þýðir
að

.. math::

  \int_{{{\mathbb  R}}^n} f_j(x){\varphi}(x)\, dx \to u({\varphi}), 
   \qquad {\varphi}\in C_0^{\infty}(X),

og við táknum þessa samleitni einnig með :math:`f_j\to u` og
:math:`\lim_{j\to+{\infty}} f_j=u`.

--------------

Ef :math:`u_{\varepsilon}` eru dreififöll sem háð eru breytunni
:math:`{\varepsilon}\in {{\mathbb  R}}` þá skilgreinum við
:math:`\lim_{{\varepsilon}\to 0}u_{\varepsilon}` með hliðstæðum hætti. Sama er að segja um
:math:`\lim_{t\to +{\infty}}u_t` ef :math:`u_t` eru dreififöll sem háð
eru samfelldu breytunni :math:`t`.

Setning
^^^^^^^

Ef :math:`f_{\varepsilon}\to {\delta}_0`, þá gildir

.. math::

  \lim\limits_{{\varepsilon}\to 0} f_{\varepsilon}\ast {\varphi}(x)
   ={\varphi}(x), \qquad {\varphi}\in C_0^{\infty}({{\mathbb  R}}^n), \quad x\in {{\mathbb  R}}^n.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við tökum :math:`{\varphi}\in C_0^{\infty}({{\mathbb  R}}^n)` og
skilgreinum :math:`{\psi}_x(y)={\varphi}(x-y)`. Þá gildir

.. math::

  \begin{aligned}
   f_{\varepsilon}\ast {\varphi}(x)
   &=\int_{{{\mathbb  R}}^n}f_{\varepsilon}(x-y){\varphi}(y)\,  dy
   =\int_{{{\mathbb  R}}^n}f_{\varepsilon}(y){\varphi}(x-y)\,  dy \\
   &=\int_{{{\mathbb  R}}^n}f_{\varepsilon}(y){\psi}_x(y)\,  dy 
   \to {\psi}_x(0)={\varphi}(x).\end{aligned}

.. end-toggle::

Auðvelt er að finna föll sem stefna á :math:`{\delta}`-föll í veikum
skilningi:

Setning
^^^^^^^

Látum :math:`f` vera heildanlegt fall á :math:`{{\mathbb  R}}^n` með
heildi jafnt :math:`1` og setjum
:math:`f_{\varepsilon}(x)={\varepsilon}^{-n}f(x/\varepsilon)`. Þá
stefnir :math:`f_{\varepsilon}` á :math:`{\delta}_0` í veikum skilningi
ef :math:`{\varepsilon}\to 0`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Ef :math:`{\varphi}` er takmarkað samfellt fall á
:math:`{{\mathbb  R}}^n`, þá er

.. math::

  \begin{aligned}
   \int_{{{\mathbb  R}}^n}f_{\varepsilon}(x){\varphi}(x)\, dx 
   &=\int_{{{\mathbb  R}}^n}{\varepsilon}^{-n}f(x/{\varepsilon}){\varphi}(x)\, dx 
   =\int_{{{\mathbb  R}}^n}f(y){\varphi}({\varepsilon}y)\, dy\\
   &\to {\varphi}(0)\int_{{{\mathbb  R}}^n}f(y)\, dy={\varphi}(0)={\delta}_0({\varphi}).\end{aligned}

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Varmaleiðnikjarninn

Í grein 16.2 sáum við hvernig varmaleiðnijafnan
:math:`{\partial}_tu-{\kappa}\Delta u=f` er leyst á
:math:`{{\mathbb  R}}^n\times {{\mathbb  R}}_+` með upphafsgildum
:math:`u(x,0)={\varphi}(x)` fyrir :math:`x\in {{\mathbb  R}}^n`. Þar
fengum við að lausnin er gefin með földun
:math:`u(x,t)=E_t\ast {\varphi}+E\ast f`, þar sem :math:`E` táknar
varmaleiðnikjarnann.

.. math::

  E(x,t)=E_t(x)=H(t)
   {\big(4{\pi}{\kappa}t\big)^{-n/2}e^{-x^2/4{\kappa}t}},
   \qquad x\in {{\mathbb  R}}^n,\ (x,t)\neq (0,0).

Við sjáum nú að ef við tökum
:math:`f(x)=\big(4{\pi}\big)^{-n/2}e^{-x^2/4}` og setjum
:math:`{\varepsilon}=\sqrt{{\kappa} t}`, þá gefur setning
:ref:`Link title <set18.2.5>` að

.. math:: E_t\to {\delta}_0, \qquad  t\to 0+.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Poisson-kjarninn á efra hálfplaninu

Annað áhugavert val á föllum sem stefna á :math:`{\delta}`-fallið er
Poisson-kjarninn fyrir efra hálfplanið, sem kom fyrir í
lausnarformúlunni fyrir Dirichlet-verkefnið á efra hálfplaninu í grein
17.4,

.. math::

  P_{\Bbb H_+}(x,y)=\dfrac{y}{\pi(x^2+y^2)}, \qquad (x,y) \in
   {{\mathbb  R}}^2\setminus{{\{(0,0)\}}}.

Ef við setjum nú :math:`f(x)=1/{\pi}(x^2+1)`, þá uppfyllir :math:`f`
skilyrðin í setningu :ref:`Link title <set18.2.5>` og
:math:`f_{\varepsilon}(x)=P_{\Bbb H_+}(x,{\varepsilon})`. Þar með fáum við

.. math:: P_{\Bbb H_+}(\cdot ,y) \to {\delta}_0, \qquad y\to 0+.

.. end-toggle::

Snúum okkur nú að eðlisfræðilegum líkönum, þar sem :math:`{\delta}`-föll
koma fyrir á náttúrulegan hátt:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Massaþéttleiki, þyngdarmætti

Lítum á hlut með massa :math:`M` í þrívíðu rúmi á takmörkuðu svæði
:math:`K` og látum :math:`{\varrho}` vera massaþéttleika hans. Þá er
:math:`{\varrho}(x)=0` ef :math:`x =(x_1,x_2,x_3)\not \in K` og massi
hlutarins er

.. math:: M=\int_K {\varrho}(x)\, dx.

Hugsum okkur nú að :math:`a` sé punktur í :math:`K` og að massinn
skreppi saman þannig að ögn í punkti :math:`x` flyst yfir í punktinn
:math:`y=T_{\varepsilon}(x)= a+{\varepsilon}(x-a)`.

.. figure:: ./myndir/fig1210.svg
    :align: center
    :alt: Vörpunin :math:`T_{\varepsilon}`

    Mynd: Vörpunin :math:`T_{\varepsilon}`

Massaþéttleiki hinnar nýju massadreifingar í
:math:`K_{\varepsilon}=\{y=a+{\varepsilon}(x-a); x\in K\}` er

.. math::

  {\varrho}_{\varepsilon}(y)=
   {\varepsilon}^{-3}{\varrho}(a+(y-a)/{\varepsilon}).

Athugið að stuðullinn :math:`{\varepsilon}^{-3}` er til kominn vegna
þess að vörpunin :math:`T_{\varepsilon}` breytir rúmmáli í hlutfallinu
:math:`{\varepsilon}^3` og andhvefa hennar breytir rúmmáli í hlutfallinu
:math:`{\varepsilon}^{-3}`. Nú fáum við að

.. math::

  \begin{aligned}
   \int_{{{\mathbb  R}}^3}{\varrho}_{\varepsilon}(y)\, dy
   &=\int_{{{\mathbb  R}}^3}{\varepsilon}^{-3} {\varrho}(a+(y-a)/{\varepsilon})\, dy
   =\int_{{{\mathbb  R}}^3}{\varrho}(x)\, dx=M,\\
   \int_{{{\mathbb  R}}^3}{\varrho}_{\varepsilon}(y){\varphi}(y)\, dy
   &=\int_{{{\mathbb  R}}^3}{\varepsilon}^{-3} {\varrho}(a+(y-a)/{\varepsilon})
   {\varphi}(y)\, dy\\
   &=\int_{{{\mathbb  R}}^3}{\varrho}(x){\varphi}(a+{\varepsilon}(x-a))\, dx
   \to {\varphi}(a)\int_{{{\mathbb  R}}^3}{\varrho}(x)\, dx=M{\delta}_a({\varphi}).\end{aligned}

Þessi útreikningur segir okkur að massaþéttleikinn
:math:`{\varrho}_{\varepsilon}` stefni á :math:`M{\delta}_a` í veikum
skilningi. Við túlkum því :math:`{\delta}_a` sem massaþéttleika
einingarpunktmassa í punktinum :math:`a`.

Lítum nú á þyngdarmættið :math:`u_{\varepsilon}` sem massinn skapar í
rúminu. Samkvæmt þyngdarlögmáli Newtons er það gefið með formúlunni

.. math::

  u_{\varepsilon}(x)=- G\int_{K_{\varepsilon}}
   \dfrac{{\varrho}_{\varepsilon}(y)}{4\pi|x-y|}\, dy,

þar sem :math:`G` táknar þyngdarfastann. Við getum skrifað þessa formúlu
sem földunarheildi

.. math:: u_{\varepsilon}(x)=G\big(E\ast {\varrho}_{\varepsilon}\big)(x),

þar sem

.. math:: E(x)=\dfrac {-1}{4{\pi}|x|}, \qquad x\in {{\mathbb  R}}^3\setminus\{(0,0,0)\},

táknar *Newton-mættið*. Ef við látum :math:`{\varepsilon}\to 0`, þá fáum
við

.. math:: u_{\varepsilon}(x)\to \dfrac {-GM}{4{\pi}|x-a|}=GME(x-a).

Við getum því litið á Newton-mættið sem þyngdarmættið, sem punktmassi
:math:`M=1/G` í upphafspunkti skapar í rúminu.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Hleðsluþéttleiki, rafstöðumætti

Nú skulum við líta á fallið :math:`{\varrho}` í síðasta dæmi sem
hleðsluþéttleika í :math:`K` með heildarhleðsluna :math:`Q`. Með
nákvæmlega sömu rökum og áður fáum við þá að
:math:`{\varrho}_{\varepsilon}\to Q{\delta}_a`. Við túlkum því
:math:`{\delta}_a` sem hleðsluþéttleika einingarpunkthleðslu í punktinum
:math:`a`.

Mætti rafstöðusviðsins sem hleðsludreifingin skapar í rúminu er gefin
með

.. math::

  u_{\varepsilon}(x)=\dfrac 1{{\epsilon_0}}\int_{K_{\varepsilon}}
   \dfrac{{\varrho}_{\varepsilon}(y)}{4{\pi}|x-y|}\, dy
   =-\dfrac 1{{\epsilon}_0}E\ast {\varrho}_{\varepsilon}(x),

þar sem :math:`E` táknar Newton-mættið eins og áður og
:math:`{\epsilon}_0` er rafsvörunarstuðullinn í tómarúmi. Ef við látum
:math:`{\varepsilon}\to 0`, þá fáum við

.. math::

  u_{\varepsilon}(x)\to \dfrac Q{{\epsilon}_0}\cdot
   \dfrac 1{4{\pi}|x-a|}=-\dfrac Q{{\epsilon}_0}E(x-a).

Við sjáum því að :math:`E` er rafstöðumættið sem neikvæð hleðsla með
styrk :math:`{\epsilon}_0` í upphafspunkti hnitakerfisins skapar í
rúminu. Í rafstöðufræði kallast :math:`-E(x)=1/4{\pi}|x|`
*Coulomb-mætti*.

.. end-toggle::

Veikar afleiður og grunnlausnir
-------------------------------

Veikar afleiður og grunnlausnir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`f\in C^1({{\mathbb  R}}^n)` og lítum á dreififallið
:math:`u_{{\partial}_jf}`. Með því að hlutheilda með tilliti til
breytistærðarinnar :math:`x_j`, þá fáum við

.. math::

  u_{{\partial}_jf}({\varphi})=
   \int_{{{\mathbb  R}}^n} {\partial}_jf(x){\varphi}(x)\, dx
   =-\int_{{{\mathbb  R}}^n} f(x){\partial}_j{\varphi}(x)\, dx
   =-u_f({\partial}_j{\varphi}).

Nú er ljóst að :math:`{\varphi}\mapsto -u_f({\partial}_j{\varphi})` er
línuleg vörpun og að hún skilgreinir dreififall. Ef
:math:`f\in C^k({{\mathbb  R}}^n)`, þá fáum við með ítrekaðri
hlutheildun að

.. math::

  u_{{\partial}^{\alpha}f}({\varphi})
   =(-1)^{|{\alpha}|}u_f({\partial}^{\alpha}{\varphi}).

Þessa formúlu leggjum við til grundvallar á skilgreiningu á afleiðum
dreififalla:

Skilgreining
^^^^^^^^^^^^

Látum :math:`u` vera dreififall á opnu hlutmengi :math:`X` í
:math:`{{\mathbb  R}}^n`. Þá er hlutafleiða þess :math:`{\partial}_ju`
skilgreind með

.. math::

  {\partial}_ju({\varphi})=-u({\partial}_j{\varphi}), \qquad {\varphi}\in
   C_0^{\infty}(X),

og fyrir sérhvert fjölnúmer :math:`{\alpha}` skilgreinum við afleiðuna
:math:`{\partial}^{\alpha}u` af :math:`u` sem dreififallið

.. math::

  {\partial}^{\alpha}u({\varphi})
   =(-1)^{|{\alpha}|} u({\partial}^{\alpha}{\varphi}), \qquad {\varphi}\in
   C_0^{\infty}(X).

Ef :math:`u=u_f`, þar sem fallið :math:`f` er heildanlegt á sérhverju
þjöppuðu hlutmengi af :math:`X`, þá nefnist
:math:`{\partial}^{\alpha}(u_f)` *veika* :math:`{\alpha}`  *hlutafleiðan*
af :math:`f` eða :math:`{\alpha}` *hlutafleiða* :math:`f`  *í skilningi
dreififalla* og við skrifum þá :math:`{\partial}^{\alpha}f` í stað
:math:`{\partial}^{\alpha}(u_f)`, þegar ekki er um að villast að átt er
við veiku hlutafleiðuna.

--------------

Eins og fram hefur komið, þá er veika :math:`{\alpha}` hlutafleiðan af
:math:`f\in C^k(X)` ekkert annað en dreififallið sem
:math:`{\partial}^{\alpha}f` skilgreinir, þ.e.a.s.

.. math:: {\partial}^{\alpha}(u_f)=u_{{\partial}^{\alpha}f},

og því getum við litið á hlutafleiður dreififalla sem alhæfingu á
afleiðum venjulegra falla.

Við skilgreinum síðan hlutafleiðuvirkjann :math:`{\partial}^{\alpha}`,
en hann úthlutar dreififallinu :math:`u` hlutafleiðunni
:math:`{\partial}^{\alpha}u`. Í framhaldi af því getum við síðan
skilgreint línulega hlutafleiðuvirkja

.. math::

  P({\partial})= \sum\limits_{|{\alpha}|\leq m} 
   a_{\alpha}{\partial}^{\alpha}

og myndað afleiðujöfnur fyrir dreififöll

.. math:: P({\partial})u=f,

þar sem :math:`f` er gefið dreififall. Stuðlarnir :math:`a_{\alpha}`
geta staðið fyrir tvinntölur eða jafnvel föll í :math:`C^{\infty}(X)`.
*Dreififallalausn* eða *veik lausn* er síðan :math:`u\in {\cal D}'(X)`
sem uppfyllir jöfnuna.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Veikar lausnir bylgjujöfnunnar

Í grein 15.2 sáum við að lausn á bylgjujöfnunni
:math:`{\partial}_t^2-c^2{\partial}_x^2u=0` á :math:`{{\mathbb  R}}^2`
er af gerðinni

.. math:: u(x,t)=f(x+ct)+g(x-ct)

og til þess að staðfesta að þetta sé lausn þá þarf að gera ráð fyrir að
föllin :math:`f` og :math:`g` séu tvisvar samfellt deildanleg. Það kemur
í ljós að bylgjujafnan er uppfyllt í veikum skilningi fyrir :math:`u` af
gerðinni (:ref:`Link title <18.3.5>`), ef við gerum einungis ráð fyrir að föllin
:math:`f` og :math:`g` séu heildanleg á takmörkuðum bilum. Við skulum nú
staðfesta að þetta sé rétt.

Veika afleiðan af :math:`u` er gefin með

.. math::

  \begin{gathered}
   {{\langle \big(\partial_t^2-c^2\partial_x^2\big)u,\varphi\rangle}}
   ={{\langle u,\big(\partial_t^2-c^2\partial_x^2\big)\varphi\rangle}}\\
   =\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}
   \big(f(x+ct)+g(x-ct)\big)
   \big(\partial_t^2-c^2\partial_x^2\big)\varphi(x,t)\, dx dt,\end{gathered}

þar sem :math:`\varphi\in C_0^\infty({{\mathbb  R}}^2)`. Nú skiptum við
yfir í kennihnit eins og í (:ref:`Link title <15.2.4>`) og (:ref:`Link title <15.2.5>`) og setjum
:math:`\psi(\xi,\eta)=\varphi(x,t)`. Þá er
:math:`\big(\partial_t^2-c^2\partial_x^2\big)\varphi(x,t)= -4c^2\partial_\xi\partial_\eta\psi(\xi,\eta)` samkvæmt (:ref:`Link title <15.2.6>`).
Jacobi-ákveða hnitaskiptanna :math:`(\xi,\eta)\mapsto (x,t)` er
:math:`-1/2c` og þar með er

.. math::

  \begin{aligned}
   {{\langle \big(\partial_t^2-c^2\partial_x^2\big)u,\varphi\rangle}}
   &=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}
   \big(f(\xi)+g(\eta)\big)
   \big(-4c^2\partial_\xi\partial_\eta\psi(\xi,\eta)\big)\, 
   \dfrac 1{2c} \, d\xi d\eta\\
   &=-2c\int_{-\infty}^{+\infty}f(\xi)\int_{-\infty}^{+\infty}
   \partial_\eta\partial_\xi\psi(\xi,\eta)\, d\eta\, d\xi\\
   &-2c\int_{-\infty}^{+\infty}g(\eta)\int_{-\infty}^{+\infty}
   \partial_\xi\partial_\eta\psi(\xi,\eta)\, d\xi\, d\eta=0.\end{aligned}

Athugið að hér höfum við notfært okkur að :math:`\psi` er :math:`0`
fyrir utan takmarkað mengi og því er

.. math::

  \begin{gathered}
   \int_{-\infty}^{+\infty}
   \partial_\eta\partial_\xi\psi(\xi,\eta)\, d\eta=
   \bigg[\partial_\xi\psi(\xi,\eta)\bigg]_{\eta\to -\infty}^{\eta\to
   +\infty}=0,\\
   \int_{-\infty}^{+\infty}
   \partial_\xi\partial_\eta\psi(\xi,\eta)\, d{\xi}=
   \bigg[\partial_\eta\psi(\xi,\eta)\bigg]_{\xi\to -\infty}^{\xi\to
   +\infty}=0.\end{gathered}

Á mynd 15.1 er útbreiðslu bylgju lýst. Það eru brot í ferlinum, en það
kemur ekki að sök, því við tökum lausn í veikum skilningi.

.. end-toggle::

Skilgreining
^^^^^^^^^^^^

Látum :math:`P({\partial})` vera afleiðuvirkja með fastastuðla.
Dreififall :math:`E` sem uppfyllir jöfnuna

.. math:: P({\partial})E={\delta}

nefnist *grunnlausn* afleiðuvirkjans :math:`P({\partial})`.

--------------

Grunnlausnir hlutafleiðuvirkja eru mjög mikilvægar vegna þess að með
þeim er hægt að ákvarða sérlausnir. Til þess að sjá það skulum við
athuga að ef :math:`{\varphi}\in C_0^{\infty}({{\mathbb  R}}^n)`, þá er

.. math::

  {\partial}^{\alpha} u({\varphi})
   ={{\langle {\partial}^{\alpha}u,\varphi\rangle}}
   =(-1)^{|{\alpha}|}{{\langle u,{\partial}^{\alpha}{\varphi}\rangle}}
   ={{\langle u,(-{\partial})^{\alpha}{\varphi}\rangle}}

og þar með er

.. math::

  {{\langle P({\partial})u,\varphi\rangle}}
   ={{\langle \sum a_{\alpha} {\partial}^{\alpha}u,\varphi\rangle}}
   ={{\langle u,\sum a_{\alpha} \big(-{\partial}\big)^{\alpha}{\varphi}\rangle}}
   ={{\langle u,P(-{\partial}){\varphi}\rangle}}.

Athugum nú að fyrir fall :math:`F`, sem er heildanlegt á þjöppuðum
hlutmengjum í :math:`{{\mathbb  R}}^n` er földunin
:math:`F\ast {\varphi}` vel skilgreind ef :math:`{\varphi}\in C_0^{\infty}({{\mathbb  R}}^n)` með formúlunni

.. math:: F\ast {\varphi}(x)=\int_{{{\mathbb  R}}^n} F(y){\varphi}(x-y)\, dy

og greinilegt er að
:math:`F\ast {\varphi}\in C^{\infty}({{\mathbb  R}}^n)`, því við megum
taka afleiður með tilliti til :math:`x` undir heildið. Við fáum þá

.. math::

  \begin{aligned}
   P({\partial}) \, F\ast {\varphi}(x)
   &=\int_{{{\mathbb  R}}^n} F(y) P({\partial}_x){\varphi}(x-y)\, dy\\
   &=\int_{{{\mathbb  R}}^n} F(y) P(-{\partial}_y){\varphi}(x-y)\, dy\\
   &={{\langle u_F,P(-{\partial}){\varphi}(x-\cdot)\rangle}}\\
   &={{\langle P({\partial})u_F,{\varphi}(x-\cdot)\rangle}}.\end{aligned}

Hér táknar :math:`P(-{\partial}){\varphi}(x-\cdot)` að
hlutafleiðuvirkinn :math:`P(-{\partial})` er látinn verka á
:math:`{\varphi}(x-y)` með tilliti til :math:`y`. Ef dreififallið
:math:`E=u_F` er grunnlausn hlutafleiðuvirkjans :math:`P({\partial})`,
þá fáum við

.. math::

  P({\partial}) \, F\ast {\varphi}(x)
   ={{\langle P({\partial})u_F,{\varphi}(x-\cdot)\rangle}}
   ={{\langle \delta,{\varphi}(x-\cdot)\rangle}}={\varphi}(x).

Þar með er :math:`u=F\ast {\varphi}` lausn á hliðruðu jöfnunni
:math:`P({\partial})u={\varphi}`.

Skilgreining
^^^^^^^^^^^^

Ef :math:`u\in {\cal D}'({{\mathbb  R}}^n)` og
:math:`{\varphi}\in C_0^{\infty}({{\mathbb  R}}^n)`, þá skilgreinum við
földun :math:`u` og :math:`{\varphi}` með formúlunni

.. math:: u\ast {\varphi}(x)=u({\varphi}(x-\cdot))={{\langle u,{\varphi}(x-\cdot)\rangle}}.

--------------

Það er ekki erfitt að sýna fram á að
:math:`u\ast {\varphi}\in C^{\infty}({{\mathbb  R}}^n)`. Ef
:math:`E\in {\cal D}'({{\mathbb  R}}^n)` er grunnlausn
hlutafleiðuvirkjans :math:`P({\partial})`, þá er
:math:`u=E\ast {\varphi}` sérlausn jöfnunnar
:math:`P({\partial})u={\varphi}`. Þegar eiginleikar grunnlausnarinnar
:math:`E` eru þekktir þá er oft hægt að skipta á fallinu
:math:`{\varphi}` og falli :math:`f` sem er ekki eins oft deildanlegt og
:math:`{\varphi}` og jafnvel ekki með þjappaða stoð, þannig að
:math:`u=E\ast f` sé vel skilgreind lausn á :math:`P({\partial})u=f`.

Grunnlausn bylgjuvirkjans
-------------------------

Í setningu 15.5.1 er að finna lausn einvíðu bylgjujöfnunnar
:math:`{\partial}_t^2-c^2{\partial}_x^2u=f` með upphafsskilyrðum
:math:`u(x,0)={\varphi}(x)` og :math:`{\partial}_tu(x,0)={\psi}(x)`. Hún
er gefin með d’Alembert-formúlunni

.. math::

  u(x,t)={\partial}_t\big(E_t\ast {\varphi}\big)(x)+
   E_t\ast {\psi}(x)+E\ast f(x,t),

þar sem fallið :math:`E` er gefið með

.. math::

  E(x,t)=\dfrac 1{2c} H(ct-x)H(ct+x)=
   \begin{cases} 1/2c, &|x|\leq ct,\\ 0, &|x|>ct.\end{cases}

Þetta fall reynist vera grunnlausn bylgjuvirkjans. Til þess að staðfesta
það, þurfum við að sýna að

.. math::

  {{\langle \big(\partial_t^2-c^2\partial_x^2\big)E,\varphi\rangle}}
   ={{\langle E,\big(\partial_t^2-c^2\partial_x^2\big)\varphi\rangle}}=\varphi(0,0),
   \qquad \varphi\in C_0^\infty({{\mathbb  R}}^2).

Við notum nú sama rithátt og í grein 15.2, skiptum yfir í kennihnit og
fáum þá á sama hátt og í sýnidæmi 18.3.2

.. math::

  \begin{aligned}
   {{\langle \big(\partial_t^2-c^2\partial_x^2\big)E,\varphi\rangle}}
   &=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}
   \dfrac 1{2c}H(ct-x)H(ct+x)
   \big(\partial_t^2-c^2\partial_x^2\big)\varphi(x,t)\, dxdt\\
   &=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}
   \dfrac
   1{2c}H(-\eta)H(\xi)(-4c^2\partial_\xi\partial_\eta\psi(\xi,\eta))
   \dfrac 1{2c}\, d\xi d\eta\\
   &=-\int_{-\infty}^{0}\bigg(\int_{0}^{+\infty}
   \partial_\xi\partial_\eta\psi(\xi,\eta)\, d\xi\bigg)\, d\eta\\
   &=\int_{-\infty}^{0} \partial_\eta\psi(0,\eta)\, d\eta=\psi(0,0)=\varphi(0,0).\end{aligned}

Grunnlausn varmaleiðnivirkjans
------------------------------

Varmaleiðnikjarninn :math:`E` reynist vera grunnlausn
varmaleiðnijöfnunnar. Við skulum sýna fram á það í tilfellinu
:math:`n=1`. Tilfellið :math:`n>1` gengur nánast eins fyrir sig. Til
þess þurfum við að sýna að

.. math::

  {{\langle \big(\partial_t-\kappa\partial_x^2\big) E,\varphi\rangle}}
   ={{\langle E,\big(-\partial_t-\kappa\partial_x^2\big)
   \varphi\rangle}}=\varphi(0,0), \qquad \varphi\in C_0^\infty({{\mathbb  R}}^2).

Við athugum að :math:`E(x,t)=0` ef :math:`t<0`, svo

.. math::

  {{\langle \big(\partial_t-\kappa\partial_x^2\big) E,\varphi\rangle}}
   =\lim_{\varepsilon\to 0+}
   \int_\varepsilon^{+\infty}
   \int_{-\infty}^{+\infty}
   E(x,t)\big(-\partial_t\varphi(x,t)-\kappa\partial_x^2\varphi(x,t)\big) 
   \, dxdt.

Ef :math:`x` er haldið föstu og heildað er með tilliti til :math:`t`, þá
fæst

.. math::

  \int_\varepsilon^{+\infty}E(x,t)\big(-\partial_t\varphi(x,t)\big)\, dt
   =-\bigg[ E(x,t)\varphi(x,t) \bigg]_\varepsilon^{+\infty}
   +\int_\varepsilon^{+\infty}\partial_tE(x,t)\varphi(x,t)\, dt.

Nú skulum við halda :math:`t` föstu og hlutheilda með tilliti til
:math:`x` tvisvar sinnum. Fyrst :math:`\varphi=0` fyrir utan takmarkað
mengi, þá er

.. math::

  \int_{-\infty}^{+\infty} E(x,t) \partial_x^2\varphi(x,t)\, dx
   =\int_{-\infty}^{+\infty} \partial_x^2 E(x,t) \varphi(x,t)\, dx.

Nú notfærum við okkur (:ref:`Link title <18.5.3>`) og (:ref:`Link title <18.5.4>`) í
(:ref:`Link title <18.5.2>`) og fáum þá

.. math::

  \begin{aligned}
    {{\langle \big(\partial_t-\kappa\partial_x^2\big) E,\varphi\rangle}}
   &=\lim_{\varepsilon\to 0+}\bigg(
   \int_{-\infty}^{+\infty} E(x,\varepsilon) 
   \varphi(x,\varepsilon)\, dx\\
   &+\int_\varepsilon^{+\infty}
   \int_{-\infty}^{+\infty}
   \big(\partial_t-\kappa\partial_x^2\big) 
   E(x,t)\varphi(x,t) \, dxdt \bigg)\\
   &=\lim_{\varepsilon\to 0+}\bigg(
   \int_{-\infty}^{+\infty} 
   \dfrac 1{\sqrt{4\pi\kappa\varepsilon}}e^{-x^2/4\kappa\varepsilon}
   \varphi(x,\varepsilon)\, dx\bigg).\end{aligned}

Hér höfum við notfært okkur að :math:`E` er lausn á varmaleiðnijöfnunni
ef :math:`t>0`. Nú skiptum við um breytistærð og fáum að lokum

.. math::

  {{\langle \big(\partial_t-\kappa\partial_x^2\big) E,\varphi\rangle}}
   =\lim_{\varepsilon\to 0+}\int_{-{\infty}}^{+{\infty}}
   \dfrac 1{\sqrt{\pi}}e^{-y^2}
   \varphi(\sqrt{4\kappa\varepsilon}\, y,\varepsilon)\, dy
   =\varphi(0,0).

Grunnlausn Laplace-virkjans
---------------------------

Grunnlausn Laplace-virkjans
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú snúum við okkur að Laplace-virkjanum. Í útreikningum okkar á
Green-föllum í grein 17.7, gegndi fallið :math:`E`, sem skilgreint er
með

.. math::

  E(x)=\begin{cases} \dfrac 1{2{\pi}} \ln |x|,  & x\in {{\mathbb  R}}^n\setminus{{\{0\}}}, \ n=2,\\
   \dfrac {-1}{4{\pi}|x|},  & x\in {{\mathbb  R}}^n\setminus {{\{0\}}}, \ n=3,
   \end{cases}

lykilhlutverki. Það reynist vera grunnlausn Laplace-virkjans. Við byrjum
á tilfellinu :math:`n=2`. Athugum að formúlan yfir Laplace-virkjann í
pólhnitum í viðauka D gefur að fyrir föll :math:`v` af gerðinni
:math:`v(x_1,x_2)=g(r)` er

.. math::

  \Delta v=
   \dfrac 1{r^2}\bigg(r\partial_r\big(r\partial_r\big)
   +\partial_\theta^2 \bigg)g(r) =\dfrac 1r \big(rg{{^{\prime}}}(r)\big){{^{\prime}}},

svo það er greinilegt að :math:`\Delta E=0` á
:math:`{{\mathbb  R}}^2\setminus\{(0,0)\}`. Til þess að staðfesta að
:math:`E` sé grunnlausn, þá þurfum við að sanna að

.. math::

  {{\langle \Delta E,\varphi\rangle}}={{\langle E,\Delta\varphi\rangle}}=\delta(\varphi)=
   \varphi(0,0), \qquad \varphi\in C_0^\infty({{\mathbb  R}}^2).

Við snúum þessari formúlu yfir í pólhnit og setjum
:math:`\psi(r,\theta)=\varphi(r\cos \theta,r\sin \theta)`. Þá fáum við
að

.. math::

  {{\langle \Delta E,\varphi\rangle}}={{\langle E,\Delta\varphi\rangle}}
   =\dfrac 1{2\pi}\int_0^{2\pi}\int_0^{\infty}
   \ln r\bigg[\dfrac 1r\partial_r\big(r\partial_r\psi\big)
   +\dfrac 1{r^2}\partial_\theta^2\psi
   \bigg] r\, drd\theta.

Fallið :math:`\psi` er :math:`2\pi`-lotubundið í :math:`{\theta}` og
því er heildið af seinni liðnum :math:`0`. Við höfum einnig að
:math:`\psi(r,\theta)=0`, ef :math:`r` er nógu stórt, og því fáum við
með hlutheildun

.. math::

  \begin{aligned}
   {{\langle E,\Delta \varphi\rangle}}&=
   \dfrac 1{2\pi}\int_0^{2\pi}\int_0^{\infty}
   \big(\ln r\big) \partial_r\big(r\partial_r\psi\big) \, dr d\theta\\
   &=\dfrac 1{2\pi}\int_0^{2\pi}\bigg(
   \bigg[ \big(\ln r\big) r\partial_r\psi\bigg]_0^\infty
   -\int_0^\infty \partial_r\psi\, dr
   \bigg) d\theta\\
   &=\dfrac 1{2\pi}\int_0^{2\pi}\psi(0,\theta)\, d\theta
   =\varphi(0,0)\dfrac 1{2\pi}\int_0^{2\pi}\, d\theta = \varphi(0,0).\end{aligned}

Í tilfellinu :math:`n=3` er :math:`E` gefið með formúlunni

.. math::

  E(x)=\dfrac{-1}{4\pi r}, \qquad r=|x|,
   \quad x\in {{\mathbb  R}}^3\setminus{{\{0\}}}.

Til þess að sýna fram á að þetta sé grunnlausn, þá snúum við yfir í
kúluhnit og setjum :math:`\psi(r,\theta,\phi)= \varphi(r\sin\theta\cos\phi,r\sin\theta\sin\phi,r\cos\theta)`.
Laplace-virkinn í kúluhnitum er gefinn í viðauka D. Þar með er

.. math::

  \begin{gathered}
   {{\langle E,\Delta \varphi\rangle}}
   =\dfrac {-1}{4\pi}\int_0^\infty\int_0^\pi\int_0^{2\pi}\\
   \dfrac 1r\bigg[
   \dfrac 1{r^2}\partial_r\big(r^2\partial_r\psi\big)
   +\dfrac 1{r^2\sin \theta} 
   \partial_\theta\big(\sin \theta\partial_\theta\psi\big)
   +\dfrac 1{r^2\sin^2\theta}\partial_\phi^2\psi
   \bigg] r^2\sin\theta\, dr d\theta d\phi.\end{gathered}

Nú er :math:`\psi` :math:`2\pi`-lotubundið sem fall af :math:`\phi` og
því er heildið af síðasta liðnum :math:`0`. Við höfum einnig að

.. math::

  \int_0^\pi\dfrac 1{r^2\sin\theta} 
   \partial_\theta\big(\sin
   \theta\partial_\theta\psi\big)r^2\sin\theta\, d\theta =
   \bigg[\sin \theta\partial_\theta\psi\bigg]_0^\pi=0.

Eftir stendur því

.. math::

  \begin{aligned}
   {{\langle \Delta E,\varphi\rangle}} 
   &= -\dfrac 1{4\pi}
   \int_0^\infty\int_0^\pi\int_0^{2\pi}
   \dfrac 1r \partial_r\big(r^2\partial_r\psi\big)
   \sin\theta\, dr d\theta d\phi\\
   &= -\dfrac 1{4\pi}
   \int_0^\pi\int_0^{2\pi}
   \bigg(
   \bigg[\dfrac 1r r^2\partial_r\psi\bigg]_0^\infty
   +\int_0^\infty \partial_r\psi \, dr
   \bigg) \sin\theta\, d\theta d\phi\\
   &= \dfrac 1{4\pi}
   \int_0^\pi\int_0^{2\pi}
   \psi(0,\theta,\phi) \, \sin\theta\, d\theta d\phi=\varphi(0).\end{aligned}

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Hleðsluþéttleiki á línu og grunnlausn Laplace-virkjans

Í sýnidæmi 18.2.9 sáum við að Coulomb-mættið er rafmætti sem hleðsla
:math:`Q={\epsilon}_0` í upphafspunktinum skapar í rúminu
:math:`{{\mathbb  R}}^3`. Hugsum okkur nú jafna hleðsludreifingu
:math:`{\varrho}_\ell` [:math:`C/m`] á línu :math:`\ell` í þrívíðu rúmi
og veljum hnitakerfið þannig að línan fari gegnum punktinn
:math:`({\xi},{\eta})` í planinu :math:`{{\mathbb  R}}^2` og standi
hornrétt á það. Með svipuðum rökum og í sýnidæmi 18.2.9 getum við sýnt
fram á að þessi hleðsludreifing sé veikt markgildi af samfelldri
hleðsludreifingu í sívalningi :math:`S_r` með geislann :math:`r`
umhverfis línuna :math:`\ell`, sem skreppur saman í hleðsludreifingu á
línunni ef :math:`r\to 0+`. Við fáum þá að hleðsluþéttleikinn er
dreififallið :math:`{\varrho}_\ell {\delta}_{\zeta}` og að rafmættið er
lausn á tvívíðu Laplace-jöfnunni

.. math:: \Delta  V=-({\varrho}_\ell/\epsilon_0){\delta}_{\zeta}.

Mættið er þar með gefið með

.. math::

  V(z)=\dfrac{-{\varrho}_\ell}{\epsilon_0}E(z-{\zeta})
   =\dfrac{-{\varrho}_\ell}{2{\pi}\epsilon_0} \ln|z-{\zeta}|,

þar sem
:math:`z=x+iy, {\zeta}={\xi}+i{\eta}\in {{\mathbb  R}}^2={{\mathbb  C}}`.
Grunnlausnin :math:`E(z)=\big(\ln|z|\big)/2{\pi}` er því sjálf
rafstöðumættið sem línuhleðslan af styrk :math:`-\epsilon_0` á línunni
gegnum :math:`{\zeta}=0` skapar í rúminu.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Green-föll í rafstöðufræði

Látum :math:`X` vera takmarkað svæði í þrívíðu rúmi og gerum ráð fyrir
að jaðar þess sé úr leiðandi efni. Ef punkthleðsla :math:`Q` er staðsett
í punktinum :math:`{\xi}` í :math:`X` þá skapast rafmætti :math:`u` í
svæðinu :math:`X` sem uppfyllir
:math:`-{\epsilon}\Delta u=Q{\delta}_{\xi}`, því hleðsluþéttleikinn er
:math:`Q{\delta}_{\xi}`, og :math:`u` er núll á jaðrinum. Ef við gefum
okkur að til sé Green-fall á svæðinu :math:`X`, þá uppfyllir fallið

.. math:: x\mapsto v(x)=G(x,{\xi})=E(x-{\xi})+w_X(x,{\xi})

jöfnuna :math:`\Delta v={\delta}_{\xi}` og :math:`v` er núll á jaðrinum. Þar með segir
ótvíræðnisetningin fyrir Dirichlet-verkefnið að

.. math:: u(x)=-\dfrac Q\epsilon G(x,{\xi}), \qquad x\in X.

.. end-toggle::

Fourier-ummyndun af dreififöllum og grunnlausnir
------------------------------------------------

Fourier-ummyndun af dreififöllum og grunnlausnir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við ætlum nú að reifa mjög lauslega hvernig Fourier-ummyndun
er alhæfð yfir á dreififöll. Við skulum byrja á því
að taka :math:`f\in L^1({{\mathbb  R}})` og
:math:`{\varphi}\in C_0^{\infty}({{\mathbb  R}})`. Þá segir reikniregla
(xii) að

.. math::

  u_{\widehat f}({\varphi})=\int_{-{\infty}}^{+{\infty}} 
   \widehat f(x){\varphi}(x) \, dx
   =\int_{-{\infty}}^{+{\infty}} 
   f(x)\widehat {\varphi}(x) \, dx =u_f(\widehat {\varphi}).

Út frá þessari formúlu gæti maður í fljótheitum ályktað að hægt sé að
skilgreina Fourier-mynd :math:`\widehat u` af hvaða dreififalli
:math:`u\in {{\mathbb  D}}{{^{\prime}}}({{\mathbb  R}})` sem er með
formúlunni :math:`\widehat u({\varphi})=u(\widehat {\varphi})`. Það er
rangt, því :math:`\widehat {\varphi}\notin C_0^{\infty}({{\mathbb  R}})`
og þar með er :math:`u(\widehat {\varphi})` ekki skilgreint. Við
skilgreinum nú nýtt fallarúm sem inniheldur
:math:`C_0^{\infty}({{\mathbb  R}})`:

Skilgreining
^^^^^^^^^^^^

Rúm allra falla :math:`{\varphi}\in C^{\infty}({{\mathbb  R}})`, sem
uppfylla

.. math::

  \max\limits_{x\in {{\mathbb  R}}} |x^{\mu}{\varphi}^{({\nu})}(x)|<+{\infty}, 
   \qquad {\mu},{\nu}=0,1,2,\dots,

nefnist *fallarúm Schwartz* eða *Schwartz-fallarúmið*. Við táknum það
með :math:`{{\cal S}}({{\mathbb  R}})`.

--------------

Athugið að
:math:`C_0^{\infty}({{\mathbb  R}})\subset {{\cal S}}({{\mathbb  R}})`
og að skilyrðið (:ref:`Link title <6.9.2>`) segir að sérhver afleiða af falli í
:math:`{{\cal S}}({{\mathbb  R}})` stefni hraðar á :math:`0` í
:math:`\pm {\infty}` en hvaða neikvætt veldi af :math:`x` sem er. Dæmi um fall
:math:`{\varphi}\in {{\cal S}}({{\mathbb  R}})\setminus C_0^{\infty}({{\mathbb  R}})`
er :math:`{\varphi}(x)=e^{-x^2}`.

Skilgreining
^^^^^^^^^^^^

Línuleg vörpun :math:`u:{{\cal S}}({{\mathbb  R}}) \to {{\mathbb  C}}`,
nefnist *Schwartz-dreififall* , ef hún er samfelld í þeim skilningi að

.. math:: u({\varphi}_j)\to u({\varphi}), \qquad j\to +{\infty},

þar sem :math:`{\varphi}_j\to {\varphi}` í
:math:`{{\cal S}}({{\mathbb  R}})`, en með því er átt við að

.. math::

  \max\limits_{x\in {{\mathbb  R}}} |x^{\mu}({\varphi}_j^{({\nu})}(x)-{\varphi}^{({\nu})}(x))|\to 0,
   \qquad j\to +{\infty},

fyrir öll :math:`{\mu},{\nu}=0,1,2,\dots`. Rúm allra
Schwartz-dreififalla nefnum við *dreififallrúm Schwartz* eða
*Schwartz-dreififallarúmið* og við táknum það með
:math:`{{\cal S}}{{^{\prime}}}({{\mathbb  R}})`.

--------------

Sérhvert stak í :math:`{{\cal S}}{{^{\prime}}}({{\mathbb  R}})`
skilgreinir sjálfkrafa stak í
:math:`{{\mathbb  D}}{{^{\prime}}}({{\mathbb  R}})` og því getum við
litið á :math:`{{\cal S}}{{^{\prime}}}({{\mathbb  R}})` sem hlutrúm í
:math:`{{\mathbb  D}}{{^{\prime}}}({{\mathbb  R}})`. Reiknireglurnar
\(ix) og (x) segja okkur að Fourier-ummyndunin sé gagntæk vörpun á
:math:`{{\cal S}}({{\mathbb  R}})` og jafnframt að
:math:`\widehat {\varphi}_j\to \widehat {\varphi}` í
:math:`{{\cal S}}({{\mathbb  R}})` ef :math:`{\varphi}_j\to {\varphi}` í
:math:`{{\cal S}}({{\mathbb  R}})`. Þess vegna fæst eðlileg alhæfing á
Fourier-ummyndun frá :math:`L^1({{\mathbb  R}})` yfir á
:math:`{{\cal S}}{{^{\prime}}}({{\mathbb  R}})`:

Skilgreining
^^^^^^^^^^^^

Ef :math:`u\in {{\cal S}}{{^{\prime}}}({{\mathbb  R}})`, þá
skilgreinum við Fourier-myndina
:math:`\widehat u={{\cal F}}u\in {{\cal S}}{{^{\prime}}}({{\mathbb  R}})`
með formúlunni

.. math:: \widehat u({\varphi}) = u(\widehat {\varphi}).

--------------

Það er ljóst að sérhvert fall :math:`f\in L^1({{\mathbb  R}})`
skilgreinir Schwartz-dreififall,
:math:`u_f\in {{\cal S}}{{^{\prime}}}({{\mathbb  R}})`, og að
(:ref:`Link title <6.9.5>`) er alhæfing á (:ref:`Link title <6.9.1>`).

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Dirac-fallið :math:`{\delta}_a` er greinilega í
:math:`{{\cal S}}{{^{\prime}}}({{\mathbb  R}})` og

.. math::

  \widehat {\delta}_a({\varphi})= \widehat {\varphi}(a)=
   \int_{-{\infty}}^{+{\infty}} e^{-ixa} {\varphi}(x)\, dx.

Þar með er :math:`\widehat {\delta}_a` gefið sem :math:`u_f` með
:math:`f({\xi})=e^{-ia{\xi}}`. Við skrifum því

.. math:: \widehat {\delta}_a({\xi})=e^{-ia{\xi}}.

Við getum einnig litið svo á að hér hafi :math:`{\delta}`-fallið í
punktinum :math:`a` verkað á fallið :math:`x\mapsto e^{-ix{\xi}}`, en
samkvæmt skilgreiningu úthlutar :math:`{\delta}_a` fallinu
:math:`{\varphi}` gildi sínu :math:`{\varphi}(a)` í punktinum :math:`a`.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum nú á dreififallið
:math:`u_f\in {{\cal S}}{{^{\prime}}}({{\mathbb  R}})` með
:math:`f(x)=\cos x`,

.. math:: u_f({\varphi})=\int_{-{\infty}}^{+{\infty}} \cos x \, {\varphi}(x)\, dx.

Við notum nú andhverfuformúlu Fouriers og fáum

.. math::

  \begin{aligned}
   \widehat u_f({\varphi})&=u_f(\widehat {\varphi})=
   \int_{-{\infty}}^{+{\infty}} \cos x \, \widehat {\varphi}(x)\, dx\\
   &=\tfrac 12 \int_{-{\infty}}^{+{\infty}} 
   e^{ix} \widehat {\varphi}(x)\, dx+
   \tfrac 12 \int_{-{\infty}}^{+{\infty}} 
   e^{-ix} \widehat {\varphi}(x)\, dx\\
   &={\pi}\big({\varphi}(1)+{\varphi}(-1)\big)
   ={\pi}\big({\delta}_1({\varphi})+{\delta}_{-1}({\varphi})\big).\end{aligned}

Formúlan verður því

.. math:: \widehat{ \cos} = {\pi}\big({\delta}_1+{\delta}_{-1}\big).

.. end-toggle::

Reiknireglurnar (ix) og (x) eru óbreyttar fyrir Fourier-myndir
Schwartz-dreififalla, því

.. math::

  {{\cal F}}\{u{{^{\prime}}}\}=i{\xi}{{\cal F}}u, \qquad
   {{\cal F}}\{x u\}=i\big({{\cal F}}u\big){{^{\prime}}},

með þrepun fæst,

.. math::

  {{\cal F}}\{u^{(k)}\}=(i{\xi})^k{{\cal F}}u, \qquad
   {{\cal F}}\{x^k u\}=i^k\big({{\cal F}}u\big)^{(k)},

og að lokum

.. math:: {{\cal F}}\{P(D)u\}=P(i{\xi}) {{\cal F}}u,

ef :math:`P(D)` er afleiðuvirki með fastastuðla. Látum nú :math:`E`
vera grunnlausn virkjans :math:`P(D)` og gerum ráð fyrir að
:math:`E\in {{\cal S}}{{^{\prime}}}({{\mathbb  R}})`. Þá uppfyllir
:math:`E` jöfnuna :math:`P(D)E={\delta}`. Ef við tökum Fourier-mynd
beggja vegna jafnaðarmerkisins og gefum okkur að
:math:`{\xi}\mapsto P(i{\xi})` hafi enga núllstöð á raunásnum, þá fáum
við

.. math:: \widehat E({\xi}) =\dfrac 1{P(i{\xi})}.

Við reiknuðum út andhverfu Fourier-myndina af þessu falli í setningu
6.5.2. Niðurstaðan verður því:

Setning
^^^^^^^

Látum :math:`P` vera margliðu af stigi :math:`\geq 2`, gerum ráð fyrir
að :math:`P` hafi engar núllstöðvar á þverásnum og látum :math:`E` vera
andhverfu Fourier-myndina af fallinu :math:`{\xi}\mapsto 1/P(i{\xi})`,
sem gefið er með formúlunni (:ref:`Link title <6.5.7>`). Þá er :math:`E` grunnlausn
afleiðuvirkjans :math:`P(D)`.

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^
Látum :math:`\varphi:{{\mathbb  R}}\to {{\mathbb  R}}` vera
fallið, sem skilgreint er með :math:`\varphi(x)=x^{-a}e^{-1/x}` ef
:math:`x>0` og :math:`\varphi(x)=0` ef :math:`x\leq 0`, þar sem
:math:`a\in {{\mathbb  R}}`. Sýnið að
:math:`\varphi\in C^{\infty}({{\mathbb  R}})`. [*Leiðbeining:* Sýnið með
þrepun að :math:`\varphi^{(n)}(x)=x^{-a}P_n(1/x)e^{-1/x}`, :math:`x>0`,
þar sem :math:`P_n` er margliða og að af því leiði að
:math:`\varphi^{(n)}(0)` er til fyrir öll :math:`n`.]

.. figure:: ./myndir/fig0210.svg
    :align: center
    :alt: Vantar titil

    Mynd: Vantar titil

Dæmi
^^^^

Látum :math:`a` og :math:`b` vera tvær rauntölur, :math:`a<b`. Notið
niðurstöðuna úr dæmi 1 til þess að sýna að til sé fall :math:`\varphi\in {{\mathbb  C}}^{\infty}({{\mathbb  R}})` þannig að :math:`\varphi(x)>0`,
ef :math:`x\in ]a,b[`, :math:`\varphi(x)=0`, ef :math:`x\not\in ]a,b[`
og :math:`\int_{-{\infty}}^{+{\infty}}\varphi(x)\, dx=1`.


Dæmi
^^^^

Látum :math:`a,b\in {{\mathbb  R}}`, :math:`a<b` og
:math:`{\varepsilon}>0`. Sýnið að til sé fall
:math:`{\psi}\in C^{\infty}_0([a-{\varepsilon},b+{\varepsilon}])` þannig
að :math:`{\psi}(x)=1` ef :math:`x\in [a,b]`. [*Leiðbeining:* Látum
:math:`\varphi` vera fallið í dæmi 2, þar sem skipt er á :math:`a` og
:math:`-{\varepsilon}/2` og :math:`b` og :math:`{\varepsilon}/2` og
látum fallið :math:`{\chi}` vera skilgreint sem :math:`{\chi}(x)=1` ef
:math:`x\in[a-{\varepsilon}/2,b+{\varepsilon}/2]` og :math:`{\chi}(x)=0`
ef :math:`x\notin[a-{\varepsilon}/2,b+{\varepsilon}/2]`. Setjið síðan
:math:`{\psi}(x)={\chi}\ast \varphi(x)`.]

.. figure:: ./myndir/fig0211.svg
    :align: center
    :alt: Vantar titil

    Mynd: Vantar titil

Dæmi
^^^^

Látum :math:`f,g\in C(X)`, þar sem :math:`X` er opið mengi á
:math:`{{\mathbb  R}}` og gerum ráð fyrir að :math:`u_f=u_g`. Sýnið að
:math:`f=g`.

Dæmi
^^^^

Fyrir sérhvert :math:`t\in {{\mathbb  R}}` skilgreinum við
:math:`f_t(x)=t^Ne^{itx}`, þar sem :math:`N` er jákvæð heiltala. Sýnið
að :math:`f_t\to 0` í veikum skilningi ef :math:`t\to \pm{\infty}`.

[*Leiðbeining:* Hlutheildið þar til veldið á :math:`t` hefur lækkað
niður í :math:`-1`.]

Dæmi
^^^^

Látum :math:`f_t` vera fallið :math:`f_t(x)=tH(x)e^{itx}`,
:math:`x\in {{\mathbb  R}}`, þar sem :math:`H` er Heaviside-fallið.
Sýnið að :math:`f_t\to i{\delta}` í veikum skilningi ef
:math:`t\to +{\infty}`.

Dæmi
^^^^

Sýnið að :math:`f_t(x)=t^2|x|\cos(tx) \to -2{\delta}` í veikum skilningi
ef :math:`t \to +{\infty}`.

Dæmi
^^^^

Reiknið út :math:`x^j{\delta}_0^{(k)}` fyrir allar heilar tölur
:math:`j\geq 0` og :math:`k\geq 0`.

Dæmi
^^^^

Ákvarðið allar veikar lausnir á :math:`{{\mathbb  R}}` á jöfnunum:

\(i) :math:`xu{{^{\prime}}}={\delta}_0`,

\(ii) :math:`xu{{^{\prime}}}={\delta}_1-{\delta}_{-1}`,

\(iii) :math:`u{{^{\prime\prime}}}={\delta}_0{{^{\prime}}}-2{\delta}_1`.

Dæmi
^^^^

Reiknið út Fourier-myndir dreififallanna :math:`u_f` þar sem
:math:`f(x)` er gefið með formúlunum

+----------------------+-------------------+-----------------------+
| \a. :math:`\sin x`,  | \b. :math:`x^k`,  | \c. :math:`(1+x)^6`.  |
+----------------------+-------------------+-----------------------+

Dæmi
^^^^

Reiknið út Fourier-myndir dreififallanna :math:`u`, sem gefin eru og
skrifið :math:`\widehat u({\xi})=F({\xi})` ef Fourier-myndin er á
forminu :math:`u_F`, þar sem :math:`F` er fall:

+--------------------------------+----------------------------------------+----------------------------------------+
| \a. :math:`{\delta}_a^{(k)}`,  | \b. :math:`{\delta}_a-{\delta}_{-a}`,  | \c. :math:`{\delta}_a+{\delta}_{-a}`.  |
+--------------------------------+----------------------------------------+----------------------------------------+

Dæmi
^^^^

abcd) Sýnið með beinum reikningum að föllin :math:`E`, sem fengust í
dæmi 6.5.3 séu grunnlausnir afleiðuvirkjanna :math:`P(D)`.
