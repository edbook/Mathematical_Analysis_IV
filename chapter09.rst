LÍNULEG AFLEIÐUJÖFNUHNEPPI
==========================

Tilvist og ótvíræðni lausna
---------------------------

Tilvist og ótvíræðni lausna
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Viðfangsefni þessa kafla eru línuleg afleiðujöfnuhneppi af gerðinni

.. math::

  u{{^{\prime}}}=A(t)u+f(t),

  

þar sem :math:`A\in C(I,{{\mathbb  C}}^{m\times m})` er fylkjafall og
:math:`f\in C(I,{{\mathbb  C}}^m)` er vigurfall sem er skilgreint á opnu
bili :math:`I` á :math:`{{\mathbb  R}}`. Ef við skrifum upp hnitin þá
verður hneppið

.. math::

  \begin{aligned}
   u_1{{^{\prime}}}&=a_{11}(t)u_1+\cdots+a_{1m}(t)u_m+f_1(t),\\
   u_2{{^{\prime}}}&=a_{21}(t)u_1+\cdots+a_{2m}(t)u_m+f_2(t),\\
   &\qquad \qquad \vdots\qquad \qquad \qquad \qquad \vdots\\
   u_m{{^{\prime}}}&=a_{m1}(t)u_1+\cdots+a_{mm}(t)u_m+f_m(t).\end{aligned}

Hneppið er sagt vera :hover:`óhliðrað,óhliðraður`
ef fallið :math:`f` er núllfallið,
en :hover:`hliðrað,misleitur` annars. 
Upphafsgildisverkefnið

.. math::

  u{{^{\prime}}}=A(t)u+f(t), \qquad u(a)=b,

  

hefur ótvírætt ákvarðaða lausn, þar sem :math:`a` er einhver gefinn punktur í
:math:`I` og :math:`b` er einhver gefinn vigur í
:math:`{{\mathbb  C}}^m`.

Skilgreining
^^^^^^^^^^^^

Línulega rúmið, sem samanstendur af öllum lausnum á óhliðruðu jöfnunni
:math:`u{{^{\prime}}}=A(t)u`, kallast *núllrúm* línulega jöfnuhneppisins. 
Við táknum það með :math:`{\cal N}(A)`.

Setning
^^^^^^^

Látum :math:`I\subset {{\mathbb  R}}` vera bil og
:math:`A\in C(I,{{\mathbb  C}}^ {m\times m})`. Þá hefur núllrúmið :math:`{\cal N}(A)` víddina :math:`m`.

--------------

Við athugum nú að ef :math:`v` og :math:`w` eru tvær lausnir á hliðruðu
jöfnunni :math:`u{{^{\prime}}}=A(t)u+f(t)`, þá er mismunurinn
:math:`v-w` í núllrúminu, því

.. math:: (v-w){{^{\prime}}}=v{{^{\prime}}}-w{{^{\prime}}}=A(t)v+f(t)-A(t)w-f(t)=A(t)(v-w).

Þetta gefur okkur því:

Setning
^^^^^^^

Látum :math:`I` vera bil á rauntalnaásnum,
:math:`A\in C(I,{{\mathbb  C}}^ {m\times m})` og :math:`f\in C(I,{{\mathbb  C}}^ m)`. Þá er sérhver
lausn á :math:`u'=A(t)u+f(t)` af gerðinni

.. math:: u(t)=c_1u_1(t)+\cdots+c_mu_m(t)+u_p(t),

þar sem :math:`u_1,\dots,u_m` er einhver grunnur í :math:`{\cal N}(A)`,
:math:`c_1,\dots,c_m\in{{\mathbb  C}}` og :math:`u_p` er einhver lausn á
hliðruðu jöfnunni.

Jöfnur af hærri stigum og jafngild hneppi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

við vitum að línuleg :math:`m`–ta stigs afleiðujafna

.. math::

  P(t,D)v= v^{(m)}+a_{m-1}(t)v^{(m-1)}+\cdots+a_1(t)v{{^{\prime}}}+a_0(t)v=g(t), \qquad t\in I, 

  

er jafngild hneppinu

.. math::

  \begin{aligned}
   u_1{{^{\prime}}}&= u_2,\quad
   u_2{{^{\prime}}}= u_3,\quad
   \dots, \quad u_{m-1}{{^{\prime}}}= u_m\\
   u_m{{^{\prime}}}&=-a_0(t)u_1-a_1(t)u_2-\cdots-a_{m-1}(t)u_m+g(t).
  \end{aligned}

í þeim skilningi að :math:`v` er lausn á afleiðujöfnunni þá og því
aðeins að :math:`u=[v,v{{^{\prime}}},\dots,v^{(m-1)}]^t` sé lausn á
hneppinu. Fylkið :math:`A(t)` og vigurinn :math:`f(t)` verða í þessu
tilfelli

.. math::

  A(t)=\left[\begin{matrix}
   0&1&0&\dots&0\\
   0&0&1&\dots&0\\
   \vdots&\vdots&\vdots&\ddots&\vdots\\
   0&0&0&\dots&1\\
   -a_0(t)&-a_1(t)&-a_2(t)&\dots&-a_{m-1}(t)
   \end{matrix}\right],
   \qquad
   f(t)=\left[\begin{matrix}
   0\\
   0\\
   \vdots\\
   0\\
   g(t)
  \end{matrix}\right].

Setning
^^^^^^^

Látum :math:`P(t,D)=D^ m+a_{m-1}(t)D^{m-1}+\cdots+a_1(t)D+a_0(t)`
vera línulegan afleiðuvirkja og skilgreinum :math:`A(t)` sem fylkið hér að ofan. Þá er

.. math:: \det(\lambda I-A(t))=P(t,\lambda),

þ.e.a.s. :hover:`kennimargliða` :math:`A(t)` er kennimargliða virkjans :math:`P(t,D)`.

Hneppi með fastastuðla
----------------------

Hneppi með fastastuðla
~~~~~~~~~~~~~~~~~~~~~~

Nú ætlum við að byrja á því að reikna út lausnir á línulegum
afleiðujöfnuhneppum. Við lítum á óhliðrað línulegt jöfnuhneppi
:math:`u{{^{\prime}}}=Au` og gerum ráð fyrir að stuðlarnir í fylkinu
:math:`A` séu fastaföll.

Hjálparsetning
^^^^^^^^^^^^^^

Látum :math:`A` vera :math:`m\times m` fylki og :math:`\varepsilon` vera
eiginvigur :hover:`eiginvigur` þess með tilliti til 
:hover:`eigingildisins,eigingildi` :math:`\lambda`. Þá
uppfyllir vigurfallið :math:`u(t)=e^{\lambda t}\varepsilon` jöfnuna
:math:`u{{^{\prime}}}=Au`.

--------------

Þessi einfalda hjálparsetning gefur okkur að í því tilfelli að hægt er
að liða :math:`b` og :math:`f(t)` í línulegar samantektir af
eiginvigrunum, þá leysist jöfnuhneppið upp í óháðar jöfnur sem við getum
leyst hverja fyrir sig:

  

Setning
^^^^^^^

Látum :math:`A` vera :math:`m\times m` fylki og gerum ráð fyrir að
:math:`\varepsilon_1,\dots,\varepsilon_\ell` séu eiginvigrar þess með
tilliti til eigingildanna :math:`\lambda_1,\dots,\lambda_\ell`. Ef
:math:`a \in I`, :math:`b\in {{\mathbb  C}}^m` og unnt er að skrifa
:math:`b=\beta_1\varepsilon_1+\cdots+\beta_\ell\varepsilon_\ell` og
:math:`f(t)=g_1(t)\varepsilon_1+\cdots+g_\ell(t)\varepsilon_\ell`, þá er
lausnin á upphafsgildisverkefninu :hover:`upphafsgildisverkefni`

.. math:: u{{^{\prime}}}=Au+f(t), \qquad \qquad u(a)=b,

gefin með
:math:`u(t)=v_1(t)\varepsilon_1+\cdots+v_\ell(t)\varepsilon_\ell`, þar
sem stuðullinn :math:`v_j` uppfyllir

.. math::

  v_j{{^{\prime}}}(t)=\lambda_jv_j(t)+g_j(t), \qquad v_j(a)=\beta_j,

  

og er þar með

.. math::

  v_j(t)=\beta_je^{\lambda_j(t-a)}+e^{\lambda_jt}\int_a^t e^{-\lambda_j
  \tau}g_j(\tau) \, d\tau.

Úrlausn með gefinn eiginvigragrunn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við gera ráð fyrir því að fylkið :math:`A` hafi
eiginvigragrunn :math:`\varepsilon_1,\dots, \varepsilon_m` með eigingildin
:math:`\lambda_1,\dots,\lambda_m`. Þá getum við þáttað fylkið :math:`A` í

.. math::

  A=T\Lambda T^{-1},

  

þar sem eiginvigrarnir eru dálkar fylkisins :math:`T` og
:math:`\Lambda={{\operatorname{diag}}}(\lambda_1,\dots,\lambda_m)` er
hornalínufylki með tilsvarandi eigingildi á hornalínunni,

.. math::

  T=\left[\begin{matrix}
   \varepsilon_{11}&\varepsilon_{12}&\dots&\varepsilon_{1m}\\
   \varepsilon_{21}&\varepsilon_{22}&\dots&\varepsilon_{2m}\\
   \vdots&\vdots&\ddots&\vdots\\
   \varepsilon_{m1}&\varepsilon_{m2}&\dots&\varepsilon_{mm}
   \end{matrix}\right],\qquad
   \Lambda =\left[\begin{matrix}
   \lambda_1&0&\dots&0\\
   0&\lambda_2&\dots&0\\
   \vdots&\vdots&\ddots&\vdots\\
   0&0&\dots&\lambda_m
   \end{matrix}\right].

Hér skrifum við
:math:`\varepsilon_j=[\varepsilon_{1j},\dots,\varepsilon_{mj}]^t`. Hér
mikilvægt að minnast þess að ef :math:`b` er vigur í
:math:`{{\mathbb  C}}^m`, þá eru hnit hans
:math:`\beta=[\beta_1,\dots,\beta_m]^t` miðað við grunninn
:math:`\{\varepsilon_1,\dots,\varepsilon_m\}` gefin með jöfnunni
:math:`{\beta}=T^{-1}b`.

Nú skulum við skoða aftur lausnina á upphafsgildisverkefninu. Við
látum :math:`v(t)=[v_1(t),\dots,v_m(t)]^t` vera hnit :math:`u(t)`,
:math:`g(t)=[g_1(t),\dots,g_m(t)]^t` vera hnit :math:`f(t)` og
:math:`\beta=[\beta_1,\dots,\beta_m]^t` vera hnit :math:`b` miðað við
grunninn :math:`\{\varepsilon_1,\dots,\varepsilon_m\}`,
þ.e. \ :math:`v=T^{-1}u`, :math:`g=T^{-1}f` og :math:`\beta=T^{-1}b`.
Við reiknum nú afleiðuna af :math:`v` og notum :math:`A=T\Lambda T^{-1}`
.. math::

  \begin{gathered}
   v{{^{\prime}}}=T^{-1}u{{^{\prime}}}=T^{-1}(Au+f(t))=
   T^{-1}T\Lambda T^{-1}u+T^{-1}f(t)=\Lambda v+g(t), \qquad t\in I,\\
   v(a)=T^{-1}u(a)=T^{-1}b=\beta \end{gathered}

Nú er :math:`\Lambda v=(\lambda_1v_1,\dots,\lambda_mv_m)`, svo við
höfum fengið upphafsgildisverkefni fyrir :math:`v`. 
Lausnin er gefin í setningunni hér að framan.

Nú skulum við líta á þessa formúlu ögn nánar. Við skilgreinum
fylkjafallið

.. math::

  {{\operatorname{diag}}}(e^{\lambda_1t},\dots,e^{\lambda_mt})=
   \left[\begin{matrix}
   e^{\lambda_1t}&0&\dots&0\\
   0&e^{\lambda_2t}&\dots&0\\
   \vdots&\vdots&\ddots&\vdots\\
   0&0&\dots&e^{\lambda_mt}
   \end{matrix}\right],

og athugum síðan að
:math:`T{{\operatorname{diag}}}(e^{\lambda_1t},\dots,e^{\lambda_mt})`
hefur dálkana
:math:`e^{\lambda_1t}\varepsilon_1,\dots,e^{\lambda_mt}\varepsilon_m`
og því er

.. math::

  \begin{gathered}
   \beta_1e^{\lambda_1(t-a)}\varepsilon_1+
   \cdots+\beta_me^{\lambda_m(t-a)}\varepsilon_m=
   T{{\operatorname{diag}}}(e^{\lambda_1(t-a)},\dots,e^{\lambda_m(t-a)})\beta,\\
   e^{\lambda_1(t-\tau)}g_1(\tau)\varepsilon_1
   +\cdots+
   e^{\lambda_m(t-\tau)}g_m(\tau)\varepsilon_m=
   T{{\operatorname{diag}}}(e^{\lambda_1(t-\tau)},\dots,e^{\lambda_m(t-\tau)})g(\tau).\end{gathered}

Nú er :math:`\beta=T^{-1}b` og :math:`g(\tau)=T^{-1}f(\tau)`, svo við
fáum umritaðun á framsetningu á setningunni hér að framan.

Setning
^^^^^^^

Látum :math:`A` vera :math:`m\times m` fylki og gerum ráð fyrir að hægt
sé að þátta :math:`A` í :math:`A=T\Lambda T^{-1}` þar sem
:math:`\Lambda` er hornalínufylki með hornalínustökin
:math:`\lambda_1,\dots,\lambda_m`. Látum :math:`I` vera bil á
:math:`{{\mathbb  R}}`, :math:`a\in I`,
:math:`f\in C(I,{{\mathbb  C}}^m)` og :math:`b\in {{\mathbb  C}}^m`. Þá
hefur upphafsgildisverkefnið

.. math:: u{{^{\prime}}}=Au+f(t), \qquad u(a)=b

ótvírætt ákvarðaða lausn á :math:`I`, sem gefin er með formúlunni

.. math::

  \begin{aligned}
   u(t)&=T{{\operatorname{diag}}}(e^{\lambda_1(t-a)},\dots,e^{\lambda_m(t-a)})T^{-1}b\\
   &+\int_a^t T{{\operatorname{diag}}}(e^{\lambda_1(t-\tau)},\dots,e^{\lambda_m(t-\tau)})
   T^{-1}f(\tau)\, d\tau.\end{aligned}


Annars stigs hneppi
~~~~~~~~~~~~~~~~~~~

Aðferðinni sem við höfum verið að lýsa er oft hægt að beita á annars
stigs hneppi, til að leysa upphafsgildisverkefni af gerðinni

.. math::

  u{{^{\prime\prime}}}=Au+f(t), \qquad u(a)=b, \quad u{{^{\prime}}}(a)=c,


  

í því tilfelli að hægt er að skrifa

.. math::

  b=\beta_1\varepsilon_1+\cdots+\beta_\ell\varepsilon_\ell, \quad
   c=\gamma_1\varepsilon_1+\cdots+\gamma_\ell\varepsilon_\ell,\quad
   f(t)=g_1(t)\varepsilon_1+\cdots+g_\ell(t)\varepsilon_\ell.

Lausnin verður þá einfaldlega af gerðinni

.. math::

  u(t)=v_1(t)\varepsilon_1+\cdots+v_\ell(t)\varepsilon_\ell,


  

þar sem :math:`v_j` er lausnin á upphafsgildisverkefninu

.. math::

  v_j{{^{\prime\prime}}}=\lambda_j v_j +g_j(t), \qquad v_j(a)=\beta_j, \quad
   v_j{{^{\prime}}}(a)=\gamma_j. 


  

Þessi formúla er staðfest með beinum útreikningi. Ef við gerum ráð
fyrir því að öll eigingildin séu neikvæð :math:`\lambda_j=-\omega_j^2`,
þá notfærum við okkur að :math:`\cos {\omega}_j t` og
:math:`\sin {\omega}_jt` er lausnargrunnur fyrir óhliðruðu jöfnuna og
:math:`\sin({\omega}_j(t-{\tau}))/{\omega}_j` er Green–fall virkjans.
Þar með er lausnin

.. math::

  v_j(t)=\beta_j \cos(\omega_j(t-a))+
   (\gamma_j/\omega_j)\sin (\omega_j(t-a)) +
   \int_a^t\dfrac{\sin (\omega_j(t-\tau))}{\omega_j}g_j(\tau) \, d\tau. 


  

Í því tilfelli að hneppið er hreyfijöfnur einhvers eðlisfræðilegs
kerfis, þá kallast liðirnir :math:`v_j(t)\varepsilon_j` í
lausnarformúlunni *sveifluhættir* kerfisins. Þeir
eru innbyrðis óháðir eins og jöfnurnar. Stærðin :math:`{\omega}_j`
nefnist *tíðni sveifluháttarins* :math:`v_j(t)\varepsilon_j`.

Grunnfylki
----------

Grunnfylki
~~~~~~~~~~

Lítum á óhliðrað línulegt afleiðujöfnuhneppi

.. math:: u{{^{\prime}}}=A(t)u, \qquad t\in I,

þar sem :math:`A\in C(I,{{\mathbb  C}}^{m\times m})`,
:math:`A(t)=(a_{jk}(t))_{j,k=1}^ m`. 

Mengi allra lausna myndar línulegt rúm af vídd :math:`m`.

  

Hjálparsetning
^^^^^^^^^^^^^^

Látum :math:`u_1,\dots,u_m` vera föll í :math:`{\cal N}(A)`. Þá eru
eftirfarandi skilyrði jafngild:

\(i) Vigurföllin :math:`u_1,\dots,u_m` eru línulega óháð á bilinu
:math:`I`.

\(ii) Vigrarnir :math:`u_1(t),\dots,u_m(t)` eru línulega óháðir í
:math:`{{\mathbb  R}}^ m` (eða :math:`{{\mathbb  C}}^ m`) fyrir
sérhvert :math:`t\in I`.

\(iii) Vigrarnir :math:`u_1(a),\dots,u_m(a)` eru línulega óháðir í
:math:`{{\mathbb  R}}^ m` (eða :math:`{{\mathbb  C}}^ m`) fyrir
eitthvert :math:`a\in I`.

Skilgreining
^^^^^^^^^^^^

Fylki af gerðinni

.. math:: \Phi(t)=[u_1(t),\dots,u_m(t)], \qquad t\in I,

þar sem dálkavigrarnir :math:`u_1,\dots,u_m` mynda grunn í núllrúminu
:math:`{\cal N}(A)` fyrir afleiðujöfnuhneppið :math:`u{{^{\prime}}}=A(t)u`, kallast
*grunnfylki* fyrir afleiðujöfnuhneppið.

--------------

Samkvæmt hjálparsetningunni eru dálkarnir í
:math:`\Phi(t)` línulega óháðir fyrir öll :math:`t\in I` og þar með er
andhverfan :math:`\Phi(t)^{-1}` til í sérhverjum punkti
:math:`t\in I`. Við sjáum jafnframt að

.. math::

  \begin{aligned}
   \Phi{{^{\prime}}}(t)&= [u_1{{^{\prime}}}(t),\dots,u_m{{^{\prime}}}(t)]=\nonumber\\
   &=[A(t)u_1(t),\dots,A(t)u_m(t)]=\\
   &=A(t)\Phi(t).\nonumber\end{aligned}

Af hjálparsetningunni leiðir einnig að ef :math:`m\times m` fylkjafallið :math:`\Phi` uppfyllir
:math:`\Phi{{^{\prime}}}=A(t)\Phi` og :math:`\Phi(a)` hefur andhverfu
fyrir eitthvert :math:`a\in I`, þá er :math:`\Phi(t)` grunnfylki fyrir
afleiðujöfnuhneppið :math:`u{{^{\prime}}}=A(t)u`.

Setning
^^^^^^^

Látum :math:`\Phi` og :math:`\Psi` vera tvö grunnfylki fyrir
jöfnuhneppið :math:`u{{^{\prime}}}=A(t)u`. Þá er til andhverfanlegt
fylki :math:`B` þannig að

.. math::

  \Psi(t)=\Phi(t)B.

  

Upphafsgildisverkefni fyrir grunnfylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við fáum nú lýsingu á lausn upphafsgildisverkefnisins með grunnfylkjum:

  

Setning
^^^^^^^

Látum :math:`\Phi(t)` vera grunnfylki fyrir jöfnuhneppið
:math:`u{{^{\prime}}}=A(t)u`.

\(i) Sérhvert stak í :math:`{\cal N}(A)` er af gerðinni
:math:`u(t)=\Phi(t)c`, þar sem :math:`c` er vigur í
:math:`{{\mathbb  C}}^ m`.

\(ii) Vigurfallið :math:`u_p`, sem gefið er með formúlunni

.. math:: u_p(t)=\Phi(t)\int_a^ t \Phi(\tau)^{-1}f(\tau)\, d\tau,

uppfyllir :math:`u{{^{\prime}}}=A(t)u+f(t)` og :math:`u(a)=0`.

\(iii) Lausnin á upphafsgildisverkefninu
:math:`u{{^{\prime}}}=A(t)u+f(t)`, :math:`u(a)=b` er gefin með
formúlunni

.. math::

  u(t)=\Phi(t)\Phi(a)^{-1}b+
   \Phi(t)\int_a^ t \Phi(\tau)^{-1}f(\tau)\, d\tau.

--------------

Nú getum við beitt setningunni á dálkana í :math:`m\times m` fylkinu
:math:`U(t)` og fengið eftirfarandi tilvistarsetningu:

Setning
^^^^^^^

Látum :math:`A, F\in C(I,{{\mathbb  C}}^ {m\times m})` og látum
:math:`\Phi` vera grunnfylki fyrir :math:`A`. Þá hefur :math:`m\times m`
fylkjaafleiðujafnan

.. math:: U{{^{\prime}}}=A(t)U+F(t), \qquad U(a)=B,

ótvírætt ákvarðaða lausn :math:`U(t)`, sem gefin er með formúlunni

.. math::

  U(t)=\Phi(t)\Phi(a)^{-1}B + \Phi(t)\int_a^ t \Phi(\tau)^
   {-1}F(\tau) \, d\tau.

Hneppi með fastastuðla
~~~~~~~~~~~~~~~~~~~~~~

Gerum nú ráð fyrir því að :math:`A` hafi fastastuðla og að eiginvigrar
þess myndi grunn í :math:`{{\mathbb  C}}^ m`. Eins og við höfum áður
sannfært okkur um, þá er það jafngilt því að unnt sé að þátta fylkið
:math:`A` í

.. math:: A=T\Lambda T^{-1},

þar sem :math:`\Lambda` er hornalínufylki með eigingildin á
hornalínunni,

.. math::

  \Lambda={{\operatorname{diag}}}(\lambda_1,\dots,\lambda_m)=\left[\begin{matrix} 
   \lambda_1&0&\dots&0\\
   0&\lambda_2&\dots&0\\
   \vdots&\vdots&\ddots&\vdots\\
   0&0&\dots&\lambda_m\end{matrix}\right].

Lítum á fylkið

.. math:: \Phi(t)=T{{\operatorname{diag}}}(e^{t\lambda_1},\dots,e^{t\lambda_m})T^{-1}.

Það uppfyllir

.. math::

  \begin{aligned}
   \Phi{{^{\prime}}}(t)
   &=T{{\operatorname{diag}}}(\lambda_1e^{t\lambda_1},\dots,\lambda_me^{t\lambda_m})T^{-1}=\\
   &=T{{\operatorname{diag}}}(\lambda_1,\dots,\lambda_m)
   {{\operatorname{diag}}}(e^{t\lambda_1},\dots,e^{t\lambda_m})T^{-1}=\\
   &=T\Lambda T^{-1} T
   {{\operatorname{diag}}}(e^{t\lambda_1},\dots,e^{t\lambda_m})T^{-1}=\\
   &=A\Phi(t), \end{aligned}

með upphafsskilyrðinu

.. math:: \Phi(0)=I.

Þar með er :math:`\Phi` grunnfylki fyrir hneppið
:math:`u{{^{\prime}}}=Au`. Hér er komin grunnlausnin sem við notuðum í
fyrri útleiðslu okkar.

Fylkjamargliður og fylkjaveldaraðir
-----------------------------------


Ef :math:`A` er :math:`m\times m` fylki og :math:`p(\lambda)` er
margliða af tvinnbreytistærðinni :math:`\lambda`,

.. math:: p(\lambda)=a_0+a_1\lambda+\cdots+a_n\lambda^n,

þá getum við skilgreint fylkjamargliðuna :math:`p(A)` með formúlunni

.. math:: p(A)=a_0 I+a_1A+\cdots+a_n A^n,

þar sem :math:`I` táknar :math:`m\times m`–einingarfylkið. Hér höfum
við einfaldlega skipt á veldum :math:`\lambda^k` af :math:`\lambda` og
veldum :math:`A^k` af :math:`A` og jafnframt margfaldað fastaliðinn með
einingarfylkinu :math:`I`. Til þess að geta stungið :math:`A` inn í
óendanlegar veldaraðir, þá þurfum við að skilgreina samleitni:

Samleitnar fylkjarunur
~~~~~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Runa :math:`\{C_n\}_{n=0}^\infty`, af :math:`\ell\times m` fylkjum
:math:`C_n=\big(c_{jkn}\big)_{j=1,k=1}^{\ell, m}` er sögð vera samleitin
ef allar stuðlarunurnar

.. math:: \{c_{jkn}\}_{n=0}^\infty, \qquad j=1,\dots,\ell, \quad k=1,\dots, m.

eru samleitnar. Fylkið :math:`C=\big(c_{jk}\big)_{j=1,k=1}^{\ell, m}`
sem hefur stuðlana

.. math::

  c_{jk}=\lim\limits_{n\to\infty}c_{jkn}, \qquad j=1,\dots,\ell, \quad
   k=1,\dots, m,

kallast markgildi rununnar :math:`\{C_n\}_{n=0}^\infty` og við táknum
það með

.. math:: C=\lim\limits_{n\to \infty}C_n.

Óendanleg summa :math:`\sum_{n=0}^\infty C_n` af :math:`\ell\times m`
fylkjum er sögð vera samleitin, ef runan af hlutsummum
:math:`\{\sum_{n=0}^N C_n\}_{N=0}^\infty` er samleitin. Við táknum markgildið einnig með
:math:`\sum_{n=0}^\infty C_n`,

.. math::

  \sum_{n=0}^\infty C_n= \lim\limits_{N\to \infty}
   \sum_{n=0}^N C_n.

--------------

Ef :math:`C_n=a_n A^n` og :math:`A^0=I`, þá er
:math:`\sum_{n=0}^\infty C_n=\sum_{n=0}^\infty a_nA^n` veldaröð.

Fylkjastaðall
~~~~~~~~~~~~~

Til þess að geta skorið úr um samleitni veldaraða þá þurfum við að
tengja fylkið við samleitnigeisla raðarinnar. Til þess innleiðum við:

Skilgreining
^^^^^^^^^^^^

(*Fylkjastaðall*).   Ef :math:`A` er :math:`\ell\times m`
fylki, :math:`A=(a_{jk})`, með tvinntölustök, þá skilgreinum við
:hover:`staðalinn,staðall` :math:`\|A\|` af :math:`A` með formúlunni

.. math:: \|A\|=\sum_{j=1}^ \ell \sum_{k=1}^ m |a_{jk}|.

Við köllum töluna :math:`\|A\|` einnig *lengd*
fylkisins :math:`A`.

  

Setning
^^^^^^^

(*Reiknireglur um fylkjastaðal*).   

\(i) Ef :math:`A` og :math:`B` eru
:math:`\ell\times m` fylki með stök í :math:`{{\mathbb  C}}` og
:math:`c\in {{\mathbb  C}}`, þá er

.. math::

  \|A+B\|\leq \|A\|+\|B\| \qquad \text{og} \qquad
   \|cA\|=|c|\|A\|.

\(ii) Ef :math:`A` er :math:`\ell\times m` fylki og :math:`B` er
:math:`m\times n` fylki, þá er

.. math:: \|AB\|\leq \|A\|\|B\|.

\(iii) Ef :math:`A` er :math:`m\times m` fylki, þá er

.. math:: \|A^ n\|\leq \|A\|^ n.


Samleitnar fylkjaraðir
~~~~~~~~~~~~~~~~~~~~~~

  

Setning
^^^^^^^

(*Samleitnipróf fyrir fylkjaraðir*).   Látum :math:`\{C_n\}`
vera runu af :math:`\ell\times m` fylkjum þannig að talnaröðin
:math:`\sum_{n=0}^ \infty\|C_n\|` sé samleitin. Þá er fylkjaröðin
:math:`\sum_{n=0}^ \infty C_n` samleitin.

Fylgisetning
^^^^^^^^^^^^

Látum :math:`\sum_{n=0}^ \infty c_nz^ n` vera veldaröð með
tvinntölustuðla og gerum ráð fyrir að samleitnigeisli hennar sé
:math:`{\varrho}>0`. Ef :math:`A` er :math:`m\times m` fylki með
tvinntölustuðla og :math:`\|A\|<{\varrho}`, þá er fylkjaveldaröðin
:math:`\sum_{n=0}^ \infty c_nA^ n` samleitin.

--------------

Hugsum okkur nú að :math:`f:S(0,\varrho)\to {{\mathbb  C}}` sé fágað
fall sem gefið er með

.. math:: f(z)=\sum_{n=0}^ \infty c_n z^ n, \qquad z\in S(0,\varrho).

Ef :math:`A` er :math:`m\times m` fylki og :math:`\|A\|< \varrho`, þá
getum við skilgreint :math:`m\times m` fylkið :math:`f(A)` með því að
stinga :math:`A` inn í veldaröðina fyrir fágaða fallið :math:`f`,

.. math:: f(A)=\sum_{n=0}^ \infty c_nA^ n,

því fylkjaveldaröðin í hægri hliðinni er samleitin. Við skilgreinum
:math:`A^0=I`. Ef við vitum að :math:`f` er fágað fall á öllu
:math:`{{\mathbb  C}}` þá þurfum við engar áhyggjur að hafa af
samleitninni og við getum sett hvaða :math:`m\times m` fylki sem er inn
í röðina. Sem dæmi um fylkjaföll getum við tekið

.. math::

  \begin{aligned}
   e^A&=\sum\limits_{n=0}^\infty\dfrac 1{n!}{A^n}
   =I+A+\dfrac {1}{2!}A^2+\dfrac{1}{3!}A^3+\cdots,\\
   \cos A&= \sum\limits_{n=0}^\infty \dfrac{(-1)^n}{(2n)!}A^{2n}
   =I-\dfrac{1}{2!}A^2+\dfrac{1}{4!}A^4-\cdots,\\
   \sin A &=\sum\limits_{n=0}^\infty\dfrac{(-1)^n}{(2n+1)!}A^{2n+1}
   = A-\dfrac {1}{3!}A^3+\dfrac{1}{5!}A^5-\cdots,\\
   \cosh A&=\sum\limits_{n=0}^\infty\dfrac{1}{(2n)!}A^{2n}
   =I+\dfrac{1}{2!}A^2+\dfrac{1}{4!}A^4+\cdots,\\
   \sinh A &=\sum\limits_{n=0}^\infty\dfrac{1}{(2n+1)!}A^{2n+1}
   = A+\dfrac {1}{3!}A^3+\dfrac{1}{5!}A^5+\cdots,\\
   \ln (I+A) &= \sum\limits_{n=1}^\infty\dfrac{(-1)^{n+1}}{n}A^n
   =A-\dfrac{1}{2}A^2+\frac{1}3A^3-\cdots,\\
   (I-A)^{-1}&=\sum\limits_{n=0}^\infty A^n
   =I+A+A^2+\cdots, \\
   (I+A)^\alpha&= I+\alpha A+ \dfrac{\alpha(\alpha-1)}{2!}A^2 + 
   \dfrac {\alpha(\alpha-1)(\alpha-2)}{3!}A^3+\cdots.\end{aligned}

Fyrstu fimm raðirnar eru vel skilgreindar fyrir öll :math:`m\times m`
fylki, en hinar þrjár eru vel skilgreindar ef :math:`\|A\|<1`.

Veldisvísisfylkið
-----------------

Veldisvísisfylkið
~~~~~~~~~~~~~~~~~

Nú ætlum við að finna almenna formúlu fyrir grunnfylki fyrir línulegt
jöfnuhneppi með fastastuðla. Við höfum séð hvernig grunnfylkið
lítur út í því tilfelli að eiginvigrar stuðlafylkisins myndi grunn í
:math:`{{\mathbb  C}}^ m`. Við byrjum á því að skoða rununa
:math:`{{\{u_n\}}}` sem skilgreind var í aðferð Picards. Hún er

.. math::

  \begin{gathered}
   u_0(t)=b,\\
   u_1(t)=b+\int_0^ t Ab \, d\tau = (I+tA)b,\\
   u_2(t)=b+\int_0^ t A(I+\tau A)b \, d\tau = (I+tA+\dfrac 12(tA)^ 2)b,\\
   u_3(t)=b+\int_0^ t A(I+\tau A + \dfrac{\tau^ 2}2A^ 2)b \, d\tau 
   = (I+tA+\dfrac 12(tA)^ 2+\dfrac 1{3!}(tA)^ 3)b,\\
   u_n(t)= (I+tA+\dots+\dfrac 1{n!}(tA)^ n)b.\end{gathered}

Í sönnun okkar á tilvistarsetningunni sýndum við fram á að þessi runa
er samleitin í jöfnum mæli á sérhverju takmörkuðu bili á rauntalnaásnum
:math:`{{\mathbb  R}}`. Með því að velja vigurinn :math:`b` sem
grunnvigrana

.. math::

  [1,0,\dots,0]^t, \ [0,1,0,\dots,0]^t\ \dots, 
   \ [0,\dots,0,1]^t,

þá fáum við út úr aðferð Picards að fylkjaröðin
:math:`\sum_{n=0}^ \infty  \dfrac 1{n!}(tA)^ n` er samleitin. Við sjáum að hér er komin
veldaröðin fyrir veldisvísisfallið og sem grunnfylki fyrir jöfnuhneppið
:math:`u{{^{\prime}}}=Au` fáum við síðan :math:`\Phi(t)=e^ {tA}`.

Setning
^^^^^^^

:hover:`Fylkjafallið,fylkjafall` :math:`\Phi(t)= e^{tA}` er hin ótvírætt
ákvarðaða lausn upphafsgildisverkefnisins

.. math:: \Phi{{^{\prime}}}(t) = A\Phi(t), \qquad t\in {{\mathbb  R}}, \qquad \Phi(0)=I.

--------------

Hægt er að nota tilvistarsetninguna fyrir
línuleg hneppi til þess að sanna samlagningarformúluna fyrir
fylkjaveldisvísisfallið:

  

Setning
^^^^^^^

Ef :math:`A` og :math:`B` eru :math:`m\times m` fylki og :math:`AB=BA`,
þá er

.. math::

  e^{A+B}=e^ Ae^ B=e^Be^A.

  

Fylgisetning
^^^^^^^^^^^^

Fylkið :math:`e^ {tA}` hefur andhverfuna :math:`e^{-tA}`.

--------------

Setninguna hér að framan er ekki nokkur vandi að alhæfa:

Setning
^^^^^^^

Ef :math:`A` og :math:`B` eru :math:`m\times m` fylki og :math:`AB=BA`,
:math:`f` og :math:`g` eru fáguð föll á :math:`S(0,\varrho)`,
:math:`\|A\|< \varrho` og :math:`\|B\|<\varrho`, þá er

.. math:: f(A)g(B)=g(B)f(A).
  

Setning
^^^^^^^

Ef :math:`A=TBT^{-1}`, :math:`f(z)=\sum_{n=0}^\infty a_nz^n` er fágað fall, 
gefið með veldaröð sem hefur samleitnigeisla :math:`>\|A\|`, þá er :math:`f(A)=Tf(B)T^{-1}`.

--------------

Látum nú :math:`A` vera :math:`m\times m` fylki og gerum ráð því að
eiginvigrarnir :math:`\varepsilon_1,\dots,\varepsilon_m` með tilliti til
eigingildanna :math:`\lambda_1,\dots,\lambda_m` myndi grunn í
:math:`{{\mathbb  C}}^ m`. Það er jafgilt því að unnt sé að þátta
fylkið :math:`A` í

.. math:: A=T\Lambda T^{-1},

þar sem :math:`\varepsilon_1,\dots,\varepsilon_m` mynda dálkana í
:math:`T` og
:math:`\Lambda={{\operatorname{diag}}}(\lambda_1,\dots,\lambda_m)`.
Setningin gefur nú

.. math:: e^{t A}=Te^{t\Lambda} T^{-1}.

Cayley–Hamilton–setningin
-------------------------

Cayley–Hamilton–setningin
~~~~~~~~~~~~~~~~~~~~~~~~~

Veldisvísisfylkið :math:`e^ {tA}` af :math:`m\times m` fylki
:math:`A`, er gefið með óendanlegri veldaröð, sem ekki er árennileg við
fyrstu sýn. Við ætlum nú að sýna fram á að ætíð sé unnt að skrifa
:math:`e^{tA}` á forminu

.. math:: e^{tA}= f_0(t)I+f_1(t)A+\cdots+f_{m-1}(t)A^{m-1},

þar sem föllin :math:`f_0,\dots,f_{m-1}` eru gefin með samleitnum
veldaröðum á :math:`{{\mathbb  R}}`. Veldisvísisfallið :math:`e^{tA}`
er sem sagt margliða í :math:`A` af stigi :math:`\leq (m-1)` með
tvinntölustuðla sem eru háðir :math:`t`.

Skilgreining
^^^^^^^^^^^^

Ef :math:`A` er :math:`m\times m` fylki með stuðla í
:math:`{{\mathbb  C}}`, þá táknum við kennimargliðu þess með
:math:`p_A(\lambda)`,

.. math:: p_A(\lambda)=\det(\lambda I-A).

--------------

Við getum skrifað

.. math:: p_A(\lambda)=a_0+a_1\lambda+\cdots+a_{m-1}\lambda^{m-1}+\lambda^ m

og jafnframt myndað fylkjamargliðuna :math:`p_A(A)`, sem er
:math:`m\times m` fylki, með því að setja :math:`A` inn í þessa formúlu,

.. math:: p_A(A)=a_0I+a_1A+\cdots+a_{m-1}A^{m-1}+A^ m.

Setning
^^^^^^^

(*Cayley–Hamilton*).   Ef :math:`A` er :math:`m\times m`
fylki, þá er :math:`p_A(A)=0`.

--------------

Við athugum fyrst að setningin er algerlega augljós ef eiginvigrar
:math:`A` mynda grunn í :math:`{{\mathbb  C}}^ m`, því þá er unnt að
þátta fylkið :math:`A` í :math:`A=T\Lambda T^{-1}`, þar sem
:math:`\Lambda={{\operatorname{diag}}}(\lambda_1,\dots,\lambda_m)` er
hornalínufylkið með eigingildin á hornalínunni og

.. math::

  p_A(A)=Tp_A(\Lambda)T^{-1}=
   T{{\operatorname{diag}}}(p_A(\lambda_1),\dots,p_A(\lambda_m))T^{-1}=0

því eigingildin :math:`\lambda_1,\dots,\lambda_m` eru núllstövar
kennimargliðunnar :math:`p_A`.

Nú skulum við athuga hvaða þýðingu setning Cayley–Hamilton hefur. Ef við
skrifum

.. math::

  p_A(\lambda)=\lambda^
   m+a_{m-1}\lambda^{m-1}+\cdots+a_1\lambda+a_0,

þá gefur hún að

.. math::

  A^ m=-a_0I-a_1A-\cdots-a_{m-1}A^ {m-1}. 

  

Með þrepun fáum við síðan að fyrir sérhvert :math:`n\geq m` eru til
stuðlar :math:`c_{jn}` þannig að

.. math::

  \dfrac 1{n!}A^ n=
   c_{0n}I+c_{1n}A+\cdots+c_{m-1,n}A^{m-1}.

Þegar við stingum þessu inn í veldaröðina fyrir :math:`e^{tA}`, þá
fáum við

.. math::

  e^ {tA}= \sum_{j=0}^ {m-1}\bigg(
   \sum_{n=0}^\infty c_{jn}t^ n\bigg)A^ j.

Þessi formúla er alls ekki svo fráleit til útreikninga á tölvu, því við
fáum rakningarformúlur fyrir stuðlana út frá :math:`A^ m=-a_0I-a_1A-\cdots-a_{m-1}A^ {m-1}` og

.. math::

  \begin{gathered}
   \dfrac 1{(n+1)!}A^{n+1} =\dfrac 1{n+1}A\cdot\dfrac 1{n!}A^ n=\\
   =\dfrac{c_{0n}}{n+1}A+\dfrac{c_{1n}}{n+1}A^ 2+\cdots
   +\dfrac{c_{m-1,n}}{n+1}A^ m=\\
   =\dfrac{-c_{m-1,n}a_0}{n+1}I+\dfrac{c_{0n}-c_{m-1,n}a_1}{n+1}A+
   \cdots+\dfrac{c_{m-2,n}-c_{m-1,n}a_{m-1}}{n+1}A^{m-1}.\end{gathered}

Stuðlarnir með númer :math:`n=0,\dots,m-1` eru gefnir með

.. math::

  \begin{matrix}
    & c_{0n}& c_{1n}&\dots&c_{(m-1),n}\\
   n=0&1/0!&0&\dots&0\\
   n=1&0&1/1!&\dots&0\\
   \vdots&\vdots&\vdots&\ddots&\vdots\\
   n=m-1&0&0&\dots&1/n!.
   \end{matrix}

Rakningarformúlurnar fyrir stuðlana með númer :math:`n\geq m` verða
síðan

.. math::

  \begin{aligned}
   c_{0,n+1}&= \dfrac{-c_{m-1,n}a_0}{n+1},\\
   c_{j,n+1}&= \dfrac{c_{j-1,n}-c_{m-1,n}a_j}{n+1}, 
   \qquad j=1,\dots,m-1.\end{aligned}

Það er greinilega auðvelt að forrita þetta í tölvu. Lausnin á
upphafsgildisverkefninu :math:`u{{^{\prime}}}=Au`, :math:`u(0)=b` er
síðan

.. math::

  u(t) =e^{tA}b = 
   \bigg( \sum_{n=0}^\infty c_{0n}t^ n\bigg) b_0+\cdots+
   \bigg( \sum_{n=0}^ \infty c_{m-1,n}t^ n\bigg) b_{m-1},

þar sem vigrarnir :math:`b_0,\dots, b_{m-1}` eru reiknaðir út frá

.. math::

  b_0=b, \qquad b_1=Ab, \qquad b_2=A^ 2b=Ab_1, \dots,
   b_{m-1}=A^{m-1}b=Ab_{m-2}.

Newton-margliður
----------------

Brúunarverkefni
~~~~~~~~~~~~~~~

Látum :math:`f\in {{\cal O}}({{\mathbb  C}})` vera gefið fall, látum
:math:`\alpha_1,\dots,\alpha_\ell` vera ólíka punkta í
:math:`{{\mathbb  C}}`, látum :math:`m_1,\dots,m_\ell` vera jákvæðar
heiltölur og setjum :math:`m=m_1+\cdots+m_\ell`. Nú ætlum við að sýna
fram á að það verkefni að finna margliðu :math:`r` af stigi :math:`<m`,
sem uppfyllir

.. math::

  f^{(j)}(\alpha_k) = r^{(j)}(\alpha_k), \qquad j=0,\dots,m_k-1, \quad
   k=1,\dots, \ell,

  

hafi ótvírætt ákvarðaða lausn :math:`r` og við ætlum jafnframt að finna
formúlu fyrir margliðuna :math:`r`. Verkefni af þessu tagi nefnist
*brúunarverkefni*. 

Síðan munum við sjá hvernig þessar formúlur eru
notaðar til þess að reikna út veldisvísisfylkið :math:`e^{tA}`.

Úrlausn á brúunarverkefninu
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við skilgreinum rununa :math:`\lambda_1,\dots,\lambda_m` með því að
telja :math:`\alpha_1,\dots,\alpha_\ell` með margfeldni, þannig að
fyrstu :math:`m_1` gildin á :math:`\lambda_j` séu :math:`\alpha_1`,
næstu :math:`m_2` gildin á :math:`\lambda_j` séu :math:`\alpha_2`
o.s.frv. Við skilgreinum síðan

.. math::

  p(z)=(z-\alpha_1)^{m_1}\cdots(z-\alpha_\ell)^{m_\ell}
   =(z-\lambda_1)\cdots(z-\lambda_m).

  

Athugum sértilfellið þegar :math:`\ell=1`. Þá getum við skrifað lausnina
:math:`r` beint niður því hún er Taylor-margliða fallsins :math:`f` í
punktinum :math:`\alpha_1` númer :math:`m-1`,

.. math::

  r(z)=f(\alpha_1)+f'(\alpha_1)(z-\alpha_1)+\cdots +
   \frac {f^{(m-1)}(\alpha_1)}{(m-1)!}(z-\alpha_1)^{m-1}.

Almenna niðurstaðan er:

Setning
^^^^^^^

Látum :math:`f\in {{\cal O}}({{\mathbb  C}})`,
:math:`\alpha_1,\dots,\alpha_\ell` vera ólíka punkta í
:math:`{{\mathbb  C}}`, :math:`m_1,\dots,m_\ell` vera jákvæðar
heiltölur, setjum :math:`m=m_1+\cdots+m_\ell` og skilgreinum
:math:`p(z)` eins og hér að framan. Þá er til margliða :math:`r` af stigi
:math:`<m` og :math:`g\in {{\cal O}}({{\mathbb  C}})` þannig að

.. math::

  f(z)=r(z)+p(z)g(z), \qquad z\in {{\mathbb  C}}.

  

Margliðan :math:`r` er lausn á brúunarverkefninu. Bæði :math:`r` og
:math:`g` eru ótvírætt ákvörðuð og eru gefin með formúlunum

.. math::

  \begin{aligned}
   r(z)=f[\lambda_1]&+f[\lambda_1,\lambda_2](z-\lambda_1)+\cdots\\
   &+ f[\lambda_1,\dots,\lambda_m](z-\lambda_1)\cdots(z-\lambda_{m-1})\end{aligned}

og

.. math:: g(z)=f[\lambda_1,\dots,\lambda_m,z](z-\lambda_1)\cdots(z-\lambda_m),

þar sem :hover:`mismunakvótarnir,mismunakvóti` eru skilgreindir með

.. math::

  f[\lambda_i,\dots,\lambda_{i+j}]=
   \begin{cases}\dfrac{f^{(j)}(\lambda_i)}{j!},& 
   \lambda_i=\cdots=\lambda_{i+j}, \\
   \dfrac{f[\lambda_i,\dots,\lambda_{i+j-1}]-f[\lambda_{i+1},\dots,\lambda_{i+j}]}
   {\lambda_i-\lambda_{i+j}},&\lambda_i\neq \lambda_{i+j}, 
   \end{cases}


  

fyrir :math:`i=1,\dots,m` og :math:`j=0,\dots,m-i`.

--------------

Framsetningin á brúunarmargliðunni :math:`r`, sem við notum hér, er
kennd við Newton. Í þessari
útleiðslu höfum við gert ráð fyrir því að :math:`f` sé fágað á öllu
:math:`{{\mathbb  C}}`. En með því að huga vel að valinu á veginum sem
heildað er yfir, þá er hægt að sýna fram á að þessar formúlur gildi í
hvaða svæði sem er.

Newton-margliður
~~~~~~~~~~~~~~~~

Nú segir setning Cayley–Hamilton okkur að sérhvert veldi :math:`A^ n`
af :math:`m\times m` fylkinu :math:`A` með :math:`n\geq m` megi skrifa sem línulega samantekt af :math:`I,A,\dots, A^ {m-1}`,
og af því leiðir að fylkjafall :math:`f(A)`, sem gefið er með
samleitinni veldaröð, er í raun margliða í :math:`A` af stigi
:math:`\leq (m-1)`. Nú viljum við reikna út þessa margliðu og nota til þess
fallgildin :math:`f(z)`. Í tilfellinu :math:`m=4` þurfum við fyrst að
reikna út mismuakvótatöfluna

.. math::

  \begin{matrix}
   f[\lambda_1]\\
               &f[\lambda_1,\lambda_2]\\
   f[\lambda_2]&                       &f[\lambda_1, \lambda_2, \lambda_3]\\
           &f[\lambda_2,\lambda_3]& &f[\lambda_1,\lambda_2,\lambda_3,\lambda_4]\\
   f[\lambda_3]&                       &f[\lambda_2, \lambda_3, \lambda_4]\\
               &f[\lambda_3,\lambda_4]\\
   f[\lambda_4]
   \end{matrix}

þar sem :math:`\lambda_1,\dots,\lambda_4` er upptalning með margfeldni
á núllstöðvum kennimargliðu :math:`A`. Margliðan :math:`r(z)` er síðan
reiknuð út frá hornalínustökunum

.. math::

  \begin{aligned}
   r(z)&=f[\lambda_1]+f[\lambda_1,\lambda_2](z-\lambda_1)
   +f[\lambda_1, \lambda_2, \lambda_3](z-\lambda_1)(z-\lambda_2)\\
   &+f[\lambda_1, \lambda_2, \lambda_3,\lambda_4]
   (z-\lambda_1)(z-\lambda_2)(z-\lambda_3).\end{aligned}

Fylkið :math:`f(A)` fæst nú með því að stinga :math:`A` inn í formúluna
í stað breytunnar :math:`z` og setja :math:`I` inn í stað allra
fastaliða í margliðuþáttum,

.. math::

  \begin{aligned}
   f(A)&=f[\lambda_1]I+f[\lambda_1,\lambda_2](A-\lambda_1I)
   +f[\lambda_1, \lambda_2, \lambda_3](A-\lambda_1I)(A-\lambda_2I)\\
   &+f[\lambda_1, \lambda_2, \lambda_3,\lambda_4]
   (A-\lambda_1I)(A-\lambda_2I)(A-\lambda_3I).\end{aligned}

Veldisvísisfylkið
~~~~~~~~~~~~~~~~~

Við fórum út í þetta æfintýri til þes að reikna út margliðuna
:math:`e^{tA}`, sem byggir á fallinu :math:`f(z)=e^{tz}`, þar sem
:math:`t` er raunbreytistærð. Afleiðurnar eru

.. math::

  f{{^{\prime}}}(z)=te^{tz}, \qquad f{{^{\prime\prime}}}(z)=t^2e^{tz}, \qquad
   f{{^{\prime\prime\prime}}}(z)=t^3e^{tz}, \qquad \dots.

Margliðan :math:`p` verður síðan kennimargliða fylkisins :math:`A`.

  

Sýnidæmi
^^^^^^^^

\(i) Gerum ráð fyrir að :math:`A` sé :math:`2\times 2` fylki með ólík
eigingildi :math:`\alpha_1` og :math:`\alpha_2`. Þá er kennimargliðan
:math:`p_A(z)=(z-\alpha_1)(z-\alpha_2)` og mismunakvótataflan

.. math::

  \begin{matrix}
   e^{t\alpha_1}\\
   &\dfrac{e^{t\alpha_1}-e^{t\alpha_2}}{\alpha_1-\alpha_2}\\
   e^{t\alpha_2}
   \end{matrix}

og við fáum

.. math::

  e^{tz} = e^{t\alpha_1}+ 
   \dfrac{e^{t\alpha_1}-e^{t\alpha_2}}{\alpha_1-\alpha_2}
   (z-\alpha_1) +(z-\alpha_1)(z-\alpha_2)g(z),

sem gefur okkur formúluna fyrir :math:`e^{tA}`,

.. math::

  e^{tA}=e^{t\alpha_1}I+\dfrac{e^{t\alpha_1}-e^{t\alpha_2}}
   {\alpha_1-\alpha_2}(A-\alpha_1I).

\(ii) Ef hins vegar :math:`A` er :math:`2\times 2` fylki með aðeins eitt
eigingildi :math:`\alpha_1`, þá verður mismunakvótataflan

.. math::

  \begin{matrix}
   e^{t\alpha_1}\\
   &te^{t\alpha_1}\\
   e^{t\alpha_1}
   \end{matrix}

og við fáum

.. math::

  e^{tz}=e^{t\alpha_1}+te^{t\alpha_1}(z-\alpha_1)+(z-\alpha_1)^
   2g(z).

Veldisvísisfylkið verður því

.. math:: e^{tA}=e^{t\alpha_1}I+te^{t\alpha_1}(A-\alpha_1I).

\(iii) Ef :math:`A` er :math:`3\times 3` fylki með þrjú ólík eigingildi,
:math:`{\alpha}_1,{\alpha}_2,{\alpha}_3` þá verður mismunakvótataflan

.. math::

  \begin{matrix}
   e^{t{\alpha}_1}\\
   &\dfrac{e^{t\alpha_1}-e^{t\alpha_2}}{\alpha_1-\alpha_2}\\
   e^{t\alpha_2}& 
   &\dfrac1{\alpha_1-\alpha_3}\left\{
   \dfrac{e^{t\alpha_1}-e^{t\alpha_2}}{\alpha_1-\alpha_2}-
   \dfrac{e^{t\alpha_2}-e^{t\alpha_3}}{\alpha_2-\alpha_3}
   \right\}\\ 
   &\dfrac{e^{t\alpha_2}-e^{t\alpha_3}}{\alpha_2-\alpha_3}\\
   e^{t\alpha_3}\\
   \end{matrix}

og formúlan fyrir :math:`e^{tA}` verður

.. math::

  \begin{gathered}
   e^{tA}=e^{t\alpha_1}I+\dfrac{e^{t\alpha_1}-e^{t\alpha_2}}
   {\alpha_1-\alpha_2}(A-\alpha_1I)+\\
   +\dfrac1{\alpha_1-\alpha_3}\left\{
   \dfrac{e^{t\alpha_1}-e^{t\alpha_2}}{\alpha_1-\alpha_2}-
   \dfrac{e^{t\alpha_2}-e^{t\alpha_3}}{\alpha_2-\alpha_3}
   \right\} (A-\alpha_1I)(A-\alpha_2I).\end{gathered}

\(iv) Ef :math:`A` er :math:`3\times 3` fylki með tvö ólík eigingildi,
:math:`\alpha_1` tvöfalt og :math:`\alpha_2` einfalt, þá verður
mismunakvótataflan

.. math::

  \begin{matrix}
   e^{t\alpha_1}\\
   &te^{t\alpha_1}\\
   e^{t\alpha_1}& 
   &\dfrac1{\alpha_1-\alpha_2}\left\{te^{t\alpha_1}-
   \dfrac{e^{t\alpha_1}-e^{t\alpha_2}}{\alpha_1-\alpha_2}\right\}\\ 
   &\dfrac{e^{t\alpha_1}-e^{t\alpha_2}}{\alpha_1-\alpha_2}\\
   e^{t\alpha_2}\\
   \end{matrix}

og formúlan verður

.. math::

  e^{tA}=e^{t\alpha_1}I+te^{t\alpha_1}(A-\alpha_1I)+
   \dfrac1{\alpha_1-\alpha_2}\left\{te^{t\alpha_1}-
   \dfrac{e^{t\alpha_1}-e^{t\alpha_2}}{\alpha_1-\alpha_2}\right\}
   (A-\alpha_1I)^2.

\(v) Að lokum skulum við líta á tilfellið að :math:`A` sé
:math:`3\times 3` fylki með eitt eigingildi :math:`\alpha_1`.
Mismunakvótataflan verður þá einfaldlega

.. math::

  \begin{matrix}
   e^{t\alpha_1}\\
   &te^{t\alpha_1}\\
   e^{t\alpha_1}& 
   &\dfrac{t^2}{2}e^{t\alpha_1}\\ 
   &te^{t\alpha_1}\\
   e^{t\alpha_1}\\
   \end{matrix}

og veldisvísisfylkið verður

.. math::

  e^{tA}=e^{t\alpha_1}I+te^{t\alpha_1}(A-\alpha_1I)+
   \dfrac{t^2}2e^{t\alpha_1}(A-\alpha_1I)^2.

--------------

Hugsum okkur nú að við séum að finna lausn á upphafsgildisverkefninu
:math:`u{{^{\prime}}}=Au`, :math:`u(0)=b`, þar sem :math:`A` er
:math:`3\times 3` fylki með eitt eigingildi :math:`\alpha_1`. Formúlan í
sýnidæminu (v) hér að ofan gefur

.. math:: e^{tA}b=e^{t\alpha_1}b_0+te^{t\alpha_1}b_1+\dfrac {t^2}2e^{t\alpha_1}b_2

þar sem

.. math:: b_0=b, \qquad b_1=(A-\alpha_1I)b_0, \qquad b_2=(A-\alpha_1I)b_1.

Athugið að hér væri ákaflega heimskulegt að reikna fyrst út fylkið
:math:`(A-\alpha_1I)^2` og margfalda það síðan með :math:`b` til að fá
:math:`b_2`, því það kostar almennt margfalt meiri vinnu en við þurfum
að framkvæma í þeirri aðferð sem hér er lýst.
