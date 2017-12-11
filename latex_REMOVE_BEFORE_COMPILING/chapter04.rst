LEIFAREIKNINGUR
===============

Samleitnar Laurent-raðir
------------------------

Nú ætlum við að skoða föll sem eru ekki endilega fáguð á tiltekinni
hringskífu, heldur á svæðir þar sem búið er að skera út einn punkt eða
lokaða hringskífu.

Hringkragar
~~~~~~~~~~~

Mengi af gerðinni

.. math::

  A(\alpha,\varrho_1,\varrho_2)=\{z\in {{\mathbb  C}};
   \varrho_1<|z-\alpha|<\varrho_2\}

þar sem :math:`0\leq\varrho_1<\varrho_2\leq +\infty` kallast *opinn
hringkragi:hover:`hringkragi` :hover:`hringkragi!opinn`:hover:‘opinn
hringkragi‘* með miðju í :math:`\alpha`, *innri geisla:hover:‘innri
geisli hringkraga‘* :math:`\varrho_1`, og *ytri geisla:hover:‘ytri
geisli hringkraga‘* :math:`\varrho_2`, og mengi af gerðinni

.. math::

  \bar A(\alpha,\varrho_1,\varrho_2)=\{z\in {{\mathbb  C}};
   \varrho_1\leq|z-\alpha|\leq\varrho_2\}

þar sem :math:`0<\varrho_1<\varrho_2\leq +\infty` kallast *lokaður
hringkragi*:hover:`hringkragi!lokaður` með miðju í :math:`\alpha`,
*innri geisla* :math:`\varrho_1`, og *ytri geisla* :math:`\varrho_2`.

.. figure:: ./myndir/fig097.svg
    :align: center
    :alt: Hringkragi

   Mynd: Hringkragi

Laurent-setningin
~~~~~~~~~~~~~~~~~

Fágað fall á skífu er hægt að setja fram með veldaröð. Ef fall er fágað
á hringkraga þá koma til sögunnar neikvæð veldi:

Setning
^^^^^^^

(*Laurent:hover:`Laurent-setningin`*:hover:`setning!Laurent`).   Látum
:math:`X` vera opið hlutmengi af :math:`{{\mathbb  C}}` og gerum ráð
fyrir að :math:`A(\alpha,\varrho_1,\varrho_2)\subset X`. Ef
:math:`f\in {{\cal O}}(X)`, þá er unnt að skrifa :math:`f` sem

.. math::

  f(z)=\sum_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n, \qquad z\in
   A(\alpha,\varrho_1,\varrho_2).

Stuðlar raðarinnar :math:`a_n` eru gefnir með formúlunni

.. math::

  a_n=\dfrac 1{2\pi i}\int_{\partial S(\alpha,r)} \dfrac{f(\zeta)}
   {(\zeta-\alpha)^{n+1}} \, d\zeta,

og :math:`r` getur verið hvaða tala sem er á bilinu
:math:`]\varrho_1,\varrho_2[`. Röðin

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

kallast *Laurent-röð*:hover:`laurent-röð`. *Innri samleitnigeisli
:hover:‘innri samleitnigeisli
Laurent-raðar‘:hover:`Laurent-röð!samleitni`:hover:‘samleitin
Laurent-röð‘* raðarinnar :math:`\varrho_1` er skilgreindur sem neðra
mark yfir :math:`\varrho=|z-\alpha|` þannig að

.. math:: \sum_{n=-\infty}^{-1} a_n(z-{\alpha})^ n

er samleitin, *ytri samleitnigeisli:hover:‘ytri samleitnigeisli
Laurent-raðar‘* raðarinnar :math:`\varrho_2` er skilgreindur sem efra
mark yfir öll :math:`\varrho=|z-\alpha|` þannig að

.. math:: \sum_{n=0}^{+\infty}a_n(z-{\alpha})^ n

er samleitin. Ef :math:`\varrho_1<\varrho_2` þá segjum við að
Laurent-röðin sé *samleitin*. Stuðullinn :math:`a_{-1}` kallast
*leif:hover:`Laurent-röð!leif`:hover:`leif`*:hover:`leif!Laurent-raðar`
Laurent-raðarinnar og röðin

.. math:: \sum_{n=-\infty}^{-1}a_n(z-{\alpha})^ n

kallast
*höfuðhluti:hover:`höfuðhluti!Laurent-raðar`*:hover:`Laurent-röð!höfuðhluti`
hennar.

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
   0, & \alpha\not\in \Omega.\end{cases}

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
upp að punktur :math:`\alpha\in A` kallast *einangraður
punktur*:hover:`sérstöðupunktur!einangraður` í :math:`A` ef til er
:math:`\varepsilon>0` þannig að
:math:`S^ *(\alpha,\varepsilon)\cap A=\varnothing`,
þ.e.a.s. \* :math:`\alpha`  *er eini punkturinn í* :math:`A`  *sem liggur í
opnu skífunni :math:`S(\alpha,\varepsilon)`. Við segjum að mengið*
:math:`A`  *sé *dreift:hover:`dreift mengi`* ef sérhver punktur í því er
einangraður.

Höfuðhluti og leif
~~~~~~~~~~~~~~~~~~

Látum* :math:`X`  *vera opið mengi,* :math:`f\in {{\cal O}}(X)`  *og*
:math:`\alpha`  *vera einangraðan sérstöðupunkt fágaða fallsins :math:`f`.
Samkvæmt Laurent-setningunni getum við skrifað

.. math::

  f(z)= \sum_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n, \qquad z\in 
   S^ *(\alpha,\varepsilon)=A(\alpha,0,\varepsilon),

þar sem stuðlarnir eru ótvírætt ákvarðaðir. Við köllum þessa röð
*Laurent-röð fágaða fallsins:hover:`Laurent-röð!fágaðs falls`* :math:`f` 
*í punktinum* :math:`\alpha`, við köllum höfuðhluta raðarinnar
*höfuðhluta fágaða fallsins:hover:`höfuðhluti!fágaðs falls`* :math:`f`  *í
punktinum* :math:`\alpha` og við köllum leif raðarinnar *leif
fallsins:hover:`Laurent-röð!leif` :hover:`leif!falls`* :math:`f`  *í
punktinum* :math:`\alpha` og við táknum hana með

.. math:: {{\operatorname{Res}}}(f,\alpha).

Afmáanlegir sérstöðupunktar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Einangraður sérstöðupunktur :math:`{\alpha}` fágaða fallsins :math:`f`
er sagður vera *afmáanlegur*:hover:`sérstöðupunktur!afmáanlegur`, ef til
er :math:`r>0` og :math:`g\in {{\cal O}}(S({\alpha},r))` þannig að
:math:`S^\ast({\alpha},r)\subset X` og :math:`f(z)=g(z)` fyrir öll
:math:`z\in S^\ast({\alpha},r)`.

Setning
^^^^^^^

(*Riemann:hover:`Riemann-setningin`*:hover:`setning!Riemann`).   Ef
:math:`\alpha` er einangraður sérstöðupunktur fágaða fallsins :math:`f`,
og :math:`\lim_{z\to \alpha}(z-\alpha)f(z)= 0`, þá er :math:`\alpha`
afmáanlegur sérstöðupunktur

Skaut
~~~~~

Skilgreining
^^^^^^^^^^^^

Látum :math:`f` vera fágað fall á opnu mengi :math:`X` og :math:`\alpha`
vera einangraðan sérstöðupunkt fallsins :math:`f`. Við segjum að
:math:`\alpha` sé *skaut af stigi*:hover:`sérstöðupunktur!skaut`
:math:`m>0`, ef til er fágað fall :math:`g\in {{\cal O}}(U)`, þar sem
:math:`U` er grennd um :math:`\alpha`, þannig að :math:`g(\alpha)\neq 0`
og

.. math:: f(z)=\dfrac{g(z)}{(z-\alpha)^ m}, \qquad z\in U\setminus\set\alpha.

Skautin einkennast af:

Setning
^^^^^^^

Fall :math:`f` hefur skaut í :math:`\alpha` ef og aðeins ef
:math:`|f(z)|\to +\infty` ef :math:`z\to \alpha`.

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

Áður en við segjum skilið við skautin, þá skulum við víkja ögn að
stofnbrotaliðun:hover:`stofnbrotaliðun`. Við höfum gengum út frá því sem
vísum hlut, að það væri alltaf hægt að liða rætt fall í
stofnbrot:hover:`stofnbrot`. Nú skulum við sanna þetta og leiða út
formúlurnar fyrir stuðlunum í stofnbrotaliðuninni.

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

Stuðlarnir í stofnbrotaliðuninni fást nú með því að reikna liðina í
veldaröð fallanna :math:`(z-\alpha_j)^{m_j}R(z)` í punktunum
:math:`\alpha_j`, þeir eru gefnir með formúlunni

.. math::

  A_{j,\ell}=\left.\dfrac 1{\ell!}
   \bigg(\dfrac {d}{dz}\bigg)^{\ell}\bigg(
   \dfrac{P(z)}{q_j(z)}\bigg)\right|_{z=\alpha_j}, \qquad \ell=0,\dots,m_j-1,

þar sem :math:`q_j(z)=Q(z)/(z-\alpha_j)^{m_j}`.

Verulegir sérstöðupunktar
~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Einangraður sérstöðupunktur fágaða fallsins :math:`f` kallast *verulegur
sérstöðupunktur*:hover:`sérstöðupunktur!verulegur`, ef hann er hvorki
afmáanlegur sérstöðupunktur né skaut.

Hegðun fágaðra falla í grennd um verulega sérstöðupunkta er lýst með:

Setning
^^^^^^^

(*Casorati-Weierstrass:hover:`Casorati-Weierstrass-setningin`
*:hover:`setning!Casorati-Weierstrass`).   Gerum ráð fyrir að
:math:`\alpha` sé verulegur sérstöðupunktur fallsins :math:`f`. Ef
:math:`\beta\in {{\mathbb  C}}`, :math:`\varepsilon>0` og
:math:`\delta>0`, þá er til :math:`z\in S(\alpha,\delta)` þannig að
:math:`f(z)\in S(\beta,\varepsilon)`.

Leifasetningin 
---------------

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

(*Leifasetningin*:hover:`leifasetningin`).   Látum :math:`X` vera opið
hlutmengi í :math:`{{\mathbb  C}}` og látum :math:`\Omega` vera opið
hlutmengi af :math:`X` sem uppfyllir sömu forsendur og í
Cauchy-setningunni. Látum :math:`A` vera dreift hlutmengi af :math:`X`
sem sker ekki jaðarinn :math:`\partial\Omega` á :math:`\Omega`. Ef
:math:`f\in {{\cal O}}(X\setminus A)`, þá er

.. math::

  \int_{\partial\Omega}f(z)\, dz = 2\pi i \sum_{\alpha\in \Omega\cap A}
   {{\operatorname{Res}}}(f,\alpha).

Leifasetningin hefur mikla hagnýta þýðingu við útreikninga á ákveðnum
heildum. Við gerum þeim hagnýtingum skil í næsta kafla, en það sem eftir
er þessa kafla ætlum við að halda áfram að fjalla um ýmsar afleiðingar
af Cauchy-setningunni.

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
hluta af forsendum Cauchy–setningarinnar. Til viðbótar gerum við ráð
fyrir að :math:`A` sé dreift hlutmengi af :math:`X` og að
:math:`f\in {{\cal A}}(X\setminus A)`. Þá eru allir punktarnir í
:math:`A` einangraðir sérstöðupunktar fallsins :math:`f` og
leifasetningin segir okkur að

.. math::

  \int _{\partial {\Omega}} f(\zeta)\, d\zeta =2\pi i
  \sum\limits_{\alpha\in A\cap \Omega}
   {{\operatorname{Res}}}(f,\alpha).

Ef :math:`A\cap \Omega=\varnothing`, þá er summan sett :math:`0`, eins
og alltaf þegar summa yfir tóma mengið er tekin. Þetta er í fullu
samræmi við Cauchy–setninguna, því í þessu tilfelli er :math:`f` fágað í
grennd um :math:`\overline\Omega=\partial\Omega\cup \Omega` og þá er
heildið í vinstri hliðinni jafnt :math:`0`. Cauchy–formúlan er líka
sértilfelli af leifasetningunni, því ef :math:`z\in \Omega` og
:math:`\Omega\cap A=\varnothing`, þá hefur fallið
:math:`\zeta\mapsto f(\zeta)/(\zeta-z)` eitt skaut :math:`z` af stigi
:math:`\leq 1` í :math:`\Omega` og leifasetningin segir okkur að

.. math::

  \dfrac 1{2\pi i}\int_{\partial\Omega} \dfrac{f(\zeta)}{\zeta-z}\,
   d\zeta = {{\operatorname{Res}}}\bigg( \dfrac{f(\zeta)}{\zeta-z},z\bigg)=f(z).

Leif í einföldu skauti
~~~~~~~~~~~~~~~~~~~~~~

Áður en við snúum okkur að því að beita leifasetningunni til að leysa
ákveðin dæmi, þá skulum við huga að því, hvernig farið er að því að
reikna út leif :math:`{{\operatorname{Res}}}(f,\alpha)` fallsins
:math:`f` í einangraða sérstöðupunktinum :math:`\alpha`. Samkvæmt
skilgreiningu er :math:`{{\operatorname{Res}}}(f,\alpha)=a_{-1}`, þar
sem

.. math::

  f(z)=\sum\limits_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n, \qquad
   z\in S^ *(\alpha,\varepsilon),
er framsetning á* :math:`f`  *með Laurent–röð. Ef við höfum skaut af stigi*
:math:`1`  *í punktinum :math:`\alpha`, þá eru allir stuðlarnir
:math:`a_n=0`, :math:`n<-1`, í Laurent–röðinnni og við fáum

.. math::

  (z-\alpha)f(z)=\sum\limits_{n=-1}^{+\infty} a_n(z-\alpha)^{n+1} =
   \sum\limits_{n=0}^{+\infty} a_{n-1}(z-\alpha)^{n}.

Af þessari formúlu leiðir síðan

.. math::

  {{\operatorname{Res}}}(f,\alpha)=\lim_{z\to \alpha}(z-\alpha)f(z).
Leif í skauti af stigi* :math:`m>1` 
*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við skulum gera ráð fyrir að* :math:`f`  *hafi skaut af stigi* :math:`m>0`  *í
punktinum :math:`\alpha`. Samkvæmt skilgreiningu er þá til fágað fall*
:math:`g`  *í grennd* :math:`U`  *um* :math:`\alpha`  *þannig að*
:math:`g(\alpha)\neq 0`  *og :math:`f(z)=g(z)/(z-\alpha)^ m`,
:math:`z\in  U\setminus {{\{\alpha\}}}`. Við sjáum sambandið milli stuðlanna*
:math:`b_n`  *í Taylor–röð fallsins* :math:`g`  *í punktinum* :math:`\alpha` 
*og stuðlanna* :math:`a_n`  *í Laurent röð fallsins :math:`f`, út frá
formúlunni

.. math::

  f(z)=(z-\alpha)^{-m}\sum_{n=0}^{+\infty}b_n(z-\alpha)^ n=
   \sum_{n=0}^{+\infty}b_n(z-\alpha)^ {n-m}=
   \sum_{n=-m}^{+\infty}b_{n+m}(z-\alpha)^ {n},

sem gefur okkur

.. math::

  {{\operatorname{Res}}}(f,\alpha)=a_{-1}=b_{m-1}=\dfrac{g^{(m-1)}(\alpha)}{(m-1)!}.
Sértilfellið að* :math:`\alpha`  *sé skaut af fyrsta stigi, sem við
skrifuðum upp í (:ref:`Link title <11.1.3>`), er einfaldast,

.. math::

  {{\operatorname{Res}}}(f,\alpha)= g(\alpha), \qquad\qquad m=1.

Cauchy-formúla fyrir afleiður og leifasetning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cauchy–formúlan fyrir afleiður er einnig sértilfelli af
leifasetningunni, því ef* :math:`A\cap \Omega=\varnothing`  *og*
:math:`z\in \Omega`  *þá hefur fallið*
:math:`\zeta\mapsto f(\zeta)/(\zeta-z)^{n+1}`  *skaut af stigi*
:math:`\leq n+1`  *og samkvæmt (:ref:`Link title <11.1.4>`) er

.. math::

  \dfrac{n!}{2\pi i}
   \int_{\partial\Omega}\dfrac{f(\zeta)}{(\zeta-z)^{n+1}}\, d\zeta = 
   {n!} {{\operatorname{Res}}}\bigg(\dfrac{f(\zeta)}{(\zeta-z)^{n+1}},z\bigg) =
   f^{(n)}(z).

Leif af kvóta tveggja falla
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við hugsa okkur að* :math:`f`  *hafi skaut af stigi* :math:`m`  *í*
:math:`\alpha`  *og að* :math:`f`  *sé gefið í grennd um* :math:`\alpha`  *sem*
:math:`f(z)=g(z)/h(z)`, þar sem :math:`g(\alpha)\neq 0`  *og :math:`h(\alpha)=0`. Þá getum við skrifað*
:math:`h(z)=(z-\alpha)^mh_1(z)`  *þar sem* :math:`h_1(z)`  *er fágað í grennd
um* :math:`\alpha`  *og :math:`h_1(\alpha)=h^{(m)}(\alpha)/m!\neq 0`. Ef*
:math:`f`  *hefur skaut af fyrsta stigi, þá er leifin

.. math::

  {{\operatorname{Res}}}(f,\alpha)= \lim_{z\to \alpha}(z-\alpha) f(z)
   =\lim_{z\to \alpha} 
   \dfrac{(z-\alpha)g(z)}{h(z)-h(\alpha)}=\dfrac{g(\alpha)}{h{{^{\prime}}}(\alpha)}.

Þetta segir okkur, að formúlan sem við leiddum út í setningu 3.3.6, er
ekkert annað en sértilfelli af leifasetningunni, því þar gerðum við ráð
fyrir að núllstöðvar* :math:`\alpha_1,\dots,\alpha_m`  *margliðunnar*
:math:`Q`  *væru einfaldar og því gefur leifasetningin

.. math::

  \int_{\partial\Omega}\dfrac{f(\zeta)}{Q(\zeta)}\, d\zeta
   =  2\pi i\sum_{\alpha_j\in \Omega}
   {{\operatorname{Res}}}\bigg(\dfrac{f(\zeta)}{Q(\zeta)}, \alpha_j\bigg) 
   =  2\pi i\sum_{\alpha_j\in \Omega} \dfrac{f(\alpha_j)}{Q{{^{\prime}}}(\alpha_j)}.

Ef* :math:`f(z)=g(z)/h(z)`, þar sem :math:`g(\alpha)\neq 0`  *og* :math:`h`  *hefur núllstöð af stigi* :math:`m>1`  *og við skrifum
:math:`h(z)=(z-{\alpha})^mh_1(z)`, þá er

.. math::

  {{\operatorname{Res}}}(f,\alpha)=\dfrac 1{(m-1)!}\cdot
   \left.\dfrac {d^{m-1}}{dz^{m-1}}\bigg(\dfrac
   {g(z)}{h_1(z)}\bigg)\right|_{z=\alpha}. 
Leifar reiknaðar út frá stuðlum í veldaröðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Höldum nú áfram með útreikning okkar á leifum, gerum ráð fyrir að*
:math:`f=g/h`  *og

.. math::

  f(z)=\sum\limits_{n=-m}^{\infty}a_n(z-\alpha)^n, \quad
   g(z)=\sum\limits_{n=k}^{\infty}b_n(z-\alpha)^n, \quad
   h(z)=\sum\limits_{n=l}^{\infty}c_n(z-\alpha)^n,

hugsum okkur að stuðlarnir* :math:`b_n`, :math:`c_n`  *séu gefnir,*
:math:`c_l\neq 0`, :math:`b_k\neq 0`  *og að við viljum reikna út leifina*
:math:`{{\operatorname{Res}}}(f,\alpha)=a_{-1}`. Taylor–röð :math:`g`  *er
þá gefin sem margfeldi af Laurent–röð* :math:`f`  *og Taylor–röð :math:`h`,

.. math::

  \sum\limits_{n=-m}^{\infty}a_n(z-\alpha)^n
   \sum\limits_{n=l}^{\infty}c_n(z-\alpha)^n=
   \sum\limits_{n=k}^{\infty}b_n(z-\alpha)^n.

Þetta segir okkur að* :math:`-m+l=k`  *og að við fáum sambandið milli
stuðlanna með því að margfalda saman raðirnar í vinstri hliðinni

.. math::

  \begin{gathered}
   a_{-m}c_l=b_k,\\
   a_{-m+1}c_l+a_{-m}c_{l+1}=b_{k+1},\\
   a_{-m+2}c_l+a_{-m+1}c_{l+1}+a_{-m}c_{l+2}=b_{k+2},\\
   \qquad \vdots\qquad\qquad\qquad\vdots\\
   a_{-2}c_l+a_{-3}c_{l+1}+\cdots+a_{-m}c_{l+m-2}=b_{k+m-2}\\
   a_{-1}c_l+a_{-2}c_{l+1}+\cdots+a_{-m}c_{l+m-1}=b_{k+m-1}.\end{gathered}

Fyrst* :math:`c_l\neq 0`, þá fáum við :math:`m`  *skrefa rakningarformúlu
fyrir* :math:`a_{-m}, a_{-m+1},\dots, a_{-1}`  *og í síðasta skrefinu er leif* :math:`f`  *í*
:math:`\alpha`  *fundin,

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
Ef engin af aðferðunum, sem við höfum verið að fjalla um hér, dugir til
að finna leifina þá er ekkert annað að gera en að reikna hana út frá
formúlunni sem við leiddum út í Laurent–setningunni,

.. math::

  {{\operatorname{Res}}}(f,\alpha) = \dfrac 1{2\pi i}\int_{\partial
   S(\alpha,\varepsilon)} f(\zeta)\, d\zeta,

þar sem við veljum geislann* :math:`\varepsilon`  *í hringnum nógu lítinn.

Heildi yfir einingarhringinn
----------------------------

Við skulum gera ráð fyrir að* :math:`f`  *sé fall af tveimur breytistærðum*
:math:`(x,y)`  *og að* :math:`f`  *sé skilgreint í grennd um
einingarhringinn, :math:`x^ 2+y^ 2=1`. Við fáum nú endurbót á
aðferðinni, sem við leiddum út eftir setningu 3.3.6. Eins og þar athugum
við, að ef* :math:`z`  *er á einingarhringnum, :math:`z=e^{i\theta}`, þá
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

ef til er opin grennd* :math:`X`  *um lokuðu einingarskífuna*
:math:`\overline S(0,1)`  *og dreift mengi* :math:`A`  *þannig að fallið*
:math:`z\mapsto f\big({(z^ 2+1)}/{(2z)},{(z^ 2-1)}/{(2iz)}\big)/(iz)`  *sé fágað á
:math:`X\setminus A`.

Heildi yfir raunásinn
---------------------

Nú ætlum við að snúa okkur að heildum af gerðinni

.. math::

  I=\int_{-\infty}^{+\infty}f(x) \, dx 
þar sem fallið* :math:`f`  *er fágað í grennd um :math:`{{\mathbb  R}}`.
Hugsum okkur fyrst að*
:math:`f\in {{\cal O}}({{\mathbb  C}}\setminus A)`, þar sem :math:`A`  *er
dreift mengi. Aðferðin byggir á því að athuga að

.. math:: I=\lim_{r\to +\infty}\int_{-r}^ r f(x)\, dx,

ef heildið (:ref:`Link title <11.3.1>`) er samleitið. Leifasetningin gefur okkur þá

.. math::

  \int_{-r}^{r}f(x)\, dx +\int_{\gamma_r}f(z)\, dz =
   2\pi i\sum_{\alpha\in A\cap \Omega_r}{{\operatorname{Res}}}(f,\alpha)

og jafnframt

.. math::

  \int_{-r}^{r}f(x)\, dx +\int_{\beta_r}f(z)\, dz =
   -2\pi i\sum_{\alpha\in A\cap \widetilde\Omega_r}{{\operatorname{Res}}}(f,\alpha),

þar sem* :math:`\Omega_r`  *og* :math:`\widetilde\Omega_r`  *eru
hálfskífurnar á myndinni.

.. figure:: ./myndir/fig101.svg
    :align: center
    :alt: Hálfskífur í efra og neðra hálfplani

   Mynd: Hálfskífur í efra og neðra hálfplani

Ef unnt er að sýna fram á að önnur hvor summan í hægri hliðunum hafi
markgildi ef* :math:`r\to +\infty`  *og að tilsvarandi vegheildi

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

þar sem*
:math:`H_+=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z>0\}`  *táknar
efra hálfplanið og*
:math:`H_-=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z<0\}`  *táknar
neðra hálfplanið.

Lítum nú á tilfellið að* :math:`f(x)=P(x)/Q(x)`  *sé rætt fall, að*
:math:`P`  *og* :math:`Q`  *séu margliður með
:math:`{{\operatorname{stig}}}\, P\leq {{\operatorname{stig}}}\, Q-2`,
og að* :math:`Q`  *hafi engar núllstöðvar á :math:`{{\mathbb  R}}`. Auðvelt
er að sannfæra sig um að til er fasti* :math:`C`  *þannig að

.. math:: |f(z)|\leq \dfrac C{r^ 2},

ef* :math:`|z|=r`  *og* :math:`r`  *er það stórt að allar núllstöðvar*
:math:`Q`  *liggja í* :math:`S(0,r-1)`. Lengd veganna :math:`\gamma_r`  *og*
:math:`\beta_r`  *er :math:`\pi r`, svo við fáum

.. math:: |\int_{\gamma_r}f(z)\, dz|\leq \pi C/r\to 0, \qquad r\to +\infty,

og sama mat fæst fyrir heildið af* :math:`f(z)`  *yfir :math:`\beta_r`.
Niðurstaðan verður því að

.. math::

  \int\limits_{-\infty}^ {+\infty} f(x)\, dx =
   2\pi i\sum_{\alpha\in {\cal N}(Q)\cap H_+}{{\operatorname{Res}}}\big(f,\alpha)
   =-2\pi i\sum_{\alpha\in {\cal N}(Q)\cap H_-}{{\operatorname{Res}}}\big(f,\alpha),

þar sem* :math:`{\cal N}(Q)`  *er núllstöðvamengi :math:`Q`.*
*