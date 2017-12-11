=-0.4truecm =-1truecm =16truecm =23truecm =0truecm

#1#2 #1#2 0 1 0 = -1 0 by-1 1 = 1 2 = -0 2 by100 = 1 100 by2 100 by1 1 1
=-100 0 [section] [setning+] Skilgreining [setning+] Setning og
skilgreining [setning+] Hjálparsetning [setning+] Fylgisetning
[setning+] Sýnidæmi [setning+] Forrit

[1]*#1:*\ :math:`\blacksquare`

#1\ **#1.**   #1\ **#1.**   #1\ **#1.**

FÁGUÐ FÖLL
==========

Markgildi og samfelld föll
--------------------------

Skífur og hringir
~~~~~~~~~~~~~~~~~

Áður en lengra er haldið skulum við innleiða rithátt fyrir skífur. *Opna
skífu:hover:‘opin skífa‘:hover:‘skífa!opin‘* með miðju :math:`\alpha` og
geisla :math:`\varrho` táknum við með

.. math:: S(\alpha,\varrho)=\{z\in {{\mathbb  C}}; |z-\alpha|<\varrho\},

 *lokaða skífu:hover:‘lokuð skífa‘:hover:‘skífa!lokuð‘* með miðju
:math:`\alpha` og geisla :math:`\varrho` táknum við með

.. math:: \overline S(\alpha,\varrho)=\{z\in {{\mathbb  C}}; |z-\alpha|\leq\varrho\}

 og *gataða opna skífu:hover:‘götuð opin skífa‘:hover:‘skífa!götuð
opin‘* með miðju :math:`\alpha` og geisla :math:`\varrho` táknum við með

.. math:: S^\ast(\alpha,\varrho)=\{z\in {{\mathbb  C}}; 0<|z-\alpha|<\varrho\}.

Athugið að fallið
:math:`[a,b]\ni \theta\mapsto \alpha+\varrho e^{i\theta}` stikar
hringboga með miðju :math:`\alpha` og geislann :math:`\varrho` frá
punktinum :math:`\alpha+\varrho e^{ia}` til punktsins
:math:`\alpha+\varrho e^{ib}` og að það stikar heilan hring ef
:math:`b-a=2\pi`.

Opin og lokuð mengi
~~~~~~~~~~~~~~~~~~~

Hlutmengi :math:`X` í :math:`{{\mathbb  C}}` er sagt vera *opið* ef um
sérhvern punkt :math:`a\in X` gildir að til er opin skífa :math:`S(a,r)`
sem er innihaldin í :math:`X`. Hlutmengi :math:`X` í
:math:`{{\mathbb  C}}` er sagt vera *lokað* ef fyllimengi þess
:math:`{{\mathbb  C}}\setminus X` er opið. Þá er ljóst að mengi
:math:`X` er lokað þá og því aðeins að um sérhvern punkt :math:`a` í
fyllimenginu :math:`{{\mathbb  C}}\setminus X` gildir að til er
:math:`r>0` þannig að :math:`S(a,r)\subset {{\mathbb  C}}\setminus X`.

*Jaðar* hlutmengis :math:`X` í :math:`{{\mathbb  C}}` samanstendur af
öllum punktum :math:`a\in {{\mathbb  C}}` þannig að sérhver opin skífa
:math:`S(a,r)` með :math:`r>0` sker bæði :math:`X` og
:math:`{{\mathbb  C}}\setminus X`. Við táknum jaðar :math:`X` með
:math:`\partial X`. Ef :math:`X` er opið, þá er
:math:`\partial X\subset {{\mathbb  C}}\setminus X`. Ef :math:`X` er
lokað, þá er :math:`\partial X\subset X`.

Punktur :math:`a\in {{\mathbb  C}}` nefnist *þéttipunktur* mengisins
:math:`X` ef um sérhvert :math:`r>0` gildir að gataða opna skífan
:math:`S^\ast(a,r)` inniheldur punkta úr :math:`X`.

Hlutmengi :math:`X` í :math:`{{\mathbb  C}}` er sagt vera
*samanhangangi* ef um sérhverja tvo punkta :math:`a` og :math:`b` í
:math:`X` gildir að til er samfelldur ferill
:math:`[0,1]\ni t\mapsto \gamma(t)\in {{\mathbb  C}}` sem er innihaldinn
í :math:`X`. Opið samanhangandi mengi nefnist *svæði*.

Athugið að sérhver opin skífa er svæði, því sérhverja tvo punkta í henni
má tengja saman með línustriki. Lokaðar skífur eru ferilsamanhangandi,
og sama er að segja um gataðar skífur.

Markgildi
~~~~~~~~~

Látum nú :math:`X` vera hlutmengi í :math:`{{\mathbb  C}}` og
:math:`f:X\to {{\mathbb  C}}` vera fall. Við segjum að :math:`f(z)`
stefni á tvinntöluna :math:`L` þegar :math:`z` stefnir á :math:`a`, ef
:math:`a` er þéttipunktur í :math:`X` og fyrir sérhvert
:math:`\varepsilon>0` gildir að til er :math:`\delta>0` þannig að

.. math:: |f(z)-L|<\varepsilon \qquad \text{ fyrir öll } z\in X\cap S^\ast(a,\delta).

 Við köllum þá töluna :math:`L` *markgildi :math:`f` þegar :math:`z`
stefnir á :math:`a`* og skrifum

.. math::

   \lim_{z\to a}f(z)=L  \qquad \text{ eða } \quad f(z)\to L \text{ ef }
   z\to a.

 Við höfum nokkrar reiknireglur fyrir markgildi: Ef :math:`f` og
:math:`g` eru tvinngild föll sem skilgreind eru á menginu :math:`X`,
:math:`\lim_{z\to a}f(z)=L` og :math:`\lim_{z\to a}g(z)=M`, þá er

.. math::

   \begin{gathered}
   \lim_{z\to a}(f(z)+g(z))=\lim_{x\to a}f(z)+\lim_{x\to a}g(z)=L+M,\\
   \lim_{z\to a}(f(z)-g(z))=\lim_{x\to a}f(z)-\lim_{x\to a}g(z)=L-M,\\
   \lim_{z\to a}(f(z)g(z))=\big(\lim_{x\to a}f(z)\big)\big(\lim_{x\to
   a}g(z)\big)=LM\\
   \lim_{z\to a}\dfrac{f(z)}{g(z)}=\dfrac{\lim_{x\to a}f(z)}{\lim_{x\to
   a}g(z)}=\dfrac LM.\end{gathered}

 Í síðustu formúlunni þarf að gera ráð fyrir að :math:`M\neq 0`.

Samfelldni
~~~~~~~~~~

Fallið :math:`f:X\to {{\mathbb  C}}` er sagt vera samfellt í punktinum
:math:`a\in X` ef

.. math:: \lim_{z\to a}f(z)=f(a).

Af reiknireglunum fyrir markgildi leiðir að ef :math:`f` og :math:`g`
eru föll á mengi :math:`X` með gildi í :math:`{{\mathbb  C}}` sem eru
samfelld í punktinum :math:`a\in X`, þá eru :math:`f+g`, :math:`f-g`,
:math:`fg` og :math:`f/g` samfelld í :math:`a` og

.. math::

   \begin{gathered}
   \lim_{x\to a}(f(z)+g(z))=f(a)+g(a),\\
   \lim_{x\to a}(f(z)-g(z))=f(a)-g(a),\\
   \lim_{x\to a}(f(z)g(z))=f(a)g(a),\\
   \lim_{x\to a}\dfrac{f(z)}{g(z)}=\dfrac{f(a)}{g(a)}, 
   \qquad \text{ef } \ g(a)\neq 0.\end{gathered}

 Ef :math:`f:X\to {{\mathbb  C}}` og :math:`g:Y\to {{\mathbb  C}}` eru
föll, :math:`f(X)\subset Y`, :math:`a` er þéttipunkur :math:`X`,
:math:`b=\lim_{z\to a}f(z)` er þéttipunktur mengisins :math:`Y` og
:math:`g` er samfellt í :math:`b`, þá er

.. math:: \lim_{z\to a} g\circ f(z)=g(\lim_{z\to a}f(z)).

Ritháttur fyrir hlutafleiður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f` er fall af breytistærðunum :math:`x,y,z,\dots`, þá skrifum
við

.. math::

   {\partial}_xf=\dfrac{\partial f}{\partial x}, \qquad
   {\partial}_yf=\dfrac{\partial f}{\partial y}, \qquad
   {\partial}_zf=\dfrac{\partial f}{\partial z}, \ \dots

 og hærri afleiður táknum við með

.. math::

   {\partial}_x^2f=\dfrac{\partial^2f}{\partial x^2}, \qquad
   {\partial}_{xy}^2f=\dfrac{\partial^2f}{\partial x\partial y}, \qquad
   {\partial}_{xxy}^3f=\dfrac{\partial^3f}{\partial x^2\partial y}, \ \dots.

Í mörgum bókum eru hlutafleiður skrifaðar sem :math:`f_{x}`, :math:`f_y`
o.s.frv. Þessi ritháttur hentar okkur illa, því við notum lágvísinn til
þess að tákna ýmislegt annað en hlutafleiður. Mun skýrari ritháttur, sem
við notum þó ekki, er að tákna hlutafleiður með :math:`f_x'`,
:math:`f_y'` o.s.frv.

Samfellt deildanleg föll
~~~~~~~~~~~~~~~~~~~~~~~~

Við fjöllum mikið um samfelld og deildanleg föll og þess vegna er mjög
hagkvæmt að innleiða rithátt fyrir mengi allra falla sem eru samfelld á
einhverju mengi. Ef :math:`X` er opið hlutmengi í :math:`{{\mathbb  C}}`
þá látum við :math:`C(X)` tákna mengi allra samfelldra falla
:math:`f:X\to {{\mathbb  C}}`. Það er til mikilla þæginda að gera frá
byrjun ráð fyrir að föllin séu tvinntölugild. Við látum
:math:`C\sp m(X)` tákna mengi allra :math:`m` sinnum samfellt
deildanlegra:hover:‘samfellt deilanlegur‘ falla. Hér er átt við að allar
hlutafleiður fallsins :math:`f` af stigi :math:`\leq m` eru til og þar
að auki samfelldar. Við skrifum :math:`C^0(X)=C(X)` og táknum mengi
óendanlega oft deildanlegra falla með :math:`C^{\infty}(X)`.

Fáguð föll
----------

Látum :math:`f:X\to {{\mathbb  C}}` vera fall á opnu hlutmengi :math:`X`
af :math:`{{\mathbb  C}}`. Ef við látum :math:`z` tákna tvinnbreytistærð
með gildi í :math:`X`, þá getum við skrifað

.. math::

   f(z)=u(z)+iv(z)=u(x,y)+iv(x,y), \qquad z=x+iy=(x,y) \in X,


   .. _4.2.1:

 þar sem föllin :math:`u={{\operatorname{Re\, }}}f` og
:math:`v={{\operatorname{Im\, }}}f` eru raunhluti og þverhluti fallsins
:math:`f`. Við getum þá jafnframt litið á :math:`f` sem vigurgilt fall
af tveimur raunbreytistærðum

.. math::

   f:X\to {{\mathbb  R}}\sp 2, \qquad f(x,y)=(u(x,y), v(x,y)).


   .. _4.2.2:

 Hugtök eins og samfelldni, deildanleiki og heildanleiki eru skilgreind
eins og venjulega fyrir vigurgild föll. Þetta þýðir að :math:`f` er
samfellt á :math:`X`, :math:`f\in C(X)`, þá og því aðeins að föllin
:math:`u` og :math:`v` séu samfelld á :math:`X`, :math:`u,v\in C(X)`.
Eins er :math:`f` :math:`k`–sinnum samfellt deildanlegt á :math:`X`,
:math:`f\in C\sp k(X)` þá og því aðeins að :math:`u,v\in C\sp k(X)` og
við skilgreinum hlutafleiður af :math:`f` sem tvinnföllin

.. math::

   \begin{gathered}
   \partial_xf=\partial_xu+i\partial_xv, \qquad
   \partial_yf=\partial_yu+i\partial_yv,\\
   \partial\sp 2_xf=\partial\sp 2_xu+i\partial\sp 2_xv, \qquad
   \partial\sp 2_{xy}f=\partial\sp 2_{xy}u+i\partial\sp 2_{xy}v,\qquad
   \partial\sp 2_yf=\partial\sp 2_yu+i\partial\sp 2_yv.\end{gathered}

 Þannig er síðan haldið áfram eftir því sem deildanleiki :math:`u` og
:math:`v` endist. Nú ætlum við að innleiða nýtt deildanleikahugtak, þar
sem við lítum á breytistærðina sem *tvinntölu:hover:‘tvinntala‘* en ekki
sem vigur:

:math:`{{\mathbb  C}}`-deildanleg föll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Látum :math:`f:X\to {{\mathbb  C}}` vera fall á opnu hlutmengi :math:`X`
af :math:`{{\mathbb  C}}`. Við segjum að :math:`f` sé
*:math:`{{\mathbb  C}}`–deildanlegt:hover:‘:math:`{{\mathbb  C}}`-deildanlegur‘*
í punktinum :math:`a\in X` ef markgildið

.. math::

   \lim _{\substack{ h\to 0\\ h\in{{\mathbb  C}}}}
    \dfrac{f(a+h)-f(a)}h  

   .. _4.2.3:

 er til. Markgildið táknum við með :math:`f{{\sp{\prime}}}(a)` og köllum
það
*:math:`{{\mathbb  C}}`–afleiðu:hover:‘:math:`{{\mathbb  C}}`-afleiða‘*
fallsins :math:`f` í punktinum :math:`a`. Fall
:math:`f:X\to {{\mathbb  C}}` er sagt vera *fágað:hover:‘fágað fall‘* á
opna menginu :math:`X` ef :math:`f\in
C^1(X)` og :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í sérhverjum
punkti í :math:`X`. Við látum :math:`{{\cal O}}(X)` tákna mengi allra
fágaðra falla á :math:`X`. Við segjum að :math:`f` sé *fágað í punktinum
:math:`a`* ef til er opin grennd :math:`U` um :math:`a` þannig að
:math:`f` sé fágað í :math:`U`. Fallið :math:`f` er sagt vera *heilt
fall* ef það er fágað á öllu :math:`{{\mathbb  C}}`.

Þessi skilgreining er eins og skilgreiningin af afleiðu falls af einni
raunbreytistærð.

.. \_se:sammfelldni:

Setning
^^^^^^^

Ef :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a`, þá er
:math:`f` samfellt í :math:`a`.

Reiknireglur fyrir :math:`{{\mathbb  C}}`-afleiður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reiknireglurnar fyrir :math:`{{\mathbb  C}}`-afleiður eru nánast þær
sömu og reiknireglurnar fyrir afleiður falla af einni raunbreytistærð.
Við tökum sannanirnar á þeim fyrir aftast í kaflanum:

.. \_set4.2.3:

Setning
^^^^^^^

Látum :math:`f,g:X\to {{\mathbb  C}}` vera föll, :math:`a\in X`,
:math:`\alpha,\beta\in {{\mathbb  C}}` og gerum ráð fyrir að :math:`f`
og :math:`g` séu :math:`{{\mathbb  C}}`–deildanleg í :math:`a`. Þá
gildir

(i) :math:`\alpha f+\beta g` er :math:`{{\mathbb  C}}`–deildanlegt í
:math:`a` og

.. math:: (\alpha f+\beta g){{\sp{\prime}}}(a)=\alpha f{{\sp{\prime}}}(a)+\beta g{{\sp{\prime}}}(a).

(ii) (*Leibniz-regla:hover:‘regla Leibniz‘:hover:‘Leibniz‘*). :math:`fg`
er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math:: (fg){{\sp{\prime}}}(a)=f{{\sp{\prime}}}(a)g(a)+f(a)g{{\sp{\prime}}}(a).

(iii) Ef :math:`g(a)\neq 0`, þá er :math:`f/g`
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math:: (f/g){{\sp{\prime}}}(a)=\dfrac{f{{\sp{\prime}}}(a)g(a)-f(a)g{{\sp{\prime}}}(a)}{g(a)^2}.

Fylgisetning
^^^^^^^^^^^^

:math:`{{\cal O}}(X)` er línulegt rúm yfir :math:`{{\mathbb  C}}`.

Ef :math:`f_1,f_2,\dots, f_n` eru :math:`{{\mathbb  C}}`–deildanleg í
:math:`a` og :math:`\alpha_1,\dots,\alpha_n\in {{\mathbb  C}}`, þá fáum
við með þrepun að :math:`f=\alpha_1f_1+\cdots+\alpha_nf_n` er
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math:: f{{\sp{\prime}}}(a)=\alpha_1 f_1{{\sp{\prime}}}(a)+\cdots+\alpha_nf_n{{\sp{\prime}}}(a).

 Eins fáum við með þrepun að margfeldið :math:`f=f_1f_2\cdots f_n` er
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math::

   f{{\sp{\prime}}}(a)= \sum_{j=1}^n f_j{{\sp{\prime}}}(a)\bigg(\prod_{\substack{ k=1\\ k\neq
    j}}^n f_k(a)\bigg).

 Athugið að af þessu leiðir formúlan

.. math::

   \dfrac{f{{\sp{\prime}}}(a)}{f(a)} =  \dfrac{f_1{{\sp{\prime}}}(a)}{f_1(a)}+\cdots+
   \dfrac{f_n{{\sp{\prime}}}(a)}{f_n(a)}.

Sýnidæmi
^^^^^^^^

(i) Allar margliður

.. math:: P(z)= a_0+a_1z+\cdots+a_mz^m, \qquad z\in {{\mathbb  C}},

 eru fáguð föll á öllu :math:`{{\mathbb  C}}` og afleiðan er

.. math:: P{{\sp{\prime}}}(z)= a_1+2a_2z+\cdots+ma_mz^{m-1}, \qquad z\in {{\mathbb  C}}.

 Til þess að sjá þetta, þá athugum við fyrst að sérhvert fastafall
:math:`f(z)=c` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`z` og

.. math:: \dfrac {f(z+h)-f(z)}h=0,

 sem gefur að :math:`f{{\sp{\prime}}}(z)=0` fyrir öll
:math:`z\in {{\mathbb  C}}`. Næst athugum við fallið :math:`g(z)=z`.
Jafnan

.. math:: \dfrac{g(z+h)-g(z)}h=1

 gefur að :math:`g` er :math:`{{\mathbb  C}}`–deildanlegt í sérhverjum
punkti og :math:`g{{\sp{\prime}}}(z)=1`. Með því að beita setningu
:ref:‘set4.2.3‘ (ii) og þrepun fáum við síðan að fallið :math:`h(z)=z^n`
er :math:`{{\mathbb  C}}`–deildanlegt í sérhverjum punkti
:math:`z\in {{\mathbb  C}}` og að afleiða þess er
:math:`h{{\sp{\prime}}}(z)=nz^{n-1}`. Að lokum fæst að sérhver margliða
er fágað fall, því línulegar samantektir af fáguðum föllum eru fáguð
föll.

(ii) Sérhvert rætt fall :math:`R=P/Q`, þar sem :math:`P` og :math:`Q`
eru margliður, er fágað fall á menginu
:math:`\{z\in {{\mathbb  C}}; Q(z)\neq 0\}` og

.. math:: R{{\sp{\prime}}}(z)= \dfrac{P{{\sp{\prime}}}(z)Q(z)-P(z)Q{{\sp{\prime}}}(z)}{Q(z)^2}.

Keðjureglan:hover:‘keðjuregla fyrir fáguð föll‘ fyrir
:math:`{{\mathbb  C}}`–deildanleg föll er eins og keðjureglan fyrir
raunföll:

.. \_se:2.2.6:

Setning
^^^^^^^

Látum :math:`X` og :math:`Y` vera opin hlutmengi af
:math:`{{\mathbb  C}}`, :math:`f:X\to {{\mathbb  C}}` og
:math:`g:Y\to {{\mathbb  C}}` vera föll, þannig að
:math:`f(X)\subset Y`, :math:`a\in X`, :math:`b\in Y`, :math:`b=f(a)` og
setjum

.. math:: h=g\circ f.

 (i) Ef :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og
:math:`g` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`b`, þá er
:math:`h` :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math:: h{{\sp{\prime}}}(a)=g{{\sp{\prime}}}(b)f{{\sp{\prime}}}(a).

 (ii) Ef :math:`g` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`b`,
:math:`g{{\sp{\prime}}}(b)\neq 0`, :math:`h` er
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og :math:`f` er samfellt
í :math:`a`, þá er :math:`f` :math:`{{\mathbb  C}}`–deildanlegt í
:math:`a` og

.. math:: f{{\sp{\prime}}}(a)=h{{\sp{\prime}}}(a)/g{{\sp{\prime}}}(b)

.

Mikilvæg afleiðing af þessari setningu er:

.. \_fs:2.2.7:

Fylgisetning
^^^^^^^^^^^^

Látum :math:`X` og :math:`Y` vera opin hlutmengi af
:math:`{{\mathbb  C}}`, :math:`f:X\to Y` vera gagntækt fall. Ef
:math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og
:math:`f{{\sp{\prime}}}(a)\neq 0`, þá er andhverfa fallið
:math:`f^{[-1]}` :math:`{{\mathbb  C}}`–deildanlegt í :math:`b=f(a)` og

.. math::

   \left(f^{[-1]}\right){{\sp{\prime}}}(b)= \dfrac 1{f{{\sp{\prime}}}(a)}.

   .. _4.2.4:

Cauchy-Riemann-jöfnur
~~~~~~~~~~~~~~~~~~~~~

Nú skulum við gera ráð fyrir því að :math:`f` sé
:math:`{{\mathbb  C}}`–deildanlegt í punktinum :math:`a` og huga að
sambandinu milli :math:`f{{\sp{\prime}}}(a)`, :math:`{\partial}_xf(a)`
og :math:`{\partial}_yf(a)`. Ef við skrifum
:math:`a=\alpha+i\beta=(\alpha, \beta)` og látum :math:`h\to
0` eftir rauntölunum, þá fáum við

.. math::

   \begin{aligned}
   f{{\sp{\prime}}}(a)=&\lim_{\substack{h\to 0\\ h\in {{\mathbb  R}}}}
   \dfrac{u(\alpha+h,\beta)-u(\alpha,\beta)}h+i
   \dfrac{v(\alpha+h,\beta)-v(\alpha,\beta)}h\\
   =&\partial_xu(a)+i\partial_xv(a)=\partial_xf(a).\nonumber\end{aligned}

 Ef við látum hins vegar :math:`h\to 0` eftir þvertölum, :math:`h=ik`,
:math:`k\in {{\mathbb  R}}`, þá fáum við

.. math::

   \begin{aligned}
   f{{\sp{\prime}}}(a)&=\lim_{\substack{k\to 0\\ k\in {{\mathbb  R}}}}
   \dfrac{u(\alpha,\beta+k)-u(\alpha,\beta)}{ik}+i
   \dfrac{v(\alpha,\beta+k)-v(\alpha,\beta)}{ik}\\
   &=-i(\partial_yu(a)+i\partial_yv(a))=-i\partial_yf(a).\nonumber\end{aligned}

 Við höfum því:

.. \_set4.2.8:

Setning
^^^^^^^

Látum :math:`f=u+iv:X\to {{\mathbb  C}}` vera fall af :math:`z=x+iy` á
opnu hlutmengi :math:`X` í :math:`{{\mathbb  C}}`. Ef :math:`f` er
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a\in X`, þá eru báðar
hlutafleiðurnar :math:`\partial_xf(a)` og :math:`\partial_yf(a)` til og

.. math::

   f{{\sp{\prime}}}(a)=\partial_xf(a)=-i\partial_yf(a).


   .. _4.2.7:

 Þar með gildir *Cauchy–Riemann–jafnan:hover:‘Cauchy–Riemann!jafna‘
:hover:‘Cauchy–Riemann!jöfnur‘:hover:‘jafna!Cauchy–Riemann‘*

.. math::

   \tfrac 12\big(\partial_xf(a)+i\partial_yf(a)\big)=0,


   .. _4.2.8:

 og hún jafngildir hneppinu

.. math::

   \partial_xu(a)=\partial_yv(a), \qquad \partial_yu(a)=-\partial_xv(a).


   .. _4.2.9:

Hlutafleiðujafnan (:ref:‘4.2.8‘) nefnist Cauchy–Riemann–jafna eins og
áður er getið. Venja er að tala um jafngilda jöfnuhneppið (:ref:‘4.2.9‘)
sem Cauchy–Riemann–jöfnur, í fleirtölu.

--------------

Sýnidæmi
^^^^^^^^

Kannið hvort fallið

.. math:: f(z)=(x^3-3xy^2+x-4)+i(3x^2y-y^3+y)

 er fágað með því að athuga hvort Cauchy-Riemann-jöfnurnar séu
uppfylltar

*Lausn*:  Við höfum

.. math::

   \begin{gathered}
   u(x,y)={{\operatorname{Re\, }}}f(x,y)=x^3-3xy^2+x-4,\\
   v(x,y)={{\operatorname{Im\, }}}f(x,y)=3x^2y-y^3+y,\\\end{gathered}

 Lítum nú á hlutafleiðurnar

.. math::

   \begin{aligned}
   {2}
   \dfrac{{\partial} u}{{\partial} x}&= 3x^2-3y^2+1, & \qquad
   \dfrac{{\partial} u}{{\partial} y}&= -6xy,\\ 
   \dfrac{{\partial} v}{{\partial} x}&= 6xy, &\qquad
   \dfrac{{\partial} v}{{\partial} y}&= 3x^2-3y^2+1.\end{aligned}

 Greinilegt er að Cauchy-Riemann-jöfnurnar eru uppfylltar,
:math:`{\partial} u/{\partial}x={\partial}v/{\partial}y` og
:math:`{\partial} u/{\partial}y=-{\partial}v/{\partial}x`, og þar með er
:math:`f` fágað fall. Athugið að :math:`f(z)=z^3+z-4`, sem er margliða
og þar með :math:`{{\mathbb  C}}`-deildanlegt fall.

--------------

Wirtinger-afleiður
~~~~~~~~~~~~~~~~~~

Til þess að glöggva okkur betur á Cauchy–Riemann–jöfnunni, þá skulum við
rifja það upp að fall :math:`f:X\to {{\mathbb  R}}^2` er sagt vera
deildanlegt í punktinum :math:`a`, ef til er línuleg vörpun
:math:`L:{{\mathbb  R}}^2\to {{\mathbb  R}}^2` þannig að

.. \_4.2.10:

.. math::

   \lim_{\substack{h\to 0\\ h\in {{\mathbb  R}}^2}}
   \dfrac{\| f(a+h)-f(a)-L(h)\|}{\|h\|}= 0,

þar sem :math:`\|z\|` táknar lengd vigursins :math:`z`. Vörpunin
:math:`L` er ótvírætt ákvörðuð. Hún nefnist afleiða :math:`f` í
punktinum :math:`a` og er oftast táknuð með :math:`d_af`, :math:`df_a`
eða :math:`Df(a)`. Með því að velja vigurinn :math:`h` af gerðinni
:math:`t(1,0)` og :math:`t(0,1)` og láta síðan :math:`t\to 0`, þá sjáum
við að hlutafleiðurnar :math:`{\partial}_xu(a)`,
:math:`{\partial}_yu(a)`, :math:`{\partial}_xv(a)` og
:math:`{\partial}_yv(a)` eru allar til og að fylki vörpunarinnar
:math:`d_af` miðað við grunninn :math:`\{(1,0), (0,1)\}` er

.. math::

   \left[\begin{matrix} 
   {\partial}_xu(a) & {\partial}_yu(a)\\
   {\partial}_xv(a) & {\partial}_yv(a)
   \end{matrix}\right].


   .. _4.2.11:

 Þetta fylki nefnist *Jacobi–fylki:hover:‘Jacobi-fylki‘* :math:`f` í
punktinum :math:`a`. Nú skrifum við :math:`z=(x,y)`,
:math:`a=({\alpha},{\beta})` og sjáum að (:ref:‘4.2.10‘) jafngildir því
að hægt sé að rita

.. math::

   f(z)=\left[\begin{matrix}
   u(a) \\ v(a)
   \end{matrix}\right]+
   \left[\begin{matrix}
   {\partial}_xu(a) \\ {\partial}_xv(a)
   \end{matrix}\right](x-{\alpha})+
   \left[\begin{matrix}
   {\partial}_yu(a) \\ {\partial}_yv(a)

   .. _4.2.12:

   \end{matrix}\right](y-{\beta})+
   \|z-a\|F_a(z),

 þar sem :math:`F_a:X\to {{\mathbb  R}}^2` er samfellt í :math:`a` og
:math:`F_a(a)=0`. Nú skulum við líta á :math:`f` sem tvinngilt fall
:math:`f=u+iv`. Þá er þessi jafna jafngild

.. math::

   f(z)=f(a)+ {\partial}_xf(a)(x-{\alpha})+{\partial}_yf(a)(y-{\beta})
   +(z-a)\varphi_a(z),


   .. _4.2.13:

 þar sem :math:`\varphi_a:X\to {{\mathbb  C}}` er samfellt í :math:`a`
og :math:`\varphi_a(a)=0`. Nú skrifum við

.. math::

   x-{\alpha}=\big((z-a)+\overline{(z-a)}\big)/2, \qquad
   y-{\beta}=\big((z-a)-\overline{(z-a)}\big)/2i

 og fáum því

.. math::

   \begin{gathered}
   {\partial}_xf(a)(x-{\alpha})+{\partial}_yf(a)(y-{\beta})  \\
   =\tfrac 12\big({\partial}_xf(a)-i{\partial}_yf(a)\big)(z-a)
   +\tfrac 12\big({\partial}_xf(a)+i{\partial}_yf(a)\big)\overline{(z-a)}.\end{gathered}

Skilgreining
^^^^^^^^^^^^

Við skilgreinum fyrsta stigs hlutafleiðuvirkjana
:math:`{\partial}_z={\partial}/{\partial}z` og
:math:`{\partial}_{\bar z}={\partial}/{\partial}\bar z` með

.. math::

   {\partial}_zf=\dfrac{{\partial}f}{{\partial} z}
   =\tfrac 12\big({\partial}_xf-i{\partial}_yf\big) \quad \text{ og } \quad
   {\partial}_{\bar z}f=\dfrac{{\partial}f}{{\partial}\bar z}
   =\tfrac 12\big({\partial}_xf+i{\partial}_yf\big)


   .. _4.2.14:

 Tölurnar :math:`{\partial}_zf(a)` og :math:`{\partial}_{\bar z}f(a)`
nefnast *Wirtinger–afleiður:hover:‘Wirtinger-afleiður‘* fallsins
:math:`f` í punktinum :math:`a` og virkinn :math:`{\partial}_{\bar z}`
nefnist
*Cauchy–Riemann–virki:hover:‘virki!Cauchy–Riemann‘:hover:‘Cauchy–Riemann!virki‘*

Nú höfum við umritað (:ref:‘4.2.13‘) yfir í

.. math::

   f(z)=f(a)+{\partial}_zf(a)(z-a)+{\partial}_{\bar z}f(a)\overline{(z-a)}
   + (z-a)\varphi_a(z).


   .. _4.2.15:

Hugsum okkur nú að :math:`f:X\to {{\mathbb  C}}` sé eitthvert fall og að
til séu tvinntölur :math:`A`, :math:`B` og fall
:math:`\varphi_a:X\to {{\mathbb  C}}`, samfellt í :math:`a` með
:math:`\varphi_a(a)=0`, þannig að

.. math::

   f(z)=f(a)+A(z-a)+B\overline{(z-a)}+(z-a)\varphi_a(z).


   .. _4.2.16:

 Þá er greinilegt að :math:`f` er deildanlegt í :math:`a` með afleiðuna
:math:`d_af(h)=Ah+B\bar h` og

.. math::

   \begin{aligned}
   {\partial}_xf(a) &=
   \lim_{\substack{ h\to 0\\ h\in {{\mathbb  R}}}} \dfrac{f(a+h)-f(a)}h
   =\lim_{\substack{ h\to 0\\ h\in {{\mathbb  R}}}} A+B+\varphi_a(a+h) = A+B,\\
   {\partial}_yf(a) &=
   \lim_{\substack{ h\to 0\\ h\in {{\mathbb  R}}}} \dfrac{f(a+ih)-f(a)}h
   =\lim_{\substack{ h\to 0\\ h\in {{\mathbb  R}}}} iA-iB+\varphi_a(a+ih) = i(A-B).\end{aligned}

 Ef við leysum :math:`A` og :math:`B` út úr þessum jöfnum, þá fáum við

.. math::

   \begin{aligned}
   A&= \tfrac 12\big({\partial}_xf(a)-i{\partial}_yf(a)\big)
   ={\partial}_zf(a),\\
   B&= \tfrac 12\big({\partial}_xf(a)+i{\partial}_yf(a)\big)
   ={\partial}_{\bar z}f(a).\end{aligned}

 Við höfum nú sannað:

Setning
^^^^^^^

Látum :math:`X` vera opið hlutmengi í :math:`{{\mathbb  C}}`,
:math:`a\in X` og :math:`f:X\to {{\mathbb  C}}` vera fall. Þá gildir:

(i) :math:`f` er deildanlegt í :math:`a` þá og því aðeins að til séu
tvinntölur :math:`A`, :math:`B` og fall
:math:`\varphi_a:X\to {{\mathbb  C}}`, samfellt í :math:`a` og með
:math:`\varphi(a)=0`, þannig að (:ref:‘4.2.16‘) sé uppfyllt.

(ii) :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` þá og
því aðeins að :math:`f` sé deildanlegt í :math:`a` og
:math:`{\partial}_{\bar z}f(a)=0`. Þá er
:math:`f{{\sp{\prime}}}(a)={\partial}_zf(a)`.

(iii) :math:`f` er fágað í :math:`X` þá og því aðeins að :math:`f` sé
samfellt deildanlegt í :math:`X` og uppfylli Cauchy–Riemann–jöfnuna
:math:`{\partial}_{\bar z}f=0` í :math:`X`. Við höfum þá

.. math::

   f{{\sp{\prime}}}=\dfrac{df}{dz}=\dfrac{\partial f}{\partial z}=\dfrac 12\bigg(
   \dfrac{\partial f}{\partial x}-i\dfrac{\partial f}{\partial y}\bigg).


   .. _4.2.17:

Reikningur með hlutafleiðunum með tilliti til :math:`z` og
:math:`\bar z` er alveg eins of reikningur með óháðu breytunum :math:`x`
og :math:`y`. Ef fallið :math:`f(z)=f(x+iy)` er gefið með formúlu í
:math:`x` og :math:`y`, þá notum við formúlurnar :math:`x=(z+\bar z)/2`
og :math:`y=(z-\bar z)/(2i)` til þess að skipta á óháðu breytunum
:math:`x` og :math:`y` yfir í breyturnar :math:`z` og :math:`\bar z`.
Til þess að kanna hvort fall er fágað þá deildum við eins og þetta séu
óháðar breytur og könnum hvort

.. math:: \dfrac{\partial f}{\partial\bar z}=0.

 Ef :math:`\bar z` kemur alls ekki fyrir í formúlunni, þá er :math:`f`
fágað.

--------------

Sýnidæmi
^^^^^^^^

Kannið hvort fallið :math:`f(z)= |z|^2` er fágað og reiknið út
:math:`{{\mathbb  C}}`-afleiðuna ef hún er til.

*Lausn*:   Við skrifum :math:`f(z)=|z|^2=z\bar z` og sjáum að
:math:`{\partial}f/{\partial}\bar z=z`. Cauchy-Riemann-jafnan er aðeins
uppfyllt í punktinum :math:`z=0` og því er fallið :math:`f` ekki fágað í
grennd við neinn punkt.

--------------

Sýnidæmi
^^^^^^^^

Kannið hvort fallið :math:`f(z)= {{\operatorname{Re\, }}}z + i` er fágað
og reiknið út :math:`{{\mathbb  C}}`-afleiðuna ef hún er til.

:  Hér er :math:`f(z)=\tfrac 12(z+\bar z)+i` og
:math:`{\partial} f/{\partial}\bar z=\tfrac 12`. Fallið :math:`f` er því
ekki fágað.

--------------

.. \_sy:polhnit:

Sýnidæmi
^^^^^^^^

(*Cauchy-Riemann-jöfnur á pólformi*):   Leiðið út jöfnurnar

.. math::

   \dfrac{\partial u}{\partial r}=\dfrac 1r\dfrac{\partial v}{\partial
   \theta} \qquad \text{ og } \qquad 
   \dfrac{\partial v}{\partial r}=-\dfrac 1r\dfrac{\partial u}{\partial
   \theta}

 frá jöfnunum

.. math::

   \dfrac{\partial u}{\partial x}=\dfrac{\partial v}{\partial y}
   \qquad \text{  og } \qquad 
   \dfrac{\partial v}{\partial y}=-\dfrac{\partial v}{\partial x}.

*Lausn*: Samkvæmt skilgreiningu á afleiðunni :math:`\partial u/\partial
r` er

.. math::

   \dfrac{\partial u}{\partial r}=\dfrac{\partial}{\partial r} u(r\cos
   \theta,r\sin \theta)=\dfrac{\partial u}{\partial x} \cdot \cos \theta
   +\dfrac{\partial u}{\partial y}\cdot \sin \theta=\nabla u\cdot 
   {\mathbf e}_r

 þar sem :math:`{\mathbf e}_r=(\cos \theta,\sin \theta)` er
einingarvigurinn í :math:`r`-stefnu, og

.. math::

   \dfrac 1 r\dfrac{\partial u}{\partial \theta}=\dfrac 1r
   \dfrac{\partial}{\partial \theta} u(r\cos
   \theta,r\sin \theta)=\dfrac{\partial u}{\partial x}\cdot (-\sin \theta)+
   \dfrac{\partial u}{\partial y}\cdot \cos \theta=\nabla u\cdot 
   {\mathbf e}_\theta

 þar sem :math:`{\mathbf e}_\theta=(-\sin \theta,\cos \theta)` er
einingarvigurinn í :math:`\theta`-stefnu. Cauchy-Riemann-jöfnurnar segja
að :math:`\nabla u=(\partial v/\partial y,-\partial v/\partial x)`. Þar
með er

.. math::

   \dfrac{\partial u}{\partial r}=\dfrac{\partial v}{\partial
   y}\cdot \cos\theta -\dfrac{\partial v}{\partial x}\cdot \sin \theta= \nabla v\cdot
   {\mathbf e}_\theta=\dfrac 1r \dfrac{\partial v}{\partial \theta}.

 og

.. math::

   \dfrac 1r\dfrac{\partial u}{\partial \theta}=\dfrac{\partial v}{\partial
   y}\cdot (-\sin\theta) -\dfrac{\partial v}{\partial x}\cdot \cos \theta= -\nabla v\cdot
   {\mathbf e}_r=-\dfrac{\partial v}{\partial r}.

 Auðvelt er að snúa röksemdafærslunni við til þess að sanna að af
jöfnunum :math:`\partial u/\partial r=(1/r)\partial v/\partial \theta`
og :math:`(1/r)\partial u/\partial \theta =-\partial v/\partial r`,
leiði Cauchy-Riemann-jöfnurnar.

--------------

Sýnidæmi
^^^^^^^^

Það er áhugaverð staðreynd að :math:`f(z)=e^z` er ótvírætt ákvarðað af
tveimur eiginleikum:  

#. :math:`f(x+i0)=\lim_{y\to 0}f(x+iy)=e^x`,

#. :math:`f'(z)=f(z)`,

þar sem gert er ráð fyrir að :math:`f` sé heilt fágað fall. Sannið þetta
með því að nota Cauchy-Riemann-jöfnurnar.

*Lausn:*  Gefur okkur að :math:`f` sé heilt fágað fall, þ.e.a.s. fágað
fall á öllu :math:`{{\mathbb  C}}`, sem uppfyllir (i) og (ii). Við ætlum
að sanna að þá sé :math:`f(z)=e^z`. Setjum
:math:`u(x,y)={{\operatorname{Re\, }}}f(z)` og
:math:`v(x,y)={{\operatorname{Im\, }}}f(z)` þar sem :math:`z=x+iy` og
:math:`x,y\in {{\mathbb  R}}`. Fyrst :math:`f` er
:math:`{{\mathbb  C}}`-deildanlegt, þá fáum við jöfnurar
:math:`f'(z)=\partial f/\partial x=-i\partial f/\partial y` þetta gefur
ásamt jöfnunni :math:`f'(z)=f(z)` að

.. math::

   \dfrac {\partial u}{\partial x}+i\dfrac {\partial v}{\partial x}=
   -i\dfrac {\partial u}{\partial y}+\dfrac {\partial v}{\partial y}=u+iv.

 Við getum eins skrifað þetta sem tvær raunjöfnur

.. math::

   \dfrac {\partial u}{\partial x}=\dfrac {\partial v}{\partial y}=u
   \qquad \text{ og } \qquad \dfrac {\partial u}{\partial y}=-\dfrac
   {\partial v}{\partial x}=-v.

 (Athugið að fyrri hlutinn af þessum jöfnum er Cauchy-Riemann
jöfnurnar.) Nú ætlum við að sýna fram á að þessar jöfnur ásamt
skilyrðinu :math:`f(x+i0)=e^x` gefi okkur að :math:`u(x,y)=e^x\cos y` og
:math:`v(x,y)=e^x\sin y`. Til þess reiknum við út
:math:`\partial^2u/\partial
y^2` og :math:`\partial^2v/\partial y^2`,

.. math::

   \dfrac{\partial^2u}{\partial y^2}=-\dfrac{\partial v}{\partial y}=-u
   \quad \text{ og } \quad 
   \dfrac{\partial^2v}{\partial y^2}=\dfrac{\partial u}{\partial y}=-v.

 Við höfum því sýnt að fyrir fast :math:`x` uppfylla :math:`u` og
:math:`v` afleiðujöfnu sem föll af :math:`y`. Við vitum hvernig lausnin
á þessari jöfnu er

.. math::

   u(x,y)=A(x)\cos y+ B(x)\sin y \qquad \text{ og } \qquad
   v(x,y)=C(x)\cos y+D(x)\sin y.

 Skilyrðið :math:`f(x+i0)=e^x` gefur okkur að :math:`u(x,0)=A(x)=e^x` og
:math:`v(x,0)=C(x)=0`. Skilyrðið
:math:`\partial u(x,0)/\partial y=-v(x,0)=0` gefur okkur að
:math:`B(x)=0` og skilyrðið :math:`\partial v(x,0)/\partial
y=u(x,0)=e^x` gefur okkur :math:`D(x)=e^x`. Niðurstaðan er því að

.. math:: f(z)=u(x,y)+iv(x,y)=e^x\cos y+ie^x\sin y=e^z,\qquad z\in {{\mathbb  C}}.

--------------

Samleitnar veldaraðir
---------------------

Einu dæmin um fáguð föll sem við höfum nefnt til þessa eru margliður
:math:`P`, en þær eru fágaðar á öllu :math:`{{\mathbb  C}}`, og ræð föll
:math:`R=P/Q`, en þau eru fáguð á
:math:`{{\mathbb  C}}\setminus\{z\in {{\mathbb  C}}; Q(z)=0\}`. Nú ætlum
við að bæta verulega við dæmaforðann með því að sanna að öll föll, sem
unnt er að setja fram með samleitnum veldaröðum, séu fáguð á
samleitniskífu raðarinnar.

Ef fallið :math:`f` er skilgreint á einhverju opnu mengi :math:`Y` á
:math:`{{\mathbb  R}}` og er gefið með samleitinni veldaröð á
:math:`]a-{\varrho},a+{\varrho}[\subset Y`,

.. math::

   f(x)=\sum\limits_{n=0}^{\infty} a_n(x-a)^n, \qquad 
   x\in  ]a-{\varrho},a+{\varrho}[,

 þá er röðin samleitin á opnu skífunni
:math:`S(a,{\varrho})\subseteq {{\mathbb  C}}` og við getum framlengt
skilgreiningarsvæði :math:`f` yfir á :math:`S(a,{\varrho})` með því að
setja

.. math::

   f(z)=\sum\limits_{n=0}^{\infty} a_n(z-a)^n, \qquad 
   z\in  S(a,{\varrho}).

Skilgreining
^^^^^^^^^^^^

Fall sem skilgreint er á opnu mengi :math:`U` á rauntalnaásnum er sagt
vera *raunfágað* ef það hefur þann eiginleika að í grennd um sérhvern
punkt í :math:`U` er hægt að setja :math:`f` fram með samleitinni
veldaröð.

Fallið :math:`z\mapsto 1/(1-z)` er fágað á
:math:`{{\mathbb  C}}\setminus\{1\}` og það gefið með geómetrísku
röðinni

.. math:: \dfrac 1{1-z}=\sum_{n=0}^\infty z^n, \qquad z\in S(0,1).

 Veldisvísisfallið, hornaföllin og breiðbogaföllin eru öll gefin með
samleitnum veldaröðum á :math:`{{\mathbb  R}}` og fáguðu framlengingar
þeirra eru því gefnar með sömu röðum á öllu :math:`{{\mathbb  C}}`

.. math::

   \begin{gathered}
   \exp z =e\sp z = \sum_{n=0}^\infty \dfrac 1{n!}z^n, \\
   \cos z = \sum_{k=0}\sp \infty \dfrac {(-1)\sp k}{(2k)!}z\sp{2k}, \quad
   \sin z = \sum_{k=0}\sp \infty \dfrac {(-1)\sp k}{(2k+1)!}z\sp{2k+1},
   \quad\\
   \cosh z = \sum_{k=0}\sp \infty \dfrac {1}{(2k)!}z\sp{2k}, \quad
   \sinh z = \sum_{k=0}\sp \infty \dfrac {1}{(2k+1)!}z\sp{2k+1}.\end{gathered}

.. \_set4.3.1:

Setning
^^^^^^^

Gerum ráð fyrir að :math:`X` sé opið hlutmengi af
:math:`{{\mathbb  C}}`, :math:`S(\alpha,\varrho)\subset X`, að
:math:`f:X\to {{\mathbb  C}}` sé fall, sem gefið er á
:math:`S(\alpha,\varrho)` með samleitinni veldaröð,

.. math:: f(z)=\sum_{n=0}^\infty a_n(z-\alpha)^n, \qquad z\in S(\alpha,\varrho).

 Þá er :math:`f` fágað á :math:`S(\alpha,\varrho)` og

.. math::

   f{{\sp{\prime}}}(z)=\sum_{n=1}^\infty na_n(z-\alpha)^{n-1}, \qquad z\in
   S(\alpha,\varrho).

Sönnunina tökum við fyrir í grein 2.6. Ef :math:`\sum_{n=0}a_nz^n` og
:math:`\sum_{n=0}^\infty b_nz^n` eru tvær samleitnar veldaraðir með
samleitnigeisla :math:`\varrho_a` og :math:`\varrho_b`, þá höfum við
fáguð föll :math:`f` og :math:`g` í :math:`S(\alpha,\varrho_a)` og
:math:`S(\alpha,\varrho_b)` sem gefin eru með

.. math::

   f(z)=\sum_{n=0}^\infty a_n(z-\alpha)^n, \qquad \text{ og } \qquad
   g(z)=\sum_{n=0}^\infty b_n(z-\alpha)^n.

 Ef við setjum :math:`\varrho=\min\{\varrho_a,\varrho_b\}`, þá eru
fáguðu föllin :math:`f+g` og :math:`fg` einnig gefin veldaröðum á
skífunni :math:`S(\alpha,\varrho)` með

.. math::

   f(z)+g(z)=\sum_{n=0}^\infty (a_n+b_n)(z-\alpha)^n 
   \qquad \text{ og } \qquad f(z)g(z)=\sum_{n=0}^\infty c_n(z-\alpha)^n,

 þar sem stuðlarnir :math:`c_n` eru gefnir með

.. math:: c_n=\sum_{k=0}^n a_kb_{n-k}, \qquad n=0,1,2,\dots.

Eftirfarandi setning nefnist *samsemdarsetning:hover:‘samsemdarsetning‘
fyrir samleitnar veldaraðir:hover:‘samsemdarsetning!fyrir samleitnar
veldaraðir‘*:

Setning
^^^^^^^

Gerum ráð fyrir að :math:`f,g\in {{\cal O}}(S(\alpha,\varrho))` séu
gefin með samleitnum veldaröðum

.. math::

   f(z)=\sum\limits_{n=0}^\infty a_n(z-\alpha)^n, \qquad
   g(z)=\sum\limits_{n=0}^\infty b_n(z-\alpha)^n, \qquad
   z\in S(\alpha,\varrho),

 og gerum ráð fyrir að til sé runa :math:`\{\alpha_j\}` af ólíkum
punktum í :math:`S(\alpha,\varrho)` þannig að :math:`\alpha_j\to \alpha`
og :math:`f(\alpha_j)=g(\alpha_j)` fyrir öll :math:`j`. Þá er
:math:`a_n=b_n` fyrir öll :math:`n` og þar með :math:`f(z)=g(z)` fyrir
öll :math:`z\in S(\alpha,\varrho)`.

Sönnun
^^^^^^

Fallið :math:`h=f-g\in {{\cal O}}(S(\alpha,\varrho))` hefur
veldaraðarframsetninguna

.. math::

   h(z)=\sum\limits_{n=0}^\infty c_n(z-\alpha)^n, \qquad z\in
   S(\alpha,\varrho),

 þar sem :math:`c_n=a_n-b_n`. Við þurfum að sanna að :math:`c_n=0` fyrir
öll :math:`n`. Gerum ráð fyrir að til sé :math:`N` þannig að
:math:`c_N\neq 0` og veljum :math:`N` eins lítið og kostur er. Þá er

.. math::

   \begin{aligned}
   h(z)&= \sum\limits_{n=N}^\infty c_n(z-\alpha)^n = 
   (z-\alpha)^N\sum\limits_{n=0}^\infty c_{N+n}(z-\alpha)^n\\
   &= (z-\alpha)^N k(z), \qquad 
   k(z) = \sum\limits_{n=0}^\infty c_{N+n}(z-\alpha)^n.\end{aligned}

 Fallið :math:`k` er fágað á :math:`S(\alpha,\varrho)` og þar með er það
samfellt, :math:`k(\alpha)=c_{N}`, svo til er opin grennd :math:`U` um
:math:`\alpha` þar sem :math:`k(z)\neq 0`. Fyrst
:math:`\alpha_j\to \alpha`, þá er :math:`\alpha_j\in U` ef :math:`j` er
nógu stórt og þar með er
:math:`h(\alpha_j)=(\alpha_j-\alpha)^Nk(\alpha_j)\neq 0`. Þetta er hins
vegar í mótsögn við forsendu okkar að :math:`h(\alpha_j)=0`.

Fylgisetning
^^^^^^^^^^^^

Ef  :math:`\sum_{n=0}^{\infty} a_nx^n` er samleitin veldaröð, :math:`I`
er opið bil sem inniheldur :math:`0` og :math:`\sum_{n=0}^{\infty}
a_nx^n=0` fyrir öll :math:`x\in I`, þá er :math:`a_n=0` fyrir öll
:math:`n=0,1,2,\dots`.

Í setningu :ref:‘set4.3.1‘ sönnuðum við að sérhvert fall sem gefið er
með veldaraðaframsetningu á einhverri skífu sé fágað. Nú hugum við að
andhverfu þessarar staðhæfingar:

Setning
^^^^^^^

Látum :math:`X\subset {{\mathbb  C}}` vera opið og
:math:`f\in {{\cal O}}(X)`. Ef :math:`\alpha\in X`,
:math:`0<\varrho<d(\alpha,\partial X)`, þar sem
:math:`d(\alpha,\partial X)` táknar fjarlægð punktsins :math:`\alpha`
frá jaðrinum :math:`\partial X` á menginu :math:`X`, þá er hægt að setja
:math:`f` fram í :math:`S(\alpha,\varrho)` með samleitinni veldaröð

.. math::

   f(z) = \sum\limits_{n=0}^\infty a_n(z-\alpha)^n, \qquad z\in
   S(\alpha,\varrho).

.. figure:: ./myndir/fig031.svg

:align: center

:alt: Skífa í skilgreiningarsvæði :math:`f`

2BeRemovedMynd: Skífa í skilgreiningarsvæði :math:`f`

Þessa setningu sönnum við ekki fyrr en í kafla 3, en við skulum skoða
nokkrar afleiðingar hennar.

Fylgisetning
^^^^^^^^^^^^

Ef :math:`f\in {{\cal O}}(X)`, þá er
:math:`f{{\sp{\prime}}}\in {{\cal O}}(X)`.

Sönnun
^^^^^^

Ef :math:`f` er sett fram með veldaröðinni
:math:`f(z)=\sum_{n=0}^\infty a_n(z-\alpha)^n` fyrir öll :math:`z\in
S(\alpha,\varrho)`, þá er :math:`f{{\sp{\prime}}}` sett fram með
veldaröðinni :math:`f'(z)=\sum_{n=1}^\infty na_n(z-\alpha)^{n-1}`,
samkvæmt setningu :ref:‘set4.3.1‘, og er því fágað.

Nú sjáum við að fallið :math:`f{{\sp{\prime}}}` er fágað og afleiða þess
:math:`f{{\sp{\prime\prime}}}` er einnig fáguð og þannig áfram út í hið
óendanlega. Fyrir sérhvert fágað fall :math:`f\in {{\cal O}}(X)`
skilgreinum við hærri afleiður :math:`f^{(k)}` með þrepun
:math:`f^{(0)}=f` og :math:`f^{(k)}=\big(f^{(k-1)}\big){{\sp{\prime}}}`,
fyrir :math:`k\geq 1`. Við fáum síðan:

.. \_se:2.3.7:

Setning
^^^^^^^

Látum :math:`X` vera opið hlutmengi af :math:`{{\mathbb  C}}`,
:math:`f\in {{\cal O}}(X)`, :math:`\alpha\in
X` og :math:`0<\varrho<d(\alpha,\partial X)`. Þá er

.. math::

   f(z)= \sum\limits_{n=0}^\infty \dfrac
   {f^{(n)}(\alpha)}{n!}(z-\alpha)^n, \qquad z\in S(\alpha,\varrho).

 Þessi veldaröð kallast
*Taylor–röð:hover:‘Taylor-röð‘:hover:‘Taylor-röð!falls í punkti‘
fallsins :math:`f` í punktinum :math:`\alpha`*.

Ef við byrjum með raunfágað fall á bili á rauntalnaásnum, þá vitum við
að við getum stækkað skilgreiningarmengi þess yfir í opið mengi í
:math:`{{\mathbb  C}}`. Sú aðgerð fellur undir eftirfarandi almenna
skilgreiningu:

Skilgreining
^^^^^^^^^^^^

Látum :math:`f:Y\to {{\mathbb  C}}` vera raunfágað fall á opnu mengi
:math:`Y` á :math:`{{\mathbb  R}}` og gerum ráð fyrir að
:math:`F:X\to {{\mathbb  C}}` sé fágað fall á opnu hlutmengi :math:`X`
af :math:`{{\mathbb  C}}`, þannig að :math:`Y\subset X` og
:math:`F(x)=f(x)` fyrir öll :math:`x\in Y`. Þá kallast :math:`F` *fáguð
framlenging:hover:‘fáguð framlenging‘* eða *fáguð útvíkkun:hover:‘fáguð
útvíkkun‘* á fallinu :math:`f`.

Í kafla 3 eigum við eftir sjá, að ef mengið :math:`X` er samanhangandi,
þá er fáguð framlenging :math:`F` á :math:`f` ótvírætt ákvörðuð. Við
megum því nota sama tákn :math:`f` fyrir upprunalega fallið og fyrir
útvíkkunina.

Veldaröð veldisvísisfallsins
----------------------------

Enginn vafi leikur á því að veldisvísisfallið er merkilegasta fall
stærðfræðigreiningarinnar. Við skilgreindum það með formúlunni

.. math:: \exp z=e^x(\cos y+i\sin y), \qquad z=x+iy \in {{\mathbb  C}}.

 Við hefðum eins getað notað veldaraðarframsetninguna á
:math:`x\mapsto e^x` til þess að skilgreina fágaða framlengingu
veldisvísisfallsins. Við skulum nú kanna nokkra eiginleika
veldisvísisfallsins út frá veldaröðinni.

Með því að deilda röðina lið fyrir lið fáum við

.. math:: \exp{{\sp{\prime}}}z=\exp z, \qquad \text{eða} \qquad \dfrac d{dz}e^z=e^z.

 Undirstöðueiginleiki veldisvísisfallsins er
*samlagningarformúla:hover:‘samlagningarformúla!veldisvísisfallsins‘
:hover:‘veldisvísisfallið!samlagningarformúla‘* þess

.. math:: e^{z+w}=e^ze^w, \qquad z,w\in {{\mathbb  C}}.

 Hún leiðir af tvíliðureglunni :hover:‘tvíliðuregla‘,

.. math::

   \begin{aligned}
   e^{z+w}&=\sum_{n=0}^\infty\dfrac 1{n!}(z+w)^n\\
   &=\sum_{n=0}^\infty\dfrac 1{n!}\sum_{k=0}^n \dfrac{n!}{k!(n-k)!}z^kw^{n-k}\\
   &=\sum_{n=0}^\infty\sum_{k=0}^n \dfrac {z^k}{k!}\dfrac {w^{n-k}}{(n-k)!}\\
   &=\bigg(\sum_{n=0}^\infty \dfrac {z^n}{n!}\bigg)\bigg(\sum_{n=0}^\infty\dfrac
   {w^{n}}{n!}\bigg)=e^ze^w. \end{aligned}

 Flestir eiginleikar veldisvísisfallsins er leiddir út frá
samlagningarformúlunni. Til dæmis sjáum við að

.. math::

   e^{-z}=\dfrac 1{e^z}, \qquad z\in {{\mathbb  C}}.

   .. _4.5.1:

 Á rauntalnaásnum er veldisvísisfallið :math:`x\mapsto e^x` stranglega
vaxandi því afleiða þess er :math:`e^x` og hún er jákvæð. Við höfum líka
:math:`e^x\to+\infty` ef :math:`x\to \infty`, því sérhver liður í
veldaröðinni með númer :math:`n\geq 1` er stranglega vaxandi og stefnir
á óendanlegt. Af þessu leiðir síðan að :math:`e^{x}=1/e^{-x}\to 0` ef
:math:`x\to -\infty`. Milligildissetningin segir okkur nú að
veldisvísisfallið tekur öll jákvæð gildi á rauntalnaásnum.

Snúum okkur þá að gildunum á þverásnum :math:`\{ix\in {{\mathbb  C}};
 x\in {{\mathbb  R}}\}`. Reglurnar um reikning með samoka tvinntölum
gefa okkur

.. math:: \overline{e^z}=e^{\overline z},\qquad z\in {{\mathbb  C}},

 og síðan

.. math:: |e^z|^2=e^z\overline{e^{z}}=e^ze^{\overline z}=e^{x+iy}e^{x-iy}=e^{2x}

 Þar með er

.. math:: |e^z|=e^{{{\operatorname{Re\, }}}z}, \qquad z\in {{\mathbb  C}},

 og sérstaklega gildir

.. math:: |e^{iy}|=1, \qquad y\in {{\mathbb  R}}.

 Af þessu leiðir að veldisvísisfallið hefur enga
núllstöð:hover:‘veldisvísisfallið!núllstöð‘ :math:`e^z=e^xe^{iy}` og
hvorugur þátturinn í hægri hliðinni getur verið núll.

Með því að stinga :math:`iz` inn í veldaröðina fyrir veldisvísisfallið
sjáum við að formúlan :math:`e^{ix}=\cos x+i\sin x` gildir áfram um
tvinntölur :math:`z\in{{\mathbb  C}}`,

.. math::

   e^{iz}=\sum\limits_{n=0}^\infty\dfrac{i^n}{n!}z^n
   =\sum\limits_{n=0}^\infty\dfrac{(-1)^n}{(2n)!}z^{2n}
   +i\sum\limits_{n=0}^\infty\dfrac{(-1)^n}{(2n+1)!}z^{2n+1}
   =\cos z +i \sin z.

 Allir liðirnir í kósínus–röðinni hafa jöfn veldi og allir liðirnir í
sínus–röðinni hafa oddatöluveldi, svo :math:`\cos` er jafnstætt, en
:math:`\sin` er oddstætt. Þar með er

.. math:: e^{-iz}=\cos z-i\sin z, \qquad z\in {{\mathbb  C}}.

 Við leysum nú :math:`\cos z` og :math:`\sin z` út úr síðustu tveimur
jöfnunum og fáum *jöfnur
Eulers:hover:‘Euler‘:hover:‘Euler!jöfnur‘:hover:‘jöfnur Eulers‘*

.. math::

   \cos z =\frac 12(e^{iz}+e^{-iz}), \qquad
   \sin z =\frac 1{2i}(e^{iz}-e^{-iz}).

 Afleiðurnar af :math:`\cos` og :math:`\sin` getum við annað hvort
reiknað með því að deilda veldaraðirnar eða með því að deilda jöfnur
Eulers,

.. math:: \cos{{\sp{\prime}}}z=-\sin z, \qquad \sin{{\sp{\prime}}}z=\cos z, \qquad z\in {{\mathbb  C}}.

Lograr, rætur:hover:‘rót‘ og horn:hover:‘horn‘
----------------------------------------------

Veldisvísisfallið :math:`e^z` er lotubundið með lotuna :math:`2\pi i`,

.. math:: \exp(z+2{\pi}i) = \exp z, \qquad z\in {{\mathbb  C}}.

 Þetta leiðir beint af þeirri staðreynd að kósínus og sínus eru
lotubundin með lotuna :math:`2{\pi}`. Þar með getur :math:`\exp` ekki
haft neina andhverfu á öllu menginu :math:`{{\mathbb  C}}`. Veldisföllin
:math:`z^n`, :math:`n\geq 2` geta ekki heldur haft neina andhverfu á
öllu :math:`{{\mathbb  C}}`. Hins vegar hafa þessi föll andhverfur *frá
hægri* á minni hlutmengjum í :math:`{{\mathbb  C}}`:

Skilgreining
^^^^^^^^^^^^

Látum :math:`X` vera opið hlutmengi af :math:`{{\mathbb  C}}`. Samfellt
fall :math:`\lambda:X\to
{{\mathbb  C}}` kallast *logri á :math:`X`:hover:‘logri‘* ef

.. math::

   e^{\lambda(z)}=z, \qquad z\in X.


   .. _4.6.1:

 Samfellt fall :math:`\varrho:X\to {{\mathbb  C}}` kallast *:math:`n`–ta
rót:hover:‘\ :math:`n`–ta rót‘* á :math:`X` ef

.. math::

   \big(\varrho(z)\big)^n=z, \qquad z\in X.


   .. _4.6.2:

 Samfellt fall :math:`\theta:X\to {{\mathbb  R}}` kallast *horn á
:math:`X`* ef

.. math::

   z=|z|e^{i\theta(z)}, \qquad z\in X.


   .. _4.6.3:

Helstu eiginleikar logra, róta:hover:‘rót‘ og horna:hover:‘horn‘ eru:

Setning
^^^^^^^

(i) Ef :math:`\lambda` er logri á :math:`X`, þá er :math:`0\not\in X`,
:math:`\lambda\in {{\cal O}}(X)` og

.. math:: \lambda{{\sp{\prime}}}(z)=\frac 1z, \qquad z\in X.

 Föllin :math:`\lambda(z)+i2\pi k`, :math:`k\in {{\mathbb  Z}}` eru
einnig lograr á :math:`X`.

(ii) Ef :math:`\lambda` er logri á :math:`X`, þá er

.. math::

   \lambda(z)=\ln
   |z|+i\theta(z), \qquad z\in X,

 þar sem :math:`\theta:X\to {{\mathbb  R}}` er horn á :math:`X`. Öfugt,
ef :math:`\theta:X\to {{\mathbb  R}}` er horn á :math:`X`, þá er
:math:`\lambda(z)=\ln|z|+i\theta(z)` logri á :math:`X`.

(iii) Ef :math:`\varrho` er :math:`n`–ta rót á :math:`X` þá er
:math:`\varrho\in {{\cal O}}(X)` og

.. math:: \varrho{{\sp{\prime}}}(z)=\frac {\varrho(z)}{nz}, \qquad z\in X.

 (iv) Ef :math:`\lambda` er logri á :math:`X`, þá er
:math:`\varrho(z)=e\sp{\lambda(z)/n}` :math:`n`–ta rót á :math:`X`.

Sönnun
^^^^^^

(i) Veldisvísisfallið tekur ekki gildið :math:`0`, svo
:math:`z=\exp(\lambda(z))\neq 0` fyrir öll :math:`z\in X`. Setning 4.2.6
(ii) gefur að :math:`\lambda` er fágað og af jöfnunni
:math:`z=\exp(\lambda(z))`, leiðir
:math:`1=\exp(\lambda(z))\lambda{{\sp{\prime}}}(z)=z\lambda{{\sp{\prime}}}(z)`.
Þar með er :math:`\lambda{{\sp{\prime}}}(z)=1/z`. Síðasta staðhæfingin
er augljós, því veldisvísisfallið hefur lotuna :math:`2\pi i`.

(ii) Við höfum
:math:`|z|=|e^{\lambda(z)}|=e^{{{\operatorname{Re\, }}}\lambda(z)}`
fyrir öll :math:`z\in X`. Þetta gefur
:math:`{{\operatorname{Re\, }}}\lambda(z)=\ln |z|` og þar með að
:math:`z=|z|e^{i{{\operatorname{Im\, }}}\lambda(z)}`. Samkvæmt
skilgreiningu segir þetta að
:math:`\theta(z)={{\operatorname{Im\, }}}\lambda(z)` sé horn á
:math:`X`. Öfugt, ef :math:`\theta` er horn á :math:`X` og við setjum
:math:`\lambda(z)=\ln |z|+i\theta(z)`, þá er
:math:`\exp(\lambda(z))=\exp(\ln|z|)\exp(i\theta(z))=|z|e^{i\theta(z)}=z`,
fyrir öll :math:`z\in X`.

(iii) Við höfum að :math:`(\varrho(z))^n=z` fyrir öll :math:`z\in X`,
svo setning 4.2.6 (ii) gefur okkur að :math:`\varrho\in {{\cal O}}(X)`.
Ef við deildum þessa jöfnu, fáum við
:math:`n(\varrho(z))^{n-1}\varrho{{\sp{\prime}}}(z)=1`. Við margföldum
nú í gegn með :math:`\varrho(z)` og fáum
:math:`\varrho(z)=n(\varrho(z))^n\varrho{{\sp{\prime}}}(z)=nz\varrho{{\sp{\prime}}}(z)`.

(iv) :math:`\varrho(z)^n=(\exp(\lambda(z)/n))^n=\exp(\lambda(z))=z`,
:math:`z\in X`.

--------------

Athugið að fyrir sérhverja tvinntölu :math:`{\alpha}` getum við
skilgreint fágað *veldisfall með veldisvísi* :math:`\alpha` með

.. math:: z^\alpha=\exp(\alpha\lambda(z)), \qquad z\in X,

 þar sem :math:`\lambda` er gefinn logri á :math:`X` og við fáum að

.. math::

   \dfrac d{dz}z^\alpha=\dfrac d{dz}e^{\alpha\lambda(z)}=e^{\lambda(z)}\frac
   \alpha z =\alpha e^{\alpha\lambda(z)}e^{-\lambda(z)}=
   \alpha e^{(\alpha-1)\lambda(z)}=\alpha z^{\alpha-1}.

 Þetta er sem sagt gamalkunn regla, sem gildir áfram fyrir
:math:`{{\mathbb  C}}`–afleiður. Hér verðum við að hafa í huga að
skilgreiningin er algerlega háð því hvernig logrinn er skilgreindur. Ef
við skiptum til dæmis á logranum :math:`\lambda(z)` og
:math:`\lambda(z)+2\pi i`, þá verður

.. math:: e^{\alpha(\lambda(z)+2\pi i)}=e^{\alpha\lambda(z)}e^{2\pi i\alpha}.

 Ef :math:`\alpha` er heiltala þá er :math:`z^\alpha` samkvæmt þessari
skilgreininingu það sama og fæst út úr veldareglunum með heiltöluveldi,
en ef :math:`\alpha` er ekki heiltala, þá er skilgreiningin háð valinu á
logranum.

Ef :math:`\alpha \in X`, þá skilgreinum við *veldisvísisfall með
grunntölu :math:`\alpha`* sem fágaða fallið á :math:`{{\mathbb  C}}`,
sem gefið er með

.. math:: \alpha^z=e^{z\lambda(\alpha)}.

 Athugið að skilgreiningin er háð valinu á logranum. Keðjureglan gefur

.. math::

   \dfrac d{dz}\alpha^z=
   \dfrac d{dz}e^{z\lambda(\alpha)}=e^{z\lambda(\alpha)}\cdot
   \lambda(\alpha)=\alpha^z\lambda(\alpha).

--------------

Sýnidæmi
^^^^^^^^

Hvernig er :math:`i^i` skilgreint?

*Lausn*:  Talan :math:`i` hefur lengdina :math:`1` og horngildið
:math:`\tfrac 12
\pi+2\pi k`, þar sem :math:`k\in {{\mathbb  Z}}`. Ef :math:`X` er svæði
sem inniheldur :math:`i` og :math:`\lambda` er logri á :math:`X`, þá er
:math:`\lambda(i)=i(\tfrac 12 \pi+2\pi k)` fyrir eitthvert
:math:`k\in {{\mathbb  Z}}`. Með þessu vali á :math:`\lambda` verður

.. math:: i^i=e^{i\lambda(i)}=e^{-(\tfrac 12\pi+2\pi k)}.

 Gildið :math:`i^i` er því háð því hvaða logra við veljum og við höfum
óendanlega marga valmöguleika.

--------------

0 2 1 0 = -1 0 by-1 1 = 1 2 = -0 2 by100 = 1 100 by2 100 by1 1 0 0 = 0
by-1 2 0pt 0 0pt 0 Lítum nú á mengið
:math:`X={{\mathbb  C}}\setminus {{\mathbb  R}}_-`, sem fæst með því að
skera neikvæða raunásinn og :math:`0` út úr tvinntalnaplaninu. Við
skilgreinum síðan pólhnit í :math:`X` eins og myndin sýnir og veljum
hornið :math:`\theta(z)` þannig að :math:`-\pi<\theta(z)<\pi`,
:math:`z\in X`. Fallið

.. math::

   {{\operatorname{Arg}}}:{{\mathbb  C}}\setminus {{\mathbb  R}}_-\to {{\mathbb  R}}, \qquad
   {{\operatorname{Arg}}}z=\theta(z),\quad z\in X

 0 er kallað *höfuðgrein
hornsins:hover:‘logri!höfuðgrein‘:hover:‘höfuðgrein!horns‘* og við
reiknuðum út formúlu fyrir því í kafla 1,

.. math:: {{\operatorname{Arg}}}\, z=2\arctan\bigg(\dfrac y{|z|+x}\bigg), \qquad z=x+iy\in X.

 Fallið

.. math::

   {{\operatorname{Log}}}:{{\mathbb  C}}\setminus {{\mathbb  R}}_-\to {{\mathbb  C}}, \qquad
   {{\operatorname{Log}}}z=\ln |z| +i{{\operatorname{Arg}}}(z),\quad z\in X,

 er kallað *höfuðgrein
lografallsins:hover:‘höfuðgrein‘:hover:‘höfuðgrein!lografallsins‘*.
Fallið

.. math:: z^\alpha = e^{\alpha{{\operatorname{Log}}}z}, \qquad z\in {{\mathbb  C}}\setminus {{\mathbb  R}}_-,

 kallast *höfuðgrein
veldisfallsins:hover:‘veldisfall‘:hover:‘veldisfall!höfuðgrein‘ með
veldisvísi :math:`\alpha`*. Tvö síðastnefndu föllin eru fágaðar
framlengingar á föllunum :math:`\ln x` og :math:`x^\alpha` frá jákvæða
raunásnum yfir í opna mengið
:math:`{{\mathbb  C}}\setminus {{\mathbb  R}}_-` í tvinntalnaplaninu.

--------------

Sýnidæmi
^^^^^^^^

Skrifið eftirfarandi tvinntölur á forminu :math:`x+iy`, þar sem
:math:`x` og :math:`y` eru rauntölur.

**a)** :math:`{{\operatorname{Log}}}{(-i)}`.
:math:`{{\operatorname{Log}}}({1+i})`.
:math:`{{\operatorname{Log}}}((1+i)^{\pi i})`.

*Lausn:*   **a)**  Höfuðgrein lograns er
:math:`{{\operatorname{Log}}}z=\ln |z|+i {{\operatorname{Arg}}}(z)`,
:math:`\ln|-i|=\ln 1=0` og :math:`{{\operatorname{Arg}}}(-i)=-\pi/2`.
Svarið verður því :math:`{{\operatorname{Log}}}(-i)=-i\pi/2`.

**b)**  Við höfum :math:`\ln|1+i|=\ln\sqrt 2` og
:math:`{{\operatorname{Arg}}}(1+i)=\pi/4` og því er
:math:`{{\operatorname{Log}}}(1+i)=\ln \sqrt 2+i\pi/4`.

**c)**   Við notum niðurstöðuna úr síðasta lið til þess að reikna
:math:`(1+i)^{i\pi}=e^{i\pi(\ln\sqrt 2+i\pi/4)}=e^{-\pi^2/4+i\pi
\ln\sqrt 2}`. Af því leiðir að :math:`\ln|(1+i)^{i\pi}|=\ln
e^{-\pi^2/4}=-\pi^2/4` og þar sem :math:`0<\pi\ln \sqrt 2<\pi`, þá fáum
við einnig :math:`{{\operatorname{Arg}}}((1+i)^{i\pi})=\pi\ln\sqrt 2`.
Niðurstaðan verður því

.. math::

   {{\operatorname{Log}}}((1+i)^{i\pi})=-\pi^2/4+i\pi\ln\sqrt 2=i\pi(\ln\sqrt
   2+i\pi/4)=i\pi{{\operatorname{Log}}}(1+i)

Athugið að gamla góða lograreglan
:math:`{{\operatorname{Log}}}(z^\alpha)=\alpha {{\operatorname{Log}}}z`,
gildir ekki almennt.

Sýnidæmi
^^^^^^^^

Sýnið að
:math:`{{\operatorname{Log}}}(1+\sqrt 3 i)^4\neq 4 {{\operatorname{Log}}}(1+\sqrt 3 i)`.

*Lausn*:   Við byrjum á að setja töluna :math:`1+\sqrt 3` fram á
pólformi með horngildi á bilinu :math:`]-\pi,\pi[`, sem er
:math:`1+\sqrt 3 i=2e^{i{\pi}/3}`. Því er

.. math:: 4{{\operatorname{Log}}}(1+\sqrt 3 i)=4(\ln 2+i{\pi}/3)=4\ln 2+i4{\pi}/3.

 Á hinn bóginn er :math:`(1+\sqrt 3 i)^4=2^4e^{i4{\pi}/3}=
2^4e^{-i2{\pi}/3}` og því er

.. math:: {{\operatorname{Log}}}(1+\sqrt 3 i)^4=\ln 2^4-i2{\pi}/3=4\ln 2-i2{\pi}/3.

 Niðurstaðan er að jafnaðarmerki gildir ekki.

--------------

Sýnidæmi
^^^^^^^^

Í pólhnitum verður höfuðgrein lograns

.. math:: {{\operatorname{Log}}}z =\ln r+i\theta,  \qquad z=re^{i\theta}, \ -\pi<\theta<\pi.

 Þar með eru raun- og þverhluti :math:`{{\operatorname{Log}}}z` gefin í
pólhnitum með :math:`u(x,y)=\ln r` og :math:`v(x,y)=\theta`. Við getum
því auðveldlega staðfest að :math:`{{\operatorname{Log}}}` sé fágað
fall, með því að beita niðurstöðunni í sýnidæmi :ref:‘sy:polhnit‘

.. math::

   \dfrac{\partial u}{\partial r}=\dfrac 1r=\dfrac 1r\cdot \dfrac 
   {\partial v}{\partial \theta}\qquad \text{ og } \qquad
   \dfrac 1r\cdot \dfrac{\partial u}{\partial \theta}=0=\dfrac {\partial
   v}{\partial r}.

 Það er aðeins meiri fyrirhöfn að sýna fram á að
:math:`{{\operatorname{Log}}}` sé fágað með því að deilda með tilliti
til :math:`x` og :math:`y`.

--------------

.. \_sy:2.5.7:

Sýnidæmi
^^^^^^^^

Nú ætlum við að finna fágaða framlengingu á fallinu
:math:`f(x)=\arccos x` frá bilinu :math:`]-1,1[` yfir á opið mengi
:math:`X` í :math:`{{\mathbb  C}}` þannig að :math:`f(z)` verði
andhverfa tvinngilda :math:`\cos`–fallsins, :math:`\cos f(z)=z`. Við
þurfum þá að byrja á því að leysa jöfnuna :math:`z=\cos w`,

.. math::

   \begin{gathered}
   z=\cos w =\frac 12(e^{iw}+e^{-iw}),\\
   e^{iw}-2z+e^{-iw}=0, \\
   e^{2iw}-2ze^{iw}+1=(e^{iw}-z)^2-z^2+1=0,\\
   (e^{iw}-z)^2=-(1-z^2).\end{gathered}

 Nú þurfum við að taka kvaðratrót, svo við látum
:math:`{{\operatorname{Log}}}` tákna höfuðgrein lografallsins. Þá er
höfuðgrein kvaðratrótarinnar fallið

.. math::

   {{\mathbb  C}}\setminus{{\mathbb  R}}_- \to {{\mathbb  C}}, \qquad
   z\mapsto z\sp{\frac 12}=\exp(\tfrac 12{{\operatorname{Log}}}z).

 Þar með er

.. math::

   (1-z^2)^{1/2}=\exp(\tfrac 12{{\operatorname{Log}}}(1-z^2)), \qquad z\in
   X={{\mathbb  C}}\setminus\{x\in {{\mathbb  R}}; |x|\geq 1\},

.. figure:: ./myndir/fig033.svg

:align: center

:alt: Skilgreiningarsvæði :math:`\arccos`

2BeRemovedMynd: Skilgreiningarsvæði :math:`\arccos`

því :math:`z\in X` þá og því aðeins að
:math:`1-z\sp 2\in {{\mathbb  C}}\setminus\{x\in {{\mathbb  R}};
x\leq 0\}`. Við höldum nú áfram með útreikningana,

.. math:: e^{iw}=z\pm i(1-z^2)^{1/2}.

 Til þess að sjá hvort formerkið á að taka, þá athugum við að
:math:`\cos {\pi}/2=0` segir að :math:`z=0` svari til :math:`w=\pi/2`,
svo :math:`-` er útilokað og við sjáum jafnframt að

.. math::

   f(z) = w=-i\lambda(z+i(1-z^2)^{\frac 12}), 
   \qquad z\in X,

 þar sem :math:`\lambda` er einhver logri. Til þess að sýna að við megum
taka :math:`{\lambda}` sem höfuðgrein lografallsins, þá þurfum við að
vita að myndmengið af vörpuninni

.. math::

   X\to {{\mathbb  C}}, \qquad z\mapsto z+i(1-z^2)^{\frac 12},

   .. _4.6.4:

 sé í skilgreiningarsvæði höfuðgreinarinnar. Við sjáum að þessi vörpun
varpar :math:`x\in ]-1,1[` á :math:`x+i\sqrt{1-x^2}` sem er punktur í
efra hálfplaninu
:math:`\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z>0\}`.

Nú kemur í ljós að engin rauntala liggur í myndmenginu. Það sjáum við
með því að gera ráð fyrir að :math:`z+i(1-z\sp 2)\sp{\frac
12}=t\in {{\mathbb  R}}` og fáum

.. math::

   i(1-z\sp 2)\sp{\frac 12}=t-z,\qquad
   -(1-z\sp 2)=t\sp 2+z\sp 2-2tz,\qquad
   z=\dfrac{t\sp 2+1}{2t}\in {{\mathbb  R}}.

 0 2 1 0 = -1 0 by-1 1 = 1 2 = -0 2 by100 = 1 100 by2 100 by1 1 0 0 = 0
by-1 9 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt Jafnan
:math:`z^2=1+(t-z)^2` segir okkur að :math:`|z|\geq 1`. Við höfum því
:math:`z\not\in X`.

Þar sem mengið   :math:`X`  er samanhangandi, þá er myndmengi þess við
vörpunina (:ref:‘4.6.4‘) hlutmengi í efra hálfplaninu
:math:`\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z>0\}`, en það er
aftur hlutmengi af skilgreiningarmengi :math:`{{\operatorname{Log}}}`.
Við höfum því

.. math::

   f(z) = -i{{\operatorname{Log}}}(z+i(1-z^2)^{\frac 12}), 
   \qquad z\in {{\mathbb  C}}\setminus\{x\in {{\mathbb  R}};
   |x|\geq 1\}.

 Til þess að staðfesta að þessi formúla gefi okkur virkilega fágaða
framlengingu á :math:`\arccos`–fallinu, þá setjum við
:math:`z=x\in ]-1,1[` inn í formúluna og við sjáum á myndinni að

.. math::

   \begin{aligned}
   f(x)&=-i{{\operatorname{Log}}}(x+i(1-x^2)^{1/2})\\ 
   &={{\operatorname{Arg}}}(x+i\sqrt{1-x^2})-i\ln|\sqrt{1-x^2}+ix|\\
   &={{\operatorname{Arg}}}(x+i\sqrt{1-x^2})=\arccos x, \qquad x\in [-1,1].\end{aligned}

--------------

Sýnidæmi
^^^^^^^^

Með sama hætti getum við fundið fágaða framlengingu á fallinu
:math:`f(x)=\arcsin x` frá bilinu :math:`]-1,1[` yfir á opið mengi
:math:`X` í :math:`{{\mathbb  C}}`, þannig að :math:`f(z)` verði
andhverfa tvinngilda :math:`\sin`–fallsins, :math:`\sin f(z)= z`. Eins
og í síðasta dæmi, þá byrjum við á því að leysa jöfnuna
:math:`z=\sin w`,

.. math::

   \begin{gathered}
   z=\sin w =\frac 1{2i}(e^{iw}-e^{-iw}),\\
   e^{iw}-2iz-e^{-iw}=0, \\
   e^{2iw}-2ize^{iw}-1=(e^{iw}-iz)^2+z^2-1=0,\\
   (e^{iw}-iz)^2=1-z^2.\end{gathered}

 Nú þurfum við að taka kvaðratrót. Það gerum við með sama hætti og í
síðasta sýndæmi og við skilgreinum :math:`X` eins og þar. Þá gildir

.. math:: e^{iw}-iz=\pm(1-z^2)^{1/2}.

 Til þess að sjá hvort formerkið á að taka, þá athugum við að
:math:`\sin 0=0` segir að :math:`z=0` svari til :math:`w=0`, svo
:math:`-` er útilokað og við sjáum jafnframt að

.. math::

   f(z)= w=-i\lambda((1-z^2)^{1/2}+iz), \qquad z\in {{\mathbb  C}}\setminus\{x\in {{\mathbb  R}};
   |x|\geq 1\},

 þar sem :math:`{\lambda}` er einhver logri. Nú er eftir að sýna
:math:`{\lambda}` sé höfuðgrein lograns. Til þess þurfum við að vita að
myndmengið af vörpuninni

.. math::

   X\to {{\mathbb  C}}, \qquad z\mapsto (1-z^2)^{\frac 12}+iz,


   .. _4.6.5:

 sé í skilgreiningarsvæði höfuðgreinarinnar.

Nú kemur í ljós að engin hrein þvertala liggur í myndmenginu. Það sjáum
við með því að gera ráð fyrir að :math:`(1-z\sp 2)\sp{\frac 12}+iz=it`,
:math:`t\in {{\mathbb  R}}` og fáum

.. math::

   (1-z\sp 2)\sp{\frac 12}=i(t-z),\qquad
   (1-z\sp 2)=-(t\sp 2+z\sp 2-2tz),\qquad
   z=\dfrac{-t\sp 2-1}{2t}.

 0 2 1 0 = -1 0 by-1 1 = 1 2 = -0 2 by100 = 1 100 by2 100 by1 1 0 0 = 0
by-1 12 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 0pt
0 0pt Þar með er :math:`z` rauntala og jafnan :math:`z^2=1+(t-z)^2`
segir okkur að :math:`|z|\geq 1`. Þar með höfum við að
:math:`z\not\in X`.

Við sjáum að vörpunin :ref:‘4.6.5‘ varpar :math:`x\in ]-1,1[` á
:math:`\sqrt{1-x^2}+ix` sem er punktur í hægra hálfplaninu
:math:`\{z\in {{\mathbb  C}}; {{\operatorname{Re\, }}}z>0\}`. Þar sem
mengið :math:`X` er samanhangandi þá er myndmengi vörpunarinnar
hlutmengi í hægra hálfplaninu
:math:`\{z\in {{\mathbb  C}}; {{\operatorname{Re\, }}}z>0\}`, en það er
aftur hlutmengi af skilgreiningarmengi :math:`{{\operatorname{Log}}}`.
Við höfum því

.. math::

   \begin{gathered}
   f(z) = -i{{\operatorname{Log}}}((1-z^2)^{\frac 12}+iz), \\
   z\in {{\mathbb  C}}\setminus\{x\in {{\mathbb  R}};|x|\geq 1\}.\end{gathered}

 Til þess að staðfesta að þessi formúla gefi okkur útvíkkun á
:math:`\arcsin`–fallinu, þá setjum við :math:`z=x\in ]-1,1[` inn í
formúluna og fáum

.. math:: f(x)=-i{{\operatorname{Log}}}((1-x^2)^{1/2}+ix)={{\operatorname{Arg}}}(\sqrt{1-x^2}+ix)-i\ln|\sqrt{1-x^2}+ix|.

 Við sjáum á myndinni að
:math:`{{\operatorname{Arg}}}(\sqrt{1-x^2}+ix)=\arcsin x` og við höfum
einnig að :math:`|\sqrt{1-x^2}+ix|=1`, svo

.. math:: \arcsin x=-i{{\operatorname{Log}}}((1-x^2)^{1/2}+ix),\qquad x\in ]-1,1[.

--------------

Sýnidæmi
^^^^^^^^

Að lokum skulum við líta á fágaða útvíkkun á fallinu :math:`\arctan x`,
en það er raunfágað á öllu menginu :math:`{{\mathbb  R}}`. Við byrjum á
því að leysa jöfnuna :math:`z=\tan w`, en hún gefur

.. math::

   z=\dfrac{\sin w}{\cos
   w}=\dfrac{e\sp{iw}-e\sp{-iw}}{i(e\sp{iw}+e\sp{-iw})} =
   \dfrac{e\sp{2iw}-1}{i(e\sp{2iw}+1)}, \qquad
   e\sp{2iw}=\dfrac{iz+1}{-iz+1} =\dfrac{i-z}{i+z}.

 Nú skulum við kanna fyrir hvaða mengi :math:`X` formúlan

.. math::

   f(z)=\dfrac{-i}2 {{\operatorname{Log}}}\bigg(\dfrac{i-z}{i+z}\bigg), \qquad z\in X,


   .. _4.6.6:

 0 2 3 0 4 1 0 = -1 0 by-1 1 = 1 2 = -0 2 by100 = 1 100 by2 100 by1 1 0
0 = 0 by-1 15 0pt 0 0pt 0 0pt 0 0pt 0 0pt 0 50pt 0 0pt 0 0pt 0 0pt 0 0pt
0 0pt 0 0pt 0 0pt 0 0pt 0 0pt gildir. Hún gildir um öll :math:`z` þannig
að :math:`(i-z)/(i+z)=t` er ekki á neikvæða raunásnum. Við skulum taka
:math:`t\leq
0` og sjá hvaða punktar :math:`z` eru þar með útilokaðir. Við leysum
:math:`z` út, :math:`z=i(1-t)/(1+t)` og sjáum þar með að :math:`z` er
hrein þvertala og

.. math:: |z|=(1+|t|)/(1-|t|)\geq 1.

 Hér með höfum við séð að fallið :math:`f` er vel skilgreint með
formúlunni hér að framan ef :math:`X={{\mathbb  C}}\setminus\{ix; x\in
{{\mathbb  R}}, |x|\geq 1\}`. Nú er einungis eftir að sýna fram á að
:math:`f(x)=\arctan x` fyrir öll :math:`x\in {{\mathbb  R}}`. Við
athugum fyrst að

.. math:: f(x)=\dfrac {-i}2 {{\operatorname{Log}}}\bigg(\dfrac{i-x}{i+x}\bigg) = \dfrac 12 {{\operatorname{Arg}}}\bigg( \dfrac{i-x}{i+x}\bigg), \ \  x\in {{\mathbb  R}},

 því :math:`|i-x|=|i+x|` fyrir öll :math:`x\in {{\mathbb  R}}`, svo
:math:`\ln (|i-x|/|i+x|)=0`. Talan
:math:`\theta= {{\operatorname{Arg}}}((i-x)/(i+x))` er hornið milli
tvinntalnanna :math:`i-x` og :math:`i+x` og greinilega gildir
:math:`\tan(\theta/2)=x`. Þar með er niðurstaðan
:math:`f(x)=\theta/2=\arctan x`.

--------------

Sýnidæmi
^^^^^^^^

Sýnið að :math:`\dfrac d{dz}\arcsin z= \dfrac 1{(1-z^2)^{\frac
12}}`,   :math:`\{x\in {{\mathbb  R}}\,;\, |x|\geq 1 \}`.

*Lausn:*   Skrifum :math:`w=\arcsin z`. Þá er :math:`z=\sin w`. Ef við
setjum :math:`f(w)=\sin w`, þá er

.. math::

   f{{\sp{\prime}}}(w)=\cos w=(1-\sin ^2 w)^{\frac 12}
   =(1-z^2)^{\frac 12}

 Hér er höfuðgrein kvaðratrótarinnar tekin. Í sýnidæmi :ref:‘sy:2.5.7‘
vorum við búin að sannfæra okkur um að :math:`1-z^2` væri punktur í
:math:`{{\mathbb  C}}\setminus
{{\mathbb  R}}_-`, sem er skilgreiningarsvæði höfuðgreinarinnar.
Samkvæmt reiknireglunni um afleiður af andhverfu falls er

.. math::

   \dfrac d{dz} \arcsin z=\big(f^{[-1]}\big){{\sp{\prime}}}(z)=
   \dfrac 1{f{{\sp{\prime}}}(w)} =\dfrac 1{(1-z^2)^{\frac 12}}.

Sannanir á nokkrum niðurstöðum
------------------------------

Nú tökum við fyrir sannanir á nokkrum niðurstöðum sem sleppt var í fyrr
í kaflanum. Það er hyggilegt að byrja á því að setja fram skilyrðið um
:math:`{{\mathbb  C}}`-deildanleika fram á nýjan hátt:

.. \_hs4.8.1:

Hjálparsetning
^^^^^^^^^^^^^^

Látum :math:`X` vera opið mengi í :math:`{{\mathbb  C}}`, :math:`a\in X`
og :math:`f:X\to {{\mathbb  C}}` vera fall. Þá gildir:

(i) :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í punktinum
:math:`a` þá og því aðeins að til sé tvinntala :math:`A` og fall
:math:`\varphi_a:X\to {{\mathbb  C}}`, samfellt í :math:`a` og með
:math:`\varphi_a(a)=0`, þannig að

.. math::

   f(z)=f(a)+A(z-a)+(z-a)\varphi_a(z), \qquad z\in X.


   .. _4.8.1:

 Talan :math:`A` er ótvírætt ákvörðuð, :math:`A=f{{\sp{\prime}}}(a)`.

(ii) :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í punktinum
:math:`a` þá og því aðeins að til sé fall
:math:`F_a:X\to {{\mathbb  C}}`, sem er samfellt í :math:`a`, þannig að

.. math::

   f(z)=f(a)+(z-a)F_a(z), \qquad z\in X.


   .. _4.8.2:

 Fallið :math:`F_a` er ótvírætt ákvarðað og
:math:`F_a(a)=f{{\sp{\prime}}}(a)`.

Sönnun
^^^^^^

(i) Ef :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a`, þá
skilgreinum við

.. math::

   \varphi_a(z)=\begin{cases}
   \dfrac{f(z)-f(a)}{z-a}-f{{\sp{\prime}}}(a),& z\neq a,\\ 
   0,& x=a.\end{cases}

 Þá er ljóst að (:ref:‘4.8.1‘) gildir og
:math:`\lim_{z\to a}\varphi(z)=\varphi(a)=0`. Öfugt, ef (:ref:‘4.8.1‘)
gildir, þá er

.. math::

   \lim\limits_{h\to 0} \dfrac{f(a+h)-f(a)}h=
   \lim\limits_{h\to 0}A+\varphi_a(a+h)=A

 og því er :math:`f` :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og
:math:`f{{\sp{\prime}}}(a)=A`.

(ii) leiðir beint af (i). Við tökum :math:`F_a(z)=A+\varphi_a(z)`.

Sönnun
^^^^^^

Sönnun á setningu 2.2.2 Samkvæmt hjálparsetningu :ref:‘hs4.8.1‘ (ii) er

.. math:: \lim_{z\to a} f(z)=f(a)+\lim_{z\to a} (z-a)F_a(z)=f(a).

Sönnun
^^^^^^

Sönnun á setningu 2.2.3 Við beitum hjálparsetningu :ref:‘hs4.8.1‘ í
öllum liðunum. Látum því :math:`F_a,G_a:X\to {{\mathbb  C}}` vera föll
sem eru samfelld í :math:`a` og uppfylla

.. math::

   f(z)=f(a)+(z-a)F_a(z), \quad g(z)=g(a)+(z-a)G_a(z), \qquad z\in X.


   .. _4.8.3:

(i) Setjum :math:`h=\alpha f+\beta g`. Samkvæmt hjálparsetningu
:ref:‘hs4.8.1‘ dugir að sanna að til sé fall :math:`H_a`, sem er
samfellt í :math:`a`, þannig að :math:`h(z)=h(a)+(z-a)H_a(z)`. Af
(:ref:‘4.8.3‘) leiðir að :math:`H_a=\alpha F_a+\beta G_a` og að við fáum
:math:`h{{\sp{\prime}}}(a)=H_a(a)=\alpha F_a(a)+\beta
G_a(a)=\alpha f{{\sp{\prime}}}(a)+\beta g{{\sp{\prime}}}(a)`.

(ii) Setjum nú :math:`h=fg`. Hér dugir að sanna að
:math:`h(z)=h(a)+(z-a)H_a(z)` þar sem :math:`H_a` er samfellt í
:math:`a`. Samkvæmt (:ref:‘4.8.3‘) er

.. math:: h(z)=h(a)+(z-a)\left(F_a(z)g(a)+f(a)G_a(z)+(z-a)F_a(z)G_a(z)\right).

 Þar með er

.. math:: H_a(z)=F_a(z)g(a)+f(a)G_a(z)+(z-a)F_a(z)G_a(z)

 sem er samfellt í :math:`a` og
:math:`H_a(a)=F_a(a)g(a)+f(a)G_a(a)=f{{\sp{\prime}}}(a)g(a)+f(a)g{{\sp{\prime}}}(a)`.

(iii) Fyrst :math:`g(a)\neq 0` og :math:`g` er samfellt í :math:`a`, þá
er mengið :math:`Y=\{z\in X; g(z)\neq 0\}` grennd um punktinn :math:`a`
og við athugum að

.. math::

   \dfrac 1{g(z)} =\dfrac 1{g(a)}+(z-a)\dfrac {-G_a(z)}{g(a)g(z)}, \qquad
   z\in Y.

 Fyrst :math:`g(a)\neq 0` og :math:`g` er samfellt í :math:`a`, þá sjáum
við að fallið

.. math:: z\mapsto \dfrac {-G_a(z)}{g(a)g(z)}, \qquad z\in Y,

 er samfellt í :math:`a` og þar með er :math:`1/g`
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math::

   \left(\dfrac 1g\right){{\sp{\prime}}}(a)= \dfrac{-G_a(a)}{g(a)^2} =
   \dfrac {-g{{\sp{\prime}}}(a)}{g(a)\sp 2}.

 Reglan leiðir nú af þessari formúlu og (ii).

Sönnun
^^^^^^

Sönnun á setningu 2.2.6 (i) Við ætlum að beita hjálparsetningu
:ref:‘hs4.8.1‘ (ii) og látum því :math:`F_a:X\to {{\mathbb  C}}` vera
samfellt í :math:`a` og :math:`G_b:Y\to {{\mathbb  C}}` vera samfellt í
:math:`b` þannig að

.. math::

   f(z)=f(a)+(z-a)F_a(z), \quad z\in X, \qquad g(w)=g(b)+(w-b)G_b(w), \quad
   w\in Y.

 Þá er

.. math::

   \begin{aligned}
   h(z)&=g(f(z))=g(b)+(f(z)-b)G_b(f(z))\\
   &=g(f(a))+(f(z)-f(a))G_b(f(z))\\
   &=h(a)+(z-a)F_a(z)G_b(f(z))\\
   &=h(a)+(z-a)H_a(z).\end{aligned}

 þar sem fallið :math:`H_a(z)=G_b(f(z))F_a(z)` er greinilega samfellt í
:math:`a`, því :math:`F_a` er samfellt í :math:`a`, :math:`f` er
samfellt í :math:`a` og :math:`G_b` er samfellt í :math:`b=f(a)`. Við
höfum
:math:`H_a(a)=G_b(b)F_a(a)=g{{\sp{\prime}}}(b)f{{\sp{\prime}}}(a)`.

(ii) Látum nú :math:`G_b:Y\to {{\mathbb  C}}` vera samfellt í :math:`b`,
:math:`H_a:X\to {{\mathbb  C}}` vera samfellt í :math:`a` og gerum ráð
fyrir að

.. math::

   g(w)=g(b)+(w-b)G_b(w), \quad
   w\in Y, \qquad h(z)=h(a)+(z-a)H_a(z), \quad z\in X.

 Ef við stingum :math:`w=f(z)` inn í fyrri jöfnuna og notum að
:math:`g(f(z))=h(z)`, þá fáum við

.. math::

   (f(z)-f(a))G_b(f(z))=(z-a)H_a(z),\qquad z\in X. 

   .. _4.8.4:

 Fyrst :math:`G_b` er samfellt í :math:`b`,
:math:`G_b(b)=g{{\sp{\prime}}}(b)\neq 0` og :math:`f` er samfellt í
:math:`a`, þá er til grennd :math:`U` um :math:`a` þannig að
:math:`G_b(f(z))\neq 0` fyrir öll :math:`z\in U`. Nú setjum við

.. math::

   F_a(z)=\begin{cases}
   \dfrac{H_a(z)}{G_b(f(z))}, &z\in U,\\
   \dfrac{f(z)-f(a)}{z-a}, &z\in X\setminus U.
   \end{cases}

 Þá gefur (:ref:‘4.8.4‘) að :math:`f(z)=f(a)+(z-a)F_a(z)`. Greinilega er
:math:`F_a` samfellt í punktinum :math:`a` og

.. math:: F_a(a)=\dfrac{H_a(a)}{G_b(f(a))}=\dfrac{h{{\sp{\prime}}}(a)}{g{{\sp{\prime}}}(b)}.

Sönnun
^^^^^^

Sönnun á fylgisetningu 2.2.7 Setjum :math:`h(z)=z`,
:math:`z\in {{\mathbb  C}}`. Þá er :math:`h` fágað á
:math:`{{\mathbb  C}}` og

.. math:: z=h(z)=f\circ f^{[-1]}(z), \qquad z\in Y.

 Hér er :math:`f` í hlutverki :math:`g` og :math:`f^{[-1]}` í hlutverki
:math:`f` í setningu :ref:‘se:2.2.6‘ (ii). Þar með er :math:`f^{[-1]}`
:math:`{{\mathbb  C}}`–deildanlegt í :math:`b` og formúlan
:math:`(f^{[-1]})'(b)=1/f'(a)` gildir.

Sönnun
^^^^^^

Sönnun á setningu 2.3.2 Við sönnum setninguna í sértilfellinu
:math:`\alpha=0`. Almenna tilfellið fæst síðan með því að skipta á
fallinu :math:`f(z)` og :math:`f(z+\alpha)`. Við tökum
:math:`a\in S(0,\varrho)`. Samkvæmt hjálparsetningu :ref:‘hs4.8.1‘ (ii)
dugir að sanna að til sé fall :math:`F_a:X\to {{\mathbb  C}}`, þannig að
:math:`f(z)=f(a)+(z-a)F_a(z)`, :math:`F_a` samfellt í :math:`a` og
:math:`F_a(a)=\sum_{n=1}^\infty na_na^{n-1}`. Við athugum fyrst að

.. math::

   \begin{gathered}
   z^n-a^n=(z-a)(z^{n-1}+az^{n-2}+\cdots+a^{n-2}z+a^{n-1}),\\
    \lim_{z\to a}(z^{n-1}+az^{n-2}+\cdots+a^{n-2}z+a^{n-1}) = na^{n-1}.\end{gathered}

 Af fyrri formúlunni leiðir

.. math::

   \begin{aligned}
   f(z)&=f(a)+\sum_{n=0}^\infty a_n(z^n-a^n)\\
   &=f(a)+(z-a)\sum_{n=1}^\infty 
   a_n (z^{n-1}+az^{n-2}+\cdots+a^{n-2}z+a^{n-1})\end{aligned}

 þar sem síðasta röðin er samleitin fyrir öll :math:`z\in S(0,\varrho)`.
Við setjum því

.. math::

   F_a(z)=\begin{cases}    
   \sum_{n=1}^\infty a_n
   (z^{n-1}+az^{n-2}+\cdots+a^{n-2}z+a^{n-1}),
   &z\in S(0,\varrho),\\
   \dfrac{f(z)-f(a)}{z-a}, \qquad z\in X\setminus S(0,\varrho).
   \end{cases}

 Við þurfum nú einungis að sanna að

.. math:: \lim_{z\to a} F_a(z)=F_a(a)=\sum_{n=1}^\infty na_na^{n-1}.

 Til þess að gera það, þá tökum við :math:`r` sem uppfyllir
:math:`|a|<r<\varrho`, og athugum að

.. math::

   |a_n(z^{n-1}+az^{n-2}+\cdots+a^{n-2}z+a^{n-1})|\leq n|a_n|r^{n-1},
   \qquad |z|\leq r,

 og jafnframt að

.. math:: \sum_{n=1}^\infty n|a_n|r^{n-1}<+\infty,

 því samleitnigeisli raðarinnar er :math:`\geq \varrho>r`. Samleitnipróf
Weierstrass (setning 3.5.3) segir okkur nú að röðin sem skilgreinir
:math:`F_a` sé samleitin í jöfnum mæli á menginu
:math:`\overline S(0,r)`. Þar með er :math:`F_a` samfellt í
:math:`S(0,\varrho)` og

.. math::

   \begin{aligned}
   F_a(a)&=\lim_{z\to a} F_a(z)\\
   &=  \lim_{z\to a}
   \sum_{n=1}^\infty a_n (z^{n-1}+az^{n-2}+\cdots+a^{n-2}z+a^{n-1})\\
   &=\sum_{n=1}^\infty na_na^{n-1}.\end{aligned}

Æfingardæmi
-----------

**.**

Staðfestið að fallið :math:`e^z=e^x(\cos y+i\sin y)` sé fágað með því að
sýna að Cauchy-Riemann-jöfnurnar séu uppfylltar.

**.**

Sýnið að einungis sé til eitt fall
:math:`f\in {{\cal O}}({{\mathbb  C}})` sem uppfyllir
:math:`f(z+w)=f(z)f(w)` fyrir öll :math:`z,w\in {{\mathbb  C}}` og
:math:`f(x)=e^x` fyrir öll :math:`x\in
{{\mathbb  R}}`.

**.**

Hver eftirtalinna falla eru fáguð föll af
:math:`z=x+iy=r(\cos {\theta} +i\sin {\theta})`? Reiknið út
Wirtinger-afleiðurnar :math:`\partial_z f` og
:math:`\partial_{\bar z}f`.

+---------------------------------------------------+-----------------------------------------------------+
| a) :math:`f(z)= 1/(z-2)`,                         | b) :math:`f(z)= z+1/z`,                             |
+---------------------------------------------------+-----------------------------------------------------+
| c) :math:`f(z)= 1/(z^2-1)`,                       | d) :math:`f(z)= z^2|z|^2`,                          |
+---------------------------------------------------+-----------------------------------------------------+
| e) :math:`f(z)= ({{\operatorname{Im\, }}}z)^2`,   | f) :math:`f(z)= r(\cos {\theta}-i\sin {\theta})`,   |
+---------------------------------------------------+-----------------------------------------------------+

**.**

Kannið hvort eftirtalin föll eru fáguð með því að athuga hvort
Cauchy-Riemann- jöfnurnar séu uppfylltar

+-------------------------------------------------------------------------+
| a) :math:`f(z)=x^2-y^2-2ixy`,                                           |
+-------------------------------------------------------------------------+
| b) :math:`f(z)=\frac 12\ln(x^2+y^2)+i\arctan(y/x)`,                     |
+-------------------------------------------------------------------------+
| c) :math:`f(z)=\frac 12\ln(x^2+y^2)+i{{\operatorname{arccot}}}(x/y)`.   |
+-------------------------------------------------------------------------+

**.**

Látum :math:`f: X\to {{\mathbb  C}}`, :math:`f=u+iv` vera fágað fall þar
sem :math:`u={{\operatorname{Re\, }}}f` og
:math:`v={{\operatorname{Im\, }}}f` tákna raun- og þverhluta. Sýnið að
stiglarnir :math:`\nabla u` og :math:`\nabla v` séu innbyrðis hornréttir
í sérhverjum punkti :math:`z\in X`.

**.**

Hlutafleiðuvirkinn

.. math::

   {\Delta}=\dfrac {\partial^2 }{\partial x^2}+  
   \dfrac {\partial^2 }{\partial y^2}

 nefnist *Laplace-virki:hover:‘Laplace!virki‘:hover:‘virki!Laplace‘*,
óhliðraða hlutafleiðujafnan :math:`{\Delta}u=0` nefnist
*Laplace-jafna:hover:‘Laplace!jafna‘:hover:‘jafna!Laplace‘* og lausn
:math:`u:X\to {{\mathbb  C}}` á henni er sögð vera *þýtt fall* á
:math:`X`. Látum :math:`f: X\to {{\mathbb  C}}`, :math:`f=u+iv` vera
fágað fall þar sem :math:`u={{\operatorname{Re\, }}}f` og
:math:`v={{\operatorname{Im\, }}}f` tákna raun- og þverhluta. Sýnið að
bæði :math:`u` og :math:`v` séu þýð föll, þ.e. að þau uppfylli
Laplace–jöfnuna

.. math::

   \dfrac {\partial^2 u}{\partial x^2}+  
   \dfrac {\partial^2 u}{\partial y^2}=  
   \dfrac {\partial^2 v}{\partial x^2}+  
   \dfrac {\partial^2 v}{\partial y^2}=0.

**.**

Sýnið að
:math:`{\Delta}=4\dfrac{{\partial}^2}{{\partial}z{\partial}\bar z}`.

**.**

Sýnið að í pólhnitum :math:`z=re^{i{\theta}}` séu hlutafleiðuvirkjarnir
:math:`{\partial}/{\partial}z`, :math:`{\partial}/{\partial}\bar z` og
:math:`{\Delta}` gefnir með formúlunum:

.. math::

   \begin{gathered}
   \dfrac{\partial}{\partial z} =
   \dfrac {e^{-i\theta}}2\bigg(\dfrac{\partial}{\partial r} -\dfrac ir
   \dfrac{\partial}{\partial \theta}\bigg), \qquad
   \dfrac{\partial}{\partial \bar z} =
   \dfrac {e^{i\theta}}2\bigg(\dfrac{\partial}{\partial r} +\dfrac ir
   \dfrac{\partial}{\partial \theta}\bigg)\\
   \Delta
   =\dfrac{\partial^2}{\partial r^2}+\dfrac 1r
   \dfrac{\partial}{\partial r}
   +\dfrac 1{r^2}\dfrac{\partial^2}{\partial\theta^2}
   =\dfrac 1r\dfrac{\partial}{\partial r}\bigg(
   r\dfrac{\partial}{\partial r}\bigg) +\dfrac 1{r^2}
   \dfrac{\partial^2}{\partial \theta^2}.\end{gathered}

**.**

Sýnið að um sérhvert fágað fall :math:`f: X\to {{\mathbb  C}}` gildi

.. math::

   \bigg( {\partial}_x|f(z)|\bigg)^2 +
   \bigg( {\partial}_y|f(z)|\bigg)^2 = |f{{\sp{\prime}}}(z)|^2,

 fyrir öll :math:`z` þannig að :math:`f(z)\neq 0`.

**.**

Látum :math:`f:X\to {{\mathbb  C}}` vera fágað fall á opnu hlutmengi
:math:`X` í :math:`{{\mathbb  C}}`. Sýnið að Jacobi-ákveðan af fallinu
:math:`f` í punktinum :math:`z` sé :math:`|f{{\sp{\prime}}}(z)|^2`.
Látum :math:`M` vera lokað og takmarkað hlutmengi af
:math:`{{\mathbb  C}}` og gerum ráð fyrir að :math:`f` varpi einhverri
opinni grennd um :math:`M` gagntækt á opna grennd um :math:`N=f(M)`.
Notið formúluna fyrir breytuskipti í tvöföldu heildi til þess að sýna að

.. math::

   \iint\limits_{N}{\varphi}({\zeta})\, d{\xi}d{\eta}=
   \iint\limits_{M}\varphi(f(z))|f{{\sp{\prime}}}(z)|^2\, dxdy,

 fyrir sérhvert fall sem er samfellt í grennd um :math:`N`,
:math:`{\zeta}={\xi}+i{\eta}` og :math:`z=x+iy`.

**.**

Leiðið út eftirfarandi formúlur fyrir andhverfur breiðbogafallanna og
finnið heppilegt mengi þar sem þær gilda:

+---------------------------------------------------------------------------------------------------------+
| a) :math:`{{\operatorname{arcsinh}}}z= {{\operatorname{Log}}}\big( z+(z^2+1)^{\frac 12}\big)`,          |
+---------------------------------------------------------------------------------------------------------+
| b) :math:`{{\operatorname{arccosh}}}z= {{\operatorname{Log}}}\big( z+(z^2-1)^{\frac 12}\big)`,          |
+---------------------------------------------------------------------------------------------------------+
| c) :math:`{{\operatorname{arctanh}}}z= \dfrac 12 {{\operatorname{Log}}}\bigg(\dfrac {1+z}{1-z}\bigg)`   |
+---------------------------------------------------------------------------------------------------------+

**.**

Leiðið út eftirfarandi formúlur fyrir afleiður andhverfu hornafallanna
og breiðbogafallanna:

+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| a) :math:`\dfrac d{dz}\arcsin z= \dfrac 1{(1-z^2)^{\frac 12}}`,                      | b) :math:`\dfrac d{dz} \arccos z= \dfrac {-1}{(1-z^2)^{\frac 12}}`,                 |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| c) :math:`\dfrac d{dz} \arctan z= \dfrac 1{1+z^2}`,                                  | d) :math:`\dfrac d{dz}{{\operatorname{arcsinh}}}z= \dfrac 1{(z^2+1)^{\frac 12}}`,   |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| e) :math:`\dfrac d{dz} {{\operatorname{arccosh}}}z= \dfrac 1{(z^2-1)^{\frac 12}}`,   | f) :math:`\dfrac d{dz} {{\operatorname{arctanh}}}z= \dfrac 1{1-z^2}`.               |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

**.**

Skilgreinum :math:`{\alpha}^z=e^{z{{\operatorname{Log}}}\alpha}`.
Skrifið eftirfarandi tvinntölur á forminu :math:`x+iy`, þar sem
:math:`x` og :math:`y` eru rauntölur, og teiknið þær á mynd:

+------------------------------------------+----------------------+--------------------------+-----------------------------+---------------------------------+
| a) :math:`{{\operatorname{Log}}}(-i)`,   | b) :math:`(-i)^i`,   | c) :math:`2^{{\pi}i}`,   | d) :math:`(1+i)^{(1+i)}`,   | e) :math:`(1+i)^i(1+i)^{-i}`.   |
+------------------------------------------+----------------------+--------------------------+-----------------------------+---------------------------------+

**.**

Finnið allar lausnir jafnanna:

+-----------------------------------------------+---------------------+---------------------------------------+---------------------------+
| a) :math:`{{\operatorname{Log}}}z={\pi}/4`,   | b) :math:`e^z=i`,   | c)\ :math:`^\ast` :math:`\sin z=i`,   | d) :math:`\tan^2 z=-1`.   |
+-----------------------------------------------+---------------------+---------------------------------------+---------------------------+
