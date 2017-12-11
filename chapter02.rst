FÁGUÐ FÖLL
==========

Markgildi og samfelld föll
--------------------------

Skífur og hringir
~~~~~~~~~~~~~~~~~

*Opna skífu* með miðju
:math:`\alpha` og geisla :math:`\varrho` táknum við með

.. math:: S(\alpha,\varrho)=\{z\in {{\mathbb  C}}; |z-\alpha|<\varrho\},

*lokaða skífu* með miðju
:math:`\alpha` og geisla :math:`\varrho` táknum við með

.. math:: \overline S(\alpha,\varrho)=\{z\in {{\mathbb  C}}; |z-\alpha|\leq\varrho\}

og *gataða opna skífu* með miðju :math:`\alpha` og geisla :math:`\varrho` táknum við með

.. math:: S^\ast(\alpha,\varrho)=\{z\in {{\mathbb  C}}; 0<|z-\alpha|<\varrho\}.

Athugið að fallið
:math:`[a,b]\ni \theta\mapsto \alpha+\varrho e^{i\theta}` stikar
hringboga með miðju :math:`\alpha` og geislann :math:`\varrho` frá
punktinum :math:`\alpha+\varrho e^{ia}` til punktsins
:math:`\alpha+\varrho e^{ib}` og að það stikar heilan hring ef
:math:`b-a=2\pi`.

Opin og lokuð mengi
~~~~~~~~~~~~~~~~~~~

Hlutmengi :math:`X` í :math:`{{\mathbb  C}}` er sagt vera :hover:`opið,opið mengi` ef um
sérhvern punkt :math:`a\in X` gildir að til er opin skífa :math:`S(a,r)`
sem er innihaldin í :math:`X`.

Hlutmengi :math:`X` í :math:`{{\mathbb  C}}` er sagt vera :hover:`lokað,lokað mengi` ef
fyllimengi þess :math:`{{\mathbb  C}}\setminus X` er opið.

Ljóst er að mengi :math:`X` er lokað þá og því aðeins að um sérhvern
punkt :math:`a` í fyllimenginu :math:`{{\mathbb  C}}\setminus X` gildir
að til er :math:`r>0` þannig að
:math:`S(a,r)\subset {{\mathbb  C}}\setminus X`.

:hover:`Jaðar,jaðar` hlutmengis :math:`X` í :math:`{{\mathbb  C}}` samanstendur af
öllum punktum :math:`a\in {{\mathbb  C}}` þannig að sérhver opin skífa
:math:`S(a,r)` með :math:`r>0` sker bæði :math:`X` og
:math:`{{\mathbb  C}}\setminus X`. Við táknum jaðar :math:`X` með
:math:`\partial X`.

Ef :math:`X` er opið, þá er
:math:`\partial X\subset {{\mathbb  C}}\setminus X`.

Ef :math:`X` er lokað, þá er :math:`\partial X\subset X`.

Punktur :math:`a\in {{\mathbb  C}}` nefnist :hover:`þéttipunktur` mengisins
:math:`X` ef um sérhvert :math:`r>0` gildir að gataða opna skífan
:math:`S^\ast(a,r)` inniheldur punkta úr :math:`X`.

Hlutmengi :math:`X` í :math:`{{\mathbb  C}}` er sagt vera
:hover:`vegsamanhangandi` ef um sérhverja tvo punkta :math:`a` og :math:`b` í
:math:`X` gildir að til er samfelldur ferill
:math:`[0,1]\ni t\mapsto \gamma(t)\in {{\mathbb  C}}` sem er innihaldinn
í :math:`X`,  :math:`\gamma(0)=a` og :math:`\gamma(1)=b`.

Opið vegsamanhangandi mengi nefnist :hover:`svæði`.

Athugið að sérhver opin skífa er svæði, því sérhverja tvo punkta í henni
má tengja saman með línustriki. Lokaðar skífur eru samanhangandi, og
sama er að segja um gataðar skífur.

Markgildi
~~~~~~~~~

Látum nú :math:`X` vera hlutmengi í :math:`{{\mathbb  C}}` og
:math:`f:X\to {{\mathbb  C}}` vera fall.

Við segjum að :math:`f(z)` stefni á tvinntöluna :math:`L` þegar
:math:`z` stefnir á :math:`a`, ef :math:`a` er þéttipunktur í :math:`X`
og fyrir sérhvert :math:`\varepsilon>0` gildir að til er
:math:`\delta>0` þannig að

.. math:: |f(z)-L|<\varepsilon \qquad \text{ fyrir öll } z\in X\cap S^\ast(a,\delta).

Við köllum þá töluna :math:`L` :hover:`markgildi` :math:`f`  *þegar* :math:`z` 
*stefnir á* :math:`a` og skrifum

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
einhverju mengi.

Ef :math:`X` er opið hlutmengi í :math:`{{\mathbb  C}}` þá látum við
:math:`C(X)` tákna mengi allra samfelldra falla
:math:`f:X\to {{\mathbb  C}}`. Það er til mikilla þæginda að gera frá
byrjun ráð fyrir að föllin séu tvinntölugild. 

Við látum :math:`C^ m(X)` tákna mengi allra :math:`m` sinnum 
:hover:`samfellt deildanlegra,samfellt diffranlegur` falla. Hér er átt við að allar hlutafleiður fallsins :math:`f` af stigi :math:`\leq m` eru til og þar að auki samfelldar. Við skrifum :math:`C^0(X)=C(X)` og táknum mengi óendanlega oft deildanlegra falla með :math:`C^{\infty}(X)`.

Fáguð föll
----------

Látum :math:`f:X\to {{\mathbb  C}}` vera fall á opnu hlutmengi :math:`X`
af :math:`{{\mathbb  C}}`. Ef við látum :math:`z` tákna tvinnbreytistærð
með gildi í :math:`X`, þá getum við skrifað

.. math::

  f(z)=u(z)+iv(z)=u(x,y)+iv(x,y), \qquad z=x+iy=(x,y) \in X,

þar sem föllin :math:`u={{\operatorname{Re\, }}}f` og
:math:`v={{\operatorname{Im\, }}}f` eru raunhluti og þverhluti fallsins
:math:`f`. Við getum þá jafnframt litið á :math:`f` sem vigurgilt fall
af tveimur raunbreytistærðum

.. math::

  f:X\to {{\mathbb  R}}^ 2, \qquad f(x,y)=(u(x,y), v(x,y)).

Hugtök eins og samfelldni, deildanleiki og heildanleiki eru skilgreind
eins og venjulega fyrir vigurgild föll. Þetta þýðir að :math:`f` er
samfellt á :math:`X`, :math:`f\in C(X)`, þá og því aðeins að föllin
:math:`u` og :math:`v` séu samfelld á :math:`X`, :math:`u,v\in C(X)`.

Eins er :math:`f` :math:`k`–sinnum samfellt deildanlegt á :math:`X`,
:math:`f\in C^ k(X)` þá og því aðeins að :math:`u,v\in C^ k(X)` og
við skilgreinum hlutafleiður af :math:`f` sem tvinnföllin

.. math::

  \begin{gathered}
   \partial_xf=\partial_xu+i\partial_xv, \qquad
   \partial_yf=\partial_yu+i\partial_yv,\\
   \partial^ 2_xf=\partial^ 2_xu+i\partial^ 2_xv, \qquad
   \partial^ 2_{xy}f=\partial^ 2_{xy}u+i\partial^ 2_{xy}v,\qquad
   \partial^ 2_yf=\partial^ 2_yu+i\partial^ 2_yv.\end{gathered}

Þannig er síðan haldið áfram eftir því sem deildanleiki :math:`u` og
:math:`v` endist. Nú ætlum við að innleiða nýtt deildanleikahugtak, þar
sem við lítum á breytistærðina sem :hover:`tvinntölu,tvinntala` en ekki
sem vigur:

:math:`{{\mathbb  C}}`-deildanleg föll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Látum :math:`f:X\to {{\mathbb  C}}` vera fall á opnu hlutmengi :math:`X`
af :math:`{{\mathbb  C}}`. Við segjum að :math:`f` sé
:math:`{{\mathbb  C}}` *–deildanlegt* 
í punktinum :math:`a\in X` ef markgildið

.. math::

  \lim _{\substack{ h\to 0\\ h\in{{\mathbb  C}}}}
    \dfrac{f(a+h)-f(a)}h  

er til. Markgildið táknum við með :math:`f{{^{\prime}}}(a)` og köllum
það
:math:`{{\mathbb  C}}` *–afleiðu* 
fallsins :math:`f` í punktinum :math:`a`. 

Fall :math:`f:X\to {{\mathbb  C}}` er sagt vera :hover:`fágað,fágað fall` á opna menginu :math:`X` ef :math:`f\in C^1(X)` og :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í sérhverjum punkti í :math:`X`. 

Við látum :math:`{{\cal O}}(X)` tákna mengi allra
fágaðra falla á :math:`X`. Við segjum að :math:`f` sé *fágað í punktinum*
:math:`a` ef til er opin grennd :math:`U` um :math:`a` þannig að
:math:`f` sé fágað í :math:`U`. 

Fallið :math:`f` er sagt vera :hover:`heilt fall` 
ef það er fágað á öllu :math:`{{\mathbb  C}}`.

Þessi skilgreining er eins og skilgreiningin af afleiðu falls af einni
raunbreytistærð.



Setning
^^^^^^^

Ef :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a`, þá er
:math:`f` samfellt í :math:`a`.

Reiknireglur fyrir :math:`{{\mathbb  C}}`-afleiður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reiknireglurnar fyrir :math:`{{\mathbb  C}}`-afleiður eru nánast þær
sömu og reiknireglurnar fyrir afleiður falla af einni raunbreytistærð.



Setning
^^^^^^^

Látum :math:`f,g:X\to {{\mathbb  C}}` vera föll, :math:`a\in X`,
:math:`\alpha,\beta\in {{\mathbb  C}}` og gerum ráð fyrir að :math:`f`
og :math:`g` séu :math:`{{\mathbb  C}}`–deildanleg í :math:`a`. Þá
gildir

(i) :math:`\alpha f+\beta g` er :math:`{{\mathbb  C}}`–deildanlegt í
:math:`a` og

.. math:: (\alpha f+\beta g){{^{\prime}}}(a)=\alpha f{{^{\prime}}}(a)+\beta g{{^{\prime}}}(a).

(ii) (*Leibniz-regla*). :math:`fg`
er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math:: (fg){{^{\prime}}}(a)=f{{^{\prime}}}(a)g(a)+f(a)g{{^{\prime}}}(a).

(iii) Ef :math:`g(a)\neq 0`, þá er :math:`f/g`
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math:: (f/g){{^{\prime}}}(a)=\dfrac{f{{^{\prime}}}(a)g(a)-f(a)g{{^{\prime}}}(a)}{g(a)^2}.

Fylgisetning
^^^^^^^^^^^^

:math:`{{\cal O}}(X)` er línulegt rúm yfir :math:`{{\mathbb  C}}`.

Ef :math:`f_1,f_2,\dots, f_n` eru :math:`{{\mathbb  C}}`–deildanleg í
:math:`a` og :math:`\alpha_1,\dots,\alpha_n\in {{\mathbb  C}}`, þá fáum
við með þrepun að :math:`f=\alpha_1f_1+\cdots+\alpha_nf_n` er
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math:: f{{^{\prime}}}(a)=\alpha_1 f_1{{^{\prime}}}(a)+\cdots+\alpha_nf_n{{^{\prime}}}(a).

Eins fáum við með þrepun að margfeldið :math:`f=f_1f_2\cdots f_n` er
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og

.. math::

  f{{^{\prime}}}(a)= \sum_{j=1}^n f_j{{^{\prime}}}(a)\bigg(\prod_{\substack{ k=1\\ k\neq
    j}}^n f_k(a)\bigg).

Athugið að af þessu leiðir formúlan

.. math::

  \dfrac{f{{^{\prime}}}(a)}{f(a)} =  \dfrac{f_1{{^{\prime}}}(a)}{f_1(a)}+\cdots+
   \dfrac{f_n{{^{\prime}}}(a)}{f_n(a)}.

Sýnidæmi
^^^^^^^^

\(i) Allar margliður

.. math:: P(z)= a_0+a_1z+\cdots+a_mz^m, \qquad z\in {{\mathbb  C}},

eru fáguð föll á öllu :math:`{{\mathbb  C}}` og afleiðan er

.. math:: P{{^{\prime}}}(z)= a_1+2a_2z+\cdots+ma_mz^{m-1}, \qquad z\in {{\mathbb  C}}.

\(ii) Sérhvert rætt fall :math:`R=P/Q`, þar sem :math:`P` og :math:`Q`
eru margliður, er fágað fall á menginu
:math:`\{z\in {{\mathbb  C}}; Q(z)\neq 0\}` og

.. math:: R{{^{\prime}}}(z)= \dfrac{P{{^{\prime}}}(z)Q(z)-P(z)Q{{^{\prime}}}(z)}{Q(z)^2}.

:hover:`Keðjureglan` fyrir
:math:`{{\mathbb  C}}`–deildanleg föll er eins og keðjureglan fyrir
raunföll:



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

.. math:: h{{^{\prime}}}(a)=g{{^{\prime}}}(b)f{{^{\prime}}}(a).

(ii) Ef :math:`g` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`b`,
:math:`g{{^{\prime}}}(b)\neq 0`, :math:`h` er
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og :math:`f` er samfellt
í :math:`a`, þá er :math:`f` :math:`{{\mathbb  C}}`–deildanlegt í
:math:`a` og

.. math:: f{{^{\prime}}}(a)=h{{^{\prime}}}(a)/g{{^{\prime}}}(b).

Mikilvæg afleiðing af þessari setningu er:



Fylgisetning
^^^^^^^^^^^^

Látum :math:`X` og :math:`Y` vera opin hlutmengi af
:math:`{{\mathbb  C}}`, :math:`f:X\to Y` vera gagntækt fall. Ef
:math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` og
:math:`f{{^{\prime}}}(a)\neq 0`, þá er andhverfa fallið
:math:`f^{[-1]}` :math:`{{\mathbb  C}}`–deildanlegt í :math:`b=f(a)` og

.. math::

  \left(f^{[-1]}\right){{^{\prime}}}(b)= \dfrac 1{f{{^{\prime}}}(a)}.

Cauchy-Riemann-jöfnur
~~~~~~~~~~~~~~~~~~~~~

Nú skulum við gera ráð fyrir því að :math:`f` sé
:math:`{{\mathbb  C}}`–deildanlegt í punktinum :math:`a` og huga að
sambandinu milli :math:`f{{^{\prime}}}(a)`, :math:`{\partial}_xf(a)`
og :math:`{\partial}_yf(a)`. Ef við skrifum
:math:`a=\alpha+i\beta=(\alpha, \beta)` og látum :math:`h\to 0` eftir rauntölunum, þá fáum við

.. math::

  \begin{aligned}
   f{{^{\prime}}}(a)=&\lim_{\substack{h\to 0\\ h\in {{\mathbb  R}}}}
   \dfrac{u(\alpha+h,\beta)-u(\alpha,\beta)}h+i
   \dfrac{v(\alpha+h,\beta)-v(\alpha,\beta)}h\\
   =&\partial_xu(a)+i\partial_xv(a)=\partial_xf(a).\nonumber\end{aligned}

Ef við látum hins vegar :math:`h\to 0` eftir þvertölum, :math:`h=ik`,
:math:`k\in {{\mathbb  R}}`, þá fáum við

.. math::

  \begin{aligned}
   f{{^{\prime}}}(a)&=\lim_{\substack{k\to 0\\ k\in {{\mathbb  R}}}}
   \dfrac{u(\alpha,\beta+k)-u(\alpha,\beta)}{ik}+i
   \dfrac{v(\alpha,\beta+k)-v(\alpha,\beta)}{ik}\\
   &=-i(\partial_yu(a)+i\partial_yv(a))=-i\partial_yf(a).\nonumber\end{aligned}

Við höfum því:



Setning
^^^^^^^

Látum :math:`f=u+iv:X\to {{\mathbb  C}}` vera fall af :math:`z=x+iy` á
opnu hlutmengi :math:`X` í :math:`{{\mathbb  C}}`. Ef :math:`f` er
:math:`{{\mathbb  C}}`–deildanlegt í :math:`a\in X`, þá eru báðar
hlutafleiðurnar :math:`\partial_xf(a)` og :math:`\partial_yf(a)` til og

.. math::

  f{{^{\prime}}}(a)=\partial_xf(a)=-i\partial_yf(a).

Þar með gildir *Cauchy–Riemann–jafnan*

.. math::

  \tfrac 12\big(\partial_xf(a)+i\partial_yf(a)\big)=0,

og hún jafngildir hneppinu

.. math::

  \partial_xu(a)=\partial_yv(a), \qquad \partial_yu(a)=-\partial_xv(a),

sem venja er að kalla Cauchy–Riemann–jöfnur, í fleirtölu.

Wirtinger-afleiður
~~~~~~~~~~~~~~~~~~

Til þess að glöggva okkur betur á Cauchy–Riemann–jöfnunni, þá skulum við
rifja það upp að fall :math:`f:X\to {{\mathbb  R}}^2` er sagt vera
deildanlegt í punktinum :math:`a`, ef til er línuleg vörpun
:math:`L:{{\mathbb  R}}^2\to {{\mathbb  R}}^2` þannig að



.. math::

  \lim_{\substack{h\to 0\\ h\in {{\mathbb  R}}^2}}
   \dfrac{\| f(a+h)-f(a)-L(h)\|}{\|h\|}= 0,

þar sem :math:`\|z\|` táknar lengd vigursins :math:`z`. 

Vörpunin :math:`L` er ótvírætt ákvörðuð. Hún nefnist afleiða :math:`f` í
punktinum :math:`a` og er oftast táknuð með :math:`d_af`, :math:`df_a`
eða :math:`Df(a)`. 

Með því að velja vigurinn :math:`h` af gerðinni
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

Þetta fylki nefnist *Jacobi–fylki* :math:`f` í
punktinum :math:`a`. Nú skrifum við :math:`z=(x,y)`,
:math:`a=({\alpha},{\beta})` og sjáum að markgildið hér fyrir ofan jafngildir því
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
   \end{matrix}\right](y-{\beta})+
   \|z-a\|F_a(z),

þar sem :math:`F_a:X\to {{\mathbb  R}}^2` er samfellt í :math:`a` og
:math:`F_a(a)=0`. Nú skulum við líta á :math:`f` sem tvinngilt fall
:math:`f=u+iv`. Þá er þessi jafna jafngild

.. math::

  f(z)=f(a)+ {\partial}_xf(a)(x-{\alpha})+{\partial}_yf(a)(y-{\beta})
   +(z-a)\varphi_a(z),

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

Tölurnar :math:`{\partial}_zf(a)` og :math:`{\partial}_{\bar z}f(a)`
nefnast *Wirtinger–afleiður* fallsins
:math:`f` í punktinum :math:`a` og virkinn :math:`{\partial}_{\bar z}`
nefnist *Cauchy–Riemann–virki*.

--------------

Hugsum okkur nú að :math:`f:X\to {{\mathbb  C}}` sé eitthvert fall og að
til séu tvinntölur :math:`A`, :math:`B` og fall
:math:`\varphi_a:X\to {{\mathbb  C}}`, samfellt í :math:`a` með
:math:`\varphi_a(a)=0`, þannig að

.. math::

  f(z)=f(a)+A(z-a)+B\overline{(z-a)}+(z-a)\varphi_a(z).

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

Látum :math:`X\subset {{\mathbb  C}}` vera opið, :math:`a\in X` og
:math:`f:X\to {{\mathbb  C}}` vera fall. Þá gildir:

(i) :math:`f` er deildanlegt í :math:`a` þá og því aðeins að til séu
tvinntölur :math:`A`, :math:`B` og fall
:math:`\varphi_a:X\to {{\mathbb  C}}`, samfellt í :math:`a` og með
:math:`\varphi(a)=0`, þannig að

.. math:: f(z)=f(a)+A(z-a)+B\overline{(z-a)}+(z-a)\varphi_a(z).

(ii) :math:`f` er :math:`{{\mathbb  C}}`–deildanlegt í :math:`a` þá og
því aðeins að :math:`f` sé deildanlegt í :math:`a` og
:math:`{\partial}_{\bar z}f(a)=0`. Þá er
:math:`f{{^{\prime}}}(a)={\partial}_zf(a)`.

(iii) :math:`f` er fágað í :math:`X` þá og því aðeins að :math:`f` sé
samfellt deildanlegt í :math:`X` og uppfylli Cauchy–Riemann–jöfnuna
:math:`{\partial}_{\bar z}f=0` í :math:`X`. Við höfum þá

.. math::

  f{{^{\prime}}}=\dfrac{df}{dz}=\dfrac{\partial f}{\partial z}=\dfrac 12\bigg(
   \dfrac{\partial f}{\partial x}-i\dfrac{\partial f}{\partial y}\bigg).

--------------

Reikningur með hlutafleiðunum með tilliti til :math:`z` og
:math:`\bar z` er alveg eins of reikningur með óháðu breytunum :math:`x`
og :math:`y`.

Ef fallið :math:`f(z)=f(x+iy)` er gefið með formúlu í :math:`x` og
:math:`y`, þá notum við formúlurnar :math:`x=(z+\bar z)/2` og
:math:`y=(z-\bar z)/(2i)` til þess að skipta á óháðu breytunum :math:`x`
og :math:`y` yfir í breyturnar :math:`z` og :math:`\bar z`. Til þess að
kanna hvort fall er fágað þá deildum við eins og þetta séu óháðar
breytur og könnum hvort

.. math:: \dfrac{\partial f}{\partial\bar z}=0.

Ef :math:`\bar z` kemur alls ekki fyrir í formúlunni, þá er :math:`f`
fágað.

Samleitnar veldaraðir
---------------------

Samleitnar veldaraðir
~~~~~~~~~~~~~~~~~~~~~

Einu dæmin um fáguð föll sem við höfum nefnt til þessa eru margliður
:math:`P`, en þær eru fágaðar á öllu :math:`{{\mathbb  C}}`, og ræð föll
:math:`R=P/Q`, en þau eru fáguð á
:math:`{{\mathbb  C}}\setminus\{z\in {{\mathbb  C}}; Q(z)=0\}`. 

Nú ætlum við að bæta verulega við dæmaforðann með því að sanna að öll föll, sem unnt er að setja fram með samleitnum veldaröðum, séu fáguð á
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
vera :hover:`raunfágað,raunfágaður` ef það hefur þann eiginleika að í grennd um sérhvern
punkt í :math:`U` er hægt að setja :math:`f` fram með samleitinni
veldaröð.

--------------

Fallið :math:`z\mapsto 1/(1-z)` er fágað á
:math:`{{\mathbb  C}}\setminus\{1\}` og það gefið með geómetrísku
röðinni

.. math:: \dfrac 1{1-z}=\sum_{n=0}^\infty z^n, \qquad z\in S(0,1).

Veldisvísisfallið, hornaföllin og breiðbogaföllin eru öll gefin með
samleitnum veldaröðum á :math:`{{\mathbb  R}}` og fáguðu framlengingar
þeirra eru því gefnar með sömu röðum á öllu :math:`{{\mathbb  C}}`

.. math::

  \begin{gathered}
   \exp z =e^ z = \sum_{n=0}^\infty \dfrac 1{n!}z^n, \\
   \cos z = \sum_{k=0}^ \infty \dfrac {(-1)^ k}{(2k)!}z^{2k}, \quad
   \sin z = \sum_{k=0}^ \infty \dfrac {(-1)^ k}{(2k+1)!}z^{2k+1},
   \quad\\
   \cosh z = \sum_{k=0}^ \infty \dfrac {1}{(2k)!}z^{2k}, \quad
   \sinh z = \sum_{k=0}^ \infty \dfrac {1}{(2k+1)!}z^{2k+1}.\end{gathered}



Setning
^^^^^^^

Gerum ráð fyrir að :math:`X` sé opið hlutmengi af
:math:`{{\mathbb  C}}`, :math:`S(\alpha,\varrho)\subset X`, að
:math:`f:X\to {{\mathbb  C}}` sé fall, sem gefið er á
:math:`S(\alpha,\varrho)` með samleitinni veldaröð,

.. math:: f(z)=\sum_{n=0}^\infty a_n(z-\alpha)^n, \qquad z\in S(\alpha,\varrho).

Þá er :math:`f` fágað á :math:`S(\alpha,\varrho)` og

.. math::

  f{{^{\prime}}}(z)=\sum_{n=1}^\infty na_n(z-\alpha)^{n-1}, \qquad z\in
   S(\alpha,\varrho).

--------------

Ef :math:`\sum_{n=0}^\infty a_nz^n` og :math:`\sum_{n=0}^\infty b_nz^n`
eru tvær samleitnar veldaraðir með samleitnigeisla :math:`\varrho_a` og
:math:`\varrho_b`, þá höfum við fáguð föll :math:`f` og :math:`g` í
:math:`S(\alpha,\varrho_a)` og :math:`S(\alpha,\varrho_b)` sem gefin eru
með

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

Eftirfarandi setning nefnist :hover:`samsemdarsetning`
fyrir samleitnar veldaraðir:

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

Fylgisetning
^^^^^^^^^^^^

Ef  :math:`\sum_{n=0}^{\infty} a_nx^n` er samleitin veldaröð, :math:`I`
er opið bil sem inniheldur :math:`0` og :math:`\sum_{n=0}^{\infty} a_nx^n=0` fyrir öll :math:`x\in I`, þá er :math:`a_n=0` fyrir öll
:math:`n=0,1,2,\dots`.

--------------

Við sáum hér að framan að sérhvert fall sem gefið er með
veldaraðaframsetningu á einhverri skífu er fágað. Nú hugum við að
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

    Mynd: Skífa í skilgreiningarsvæði :math:`f`

--------------

Við skulum skoða nokkrar afleiðingar:

Fylgisetning
^^^^^^^^^^^^

Ef :math:`f\in {{\cal O}}(X)`, þá er
:math:`f{{^{\prime}}}\in {{\cal O}}(X)`.

--------------

Nú sjáum við að fallið :math:`f{{^{\prime}}}` er fágað og afleiða þess
:math:`f{{^{\prime\prime}}}` er einnig fáguð og þannig áfram út í hið
óendanlega. Fyrir sérhvert fágað fall :math:`f\in {{\cal O}}(X)`
skilgreinum við hærri afleiður :math:`f^{(k)}` með þrepun
:math:`f^{(0)}=f` og :math:`f^{(k)}=\big(f^{(k-1)}\big){{^{\prime}}}`,
fyrir :math:`k\geq 1`. Við fáum síðan:



Setning
^^^^^^^

Látum :math:`X` vera opið hlutmengi af :math:`{{\mathbb  C}}`,
:math:`f\in {{\cal O}}(X)`, :math:`\alpha\in X` og :math:`0<\varrho<d(\alpha,\partial X)`. Þá er

.. math::

  f(z)= \sum\limits_{n=0}^\infty \dfrac
   {f^{(n)}(\alpha)}{n!}(z-\alpha)^n, \qquad z\in S(\alpha,\varrho).

Þessi veldaröð kallast
*Taylor–röð* *fallsins* :math:`f`  *í punktinum* :math:`\alpha`.

Skilgreining
^^^^^^^^^^^^

Látum :math:`f:Y\to {{\mathbb  C}}` vera raunfágað fall á opnu mengi
:math:`Y` á :math:`{{\mathbb  R}}` og gerum ráð fyrir að
:math:`F:X\to {{\mathbb  C}}` sé fágað fall á opnu hlutmengi :math:`X`
af :math:`{{\mathbb  C}}`, þannig að :math:`Y\subset X` og
:math:`F(x)=f(x)` fyrir öll :math:`x\in Y`. Þá kallast :math:`F` :hover:`fáguð framlenging` 
eða *fáguð útvíkkun* á fallinu :math:`f`.

Veldaröð veldisvísisfallsins
----------------------------

Við skilgreindum veldisvísisfallið með formúlunni

.. math:: \exp z=e^x(\cos y+i\sin y), \qquad z=x+iy \in {{\mathbb  C}}.

Við hefðum eins getað notað veldaraðarframsetninguna á
:math:`x\mapsto e^x` til þess að skilgreina fágaða framlengingu
veldisvísisfallsins.

Við skulum nú kanna nokkra eiginleika veldisvísisfallsins út frá
veldaröðinni. Með því að deilda röðina lið fyrir lið fáum við

.. math:: \exp{{^{\prime}}}z=\exp z, \qquad \text{eða} \qquad \dfrac d{dz}e^z=e^z.

Undirstöðueiginleiki veldisvísisfallsins er
*samlagningarformúla þess*

.. math:: e^{z+w}=e^ze^w, \qquad z,w\in {{\mathbb  C}}.

Hún leiðir af :hover:`tvíliðureglunni,tvíliðuregla`,

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

Á rauntalnaásnum er veldisvísisfallið :math:`x\mapsto e^x` stranglega
vaxandi því afleiða þess er :math:`e^x` og hún er jákvæð. Við höfum líka
:math:`e^x\to+\infty` ef :math:`x\to \infty`, því sérhver liður í
veldaröðinni með númer :math:`n\geq 1` er stranglega vaxandi og stefnir
á óendanlegt. Af þessu leiðir síðan að :math:`e^{x}=1/e^{-x}\to 0` ef
:math:`x\to -\infty`. Milligildissetningin segir okkur nú að
veldisvísisfallið tekur öll jákvæð gildi á rauntalnaásnum.

Snúum okkur þá að gildunum á þverásnum :math:`\{ix\in {{\mathbb  C}};  x\in {{\mathbb  R}}\}`. Reglurnar um reikning með samoka tvinntölum
gefa okkur

.. math:: \overline{e^z}=e^{\overline z},\qquad z\in {{\mathbb  C}},

og síðan

.. math:: |e^z|^2=e^z\overline{e^{z}}=e^ze^{\overline z}=e^{x+iy}e^{x-iy}=e^{2x}

Þar með er

.. math:: |e^z|=e^{{{\operatorname{Re\, }}}z}, \qquad z\in {{\mathbb  C}},

og sérstaklega gildir

.. math:: |e^{iy}|=1, \qquad y\in {{\mathbb  R}}.

Af þessu leiðir að veldisvísisfallið hefur enga
:hover:`núllstöð` :math:`e^z=e^xe^{iy}` og
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
jöfnunum og fáum *jöfnur Eulers*

.. math::

  \cos z =\frac 12(e^{iz}+e^{-iz}), \qquad
   \sin z =\frac 1{2i}(e^{iz}-e^{-iz}).

Afleiðurnar af :math:`\cos` og :math:`\sin` getum við annað hvort
reiknað með því að deilda veldaraðirnar eða með því að deilda jöfnur
Eulers,

.. math:: \cos{{^{\prime}}}z=-\sin z, \qquad \sin{{^{\prime}}}z=\cos z, \qquad z\in {{\mathbb  C}}.

Lograr, rætur og horn
---------------------

Lograr, rætur og horn
~~~~~~~~~~~~~~~~~~~~~

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
fall :math:`\lambda:X\to {{\mathbb  C}}` kallast :hover:`logri` *á* :math:`X` ef

.. math::

  e^{\lambda(z)}=z, \qquad z\in X.

Samfellt fall :math:`\varrho:X\to {{\mathbb  C}}` kallast :math:`n` *–ta
rót* á :math:`X` ef

.. math::

  \big(\varrho(z)\big)^n=z, \qquad z\in X.

Samfellt fall :math:`\theta:X\to {{\mathbb  R}}` kallast *horn á*
:math:`X` ef

.. math::

  z=|z|e^{i\theta(z)}, \qquad z\in X.


--------------

Helstu eiginleikar logra, róta og horna eru:

Setning
^^^^^^^

\(i) Ef :math:`\lambda` er logri á :math:`X`, þá er :math:`0\not\in X`,
:math:`\lambda\in {{\cal O}}(X)` og

.. math:: \lambda{{^{\prime}}}(z)=\frac 1z, \qquad z\in X.

Föllin :math:`\lambda(z)+i2\pi k`, :math:`k\in {{\mathbb  Z}}` eru
einnig lograr á :math:`X`.

\(ii) Ef :math:`\lambda` er logri á :math:`X`, þá er

.. math::

  \lambda(z)=\ln
   |z|+i\theta(z), \qquad z\in X,

þar sem :math:`\theta:X\to {{\mathbb  R}}` er horn á :math:`X`. Öfugt,
ef :math:`\theta:X\to {{\mathbb  R}}` er horn á :math:`X`, þá er
:math:`\lambda(z)=\ln|z|+i\theta(z)` logri á :math:`X`.

\(iii) Ef :math:`\varrho` er :math:`n`–ta rót á :math:`X` þá er
:math:`\varrho\in {{\cal O}}(X)` og

.. math:: \varrho{{^{\prime}}}(z)=\frac {\varrho(z)}{nz}, \qquad z\in X.

\(iv) Ef :math:`\lambda` er logri á :math:`X`, þá er
:math:`\varrho(z)=e^{\lambda(z)/n}` :math:`n`–ta rót á :math:`X`.

--------------

Fyrir sérhverja tvinntölu :math:`{\alpha}` skilgreinum við fágað
*veldisfall með veldisvísi* :math:`\alpha` með

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
grunntölu* :math:`\alpha` sem fágaða fallið á :math:`{{\mathbb  C}}`,
sem gefið er með

.. math:: \alpha^z=e^{z\lambda(\alpha)}.

Athugið að skilgreiningin er háð valinu á logranum. Keðjureglan gefur

.. math::

  \dfrac d{dz}\alpha^z=
   \dfrac d{dz}e^{z\lambda(\alpha)}=e^{z\lambda(\alpha)}\cdot
   \lambda(\alpha)=\alpha^z\lambda(\alpha).

--------------

Lítum nú á mengið
:math:`X={{\mathbb  C}}\setminus {{\mathbb  R}}_-`, sem fæst með því að
skera neikvæða raunásinn og :math:`0` út úr tvinntalnaplaninu. 
Við skilgreinum síðan pólhnit í :math:`X` eins og myndin sýnir og veljum
hornið :math:`\theta(z)` þannig að :math:`-\pi<\theta(z)<\pi`,
:math:`z\in X`. 

.. figure:: ./myndir/fig032.svg
   :align: center
   :alt: Mynd: Höfuðgrein hornsins

   Mynd: Höfuðgrein hornsins

Fallið

.. math::

  {{\operatorname{Arg}}}:{{\mathbb  C}}\setminus {{\mathbb  R}}_-\to {{\mathbb  R}}, \qquad
   {{\operatorname{Arg}}}z=\theta(z),\quad z\in X

er kallað *höfuðgrein hornsins* og við
reiknuðum út formúlu fyrir því í kafla 1,

.. math:: {{\operatorname{Arg}}}\, z=2\arctan\bigg(\dfrac y{|z|+x}\bigg), \qquad z=x+iy\in X.

Fallið

.. math::

  {{\operatorname{Log}}}:{{\mathbb  C}}\setminus {{\mathbb  R}}_-\to {{\mathbb  C}}, \qquad
   {{\operatorname{Log}}}z=\ln |z| +i{{\operatorname{Arg}}}(z),\quad z\in X,

er kallað *höfuðgrein lografallsins*.
Fallið

.. math:: z^\alpha = e^{\alpha{{\operatorname{Log}}}z}, \qquad z\in {{\mathbb  C}}\setminus {{\mathbb  R}}_-,

kallast *höfuðgrein veldisfallsins með veldisvísi* 
:math:`\alpha`. Tvö síðastnefndu föllin eru fágaðar
framlengingar á föllunum :math:`\ln x` og :math:`x^\alpha` frá jákvæða
raunásnum yfir í opna mengið
:math:`{{\mathbb  C}}\setminus {{\mathbb  R}}_-` í tvinntalnaplaninu.
