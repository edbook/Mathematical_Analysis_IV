VELDARAÐALAUSNIR Á AFLEIÐUJÖFNUM
================================

Raunfáguð föll
--------------

Raunfáguð föll og fágaðar útvíkkanir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Fall :math:`f:X\to {{\mathbb  C}}` skilgreint á opnu mengi :math:`X` á
raunásnum, er sagt vera :hover:`raunfágað,raunfágaður` á :math:`X` ef
hægt er að skrifa :math:`X` sem sammengi af opnum bilum
:math:`]a-\varrho,a+\varrho[` og fyrir sérhvert þessara bila er til
samleitin veldaröð :math:`\sum_{n=0}^\infty c_nx^n` þannig að

.. math::

  f(x)= \sum\limits_{n=0}^\infty c_n(x-a)^n, \qquad x\in
   ]a-\varrho,a+\varrho[.


  

--------------

Ef :math:`f` er fall sem sett fram með veldaröð á bilinu
:math:`]a-\varrho,a+\varrho[`, þá framlengist :math:`f` sjálfkrafa í
fágað fall á skífunni opnu :math:`S(a,\varrho)` og gildi þess eru gefin
með

.. math::

  f(z)=\sum\limits_{n=0}^\infty c_n(z-a)^ n, \qquad z\in
   S(a,\varrho).

Af þessu leiðir að um sérhvert raunfágað fall :math:`f` á opnu mengi
:math:`X` í :math:`{{\mathbb  R}}` gildir að til er fágað fall :math:`F`
á opnu mengi :math:`Y` í :math:`{{\mathbb  C}}` sem inniheldur :math:`X`
þannig að :math:`F(x)=f(x)` fyrir öll :math:`x\in X`. Fallið :math:`F`
er þá nefnt *fáguð útvíkkun* eða :hover:`fáguð framlenging` 
af :math:`f` yfir á :math:`Y`. 

Ef :math:`Y` er svæði og :math:`F_1` 
og :math:`F_2` eru tvær fágaðar útvíkkanir af :math:`f` 
yfir á :math:`Y`, þá gefur samsemdarsetningin að :math:`F_1=F_2`. 
Þetta segir okkur að fágaðar útvíkkanir yfir á svæði séu ótvírætt ákvarðaðar og því notum við bókstafinn :math:`f` líka fyrir útvíkkunina.

Ef fallið :math:`f` er raunfágað á menginu :math:`X` og :math:`f` er
gefið með veldaröðinni hér að framan á bilinu
:math:`I=]a-{\varrho},a+{\varrho}[`, þá er :math:`f\in C^{\infty}(I)` og afleiður :math:`f` eru reiknaðar með því að deilda
röðina lið fyrir lið,

.. math::

  f{{^{\prime}}}(x)= \sum\limits_{n=1}^\infty nc_n(x-a)^{n-1}
   = \sum\limits_{n=0}^\infty (n+1)c_{n+1}(x-a)^n.

Athugið að í seinni summunni hliðruðum við til númeringu liðanna með
því að setja :math:`k=n-1` í stað :math:`n`. Þá svarar :math:`n=1` til
:math:`k=0` og :math:`n` svarar til :math:`k+1`. Þetta þurfum við oft að
gera í útreikningum í þessu kafla. Hærri afleiður eru nú reiknaðar á
sama hátt

.. math::

  \begin{aligned}
   f{{^{\prime\prime}}}(x)&= \sum\limits_{n=2}^\infty n(n-1)c_n(x-a)^{n-2}
   = \sum\limits_{n=0}^\infty (n+1)(n+2)c_{n+2}(x-a)^n,\\
   f^{(k)}(x)&= \sum\limits_{n=k}^\infty n(n-1)\cdots (n-k+1)c_n(x-a)^{n-k}\\
   &= \sum\limits_{n=0}^\infty (n+1)(n+2)\cdots(n+k)c_{n+k}(x-a)^n.\end{aligned}

Út frá þessu sést að veldaröðin er Taylor-röð 
fallsins :math:`f` í punktinum :math:`a`

.. math::

  f(x)=\sum\limits_{n=0}^\infty \dfrac{f^{(n)}(a)}{n!}(x-a)^{n}.


  

Við þekkjum ótal dæmi um raunfáguð föll sem gefin eru með Taylor-röðum
og við fengumst við fágaðar útvíkkanir þeirra í kafla 2,

.. math::

  \begin{aligned}
   e^x&=\sum\limits_{n=0}^\infty\dfrac 1{n!}{x^n}
   =1+x+\dfrac {x^2}{2!}+\dfrac{x^3}{3!}+\cdots,\\
   \cos x&= \sum\limits_{n=0}^\infty \dfrac{(-1)^n}{(2n)!}x^{2n}
   =1-\dfrac{x^2}{2!}+\dfrac{x^4}{4!}-\cdots,\\
   \sin x &=\sum\limits_{n=0}^\infty\dfrac{(-1)^n}{(2n+1)!}x^{2n+1}
   = x-\dfrac {x^3}{3!}+\dfrac{x^5}{5!}-\cdots,\\
   \cosh x&=\sum\limits_{n=0}^\infty\dfrac{1}{(2n)!}x^{2n}
   =1+\dfrac{x^2}{2!}+\dfrac{x^4}{4!}+\cdots,\\
   \sinh x &=\sum\limits_{n=0}^\infty\dfrac{1}{(2n+1)!}x^{2n+1}
   = x+\dfrac {x^3}{3!}+\dfrac{x^5}{5!}+\cdots,\\
   \ln (1+x) &= \sum\limits_{n=1}^\infty\dfrac{(-1)^{n+1}}{n}x^n
   =x-\dfrac{x^2}{2}+\frac{x^3}3-\cdots,\\
   \dfrac 1{1-x}&=\sum\limits_{n=0}^\infty x^n
   =1+x+x^2+\cdots, \\
   (1+x)^\alpha&= 1+\alpha x+ \dfrac{\alpha(\alpha-1)}{2!}x^2 + 
   \dfrac {\alpha(\alpha-1)(\alpha-2)}{3!}x^3+\cdots.\end{aligned}

Í veldaraðarframsetningum af þessu tagi setjum við alltaf :math:`0!=1`
og :math:`x^0=1` fyrir öll :math:`x`. Fimm fyrstu raðirnar eru
samleitnar á öllu :math:`{{\mathbb  R}}` en hinar eru samleitnar á
:math:`]-1,1[`.

Aðgerðir á veldaröðum
~~~~~~~~~~~~~~~~~~~~~

Framsetning á föllum með veldaröðum er sérstaklega þægileg vegna þess að
aðgerðir á þeim eru nánast þær sömu og aðgerðir á margliðum. Gerum nú
ráð fyrir því að föllin :math:`f` og :math:`g` séu gefin með veldaröðum
á bilinu :math:`]a-{\varrho},a+{\varrho}[`,

.. math::

  f(x)=\sum\limits_{n=0}^{\infty} a_n(x-a)^n,\qquad
   g(x)=\sum\limits_{n=0}^{\infty} b_n(x-a)^n.

Þá er summa þeirra gefin með veldaröðinni

.. math::

  f(x)+g(x)=\sum\limits_{n=0}^{\infty} (a_n+b_n)(x-a)^n,

  

og margfeldið er gefið með röðinni

.. math::

  f(x)g(x)=\sum\limits_{n=0}^{\infty} c_n(x-a)^n, 
   \qquad
   c_n=a_0b_n+a_1b_{n-1}+\cdots+a_nb_0.

  

Ef :math:`g(a)=b_0\neq 0`, þá er til :math:`{\varrho}_1\leq {\varrho}`
þannig að :math:`g(x)\neq 0` fyrir öll :math:`x` á bilinu
:math:`]a-{\varrho}_1,a+{\varrho}_1[`. Kvótinn :math:`f(x)/g(x)` er þá
gefinn með veldaröð :math:`\sum\limits_{n=0}^{\infty} d_n(x-a)^n`. Til
þess að reikna út stuðlana :math:`d_n` þá notum við formúluna hér að 
framan á margfeldið

.. math::

  \sum\limits_{n=0}^{\infty} d_n(x-a)^n
   \sum\limits_{n=0}^{\infty} b_n(x-a)^n
   =\sum\limits_{n=0}^{\infty} a_n(x-a)^n.

Formúlan fyrir stuðlana í margfeldinu gefur

.. math::

  d_0b_0=a_0, \quad
   d_0b_1+d_1b_0=a_1, \quad \dots, \quad 
   d_0b_n+d_1b_{n-1}+\cdots+d_nb_0=a_n.

Við fáum því rakningarformúlu fyrir stuðlana

.. math::

   \begin{aligned}
   f(x)/g(x)&=\sum\limits_{n=0}^{\infty} d_n(x-a)^n\\
   d_0&=a_0/b_0,\\
   d_1&=(a_1-d_0b_1)/b_0,\\
   &\quad \vdots\qquad\qquad \vdots\\
   d_n&=(a_n-d_0b_n-d_1b_{n-1}-\cdots-d_{n-1}b_1)/b_0.
   \end{aligned}

Raðalausnir umhverfis venjulega punkta
--------------------------------------

Nú skulum við snúa okkur að almennum afleiðuvirkja. 

Við vitum að ef öll
stuðlaföllin :math:`a_0(x),\dots,a_{m}(x)` eru raunfáguð á bilinu
:math:`I` og :math:`a_m(x)\neq 0` fyrir öll :math:`x\in I`, þá hefur
afleiðujafnan :math:`P(x,D)u=0` :math:`m` línulega óháðar lausnir, sem
eru fágaðar á :math:`I` og unnt er að ákvarða stuðlana í
veldaraðarframsetningu þessara falla út frá stuðlunum í
veldaraðarframsetningu :math:`a_0,\dots,a_{m-1}`. 

Við ætlum nú að ganga
út frá þessari setningu og reikna út lausnir með veldaröðum.

Nokkur dæmi um veldaraðalausnir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugmyndin bakvið veldaraðalausnir á afleiðujöfnum er einföld. Við göngum
út frá þeirri lausnartilgátu að til sé lausn sem gefin er með veldaröð,

.. math:: u(x)=\sum\limits_{n=0}^{\infty} c_n(x-a)^n.

Síðan stingum við röðinni inn í jöfnuna og leiðum út formúlu fyrir
stuðlana :math:`c_n`.

Einangraðir sérstöðupunktar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við rifjum nú upp þekkt hugtök fyrir fáguð föll:

Skilgreining
^^^^^^^^^^^^

Látum :math:`f` vera raunfágað fall á opnu mengi :math:`X` í
:math:`{{\mathbb  R}}`, :math:`a\in X`, gerum ráð fyrir að punkturinn
:math:`a\in X` sé núllstöð fallsins :math:`f` og

.. math:: f(x)=\sum_{n=0}^ \infty c_n(x-a)^ n.

Þá kallast minnsta gildið á :math:`n` þannig að :math:`c_n\neq 0`
:hover:`margfeldni` eða :hover:`stig` :math:`a`.

--------------

Ef :math:`a` er núllstöð fallsins :math:`f` af stigi :math:`N` og við
setjum :math:`b_n=c_{N+n}`, þá er :math:`b_0\neq 0` og

.. math::

  f(x)=\sum_{n=N}^ \infty c_n(x-a)^ n=
   (x-a)^ N\sum_{n=N}^ \infty c_n(x-a)^ {n-N} =
   (x-a)^ N\sum_{n=0}^ \infty b_n(x-a)^ n.

Það er því greinilega jafngilt að fallið :math:`f` hafi núllstöð af
stigi :math:`N` í punktinum :math:`a` og að hægt sé að skrifa :math:`f`
í grennd um :math:`a` með formúlu af gerðinni

.. math:: f(x)=(x-a)^ N\sum_{n=0}^ \infty b_n(x-a)^ n,

þar sem :math:`b_0\neq 0`.

Skilgreining
^^^^^^^^^^^^

Látum :math:`f` vera raunfágað fall á opnu mengi :math:`X` í
:math:`{{\mathbb  R}}`, gerum ráð fyrir að :math:`a\not\in X` og að
:math:`\{x; 0<|x-a|<r\}\subset X` fyrir eitthvert :math:`r>0`. 

Þá kallast punkturinn :math:`a` 
:hover:`einangraður sérstöðupunktur` raunfágaða fallsins :math:`f`. Við
segjum að einangraður sérstöðupunktur sé 
:hover:`afmáanlegur sérstöðupunktur` ef til er :math:`\varrho>0`, þannig að :math:`\{x; 0<|x-a|<{\varrho}\}\subset X` og raunfágað 
fall :math:`g` á :math:`\{x; |x-a|<{\varrho}\}` þannig að 
:math:`f(x)=g(x)` ef :math:`0<|x-a|<{\varrho}`.

--------------

Skilgreiningin segir að :math:`a` sé afmáanlegur sérstöðupunktur
raunfágaða fallsins :math:`f` þá og því aðeins að hægt sé að bæta
punktinum :math:`a` við skilgreiningarsvæði :math:`f` þannig að
:math:`f` verði raunfágað á :math:`X\cup {{\{a\}}}`.

Venjulegir punktar
~~~~~~~~~~~~~~~~~~

Nú skulum við líta á jöfnuna

.. math::

  a_2(x)u{{^{\prime\prime}}}+a_1(x)u{{^{\prime}}}+a_0(x)u=0,

  

þar sem föllin :math:`a_0`, :math:`a_1` og :math:`a_2` eru raunfáguð á
bili :math:`I` á :math:`{{\mathbb  R}}`. Það þýðir að fyrir sérhvern
punkt :math:`a\in I` má skrifa föllin með veldaröðum í :math:`(x-a)`,
sem eru samleitnar í grennd um punktinn :math:`a`,

.. math:: a_j(x)=\sum_{n=0}^ \infty a_{jn}(x-a)^ n, \qquad j=0,1,2.

Við skilgreinum nú

.. math::

  P(x)=\dfrac{a_1(x)}{a_2(x)}, \qquad 
   Q(x)=\dfrac{a_0(x)}{a_2(x)}.

  

Þessi föll eru greinilega vel skilgreind í sérhverjum punkti þar sem
:math:`a_2(x)\neq 0`, en í núllstöðvunum þurfa þau ekki að vera
skilgreind. Þar sem föllin :math:`P` og :math:`Q` eru skilgreind fáum
við jafngilda afleiðujöfnu

.. math::

  u{{^{\prime\prime}}}+P(x)u{{^{\prime}}}+Q(x)u=0,

  

Skilgreining
^^^^^^^^^^^^

Við segjum að punkturinn :math:`a\in I` sé 
:hover:`venjulegur punktur` 
annars stigs afleiðujöfnu, ef :math:`a_2(a)\neq 0` eða :math:`a_2(a)=0`
og :math:`a` er afmáanlegur sérstöðupunktur fallanna :math:`P` og
:math:`Q`. Ef :math:`a` er ekki venjulegur punktur, þá kallast :math:`a`
*sérstöðupunktur* jöfnunnar.

--------------

Lítum nú á afleiðujöfnuna, umritum hana eins og hér að framan og gerum
ráð fyrir að stuðlarnir :math:`P(x)` og :math:`Q(x)` hafi
veldaraðaframsetningu

.. math::

  P(x)=\dfrac{a_1(x)}{a_2(x)}= \sum_{n=0}^ \infty P_n(x-a)^ n,
   \qquad
   Q(x)=\dfrac{a_0(x)}{a_2(x)}= \sum_{n=0}^ \infty Q_n(x-a)^ n,

  

Við göngum út frá þeirri lausnartilgátu að :math:`u` sé gefið með
veldaröð umhverfis punktinn :math:`a`,

.. math::

  u(x)=\sum\limits_{n=0}^\infty c_n(x-a)^ n, \ 
   u'(x)=\sum\limits_{n=0}^\infty (n+1)c_{n+1}(x-a)^ n, \ 
   u{{^{\prime\prime}}}(x)=\sum\limits_{n=0}^\infty (n+2)(n+1)c_{n+2}(x-a)^ n.

Ef við stingum þessum röðum inn í afleiðujöfnuna, þá fáum við

.. math::

  0= \sum_{n=0}^ \infty (n+2)(n+1)c_{n+2}(x-a)^ n +
   P(x)\sum_{n=0}^ \infty (n+1)c_{n+1}(x-a)^ n +
   Q(x)\sum_{n=0}^ \infty c_n(x-a)^ n.

Með því að margfalda saman raðirnar fyrir :math:`P` og
:math:`u{{^{\prime}}}` annars vegar og :math:`Q` og :math:`u` hins
vegar þá fáum við

.. math::

  \begin{gathered}
   P(x)\sum_{n=0}^ \infty (n+1)c_{n+1}(x-a)^ n=
   \sum_{n=0}^\infty  
   \bigg(\sum_{k=0}^ n (k+1)P_{n-k}c_{k+1}\bigg)(x-a)^ n,\\
   Q(x)\sum_{n=0}^ \infty c_n(x-a)^ n=
    \sum_{n=0}^\infty  
   \bigg( \sum_{k=0}^ n  Q_{n-k}c_k\bigg) (x-a)^ n,\end{gathered}

svo afleiðujafnan verður

.. math::

  0= \sum_{n=0}^ \infty 
   \bigg((n+2)(n+1)c_{n+2} +
   \sum_{k=0}^{n} \big((k+1)P_{n-k}c_{k+1}+
   Q_{n-k} c_k\big)\bigg)(x-a)^ n.

Val okkar á :math:`c_0` og :math:`c_1` er frjálst og við fáum
rakningarformúluna

.. math::

  c_{n+2} = \dfrac{-1}{(n+2)(n+1)}
  \sum_{k=0}^ n \big[(k+1)P_{n-k}c_{k+1} +  Q_{n-k}c_k\big],

fyrir :math:`n=0,1,2,\dots`.

Setning
^^^^^^^

Gerum ráð fyrir að :math:`a` sé venjulegur punktur afleiðujöfnunnar

.. math::

  a_2(x)u{{^{\prime\prime}}}+a_1(x)u{{^{\prime}}}+a_0(x)u=0,


  

og látum föllin :math:`P(x)=a_1(x)/a_2(x)` og
:math:`Q(x)=a_0(x)/a_2(x)` vera gefin með veldaröðunum
:math:`P(x)=\sum_{n=0}^ \infty P_n(x-a)^ n` og
:math:`Q(x)= \sum_{n=0}^ \infty Q_n(x-a)^ n`. Þá eru sérhver lausn
:math:`u` á afleiðujöfnunni gefin með veldaröð

.. math:: u(x)=\sum_{n=0}^ \infty c_n(x-a)^ n

þar sem stuðlarnir :math:`c_n` uppfylla rakningarformúluna.
Samleitnigeislinn er að minnsta kosti jafn stór og minni samleitnigeisli
raðanna tveggja.

--------------

Útreikningar okkar hér að framan byggðu á þeirri lausnartilgátu að
:math:`u` væri raunfágað.

Sýnidæmi
^^^^^^^^

(*Jafna Legendre*).  
Gerum ráð fyrir að jafnan

.. math::

  \dfrac {d}{dx}((1-x^ 2)\dfrac{du}{dx})+\lambda u=
   (1-x^ 2)u{{^{\prime\prime}}}-2xu{{^{\prime}}}+\lambda u=0

hafi veldaraðalausn umhverfis punktinn :math:`a=0`,

.. math::

  \begin{gathered}
   u(x)=\sum\limits_{n=0}^\infty c_nx^ n, \quad
   u{{^{\prime}}}(x)=\sum\limits_{n=1}^\infty nc_nx^{n-1}, \quad 
   xu{{^{\prime}}}(x)=\sum\limits_{n=0}^\infty nc_nx^ n, \quad
   \\
   u{{^{\prime\prime}}}(x)
   =\sum\limits_{n=2}^\infty n(n-1)c_nx^ {n-2}=
   \sum\limits_{n=0}^\infty (n+2)(n+1)c_{n+2}x^ n,\\
   x^ 2u{{^{\prime\prime}}}(x)=\sum\limits_{n=0}^\infty n(n-1)c_nx^ n.\end{gathered}

Við stingum síðan þessum röðum inn í afleiðujöfnuna og fáum

.. math::

  \begin{aligned}
   0&=
   \sum\limits_{n=0}^\infty (n+2)(n+1)c_{n+2}x^ n -
   \sum\limits_{n=0}^\infty n(n-1)c_nx^ n\\
   &-2\sum\limits_{n=0}^\infty nc_nx^ n+
   \lambda\sum\limits_{n=0}^\infty c_nx^ n
   \\
   &=\sum\limits_{n=0}^\infty
   ((n+2)(n+1)c_{n+2} +(\lambda-n(n-1)-2n)c_n)x^ n.\end{aligned}

Stuðlarnir verða því að uppfylla

.. math:: c_{n+2}=- \dfrac{\lambda-(n+1)n}{(n+2)(n+1)}c_n.

Valið á fyrstu tveimur stuðlunum er frjálst og við fáum

.. math::

  \begin{gathered}
   c_2= -\dfrac{\lambda}{2\cdot 1}c_0, \quad
   c_4= \dfrac{(\lambda-3\cdot 2)\lambda}{4\cdot 3\cdot 2\cdot
   1}c_0,\quad \dots, \\
   c_{2k}=(-1)^
   k\dfrac{(\lambda-(2k-1)(2k-2))(\lambda-(2k-3)(2k-4))\cdots
   (\lambda-3\cdot 2)\lambda}{(2k)!}c_0\\
   c_3=- \dfrac{\lambda-2\cdot 1}{3\cdot 2}c_1, \quad
   c_5= \dfrac{(\lambda-4\cdot 3)(\lambda-2\cdot 1)}{5\cdot 4\cdot 3\cdot 2}
   c_1,\quad \dots,\\
   c_{2k+1}=(-1)^
   k\dfrac{(\lambda-2k(2k-1))(\lambda-(2k-2)(2k-3))\cdots
   (\lambda-2\cdot 1)}{(2k+1)!}c_1.\end{gathered}

Ef við skrifum :math:`\lambda=\alpha(\alpha+1)` og notfærum okkur að

.. math:: \alpha(\alpha+1)-n(n+1)=(\alpha-n)(\alpha+n+1),

þá verður rakningarformúlan fyrir röðina

.. math:: c_{n+2}= -\dfrac{(\alpha-n)(\alpha+n+1)}{(n+2)(n+1)}c_n

og almenn lausn jöfnunnar verður því

.. math::

  \begin{gathered}
   u(x) = c_0\sum\limits_{k=0}^\infty
   a_{2k}
   x^{2k}
   +
   c_1\sum\limits_{k=0}^\infty
   a_{2k+1}
   x^ {2k+1},\\
   a_0=a_1=1,\\
   \\
   a_{2k}= (-1)^ k 
   \dfrac{\alpha(\alpha-2)\cdots(\alpha-2k+2)
   (\alpha+1)(\alpha+3)\cdots(\alpha+2k-1)}{(2k)!},\\
   a_{2k+1}= (-1)^ k 
   \dfrac{(\alpha-1)(\alpha-3)\cdots(\alpha-2k+1)
   (\alpha+2)(\alpha+4)\cdots(\alpha+2k)}{(2k+1)!}.\end{gathered}

Nú tökum við eftir því að ef :math:`\alpha` er jöfn heiltala þá eru
allir liðir í fyrri summunni með númer :math:`2k\geq \alpha+2` jafnir
núll og fyrri summan er því margliða af stigi :math:`\alpha`. Ef hins
vegar :math:`\alpha` er oddatala þá er seinni veldaröðin margliða. 

Við fáum því að fyrir sérhvert :math:`n` er til margliðulausn á jöfnu
Legendre, ef :math:`\lambda` er valið sem :math:`\lambda=n(n+1)`. Venja
er að skilgreina Legendre–margliðurnar sem þessar lausnir eftir að hafa valið ákveðin gildi á stuðlunum :math:`c_0` og :math:`c_1`.

Legendre–margliðurnar koma fyrir í ýmsum útreikningum, meðal annars í
rafsegulfræði. Við höfum ekki tök á því að gera þeim nein skil hér.

--------------

Sýnidæmi
^^^^^^^^

(*Jafna Hermite*).   Við
lítum nú á afleiðujöfnuna
:math:`u{{^{\prime\prime}}}-2xu{{^{\prime}}}+\lambda u=0` og leysum
hana með því að gera ráð fyrir að lausnin sé gefin með veldaröð. Við
notum formúlurnar fyrir :math:`u{{^{\prime\prime}}}` og
:math:`xu{{^{\prime}}}` úr sýnidæminu hér að framan. Til einföldunar
setjum við :math:`\lambda=2\alpha`. Það gefur okkur

.. math::

  \begin{aligned}
   0&=
   \sum\limits_{n=0}^\infty (n+2)(n+1)c_{n+2}x^ n
   -2\sum\limits_{n=0}^\infty nc_nx^ n+
   2\alpha\sum\limits_{n=0}^\infty c_nx^ n=
   \\
   &=\sum\limits_{n=0}^\infty
   ((n+2)(n+1)c_{n+2} +2(\alpha-n)c_n)x^ n.\end{aligned}

Stuðlarnir verða því að uppfylla

.. math:: c_{n+2}=- \dfrac{2(\alpha-n)}{(n+2)(n+1)}c_n.

Við fáum nú formúlu fyrir lausnina

.. math::

  u(x) = c_0\sum\limits_{k=0}^\infty
   a_{2k}
   x^{2k}
   +
   c_1\sum\limits_{k=0}^\infty
   a_{2k+1}
   x^ {2k+1},

þar sem stuðlarnir :math:`a_k` eru gefnir með formúlunum

.. math::

  \begin{gathered}
   a_0=a_1=1,\\
   a_2=-2\dfrac{\alpha}{2\cdot 1}, \qquad
   a_4=4\dfrac{(\alpha-2)\alpha}{4\cdot 3\cdot 2\cdot 1},  \quad\dots,
   \\
   a_{2k}=(-1)^ k 2^ k \dfrac{(\alpha-2k+2)\cdots(\alpha-2)\alpha}{(2k)!},\\
   a_3=-2\dfrac{(\alpha-1)}{3\cdot 2}, \qquad
   a_5=4\dfrac{(\alpha-3)(\alpha-1)}{5\cdot 4\cdot 3\cdot 2},  \quad\dots,\\
   a_{2k+1}= (-1)^ k 2^ k
   \dfrac{(\alpha-2k+1)\cdots(\alpha-3)(\alpha-1)}{(2k+1)!}.\end{gathered}

Við sjáum nú að ef :math:`\alpha` er heiltala :math:`>0` þá fæst lausn
sem er margliða. Fyrir ákveðið val á :math:`c_0` og :math:`c_1` fæst
runa af margliðum, en þær nefnast *Hermite–margliður*.

:math:`\Gamma`–fallið
---------------------

Þegar rakningarformúlur eru notaðar til að finna beinar formúlur fyrir
stuðlana í raðalausnum afleiðujafna koma endurtekin margfeldi oft fyrir.
Þá er þægilegt að grípa til :math:`\Gamma`–fallsins, en það er
skilgreint með formúlunni

.. math::

  \Gamma(z)=\int_0^\infty e^{-t}t^{z-1}\, dt, \qquad z\in {{\mathbb  C}}, \quad {{\operatorname{Re\, }}}z>0.


  

Greinilegt er að fyrir þessi gildi á :math:`z` er heildið alsamleitið.
Athugum nú að hlutheildunin

.. math::

  \int_0^\infty e^{-t}t^{z}\, dt =\left[ -e^{-t}t^z\right]_0^\infty +
   \int_0^\infty e^{-t}zt^{z-1}\, dt= z\int_0^\infty e^{-t}t^{z-1}\, dt

gefur okkur formúluna

.. math::

  \Gamma(z+1)=z\Gamma(z),


  

og með þrepun fáum við síðan

.. math::

  \Gamma(z+n)= z(z+1)\cdots(z+n-1)\Gamma(z), 
   \qquad n=1,2,3,\dots.


  

Þessa formúlu getum við síðan notað til að framlengja
skilgreiningarsvæði :math:`\Gamma` yfir á mengið

.. math:: {{\mathbb  C}}\setminus\{0,-1, -2, -3,\dots\}.

Við veljum :math:`n` það stórt að :math:`{{\operatorname{Re\, }}}z+n>0`
og notum

.. math::

  \Gamma(z)=\dfrac{\Gamma(z+n)}{z(z+1)\cdots(z+n-1)},


  

til að skilgreina :math:`{\Gamma}(z)` fyrir :math:`z` með
:math:`{{\operatorname{Re\, }}}z\leq 0`.

Við getum auðveldlega reiknað út :math:`\Gamma(1)`, því

.. math:: \Gamma(1)=\int_0^\infty e^{-t}\, dt=\left[-e^{-t}\right]_0^\infty=1,

en formúlan hér að framan gefur okkur síðan

.. math::

  \Gamma(n)=(n-1)!

  

Niðurstaðan er því sú að :math:`{\Gamma}` er framlenging á fallinu
:math:`n\mapsto (n-1)!` frá mengi náttúrlegra talna
:math:`\{1,2,3,\dots\}` yfir á mengið
:math:`{{\mathbb  C}}\setminus\{0,-1, -2, -3,\dots\}`.

Við getum líka reiknað út :math:`\Gamma(1/2)`, en það er gert með því að
skipta fyrst um breytistærð í heildinu

.. math::

  \Gamma(1/2)=\int_0^\infty e^{-t}t^{-1/2}\, dt =
   2\int_0^\infty e^{-x^2}\, dx= \int_{-\infty}^\infty e^{-x^2}\, dx.

Síðan athugum við að :math:`\Gamma(1/2)^2` má skrifa sem tvöfalt heildi

.. math::

  \Gamma(1/2)^2= 
   \int_{-\infty}^\infty e^{-x^2}\, dx\int_{-\infty}^\infty e^{-y^2}\,dy=
   \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-(x^2+y^2)}\, dxdy.

Næsta skref er að skipta yfir í pólhnit

.. math::

  \Gamma(1/2)^2=\int_0^\infty\int_0^{2\pi}e^{-r^2} \, rdrd\theta =
   \pi \int_0^\infty e^{-r^2} \, 2rdr= \pi\left[-e^{-r^2}\right]_0^\infty=\pi.

Við höfum því

.. math::

  \Gamma(1/2)=\sqrt\pi, \qquad \Gamma(-1/2)=-2\sqrt\pi,

og í framhaldi af því

.. math::

  \Gamma(n+1/2) =\frac 12\frac 32\cdots (n-\frac 12)\sqrt \pi=
   \dfrac{(2n-1)!}{2^{2n-1}(n-1)!}\sqrt \pi.

.. figure:: ./myndir/fig038.svg
    :align: center
    :alt: Gamma–fallið.

    Mynd: Gamma–fallið.

Aðferð Frobeniusar
------------------

Reglulegir sérstöðupunktar
~~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessari grein ætlum við að líta á raðalausnir á jöfnunni

.. math::

  a_2(x)u{{^{\prime\prime}}}+a_1(x)u{{^{\prime}}}+a_0(x) u=0


  

í grennd um sérstöðupunkta. Ef :math:`a` er sérstöðupunktur, þá kemur í
ljós að ekki er alltaf hægt að skrifa lausnirnar sem veldaraðir. Hins
vegar er stundum hægt að skrifa þær sem margfeldi af veldaröð og
veldisfalli

.. math::

  u(x)= |x-a|^ r\sum_{n=0}^ \infty c_n(x-a)^ n.


  

Aðferð Frobeniusar gengur út á að leita að lausn af þessari gerð og
ákvarða bæði veldið :math:`r` og stuðlana :math:`c_n` út frá veldaröðum
stuðlafallanna í afleiðujöfnunni.

Skilgreining
^^^^^^^^^^^^

Látum :math:`f` vera raunfágað fall á opnu mengi :math:`X` í
:math:`{{\mathbb  R}}`. Við segjum að einangraður sérstöðupunktur
:math:`a` raunfágaða fallsins :math:`f` sé :hover:`skaut`
af stigi* :math:`m>0`, ef til er
:math:`\varrho>0` og raunfágað fall :math:`g` á
:math:`\{x; |x-a|<\varrho\}`, þannig að
:math:`\{x; 0<|x-a|<{\varrho}\}\subset X`, :math:`g(a)\neq 0` og

.. math:: f(x)=\dfrac {g(x)}{(x-a)^m}\qquad 0<|x-a|<\varrho.

--------------

Látum :math:`a` vera sérstöðupunkt fyrir afleiðujöfnuna og
skrifum

.. math::

  P(x)=\dfrac{a_1(x)}{a_2(x)}=\dfrac{p(x)}{x-a}, \qquad
   Q(x)=\dfrac{a_0(x)}{a_2(x)}=\dfrac{q(x)}{(x-a)^2}.

  

Skilgreining
^^^^^^^^^^^^

Við segjum að :math:`a` sé 
:hover:`reglulegur sérstöðupunktur` 
afleiðujöfnunnar, ef :math:`a` er sérstöðupunktur
jöfnunnar, fallið :math:`P` hefur annað hvort afmáanlegan sérstöðupunkt
í :math:`a` eða skaut af stigi :math:`\leq 1` og :math:`Q` hefur annað
hvort afmáanlegan sérstöðupunkt í :math:`a` eða skaut af stigi
:math:`\leq 2`.

--------------

Punkturinn :math:`a` er reglulegur sérstöðupunktur afleiðujöfnunnar þá
og því aðeins að föllin :math:`p` og :math:`q`, sem skilgreind eru hér
fyrir ofan, séu bæði fáguð í grennd um :math:`a`.

Útfærsla á aðferð Forbeniusar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við gera ráð fyrir að við höfum afleiðujöfnu með reglulegan
sérstöðupunkt :math:`a` og að við umritum hana yfir á formið

.. math:: (x-a)^2u{{^{\prime\prime}}}+(x-a)p(x)u{{^{\prime}}}+q(x)u=0,

þar sem föllin :math:`p` og :math:`q` eru sett fram með veldaröðum

.. math::

  p(x)= \sum_{n=0}^\infty p_n(x-a)^n, \quad
   q(x)= \sum_{n=0}^\infty q_n(x-a)^n.

Við gerum ráð fyrir því að unnt sé að skrifa lausnina sem



.. math::

  u(x)= (x-a)^r\sum_{n=0}^\infty a_n(x-a)^n=
   \sum_{n=0}^\infty a_n(x-a)^{n+r}, \qquad a<x<a+\varrho.

Við stingum röðinni inn í jöfnuna og fáum

.. math::

  \begin{gathered}
   \sum_{n=0}^\infty (n+r)(n+r-1)a_n(x-a)^{n+r} +
   p(x)\sum_{n=0}^\infty (n+r)a_n(x-a)^{n+r} \\
   + q(x)\sum_{n=0}^\infty a_n(x-a)^{n+r} = 0.\end{gathered}

Við stingum nú röðunum fyrir :math:`p` og :math:`q` inn í jöfnuna og
margföldum síðan raðirnar saman

.. math::

  \begin{gathered}
   p(x)\sum_{n=0}^\infty (n+r)a_n(x-a)^{n+r}= \sum_{n=0}^\infty
   \sum_{k=0}^n(k+r)p_{n-k}a_{k} (x-a)^{n+r},\\
   q(x)\sum_{n=0}^\infty a_n(x-a)^{n+r}= \sum_{n=0}^\infty
   \sum_{k=0}^n q_{n-k}a_{k} (x-a)^{n+r}.\end{gathered}

Til þess að jafnan gildi, þá þurfa stuðlarnir við öll veldin í
liðuninni að vera núll, en það jafngildir

.. math::

  (n+r)(n+r-1)a_n+\sum_{k=0}^n\big((k+r)p_{n-k}+q_{n-k}\big)a_k=0,
   \qquad n=0,1,2,\dots.


  

Athugum nú sérstaklega tilfellið :math:`n=0`, en það er jafnan

.. math:: (r(r-1)+p_0r+q_0)a_0=0.

Til þess að við getum valið stuðulinn :math:`a_0` frjálst, þá þarf
talan :math:`r` að uppfylla annars stigs jöfnuna

.. math::

  r(r-1)+p_0r+q_0=r(r-1)+ p(a)r+q(a)=0.


  

Skilgreining
^^^^^^^^^^^^

Gerum ráð fyrir að :math:`a` sé reglulegur sérstöðupunktur
afleiðujöfnunnar

.. math::

  (x-a)^2u{{^{\prime\prime}}}+(x-a)p(x)u{{^{\prime}}}+q(x)u=0.

  

Þá kallast margliðan

.. math:: \varphi(\lambda)=\lambda(\lambda-1)+p(a)\lambda+q(a)

*vísamargliða afleiðujöfnunnar í punktinum* :math:`a`, jafnan
:math:`\varphi(\lambda)=0` kallast *vísajafna afleiðujöfnunnar í
punktinum* :math:`a`. Núllstöðvar hennar kallast
*vísar jöfnunnar í punktinum* :math:`a`.

--------------

Við höfum sem sagt komist að því í útreikningum okkar, að til þess að
fallið :math:`u(x)` sem gefið er með formúlunni, geti verið lausn á
afleiðujöfnunni, þá þarf talan :math:`r` að vera vísir jöfnunnar í
punktinum :math:`a`.

Lítum nú á jöfnuna aftur í tilfellinu :math:`n>0`, en hún er

.. math::

  \begin{gathered}
   (n+r)(n+r-1)a_n+\sum_{k=0}^n\big((k+r)p_{n-k}+q_{n-k}\big)a_k\\
   =\big((n+r)(n+r-1)+p_0(n+r)+q_0 \big)a_n 
   +\sum_{k=0}^{n-1}\big((k+r)p_{n-k}+q_{n-k}\big)a_k\\
   = \varphi(n+r)a_n + \sum_{k=0}^{n-1}\big((k+r)p_{n-k}+q_{n-k}\big)a_k=0.\end{gathered}

Ef :math:`r` er vísir jöfnunnar og :math:`\varphi(n+r)\neq 0` fyrir öll
:math:`n>0`, þá fáum við rakningarformúluna

.. math:: a_n=\dfrac{-1}{\varphi(r+n)}\sum_{k=0}^{n-1}\big((k+r)p_{n-k}+q_{n-k}\big)a_k.

Við erum nú komin að meginniðurstöðu kaflans:

Setning
^^^^^^^

(*Frobenius*).   Gerum ráð fyrir því að :math:`a` sé
reglulegur sérstöðupunktur afleiðujöfnunnar

.. math::

  (x-a)^2u{{^{\prime\prime}}}+ (x-a)p(x)u{{^{\prime}}}+q(x)u=0


  

og gerum ráð fyrir að föllin :math:`p` og :math:`q` séu sett fram með
veldaröðunum

.. math::

  p(x)=\sum_{n=0}^\infty p_n(x-a)^n, \qquad
   q(x)=\sum_{n=0}^\infty q_n(x-a)^n,


  

og að þær séu samleitnar ef :math:`|x-a|<\varrho`. Látum :math:`r_1` og
:math:`r_2` vera núllstöðvar vísajöfnunnar

.. math:: \varphi(\lambda)=\lambda(\lambda-1)+p(a)\lambda+q(a)=0

og gerum ráð fyrir að
:math:`{{\operatorname{Re\, }}}r_1\geq {{\operatorname{Re\, }}}r_2`. Þá
gildir:

\(i) Til er lausn :math:`u_1` á afleiðujöfnunni sem gefin er með

.. math:: u_1(x)=|x-a|^{r_1}\sum_{n=0}^\infty a_n(x-a)^n.

Röðin er samleitin fyrir öll :math:`x` sem uppfylla
:math:`0<|x-a|<\varrho`. Valið á :math:`a_0` er frjálst, en hinir
stuðlar raðarinnar fást með rakningarformúlunni

.. math::

  a_n=\dfrac{-1}{\varphi(n+r_1)}
   \sum_{k=0}^{n-1}((k+r_1)p_{n-k}+q_{n-k})a_k, \qquad n=1,2,3,\dots.

\(ii) Ef :math:`r_1-r_2\neq 0,1,2,\dots`, þá er til önnur línulega óháð
lausn :math:`u_2`, sem gefin er með

.. math:: u_2(x)=|x-a|^{r_2}\sum_{n=0}^\infty b_n(x-a)^n.

Röðin er samleitin fyrir öll :math:`x` sem uppfylla
:math:`0<|x-a|<\varrho`. Valið á :math:`b_0` er frjálst, en hinir
stuðlar raðarinnar fást með rakningarformúlunni

.. math::

  b_n=\dfrac{-1}{\varphi(n+r_2)}
   \sum_{k=0}^{n-1}((k+r_2)p_{n-k}+q_{n-k})b_k, \qquad n=1,2,3,\dots.

\(iii) Ef :math:`r_1-r_2=0`, þá er til önnur línulega óháð lausn
:math:`u_2`, sem gefin er með

.. math::

  u_2(x)=|x-a|^{r_1+1}\sum_{n=0}^\infty b_n(x-a)^n+
   u_1(x)\ln|x-a|.

Röðin er samleitin fyrir öll :math:`x` sem uppfylla
:math:`0<|x-a|<\varrho` og stuðlar raðarinnar fást með innsetningu í
jöfnuna.

\(iv) Ef :math:`r_1-r_2=N`, þar sem :math:`N` er jákvæð heiltala, þá er
til önnur línulega óháð lausn, sem gefin er með

.. math::

  u_2(x)=|x-a|^{r_2}\sum_{n=0}^\infty b_n(x-a)^n+
   \gamma u_1(x)\ln|x-a|.

Röðin er samleitin fyrir öll :math:`x` sem uppfylla
:math:`0<|x-a|<\varrho`. Stuðlar raðarinnar og :math:`\gamma` fást með
innsetningu í jöfnuna.


Bessel–jafnan
-------------

Bessel–jafnan
~~~~~~~~~~~~~

Við skulum nú taka fyrir aðferð Frobeniusar til þess að leysa
Bessel–jöfnuna

.. math::

  P(x,D)u=x^2u{{^{\prime\prime}}}+xu{{^{\prime}}}+(x^2-\alpha^2)u=0


  

í grennd um reglulega sérstöðupunktinn :math:`a=0`. Hér er
:math:`p(x)=1` og :math:`q(x)=x^2-\alpha^2`, svo vísajafnan er

.. math::

  \varphi(\lambda)=\lambda(\lambda-1)+\lambda-\alpha^2=
   \lambda^2-\alpha^2=0


  

og núllstöðvar hennar eru :math:`r_1=\alpha` og :math:`r_2=-\alpha`.
Við hugsum okkur að :math:`{{\operatorname{Re\, }}}\alpha\geq 0`.
Setning Frobeniusar segir okkur að við fáum lausn af gerðinni

.. math:: u_1(x)=|x|^\alpha\sum_{n=0}^\infty a_n x^n,

þar sem við getum valið stuðulinn :math:`a_0` frjálst og hina stuðlana
út frá rakningarformúlunni

.. math:: \varphi(\alpha+1)a_1=0, \qquad \varphi(\alpha+n)a_n=-a_{n-2}.

Þar sem :math:`\varphi(\alpha+1)\neq 0` þá verður :math:`a_1=0` og í
framhaldi af því fæst :math:`0=a_3=a_5=\cdots`. Til þess að finna
formúluna fyrir :math:`a_{2k}` þá athugum við að

.. math::

  \varphi(\alpha+2k)=(\alpha+2k)^2-\alpha^2= 4k\alpha+4k^2=
   2^2k(\alpha+k),

og þar með verður

.. math::

  \begin{gathered}
   a_2=\dfrac{-a_0}{2^2(\alpha+1)}, \quad
   a_4=\dfrac{a_0}{2^42(\alpha+1)(\alpha+2)}, \dots  \\
   a_{2k}=\dfrac{(-1)^ka_0}{2^{2k}k!(\alpha+1)\cdots(\alpha+k)}.\end{gathered}

Athugum nú að

.. math:: (\alpha+1)\cdots(\alpha+k)={\Gamma}({\alpha}+k+1)/{\Gamma}({\alpha}+1).

Það er því eðlilegt að velja

.. math:: a_0=\dfrac 1{2^\alpha\Gamma(\alpha+1)}.

Skilgreining
^^^^^^^^^^^^

Lausnin á Bessel–jöfnunni
:math:`x^2u{{^{\prime\prime}}}+xu{{^{\prime}}}+(x^2-\alpha^2)u=0`,
sem gefin er með formúlunni

.. math::

  J_\alpha(x)=\left|\dfrac x2\right|^\alpha\sum_{k=0}^\infty
   \dfrac{(-1)^k}{k!\Gamma(\alpha+k+1)}\left( \dfrac x2\right)^{2k}


  

er kölluð *fall Bessels af fyrstu gerð með vísi* :math:`\alpha`.

--------------

Nú þurfum við að finna línulega óháða lausn og skiptum í tilfelli:

Talan :math:`-{\alpha}` er vísir Bessel-jöfnunnar og með því að skipta á
:math:`{\alpha}` og :math:`-{\alpha}` í rakningarformúlunum hér að
framan, þá fáum við aðra línulega óháða lausn

.. math::

  J_{-\alpha}(x)=\left|\dfrac x2\right|^{-\alpha}\sum_{k=0}^\infty
   \dfrac{(-1)^k}{k!\Gamma(-\alpha+k+1)}\left( \dfrac x2\right)^{2k}


  

og sérhverja lausn má síðan skrifa sem línulega samantekt af
:math:`J_{\alpha}` og :math:`J_{-\alpha}`.

Bessel-jafnan í tilfellinu :math:`{\alpha}=0` er jafngild jöfnunni

.. math::

  xu{{^{\prime\prime}}}+u{{^{\prime}}}+xu=0,


  

og við erum búin að finna eina lausn á henni

.. math::

  u_1(x)=J_0(x)=\sum\limits_{k=0}^{\infty}
   \dfrac{(-1)^k}{2^{2k}(k!)^2}x^{2k}.

Samkvæmt tilfelli (iii) í setningu Frobeniusar vitum við að til er
önnur línulega óháð lausn :math:`u_2`, sem gefin er á jákvæða raunásnum
með formúlu af gerðinni

.. math::

  u_2(x)=J_0(x)\ln x+x\sum\limits_{n=0}^{\infty} b_nx^n
   =J_0(x)\ln x+\sum\limits_{m=1}^{\infty} A_mx^m.


  

Við reiknum út afleiðurnar af :math:`u_2`

.. math::

  \begin{aligned}
   u_2{{^{\prime}}}(x)&=J_0{{^{\prime}}}(x)\ln x +\dfrac{J_0(x)}x+
   \sum\limits_{m=1}^{\infty} mA_mx^{m-1},\\
   u_2{{^{\prime\prime}}}(x)&= J_0{{^{\prime\prime}}}(x)\ln x+\dfrac{2J_0{{^{\prime}}}(x)}x-\dfrac{J_0(x)}{x^2}
   +\sum\limits_{m=1}^{\infty} m(m-1)A_mx^{m-2},\end{aligned}

stingum þeim inn í afleiðujöfnuna og notfærum okkur að :math:`J_0` er
lausn. Þá fáum við

.. math::

  2J_0{{^{\prime}}}(x)+\sum\limits_{m=1}^{\infty} m(m-1)A_mx^{m-1}
   +\sum\limits_{m=1}^{\infty} mA_mx^{m-1}
   +\sum\limits_{m=1}^{\infty} A_mx^{m+1}=0.

Til þess að fá formúlu fyrir stuðlana :math:`A_m`, þá verðum við að
stinga röðinni fyrir :math:`J_0{{^{\prime}}}` inn í þessa jöfnu,

.. math::

  J_0{{^{\prime}}}(x)=\sum \limits_{k=1}^{\infty}
   \dfrac{(-1)^k2k}{2^{2k}(k!)^2}x^{2k-1}
   =\sum \limits_{k=1}^{\infty}
   \dfrac{(-1)^kx^{2k-1}}{2^{2k-1}k!(k-1)!}

og taka summurnar þrjár saman í eina. Við fáum þá jöfnuna

.. math::

  A_1x^0+4A_2x+\sum\limits_{m=2}^{\infty} 
   \big((m+1)^2A_{m+1}+A_{m-1}\big)x^m
   =\sum \limits_{k=1}^{\infty}
   \dfrac{(-1)^{k-1}x^{2k-1}}{2^{2k-2}k!(k-1)!}.

Nú eru allir stuðlarnir í hægri hliðinni við slétt veldi af :math:`x`
jafnir :math:`0` og því fáum við

.. math:: A_1=0, \qquad   (2k+1)^2A_{2k+1}+A_{2k-1}=0.

Þessar jöfnur gefa að :math:`A_m=0` ef :math:`m` er oddatala. Snúum
okkur nú að :math:`A_m` þar sem :math:`m` er slétt tala. Við höfum

.. math::

  4A_2=1, \qquad (2k)^2A_{2k}+A_{2k-2}=
   \dfrac{(-1)^{k-1}}{2^{2k-2}k!(k-1)!}.

Með þrepun fæst síðan formúlan

.. math:: A_{2k}=\dfrac{(-1)^{k-1}}{2^{2k}(k!)^2} h_k, \qquad k=1,2,3,\dots,

þar sem :math:`h_k=1+1/2+1/3+\cdots+1/k`. Við getum því skrifað
lausnina sem

.. math::

  u_2(x)= J_0(x)\ln x+
   \sum\limits_{k=1}^{\infty}
   \dfrac{(-1)^{k-1}h_k}{2^{2k}(k!)^2} x^{2k}.

Það er venja að nota annað fall en :math:`u_2` sem grunnfall:

Skilgreining
^^^^^^^^^^^^

Fallið :math:`Y_0`, sem skilgreint er með

.. math::

  Y_0(x)=\dfrac 2{\pi}\left[J_0(x)\bigg(\ln \dfrac {|x|}2+{\gamma}\bigg)
   +\sum\limits_{k=0}^{\infty}
   \dfrac{(-1)^{k-1}h_k}{2^{2k}(k!)^2} x^{2k}\right],

þar sem :math:`h_k=1+1/2+1/3+\cdots+1/k` og :math:`{\gamma}` táknar
fasta Eulers

.. math::

  \begin{aligned}
   {\gamma}&=\lim\limits_{k\to {\infty}} \big(1+1/2+\cdots+1/k-\ln k\big)
   \\
   &\approx 0.577 \,  215 \,  644 \, 90 \dots,\nonumber\end{aligned}

nefnist *fall Bessels af annarri gerð með vísi* :math:`0`.

--------------

Það er ljóst að föllin :math:`J_0` og :math:`Y_0` eru línulega óháð, svo
sérhverja lausn á Bessel-jöfnunni með vísi :math:`{\alpha}=0` er unnt að
skrifa sem línulega samantekt af þeim.

Hér er gengið út frá lausnarformúlunni í tilfelli (iv) í setningu
Frobeniusar. Lausnaraðferðin er sú sama og í tilfellinu
:math:`{\alpha}=0`, en útfærslan er töluvert snúnari og förum við ekki
út í hana hér. Niðurstaðan er alla vega sú, að til sögunnar kemur nýtt
fall:

Skilgreining
^^^^^^^^^^^^

Fallið :math:`Y_{\alpha}`, :math:`{\alpha}=1,2,3,\dots` sem skilgreint
er með

.. math::

  \begin{aligned}
   Y_{\alpha}(x)=\dfrac 2{\pi}\bigg[
   J_{\alpha}(x)\bigg(\ln \dfrac {|x|}2+{\gamma}\bigg)
   &+x^{\alpha}\sum\limits_{k=0}^{\infty}
   \dfrac{(-1)^{k-1}\big(h_k+h_{k+\alpha}\big)}
   {2^{2k+\alpha+1}k!(k+{\alpha})!} x^{2k}\\
   &-x^{-\alpha}\sum\limits_{k=0}^{\alpha-1}
   \dfrac{(\alpha-k-1)!}{2^{2k-\alpha+1}k!}x^{2k}\bigg],
   \end{aligned}

þar sem :math:`h_k=1+1/2+1/3+\cdots+1/k` og :math:`{\gamma}` táknar
fasta Eulers, nefnist *fall Bessels af annarri gerð með vísi*
:math:`{\alpha}`.

--------------

Almenn lausn á Bessel-jöfnunni með vísi :math:`{\alpha}` er línuleg
samantekt af :math:`J_{\alpha}` og :math:`Y_{\alpha}`,
:math:`{\alpha}=1,2,3,\dots`. Það er hægt að skilgreina
:math:`Y_{\alpha}` fyrir önnur gildi á :math:`{\alpha}`. Það er gert með
formúlunni

.. math::

  Y_{\alpha}(x)=\dfrac 1{\sin {\alpha}{\pi}}\left[
   J_{\alpha}(x)\cos{\alpha}{\pi} -J_{-{\alpha}}(x)
   \right], \qquad {\alpha}\in {{\mathbb  C}}, \ {{\operatorname{Re\, }}}{\alpha}\geq 0, {\alpha}\neq
   1,2,3,\dots.

Þá fæst nokkuð merkileg formúla

.. math::

  Y_{\alpha}(x)=\lim_{{\beta}\to {\alpha}} Y_{\beta}(x), \qquad 
   {\alpha}=1,2,3,\dots .

Við höldum ekki lengra inn á þessa braut og endum kaflann með gröfum
fallanna :math:`J_0`, :math:`Y_0`, :math:`J_1`, :math:`Y_1`, :math:`J_2`
og :math:`Y_2`.
