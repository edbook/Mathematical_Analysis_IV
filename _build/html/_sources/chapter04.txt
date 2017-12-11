LEIFAREIKNINGUR
===============

Samleitnar Laurent-raðir
------------------------

Fyrir sérhvert fall :math:`f\in {{\cal O}}(X)` og sérhvern punktur í
:math:`\alpha\in X` fæst veldaraðarframsetning á fallinu :math:`f` og
röðin er samleitin á sérhverri skífu :math:`S(\alpha,\varrho)\subset X`.
Þessi setning á sér alhæfingu jafnvel fyrir punkta :math:`\alpha` utan
:math:`X`, ef hægt er að koma fyrir opnum hringkraga með miðju í
:math:`\alpha` inni í :math:`X`

Hringkragar
~~~~~~~~~~~

Mengi af gerðinni

.. math::

  A(\alpha,\varrho_1,\varrho_2)=\{z\in {{\mathbb  C}}\,;\,
   \varrho_1<|z-\alpha|<\varrho_2\}

þar sem :math:`0\leq\varrho_1<\varrho_2\leq +\infty` kallast *opinn*
:hover:`hringkragi` með miðju í :math:`\alpha`, *innri geisla* 
:math:`\varrho_1`, og *ytri geisla* :math:`\varrho_2`, og mengi af gerðinni

.. math::

  \bar A(\alpha,\varrho_1,\varrho_2)=\{z\in {{\mathbb  C}}\,;\,
   \varrho_1\leq|z-\alpha|\leq\varrho_2\}

þar sem :math:`0<\varrho_1<\varrho_2\leq +\infty` kallast *lokaður*
:hover:`hringkragi` með miðju í :math:`\alpha`,
*innri geisla* :math:`\varrho_1`, og *ytri geisla* :math:`\varrho_2`.

.. figure:: ./myndir/fig097.svg
    :align: center
    :alt: Hringkragi

    Mynd: Hringkragi

Laurent-setningin
~~~~~~~~~~~~~~~~~

Fágað fall á skífu er hægt að setja fram með veldaröð. Ef fall er fágað
á hringkraga þá koma til sögunnar veldaraðir með neikvæða veldisvísa:

Setning
^^^^^^^

(*Laurent*).   Látum
:math:`X` vera opið hlutmengi af :math:`{{\mathbb  C}}` og gerum ráð
fyrir að :math:`A(\alpha,\varrho_1,\varrho_2)\subset X`, þar sem
:math:`0\leq \varrho_1<\varrho_2\leq +\infty`. Ef :math:`f\in {{\cal O}}(X)`, þá er
unnt að skrifa :math:`f` sem

.. math::

  f(z)=\sum_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n, \qquad z\in
   A(\alpha,\varrho_1,\varrho_2).


   

Stuðlar raðarinnar :math:`a_n` eru gefnir með formúlunni

.. math::

  a_n=\dfrac 1{2\pi i}\int_{\partial S(\alpha,r)} \dfrac{f(\zeta)}
   {(\zeta-\alpha)^{n+1}} \, d\zeta,


   

og heildið er óháð því hvaða tala :math:`r\in ]\varrho_1,\varrho_2[` er
valin. Röðin

.. math:: \sum_{n=0}^{+\infty}a_n(z-\alpha)^ n

er samleitin ef :math:`|z-\alpha|<\varrho_2` og röðin

.. math:: \sum_{n=-\infty}^{-1}a_n(z-\alpha)^ n

er samleitin ef :math:`|z-\alpha|>\varrho_1`.

Laurent-raðir
~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Röð af gerðinni

.. math:: \sum_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n

kallast *Laurent-röð*. *Innri samleitnigeisli* 
raðarinnar :math:`\varrho_1` er skilgreindur sem neðra mark yfir
:math:`\varrho=|z-\alpha|` þannig að

.. math:: \sum_{n=-\infty}^{-1} a_n(z-{\alpha})^ n

er samleitin, *ytri samleitnigeisli* raðarinnar :math:`\varrho_2` er skilgreindur sem efra
mark yfir öll :math:`\varrho=|z-\alpha|` þannig að

.. math:: \sum_{n=0}^{+\infty}a_n(z-{\alpha})^ n

er samleitin. Ef :math:`\varrho_1<\varrho_2` þá segjum við að
Laurent-röðin sé *samleitin*. Stuðullinn :math:`a_{-1}` kallast 
:hover:`leif` Laurent-raðarinnar og röðin

.. math:: \sum_{n=-\infty}^{-1}a_n(z-{\alpha})^ n

kallast :hover:`höfuðhluti` hennar.

--------------

Ef Laurent-röð :math:`\sum_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n` er
samleitin og :math:`\varrho_1` og :math:`\varrho_2` tákna innri og ytri
samleitnigeisla hennar, þá skilgreinir hún fágað fall á hringkraganum
:math:`A(\alpha,\varrho_1,\varrho_2)` með formúlunni

.. math:: f(z)=\sum_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n.

Hugsum okkur nú að :math:`\gamma` sé lokaður vegur sem liggur í
:math:`A(\alpha,\varrho_1,\varrho_2)` og lítum á heildið

.. math::

  \int_{\gamma} f(z)\, dz=
   \sum_{n=-\infty}^{+\infty} a_n
   \int_{\gamma} (z-\alpha)^ n\, dz.


   

Hér höfum við notfært okkur að röðin er samleitin í jöfnum mæli á
veginum :math:`\gamma` til þess að flytja heildið inn fyrir summutáknið.
Nú athugum við að allir liðirnir í summunni hafa stofnfall nema sá með
númerið :math:`n=-1`. Þar með er

.. math::

  \int_{\gamma} f(z)\, dz=
   a_{-1}
   \int_{\gamma} \dfrac {dz}{z-\alpha}.

Ef nú :math:`\gamma` er einfaldur lokaður vegur, sem stikar jaðarinn
:math:`\partial\Omega` á svæðinu :math:`\Omega` í jákvæða stefnu, þá
segir Cauchy-formúlan að síðasta heildið sé :math:`2\pi i` ef
:math:`\alpha` er inni í svæðinu, en Cauchy-setningin segir að það sé
:math:`0` ef :math:`\alpha` er utan þess. Þar með er

.. math::

  \int_\gamma f(z) \, dz =\begin{cases}
   2\pi i\, a_{-1}, &\alpha\in \Omega,\\
   0, & \alpha\not\in \overline \Omega.\end{cases}


   

Í tilfellinu að :math:`A(\alpha,\varrho_1,\varrho_2)\subset S(\alpha,\varrho_2)\subset X`, þ.e. þegar fallið :math:`f` er fágað á
svæði sem inniheldur alla hringskífuna :math:`S(\alpha,\varrho_2)`, þá
eru föllin

.. math::

  \zeta\mapsto \dfrac
   {f(\zeta)}{(\zeta-\alpha)^{n+1}}=(\zeta-\alpha)^{-n-1}f({\zeta}),

fáguð í :math:`S(\alpha,\varrho_2)` fyrir öll :math:`n<0`.
Cauchy-setninginn segir okkur þá að :math:`a_n=0` ef :math:`n<0` og
Cauchy-formúlan fyrir afleiður gefur okkur

.. math:: a_n=\dfrac{f^{(n)}(\alpha)}{n!}, \qquad n\geq 0.

Ef
:math:`A(\alpha,\varrho_1,\varrho_2)\subset S(\alpha,\varrho_2)\subset X`,
þá þýðir þetta sem sagt að Laurent-röð fallsins :math:`f` í
:math:`{\alpha}` sé Taylor-röð þess.

Einangraðir sérstöðupunktar
---------------------------

Einangraðir punktar og dreifð mengi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`A` vera hlutmengi í :math:`{{\mathbb  C}}`. Rifjum það
upp að punktur :math:`\alpha\in A` kallast 
:hover:`einangraður punktur` í :math:`A` ef til er
:math:`\varepsilon>0` þannig að :math:`\alpha` er eini punkturinn í
:math:`A` sem liggur í opnu skífunni :math:`S(\alpha,\varepsilon)`. Við
segjum að mengið :math:`A` sé *dreift* ef sérhver
punktur í því er einangraður.

Höfuðhluti og leif
~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Látum :math:`X` vera opið mengi, :math:`\alpha\in \partial X` og
:math:`f\in {{\cal O}}(X)`.

\(i) Punkturinn :math:`\alpha` er sagður vera :hover:`einangrður sérstöðupunktur`
fágaða fallsins :math:`f` ef :math:`\alpha` er einangraður punktur í jaðrinum
:math:`\partial X`.

\(ii) Samkvæmt Laurent-setningunni getum við skrifað

.. math::

    f(z)= \sum_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n, \qquad z\in 
    S^\ast(\alpha,\varepsilon)=A(\alpha,0,\varepsilon),

þar sem stuðlarnir :math:`a_n` eru ótvírætt ákvarðaðir. Við köllum
þessa röð *Laurent-röð fágaða fallsins*
:math:`f` *í punktinum* :math:`\alpha`.

\(iii) Við köllum :hover:`höfuðhluta,höfuðhluti` raðarinnar *höfuðhluta fágaða fallsins*
:math:`f`  *í punktinum*
:math:`\alpha`.

\(iv) Við köllum :hover:`leif` raðarinnar *leif fallsins*
:math:`f`  *í punktinum*
:math:`\alpha` og við táknum hana með

.. math:: {{\operatorname{Res}}}(f,\alpha).

\(v) Punkturinn :math:`{\alpha}` er sagður vera :hover:`afmáanlegur,afmáanlegur sérstöðupunktur`,
ef :math:`a_n=0` fyrir öll
:math:`n<0`, sem jafngildir því að segja að höfuðhluti
Laurent-raðarinnar sé núllröðin.

\(vi) Punkturinn :math:`\alpha` er sagður vera :hover:`skaut`
ef til er :math:`m>0` þannig að
:math:`a_{-m}\neq 0` og :math:`a_n=0` ef :math:`n<-m`. Talan
:math:`m` nefnist þá *stig skautsins* :math:`\alpha`.

\(vii) Punkturinn :math:`\alpha` kallast :hover:`verulegur sérstöðupunktur`,
ef til eru óendanlega mörg gildi á :math:`n<0`
þannig að :math:`a_n\neq 0`, en það jafngildir því að segja að
:math:`\alpha` sé hvorki afmáanlegur sérstöðupunktur né skaut.

Afmáanlegir sérstöðupunktar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`\alpha` er afmáanlegur, þá er Laurent-röð :math:`f` í
:math:`\alpha` veldaröð

.. math:: f(z)=\sum_{n=0}^\infty a_n(z-\alpha)^n, \qquad z\in S^\ast(\alpha,\varepsilon).

Þar með er :math:`\lim_{z\to \alpha}f(z)=a_0`, svo við skilgreinum
:math:`f(\alpha)=a_0`. Veldaröðin skilgreinir fágað fall í
samleitniskífu sinni sem er grennd um :math:`\alpha`. Þetta segir okkur
að :math:`\alpha` sé afmáanlegur sérstöðupunktur þá og því aðeins að
:math:`f` framlengist í fágað fall í grennd um :math:`\alpha`.

Ef :math:`f` er núllfallið á :math:`S(\alpha,\varepsilon)` þá eru allir
stuðlar veldaraðarinnar :math:`0`, en ef :math:`f` er ekki núllfallið,
þá er til :math:`m\geq 0` þannig að :math:`a_m\neq 0` og :math:`a_n=0`
ef :math:`0\leq n<m` og veldaraðarframsetning :math:`f` í :math:`\alpha`
er

.. math::

  \begin{aligned}
   f(z)&=\sum_{n=m}^\infty a_n(z-\alpha)^n\\
   &=a_{m}(z-\alpha)^{m}+a_{m+1}(z-\alpha)^{m+1}+a_{m+2}(z-\alpha)^{m+2}+\cdots
   \\
   &=(z-\alpha)^{m}\sum_{k=0}^\infty a_{m+k} (z-\alpha)^k
   =(z-\alpha)^{m}g(z), \qquad z\in
     S(\alpha,\varepsilon),  \end{aligned}

þar sem fallið :math:`g\in {{\cal O}}(X\cup\{\alpha\})` er skilgreint
með

.. math::

  g(z)=\begin{cases}
     &\dfrac{f(z)}{(z-\alpha)^m},& z\in X,\\
   a_m=&\dfrac{f^{(m)}(\alpha)}{m!},&z=\alpha.
   \end{cases}

Niðurstaðan er því:

.. \_se:4.2.2xx:

Setning
^^^^^^^

Einangraður sérstöðupunktur :math:`\alpha` fallsins :math:`f` er
:hover:`afmáanlegur` ef og aðeins ef til er heiltala :math:`m\geq 0` og fágað
fall :math:`g\in {{\cal O}}(U)` á grennd :math:`U` um :math:`\alpha`,
þannig að :math:`g(\alpha)\neq 0` og

.. math:: f(z)=(z-\alpha)^m g(z), \qquad z\in U.

--------------

Við getum einkennt afmáanlega sérstöðupunkta á annan hátt:

.. \_se:4.2.3xx:

Setning
^^^^^^^

(*Riemann*).   Gerum
ráð fyrir að :math:`\alpha` sé einangraður sérstöðupunktur fágaða
fallsins :math:`f`. Þá er :math:`\alpha` afmáanlegur sérstöðupunktur ef
og aðeins ef

.. math::

  \lim_{z\to \alpha}(z-\alpha)f(z)= 0.

Skaut
~~~~~

Ef :math:`\alpha` er skaut af stigi :math:`m`, þá getum við skrifað

.. math::

  \begin{aligned}
   f(z)&=\sum_{n=-m}^\infty a_n(z-\alpha)^n\\
   &=a_{-m}(z-\alpha)^{-m}+a_{m+1}(z-\alpha)^{-m+1}+a_{m+2}(z-\alpha)^{-m+2}+\cdots
   \\
   &=(z-\alpha)^{-m}\sum_{k=0}^\infty a_{-m+k} (z-\alpha)^k
   =\dfrac{g(z)}{(z-\alpha)^m}, \qquad z\in
     S^\ast(\alpha,\varepsilon),  \end{aligned}

þar sem fallið :math:`g\in {{\cal O}}(X\cup\{\alpha\})` er skilgreint
með

.. math::

   g(z)=\begin{cases}
   (z-\alpha)^m f(z),& z\in X,\\
   a_{-m},&z=\alpha.
   \end{cases}

Þessi framsetning á fallinu :math:`f` í grennd um :math:`\alpha` auðkennir
skaut af stigi :math:`m`:

.. \_se:4.2.4xx:

Setning
^^^^^^^

Einangraður sérstöðupunktur :math:`\alpha` fallsins :math:`f` er
:hover:`skaut` *af stigi* :math:`m` ef og aðeins ef til er fágað
fall :math:`g\in {{\cal O}}(U)` á grennd :math:`U` um :math:`\alpha`,
þannig að :math:`g(\alpha)\neq 0` og

.. math:: f(z)=\dfrac{g(z)}{(z-\alpha)^ m}, \qquad z\in U\setminus{{\{\alpha\}}}.

--------------

Við höfum einfalda einkenningu á skautum í líkingu við setningu
Riemanns:

.. \_se:4.2.5xx:

Setning
^^^^^^^

Fall :math:`f` hefur skaut í :math:`\alpha` ef og aðeins ef
:math:`|f(z)|\to +\infty` þegar :math:`z\to \alpha`.

--------------

Hugsum okkur nú að fallið :math:`f` hafi skaut í punktinum
:math:`\alpha` af stigi :math:`m`. Þá er fallið sett fram með
Laurent-röð af gerðinni

.. math:: f(z)=\sum\limits_{n=-m}^{+\infty} a_n(z-\alpha)^n,

í grennd um :math:`\alpha`. Ef höfuðhlutinn er táknaður með
:math:`h(z)`, þá er :math:`\alpha` afmáanlegur sérstöðupunktur
mismunarins

.. math::

  f(z)-h(z) =f(z)-\sum\limits_{n=-m}^{-1} a_n(z-\alpha)^n 
   = \sum\limits_{n=0}^\infty a_n(z-\alpha)^n.

Stofnbrotaliðun
~~~~~~~~~~~~~~~

Í grein 1.5 gengum við út frá því sem vísum
hlut, að það væri alltaf hægt að liða rætt fall í 
:hover:`stofnbrot`. 
Nú skulum við sanna þetta og leiða út formúlurnar
fyrir stuðlunum í :hover:`stofnbrotaliðuninni,stofnbrotaliðun`.

Látum :math:`R=P/Q` vera rætt fall og gerum ráð fyrir að
:math:`{{\operatorname{stig}}}P<{{\operatorname{stig}}}Q`. Látum
:math:`\alpha_1,\dots,\alpha_k` vera ólíkar núllstöðvar :math:`Q`, látum
:math:`m_1,\dots,m_k` vera margfeldni þeirra og setjum
:math:`m={{\operatorname{stig}}}Q=m_1+\cdots+m_k`. Þá er greinilegt að
fallið :math:`R` hefur skaut af stigi :math:`\leq m_j` í
:math:`\alpha_j` og ef við látum

.. math::

  h_j(z)=\dfrac{A_{j,0}}{(z-\alpha_j)^{m_j}}+\cdots+
   \dfrac{A_{j,m_j-1}}{(z-\alpha_j)}

tákna höfuðhluta fallsins :math:`R` í punktinum :math:`\alpha_j`, þá
hefur fallið

.. math:: f(z)= R(z)-h_1(z)-\cdots-h_k(z)

afmáanlega sérstöðupunkta í :math:`\alpha_1,\dots,\alpha_k`. Við setjum
:math:`f(\alpha_j)=\lim_{z\to \alpha_j}f(z)`, og fáum að :math:`f\in {{\cal O}}({{\mathbb  C}})`. Fyrst
:math:`{{\operatorname{stig}}}P <{{\operatorname{stig}}}Q`, þá sjáum við
að fallið sem stendur hægra megin jafnaðarmerkisins stefnir á :math:`0`
ef :math:`|z|\to +\infty`. Setning Liouville segir okkur nú að :math:`f` sé núllfallið.
Þar með er

.. math:: R(z)=h_1(z)+\cdots+h_k(z).

Ef við styttum þáttinn :math:`(z-\alpha_j)^{m_j}` út úr margliðunni
:math:`Q(z)` þá fáum við margliðu og getum skrifað fallið :math:`R` sem

.. math::

  R(z)=\dfrac{f_j(z)}{(z-\alpha_j)^{m_j}}, \qquad
   f_j(z)=\dfrac{P(z)}{q_j(z)},  \quad q_j(z)=\dfrac{Q(z)}{(z-\alpha_j)^{m_j}}
   =\prod\limits_{\substack{\ell=1\\ \ell\neq j}}^k
   (z-\alpha_\ell)^{m_\ell}.

Fallið :math:`f_j` er fágað í grennd um :math:`\alpha_j` og stuðlarnir
í stofnbrotaliðun :math:`R` í :math:`\alpha_j` eru :math:`m_j` fyrstu
liðir í Taylor-röð :math:`f_j` í :math:`\alpha_j`,

.. math::

  A_{j,\ell}=\dfrac {f_j^{(\ell)}(\alpha_j)}{\ell!}
   \qquad \ell=0,\dots,m_j-1.

Verulegir sérstöðupunktar
~~~~~~~~~~~~~~~~~~~~~~~~~

Hegðun fágaðra falla í grennd um verulega sérstöðupunkta er lýst með:

Setning
^^^^^^^

(*Casorati-Weierstrass*).   Gerum ráð fyrir að :math:`\alpha` sé
einangraður sérstöðupunktur fallsins :math:`f\in {{\cal O}}(X)`. Þá er
:math:`\alpha` verulegur þá og því aðeins að

.. math::

  f(S^\ast(\alpha,\varepsilon))\cap S(\beta,\delta)\neq \varnothing

fyrir sérhvert :math:`\varepsilon>0` þannig að
:math:`S^\ast(\alpha,\varepsilon)\subset X`, sérhvert
:math:`\beta\in {{\mathbb  C}}`, og sérhvert :math:`\delta>0`.

--------------

Setningunar má túlka þannig að hegðun falls í gataðri grennd um
verulegan sérstöðupunkt sé mjög villt, þannig að sama hversu lítil götuð
grennd um punktinn er tekin, fallið :math:`f` varpar henni um allt
planið þannig að mynd grenndarinnar skeri allar opnar skífur.

Til er miklu nákvæmari setning sem er einnig miklu erfiðara að sanna:

Setning
^^^^^^^

(*Picard-setning hin meiri*).   Gerum ráð fyrir að :math:`\alpha` sé
einangraður sérstöðupunktur fallsins :math:`f\in {{\cal O}}(X)`.
Punkturinn :math:`\alpha` er verulegur sérstöðupunktur þá og því aðeins
að fyrir sérhvert :math:`\varepsilon>0` er myndmengið
:math:`f(S^\ast(\alpha,\varepsilon))` allt tvinntalanplanið
:math:`{{\mathbb  C}}` með í hæsta lagi tveimur undantekningum.

Leifasetning
------------

Leifasetning
~~~~~~~~~~~~

Við sáum í síðasta kafla hvernig hægt er að hagnýta Cauchy-formúluna og
Cauchy-formúluna fyrir afleiður til þess að reikna út ákveðin heildi.
Við ætlum nú að beita Cauchy-setningunni til þess að alhæfa þessar
formúlur fyrir heildi yfir lokaða vegi. Við höfum séð að það er
einstaklega auðvelt að reikna út vegheildi af föllum, sem gefin eru með
samleitnum Laurent-röðum yfir lokaða vegi, því við getum alltaf heildað
röðina lið fyrir lið og allir liðirnir hafa stofnfall nema sá með
númerið :math:`-1`.

Setning
^^^^^^^

(:hover:`Leifasetning,leifasetning`).   Látum :math:`X` vera opið
hlutmengi í :math:`{{\mathbb  C}}` og látum :math:`\Omega` vera opið
hlutmengi af :math:`X` sem uppfyllir sömu forsendur og í
Cauchy-setningunni. Látum :math:`A` vera dreift hlutmengi af :math:`X`
sem sker ekki jaðarinn :math:`\partial\Omega` á :math:`\Omega`. Ef
:math:`f\in {{\cal O}}(X\setminus A)`, þá er

.. math::

  \int_{\partial\Omega}f(z)\, dz = 2\pi i \sum_{\alpha\in \Omega\cap A}
   {{\operatorname{Res}}}(f,\alpha).


   


Útreikningur á leifum
---------------------

Cauchy-formúla og leifasetning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`X` vera opið hlutmengi af :math:`{{\mathbb  C}}` og
:math:`\Omega` vera opið hlutmengi af :math:`X`, þannig að jaðarinn
:math:`\partial\Omega` af :math:`\Omega` sé einnig innihaldinn í
:math:`X`. Við hugsum okkur jafnframt að :math:`\partial\Omega` sé
stikaður af endanlega mörgum vegum :math:`\gamma_1,\dots,\gamma_N`, sem
skerast aðeins í endapunktum, og að þeir stiki :math:`\partial\Omega` í
jákvæða stefnu, sem þýðir að svæðið sé vinstra megin við snertilínuna í
punkti :math:`\gamma_j(t)`, ef horft er í stefnu
:math:`\gamma_j{{^{\prime}}}(t)`. Hér höfum við verið að telja upp
þann hluta af forsendum Cauchy–setningarinnar sem lýsa stikun á jaðri.
Til viðbótar gerum við ráð fyrir að :math:`A` sé dreift hlutmengi af
:math:`X` og að :math:`f\in {{\cal A}}(X\setminus A)`. Þá eru allir
punktarnir í :math:`A` einangraðir sérstöðupunktar fallsins :math:`f` og
leifasetningin segir okkur að

.. math::

  \int _{\partial {\Omega}} f(\zeta)\, d\zeta =2\pi i

   

  \sum\limits_{\alpha\in A\cap \Omega}
   {{\operatorname{Res}}}(f,\alpha).

Ef :math:`A\cap \Omega=\varnothing`, þá er summan sett :math:`0`, eins
og alltaf þegar summa yfir tóma mengið er tekin. Þetta er í fullu
samræmi við Cauchy–setninguna, því í þessu tilfelli er :math:`f` fágað í
grennd um :math:`\overline\Omega=\partial\Omega\cup \Omega` og þá er
heildið í vinstri hliðinni jafnt :math:`0`.

Cauchy–formúlan er líka sértilfelli af leifasetningunni, því ef
:math:`z\in \Omega` og :math:`\Omega\cap A=\varnothing`, þá hefur fallið
:math:`\zeta\mapsto f(\zeta)/(\zeta-z)` eitt skaut :math:`z` af stigi
:math:`\leq 1` í :math:`\Omega` og leifasetningin segir okkur að

.. math::

  \dfrac 1{2\pi i}\int_{\partial\Omega} \dfrac{f(\zeta)}{\zeta-z}\,
   d\zeta = {{\operatorname{Res}}}\bigg( \dfrac{f(\zeta)}{\zeta-z},z\bigg)=f(z).

Leif í einföldu skauti
~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við huga að því, hvernig farið er að því að reikna út leif
:math:`{{\operatorname{Res}}}(f,\alpha)` fallsins :math:`f` í einangraða
sérstöðupunktinum :math:`\alpha`. Samkvæmt skilgreiningu er
:math:`{{\operatorname{Res}}}(f,\alpha)=a_{-1}`, þar sem

.. math::

  f(z)=\sum\limits_{n=-\infty}^{+\infty}a_n(z-\alpha)^n, 

   

  \qquad z\in S^\ast(\alpha,\varepsilon),

er framsetning á :math:`f` með Laurent–röð.

Ef við höfum skaut af stigi :math:`1` í punktinum :math:`\alpha`, þá eru
:math:`a_n=0` fyrir öll :math:`n<-1`, í Laurent–röðinnni og við fáum

.. math:: (z-\alpha)f(z)=a_{-1}+a_0(z-\alpha)+a_1(z-\alpha)^2+\cdots.

Af þessari formúlu leiðir síðan

.. math::

   

  {{\operatorname{Res}}}(f,\alpha)=a_{-1}=\lim_{z\to \alpha}(z-\alpha)f(z).

Leif í skauti af stigi :math:`m>1`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við skulum gera ráð fyrir að :math:`f` hafi skaut af stigi :math:`m>0` í
punktinum :math:`\alpha`. Við látum :math:`g` vera fallið sem skilgreint
með

.. math::

   g(z)=\begin{cases}
   (z-\alpha)^m f(z),& z\in X,\\
   a_{-m},&z=\alpha.
   \end{cases}

Við sjáum að stuðlar
:math:`b_n` í Taylor–röð fallsins :math:`g` í punktinum :math:`\alpha`
gefnir með :math:`b_n=a_{-m+n}` og því er

.. math::

  {{\operatorname{Res}}}(f,\alpha)=a_{-1}=b_{m-1}=\dfrac{g^{(m-1)}(\alpha)}{(m-1)!}.


   

Sértilfellið að :math:`\alpha` sé skaut af fyrsta stigi er einfaldast,

.. math::

  {{\operatorname{Res}}}(f,\alpha)= g(\alpha), \qquad\qquad m=1.


   

Cauchy-formúla fyrir afleiður og leifasetning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cauchy–formúlan fyrir afleiður er einnig sértilfelli af
leifasetningunni, því ef :math:`A\cap \Omega=\varnothing` og
:math:`z\in \Omega` þá hefur fallið
:math:`\zeta\mapsto f(\zeta)/(\zeta-z)^{n+1}` skaut af stigi
:math:`\leq n+1` í punktinum :math:`z` og samkvæmt formúlunni hér að
framan er

.. math::

  \dfrac{n!}{2\pi i}
   \int_{\partial\Omega}\dfrac{f(\zeta)}{(\zeta-z)^{n+1}}\, d\zeta = 
   {n!} {{\operatorname{Res}}}\bigg(\dfrac{f(\zeta)}{(\zeta-z)^{n+1}},z\bigg) =
   f^{(n)}(z).

Leif af kvóta tveggja falla
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við hugsa okkur að :math:`f` hafi skaut af stigi :math:`m` í
:math:`\alpha` og að :math:`f` sé gefið í grennd um :math:`\alpha` sem
:math:`f(z)=g(z)/h(z)`, þar sem :math:`g(\alpha)\neq 0` og :math:`h(\alpha)=0`. Þá getum við skrifað
:math:`h(z)=(z-\alpha)^mh_1(z)` þar sem :math:`h_1(z)` er fágað í grennd
um :math:`\alpha` og :math:`h_1(\alpha)=h^{(m)}(\alpha)/m!\neq 0`. Ef
:math:`f` hefur skaut af fyrsta stigi, þá er leifin

.. math::

  {{\operatorname{Res}}}(f,\alpha)= \lim_{z\to \alpha}(z-\alpha) f(z)
   =\lim_{z\to \alpha} 
   \dfrac{(z-\alpha)g(z)}{h(z)-h(\alpha)}=\dfrac{g(\alpha)}{h{{^{\prime}}}(\alpha)}.


   

Þetta segir okkur, að formúlan sem við leiddum út þegar við fjölluðum
um útreikning á heildum í kafla 3
ekkert annað en sértilfelli af leifasetningunni, því þar gerðum við ráð
fyrir að núllstöðvar :math:`\alpha_1,\dots,\alpha_m` margliðunnar
:math:`Q` væru einfaldar og því gefur leifasetningin

.. math::

  \int_{\partial\Omega}\dfrac{f(\zeta)}{Q(\zeta)}\, d\zeta
   =  2\pi i\sum_{\alpha_j\in \Omega}
   {{\operatorname{Res}}}\bigg(\dfrac{f(\zeta)}{Q(\zeta)}, \alpha_j\bigg) 
   =  2\pi i\sum_{\alpha_j\in \Omega} \dfrac{f(\alpha_j)}{Q{{^{\prime}}}(\alpha_j)}.

Ef :math:`f(z)=g(z)/h(z)`, þar sem :math:`g(\alpha)\neq 0` og :math:`h` hefur núllstöð af stigi :math:`m>1` og við skrifum
:math:`h(z)=(z-{\alpha})^mh_1(z)`, þá er

.. math::

  {{\operatorname{Res}}}(f,\alpha)=\dfrac 1{(m-1)!}\cdot
   \left.\dfrac {d^{m-1}}{dz^{m-1}}\bigg(\dfrac
   {g(z)}{h_1(z)}\bigg)\right|_{z=\alpha}. 

   

Stofnbrotaliðun og leifasetning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessu samhengi er skemmtilegt að nefna, að formúlan fyrir
stofnbrotaliðun, sem við settum fram í grein 1.5 og leiddum út í grein
4.2, leiðir beint af leifasetninunni og formúlunni hér að framan. Við
gerðum ráð fyrir að
:math:`{{\operatorname{stig}}}\, P<{{\operatorname{stig}}}\, Q`, að
:math:`Q` hefði núllstöðvar :math:`\alpha_1,\dots,\alpha_k` af stigi
:math:`m_1,\dots,m_k`,
:math:`m={{\operatorname{stig}}}\, Q=m_1+\cdots+m_k`, og við skrifuðum
:math:`Q(z)=(z-\alpha_j)^{m_j}q_j(z)`, þar sem :math:`q_j` er margliða
af stigi :math:`m-m_j`. Við veljum nú hringinn :math:`\gamma_r`, með
miðju í :math:`0` og geislann :math:`r` það stóran að
:math:`\alpha_1,\dots,\alpha_k` og :math:`z` liggi innan hans.
Leifasetningin gefur okkur þá

.. math::

  \begin{aligned}
   \dfrac 1{2\pi i}\int_{\gamma_r}\dfrac{P(\zeta)}{Q(\zeta)(\zeta-z)}\, d\zeta 
   &={{\operatorname{Res}}}\bigg(\dfrac{P(\zeta)}{Q(\zeta)(\zeta-z)},z\bigg) +
   \sum_{j=1}^k
   {{\operatorname{Res}}}\bigg(\dfrac{P(\zeta)}{Q(\zeta)(\zeta-z)},\alpha_j\bigg)\\
   &=\dfrac{P(z)}{Q(z)} +\sum\limits_{j=1}^k 
   \dfrac 1{(m_j-1)!}\cdot
   \left.\dfrac{d^{m_j-1}}{d{\zeta}^{m_j-1}}
   \bigg(\dfrac{P(\zeta)}{q_j(\zeta)(\zeta-z)}\bigg)\right|_{\zeta=\alpha_j}.\end{aligned}

Fyrst :math:`{{\operatorname{stig}}}\, P <{{\operatorname{stig}}}\, Q`,
þá er til fasti :math:`C` þannig að :math:`|P(\zeta)/Q(\zeta)|\leq C/r`
ef :math:`|\zeta|=r` og :math:`r` er nógu stórt. Heildið í vinstri hlið
jöfnunnar er óháð tölunni :math:`r` og við getum því metið það með
:math:`2\pi rC/r(r-|z|)\to 0`, :math:`r\to +\infty`. Heildið er því
:math:`0` og við fáum

.. math::

  \dfrac{P(z)}{Q(z)} =\sum\limits_{j=1}^k 
   \dfrac1{(m_j-1)!}\cdot
   \left.\dfrac{d^{m_j-1}}{d{\zeta}^{m_j-1}}
   \bigg(\dfrac{P(\zeta)}{q_j(\zeta)(z-\zeta)}\bigg)\right|_{\zeta=\alpha_j}.

Til þess að komast á leiðarenda með þessa formúlu þurfum við að nota
alhæfinguna fyrir formúlu Leibniz fyrir :math:`n`-tu afleiðu af
margfeldi tveggja falla. Venjulega er hún skrifuð

.. math::

  (\varphi\psi)^{(n)}(\zeta)=\sum_{\ell=0}^n \binom n\ell 
   \varphi^{(n-\ell)}(\zeta)\psi^{(\ell)}(\zeta),
   \qquad \binom n\ell=\dfrac {n!}{\ell!(n-\ell)!}.

Ef við deilum öllum liðum með :math:`n!` þá má skrifa hana

.. math::

  \dfrac 1{n!}(\varphi\psi)^{(n)}(\zeta)=
   \sum_{\ell=0}^n 
   \dfrac 1{(n-\ell)!} \varphi^{(n-\ell)}(\zeta)\cdot 
   \dfrac 1{\ell!}\psi^{(\ell)}(\zeta).

Nú setjum við :math:`n=m_j-1`, :math:`\varphi(\zeta)=(z-\zeta)^{-1}`,
:math:`\psi(\zeta)=P(\zeta)/q_j(\zeta)= f_j(\zeta)` og skilgreinum stuðlana
:math:`A_{j,\ell}=f_j^{(\ell)}(\alpha_j)/\ell!`. Þá fáum við með ítrun

.. math::
   
   \begin{gathered}
   \varphi(\zeta)=(z-\zeta)^{-1}, \quad 
   \varphi'(\zeta)=1\cdot(z-\zeta)^{-2}, \quad
   \varphi''(\zeta)=1\cdot2\cdot (z-\zeta)^{-3},\\
   \quad \dots, \quad
   \varphi^{(\ell)}(\zeta)=\ell! \cdot (z-\zeta)^{-\ell-1}.
  \end{gathered}

og

.. math::

  \begin{gathered}
   \dfrac1{(m_j-1)!}\cdot
   \left.\dfrac{d^{m_j-1}}{d{\zeta}^{m_j-1}}
   \bigg(\dfrac{P(\zeta)}{q_j(\zeta)(z-\zeta)}\bigg)\right|_{\zeta=\alpha_j}\\
   =\sum_{\ell=0}^{m_j-1}(z-\alpha_j)^{-(m_j-\ell)}
   \cdot \dfrac{f_j^{(\ell)}(\alpha_j)}{\ell!}  
   = \dfrac{A_{j,0}}{(z-\alpha_j)^{m_j}}+\cdots+\dfrac{A_{j,m_j-1}}{(z-\alpha_j)} \end{gathered}

Niðurstaðan er sú sama og við höfum áður séð,

.. math::

  \dfrac{P(z)}{Q(z)} =\sum\limits_{j=1}^k 
   \dfrac{A_{j,0}}{(z-\alpha_j)^{m_j}}+\cdots+\dfrac{A_{j,m_j-1}}{(z-\alpha_j)},
   \quad A_{j,\ell}=\dfrac{f_j^{(\ell)}(\alpha_j)}{\ell!}, \quad
   f_j(z)=\dfrac{(z-\alpha_j)^{m_j}P(z)}{Q(z)}.

Leifar reiknaðar út frá stuðlum í veldaröðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við gera ráð fyrir að :math:`f=g/h`,

.. math::

  f(z)=\sum\limits_{n=-m}^{\infty}a_n(z-\alpha)^n, \quad
   g(z)=\sum\limits_{n=k}^{\infty}b_n(z-\alpha)^n, \quad
   h(z)=\sum\limits_{n=l}^{\infty}c_n(z-\alpha)^n,

hugsum okkur að stuðlarnir :math:`b_n`, :math:`c_n` séu gefnir,
:math:`c_l\neq 0`, :math:`b_k\neq 0` og að við viljum reikna út leifina
:math:`{{\operatorname{Res}}}(f,\alpha)=a_{-1}`. Taylor–röð :math:`g` er
þá gefin sem margfeldi af Laurent–röð :math:`f` og Taylor–röð :math:`h`,

.. math::

  \sum\limits_{n=-m}^{\infty}a_n(z-\alpha)^n
   \sum\limits_{n=l}^{\infty}c_n(z-\alpha)^n=
   \sum\limits_{n=k}^{\infty}b_n(z-\alpha)^n.

Þetta segir okkur að :math:`-m+l=k` og að við fáum sambandið milli
stuðlanna með því að margfalda saman raðirnar í vinstri hliðinni

.. math::

  \begin{gathered}
   a_{-m}c_l=b_k,\\
   a_{-m+1}c_l+a_{-m}c_{l+1}=b_{k+1},\\
   a_{-m+2}c_l+a_{-m+1}c_{l+1}+a_{-m}c_{l+2}=b_{k+2},\\
   \qquad \vdots\qquad\qquad\qquad\vdots\\
   a_{-2}c_l+a_{-3}c_{l+1}+\cdots+a_{-m}c_{l+m-2}=b_{k+m-2}\\
   a_{-1}c_l+a_{-2}c_{l+1}+\cdots+a_{-m}c_{l+m-1}=b_{k+m-1}.\end{gathered}

Fyrst :math:`c_l\neq 0`, þá fáum við :math:`m` skrefa rakningarformúlu
fyrir :math:`a_{-m}, a_{-m+1},\dots, a_{-1}` og í síðasta skrefinu er leif :math:`f` í
:math:`\alpha` fundin,

.. math::

  \begin{aligned}
   a_{-m}&=c_l^{-1}b_k,\\
   a_{-m+1}&=c_l^{-1}\big(b_{k+1}
   -a_{-m}c_{l+1}\big),\\
   a_{-m+2}&=c_l^{-1}\big(b_{k+2}
   -a_{-m+1}c_{l+1}-a_{-m}c_{l+2}\big),\\
   &\qquad \vdots\qquad\qquad\qquad\vdots\\
   a_{-2}&=c_l^{-1}\big(b_{k+m-2}
   -a_{-3}c_{l+1}-\cdots-a_{-m}c_{l+m-2}\big)\\
   {{\operatorname{Res}}}(f,\alpha)=a_{-1}&=c_l^{-1}\big(
   b_{k+m-1}-a_{-2}c_{l+1}-\cdots-a_{-m}c_{l+m-1}\big).
   \end{aligned}

Ef engin af aðferðunum, sem við höfum verið að fjalla um hér, dugir til
að finna leifina þá er ekkert annað að gera en að reikna hana út frá
formúlunni sem við leiddum út í Laurent–setningunni,

.. math::

  {{\operatorname{Res}}}(f,\alpha) = \dfrac 1{2\pi i}\int_{\partial
   S(\alpha,\varepsilon)} f(\zeta)\, d\zeta,

þar sem við veljum geislann :math:`\varepsilon` í hringnum nógu lítinn.

Heildi yfir einingarhringinn
----------------------------

Við skulum gera ráð fyrir að :math:`f` sé fall af tveimur breytistærðum
:math:`(x,y)` og að :math:`f` sé skilgreint í grennd um
einingarhringinn, :math:`x^ 2+y^ 2=1`. Við fáum nú endurbót á
aðferðinni, sem við leiddum út eftir setningu 3.3.6. Eins og þar athugum
við, að ef :math:`z` er á einingarhringnum, :math:`z=e^{i\theta}`, þá
er

.. math::

  \begin{gathered}
   \cos\theta=\dfrac 12(e^{i\theta}+e^{-i\theta})
   =\dfrac12(z+\dfrac 1z)=\dfrac{z^ 2+1}{2z},\\ 
   \sin\theta=\dfrac 1{2i}(e^{i\theta}-e^{-i\theta})
   =\dfrac1{2i}(z-\dfrac 1z)=\dfrac{z^ 2-1}{2iz},\\ 
   dz=ie^{i\theta}d\theta, \qquad d\theta=\dfrac 1{iz}dz.\end{gathered}

Við getum því reiknað heildið út með leifareikningi

.. math::

  \begin{aligned}
   \int_0^ {2\pi}f(\cos\theta,\sin
   \theta)\, d\theta &=
   \int_{\partial S(0,1)}f\big(\dfrac{z^ 2+1}{2z},\dfrac{z^ 2-1}{2iz}\big)
   \dfrac 1{iz}\, dz\\
   &=2\pi i \sum_{\alpha\in A\cap S(0,1)} {{\operatorname{Res}}}\bigg(
   f\big(\dfrac{z^ 2+1}{2z},\dfrac{z^ 2-1}{2iz}\big)\dfrac 1{iz},\alpha
   \bigg),\end{aligned}

ef til er opin grennd :math:`X` um lokuðu einingarskífuna
:math:`\overline S(0,1)` og dreift mengi :math:`A` þannig að fallið
:math:`z\mapsto f\big({(z^ 2+1)}/{(2z)},{(z^ 2-1)}/{(2iz)}\big)/(iz)` sé fágað á
:math:`X\setminus A`.

Heildi yfir raunásinn
---------------------

Nú ætlum við að snúa okkur að heildum af gerðinni

.. math::

  I=\int_{-\infty}^{+\infty}f(x) \, dx 

   

þar sem fallið :math:`f` er fágað í grennd um :math:`{{\mathbb  R}}`.
Hugsum okkur fyrst að
:math:`f\in {{\cal O}}({{\mathbb  C}}\setminus A)`, þar sem :math:`A` er
dreift mengi. Aðferðin byggir á því að athuga að

.. math:: I=\lim_{r\to +\infty}\int_{-r}^ r f(x)\, dx,

ef heildið er samleitið. Leifasetningin gefur okkur þá

.. math::

  \int_{-r}^{r}f(x)\, dx +\int_{\gamma_r}f(z)\, dz =
   2\pi i\sum_{\alpha\in A\cap \Omega_r}{{\operatorname{Res}}}(f,\alpha)

og jafnframt

.. math::

  \int_{-r}^{r}f(x)\, dx +\int_{\beta_r}f(z)\, dz =
   -2\pi i\sum_{\alpha\in A\cap \widetilde\Omega_r}{{\operatorname{Res}}}(f,\alpha),

þar sem :math:`\Omega_r` og :math:`\widetilde\Omega_r` eru
hálfskífurnar á myndinni.

.. figure:: ./myndir/fig101.svg
    :align: center
    :alt: Hálfskífur í efra og neðra hálfplani

    Mynd: Hálfskífur í efra og neðra hálfplani

Ef unnt er að sýna fram á að önnur hvor summan í hægri hliðunum hafi
markgildi ef :math:`r\to +\infty` og að tilsvarandi vegheildi

.. math::

  \int_{\gamma_r}f(z)\, dz \qquad \text{ eða }
   \qquad \int_{\beta_r}f(z)\, dz

stefni á núll, þá verður

.. math::

  I=\int_{-\infty}^{+\infty}f(x)\, dx =
   2\pi i\sum_{\alpha\in A\cap H_+}{{\operatorname{Res}}}\big(f,\alpha)

eða

.. math::

  I=\int_{-\infty}^{+\infty}f(x)\, dx =
   -2\pi i\sum_{\alpha\in A\cap H_-}{{\operatorname{Res}}}\big(f,\alpha)

þar sem
:math:`H_+=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z>0\}` táknar
efra hálfplanið og
:math:`H_-=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z<0\}` táknar
neðra hálfplanið.

Heildi af ræðum föllum yfir raunásinn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aðferðin sem við vorum að lýsa gengur alltaf ef fallið :math:`f` er
rætt. Lítum nú á :math:`f=P/Q`, þar sem :math:`P(z)=\sum_{j=0}^ka_jz^j`
og :math:`Q(z)=\sum_{j=0}^mb_jz^j` eru margliður með
:math:`k={{\operatorname{stig}}}\, P\leq {{\operatorname{stig}}}\, Q-2=m-2`,
og gerum ráð fyrir að að :math:`Q` hafi engar núllstöðvar á
:math:`{{\mathbb  R}}`. Þá er

.. math::

  f(z)=\dfrac{a_k}{b_mz^{m-k}}\cdot 
   \dfrac{1+(a_{k-1}/a_k)z^{-1}+\cdots +(a_0/a_k)z^{-k}}
   {1+(b_{m-1}/b_m)z^{-1}+\cdots +(b_0/b_m)z^{-m}}.

Brotið í hægri hliðinni stefnir á :math:`1` ef :math:`r\to +\infty` og
því fáum við að

.. math:: |f(z)|\leq \dfrac {2|a_k|/|b_m|}{r^{m-k}},

ef :math:`|z|=r` og :math:`r` er það stórt að allar núllstöðvar
:math:`Q` liggja í :math:`S(0,r-1)`. Lengd veganna :math:`\gamma_r` og
:math:`\beta_r` er :math:`\pi r`, og :math:`m-k\geq 2` og því stefna
heildin af :math:`f(z)` yfir vegina :math:`\gamma_r` og :math:`\beta_r`
bæði á :math:`0` ef :math:`r\to +\infty`. Við höfum því:

.. \_se:4.6.1xx:

Setning
^^^^^^^

Látum :math:`f=P/Q`, þar sem :math:`P` og :math:`Q` eru margliður með
:math:`{{\operatorname{stig}}}\, P\leq {{\operatorname{stig}}}\, Q-2`,
og gerum ráð fyrir að að :math:`Q` hafi engar núllstöðvar á
:math:`{{\mathbb  R}}`. Þá er

.. math::

  \int\limits_{-\infty}^ {+\infty} f(x)\, dx =
   2\pi i\sum_{\alpha\in {\cal N}(Q)\cap H_+}{{\operatorname{Res}}}\big(f,\alpha)
   =-2\pi i\sum_{\alpha\in {\cal N}(Q)\cap H_-}{{\operatorname{Res}}}\big(f,\alpha),

þar sem :math:`{\cal N}(Q)` táknar núllstöðvamengi :math:`Q`,
:math:`H_+` táknar efra hálfplanið og :math:`H_-` táknar neðra
hálfplanið.

Leifareikningur og Fourier–ummyndun
-----------------------------------

Oft þarf að reikna út heildi af gerðinni

.. math:: \int_{-\infty}^{+\infty} F(x,\xi)\, dx, \qquad \xi\in X\subset {{\mathbb  C}},

og rannsaka það sem fall af breytunni :math:`\xi`. Ef fallið :math:`F`
á sér fágaða framlengingu sem fall af :math:`x` yfir svæði sem
inniheldur rauntalnalínuna, þá er stundum hægt að beita leifareikningi
til þess að reikna út heildið.

Lang mikilvægustu dæmin um svona heildi eru Fourier-myndir. Við látum
:math:`L^1({{\mathbb  R}})` tákna mengi allra tvinngildra falla
:math:`f` á :math:`{{\mathbb  R}}` þannig að bæði :math:`f` og
:math:`|f|` eru heildanleg föll. Þá er Fourier-mynd :math:`f` skilgreind
með

.. math::

  \widehat f(\xi)=\int_{-\infty}^{+\infty} e^{-ix\xi} f(x)\, dx, \qquad
   \xi\in {{\mathbb  R}}.

Vörpunin :math:`{{\cal F}}` sem úthlutar fallinu :math:`f` Fourier-mynd
sinni, :math:`{{\cal F}}(f)=\widehat f`, nefnist *Fourier-ummyndun*. Við
munum fjalla skipulega um Fourier-ummyndun í 16. kafla og sýna hvernig
þeim er beitt til þess að leysa afleiðujöfnur og hlutafleiðujöfnur.

Fourier-myndir reiknaðar með leifareikningi.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur nú að :math:`f\in {{\cal O}}({{\mathbb  C}}\setminus A)`,
þar sem :math:`A` er dreift mengi og skilgreinum vegina :math:`\gamma_r`
og :math:`\beta_r` eins og áður, :math:`\gamma_r(\theta)=re^{i\theta}`,
:math:`\beta_r(\theta)=re^{-i\theta}`, :math:`\theta\in [0,\pi]`.

.. figure:: ./myndir/fig101.svg
    :align: center
    :alt: Hálfskífur í efra og neðra hálfplani

    Mynd: Hálfskífur í efra og neðra hálfplani

Ef :math:`A` sker ekki hringinn
:math:`\{z\in {{\mathbb  C}}\,;\, |z|=r\}`, þá fáum við

.. math::

  \begin{gathered}
   \int_{-r}^{r}e^{-ix\xi}f(x)\, dx +\int_{\gamma_r}e^{-iz\xi}f(z)\, dz =
   2\pi i\sum_{\alpha\in A\cap \Omega_r}{{\operatorname{Res}}}(e^{-iz\xi}f(z),\alpha),\\
   \int_{-r}^{r}e^{-ix\xi}f(x)\, dx +\int_{\beta_r}e^{-iz\xi}f(z)\, dz =
   -2\pi i\sum_{\alpha\in A\cap
   \widetilde\Omega_r}{{\operatorname{Res}}}(e^{-iz\xi}f(z),\alpha),\end{gathered}

Athugum nú að  fyrir :math:`z=x+iy`

.. math::

  |e^{-iz\xi}|=e^{{{\operatorname{Re\, }}}(-i z\xi)}=e^{y\xi} \leq 1, \quad\text{
   ef }  y\geq 0 \text{ og } \xi\leq 0 \quad \text{ eða } 
  \quad y\leq 0 \text { og } \xi\geq 0.

Við fáum því matið

.. math::

  \begin{aligned}
   \big|\int_{\gamma_r}e^{-iz\xi}f(z)\, dz\big|
   &\leq  \max_{|z|=r}|f(z)|  \int_{\gamma_r}|e^{-iz\xi}|\, |dz|,  
   \qquad \xi<0 ,\\
   \big|\int_{\beta_r}e^{-iz\xi}f(z)\, dz\big|
   &\leq \max_{|z|=r}|f(z)|   
  \int_{\beta_r}|e^{-iz\xi}|\, |dz|,  \qquad \xi > 0.\end{aligned}

Hjálparsetning
^^^^^^^^^^^^^^

(*Jordan*).   Við höfum að

.. math::

  \begin{aligned}
   \int_{\gamma_r}|e^{-iz\xi}|\, |dz|
   &=\int_0^\pi e^{\xi r\sin \theta}\, rd\theta <\dfrac\pi{-\xi}, 
   \quad \xi<0,\\
   \int_{\beta_r}|e^{-iz\xi}|\, |dz| 
   &=\int_0^\pi e^{-\xi r\sin \theta}\, rd\theta
   <\dfrac\pi{\xi}, \quad \xi>0.\end{aligned}

--------------

Af hjálparsetningu Jordan og ójöfnunum hér fyrir framan leiðir nú:

.. \_set11.4.1:

Setning
^^^^^^^

Látum
:math:`f\in L^1({{\mathbb  R}})\cap {{\cal O}}({{\mathbb  C}}\setminus   A)`, þar sem :math:`A` er endanlegt mengi með engan punkt á
:math:`{{\mathbb  R}}` og gerum ráð fyrir að
:math:`\max_{|z|=r}|f(z)|\to 0` ef :math:`r\to +\infty`. Þá er

.. math::

  \widehat f(\xi) =
   \begin{cases}  2\pi i\sum_{\alpha\in A\cap H_+} 
   {{\operatorname{Res}}}(e^{-iz\xi}f(z),\alpha), & \xi < 0,\\
    -2\pi i\sum_{\alpha\in A\cap H_-} 
  {{\operatorname{Res}}}(e^{-iz\xi}f(z),\alpha),  & \xi > 0,
   \end{cases}

þar sem
:math:`H_+=\{z\in {{\mathbb  C}}\,;\,  {{\operatorname{Im\, }}}z>0\}`
táknar efra hálfplanið og
:math:`H_-=\{z\in {{\mathbb  C}}\,;\, {{\operatorname{Im\, }}}z<0\}`
táknar neðra hálfplanið.

--------------

Við höfum :math:`e^{-ix\xi}=\cos(x\xi)-i\sin (x\xi)` og því er

.. math::

  \widehat f(\xi)=\int_{-\infty}^{+\infty}\cos(x\xi) f(x)\, dx
   -i\int_{-\infty}^{+\infty}\sin(x\xi)f(x)\, dx, \qquad \xi\in {{\mathbb  R}}.

Ef :math:`f` er jafnstætt fall af :math:`x`, sem þýðir að
:math:`f(-x)=f(x)` fyrir öll :math:`x`, þá er :math:`\cos(x\xi)f(x)`
jafnstætt fall af :math:`x` og :math:`\sin(x\xi)f(x)` oddstætt af
:math:`x`. Þá er síðara heildið :math:`0` fyrir öll :math:`\xi` og við
höfum

.. math:: \widehat f(\xi)=2\int_0^{+\infty}\cos(x\xi)f(x) \, dx, \qquad \xi\in

Þar sem :math:`\cos(x\xi)` er jafnstætt fall af :math:`\xi` sýnir þetta
að :math:`\widehat f(\xi)` er jafnstætt fall af :math:`\xi`.

Hugsum okkur að :math:`f` sé jafnstætt og að við höfum komist að því að
:math:`\widehat f(\xi)=g(\xi)` þar sem :math:`g` er fall á jákvæða ásnum
:math:`{{\mathbb  R}}_+`. Þá þurfum við ekki að reikna neitt meira því
við höfum :math:`\widehat f(\xi)=g(|\xi|)` fyrir öll
:math:`\xi\in{{\mathbb  R}}`. Ef við höfum reiknað út
:math:`\widehat f(\xi)=h(\xi)` þar sem :math:`h` er fall á neikvæða
ásnum :math:`{{\mathbb  R}}_-`, þá fáum við að
:math:`\widehat f(\xi)=h(-|\xi|)` fyrir öll
:math:`\xi\in {{\mathbb  R}}`.

Ef hins vegar :math:`f` er oddstætt fall af :math:`x`, sem þýðir að
:math:`f(-x)=-f(x)` fyrir öll :math:`x`, þá er :math:`\cos(x\xi)f(x)`
oddstætt fall af :math:`x` og :math:`\sin(x\xi)f(x)` jafnstætt af
:math:`x`. Þá er fyrra heildið :math:`0` fyrir öll :math:`\xi` og við
höfum

.. math:: \widehat f(\xi)=-2i\int_0^{+\infty}\sin(x\xi)f(x) \, dx, \qquad \xi\in

Þar sem :math:`\sin(x\xi)` er oddstætt fall af :math:`\xi` sýnir þetta
að :math:`\widehat f(\xi)` er oddstætt fall af :math:`\xi`.

Hugsum okkur því að :math:`f` sé oddstætt og að við höfum að
:math:`\widehat f(\xi)=g(\xi)` þar sem :math:`g` er fall á jákvæða ásnum
:math:`{{\mathbb  R}}_+`. Þá gildir
:math:`\widehat f(\xi)={{\operatorname{sign}}}(\xi)g(|\xi|)` fyrir öll
:math:`\xi\in {{\mathbb  R}}`. Ef við höfum reiknað út
:math:`\widehat f(\xi)=h(\xi)` þar sem :math:`h` er fall á neikvæða
ásnum :math:`{{\mathbb  R}}_-`, þá fáum við að
:math:`\widehat f(\xi)={{\operatorname{sign}}}(\xi)h(-|\xi|)` fyrir öll
:math:`\xi\in {{\mathbb  R}}`, þar sem :math:`{{\operatorname{sign}}}`
táknar formerkisfallið :math:`{{\operatorname{sign}}}(\xi)=1` ef
:math:`\xi>0`, :math:`{{\operatorname{sign}}}(-\xi)=-1` ef :math:`\xi<0`
og :math:`{{\operatorname{sign}}}(0)=0`.
