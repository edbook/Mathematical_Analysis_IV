
Fourier–ummyndun
================

**Samantekt.** Í þessum kafla fjöllum við um frumatriði um
Fourier–ummyndun, en hagnýtingar hennar í eðlisfræði og verkfræði eru
ótalmargar, til dæmis í rafsegulfræði, skammtafræði, tímaraðagreiningu
og upplýsinga- og merkjafræði. Við tökum fyrir það verkefni að finna
sérlausnir á afleiðujöfnum með fastastuðla, þar sem hægri hliðin er
heildanlegt fall á öllu :math:`{{\mathbb  R}}`. Við sjáum hvernig
Fourier-ummyndun tengist Laplace-ummyndun og leiðum út formúlu fyrir
andhverfa Laplace-ummyndun. Við tengjum Fourier-ummyndun við
leifareikning og sjáum hvernig andhverf Laplace-ummyndun á sér einfalda
formúlu þegar Laplace-mynd falls er fágað fall utan við endanlegt mengi.

Inngangur
---------

Byrjum á því að líta enn einu sinni á vandamálið að að finna
:hover:`sérlausn` á venjulegri afleiðujöfnu með fastastuðla

.. math:: P(D)u=(a_mD^ m+\cdots+a_1D+a_0)u=f(x).

Við sáum í kaflanum um Fourier-raðir hvernig hægt er að fá lausn :math:`u(x)` sem gefin
er með Fourier-röð ef fallið :math:`f` er lotubundið og gefið með
Fourier-röð. Nú ætlum við að gefa okkur að fallið :math:`f` sé gefið með
heildi,

.. math::

  f(x)= 
   \int\limits_{-\infty}^{+\infty} e^{ix\xi}F(\xi) \, d\xi,

þar sem :math:`|F|` er heildanlegt á :math:`{{\mathbb  R}}`. Þá er
eðlilegt að leita að lausn af sömu gerð

.. math:: u(x)=\int\limits_{-\infty}^{+\infty} e^{ix\xi} U(\xi)\, d\xi.

Ef við gefum okkur að við megum taka afleiður af :math:`u` með því að
deilda undir heildið, þá fáum við

.. math::

  u{{^{\prime}}}(x)=\int\limits_{-\infty}^{+\infty}(i\xi) e^{ix\xi}
   U(\xi)\, d\xi, \ \ 
   u''(x)=\int\limits_{-\infty}^{+\infty}(i\xi)^2 e^{ix\xi}
   U(\xi)\, d\xi, 
   \dots, 
   u^{(k)}(x)=\int\limits_{-\infty}^{+\infty}(i\xi)^ k e^{ix\xi}
   U(\xi)\, d\xi.

Þar með

.. math::

  \begin{aligned}
   P(D)u(x)
   &=a_mu^{(m)}(x)+\cdots+a_1u'(x)+a_0u(x)\\ 
   &=
   \int\limits_{-\infty}^{+\infty} 
   \big(a_m(i{\xi})^m+\cdots+a_1(i{\xi})+a_0\big)e^{ix\xi}U({\xi})\, d{\xi}\\
   &=\int\limits_{-\infty}^{+\infty} e^{ix\xi} P(i\xi)U(\xi)\, d\xi
   =\int\limits_{-\infty}^{+\infty} e^{ix\xi} F(\xi)\, d\xi = f(x).\end{aligned}

Af þessu er ljóst að við eigum að taka

.. math:: U(\xi)=\dfrac {F(\xi)}{P(i\xi)}, \qquad \xi\in {{\mathbb  R}}.

Þessi formúla hefur merkingu í sérhverjum punkti :math:`\xi` þar sem
:math:`P(i\xi)\neq 0` og einnig í punktum :math:`\xi=\alpha` þar sem
:math:`P(i\alpha)=0`, :math:`P(i{\xi})=({\xi}-{\alpha})^kQ({\xi})`,
:math:`Q({\alpha})\neq 0` og markgildið

.. math:: \lim_{{\xi}\to{\alpha}} \dfrac{F(\xi)}{(\xi-{\alpha})^k}

er til. Hér höfum við fundið samband milli fallanna :math:`F` og
:math:`U` og formúlu fyrir lausninni

.. math::

  u(x)=
   \int\limits_{-\infty}^{+\infty} 
   e^{ix\xi} \dfrac {F(\xi)}{P(i\xi)}\, d{\xi}, \qquad x\in {{\mathbb  R}}.

Viðfangsefni kaflans er að finna samband milli fallanna :math:`f` og
:math:`F` og jafnframt að kanna skilyrði á :math:`f` sem gefa okkur
framsetningu af gerðinni 

.. math::

  f(x)= 
   \int\limits_{-\infty}^{+\infty} e^{ix\xi}F(\xi) \, d\xi.

Skilgreiningar og nokkrar reiknireglur
--------------------------------------

Rúm heildanlegra falla :math:`L^1({{\mathbb  R}})`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við látum :math:`L^1({{\mathbb  R}})` tákna mengi allra falla :math:`f`
þannig að :math:`|f|` er heildanlegt á :math:`{{\mathbb  R}}`. Af
formúlunum

.. math::

  \int_{-\infty}^{+\infty}|f(x)+g(x)|\, dx
   \leq 
   \int_{-\infty}^{+\infty}|f(x)|\, dx
   +
   \int_{-\infty}^{+\infty}|g(x)|\, dx

og

.. math::

  \int_{-\infty}^{+\infty}|\alpha f(x)|\, dx
   =
   |\alpha|\int_{-\infty}^{+\infty}|f(x)|\, dx

leiðir að :math:`L^1({{\mathbb  R}})` er vigurrúm.

Skilgreining á Fourier-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fyrir sérhvert fall :math:`f\in L^1({{\mathbb  R}})` skilgreinum við
fallið

.. math::

  {{\cal F}}f(\xi)=\int_{-\infty}^{+\infty} e^{-ix\xi}f(x) \, dx, \qquad
    \xi\in {{\mathbb  R}}.

Fallið :math:`{{\cal F}}f` köllum við *Fourier–mynd* fallsins :math:`f`
og táknum hana einnig með :math:`\widehat f` og
:math:`{{\cal F}}{{\{f\}}}`. Vörpunina :math:`{{\cal F}}` sem skilgreind
er á :math:`L^1({{\mathbb  R}})` og úthlutar fallinu :math:`f`
Fourier-mynd sinni :math:`{{\cal F}}f` köllum við *Fourier–ummyndun*.
Hún er einnig kölluð *Fourier–færsla* og *Fourier–vörpun*.

Því miður er skilgreiningin á Fourier–ummyndun ekki stöðluð. Ef
lesandinn opnar einhverja bók um efnið getur hann átt von á því að sjá
hana skilgreinda með einni af formúlunum

.. math::

  \begin{gathered}
   \int_{-\infty}^{+\infty}e^{ix\xi}f(x) \, dx, \quad
   \dfrac 1{2\pi}\int_{-\infty}^{+\infty}e^{-ix\xi}f(x) \, dx,\quad
   \dfrac 1{2\pi}\int_{-\infty}^{+\infty}e^{ix\xi}f(x) \, dx,\quad\\
   \dfrac 1{\sqrt{2 \pi}}\int_{-\infty}^{+\infty}e^{-ix\xi}f(x) \, dx, \quad
   \int_{-\infty}^{+\infty}e^{-2\pi ix\xi}f(x) \, dx,\end{gathered}

eða jafnvel á einhvern enn annan hátt. Ef tekin er önnur skilgreining á
Fourier-mynd en sú sem við höfum, þá verða reiknireglur og setningar að
sjálfsögðu að einhverju leyti öðruvísi en hjá okkur. Auðvelt er að átta
sig á því í hverju munurinn liggur.

Nokkur sýnidæmi
~~~~~~~~~~~~~~~

.. _synokkurfouriersynidaemi:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Við skulum byrja á því að reikna út nokkrar Fourier-myndir sem eiga
eftir að koma fyrir í útreikningum okkar síðar. Við látum :math:`H`
tákna *Heaviside-fallið*, sem skilgreint er með

.. math:: H(x)=\begin{cases} 1, & x\geq 0,\\ 0, &x<0.\end{cases}

\(i) Lítum fyrst á fallið :math:`f(x)=H(x)e^{\alpha x}`, þar sem
:math:`\alpha\in {{\mathbb  C}}` og :math:`{{\operatorname{Re\, }}}\alpha <0`. Þá er
:math:`f` heildanlegt og

.. math::

  {{\cal F}}\{H(x)e^{\alpha x}\}(\xi)=
   \int_0^\infty e^{-ix\xi+\alpha x}\, dx=
   \left[\dfrac {e^{-ix\xi+\alpha x}}{-i\xi+\alpha}\right]_0^\infty=
   \dfrac 1{i\xi-\alpha}.

.. figure:: ./myndir/fig051.svg
    :align: center
    :alt: Fourier-mynd af veldisvísisfalli á :math:`{{\mathbb  R}}_+`

    Mynd: Fourier-mynd af veldisvísisfalli á :math:`{{\mathbb  R}}_+`

\(ii) Lítum nú á fallið :math:`f(x)=H(-x)e^{\alpha x}`, þar sem
:math:`\alpha\in {{\mathbb  C}}` og :math:`{{\operatorname{Re\, }}}\alpha >0`. Það er
heildanlegt og

.. math::

  {{\cal F}}\{H(-x)e^{\alpha x}\}(\xi)=
   \int_{-\infty}^0 e^{-ix\xi+\alpha x}\, dx=
   \left[\dfrac {e^{-ix\xi+\alpha x}}{-i\xi+\alpha}\right]_{-\infty}^0=
   \dfrac {-1}{i\xi-\alpha}.

.. figure:: ./myndir/fig052.svg
    :align: center
    :alt: Fourier-mynd af veldisvísisfalli á :math:`{{\mathbb  R}}_-`

    Mynd: Fourier-mynd af veldisvísisfalli á :math:`{{\mathbb  R}}_-`

\(iii) Fallið :math:`f(x)=e^{-\alpha|x|}`, þar sem
:math:`{{\operatorname{Re\, }}}\alpha >0`, er heildanlegt og það má
skrifa sem

.. math:: e^{-\alpha|x|}=H(x)e^{-\alpha x}+H(-x)e^{\alpha x}, \qquad x\neq 0,

Fourier-ummyndunin er augljóslega línuleg vörpun, svo við fáum

.. math::

  \begin{aligned}
   {{\cal F}}\{e^{-\alpha|x|}\}(\xi)&=
   {{\cal F}}\{H(x)e^{-\alpha x}\}(\xi)+{{\cal F}}\{H(-x)e^{\alpha x}\}(\xi)\\
   &=\dfrac 1{i\xi+\alpha}-\dfrac 1{i\xi-\alpha}
   =\dfrac {2\alpha}{\alpha^2+\xi^2}.\end{aligned}

.. figure:: ./myndir/fig053.svg
    :align: center
    :alt: Fourier-mynd :math:`e^{-\alpha|x|}`

    Mynd: Fourier-mynd :math:`e^{-\alpha|x|}`

\(iv) Fallið :math:`f(x)={{\operatorname{sign}}}(x)e^{-\alpha|x|}`, þar
sem :math:`{{\operatorname{Re\, }}}\alpha>0` og
:math:`{{\operatorname{sign}}}` táknar :hover:`formerkisfallið, formerkisfall`

.. math:: {{\operatorname{sign}}}(x)=\begin{cases} 1, &x>0,\\ 0, &x=0,\\ -1, &x<0,\end{cases}

er unnt að skrifa sem

.. math:: {{\operatorname{sign}}}(x)e^{-\alpha|x|}=H(x)e^{-\alpha x}-H(-x)e^{\alpha x}.

Nú notfærum við okkur að :math:`{{\cal F}}` er línuleg vörpun og fáum

.. math::

  {{\cal F}}\{{{\operatorname{sign}}}(x)e^{-\alpha|x|}\}(\xi)=
   \dfrac 1{i\xi+\alpha}+\dfrac 1{i\xi-\alpha}=\dfrac {-2i\xi}{\alpha^2+\xi^2}.

.. figure:: ./myndir/fig054.svg
    :align: center
    :alt: Fourier-mynd :math:`{{\operatorname{sign}}}(x)e^{-\alpha|x|}`

    Mynd: Fourier-mynd :math:`{{\operatorname{sign}}}(x)e^{-\alpha|x|}`

.. end-toggle::

Fourier-mynd þéttifalls stöðluðu normaldreifingarinnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rifjum upp að

.. math::

  \int\limits_{-\infty}^{+\infty}
   e^{-x^ 2}\, dx =\sqrt \pi.

Með skipti á breytistærðum :math:`y=\sqrt \alpha x` fáum við síðan að

.. math::

  \sqrt{\tfrac \alpha\pi} \int\limits_{-\infty}^{+\infty}
   e^{-\alpha x^ 2}\, dx =1

fyrir öll :math:`\alpha>0`. Rifjum upp að fallið :math:`\varphi_{0,1}`
sem gefið er með

.. math:: \varphi_{0,1}(x)=\dfrac{e^{-\frac 12 x^2}}{\sqrt{2\pi}}, \qquad x\in {{\mathbb  R}},

er þéttifall *stöðluðu normaldreifingarinnar* og

.. math::

  \varphi_{\mu,\sigma}(x)=\dfrac {e^{-\frac 12
     (x-\mu)^2/\sigma^2}}{\sqrt{2\pi}\, \sigma}, 
   \qquad x\in {{\mathbb  R}},

er þéttifall normaldreifingar með *væntigildi* :math:`\mu` og
*staðalfrávik* :math:`\sigma`.

.. _syfouriermyndthettifallsstodludunormaldreifingarinnar:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

:math:`{{\cal F}}\{\varphi_{0,1}\}(\xi)={{\cal F}}\{\tfrac 1{\sqrt{2\pi}}e^{-\frac 12 x^2}\} (\xi)=e^{-\frac 12\xi^2}`, :math:`\xi\in {{\mathbb  R}}`.

--------------

**Lausn:** Við höfum

.. math::

  \begin{aligned}
   {{\cal F}}\{\tfrac 1{\sqrt{2\pi}}e^{-\frac 12 x^2}\}(\xi)
   &=\dfrac 1{\sqrt{2\pi}}\int_{-\infty}^{+\infty}
   e^{-i x\xi}e^{-\frac 12 x^2}\, dx
   =\dfrac 1{\sqrt{2\pi}}\int_{-\infty}^{+\infty}
   e^{-\frac 12 x^2-i x\xi}\, dx\\
   &=\dfrac 1{\sqrt{2\pi}}\int_{-\infty}^{+\infty}
   e^{-\frac 12 (x+i\xi)^2-\frac 12\xi^2}\, dx
   =\bigg(\dfrac 1{\sqrt{2\pi}}\int_{-\infty}^{+\infty}
   e^{-\frac 12 (x+i\xi)^2}\, dx\bigg)
   e^{-\frac 12\xi^2}.\end{aligned}

Til þess að staðfesta formúluna fyrir
:math:`{{\cal F}}\{\tfrac 1{\sqrt{2\pi}}e^{-\frac 12 x^2}\}` þurfum við
einungis að sýna að heildið

.. math:: I(y)= \int\limits_{-\infty}^{+\infty} e^{-\frac 12 (x+iy)^ 2}\, dx

sé óháð :math:`y` og þar með :math:`I(y)=I(0)=\sqrt{2\pi}`. Við metum
fyrst afleiðuna af heildisstofninum

.. math::

  |\partial_y e^{-(x+iy)^ 2}|=
   |-2i(x+iy) e^{-x^ 2+y^ 2 -2ixy}|= 2\sqrt{x^ 2+y^ 2}
   e^{-x^ 2+y^ 2}.

Ef :math:`y` liggur í takmörkuðu bili :math:`[-a,a]` á
:math:`{{\mathbb  R}}` þá sjáum við að

.. math::

  |\partial_y e^{-(x+iy)^ 2}|\leq 
    2\sqrt{x^ 2+a^ 2} e^{-x^ 2+a^ 2}.

Hægri hliðin er heildanlegt fall og setning Lebesgue í viðauka C segir
okkur að við getum tekið afleiðu af :math:`I` með því að deilda með
tilliti til :math:`y` undir heildið. Þá fæst

.. math::

  I{{^{\prime}}}(y)= \int_{-\infty}^{+\infty} \partial_ye^{-(x+iy)^2}\, dx
   =\int_{-\infty}^{+\infty} i\partial_xe^{-(x+iy)^2}\, dx
   =\left[ ie^{-(x+iy)^2}\right]_{-\infty}^{+\infty}=0.

Þar með er :math:`I(y)=I(0)=\sqrt{2 \pi}` fyrir öll
:math:`y\in {{\mathbb  R}}`. 

.. end-toggle::

Regla (i): Fourier-ummyndun er línuleg vörpun.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tökum tvö föll :math:`f,g\in L^1({{\mathbb  R}})` og tvær tölur
:math:`\alpha,\beta\in {{\mathbb  C}}`. Heildun er línuleg aðgerð og því
fáum við

.. math::

  \int_{-\infty}^{+\infty} e^{-ix\xi}\big(\alpha f(x)+\beta g(x)\big)\, dx
   =
   \alpha \int_{-\infty}^{+\infty} e^{-ix\xi} f(x) \, dx
   +\beta \int_{-\infty}^{+\infty} e^{-ix\xi} g(x)\, dx.

Samkvæmt skilgreiningunni á Fourier-myndum falla er þetta formúlan

.. math::

  {{\cal F}}\{\alpha f+\beta
   g\}(\xi)=\alpha{{\cal F}}\{f\}(\xi)+\beta{{\cal F}}\{g\}(\xi), \qquad f,g\in
   L^1({{\mathbb  R}}), \quad \alpha,\beta\in{{\mathbb  C}},

og hún segir að *Fourier-ummyndun* :math:`{{\cal F}}` sé línuleg vörpun
frá :math:`L^1({{\mathbb  R}})` með gildi í rúmi allra tvinngildra falla
á :math:`{{\mathbb  R}}`.

Regla (ii): :math:`{{\cal F}}\{f(\alpha x)\}(\xi)= (1/{|\alpha|}){{\cal F}}\{f\}(\xi/\alpha)`,  :math:`\alpha\in {{\mathbb  R}}`  :math:`\alpha\neq 0`, :math:`\xi\in {{\mathbb  R}}`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tökum nú :math:`\alpha\in {{\mathbb  R}}`, :math:`\alpha\neq 0`.
Breytistærðaskiptin :math:`y=\alpha x` í heildinu fyrir Fourier-mynd
fallsins :math:`f(\alpha x)` eru

.. math::

  \int_{-\infty}^{+\infty} e^{-ix\xi}f(\alpha  x) \, dx
   =\int_{-\infty}^{+\infty} e^{-i(y/\alpha)\xi}f(y) \tfrac 1{|\alpha|}\, dx
   =\int_{-\infty}^{+\infty} e^{-iy(\xi/\alpha)}f(y) \tfrac 1{|\alpha|}\, dy

sem er ekkert annað en formúlan

.. math::

  {{\cal F}}\{f(\alpha x)\}(\xi)=
   (1/{|\alpha|}){{\cal F}}\{f\}(\xi/\alpha), \qquad \xi\in {{\mathbb  R}}.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

:math:`{{\cal F}}\{e^{-\varepsilon x^2}\}=\sqrt{\dfrac     \pi \varepsilon} e^{-\xi^2/(4\varepsilon)}`.

*Lausn*:   Í síðasta sýnidæmi reiknuðum við út Fourier-mynd
þéttifallsins fyrir stöðluðu normaldreifinguna. Af þeirri formúlu leiðir
nú

.. math::

  {{\cal F}}\{e^{-\varepsilon x^2}\}(\xi)
   =\sqrt{2\pi} {{\cal F}}\{\tfrac 1{\sqrt{2\pi}} e^{-\frac 12(\sqrt{2\varepsilon} x)^2}\}(\xi)
   =\dfrac{\sqrt{2\pi}}{\sqrt{2\varepsilon}} 
   e^{-\frac 12(\xi/\sqrt{2\varepsilon})^2}
   =\sqrt{\dfrac \pi \varepsilon}
   e^{-\xi^2/(4\varepsilon)}.

.. end-toggle::

Regla (iii): :math:`{{\cal F}}\{f(x-\alpha)\}(\xi) =e^{-i\alpha\xi}{{\cal F}}\{f\}(\xi)`, :math:`\alpha\in {{\mathbb  R}}`, :math:`\xi\in {{\mathbb  R}}`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tökum :math:`\alpha\in {{\mathbb  R}}`, hliðrum fallinu :math:`f` um
:math:`\alpha` og reiknum síðan út Fourier-mynd,

.. math::

  \int_{-\infty}^{+\infty} e^{-ix\xi}f(x-\alpha) \, dx
   =\int_{-\infty}^{+\infty} e^{-i(y+\alpha)\xi}f(y) \, dy
   = e^{-i\alpha\xi}\int_{-\infty}^{+\infty} e^{-i y\xi}f(y) \, dy.

Hér stendur formúlan

.. math::

  {{\cal F}}\{f(x-\alpha)\}(\xi)=
   e^{-i\alpha\xi}{{\cal F}}\{f\}(\xi), \qquad \xi\in {{\mathbb  R}}.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Þéttifall normaldreifingar með væntigildi :math:`\mu` og staðalfrávik
:math:`\sigma` er

.. math::

  \varphi_{\mu,\sigma}(x)=\tfrac 1{\sqrt{2\pi}\, \sigma} 
   e^{-\frac  12((x-\mu)/\sigma)^2}=
   \dfrac 1\sigma \varphi_{0,1}((x-\mu)/\sigma)

Reiknireglur (ii), (iii) og :ref:`sýnidæmi <syfouriermyndthettifallsstodludunormaldreifingarinnar:>` gefa okkur að
Fourier-mynd þess er

.. math::

  \begin{aligned}
   {{\cal F}}\{\varphi_{\mu,\sigma}(x)\}(\xi)
   &=\dfrac 1\sigma {{\cal F}}\{\varphi_{0,1}((x-\mu)/\sigma)\}(\xi)
   =\dfrac 1\sigma e^{-i\mu\xi}{{\cal F}}\{\varphi_{0,1}(x/\sigma)\}(\xi)\\
   &=e^{-i\mu\xi}{{\cal F}}\{\varphi_{0,1}(x)\}(\sigma\xi)
   =e^{-i\mu\xi-\frac 12 \sigma^2\xi^2}.\end{aligned}

.. end-toggle::

Regla (iv): :math:`{{\cal F}}\{e^{i\alpha x}f(x)\}(\xi)={{\cal F}}\{f\}(\xi-\alpha)`, :math:`\alpha\in {{\mathbb  R}}`, :math:`\xi\in {{\mathbb  R}}`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tökum :math:`\alpha\in {{\mathbb  R}}` og lítum á Fourier-mynd fallsins
:math:`e^{i\alpha x}f(x)`,

.. math::

  {{\cal F}}\{e^{i\alpha x}f(x)\}(\xi)
   =
   \int_{-\infty}^{+\infty} e^{-ix\xi}e^{i\alpha x}f(x) \, dx
   =\int_{-\infty}^{+\infty} e^{-ix(\xi-\alpha)}f(x) \, dx
   ={{\cal F}}\{f\}(\xi-\alpha).

Regla (v): :math:`{{\cal F}}\{\overline{f(x)}\}(\xi) =\overline{{{\cal F}}\{f\}(-\xi)}`, :math:`\xi\in {{\mathbb  R}}`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú tökum við Fourier-myndina af :math:`\overline {f(x)}`,

.. math::

  {{\cal F}}\{\overline{f(x)}\}(\xi)
   =\int_{-\infty}^{+\infty} e^{-ix\xi}\overline{f(x)} \, dx
   =\int_{-\infty}^{+\infty} \overline{e^{ix\xi}f(x)} \, dx
   =\overline{\int_{-\infty}^{+\infty} e^{ix\xi}f(x)} \, dx
   =\overline{{{\cal F}}\{f\}(-\xi)}.

Regla (vi): :math:`{{\cal F}}f(\xi)=\overline{{{\cal F}}f(-\xi)}`, :math:`\xi\in{{\mathbb  R}}`, ef :math:`f` er raungilt.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fall :math:`f` er raungilt þá og því aðeins að
:math:`f(x)=\overline{f(x)}` gildi um öll :math:`x\in {{\mathbb  R}}`.
Við fáum því sem sértilfelli af reglu (v) að

.. math::

  {{\cal F}}f(\xi)=\overline{{{\cal F}}f(-\xi)}, \qquad 
   \xi\in{{\mathbb  R}}.

Regla (vii): :math:`\displaystyle{{\cal F}}f(\xi) =2\int_0^{+\infty}\cos(x\xi)f(x)\, dx`, :math:`\xi\in {{\mathbb  R}}`, ef :math:`f` er jafnstætt.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum

.. math::

  {{\cal F}}f({\xi})=
   \widehat f(\xi) = \int_{-\infty}^{+\infty} \cos(x\xi) f(x) \, dx
   -i\int_{-\infty}^{+\infty} \sin (x\xi) f(x) \, dx.

Ef :math:`f` er jafnstætt, þá er seinni heildisstofninn oddstætt fall af
:math:`x`, því :math:`\sin` er oddstætt. Þar með er seinna heildið 0.
Fyrri heildisstofninn er hins vegar jafnstætt fall og því er heildið
yfir :math:`{{\mathbb  R}}` tvöfalt heildið yfir
:math:`{{\mathbb  R}}_+`,

.. math::

  {{\cal F}}f(\xi)
   =2\int_0^{+\infty}\cos(x\xi)f(x)\, dx, \qquad \xi\in {{\mathbb  R}}.

Regla (viii): :math:`\displaystyle{{\cal F}}f(\xi) =-2i\int_0^{+\infty}\sin(x\xi)f(x)\, dx`, ef :math:`f` er oddstætt.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við gerum ráð fyrir að :math:`f` sé oddstætt og lítum aftur á heildin
í reglu (vii), þá sjáum við að fyrri heildistofninn er oddstætt
fall af :math:`x` en sá seinni jafnstætt fall. Fyrra heildið er því
:math:`0` og seinna heildið er tvöfalt heildið yfir
:math:`{{\mathbb  R}}_+`,

.. math::

  {{\cal F}}f(\xi)
   =-2i\int_0^{+\infty}\sin(x\xi)f(x)\, dx, \qquad \xi\in {{\mathbb  R}}.

Regla (ix): :math:`{{\cal F}}\{f^{(k)}\}(\xi)=(i\xi)^k{{\cal F}}\{f\}(\xi)`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum nú ráð fyrir að :math:`f` sé samfellt deildanlegt og að bæði
:math:`f` og :math:`f{{^{\prime}}}` séu í :math:`L^1({{\mathbb  R}})`.
Við þurfum þá að draga þá ályktun að
:math:`\lim_{|x|\to +\infty} f(x)=0`. Við athugum að til er fasti

.. math:: f(x)=C+\int_{-\infty}^x f'(y)\, dy,

þar sem :math:`C` er fasti, því föllin sitt hvoru megin
jafnaðarmerkisins hafa sömu afleiðu. Fastinn getur ekki verið neitt
annað en :math:`0`, því fyrst :math:`f'` er heildanlegt, þá stefnir
heildið í hægri hliðinni á :math:`0` ef :math:`x\to -\infty` og þar með
er :math:`\lim_{x\to -\infty}f(x)=C`. Ef :math:`C\neq 0`, þá er til
:math:`R_0` þannig að :math:`|f(x)|\geq \tfrac 12 |C|` ef
:math:`x\leq R_0`. Þar með er

.. math::

  \int_{-R}^{R_0}|f(x)|\, dx \geq \tfrac 12 |C|\int_{-R}^{R_0}\, dx
   =\tfrac 12 |C|(R_0+R)

Ef til látum :math:`R\to +\infty`, þá stefnir vinstri hliðin á heildið
af :math:`|f|` yfir :math:`]-\infty,R_0]`, en hægri hliðin á
:math:`+\infty`. Það er mótsögn við það að :math:`f` er heildanlegt og
því verður :math:`C=0` að gilda. Niðurstaðan verður síðan að
:math:`\lim_{x\to -\infty}f(x)=0`.

Við höfum einnig að

.. math:: f(x)=C-\int_x^{+\infty} f'(y)\, dy.

og með sömu rökum og hér að framan ályktum við að :math:`C=0` og
:math:`\lim_{x\to +\infty}f(x)=0`.

Við beitum nú hlutheildun

.. math::

  \begin{aligned}
   \int_{-\infty}^{+\infty}e^{-ix\xi}f{{^{\prime}}}(x) \, dx
   =\bigg[e^{-ix\xi}f(x)\bigg]_{-\infty}^{+\infty}-
   \int_{-\infty}^{+\infty}(-i\xi)e^{-ix\xi}f(x) \, dx.\end{aligned}

Fyrst :math:`\lim_{x\to \pm\infty}f(x)=0`, þá leiðir af þessu að

.. math:: {{\cal F}}\{f{{^{\prime}}}\}(\xi)=i\xi{{\cal F}}\{f\}(\xi), \qquad \xi\in {{\mathbb  R}}.

Ef :math:`f\in C^m({{\mathbb  R}})` og
:math:`f,f{{^{\prime}}},\dots,f^{(m)}\in L^1({{\mathbb  R}})`, þá fæst
að fyrir :math:`k=0,1,2,\dots,m`

.. math::

  {{\cal F}}\{f^{(k)}\}(\xi)= 
   (i\xi){{\cal F}}\{f^{(k-1)}\}(\xi)=\cdots
   =(i\xi)^k{{\cal F}}\{f\}(\xi),  \qquad \xi\in {{\mathbb  R}},

Af þessari formúlu leiðir síðan að um sérhvern afleiðuvirkja
:math:`P(D)=a_mD^ m+\cdots+a_1D+a_0` með fastastuðla gildir

.. math:: {{\cal F}}\{P(D)f\}(\xi)= P(i\xi){{\cal F}}\{f\}(\xi), \qquad \xi\in {{\mathbb  R}}.

Regla (x): :math:`{\cal F}\{x^jf(x)\}(\xi)=i^j\dfrac{d^j}{d\xi^j}{\cal F}\{f\}(\xi)`, :math:`\xi\in {\mathbb  R}`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum nú ráð fyrir að föllin :math:`f` og :math:`xf` séu í
:math:`L^1({{\mathbb  R}})` og lítum á fallið
:math:`\varphi(x,\xi)=e^{-ix\xi}f(x)`. Afleiða þess með tilliti til
:math:`\xi` uppfyllir

.. math::

  |\partial_\xi\varphi(x,\xi)|=|xf(x)|\leq
   \begin{cases}
   |f(x)|, & |x|\leq 1,\\
   |x||f(x)|, & |x|\geq 1.
   \end{cases}

Hægri hliðin er í :math:`L^1({{\mathbb  R}})` og því gefur
Lebesgue–setningin í viðauka C að :math:`{{\cal F}}f(\xi)` er
deildanlegt og

.. math::

  \begin{aligned}
   i\dfrac{d}{d\xi}{{\cal F}}\{f\}(\xi)=
   \int_{-\infty}^{+\infty}i\partial_\xi e^{-ix\xi}f(x) \, dx
   = \int_{-\infty}^{+\infty}e^{-ix\xi} xf(x) \, dx=
   {{\cal F}}\{ xf(x)\}(\xi).\end{aligned}

Við getum ítrekað þessa jöfnu, því ef við gefum okkur að :math:`f` og
:math:`x^jf` séu heildanleg föll, þá eru öll föllin
:math:`f,xf,\dots,x^jf` heildanleg og

.. math::

  \begin{aligned}
   i^j\dfrac{d^j}{d\xi^j}{{\cal F}}\{f\}(\xi)=
   \int_{-\infty}^{+\infty}i^j\partial_\xi^j e^{-ix\xi}f(x) \, dx
   = \int_{-\infty}^{+\infty}e^{-ix\xi} x^jf(x) \, dx=
   {{\cal F}}\{x^jf(x)\}(\xi).\end{aligned}

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Við skulum nú reikna aftur út Fourier–mynd þéttifallsins fyrir stöðluðu
normaldreifinguna :math:`f(x)=\tfrac 1{\sqrt{2\pi}}e^{-\frac 12 x^2}`,
sem við tókum fyrir í :ref:`sýnidæmi <syfouriermyndthettifallsstodludunormaldreifingarinnar:>`. Við tökum eftir því að
:math:`f` uppfyllir fyrsta stigs afleiðujöfnuna

.. math:: f{{^{\prime}}}(x)+x f(x)=0, \qquad x\in {{\mathbb  R}}.

Nú tökum við Fourier–myndina af liðunum í þessari jöfnu og notum
reiknireglur (ix) og (x). Þá fáum við jöfnuna

.. math:: i\xi\widehat f(\xi)+i\dfrac d{d\xi}\widehat f(\xi)=0, \qquad \xi\in {{\mathbb  R}},

og þar með uppfyllir :math:`\widehat f` fyrsta stigs jöfnuna

.. math:: \dfrac d{d\xi}\widehat f(\xi)+\xi \widehat f(\xi)=0, \qquad \xi\in {{\mathbb  R}}.

Almenn lausn hennar er gefin með

.. math:: \widehat f(\xi)= C e^{-\frac 12\xi^2}, \qquad \xi\in {{\mathbb  R}},

og fastinn :math:`C` ákvarðast af
:math:`C=\widehat f(0)=\int_{-\infty}^{+\infty} f(x) \, dx=1`. Við höfum
því sýnt aftur fram á að :math:`\widehat f(\xi)=e^{-\frac 12 \xi^2}`

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Við getum beitt reiknireglu (x) til þess að reikna út Fourier-mynd
fallsins :math:`f(x)=x^2e^{-x^2}`, því

.. math::

  \begin{aligned}
   {{\cal F}}f({\xi})&={{\cal F}}\{x^2e^{-x^2}\}({\xi})
   =i^2\dfrac{d^2}{d{\xi}^2}{{\cal F}}\{e^{-x^2}\}({\xi})
   =-\sqrt {\pi} \dfrac{d^2}{d{\xi}^2} e^{-\frac 14 {\xi}^2}\\
   &=\tfrac 12 \sqrt \pi\dfrac d{d{\xi}}\big({\xi}e^{-\frac 14 {\xi}^2}\big)
   =\tfrac 12 \sqrt \pi  \big(1-\tfrac 12 {\xi}^2)e^{-\frac 14{\xi}^2}.\end{aligned}

.. end-toggle::

.. _syfourierheavysidepowerexp:
Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

\(i) Við skulum reikna út Fourier-mynd
:math:`f(x)=H(x)x^ke^{{\alpha} x}`,
:math:`{{\operatorname{Re\, }}}{\alpha}<0`. Samkvæmt
:ref:`sýnidæmi <synokkurfouriersynidaemi>` (i) og reiknireglu (x) er

.. math::

  \begin{aligned}
   {{\cal F}}\{H(x)x^ke^{{\alpha} x}\}({\xi})
   &=i^k \dfrac {d^k}{d{\xi}^k}
   {{\cal F}}\{H(x)e^{{\alpha} x}\}({\xi})
   =i^k\dfrac {d^k}{d{\xi}^k}\dfrac 1{i{\xi}-{\alpha}}\\
   &=i^k\dfrac {i^k(-1)^kk!}{(i{\xi}-{\alpha})^{k+1}}
   =\dfrac {k!}{(i{\xi}-{\alpha})^{k+1}}.\end{aligned}

\(ii) Með sama hætti reiknum við út fyrir
:math:`{{\operatorname{Re\, }}}{\alpha}>0` að

.. math::

  {{\cal F}}\{H(-x)x^ke^{{\alpha} x}\}({\xi})
   =-\dfrac {k!}{(i{\xi}-{\alpha})^{k+1}}.

.. end-toggle::

Andhverf Fourier–ummyndun 
--------------------------

Andhverf Fourier–ummyndun 
~~~~~~~~~~~~~~~~~~~~~~~~~~

Fram til þessa höfum við aðeins sagt að Fourier mynd falls :math:`f` í
:math:`L^1({{\mathbb  R}})` er fall á :math:`{{\mathbb  R}}` en ekkert
sagt nánar um hvaða eiginleika hún hefur. Hér kemur niðurstaða sem bætir
úr þessu:

Hjálparsetning
^^^^^^^^^^^^^^

(*Riemann–Lebesgue*).   Ef :math:`f\in L^1({{\mathbb  R}})`, þá er
:math:`{{\cal F}}f\in C({{\mathbb  R}})` og

.. math:: \lim_{\xi\to \pm \infty}{{\cal F}}f(\xi)=0.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Til þess að sanna að :math:`{{\cal F}}f` sé samfellt, þá þurfum við að
beita setningu Lebesgues. Við skrifum

.. math::

  \widehat f(\xi+h)-\widehat f(\xi) = \int_{-\infty}^{+\infty}
   (e^{-ihx}-1)e^{-ix\xi}f(x) \,dx.

Greinilegt er að heildisstofninn stefnir á núll í sérhverjum punkti, ef
:math:`h\to 0`, og að hann er takmarkaður af fallinu :math:`2|f(x)|`,
sem er heildanlegt. Við megum því taka markgildi undir heildið og fáum
:math:`\lim_{h\to 0}(\widehat f(\xi+h)-\widehat f(\xi))=0` og þar með er
:math:`\widehat f` samfellt. Reikniregla (ix),
:math:`\widehat f(\xi)=\widehat{f'}(\xi)/(i\xi)`, gefur að
:math:`\lim_{\xi\to \pm \infty}\widehat f(\xi)=0` ef :math:`f` er
samfellt deildanlegt og
:math:`f{{^{\prime}}}\in L^ 1({{\mathbb  R}})`. Við eftirlátum
stærðfræðingunum að sýna, að um sérhvert fall
:math:`f\in L^ 1({{\mathbb  R}})` og sérhvert :math:`\varepsilon>0`
gildi að til er fall :math:`f_\varepsilon\in C^ 1({{\mathbb  R}})\cap L^ 1({{\mathbb  R}})` með afleiðu í :math:`L^ 1({{\mathbb  R}})`
þannig að :math:`\int_{-\infty}^{+\infty}|f(x)-f_\varepsilon(x)|\, dx<\varepsilon`, og að setningin leiði almennt af þessari staðreynd.

.. end-toggle::

Setjum nú
:math:`C_0({{\mathbb  R}})=\{F\in C({{\mathbb  R}})\,;\, \lim_{|\xi|\to +\infty}F(\xi)=0\}`. Þá er ljóst að :math:`C_0({{\mathbb  R}})` er
hlutrúm í :math:`C({{\mathbb  R}})`. Riemann-Lebesgue-hjálparsetningin
segir okkur að Fourier-ummyndun :math:`{{\cal F}}` varpi rúminu
:math:`L^1({{\mathbb  R}})` inn í :math:`C_0({{\mathbb  R}})`. Hægt er
að sýna fram á að til eru föll :math:`F\in C_0({{\mathbb  R}})` sem ekki
eru Fourier-myndir af föllum í :math:`L^1({{\mathbb  R}})`, en það er
jafngilt því að segja að Fourier-ummyndunin
:math:`{{\cal F}}:L^1({{\mathbb  R}})\to C_0({{\mathbb  R}})` sé ekki
átæk vörpun.

Nú skulum við gera ráð fyrir því að bæði föllin :math:`f` og
:math:`{{\cal F}}f` séu í
:math:`L^1({{\mathbb  R}})\cap C({{\mathbb  R}})` og reikna út
Fourier–myndina af :math:`{{\cal F}}f`. Þetta fall er gefið með
formúlunni

.. math::

  \begin{aligned}
   ({{\cal F}}{{\cal F}}f)(x) &=
   \int_{-\infty}^{+\infty}e^{-ix\xi}
   \bigg(\int_{-\infty}^{+\infty}e^{-iy\xi}f(y) \, dy\bigg)\, d\xi\\
   &=\int_{-\infty}^{+\infty}
   \bigg(\int_{-\infty}^{+\infty}e^{-i(x+y)\xi}f(y) \, dy\bigg)\, d\xi\\
   &=\int_{-\infty}^{+\infty}
   \bigg(\int_{-\infty}^{+\infty}e^{-it\xi}f(t-x) \, dt\bigg)\, d\xi.\end{aligned}

Nú viljum við skipta á röð heildanna, en það getum við ekki, því
:math:`\int_{-\infty}^{+\infty}e^{-it\xi} \, d\xi` er ósamleitið. Við
snúum okkur út úr þeim vandræðum með því að smeygja fallinu
:math:`e^{-\varepsilon|x|}` undir heildið og láta síðan
:math:`\varepsilon\to 0+`. Við fáum þá,

.. math::

  \begin{aligned}
   ({{\cal F}}{{\cal F}}f)(x)&=\lim_{\varepsilon\to 0}
   \int_{-\infty}^{+\infty}e^{-\varepsilon|\xi|}
   \bigg(\int_{-\infty}^{+\infty}e^{-it\xi}f(t-x) \, dt\bigg)\, d\xi\\
   &=\lim_{\varepsilon\to 0}
   \int_{-\infty}^{+\infty}f(t-x)
   \bigg(\int_{-\infty}^{+\infty}e^{-it\xi}e^{-\varepsilon|\xi|} \,
   d\xi\bigg) \, dt\\
   &=\lim_{\varepsilon\to 0} \int_{-\infty}^{+\infty}f(t-x)
   {{\cal F}}\{e^{-\varepsilon|\xi|}\}(t) \, dt\\
   &=\lim_{\varepsilon\to 0} \int_{-\infty}^{+\infty}f(t-x)
   {{\cal F}}\{e^{-|\xi|}\}(t/\varepsilon) \varepsilon^{-1}\, dt\\
   &=\lim_{\varepsilon\to 0} \int_{-\infty}^{+\infty}f(\varepsilon t-x)
   {{\cal F}}\{e^{-|\xi|}\}(t) \, dt\\
   &=f(-x)\int_{-\infty}^{+\infty}\dfrac 2{1+t^2} \, dt= 2\pi f(-x).\end{aligned}

Hér skulum við staldra ögn við og huga að því hvaða reiknireglum við
höfum beitt. Fyrst skiptum við á röð heildanna og við réttlætum það með
setningu Fubinis í viðauka C. Í næsta skrefi tökum við eftir því að
innra heildið er Fourier–mynd. Þar á eftir beitum við reiknireglu (ii)
og skiptum síðan á breytistærðum. Í síðasta skrefinu notfærum við okkur
sýnidæmi hér fyrir framan og tökum markgildi undir heildið. Til þess að
réttlæta að það megi, þá athugum við að fallið :math:`f` er takmarkað,
:math:`|f(x)|\leq C`, :math:`x\in {{\mathbb  R}}`. Þar með er

.. math::

  |f(\varepsilon t-x){{\cal F}}\{e^{-|\xi|}\}(t)|\leq  \dfrac {2C}{1+t^2},
   \qquad t\in {{\mathbb  R}}.

Í hægri hlið þessarar ójöfnu stendur fall í :math:`L^1({{\mathbb  R}})`
sem er óháð :math:`\varepsilon` og því segir setning Lebesgues að það
megi taka markgildi þegar :math:`{\varepsilon}\to 0` undir heildið.

Niðurstaðan sem við höfum sannað er:

Setning
^^^^^^^

(*Andhverfuformúla Fouriers*).  

Látum :math:`f\in L^1({{\mathbb  R}})\cap C({{\mathbb  R}})` og gerum
ráð fyrir að :math:`{{\cal F}}f=\widehat f\in L^1({{\mathbb  R}})`. Þá
er

.. math::

  f(x) =\dfrac 1{2\pi}\int_{-\infty}^{+\infty}e^{ix\xi}\widehat f(\xi) \,
   d\xi = \dfrac 1{2\pi}({{\cal F}}{{\cal F}}f)(-x), \qquad x\in {{\mathbb  R}}.

--------------

Andhverfuformúla Fouriers hefur geysimikla þýðingu. Hún segir okkur að
fallið :math:`f(x)` sé samantekt, sem gefin er með óendanlegu heildi, af
hreintóna sveiflum. Þessum hreintóna sveiflum er lýst með föllunum

.. math:: {{\mathbb  R}}\ni x\mapsto e^{ix\xi}=\cos(x\xi)+i\sin(x\xi), \qquad \xi\in {{\mathbb  R}},

sveifluhæðin er :math:`(2\pi)^{-1}|\widehat f(\xi)|` og fasahornið er
:math:`\arg \widehat f(\xi)`.

Við stöndum hér við upphafið að mikilli fræðigrein, sem kennd er við
upphafsmann sinn Jean Baptiste Joseph Fourier (1768–1830), og kölluð er
Fourier–greining. Í örfáum orðum sagt, þá snýst hún um að rannsaka
eiginleika fallsins :math:`f(x)` út frá eiginleikum Fourier–myndarinnar
:math:`\widehat f(\xi)`.

Í sönnun okkar á andhverfuformúlu Fouriers, gengum við út frá því að
Fourier–myndin væri heildanleg. Það gildir ekki almennt. Það eina sem
við vitum almennt um Fourier-myndina er það sem
Riemann-Lebesgue-hjálparsetningin segir,
:math:`\widehat f\in C_0({{\mathbb  R}})`.

Í sumum tilfellum er hægt að draga þá ályktun að Fourier–myndin sé
heildanleg út frá ýmsum eiginleikum fallanna :math:`f` og
:math:`\widehat f`.

Setning
^^^^^^^

Gerum ráð fyrir því að :math:`f` sé takmarkað fall í
:math:`L^1({{\mathbb  R}})` og að :math:`\widehat f({\xi})\geq 0` fyrir öll :math:`{\xi}\in {{\mathbb  R}}`. Þá er
:math:`\widehat f\in L^1({{\mathbb  R}}).`

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Lítum á heildið

.. math::

  \begin{aligned}
   \int_{-\infty}^{+\infty} 
   e^{-\varepsilon|\xi|}\widehat f(\xi) \, d\xi
   &=\int_{-\infty}^{+\infty} 
   e^{-\varepsilon|{\xi}|}
   \bigg(\int_{-\infty}^{+\infty} e^{-ix{\xi}}f(x)\, dx\bigg) \, d{\xi} \\
   &=\int_{-\infty}^{+\infty} \bigg(\int_{-\infty}^{+\infty} 
   e^{-ix{\xi}}e^{-\varepsilon|{\xi}|}\, d{\xi} \bigg)
   f(x)\, dx\\
   &=\int_{-\infty}^{+\infty} \dfrac{2\varepsilon}{{\varepsilon}^2+x^2}
   f(x)\, dx\end{aligned}

Hér höfum við notað niðurstöðuna úr :ref:`sýnidæmi <synokkurfouriersynidaemi>` (iii).
Fyrst fallið :math:`f` er takmarkað, segjum :math:`|f(x)|\leq C` fyrir öll
:math:`x\in {{\mathbb  R}}`, þá fáum við ójöfnuna

.. math::

  \int_{-\infty}^{+\infty} 
   e^{-\varepsilon|\xi|}\widehat f(\xi) \, d\xi
   \leq
   C\int_{-\infty}^{+\infty} \dfrac{2\varepsilon}{{\varepsilon}^2+x^2} \, dx
   =2{\pi} C.

Nú notfærum við okkur að lægsta gildi fallsins
:math:`e^{-{\varepsilon}|{\xi}|}` á bilinu :math:`[-R,R]` er
:math:`e^{-{\varepsilon}R}` til þess að fá matið

.. math::

  e^{-{\varepsilon}R}\int\limits_{-R}^R \widehat f({\xi}) \, d{\xi}
   \leq
   \int\limits_{-R}^Re^{-{\varepsilon}|{\xi}|} \widehat f({\xi}) \, d{\xi}
   \leq
   \int\limits_{-\infty}^{+\infty}
   e^{-{\varepsilon}|{\xi}|} \widehat f({\xi}) \, d{\xi}\leq 2{\pi} C.

Nú látum við :math:`{\varepsilon}\to 0` í vinstri hliðinni og fáum

.. math::

  \int\limits_{-R}^R \widehat f({\xi}) \, d{\xi}
   \leq 2{\pi}C.

Að lokum látum við :math:`R\to +{\infty}`. Það gefur

.. math::

  \int\limits_{-\infty}^{+\infty}\widehat f({\xi}) \, d{\xi}
   \leq 2{\pi}C,

og við höfum sannað að :math:`\widehat f\in L^1({{\mathbb  R}})`.

.. end-toggle::

Við getum nú sannað aðra útgáfu af andhverfuformúlu Fouriers, þar sem
við setjum einungis skilyrði á fallið :math:`f` en engin skilyrði á
:math:`\widehat f`:

Setning
^^^^^^^

(*Andhverfuformúla Fouriers*).  

Gerum ráð fyrir að
:math:`f\in PC^1({{\mathbb  R}})\cap L^1({{\mathbb  R}})`, þ.e. að
fallið :math:`f` sé samfellt deildanlegt á köflum og að :math:`|f|` sé
heildanlegt. Þá er

.. math::

  \dfrac 12(f(x+)+f(x-))=\lim_{R\to +\infty}
   \tfrac 1{2\pi}\int_{-R}^{R}e^{ix\xi}\widehat f(\xi) \, d\xi,
   \qquad x\in {{\mathbb  R}}.

Ef :math:`f` er samfellt í punktinum :math:`x`, þá er

.. math::

  f(x)=\lim_{R\to +\infty}
   \dfrac 1{2\pi}\int_{-R}^{R}e^{ix\xi}\widehat f(\xi) \, d\xi,
   \qquad x\in {{\mathbb  R}}.

--------------

.. figure:: ./myndir/fig056.svg
    :align: center
    :alt: Meðalgildi af markgildum frá hægri og vinstri

    Mynd: Meðalgildi af markgildum frá hægri og vinstri

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við sönnum setninguna í fjórum skrefum:

*Skref (i):* Gerum fyrst ráð fyrir að :math:`x=0`, :math:`f` sé samfellt
í :math:`x=0` og :math:`f(0)=0`. Setjum :math:`g(x)=f(x)/x`. Fyrst
:math:`f` er samfellt deildanlegt á köflum, samfellt í :math:`x=0` og
:math:`f(0)=0`, þá eru markgildin

.. math::

  \begin{aligned}
   g(0+)&=
   \lim_{x\to 0+}g(x) = \lim_{x\to 0+}\dfrac {f(x)-f(0)}x,\\
   g(0-)&=
   \lim_{x\to 0-}g(x) = \lim_{x\to 0-}\dfrac {f(x)-f(0)}x\end{aligned}

bæði til og fallið :math:`g` er því heildanlegt á :math:`[-1,1]`. Nú er
:math:`|g(x)|\leq |f(x)|` ef :math:`|x|\geq 1`, og þar með er
:math:`g\in  L^1({{\mathbb  R}})`. Reikniregla (x) segir okkur síðan að

.. math::

  \widehat f(\xi)=\int_{-\infty}^{+\infty}e^{-ix\xi}xg(x) \, dx=
   i\dfrac d{d\xi}\int_{-\infty}^{+\infty}e^{-ix\xi}g(x) \, dx=
   i\dfrac d{d\xi}\widehat g(\xi).

Riemann-Lebesgue-hjálparsetning gefur að
:math:`\lim_{\xi\to\pm\infty}\widehat g(\xi)=0`, og þar með er

.. math::

  \begin{aligned}
   \lim_{R\to+\infty}\dfrac
   1{2\pi}\int_{-R}^{R}\widehat f(\xi) \, d\xi
   &=\lim_{R\to+\infty}\dfrac
   i{2\pi}\int_{-R}^{R} \dfrac d{d\xi}\widehat g(\xi) \, d\xi\\
   &= \lim_{R\to+\infty}\dfrac
   i{2\pi}(\widehat g(R)-\widehat g(-R))=0=f(0).\end{aligned}

*Skref (ii):* Gerum ráð fyrir því að :math:`x=0` og :math:`\frac 12(f(0+)+f(0-))=0`. Við setjum :math:`\alpha=f(0+)` og skilgreinum
:math:`h(x)=f(x)-\alpha{{\operatorname{sign}}}(x)e^{-|x|}`. Þá er

.. math::

  \begin{gathered}
   h(0+)=
   \lim_{x\to 0+}h(x)=\lim_{x\to 0+}(f(x)-\alpha{{\operatorname{sign}}}(x)e^{-|x|})
   =\alpha-\alpha=0\\
   h(0-)=
   \lim_{x\to 0-}h(x)=\lim_{x\to 0-}(f(x)-\alpha{{\operatorname{sign}}}(x)e^{-|x|})
   =-\alpha+\alpha=0\\\end{gathered}

svo :math:`h` uppfyllir skilyrðin í skrefi (i). Í 
:ref:`sýnidæmi <synokkurfouriersynidaemi>` (iv) sýndum við að

.. math:: {{\cal F}}\{{{\operatorname{sign}}}(x)e^{-|x|}\}(\xi)=\dfrac{-2i\xi}{1+\xi^2},

sem er oddstætt, og því er heildi þess yfir :math:`[-R,R]` jafnt :math:`0`. Þar
með er

.. math::

  \begin{aligned}
   \tfrac 12(f(0+)+f(0-))&=0=h(0)
   =\lim_{R\to +\infty} \dfrac 1{2\pi}\int_{-R}^{R}\widehat h(\xi) \, d\xi\\
   &=\lim_{R\to +\infty} \dfrac 1{2\pi}\int_{-R}^{R}
   \bigg(\widehat f(\xi)+\dfrac {2i\alpha \xi}{1+\xi^2}\bigg) \, d\xi\\
   &=\lim_{R\to +\infty} \dfrac 1{2\pi}\int_{-R}^{R}\widehat f(\xi) \, d\xi.\end{aligned}

*Skref (iii):* Gerum ráð fyrir að :math:`x=0` setjum
:math:`\alpha=\frac 12(f(0+)+f(0-))` og skilgreinum :math:`j(x)=f(x)-\alpha e^{-|x|}`.
Fallið :math:`j` uppfyllir skilyrðin í skrefi (ii). Samkvæmt 
:ref:`sýnidæmi <synokkurfouriersynidaemi>` er :math:`{{\cal F}}\{e^{-|x|}\}(\xi)=2/(1+\xi^2)` og
þar með fáum við

.. math::

  \begin{aligned}
   0&=\lim_{R\to +\infty}\dfrac 1{2\pi}
   \int_{-R}^R \widehat j(\xi) \, d\xi\\
   &=\lim_{R\to +\infty}
   \bigg(\dfrac 1{2\pi}\int_{-R}^R \widehat f(\xi) \, d\xi
   -\dfrac \alpha\pi\int_{-R}^R  \dfrac { d\xi}{1+\xi^2} \bigg)=
   \lim_{R\to +\infty}
   \dfrac 1{2\pi}\int_{-R}^R \widehat f(\xi) \, d\xi -\alpha.\end{aligned}

Niðurstaðan verður

.. math::

  \tfrac 12(f(0+)+f(0-))=\alpha=
   \lim_{R\to +\infty} \dfrac 1{2\pi}\int_{-R}^R \widehat f(\xi) \, d\xi.

*Skref (iv):* Látum nú :math:`\alpha` vera einhvern punkt í
:math:`{{\mathbb  R}}` og setjum :math:`k(x)=f(x+\alpha)`. Samkvæmt
reiknireglu (iii) er
:math:`\widehat k(\xi)=e^{i\alpha\xi}\widehat f(\xi)` og skref (iii)
gefur því

.. math::

  \begin{aligned}
   \tfrac 12(f(\alpha+)+f(\alpha-))&=
   \tfrac 12(k(0+)+k(0-))=
   \lim_{R\to +\infty} \dfrac 1{2\pi}\int_{-R}^R \widehat k(\xi) \, d\xi\\
   &=\lim_{R\to +\infty} \dfrac 1{2\pi}\int_{-R}^R e^{i\alpha\xi}
    \widehat f(\xi) \, d\xi.\end{aligned}

.. end-toggle::

Földun og Fourier–ummyndun
--------------------------

Földun
~~~~~~

Látum :math:`f` og :math:`g` vera tvö föll á :math:`{{\mathbb  R}}` og
lítum á :hover:`földun` þeirra :math:`f\ast g`, sem skilgreind
er með

.. math:: f\ast g(x)= \int_{-\infty}^{+\infty}f(x-t)g(t) \, dt

fyrir öll :math:`x\in {{\mathbb  R}}` þannig að heildið sé samleitið.
Með því að innleiða breytuskiptin :math:`\tau=x-t`, þá sjáum við að

.. math::

  f\ast g(x)=
   \int_{-\infty}^{+\infty}f(x-t)g(t) \, dt=
   \int_{-\infty}^{+\infty}f(\tau)g(x-\tau) \, d\tau=g\ast f(x).

Ef annað fallið er í :math:`L^1({{\mathbb  R}})` og hitt fallið er
takmarkað, þá er földunin skilgreind fyrir öll
:math:`x\in {{\mathbb  R}}`. Ef bæði föllin eru í
:math:`L^1({{\mathbb  R}})`, þá er
:math:`f\ast g\in L^1({{\mathbb  R}})`, því setning Fubinis gefur okkur

.. math::

  \begin{aligned}
   \int_{-\infty}^{+\infty}|f\ast g(x)| \, dx&=
   \int_{-\infty}^{+\infty}|\int_{-\infty}^{+\infty}f(x-t)g(t) \, dt|\,dx\\
   &\leq 
   \int_{-\infty}^{+\infty}
   \bigg(\int_{-\infty}^{+\infty}|f(x-t)| \, dx\bigg) |g(t)|\, dt\\
   &= \int_{-\infty}^{+\infty}|f(x)| \, dx
   \int_{-\infty}^{+\infty}|g(t)|\, dt<+\infty.\end{aligned}

Lítum nú aftur á :math:`f \ast g` og gerum ráð fyrir að
:math:`f\in C^ 1({{\mathbb  R}})` og að bæði :math:`f` og :math:`f{{^{\prime}}}`
séu takmörkuð föll. Þá megum við deilda undir heildið og fáum að
:math:`f\ast g\in C^ 1({{\mathbb  R}})` með
:math:`(f\ast g){{^{\prime}}}(x)=(f{{^{\prime}}}\ast g)(x)`. Með
þrepun fáum við síðan að fyrir :math:`f\in C^ m({{\mathbb  R}})` með
föllin :math:`f,f{{^{\prime}}},\dots,f^{(m)}` takmörkuð, er
:math:`f\ast g\in C^ m({{\mathbb  R}})` og

.. math::

  (
   f\ast g)^{(k)}(x)=(f^{(k)}\ast g)(x), \qquad x\in {{\mathbb  R}}, \quad k=0,\dots,m.

Regla (xi): :math:`{{\cal F}}\{f\ast g\}(\xi)={{\cal F}}f(\xi){{\cal F}}g(\xi)`, :math:`\xi\in {{\mathbb  R}}`, :math:`f,g\in L^1({{\mathbb  R}})`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fourier–myndin af :math:`f\ast g` er auðreiknanleg, því setnig Fubinis í
viðauka C leyfir okkur að skipta á röð heildanna

.. math::

  \begin{aligned}
   \int_{-\infty}^{+\infty}e^{-ix\xi}(f\ast g)(x) \, dx 
   &=
   \int_{-\infty}^{+\infty}e^{-ix\xi}
   \bigg(\int_{-\infty}^{+\infty}f(x-t)g(t) \, dt\bigg)\, dx\\
   &=
   \int_{-\infty}^{+\infty}
   \bigg(\int_{-\infty}^{+\infty}e^{-i(x-t)\xi}f(x-t)
   e^{-it\xi}g(t) \, dt\bigg)\, dx\\
   &=
   \int_{-\infty}^{+\infty}
   \bigg(\int_{-\infty}^{+\infty}e^{-i(x-t)\xi}f(x-t)
   \, dx \bigg)e^{-it\xi}g(t) \, dt\\
   &=
   \int_{-\infty}^{+\infty}e^{-ix\xi}f(x) \, dx
   \int_{-\infty}^{+\infty}e^{-it\xi}g(t) \, dt.\end{aligned}

Niðurstaðan er því

.. math::

  {{\cal F}}\{f\ast g\}(\xi)={{\cal F}}f(\xi){{\cal F}}g(\xi), \qquad \xi\in {{\mathbb  R}},
   \quad f, g\in L^1({{\mathbb  R}})

Afleiðujöfnur og Fourier–ummyndun
---------------------------------

Sérlausnir á afleiðujöfnum reiknaðar með Fourier-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við víkja aftur að því verkefni að finna 
:hover:`sérlausn` á jöfnunni

.. math:: P(D)u=(a_mD^ m+\cdots+a_1D+a_0)u=f(x),

sem við fjölluðum um í upphafi kaflans. Við göngum út frá því að
:math:`f\in L^ 1({{\mathbb  R}})` og sömuleiðis að
:math:`u,u{{^{\prime}}},\dots,u^{(m)}\in L^ 1({{\mathbb  R}})`. Nú tökum við Fourier–myndina af föllunum sem standa
beggja vegna jafnaðarmerkisins og notum reiknireglu (ix). Þá fæst

.. math::

  P(i\xi) \widehat u(\xi) =
   \widehat f(\xi), \qquad \xi\in {{\mathbb  R}}.

Þessi jafna gefur okkur sambandið milli :math:`\widehat u` og
:math:`\widehat f`,

.. math:: \widehat u(\xi)= \dfrac{\widehat f({\xi})}{P(i\xi)}, \qquad \xi\in {{\mathbb  R}}.

Hægri hliðin í þessari jöfnu skilgreinir samfellt fall í grennd um
sérhvern punkt :math:`\alpha` þar sem :math:`P(i\alpha)\neq 0`. Ef hins
vegar :math:`P(i\alpha)=0`, :math:`P(i\xi)=(\xi-\alpha)^ kQ(\xi)`, þar
sem :math:`Q` er margliða :math:`Q(\alpha)\neq 0`, þá skilgreinir hægri
hliðin í jöfnunni fall sem er samfellt í :math:`\alpha` ef markgildið

.. math:: \lim\limits_{\xi\to \alpha} \dfrac {\widehat f(\xi)}{(\xi-\alpha)^ k}

er til. Niðurstaðan er því:

Setning
^^^^^^^

Gerum ráð fyrir því að
:math:`f\in L^ 1({{\mathbb  R}})\cap C({{\mathbb  R}})` og
:math:`\widehat f\in L^ 1({{\mathbb  R}})` og jafnframt að :math:`\widehat f(\xi)/P(i\xi)`
skilgreini samfellt fall á :math:`{{\mathbb  R}}`. Þá hefur
afleiðujafnan :math:`P(D)u=f` lausn :math:`u\in L^ 1({{\mathbb  R}})\cap C^ m({{\mathbb  R}})` sem gefin er með
formúlunni

.. math::

  u(x)=\dfrac 1{2\pi}\int_{-\infty}^ {+\infty} 
   e^{ix\xi} \dfrac{\widehat f(\xi)}{P(i\xi)}\, d\xi, \qquad x\in {{\mathbb  R}}.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við sjáum að fallið :math:`(i\xi)^ k \widehat f(\xi)/P(i\xi)` er í
:math:`L^ 1({{\mathbb  R}})` fyrir öll :math:`k\leq m`, svo setning
Lebesgues segir okkur að við megum taka afleiður af :math:`u` með því að
deilda veldisvísisfallið undir heildinu. Þar með er

.. math::

  \begin{aligned}
   P(D)u(x)&=\dfrac 1{2\pi}\int_{-\infty}^{+\infty}P(D_x)e^{ix\xi} 
   \dfrac{\widehat f(\xi)}{P(i\xi)}\, d\xi=
   \dfrac 1{2\pi}\int_{-\infty}^{+\infty}P(i\xi)e^{ix\xi} 
   \dfrac{\widehat f(\xi)}{P(i\xi)}\, d\xi\\
   &= \dfrac 1{2\pi}\int_{-\infty}^{+\infty}e^{ix\xi} 
   \widehat f(\xi)\, d\xi=f(x).\end{aligned}

.. end-toggle::

Í sumum dæmum er auðvelt að reikna út andhverfu Fourier-myndina af
fallinu :math:`\widehat f(\xi)/P(i\xi)`:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Leysum jöfnuna

.. math::

  -u{{^{\prime\prime}}}+\omega^ 2u=e^{-|x|}=f(x), \qquad \omega^ 2 \neq 1,
   \qquad x\in {{\mathbb  R}},

með því að beita Fourier-ummyndun.

Við athugum að kennimargliða jöfnunnar er :math:`P(z)=-z^2+\omega^2` og
:math:`P(i\xi)=\xi^2+\omega^2`. Við tökum Fourier–mynd af öllum liðum
beggja vegna jafnaðarmerkisins,

.. math::

  \xi^ 2 \widehat u(\xi)+\omega^ 2 \widehat u(\xi) = \dfrac
   2{1+\xi^ 2}, \qquad \xi\in {{\mathbb  R}}.

Fourier–mynd :math:`u` er því

.. math::

  \begin{aligned}
   \widehat u(\xi)&=
   \dfrac 2{(\omega^ 2+\xi^ 2)(1+\xi^ 2)} =
   \dfrac 1{1-\omega^ 2}\bigg(
   \dfrac 2{\omega^ 2+\xi^ 2}-\dfrac 2{1+\xi^ 2}\bigg)\\
   &= \dfrac 1{1-\omega^ 2}\bigg(
   \dfrac 1\omega {{\cal F}}\{e^{-\omega|x|}\}({\xi})-{{\cal F}}\{e^{-|x|}\}({\xi})
   \bigg).\end{aligned}

Athugið að hér höfum við notað niðurstöðuna úr 
:ref:`sýnidæmi <synokkurfouriersynidaemi>` (iii) og reiknireglu (ii). Niðurstaðan er því

.. math::

  u(x)= \dfrac 1{1-\omega^ 2}\bigg( \dfrac 1\omega e^{-\omega|x|} -
   e^{-|x|} \bigg).

.. end-toggle::

Stofnbrotaliðun ræðra falla og andhverf Fourier-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við hugsa okkur að :math:`{{\operatorname{stig}}}P\geq 2` og
að fallið :math:`P(i\xi)` sé núllstöðvalaust á öllum rauntalnaásnum. Þá
er fallið :math:`1/P(i\xi)` í :math:`L^ 1({{\mathbb  R}})` og við
getum skilgreint andhverfu Fourier–mynd þess,

.. math::

  E(x)=
   \dfrac 1{2\pi}\int_{-\infty}^ {+\infty} 
   e^{ix\xi} \dfrac{d\xi}{P(i\xi)},  \qquad x\in {{\mathbb  R}}.

Fallið :math:`E` er samfellt samkvæmt Riemann-Lebesgue-hjálparsetningu
og formúlan fyrir lausninni í síðustu setningu er einfaldlega

.. math:: \widehat u(\xi) = \widehat E(\xi) \widehat f(\xi), \qquad \xi\in {{\mathbb  R}}.

Nú getum við notfært okkur reiknireglu (xi) og fáum framsetningu á
lausninni sem földunarheildi,

.. math::

  u(x)=E\ast f(x)=\int_{-\infty}^ {+\infty} E(x-t) f(t)\, dt
   =\int_{-\infty}^ {+\infty} E(t) f(x-t)\, dt.

Það reynist vera auðvelt að reikna út fallið :math:`E` ef við þekkjum
stofnbrotaliðun ræða fallsins :math:`\zeta\mapsto 1/P(\zeta)`:

Setning
^^^^^^^

Gerum ráð fyrir að :math:`P` sé margliða af stigi :math:`m` með ólíkar
núllstöðvar :math:`{\lambda}_1,\dots,{\lambda}_\ell` með margfeldni
:math:`m_1,\dots,m_\ell`, að :math:`P(i{\xi})` hafi enga núllstöð á
:math:`{{\mathbb  R}}`, að :math:`Q` sé margliða af stigi
:math:`\leq m-1` og að stofnbrotaliðun á ræða fallinu :math:`Q/P` sé
gefin með

.. math::

  \dfrac {Q(\zeta)}{P({\zeta})} =\sum\limits_{k=1}^\ell
   \sum\limits_{j=1}^{m_k} \dfrac{A_{jk}}{({\zeta}-{\lambda}_k)^j}.

Þá er andhverfa Fourier-mynd fallsins
:math:`{\xi}\mapsto Q(i\xi)/P(i{\xi})` gefin með formúlunni

.. math::

  \begin{aligned}
   f(x)&=
   \sum_{\substack{{{\operatorname{Re\, }}}{\lambda}_k<0}}
   \sum\limits_{j=1}^{m_k} A_{jk} 
   \tfrac 1{(j-1)!}H(x)x^{j-1}e^{{\lambda}_kx}\\
   &-\sum_{\substack{{{\operatorname{Re\, }}}{\lambda}_k>0}} 
   \sum\limits_{j=1}^{m_k} A_{jk} \tfrac 1{(j-1)!} H(-x)x^{j-1}e^{{\lambda}_kx}, 
   \qquad x\neq 0.\nonumber\end{aligned}

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Forsendan um núllstöðvar :math:`P(i{\xi})` jafngildir því að
:math:`P({\zeta})` hafi enga núllstöð, sem er hrein þvertala, en það
þýðir að :math:`{{\operatorname{Re\, }}}\lambda_k\neq 0` fyrir öll
:math:`k`. Stofnbrotaliðunin gefur

.. math::

  \dfrac {Q(i{\xi})}{P(i{\xi})} =\sum\limits_{k=1}^\ell
   \sum\limits_{j=1}^{m_k} \dfrac{A_{jk}}{(i{\xi}-{\lambda}_k)^j}.

Samkvæmt :ref:`sýnidæmi <syfourierheavysidepowerexp>` er

.. math::

  \begin{gathered}
   {{\cal F}}\{\tfrac 1{(j-1)!}H(x)x^{j-1}e^{{\lambda}_k x}\}(\xi) = 
   \dfrac 1{(i{\xi}-{\lambda}_k)^j},
   \qquad  {{\operatorname{Re\, }}}{\lambda}_k<0,\\
   {{\cal F}}\{\tfrac 1{(j-1)!}H(-x)x^{j-1}e^{{\lambda}_k x}\}(\xi) =
   \dfrac {-1}{(i{\xi}-{\lambda}_k)^j}, 
   \qquad {{\operatorname{Re\, }}}{\lambda}_k>0.\end{gathered}

Formúlan fyrir :math:`f(x)` leiðir því beint af andhverfuformúlu Fouriers.

.. end-toggle::

Deyfðar sveiflur
~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Deyfð sveifla; framhald

Við skulum nú halda áfram með sýnidæmi um deyfðar sveiflur og
reikna út fallið :math:`E` í því tilfelli að

.. math:: P(D)=mD^2+cD+k.

\(i) *Yfirdeyfing*, :math:`c^2-4km>0`. Núllstöðvar kennimargliðunnar eru
:math:`-c/2m\pm {\omega}`, :math:`{\omega}=\sqrt{c^2-4km}\, /2m`. Þær
eru báðar neikvæðar. Við höfum stofnbrotaliðunina

.. math::

  \begin{aligned}
   \dfrac 1{P({\zeta})} &=
   \dfrac 1{m{\zeta}^2+c{\zeta}+k}=
   \dfrac 1{m({\zeta}+c/2m-{\omega})({\zeta}+c/2m+{\omega})}\\
   &=\dfrac 1{2m{\omega}}\bigg(\dfrac 1{({\zeta}+c/2m-{\omega})}-
   \dfrac 1{({\zeta}+c/2m+{\omega})}\bigg)\end{aligned}

Nú lesum við út úr jöfnuna fyrir :math:`f(x)` í setningunni hér fyrir framan (fyrir :math:`Q(\zeta)=1`) að

.. math::

  \begin{aligned}
   E(x)&=\dfrac 1{2m{\omega}}\bigg(H(x)e^{-(c/2m)x+{\omega}x}-
   H(x)e^{-(c/2m)x-{\omega}x}\bigg)\\
   &=H(x)\dfrac 1{m{\omega}} e^{-(c/2m)x}\sinh({\omega}x)
   =H(x)g(x), \qquad x\in {{\mathbb  R}},\end{aligned}

þar sem fallið :math:`g` skilgreinir Green-fall virkjans,
:math:`G(t,{\tau})=g(t-{\tau})`.

\(ii) *Markdeyfing*, :math:`c^2-4km=0`. Hér höfum við tvöfalda núllstöð á
kennimargliðunni :math:`-c/2m`. Stofnbrotaliðun :math:`1/P` er

.. math:: \dfrac 1{P({\zeta})}= \dfrac{1}{m({\zeta}+c/2m)^2}

og við fáum því

.. math:: E(x)=H(x)\cdot \dfrac 1m xe^{-(c/2m)x}=H(x)g(x).

\(iii) *Undirdeyfing*, :math:`c^2-4km<0`. Hér eru núllstöðvarnar
:math:`-c/2m\pm i{\omega}`, :math:`{\omega}=\sqrt{4km-c^2}\, /2m`. Með
samskonar útreikningi og í (i) fáum við

.. math:: E(x)=H(x)\cdot \dfrac 1{m{\omega}} e^{-(c/2m)x}\sin({\omega}x)=H(x)g(x).

.. end-toggle::

Plancherel–jafnan
-----------------

Nú höldum við áfram að bæta við reiknireglum í safnið okkar:

Regla (xii): :math:`\displaystyle \int\limits_{-\infty}^{+\infty} \widehat f(x) g(x)\, dx = \int\limits_{-\infty}^{+\infty} f(x) \widehat g(x)\, dx`, :math:`f,g\in L^1({{\mathbb  R}})`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Athugum að Riemann-Lebesgues-hjálparsetning gefur okkur að
:math:`\widehat f` og :math:`\widehat g` eru samfelld föll sem stefna á
:math:`0` í :math:`\pm{\infty}`. Því eru bæði föllin :math:`f\widehat g`
og :math:`\widehat f g` heildanleg og setning Fubinis í viðauka C gefur
að við megum skipta á röð ítrekaðra heilda með tilliti til tveggja
breytistærða

.. math::

  \int_{-\infty}^{+\infty}\widehat f(\xi)g(\xi)\, d\xi
   =
   \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} e^{-ix{\xi}}f(x)g({\xi})
   \, dxd{\xi}
   =\int_{-\infty}^{+\infty} f(x)\widehat g(x)\, dx.

Við höfum sannað reglur Plancherel og Parseval fyrir Fourier-raðir og fáum nú hliðstæðar reglur fyrir Fourier-ummyndun. Fyrst
kemur Plancherel-jafna:

Regla (xiii): :math:`\displaystyle\int_{-\infty}^{+\infty} |f(x)|^2\, dx  = \dfrac 1{2{\pi}}\int_{-\infty}^{+\infty} |\widehat f(\xi)|^2 \, d\xi`, :math:`f\in L^1({{\mathbb  R}})`, :math:`|f|\leq C`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum nú ráð fyrir að :math:`f\in L^1({{\mathbb  R}})` og að :math:`f`
sé takmarkað. Þá gildir :math:`|f(x)|^2\leq C|f(x)|` fyrir öll
:math:`x\in {{\mathbb  R}}`, þar sem :math:`C` er fasti og fallið
:math:`|f|^2` er því heildanlegt Til þess að sýna að jákvæða fallið
:math:`|\widehat f|^2=\widehat f \overline{\widehat f}` sé heildanlegt,
þá dugir að sanna að það sé
Fourier–myndin af falli :math:`g\in L^1({{\mathbb  R}})` sem er bæði
samfellt og takmarkað. Við sjáum að

.. math::

  \overline{\widehat f(\xi)} =
   \int_{-\infty}^{+\infty}  e^{ix\xi}\overline {f(x)} \, dx
   =\int_{-\infty}^{+\infty} e^{-iy\xi} \overline{f(-y)}\, dy,

og þetta segir okkur að :math:`\overline{{\widehat f}(\xi)}= {{\cal F}}\{\overline{f(-x)}\}(\xi)`. Ef við setjum nú

.. math:: g(x) = \int_{-\infty}^{+\infty} f(x-y) \overline{f(-y)}\, dy,

þá er :math:`g\in L^1({{\mathbb  R}})\cap C({{\mathbb  R}})` og

.. math:: \widehat g(\xi)={{\cal F}}g(\xi) = {{\cal F}}f(\xi){{\cal F}}\{\overline{f(-x)}\}(\xi)=|\widehat f(\xi)|^2.

Ef við setjum nú :math:`x=0` inn í andhverfuformúluna, þá fæst

.. math::

  \int_{-\infty}^{+\infty} |f(y)|^2 \, dy = g(0) =  \frac 1{2\pi}
    \int_{-\infty}^{+\infty} g(\xi) \, d\xi =
   \frac 1{2\pi}\int_{-\infty}^{+\infty} |\widehat f(\xi)|^2 \, d\xi.

Þetta er Plancherel-jafna.

Regla (xiv) :math:`\displaystyle \int\limits_{-\infty}^{+\infty}  f(x) \overline{g(x)}\, dx =\dfrac 1{2{\pi}} \int\limits_{-\infty}^{+\infty} \widehat f({\xi}) \overline{\widehat g({\xi})}\, d{\xi}`.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Tökum nú tvö föll :math:`f,g\in L^1({{\mathbb  R}})` og gerum ráð fyrir
að þau séu takmörkuð. Þá er :math:`|f+\alpha g|^2` heildanlegt fyrir
sérhverja tvinntölu :math:`\alpha` samkvæmt reglu (xiii). Ef við tökum
hvaða tvær tvinntölur :math:`a` og :math:`b` sem er, þá gildir

.. math::

  a\bar b= \dfrac 14\big(
   |a+b|^2-|a-b|^2+i|a+ib|^2-i|a-ib|^2\big).

Til þess að sanna að fallið :math:`\widehat f\overline{\widehat g}` sé
heildanlegt, þá athugum við fyrst að

.. math::

  \widehat f \overline{\widehat g} =
   \dfrac 14\big(|\widehat f +\widehat g|^2
   -|\widehat f -\widehat g|^2
   +i|\widehat f +i\widehat g|^2
   -i|\widehat f-i\widehat g|^2\big),

og síðan að samkvæmt reglu (xiii) eru allir liðirnir í hægri hlið
þessarar jöfnu heildanleg föll. Nú skiptum við á hlutverki
:math:`\widehat f, \widehat g` og :math:`f,g` í þessari jöfnu

.. math::

  f \overline{g} =
   \dfrac 14\big(|f+g|^2-
   |f-g|^2+i |f+ig|^2-i|f-ig|^2 \big).

Nú fáum við Parseval-jöfnu

.. math::

  \int\limits_{-\infty}^{+\infty}  f(x) \overline{g(x)}\, dx =
   \dfrac 1{2{\pi}} \int\limits_{-\infty}^{+\infty} 
   \widehat f({\xi}) \overline{\widehat g({\xi})}\, d{\xi}

með því að bera saman hægri hliðar þessara tveggja jafna og beita reglu
(xiii) á hvern lið.

Setning
^^^^^^^

Ef :math:`f,f{{^{\prime}}}\in L^1({{\mathbb  R}})`, þá er
:math:`\widehat f\in L^1({{\mathbb  R}})`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Samkvæmt reglu (ix) er fallið :math:`i\xi\widehat f(\xi)` Fourier-myndin
af afleiðunni :math:`f{{^{\prime}}}`. Samkvæmt reglu (xiii) er
:math:`|i\xi\widehat f(\xi)|^2=|\xi|^2|\widehat f(\xi)|^2` heildanlegt á
:math:`{{\mathbb  R}}`. Nú er fallið :math:`|\xi|^{-2}` heildanlegt á
menginu :math:`\{\xi\in{{\mathbb  R}}; |\xi|\geq 1\}` og ójafnan :math:`ab\leq \tfrac 12 (a^2+b^2)` gefur

.. math::

  |\widehat f(\xi)|= |\xi\widehat f(\xi) {\xi}^{-1}|\leq
   \tfrac 12(|\xi|^2|\widehat f(\xi)|^2+|\xi|^{-2}).

Fallið í hægri hlið ójöfnunnar er heildanlegt og því gefur hún okkur að
:math:`|\widehat f(\xi)|` er heildanlegt yfir mengið
:math:`\{\xi\in{{\mathbb  R}}; |\xi|\geq 1\}`. Nú er
:math:`|\widehat f(\xi)|` samfellt fall og þar með heildanlegt yfir
:math:`[-1,1]`. Við höfum því sýnt fram á að
:math:`\widehat f\in L^1({{\mathbb  R}})`.

.. end-toggle::

Leifareikningur og Fourier–ummyndun
-----------------------------------

Fourier-myndir reiknaðar með leifareikningi.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur nú að :math:`f\in {{\cal O}}({{\mathbb  C}}\setminus A)`,
þar sem :math:`A` er dreift mengi og skilgreinum vegina :math:`\gamma_r`
og :math:`\beta_r` eins og í leifareikningnum,
:math:`\gamma_r(\theta)=re^{i\theta}`,
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

Athugum nú að

.. math::

  |e^{-iz\xi}|=e^{{{\operatorname{Re\, }}}(-i z\xi)}=e^{y\xi} \leq 1, \quad\text{
   ef }  y\geq 0 \text{ og } \xi\leq 0 \quad \text{ eða } 
   \quad y\leq 0 \text { og } \xi\geq 0.

.. math::

  \begin{aligned}
   \big|\int_{\gamma_r}e^{-iz\xi}f(z)\, dz\big|
   &\leq  \max_{|z|=r}|f(z)|  \int_{\gamma_r}|e^{-iz\xi}|\, |dz|,  
   \qquad \xi<0 ,\label{16.7.4a}\\
   \big|\int_{\beta_r}e^{-iz\xi}f(z)\, dz\big|
   &\leq \max_{|z|=r}|f(z)|   
   \int_{\beta_r}|e^{-iz\xi}|\, |dz|,  \qquad \xi > 0.\label{16.7.5a}\end{aligned}

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

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Athugum fyrst að :math:`\sin \theta \geq 2\theta/\pi` ef
:math:`\theta\in[0,\pi/2]`.

.. figure:: ./myndir/fig102.svg
    :align: center
    :alt:

    Mynd: :math:`\sin \theta \geq 2\theta/\pi`

Ef :math:`z=\gamma_r(\theta)=re^{i\theta}`, þá er
:math:`dz=ire^{i\theta}\, d\theta` og því

.. math::

  \begin{aligned}
   \int_{\gamma_r}|e^{-iz\xi}|\, |dz| &=
   \int_0^ \pi e^{\xi r\sin\theta}r\, d\theta =
   2r\int_0^ {\pi/2} e^{\xi r\sin \theta}\, d\theta \\
   &\leq 2r\int_0^ {\pi/2} e^{2\xi r\theta/\pi}\, d\theta =
   \dfrac \pi{\xi}\left[e^{-2\xi r\theta /\pi}\right]_0^{\pi/2}
   =\dfrac \pi{-\xi}\big(1-e^{\xi r}\big)<\dfrac \pi{-\xi}.\end{aligned}

Seinni ójafnan er sönnuð á nákvæmlega sama hátt.

.. end-toggle::

Hjálparsetning Jordan og jöfnurnar fyrir framan hana gefa:

Setning
^^^^^^^

Látum
:math:`f\in L^1({{\mathbb  R}})\cap {{\cal O}}({{\mathbb  C}}\setminus   A)`, þar sem :math:`A` er endanlegt mengi og gerum ráð fyrir að
:math:`\max_{|z|=r}|f(z)|\to 0` ef :math:`r\to +\infty`. Þá er

.. math::

  \widehat f(\xi) =
   \begin{cases}  2\pi i\sum_{\alpha\in A\cap H_+} 
   {{\operatorname{Res}}}(e^{-iz\xi}f(z),\alpha), & \xi < 0,\\
    -2\pi i\sum_{\alpha\in A\cap H_-} 
   {{\operatorname{Res}}}(e^{-iz\xi}f(z),\alpha),  & \xi > 0,
   \end{cases}

þar sem :math:`H_+=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z>0\}`
táknar efra hálfplanið og
:math:`H_-=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z<0\}` táknar
neðra hálfplanið.

--------------

Áður en við byrjum að beita leifaformúlunni til þess að reikna út
Fourier-myndir þá skulum við staldra við og rifja það upp að
Fourier-mynd af jafnstæðu fallið er jafnstætt fall. Hugsum okkur að
:math:`f` sé jafnstætt og að við höfum komist að því að
:math:`\widehat f(\xi)=g(\xi)` þar sem :math:`g` er fall á jákvæða ásnum
:math:`{{\mathbb  R}}_+`. Þá þurfum við ekki að reikna neitt meira því
við höfum :math:`\widehat f(\xi)=g(|\xi|)` fyrir öll
:math:`\xi\in{{\mathbb  R}}`. Ef við höfum reiknað út
:math:`\widehat f(\xi)=h(\xi)` þar sem :math:`h` er fall á neikvæða
ásnum :math:`{{\mathbb  R}}_-`, þá fáum við að
:math:`\widehat f(\xi)=h(-|\xi|)` fyrir öll
:math:`\xi\in {{\mathbb  R}}`.

Við vitum líka að Fourier-mynd af oddstæðu falli er oddstæð. Hugsum
okkur því að :math:`f` sé oddstætt og að við höfum að
:math:`\widehat f(\xi)=g(\xi)` þar sem :math:`g` er fall á jákvæða ásnum
:math:`{{\mathbb  R}}_+`. Þá gildir
:math:`\widehat f(\xi)={{\operatorname{sign}}}(\xi)g(|\xi|)` fyrir öll
:math:`\xi\in {{\mathbb  R}}`. Ef við höfum reiknað út
:math:`\widehat f(\xi)=h(\xi)` þar sem :math:`h` er fall á neikvæða
ásnum :math:`{{\mathbb  R}}_-`, þá fáum við að
:math:`\widehat f(\xi)={{\operatorname{sign}}}(\xi)h(-|\xi|)` fyrir öll
:math:`\xi\in {{\mathbb  R}}`.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Ef :math:`f(x)=1/(1+x^2)`, :math:`x\in {{\mathbb  R}}`, þá er

.. math::

  \widehat f(\xi) = 
   \int\limits_{-\infty}^{+\infty} \dfrac{e^{-ix\xi}}{1+x^2}\, dx
   =\pi e^{-|\xi|},  \qquad \xi\in {{\mathbb  R}}.

--------------

**Lausn:** Fallið er jafnstætt, svo við það dugir að reikna heildið út fyrir
:math:`\xi <0`. Fallið :math:`f` hefur aðeins eitt skaut :math:`i` í
efra hálfplaninu sem er einfalt og
:math:`\max_{|z|=r}|f(z)|\leq 1/(r^2-1)\to 0` ef :math:`r\to+\infty`.
Við höfum því

.. math::

  \widehat f(\xi) = 2\pi i
   {{\operatorname{Res}}}\bigg(\dfrac{e^{-iz\xi}}{1+z^2},i\bigg)
   =2\pi i \dfrac{e^{-i(i\xi)}}{2i}=\pi e^{\xi}, \qquad \xi<0,

og niðurstaðan verður

.. math:: \widehat f(\xi)=\pi e^{-|\xi|}, \qquad \xi\in {{\mathbb  R}}.

Við vorum reyndar búin að reikna út Fourier-mynd fallsins
:math:`e^{-|x|}` og getum því staðfest þessa formúlu með því að beita
andhverfuformúlunni.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Ef :math:`f(x)=1/(1+x^4)`, :math:`x\in {{\mathbb  R}}`, þá er

.. math::

  \widehat f(\xi) =\int_{-\infty}^{+\infty} \dfrac{e^{-ix\xi}}{1+x^4}\,
   dx = \dfrac{\pi e^{-|\xi|/\sqrt 2}}{\sqrt 2}
   \bigg(\cos(\xi/\sqrt 2)+\sin(|\xi|/\sqrt 2) \bigg), \qquad \xi\in {{\mathbb  R}}.

--------------

**Lausn:** Fallið :math:`f` er jafnstætt og þar með :math:`\widehat f`
einnig, svo okkur dugir að reikna heildið út fyrir :math:`\xi\leq 0`.
Fallið :math:`f` hefur tvö einföld skaut í efra hálfplaninu. Þau eru
fjórðu rætur af :math:`-1` og eru því gefin með formúlunum
:math:`\alpha_1=(1+i)/\sqrt 2` og :math:`\alpha_2=(-1+i)/\sqrt 2`. Við
höfum

.. math::

  \max_{|z|=r}|f(z)| \leq  1/(r^4-1)\to 0, \qquad
   r\to+\infty.

og þar með gildir um öll :math:`\xi<0`,

.. math::

  \begin{aligned}
   \widehat f(\xi) = 2\pi i\bigg(
   {{\operatorname{Res}}}\big(\dfrac{e^{-iz\xi}}{1+z^4},\alpha_1\big) +
   {{\operatorname{Res}}}\big(\dfrac{e^{-iz\xi}}{1+z^4},\alpha_2\big)\bigg)
   =2\pi i\bigg(\dfrac{e^{-i\alpha_1\xi}}{4\alpha_1^3}+
   \dfrac{e^{-i\alpha_2\xi}}{4\alpha_2^3} \bigg).\end{aligned}

Nú notfærum við okkur að fjórðu rætur :math:`\alpha` af :math:`-1`
uppfylla :math:`\alpha^4=-1` og þar með :math:`1/\alpha^3=-\alpha`. Við
athugum jafnframt að
:math:`-i\alpha_1=\overline{(-i\alpha_2)}=(1-i)/\sqrt 2`. Þetta gefur
okkur

.. math::

  \begin{aligned}
   \widehat f(\xi) &= \dfrac{-\pi i}2\bigg(
   \alpha_1 e^{-i\alpha_1\xi}+\alpha_2 e^{-i\alpha_2\xi}\bigg)
   = \dfrac{\pi }2\bigg(
   -i\alpha_1 e^{-i\alpha_1\xi}-i\alpha_2 e^{-i\alpha_2\xi}\bigg)\\
   &= \dfrac{\pi}{\sqrt 2} {{\operatorname{Re\, }}}\big((1-i)  e^{(1-i)\xi/\sqrt 2}\big)
   = \dfrac{\pi e^{\xi/\sqrt 2}}{\sqrt 2} 
   \big(\cos(\xi/\sqrt 2)-\sin(\xi/\sqrt 2)\big).\end{aligned}

Nú notum við að :math:`\xi=-|\xi|` ef :math:`\xi\leq 0` og þar með er
niðurstaðan fengin.

.. end-toggle::

Andhverfar Fourier-myndir reiknaðar með leifareikningi.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur nú að :math:`f\in L^1({{\mathbb  R}})` og að við getum sýnt
fram á að Fourier-myndin :math:`\widehat f` eigi sér fágaða framlengingu
yfir í fall :math:`\widehat f\in {{\cal O}}({{\mathbb  C}}\setminus A)`,
þar sem :math:`A` er dreift mengi og skilgreinum vegina :math:`\gamma_r`
og :math:`\beta_r` eins og áður.

.. figure:: ./myndir/fig101.svg
    :align: center
    :alt: Hálfskífur í efra og neðra hálfplani

    Mynd: Hálfskífur í efra og neðra hálfplani

Ef :math:`A` sker ekki hringinn
:math:`\{z\in {{\mathbb  C}}\,;\, |z|=r\}`, þá fáum við

.. math::

  \begin{gathered}
   \dfrac 1{2\pi}\int_{-r}^{r}e^{ix\xi}\widehat f(\xi)\, d\xi 
   +\dfrac 1{2\pi}\int_{\gamma_r}e^{ix\zeta}\widehat f(\zeta)\, d\zeta =
   i\sum_{\alpha\in A\cap \Omega_r}{{\operatorname{Res}}}(e^{ix\zeta}\widehat
   f(\zeta),\alpha),\\
   \dfrac 1{2\pi}\int_{-r}^{r}e^{ix\xi}\widehat f(\xi)\, d\xi 
   +\dfrac 1{2\pi}\int_{\beta_r}e^{ix\zeta}\widehat f(\zeta)\, d\zeta =
   -i\sum_{\alpha\in A\cap
   \widetilde\Omega_r}{{\operatorname{Res}}}(e^{ix\zeta}\widehat f(\zeta),\alpha),\end{gathered}

Matið á veldisvísisfallinu verður nú fyrir :math:`\zeta=\xi+i\eta`,

.. math::

  |e^{ix\zeta}|
   =e^{{{\operatorname{Re\, }}}(ix\zeta)}=e^{-x\eta} \leq 1, \quad\text{
   ef }  \eta\geq 0 \text{ og } x\geq  0 \quad \text{ eða } 
   \quad \eta\leq 0 \text { og } x\leq 0.

Hjálparsetning Jordan gefur

.. math::

  \int_{\gamma_r}|e^{ix\zeta}|\, |d\zeta| <\dfrac\pi{x}, 
   \quad x>0, \qquad \text{ og } \qquad 
   \int_{\beta_r}|e^{ix\zeta}|\, |d\zeta| 
   <\dfrac\pi{-x}, \quad x<0,

og við fáum matið

.. math::

  \begin{aligned}
   \big|\int_{\gamma_r}e^{ix\zeta}\widehat f(\zeta)\, d\zeta\big|
   &\leq  \dfrac \pi x \, \max_{|\zeta|=r}|\widehat f(\zeta)|,  
   \qquad x>0 ,\label{16.7.8a}\\
   \big|\int_{\beta_r}e^{ix\zeta}\widehat f(\zeta)\, d\zeta\big|
   &\leq \dfrac \pi {(-x)} \, \max_{|\zeta|=r}|\widehat f(\zeta)|,  
   \qquad x<0.\label{16.7.9a}\end{aligned}

Niðurstaðan verðu því:

Setning
^^^^^^^

Gerum ráð fyrir því að
:math:`f\in L^1({{\mathbb  R}})\cap PC^1({{\mathbb  R}})`, að það sé
hægt að framlengja skilgreiningarsvæði Fourier–myndarinnar
:math:`\widehat f`, þannig að
:math:`\widehat f\in {{\cal O}}({{\mathbb  C}}\setminus A)`, þar sem
mengið :math:`A` er endanlegt, og
:math:`\max_{|\zeta|=r}|\widehat f(\zeta)|\to 0`, :math:`r\to +\infty`.
Þá er

.. math::

  \tfrac 12 (f(x+)+f(x-))=\begin{cases}
   i\sum\limits_{\alpha\in A\cap H_+}{{\operatorname{Res}}}\big(e^{ix\zeta}\widehat
   f(\zeta),\alpha\big), & x>0\\
   -i\sum\limits_{\alpha\in A\cap H_-}{{\operatorname{Res}}}\big(e^{ix\zeta}\widehat
   f(\zeta),\alpha\big), & x<0.
   \end{cases}

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Andhverfa Fourier–mynd fallsins :math:`F(\xi)=\xi/(\xi^2+4\xi+5)`
uppfyllir

.. math::

  \begin{aligned}
   f(x)=\lim_{R\to +\infty}\dfrac 1{2{\pi}}\int\limits_{-R}^R
   e^{ix\xi}\dfrac \xi{\xi^2+4\xi+5}\, d\xi
   = -\big(1-\tfrac 12 i{{\operatorname{sign}}}(x)\big)e^{-|x|-2ix}, \qquad x\in {{\mathbb  R}}.\end{aligned}

Fallið í hægri hliðinni er samfellt alls staðar, nema í :math:`x=0`.

--------------

**Lausn:** Fallið :math:`F` hefur tvö einföld skaut :math:`-2+i\in H_+` og
:math:`-2-i\in H_-`, og

.. math::

  \begin{gathered}
   i{{\operatorname{Res}}}\bigg( \dfrac{e^{ix\zeta}\zeta}{\zeta^2+4\zeta+5},-2+i\bigg)
   =\dfrac{ie^{ix(-2+i)}(-2+i)}{2(-2+i)+4}= (-1+i/2)e^{-x-2ix},\\
   -i{{\operatorname{Res}}}\bigg( \dfrac{e^{ix\zeta}\zeta}{\zeta^2+4\zeta+5},-2-i\bigg)
   =\dfrac{-ie^{ix(-2-i)}(-2-i)}{2(-2-i)+4}= (-1-i/2)e^{x-2ix}.\end{gathered}

Ef við tökum fallið í fyrri línunni þegar :math:`x>0` og fallið í
seinni línunni ef :math:`x<0`, þá getum við greinilega skrifað

.. math:: f(x)= -(1-i{{\operatorname{sign}}}(x)/2)e^{-|x|-2ix}.

.. end-toggle::

Andhverf Laplace–ummyndun 
--------------------------

Andhverf Laplace–ummyndun 
~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við sjá samhengið milli Fourier- og Laplace-ummynda. Látum
:math:`f` vera fall á
:math:`{{\mathbb  R}}_+=\{t\in {{\mathbb  R}}; t\geq 0\}` af
veldisvísisgerð, en samkvæmt skilgreiningu þýðir það
að til eru jákvæðir fastar :math:`M` og :math:`c` þannig að

.. math:: |f(t)|\leq Me^{c t}, \qquad t\in {{\mathbb  R}}_+.

Við sönnuðum við að Laplace–myndin
:math:`{{\cal L}}f({\zeta})` er fágað fall á hálfplaninu
:math:`\{{\zeta}\in {{\mathbb  C}}; {{\operatorname{Re\, }}}{\zeta}>c\}`.
Við framlengjum skilgreiningarsvæði fallsins :math:`f` yfir á allan
ásinn með því að setja :math:`f(t)=0` fyrir öll :math:`t<0` og sjáum þá
að

.. math::

  \begin{aligned}
   {{\cal L}}f(\zeta)&= 
   \int_{-\infty}^{+\infty} e^{-(\xi+i\eta)x} f(x) \, dx= 
   \int_{-\infty}^{+\infty} e^{-ix\eta}e^{-\xi x} f(x) \, dx
   \\
   &= {{\cal F}}\{e^{-\xi x}f(x)\}(\eta). \nonumber
    \end{aligned}

Nú festum við gildið á :math:`\xi` og lítum á þetta sem fall af
:math:`\eta` og fáum þá sem beina afleiðingu af andhverfuformúlu
Fouriers:

Setning
^^^^^^^

(*Andhverfuformúla Fourier–Mellin*).   Ef
:math:`f:{{\mathbb  R}}_+\to {{\mathbb  C}}` er samfellt deildanlegt á
köflum og uppfyllir :math:`|f(t)|\leq Me^{ct}`,
:math:`t\in {{\mathbb  R}}_+`, þar sem :math:`M` og :math:`c` eru
jákvæðir fastar, þá gildir um sérhvert :math:`\xi>c` og sérhvert
:math:`t>0` að

.. math::

  \begin{aligned}
    \label{7.2.2}
   \tfrac 12(f(t+)+f(t-))& = \lim_{R\to +\infty} \dfrac 1{2\pi}
   \int_{-R}^{+R}e^{(\xi+i\eta)t}{{\cal L}}f(\xi+i\eta) \, d\eta \\
   &= \lim_{R\to +\infty} \dfrac 1{2\pi i}
   \int_{\xi-iR}^{\xi+iR}e^{\zeta t}{{\cal L}}f(\zeta) \, d\zeta,\nonumber\end{aligned}

þar sem :math:`\int_{\xi-iR}^{\xi+iR}` táknar að heildað sé eftir
línustrikinu með upphafspunktinn :math:`\xi-iR` og lokapunktinn
:math:`\xi+iR`. Ef :math:`{{\cal L}}f(\xi+i\eta)` er í
:math:`L^ 1({{\mathbb  R}})` sem fall af :math:`\eta`, þá er :math:`f`
samfellt í :math:`t` og

.. math::

  \begin{aligned}
   f(t)&=  \dfrac 1{2\pi}
   \int_{-\infty}^{+\infty}e^{(\xi+i\eta)t}{{\cal L}}f(\xi+i\eta) \, d\eta
   \\
   &= \dfrac 1{2\pi i}
   \int_{\xi-i\infty}^{\xi+i\infty}e^{\zeta t}{{\cal L}}f(\zeta) \,
   d\zeta,\nonumber\end{aligned}

þar sem :math:`\int_{\xi-i\infty}^{\xi+i\infty}` táknar að heildað sé
eftir línunni :math:`\{\xi+i\eta; \eta\in {{\mathbb  R}}\}` í stefnu
vaxandi :math:`\eta`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við höfum að

.. math::

   {{\cal L}}f(\zeta) = {{\cal F}}\{e^{-\xi x}f(x)\}(\eta)

og því gefur andhverfuformúla Fouriers að

.. math::

  e^{-\xi t}\tfrac 12(f(t+)+f(t-)) = \lim_{R\to +\infty} \dfrac 1{2\pi}
   \int_{-R}^{+R}e^{i\eta t}{{\cal L}}f(\xi+i\eta) \, d\eta,

svo andhverfuformúlan fæst með því að margfalda þessa jöfnu með
:math:`e^{t\xi}`. Ef :math:`{{\cal L}}f(\xi+i\eta)` er í
:math:`L^ 1({{\mathbb  R}})` sem fall af :math:`\eta`, þá er heildið í hægri
hliðinni samfellt fall af :math:`t` og þar með einnig
vinstri hliðin. Fyrst :math:`f` er samfellt deildanlegt á köflum, þá
gefur andhverfuformúlan að :math:`f` er samfellt á
:math:`{{\mathbb  R}}_+`.

.. end-toggle::

Sem beina afleiðingu af andhverfuformúlunni fáum við nú að samfellt fall er
ótvírætt ákvarðað af Laplace–mynd sinni. Við athugum að setningin gildir
ekki ef sleppt er þeirri forsendu að föllin :math:`f` og :math:`g` séu
samfelld. Ástæðan er einfaldlega sú að Laplace mynd falls breytist ekki
við það að gildum þess sé breytt í einstökum punktum.

Sem eitt dæmi um gildi samsemdarsetningarinnar skulum við taka:

Setning
^^^^^^^

Látum :math:`f` og :math:`g` vera tvö samfelld föll af veldisvísisgerð á
:math:`{{\mathbb  R}}`, sem uppfylla :math:`|f(t)|\leq Me^{ct}` og
:math:`|g(t)|\leq Me^{ct}` fyrir :math:`t\in {{\mathbb  R}}_+`, og gerum
ráð fyrir að :math:`{{\cal L}}f(\alpha_j)={{\cal L}}g(\alpha_j)`, þar
sem :math:`\{\alpha_j\}` er runa af ólíkum punktum,
:math:`\alpha_j\to \alpha`, :math:`{{\operatorname{Re\, }}}\alpha_j >c`
og :math:`{{\operatorname{Re\, }}}\alpha >c`. Þá er :math:`f(t)=g(t)`
fyrir öll :math:`t\in {{\mathbb  R}}_+`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Föllin :math:`{{\cal L}}f` og :math:`{{\cal L}}g` eru fáguð á menginu
:math:`\{\zeta\in {{\mathbb  C}}; {{\operatorname{Re\, }}}\zeta >c\}` og því segir samsemdarsetning
okkur að :math:`{{\cal L}}f(\zeta)={{\cal L}}g(\zeta)` gildi um
alla punkta í þessu mengi. Nú gefur formúla Fourier-Mellin okkur að
:math:`f(t)=g(t)` fyrir öll :math:`t>0`. Fyrst bæði föllin eru samfelld
á :math:`{{\mathbb  R}}_+`, þá gildir jafnaðarmerki einnig ef
:math:`t=0`.

.. end-toggle::

Andhverf Laplace-ummyndun og leifareikningur
--------------------------------------------

Andhverf Laplace-ummyndun og leifareikningur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í útreikningum okkar höfum við oft séð dæmi þess að unnt er að útvíkka
skilgreiningarmengi :math:`{{\cal L}}f(\zeta)` frá hálfplaninu
:math:`H_c` yfir á allt planið utan við dreift mengi :math:`A` af
sérstöðupunktum. Sem dæmi getum við nefnt

.. math::

  {{\cal L}}\{\cos \beta t\}(\zeta) =\dfrac {\zeta}{\zeta^ 2+\beta^ 2},
   \qquad 
   {{\cal L}}\{\sin \beta t\}(\zeta) =\dfrac {\beta}{\zeta^ 2+\beta^ 2},

en báðar þessar Laplace-myndir eru skilgreindar á
:math:`{{\mathbb  C}}\setminus\{\pm i\beta\}`. Sjálfsagt er að beita leifareikningi til að reikna út
andhverfar Laplace–myndir með andhverfuformúlu Fourier-Mellin. Við skulum nú sjá hvernig þetta er framkvæmt.

.. figure:: ./myndir/fig103.svg
    :align: center
    :alt: Hálfhringur með upphafspunkt :math:`\xi+ir` og lokapunkt :math:`\xi-ir`

    Mynd: Hálfhringur með upphafspunkt :math:`\xi+ir` og lokapunkt :math:`\xi-ir`

Við látum :math:`M_r` vera hálfhringinn sem stikaður er með
:math:`\gamma_r(\theta)=\xi+ire^{i\theta}`, :math:`\theta\in [0,\pi]`
og
:math:`A_r=\{z\in{{\mathbb  C}}; |z-\xi|<r, {{\operatorname{Re\, }}}z<\xi\}`
vera mengið sem hann afmarkar ásamt línustrikinu milli endapunkta hans.
Ef engir sérstöðupunktar liggja á :math:`M_r`, þá gefur leifasetningin
okkur

.. math::

  \dfrac 1{2\pi i}\int_{\xi-ir}^{\xi+ir}e^{\zeta t}{{\cal L}}f(\zeta)\,
   d\zeta
   +\dfrac 1{2\pi i}\int_{\gamma_r}e^{\zeta t}{{\cal L}}f(\zeta)\, d\zeta=
   \sum_{\alpha\in A_r}{{\operatorname{Res}}}(e^{\zeta t}{{\cal L}}f(\zeta),\alpha).

Nú viljum við vita hvenær heildið yfir hálfhringinn stefnir á núll ef
:math:`r\to +\infty`. Í þessu tilfelli gefur hjálparsetning Jordan matið

.. math:: \int_{\gamma_r}|e^{\zeta t}||d\zeta|\leq \dfrac{\pi e^{\xi t}}{t}, \qquad t>0,

og af því leiðir

.. math::

  |\int_{\gamma_r}e^{\zeta t}{{\cal L}}f(\zeta)\, d\zeta|\leq
   \int_{\gamma_r}|e^{\zeta t}||d\zeta|
   \max_{\zeta\in M_r}|{{\cal L}}f(\zeta)|
   \leq \dfrac{\pi e^{\xi t}}{t}
   \max_{\zeta\in M_r}|{{\cal L}}f(\zeta)|

Út frá andhverfuformúlu Fourier–Mellin fáum við:

Setning
^^^^^^^

Látum :math:`f:{{\mathbb  R}}_+\to {{\mathbb  C}}` vera samfellt
deildanlegt á köflum og af veldisvísisgerð, með
:math:`|f(t)|\leq Me^{ct}`, :math:`t>0`, og gerum ráð fyrir að hægt sé
að framlengja :math:`{{\cal L}}f` yfir í fágað fall á
:math:`{{\mathbb  C}}\setminus A`, þar sem :math:`A` er endanlegt mengi.
Ef :math:`\xi>c`, :math:`M_r` táknar hálfhringinn sem stikaður er með
:math:`\gamma_r(\theta)=\xi+ire^{i\theta}`, :math:`\theta\in [0,\pi]`
og

.. math:: \max_{\zeta\in M_r}|{{\cal L}}f(\zeta)|\to 0, \qquad r\to +\infty,

þá er

.. math::

  \frac 12(f(t+)+f(t-))=
   \sum_{\alpha\in A}{{\operatorname{Res}}}(e^{\zeta t}{{\cal L}}f(\zeta),\alpha)
   \qquad t>0.

Ef :math:`f` er samfellt í :math:`t`, þá gildir

.. math:: f(t)= \sum_{\alpha\in A}{{\operatorname{Res}}}(e^{\zeta t}{{\cal L}}f(\zeta),\alpha).

--------------

Unnt er að skrifa Green–fallið
:math:`G(t,\tau)`, til þess að leysa jöfnuna

.. math:: P(D)u=(D^m+a_{m-1}D^{m-1}+\cdots+a_1D+a_0)u=f(t),

með upphafsskilyrðum, á forminu :math:`G(t,\tau)=g(t-\tau)`, þar sem
Laplace–mynd fallsins :math:`g` er gefin með

.. math:: {{\cal L}}g(\zeta)=\dfrac 1{P(\zeta)}.

Setning beint fyrir ofan gefur okkur þá að

.. math::

  g(t)= \sum\limits_{\alpha\in{\cal N}(P)} 
   {{\operatorname{Res}}}\bigg( \dfrac {e^{t\zeta}}{P(\zeta)},\alpha\bigg).

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Reiknum út Green–fallið fyrir virkjann
:math:`P(D)=(D-1)(D-2)(D-3)` með Fourier-ummyndun.

.. math::

  \begin{aligned}
   {{\operatorname{Res}}}\bigg(\dfrac{e^{t\zeta}}{(\zeta-1)(\zeta-2)(\zeta-3)},1\bigg)
   &=\dfrac{e^{t}}{(1-2)(1-3)}=\frac 12 e^t,\\
   {{\operatorname{Res}}}\bigg(\dfrac{e^{t\zeta}}{(\zeta-1)(\zeta-2)(\zeta-3)},2\bigg)
   &=\dfrac{e^{2t}}{(2-1)(2-3)}=-e^{2t},\\
   {{\operatorname{Res}}}\bigg(\dfrac{e^{t\zeta}}{(\zeta-1)(\zeta-2)(\zeta-3)},3\bigg)
   &=\dfrac{e^{3t}}{(3-1)(3-2)}=\frac 12e^{3t}.\end{aligned}

Eins og vænta mátti fáum við sömu niðurstöðu og áður

.. math:: g(t)=\tfrac 12\big(e^{t}-2e^{2t}+e^{3t}\big)

og þar með

.. math:: G(t,\tau)=\tfrac 12\big(e^{(t-\tau)}-2e^{2(t-\tau)}+e^{3(t-\tau)}\big).

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Notið Laplace–ummyndun og leifareikning til þess að finna Green–fall
virkjans :math:`D^4-2D^3+2D^2-2D+1`.

*Lausn*:  Green-fallið er gefið sem :math:`G(t,\tau)=g(t-\tau)`, þar sem
fallið :math:`g` uppfyllir :math:`{{\cal L}}\{g\}(\zeta)=1/P(\zeta)` og
:math:`P` er kennimargliða virkjans

.. math::

  P(\zeta)= \zeta^ 4-2\zeta^ 3+2\zeta^ 2-2\zeta+1 =
   (\zeta-1)^ 2(\zeta-i)(\zeta+i).

Við getum nú notað leifaformúluna

.. math::

  \begin{aligned}
   g(t)&= \sum\limits_{\alpha=1,i,-i} {{\operatorname{Res}}}\bigg(\dfrac{e^{\zeta t}}
   {(\zeta-1)^ 2(\zeta-i)(\zeta+i)},\alpha\bigg)\\
   &= \left.\dfrac d{d\zeta} \dfrac{e^{\zeta t}}{(\zeta-i)(\zeta+i)}
   \right|_{\zeta=1} + \dfrac{e^{it}}{(i-1)^ 2(2i)} +
    \dfrac{e^{-it}}{(-i-1)^ 2(-2i)}\\
   &= \left.\dfrac{te^{\zeta t}}{\zeta^ 2+1}\right|_{\zeta=1} 
   +\left.\dfrac{e^{\zeta t}(-2\zeta)}{(\zeta^ 2+1)^ 2}\right|_{\zeta=1} 
   +\dfrac{e^{it}}4+\dfrac{e^{-it}}4\\
   &=\tfrac 12 te^ t -\tfrac 12 e^ t +\tfrac 12\cos t.\end{aligned}

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Flokkið sérstöðupunkta fallsins

.. math::

  F(\zeta)=\dfrac{\zeta^2-(2+i)\zeta+(1+i)}
   {(\zeta^3-5\zeta^2+8\zeta-4)(\zeta^2-2\zeta+2)}

og reiknið út andhverfa Laplace–mynd þess leifareikningi.

*Lausn*:   Við finnum fullkomna þáttun nefnarans og teljarans í brotinu

.. math::

  F(\zeta)=\dfrac{(\zeta-1)(\zeta-(1+i))}
   {(\zeta-1)(\zeta-2)^ 2(\zeta-(1+i))(\zeta-(1-i))}.

Við sjáum að sérstöðupunktarnir eru :math:`\alpha=1`, :math:`\alpha=2`,
:math:`\alpha=1+i` og :math:`\alpha=1-i`. Við fullstyttum brotið og þá
stendur eftir

.. math::

  F(\zeta)=\dfrac{1}
   {(\zeta-2)^ 2(\zeta-(1-i))}.

Þetta segir okkur að sérstöðupunktarnir :math:`\alpha=1` og
:math:`\alpha=1+i` séu afmáanlegir, :math:`\alpha=1-i` sé skaut af stigi
:math:`1` og :math:`\alpha=2` sé skaut af stigi :math:`2`. Andhverfa
Laplace-myndin er

.. math::

  \begin{aligned}
   f(t) &=
   {{\operatorname{Res}}}\bigg( \dfrac{e^{\zeta t}}{(\zeta-2)^ 2(\zeta-(1-i))}, 1-i\bigg)
   +{{\operatorname{Res}}}\bigg( \dfrac{e^{\zeta t}}{(\zeta-2)^ 2(\zeta-(1-i))} , 2 \bigg)\\
   &= \dfrac{e^{(1-i)t}}{(1-i-2)^ 2}
   +\dfrac{d}{d\zeta}\bigg(\dfrac{e^{\zeta
   t}}{(\zeta-(1-i))}\bigg)_{\zeta=2}\\
   &= \dfrac{e^{(1-i)t}}{2i}+ \dfrac{te^{2t}}{1+i} -
   \dfrac{e^{2t}}{(1+i)^ 2}\\
   &=-\tfrac i2 e^{(1-i)t}+\tfrac {(1-i)}2te^{2t} -\tfrac i2 e^{2t}.\end{aligned}

.. end-toggle::

Sínus– og kósínus–ummyndanir
----------------------------

Sínus– og kósínus–ummyndanir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í reiknireglum (vii) og (viii) sáum við að

.. math:: {{\cal F}}f(\xi)=2\int_0^{+\infty}\cos(x\xi)f(x)\, dx,

ef fallið :math:`f` er jafnstætt og

.. math:: {{\cal F}}f(\xi)=-2i\int_0^{+\infty}\sin(x\xi)f(x)\, dx,

ef fallið :math:`f` er oddstætt. Ef fallið :math:`f` er ekki skilgreint
á öllum ásnum :math:`{{\mathbb  R}}` heldur einungis á
:math:`{{\mathbb  R}}_+=\{x\in {{\mathbb  R}}; x\geq 0\}`, þá eru
heildin í hægri hliðinni notuð til að skilgreina nýjar ummyndanir:

Skilgreining
^^^^^^^^^^^^

Ef :math:`f\in L^ 1({{\mathbb  R}}_+)`, þá kallast föllin

.. math::

  {{\cal F}}_c f(\xi)=\int_0^{+\infty}\cos(x\xi)f(x)\, dx \ \  \text{ og }
   \ \ 
   {{\cal F}}_s f(\xi)=\int_0^{+\infty}\sin(x\xi)f(x)\, dx, \ \  \xi\in {{\mathbb  R}}

*kósínus–mynd* og *sínus-mynd* fallsins :math:`f` og varpanirnar
:math:`{{\cal F}}_c` og :math:`{{\cal F}}_s` sem úthluta sérhverju falli
:math:`f\in L^ 1({{\mathbb  R}}_+)` samfelldu föllunum
:math:`{{\cal F}}_cf` og :math:`{{\cal F}}_sf` kallast
*kósínus–ummyndun* og *sínus–ummyndun*.

--------------

Við fáum hér enn eitt afbrigðið af andhverfuformúlunni:

Setning
^^^^^^^

(*Andhverfuformúla Fouriers* ).   Gerum ráð fyrir að
:math:`f\in L^ 1({{\mathbb  R}}_+)` og að
:math:`{{\cal F}}_cf, {{\cal F}}_sf\in L^ 1({{\mathbb  R}}_+)`. Þá er

.. math::

  \begin{gathered}
   f(x) = \dfrac 2\pi\int_0^ {+\infty} \cos(x\xi) {{\cal F}}_cf(\xi)\, d\xi,
   \qquad x > 0,\\
   f(x) = \dfrac 2\pi\int_0^ {+\infty} \sin(x\xi) {{\cal F}}_sf(\xi)\, d\xi,
   \qquad x> 0.\end{gathered}

Ef :math:`f\in L^ 1({{\mathbb  R}}_+)\cap PC^1({{\mathbb  R}}_+)`, þá
gildir

.. math::

  \begin{gathered}
   \tfrac 12(f(x+)+f(x-)) = \lim_{R\to +\infty}
   \dfrac 2\pi\int_0^ {R} \cos(x\xi) {{\cal F}}_cf(\xi)\, d\xi,
   \qquad x > 0,\\
   \tfrac 12(f(x+)+f(x-))  
   = \lim_{R\to +\infty} \dfrac 2\pi\int_0^ {R} 
   \sin(x\xi) {{\cal F}}_sf(\xi)\, d\xi, \qquad x> 0.\end{gathered}

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við framlengjum :math:`f` yfir í jafnstætt fall
:math:`\tilde f\in L^ 1({{\mathbb  R}})`, en það þýðir að
:math:`\tilde f(x)=f(-x)` ef :math:`x<0`. Þá er
:math:`{{\cal F}}\tilde f` jafnstætt fall og þar með er

.. math::

  \begin{aligned}
   f(x)&=\dfrac 1{2\pi}\int_{-\infty}^ {+\infty}
   e^{ix\xi}{{\cal F}}\tilde f(\xi) \, d\xi
   =\dfrac 1{\pi}\int_{0}^ {+\infty}
   \cos(x\xi){{\cal F}}\tilde f(\xi) \, d\xi\\
   &=\dfrac 2{\pi}\int_{0}^ {+\infty}
   \cos(x\xi){{\cal F}}_cf(\xi) \, d\xi.\end{aligned}

Seinni andhverfuformúlan fyrir :math:`{{\cal F}}_cf` er sönnuð út frá
andhverfuformúlunni fyrir :math:`\cal F f`. Formúlurnar fyrir :math:`{{\cal F}}_sf` eru
sannaðar með því að framlengja :math:`f` yfir í oddstætt fall á
:math:`{{\mathbb  R}}`.

.. end-toggle::

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Teiknið upp gröf eftirfarandi falla og reiknið út Fourier-myndir þeirra:

.. math::

  \begin{aligned}
   \text{a.}\quad 
   f(x)&=\begin{cases}  1,  &|x|\leq 1,\\  0,  &|x|>1,\end{cases} &
   \qquad\text{b.} \quad 
   f(x)&=\begin{cases}  x,  &0\leq x\leq 1,\\  0,
   &\text{annars},\end{cases} \\
   \text{c.} \quad 
   f(x)&=\begin{cases}  1-x,  &0\leq x\leq 1,\\ 0,
   &\text{annars},\end{cases} &
   \qquad
   \text{d.} \quad 
   f(x)&=\begin{cases}  1-|x|,  &|x|\leq 1,\\  0,  &|x|>1,\end{cases} \\
   \text{e.}\quad 
   f(x)& =\begin{cases}  1-x^2,  &|x|\leq 1,\\  0,  &|x|>1.\end{cases} &
   \qquad
   \text{f.} \quad
   f(x)&=\begin{cases} c, &x\in [a,b],\\ 0, &x\not\in [a,b],\end{cases} \\
   \text {g.}  \quad
   f(x)&=\begin{cases} (x-a)/(c-a), &x\in [a,c],\\ 
   (b-x)/(b-c), &x\in [c,b],\\ 0, &x\not\in [a,b].\end{cases} & &\end{aligned}

Dæmi
^^^^

Sannið reiknireglur (i)–(vi) og (viii).

Dæmi
^^^^

Notið niðurstöðuna úr :ref:`sýnidæmi <synokkurfouriersynidaemi>` og andhverfuformúluna til þess að sýna
að:

a)

.. math::

  \dfrac 2{\pi} \int\limits_{0}^{+\infty}
   \dfrac {1-\cos {\xi}}{{\xi}^2} \cos (x{\xi})\, d{\xi} =
   \begin{cases} 1-|x|, &|x|\leq 1, \\ 0, & |x|>1.\end{cases}

b)

.. math::

  \dfrac 2{\pi} \int\limits_{0}^{+\infty}
   \dfrac {\sin {\xi}}{\xi} \cos (x{\xi})\, d{\xi} =
   \begin{cases} 1, &|x|< 1, \\ 1/2, & |x|=1,\\ 0, & |x|>1.\end{cases}

c)

.. math:: \int_0^{+{\infty}} \dfrac {\sin^2{\xi}}{\xi^2}\, d{\xi} = \dfrac {\pi}2.

d)

.. math::

  \int_0^{+{\infty}} \dfrac {\cos(x{\xi})}{1+{\xi}^2} \, d{\xi}
   =\dfrac {\pi}2 e^{-|x|}.

Dæmi
^^^^

Notið niðurstöðurnar úr sýnidæmunum, reiknireglurnar og
andhverfuformúluna til þess að reikna út Fourier-myndir fallanna:

+---------------------------------------------------------------------------------------------------------------+--------------------------------------------+
| \a. :math:`f(x)= \dfrac{e^{ix}}{1+2x^2}`,                                                                     | \b. :math:`f(x)= x^4e^{-x^2}`,             |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------+
| \c. :math:`f(x)= e^{-{\alpha}x^2-{\beta}x}`, :math:`{\alpha},{\beta}\in {{\mathbb  R}}`, :math:`{\alpha}>0`,  | \d. :math:`f(x)= xe^{-|x|}`,               |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------+
| \e. :math:`f(x)= \dfrac{x}{1+x^2}`,                                                                           | \f. :math:`f(x)= \dfrac{x^2}{(1+x^2)^2}`,  |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------+
| \g. :math:`f(x)= \dfrac{1}{(1+x^2)^2}`,                                                                       | \h. :math:`f(x)=e^{-|x|}\cos x`,           |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------+
| \i. :math:`f(x)=e^{-|x|}\sin |x|`,                                                                            | \j. :math:`f(x)=1/(x^4+4)`.                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------+

Dæmi
^^^^

Beitið andhverfuformúlunni og reiknireglunum til þess að ákvarða fallið
:math:`f`, þar sem:

+-------------------------------------------------------+--------------------------------------------------------+------------------------------------------------------+
| \a. :math:`\widehat f({\xi})= e^{2i{\xi}-4|{\xi}|}`,  | \b. :math:`\widehat f({\xi})= {\xi}e^{-({\xi}-3)^2}`,  | \c. :math:`\widehat f({\xi})= |{\xi}|e^{-|{\xi}|}`.  |
+-------------------------------------------------------+--------------------------------------------------------+------------------------------------------------------+

Dæmi
^^^^

Ljúkið við sönnunina á hjálparsetningu Riemanns og Lebesgues með því að
sanna:

\(i) Fyrir sérhvert :math:`a,b\in {{\mathbb  R}}`, :math:`a<b`, gildir

.. math:: \int_a^b e^{-ix{\xi}}\, dx\to 0, \qquad {\xi}\to\pm{\infty}.

\(ii) Fyrir sérhvert þrepafall :math:`v` á bilinu :math:`[-a,a]`,
:math:`a>0`, gildir

.. math:: \int_{-a}^a e^{-ix{\xi}}v(x) \, dx\to 0, \qquad {\xi}\to\pm{\infty},

\(iii) Ef :math:`f\in L^1({{\mathbb  R}})` og :math:`\varepsilon>0`, þá
er til :math:`a>0` og þrepafall :math:`v` þannig að

.. math::

  \int_{|x|\geq a} |f(x)|\, dx <\varepsilon 
   \qquad \text{ og } \qquad
   \int_{-a}^a |f(x)-v(x)|\, dx <\varepsilon.

Notið þessar niðurstöður til þess að ljúka sönnuninni.

Dæmi
^^^^

Er til fall :math:`f\in L^1({{\mathbb  R}})` þannig að
:math:`\widehat f({\xi})=1-\sin {\xi}`?

Dæmi
^^^^

Látum :math:`f_n, f\in L^1({{\mathbb  R}})`, :math:`n=1,2,3,\dots`, og
gerum ráð fyrir að

.. math::

  \int_{-{\infty}}^{+{\infty}} |f_n(x)-f(x)|\, dx \to 0, \qquad n\to
   +{\infty}.

Sýnið að :math:`\widehat f_n\to \widehat f` í jöfnum mæli á
:math:`{{\mathbb  R}}`.

Dæmi
^^^^

Beitið leifareikningi til þess að ákvarða Fourier–myndir:

+-------------------------------------------+----------------------------------------------+
| \a. :math:`f(x)=\dfrac 1{(1+x^2)^3}`,     | \b. :math:`f(x)=\dfrac 1{1+x^6}`,            |
+-------------------------------------------+----------------------------------------------+
| \c. :math:`f(x)=\dfrac x{(x^2-2x+2)^2}`,  | \d. :math:`f(x)=\dfrac{1+x^2}{1+x^4}`,       |
+-------------------------------------------+----------------------------------------------+
| \e. :math:`f(x)=\dfrac {x^3}{1+x^6}`,     | \f. :math:`f(x)=\dfrac 1{1+x+x^2+x^3+x^4}`.  |
+-------------------------------------------+----------------------------------------------+

[*Leiðbeining:* Í f)-lið eru skautin fimmtu rætur af :math:`1`.]

Dæmi
^^^^

Reiknið út andhverfar Fourier-myndir fallanna:

+-----------------------------------------------------+-------------------------------------------------------------+
| \a. :math:`F({\xi})=\dfrac {\xi}{\xi^2+2{\xi}+2}`,  | \b. :math:`F({\xi})=\dfrac {\xi^3}{({\xi}^2+4{\xi}+5)^2}.`  |
+-----------------------------------------------------+-------------------------------------------------------------+

Dæmi
^^^^

Leysið földunarjöfnurnar:

a)

.. math::

  \int_{-{\infty}}^{+{\infty}} u(x-y)e^{-2y^2}\, dy = e^{-x^2},

b)

.. math::

  \int_{-\infty}^{+\infty}u(x-t)u(t)\, dt = e^{-x^2}.

c)

.. math::

  u(x)+\int_{-{\infty}}^{+{\infty}}  e^{-|x-y|}u(y)\, dy =xe^{-|x|}.

Dæmi
^^^^

Setjum :math:`f(x)=1/(1+x^2)`.

a) Reiknið út :math:`f\ast f` með því að beita Fourier–ummyndun.

b) Reiknið út :math:`f\ast \cdots\ast f`, þar sem þættirnir eru :math:`n` talsins.

Dæmi
^^^^

Reiknið út heildið

.. math:: \int_{-{\infty}}^{+{\infty}} \dfrac{dy}{(1+4(x-y)^2)(1+y^2)}.

Dæmi
^^^^

Látum :math:`f\in L^1({{\mathbb  R}})\cap C({{\mathbb  R}})` og gerum
ráð fyrir að :math:`\widehat f({\xi})=0` ef :math:`|{\xi}|\geq 1`. Sýnið
að :math:`f` sé :hover:`eiginfall` földunarvirkjans :math:`T`,
sem skilgreindur er með formúlunni

.. math:: Tu(x)=\int_{-{\infty}}^{+{\infty}} \dfrac{\sin(x-y)}{x-y} u(y)\, dy

Hvert er :hover:`eigengildið, eigingildi`?

Dæmi
^^^^

Látum :math:`f` vera fallið sem hefur Fourier-myndina

.. math::

  \widehat f({\xi})=\begin{cases} \sqrt{1-{\xi}^2}, &|{\xi}|\leq 1,\\
   0, &|{\xi}|>1.\end{cases}

Sýnið að :math:`f` uppfyllið afleiðujöfnuna

.. math:: t f{{^{\prime\prime}}}+3f{{^{\prime}}}+tf=0.

Setjið :math:`f` fram með veldaröð.

Dæmi
^^^^

Jafnan

.. math:: f{{^{\prime}}}(x)+f(x)+f(x+2) =\dfrac 1{1+x^2}, \qquad x\in {{\mathbb  R}},

hefur heildanlega lausn. Ákvarðið Fourier-mynd hennar.

Dæmi
^^^^

Reiknið út andhverfu Fourier-myndina :math:`E` af fallinu
:math:`{\xi}\mapsto 1/P(i{\xi})`, skrifið lausnina :math:`u` á jöfnunni
:math:`P(D)u=f` sem földunarheildi og reiknið það út í sértilfellinu
:math:`f(x)=H(x)xe^{-x}`.

+--------------------------------------------------------+-----------------------------------------------+
| \a. :math:`P({\zeta})={\zeta}^2+2{\zeta}+1`,           | \b. :math:`P({\zeta})={\zeta}^2-1`,           |
+--------------------------------------------------------+-----------------------------------------------+
| \c. :math:`P({\zeta})={\zeta}^3+{\zeta}^2-{\zeta}-1`,  | \d. :math:`P({\zeta})={\zeta}^2+2{\zeta}+5`.  |
+--------------------------------------------------------+-----------------------------------------------+

Dæmi
^^^^

Skrifið upp Plancherel-formúluna fyrir fallið :math:`f(x)=1/(1+x^2)` og
notið hana til þess að ákvarða heildið

.. math:: \int_{-{\infty}}^{+{\infty}} \dfrac {dx}{(1+x^2)^2}.

Dæmi
^^^^

Notið niðurstöðuna úr :ref:`sýnidæmi <synokkurfouriersynidaemi>`, andhverfuformúlu Fouriers og
Plancherel–jöfnuna til þess sýna að

.. math::

  \int_0^{+\infty} \dfrac {\sin x}x \, dx=\dfrac {\pi}2, \qquad 
   \int_0^{+\infty} \dfrac {\sin^ 2 x}{x^ 2} \, dx=\dfrac {\pi}2,
   \qquad  
   \int_0^{+\infty} \dfrac {\sin^ 4 x}{x^ 4} \, dx=\dfrac {\pi}3.

Dæmi
^^^^

Notið formúlu Parsevals til þess að reikna út heildið

.. math:: \int_{-{\infty}}^{+{\infty}} \dfrac{\sin x} x e^{-|x|} \, dx.

Dæmi
^^^^

Flokkið sérstöðupunkta fallanna sem gefin eru og reiknið út andhverfa
Laplace–mynd þeirra með leifareikningi:

a) :math:`F({\zeta})=\dfrac 1{({\zeta}+3)}-\dfrac 2{({\zeta}+3)^2} +\dfrac 1{({\zeta}+3)^3}`,

b) :math:`F({\zeta})=\dfrac 1{\zeta^3({\zeta}^2+1)}`,

c) :math:`F({\zeta})=\dfrac{{\zeta}-2} {({\zeta}^2-3{\zeta}+2)({\zeta}-1)({\zeta}^2+1)}`,

Dæmi
^^^^

Notið Laplace–ummyndun og leifareikning til þess að finna Green–föll
virkjanna:

+----------------------------------+------------------------------------+
| \a. :math:`D^ 2+\omega^ 2`,      | \b. :math:`(D^ 2+4)(D^ 2+9)`,      |
+----------------------------------+------------------------------------+
| \c. :math:`D^3+D^2+3D-5`,        | \d. :math:`D^4-D^2+2D+2`,          |
+----------------------------------+------------------------------------+
| \e. :math:`(D^2+1)(D-1)(D-2)`,   | \f. :math:`D^4-2D^3+2D^2-2D+1`.    |
+----------------------------------+------------------------------------+
| \g. :math:`D^2+4D+8`,            | \h. :math:`D^3-4D^2+5D-2`,         |
+----------------------------------+------------------------------------+
| \i. :math:`D^4-D^2+2D+2`.        |                                    |
+----------------------------------+------------------------------------+
