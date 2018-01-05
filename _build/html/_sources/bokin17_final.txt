
Laplace-virkinn
===============

Inngangur
---------

Hlutafleiðuvirkinn

.. math::

  \Delta=\dfrac{\partial^2}{\partial x_1^2}
   +\cdots+\dfrac{\partial^2}{\partial x_n^2}

á :math:`{{\mathbb  R}}^n` nefnist *Laplace-virki*. Óhliðraða jafnan
:math:`\Delta u=0` nefnist *Laplace-jafna* og lausn :math:`u` á henni á
einhverju opnu mengi :math:`X\subset {{\mathbb  R}}^n` er sögð vera
*þýtt* eða *harmónískt* fall. Hliðraða jafnan :math:`\Delta u=f`, þar
sem :math:`f` er gefið fall á :math:`X` nefnist *Poisson-jafna*. Í einni
vídd er Laplace-jafnan einfaldlega :math:`u{{^{\prime\prime}}}=0` og
þýðu föllin á opnum bilum á :math:`{{\mathbb  R}}` eru því öll af
gerðinni :math:`u(x)=Ax+B`, þar sem :math:`A` og :math:`B` eru fastar.
Green-fall virkjans :math:`\Delta=d^2/dx^2` er fallið
:math:`G(x,\xi)=x-\xi`.

Í þessum kafla ætlum við að fjalla um aðferðir til þess að leysa
Laplace- og Poisson-jöfnurnar með jaðarskilyrðum á nokkrum tegundum
mengja í tví- og þrívíðu rúmi. Mikilvægi Laplace- og Poisson-jafnanna
hefur komið skýrt fram í sýnidæmum hjá okkur, þar sem við fjölluðum um
rafstöðufræði og æstæð varmaleiðniverkefni.

Í tveimur víddum munum við stundum tákna óháðu breyturnar með
:math:`(x,y)` í stað :math:`(x_1,x_2)` og skrifa þær á tvinntalnaformi
:math:`z=x+iy` og á pólformi :math:`z=re^{i\theta}`. Í tveimur víddum
koma fram sterk tengsl við fáguð föll. Það byggir á þeirri staðreynd að
raun- og þverhluti fágaðs falls eru þýð föll og samskeyting á þýðu og
fáguðu falli er þýtt fall.

Meginverkefnið í þessum kafla er að leiða út heildunarframsetningu á
lausn Poisson-jöfnunnar :math:`\Delta u=f` á opnu mengi :math:`X` með
Dirichlet-jaðarskilyrði :math:`u={\varphi}` á :math:`{\partial}X`, en
hún er

.. math::

  u(x)=\int_{{\partial}X} P_X(x,{\xi}){\varphi}({\xi})\, dS({\xi}) +
   \int_X G_X(x,{\xi}) f({\xi})\, d{\xi},

þar sem :math:`P_X` nefnist *Poisson-kjarni* fyrir svæðið :math:`X` og
:math:`G_X` nefnist *Green-fall* eða *Green-kjarni* fyrir svæðið
:math:`X`. Fyrra heildið gefur þýtt fall sem uppfyllir jaðarskilyrðin og
það síðara gefur lausn á Poisson-jöfnunni með óhliðruðum jaðarskilyrðum.

Þýð föll og fágaðar varpanir
----------------------------

Þýð föll og fágaðar varpanir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Það er mikill skyldleiki með fáguðum og þýðum föllum. Til þess að sjá
hver hann er, skulum við láta :math:`f` vera fágað fall á opnu hlutmengi
:math:`X` í :math:`{{\mathbb  C}}={{\mathbb  R}}^2` og skrifa
:math:`u={{\operatorname{Re\, }}}f` og
:math:`v={{\operatorname{Im\, }}}f`. Þá eru föllin :math:`u` og
:math:`v` í :math:`C^{\infty}(X)` og þau uppfylla
Cauchy-Riemann-jöfnurnar :math:`{\partial}_xu={\partial}_yv` og
:math:`{\partial}_yu=-{\partial}_xv`. Þar með fáum við að

.. math::

  \Delta u={\partial}_x^2u+{\partial}_y^2u=
   {\partial}_x{\partial}_yv+{\partial}_y(-{\partial}_x v)=0

og

.. math::

  \Delta v={\partial}_x^2v+{\partial}_y^2v=
   {\partial}_x(-{\partial}_yu)+{\partial}_y{\partial}_x u=0.

Hér höfum við notfært okkur að blönduðu afleiðurnar uppfylla
:math:`\partial_x\partial_y u=\partial_y\partial_x u` og
:math:`\partial_x\partial_y v=\partial_y\partial_x v`. Þar með eru bæði
föllin :math:`u` og :math:`v` þýð.

Rifjum upp að Wirtinger-virkjarnir eru

.. math::

  {\partial}_z=\dfrac{{\partial}}{{\partial} z}
   =\tfrac 12\big({\partial}_x-i{\partial}_y\big) \quad \text{ og } \quad
   {\partial}_{\overline z}=\dfrac{\partial}{\partial\overline z}
   =\tfrac 12\big({\partial}_x+i{\partial}_y\big).

Með beinum útreikningi fáum við að

.. math::

  \Delta = 4\dfrac{\partial^2}{\partial z\partial\bar z}
   =4\dfrac{\partial^2}{\partial \bar z\partial z}.

Hugsum okkur nú að :math:`u` sé þýtt fall á :math:`X` og að við viljum
kanna hvort til sé :math:`f\in {{\cal A}}(X)` þannig að
:math:`u={{\operatorname{Re\, }}}f`. Þá gildir
:math:`u=\frac 12\big(f+\overline f\big)`. Nú er fall :math:`f` fágað þá
og því aðeins að :math:`\partial_{\overline  z}f=0` og þar með segir
jafnan :math:`\partial_{\overline  z}\partial_zu=\frac 14 \Delta  u=0` okkur að fallið :math:`\partial_zu`
sé fágað. Við höfum að

.. math::

  \partial_z u=\tfrac 12\big(\partial_z f+\partial_z \overline f\big)
   =\tfrac 12\big(\partial_z f+\overline{\partial_{\overline z} f}\big) 
   = \tfrac 12 f{{^{\prime}}}.

(Hér höfum við notað reikniregluna :math:`{\partial}_z\overline f =\overline{({\partial}_{\overline z}f)}`
og að fyrir fágað fall :math:`f` er
:math:`{\partial}_zf=f{{^{\prime}}}`.) Út úr þessari jöfnu lesum við
að :math:`f` er stofnfall :math:`2\partial_z u`. Nú er tilvist á
stofnfalli háð því hvernig svæðið :math:`X` lítur út. Rifjum upp að sérhvert fágað fall á stjörnusvæði hefur stofnfall 
og að svæði :math:`X` er einfaldlega
samanhangandi þá og því aðeins að sérhvert fall í :math:`{{\cal A}}(X)`
hafi stofnfall:

Setning
^^^^^^^

Ef :math:`X` er opið mengi í :math:`{{\mathbb  C}}` og
:math:`f\in {{\cal A}}(X)`, þá eru :math:`{{\operatorname{Re\, }}}f` og
:math:`{{\operatorname{Im\, }}}f` þýð föll á :math:`X`. Ef
:math:`u:X\to {{\mathbb  R}}` er þýtt fall á einfaldlega samanhangandi
svæði, þá er til :math:`f\in {{\cal A}}(X)` þannig að
:math:`u={{\operatorname{Re\, }}}f`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Fyrstu staðhæfinguna höfum við sannað. Fyrst
:math:`\partial_{\overline z}\partial_z u=0`, þá er
:math:`2\partial_z u` fágað. Látum :math:`g` vera stofnfall
:math:`2\partial_z u` og skrifum :math:`g=\varphi+i\psi`, þar sem
:math:`\varphi` og :math:`\psi` eru raun- og þverhluti :math:`g`. Þá
gildir

.. math::

  2\partial_zu = \dfrac{\partial u}{\partial x}
   -i\dfrac{\partial u}{\partial y}
   =g{{^{\prime}}}= \dfrac{\partial \varphi}{\partial x}
   +i\dfrac{\partial \psi}{\partial x}
   = \dfrac{\partial \varphi}{\partial x}
   -i\dfrac{\partial \varphi}{\partial y}.

Þessi jafna segir okkur að
:math:`{{\operatorname{grad}}}u={{\operatorname{grad}}}\varphi` og þar
með er :math:`u=\varphi+c`, þar sem :math:`c\in {{\mathbb  R}}` er
fasti. Við setjum nú :math:`f=g+c`.

.. end-toggle::

Ef :math:`u` er þýtt fall á svæði :math:`X` og :math:`X` er ekki
einfaldlega samanhangandi, þá er alls ekki víst að :math:`2\partial_z u`
hafi stofnfall. Sem dæmi getum við tekið:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Fallið :math:`u(z)=\ln |z|=\ln r`, :math:`r=\sqrt{x^2+y^2}`, er þýtt á
:math:`{{\mathbb  C}}\setminus {{\{0\}}}`. Það er ekki til neitt fágað
fall :math:`f` á öllu :math:`{{\mathbb  C}}\setminus {{\{0\}}}` þannig
að :math:`u={{\operatorname{Re\, }}}f`, því slíkt fall væri þá fágaður
logri, en enginn slíkur er til á þessu mengi. Hins vegar er ljóst að við
getum skilgreint logra á hlutmengjum af :math:`{{\mathbb  C}}\setminus {{\{0\}}}`, til dæmis :math:`f(z)={{\operatorname{Log}}}z`,
:math:`f\in {{\cal A}}({{\mathbb  C}}\setminus {{\mathbb  R}}_-)`, þar
sem :math:`{{\operatorname{Log}}}` táknar höfuðgrein lograns.

.. end-toggle::

Gerum nú ráð fyrir að :math:`v` sé eitthvert deildanlegt fall á opnu
mengi :math:`Y` í :math:`{{\mathbb  C}}`, að :math:`F:X\to Y` sé
deildanleg vörpun og setjum :math:`u(z)=v(F(z))`. Við táknum breytuna í
:math:`Y` með :math:`\zeta` og skrifum :math:`\zeta=F(z)`. Keðjureglan í
tvinnbreytunum :math:`z` og :math:`\zeta` verður þá

.. math::

  \begin{aligned}
   \dfrac{\partial u}{\partial z}(z)
   &=\dfrac{\partial v}{\partial \zeta}({\zeta})
   \dfrac{\partial F}{\partial z}(z)
   +\dfrac{\partial v}{\partial\overline\zeta}({\zeta})
   \dfrac{\partial \overline F}{\partial z}(z),
   \\
   \dfrac{\partial u}{\partial \overline z}(z)
   &=\dfrac{\partial v}{\partial \zeta}({\zeta})
   \dfrac{\partial F}{\partial \overline z}(z)
   +\dfrac{\partial v}{\partial\overline \zeta}({\zeta})
   \dfrac{\partial  \overline F}{\partial \overline z}(z).\end{aligned}

Ef :math:`F` er fágað fall, þá er
:math:`\partial F/\partial\overline z=0` og
:math:`\partial \overline F/\partial z=\overline{\partial F/\partial \overline z}=0` og þessar jöfnur einfaldast í

.. math::

  \dfrac{\partial u}{\partial z}(z)
   =\dfrac{\partial v}{\partial \zeta}({\zeta})
   \dfrac{\partial F}{\partial z}(z)
   \qquad \text{ og } \qquad 
   \dfrac{\partial u}{\partial \overline z}(z)
   =\dfrac{\partial v}{\partial\overline\zeta}({\zeta})
   \dfrac{\partial  \overline F}{\partial \overline z}(z)

og Leibniz-reglan gefur okkur

.. math::

  \tfrac 14 \Delta u(z)= \dfrac{\partial^2u}{\partial\bar z\partial z}(z)
   =\bigg(
   \dfrac{\partial^2 v}{\partial\zeta^2}({\zeta})
   \dfrac{\partial F}{\partial\bar z}(z)
   +\dfrac{\partial^2 v}{\partial\bar \zeta\partial \zeta}({\zeta})
   \dfrac{{\partial}\overline F}{\partial \bar z}(z)
   \bigg) \dfrac{\partial F}{\partial z}(z)
   +\dfrac{\partial v}{\partial \zeta}({\zeta})
   \dfrac{\partial^2 F}{\partial \bar z\partial z}(z).

Nú notfærum við okkur að :math:`\partial F/\partial \overline z =\partial^2 F/\partial \overline z\partial z=0` og
:math:`\partial\overline F/\partial\overline z=\overline{\partial F/\partial z}=\overline{F{{^{\prime}}}}` og höfum því

.. math:: \Delta_z u(z)=\Delta_\zeta v({\zeta})\big |F{{^{\prime}}}(z)\big|^2.

Af þessari jöfnu leiðir síðan:

Setning
^^^^^^^

Látum :math:`X` og :math:`Y` vera svæði í
:math:`{{\mathbb  C}}={{\mathbb  R}}^2`, :math:`F:X\to Y` vera fágaða
vörpun sem er ekki föst, :math:`v:Y\to {{\mathbb  C}}` og
:math:`u=v(F)`. Fallið :math:`u` er þýtt þá og því aðeins að :math:`v`
sé þýtt.

--------------

Með þessa setningu að vopni er oft hægt að flytja upplýsingar um þýð
föll á :math:`Y` yfir á þýð föll á svæðinu :math:`X` með vörpuninni
:math:`F`. Til þess að útskýra þetta skulum við hugsa okkur að við
viljum leysa Dirichlet-verkefnið

.. math::

  \Delta u= 0 \quad \text{ á } \quad X\qquad \text { og } \qquad
   u=\varphi  \quad \text{ á } \quad \partial X,

þar sem :math:`\varphi` er gefið samfellt fall á jaðrinum
:math:`\partial X` og gefum okkur einnig að hægt sé að framlengja fallið
:math:`F` þannig að það verði samfellt og gagntækt frá lokuninni
:math:`\overline X= X\cup \partial X` yfir á lokunina
:math:`\overline Y=Y\cup \partial Y` og táknum andhverfuna með
:math:`F^{[-1]}`, :math:`z=F^{[-1]}(\zeta)`. Gefum okkur einnig að við
getum alltaf leyst verkefnið

.. math::

  \Delta v= 0  \quad \text { á  } \quad Y \qquad \text{ og } \qquad
   v=\psi  \quad \text{ á }  \quad \partial Y,

þar sem :math:`\psi` er gefið samfellt fall á jaðrinum
:math:`\partial Y`. Ef við setjum einfaldlega
:math:`\psi(\zeta)=\varphi(F^{[-1]}(\zeta))`, fyrir
:math:`\zeta\in \partial Y`. Þá leiðir beint af 

.. math:: \Delta_z u(z)=\Delta_\zeta v({\zeta})\big |F{{^{\prime}}}(z)\big|^2

að lausn :math:`u` á Dirichlet-verkefninu á :math:`X` 
er gefin með :math:`u(z)=v(F(z))`, þar sem
:math:`v` er lausnin á Dirichlet-verkefninu á :math:`Y`.

Af tilvist á vörpuninni :math:`F` er það að segja, að til er setning,
sem nefnist *vörpunarsetning Riemanns* og hún segir að um sérhvert
einfaldlega samanhangandi svæði :math:`X\neq {{\mathbb  C}}` gildir að
til er gagntæk fáguð vörpun :math:`F:X\to \Bbb E`, þar sem
:math:`\Bbb E` táknar opnu einingarskífuna. Ef :math:`X` hefur samfellt
deildanlegan jaðar, þá fæst jafnframt að hægt er að framlengja :math:`F`
yfir í samfellda gagntæka vörpun :math:`F:\overline X\to \overline {\Bbb E}`. Það er erfitt að sanna vörpunarsetningu
Riemanns. Sönnunin er hrein tilvistarsönnun og gefur ekki neina formúlu
fyrir :math:`F`. Fyrir viss svæði er hins vegar auðvelt að ákvarða
vörpunina :math:`F`:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Brotna línulega vörpunin :math:`\zeta=F(z)=(z-i)/(z+i)` varpar efra
hálfplaninu :math:`\Bbb H_+=\{z; {{\operatorname{Im\, }}}z>0\}` á
einingarhringinn :math:`\Bbb E`. Til þess að sjá það, þá athugum við
fyrst að hún uppfyllir

.. math:: F(\infty)=1, \qquad F(0)=-1, \quad \text {  og } \quad F(1)=-i.

Punktarnir :math:`0` og :math:`1` ákvarða línuna :math:`{{\mathbb  R}}`
ótvírætt og við vitum að :math:`F` varpar línu á hring eða línu. Fyrst hún varpar :math:`\infty` á :math:`1`, þá
varpast :math:`{{\mathbb  R}}` á hring. Nú eru punktarnir :math:`1`,
:math:`-1` og :math:`-i` á einingarhringnum, svo
:math:`F({{\mathbb  R}}\cup\{\infty\})=\partial \Bbb E`. Nú er
:math:`F(i)=0` og því varpast efra hálfplanið á opnu skífuna
:math:`\Bbb E`.

.. end-toggle::

Poisson-formúlan á hringskífu
-----------------------------

Poisson-formúlan á hringskífu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessari grein höldum við áfram með Dirichlet-verkefnið fyrir
Laplace-virkjann á skífunni :math:`D_a=\{(x,y); x^2+y^2<a^2\}`,

.. math::

  \Delta u= 0  \quad \text { á  } \quad D_a
   \qquad \text{ og } \qquad
   u={\varphi}   \quad \text{ á }  \quad \partial D_a.

Hér er :math:`\varphi` gefið fall á jaðri hringskífunnar
:math:`{\partial}D_a`. Lausnina fundum við í kaflanum um raðalausnir á hlutafleiðujöfnum með því að
innleiða pólhnit og skilgreina
:math:`v(r,\theta)=u(r\cos \theta,r\sin \theta)` og
:math:`{\psi}(\theta)=\varphi(a\cos \theta,a\sin \theta)`. Lausnin er
gefin með formúlunni

.. math::

  v(r,\theta)=\sum\limits_{n=-\infty}^{+\infty}
   c_n({\psi}) \bigg(\dfrac r a\bigg)^{|n|}e^{in\theta}.

Við stingum nú skilgreiningunni á Fourier-stuðlum fallsins :math:`\psi`
inn í óendanlegu summuna og skiptum á röð heildis og summu,

.. math::

  \begin{aligned}
   v(r,\theta)&=\sum\limits_{n=-\infty}^{+\infty}
   \bigg(\dfrac 1{2{\pi}} \int_{-{\pi}}^{\pi} {\psi}(t)e^{-int}\,
   dt\bigg) 
    \bigg(\dfrac r a\bigg)^{|n|}e^{in\theta}\\
   &=\int_{-{\pi}}^{\pi}
   \bigg(\dfrac 1{2{\pi}}
   \sum\limits_{n=-\infty}^{+\infty}  
   \bigg(\dfrac r a\bigg)^{|n|}e^{in(\theta-t)}\bigg) {\psi}(t)\, dt.\end{aligned}

Við skilgreinum *Poisson-kjarnann fyrir skífuna*
:math:`D_a=\{x+iy=re^{i{\theta}}; r<a\}` með

.. math::

  \begin{aligned}
   P_{D_a}(r,{\theta})
   &=\dfrac 1{2{\pi}}
   \sum\limits_{n=-\infty}^{+\infty}  
   \bigg(\dfrac r a\bigg)^{|n|}e^{in\theta}\\
   &=\dfrac 1{2{\pi}}\bigg(1+
   \sum\limits_{n=1}^{\infty}  \bigg(\dfrac r a\bigg)^{n}e^{in\theta}
   +\sum\limits_{n=1}^{\infty}  \bigg(\dfrac r a\bigg)^{n}e^{-in\theta}
   \bigg)\nonumber\\
   &=\dfrac 1{2{\pi}}\bigg(1+
   \dfrac{\big(r/a\big)e^{i{\theta}}}{1-\big(r/a\big)e^{i{\theta}}}
   +\dfrac{\big(r/a\big)e^{-i{\theta}}}{1-\big(r/a\big)e^{-i{\theta}}}
   \bigg)\nonumber\\
   &=\dfrac 1{2{\pi}}\bigg(1+
   \dfrac{re^{i{\theta}}}{a-re^{i{\theta}}}
   +\dfrac{re^{-i{\theta}}}{a-re^{-i{\theta}}}
   \bigg)\nonumber\\
   &=\dfrac{a^2-r^2}{2{\pi}(a^2-2ar\cos {\theta}+r^2)}.\nonumber\end{aligned}

Við getum því sett lausnina fram sem heildi,

.. math::

  \begin{aligned}
   v(r,{\theta})
   &=\int_{-{\pi}}^{{\pi}} P_{D_a}(r,{\theta}-t){\psi}(t)\, dt\\
   &=\dfrac{a^2-r^2}{2{\pi}}
   \int_{-{\pi}}^{{\pi}}\dfrac{{\psi}(t)}{a^2-2ar\cos ({\theta}-t)+r^2}
   \, dt.\nonumber\end{aligned}

Þessi formúla nefnist *Poisson-formúla* fyrir hringskífuna :math:`D_a`.
Ef við stingum inn rétthyrndum hnitum
:math:`z=(x,y)=x+iy=re^{i{\theta}}`, þá verður lausnarformúlan fyrir
Dirichlet-verkefninu á einingarskífunni,

.. math::

  u(z)=\dfrac{a^2-|z|^2}{2{\pi}}\int_{-{\pi}}^{\pi}
   \dfrac{\varphi(ae^{it})}{|z-ae^{it}|^2}\, dt.

Nú athugum við að bogalengdarfrymið á hringnum :math:`{\partial}D_a` er
:math:`ds=a\, dt`, þegar hann er stikaður með
:math:`t\mapsto {\zeta}=ae^{it}` og því getum við umritað
lausnarformúluna yfir í heildi yfir :math:`{\partial} D_a` með tilliti
til bogalengdarinnar,

.. math::

  u(z)=\dfrac{a^2-|z|^2}{2{\pi}a}\int_{{\partial}D_a}
   \dfrac{\varphi({\zeta})}{|z-{\zeta}|^2}\, ds({\zeta}).

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Látum nú :math:`X` tákna svæðið, sem takmarkast af *hjartaferlinum*
:math:`r=2(1+\cos\theta)`, þ.e.
:math:`X=\{z=re^{i\theta}; r<2(1+\cos \theta), -\pi\leq \theta \leq \pi\}`,
og hugsum okkur að við viljum leysa verkefnið

.. math::

  \Delta u=0 \quad \text { á } \quad X \qquad \text { og  } \quad
   u=\varphi \quad \text{ á } \quad \partial X,

þar sem :math:`\varphi` er gefið samfellt fall á jaðrinum
:math:`\partial X`. Til þess að beita aðferðinni, sem lýst er í næstu grein hér fyrir ofan, 
þá þurfum við að finna fágaða vörpun :math:`F`, sem varpar
:math:`\overline X` gagntækt á :math:`\overline {\Bbb E}`.

.. figure:: ./myndir/fig171.svg
    :align: center
    :alt: Hjartaferill.

    Mynd: Hjartaferill.

Slík vörpun reynist vera :math:`\zeta=F(z)=z^{\frac 12 }-1`, þar sem
:math:`z\mapsto z^{\frac 12}` táknar höfuðgrein kvaðratrótarinnar.
Vörpunin :math:`F` er gagntæk og andhverfa hennar er
:math:`z=F^{[-1]}(\zeta)=(\zeta+1)^2`. Til þess að sjá að
:math:`\partial X` varpist á einingarhringinn :math:`\partial \Bbb E`,
þá tökum við punkt á jaðrinum :math:`z=re^{i\theta}` með
:math:`r=2(1+\cos\theta)=4\cos^2(\theta/2)`. Hann uppfyllir

.. math:: z^{\frac 12}-1=2\cos(\theta/2)e^{i\theta/2}-1

og því er

.. math::

  \begin{aligned}
   |z^{\frac 12}-1|^2
   &=4\cos^2(\theta/2)+1-2{{\operatorname{Re\, }}}\big(2\cos(\theta/2)e^{i\theta/2}\big)\\
   &=4\cos^2(\theta/2)+1-4\cos^2(\theta/2)=1.\end{aligned}

Þar með sjáum við að :math:`F` varpar :math:`\partial X` gagntækt á
:math:`\partial\Bbb E`. Nú lítum við á verkefnið

.. math::

  \Delta v=0 \quad \text { á } \quad \Bbb E \qquad \text { og  } \quad
   v(\zeta)=\varphi((\zeta+1)^2), \quad \zeta\in \partial\Bbb E.

Lausn þess er gefin með Poisson-formúlunni,

.. math::

  v(\zeta)=\dfrac{1-|\zeta|^2}{2{\pi}}\int_{-\pi}^{\pi}
   \dfrac{\varphi((e^{it}+1)^2)}{|\zeta-e^{it}|^2}\, dt,

og þar með er lausnin :math:`u` á Dirichlet-verkefninu í hjartanu gefin með

.. math::

  u(z)=\dfrac{1-|z^{\frac 12}-1|^2}{2{\pi}}\int_{-\pi}^{\pi}
   \dfrac{\varphi((e^{it}+1)^2)}{|z^{\frac 12}-1-e^{it}|^2}\, dt.

.. end-toggle::

Ef við stingum :math:`z=0` inn í 

.. math::

  u(z)=\dfrac{a^2-|z|^2}{2{\pi}a}\int_{{\partial}D_a}
   \dfrac{\varphi({\zeta})}{|z-{\zeta}|^2}\, ds({\zeta}).

og notfærum okkur að
:math:`|{\zeta}|=a` ef :math:`{\zeta}\in {\partial}D_a`, þá fáum við

.. math::

  u(0)=\dfrac 1{2{\pi} a}\int_{{\partial}D_a} \varphi({\zeta})\,
   ds({\zeta}).

Bein afleiðing af þessari formúlu er:

Setning
^^^^^^^

(*Meðalgildissetning*).   Látum :math:`u` vera þýtt fall á opinni
hringskífu :math:`S({\alpha},{\varrho})` og gerum ráð fyrir að :math:`u`
sé samfellt á lokuninni :math:`\overline S({\alpha},{\varrho})`. Þá er

.. math::

  u({\alpha})=\dfrac 1{2{\pi} {\varrho}} 
   \int_{{\partial}S({\alpha},{\varrho})} u({\zeta})\, ds({\zeta})
   =\dfrac 1{2{\pi}}\int_0^{2{\pi}}u({\alpha}+{\varrho}e^{it})\, dt,

þ.e. gildi fallsins :math:`u` í miðpunkti skífunnar er jafnt meðalgildi
þess yfir jaðarinn.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við beitum formúlunni fyrir framan setninguna á fallið :math:`v(z)=u({\alpha}+z)` með
:math:`{\varphi}(z)=u({\alpha}+z)`.

.. end-toggle::

Poisson-formúlan á hálfplani
----------------------------

Poisson-formúlan á hálfplani
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við láta :math:`\Bbb H_+` tákna efra hálfplanið,
:math:`\Bbb H_+=\{(x,y); x\in{{\mathbb  R}}, y>0\}`, og lítum á
Dirichlet-verkefnið

.. math::

  \Delta u= 0  \quad \text { á  } \quad \Bbb H_+
   \qquad \text{ og } \qquad
   u={\varphi}   \quad \text{ á }  \quad  {{\mathbb  R}},

þar sem :math:`\varphi` er gefið fall á :math:`{{\mathbb  R}}`. Við
skulum leiða út lausnarformúlu fyrir þetta verkefni með því að beita
Fourier-ummyndun. Til þess þurfum við að gera ráð fyrir að
:math:`\varphi` sé heildanlegt og að :math:`u(x,y)` sé heildanlegt sem
fall af :math:`x` fyrir sérhvert :math:`y>0`. Við látum þá
:math:`\widehat u(\xi,y)` tákna Fourier-mynd :math:`u` með tilliti til
:math:`x`,

.. math::

  \widehat u(\xi,y)
   ={{\cal F}}\{u(\cdot,y)\}(\xi)
   =\int_{-\infty}^{+\infty}e^{-ix\xi}u(x,y)\, dx

og gefum okkur að allar forsendur í helstu reiknireglum um
Fourier-ummyndunina séu uppfylltar, þannig að

.. math::

  {{\cal F}}\{\partial_x^ku(\cdot,y)\}(\xi)=(i\xi)^k\widehat u(\xi,y)
   \qquad \text{ og } \qquad
   {{\cal F}}\{\partial_y^ku(\cdot,y)\}(\xi)=\partial_y^k\widehat u(\xi,y).

Eftir Fourier-ummyndun af öllum liðum verkefnisins fæst
að :math:`\widehat u(\xi,y)` þarf að uppfylla

.. math::

  \begin{cases}
   -\xi^2\widehat u(\xi,y)+\partial_y^2\widehat u(\xi,y)=0, 
   &\xi\in{{\mathbb  R}}, \ y>0,\\
   \widehat u(\xi,y)=\widehat \varphi(\xi), &\xi\in {{\mathbb  R}},\\
   \widehat u(\xi,y) \text{ er takmarkað}, &y\to +\infty.
   \end{cases}

Fyrir fast :math:`\xi` er þetta annars stigs jafna í :math:`y`. Almenn
lausn hennar er af gerðinni

.. math::

  \widehat u(\xi,y)=\begin{cases}
   A(\xi)e^{-|\xi|y}+B(\xi)e^{|\xi|y}, &\xi\neq 0,\\
   A(0)+B(0)y, &\xi=0.
   \end{cases}

Til þess að :math:`\widehat u(\xi,y)` haldist takmarkað ef
:math:`y\to +\infty`, þá verður :math:`B(\xi)=0` að gilda um öll
:math:`\xi\in {{\mathbb  R}}`. Þar með er
:math:`A(\xi)=\widehat\varphi(\xi)` og við höfum formúluna

.. math:: \widehat u(\xi,y)=e^{-|\xi|y} \widehat{\varphi}(\xi).

Hægri hliðin í þessari jöfnu er margfeldi tveggja Fourier-mynda og því
getum við skrifað :math:`u(x,y)` sem földun tveggja falla ef við getum
reiknað út andhverfu Fourier-mynd fallsins
:math:`\xi\mapsto e^{-|\xi|y}`. Það er auðvelt, því í 
:ref:`sýnidæmi <synokkurfouriersynidaemi>`
sýndum við fram á að :math:`{{\cal F}}\{e^{-|\xi|y}\}(x)=2y/(x^2+y^2)`
og þar með gefur andhverfuformúlan að
:math:`{{\cal F}}\{P_{\Bbb H_+}(\cdot,y)\}(\xi)=e^{-|\xi|y}` þar sem
:math:`P_{\Bbb H_+}` er *Poisson-kjarninn fyrir efra hálfplanið*,

.. math::

  P_{\Bbb H_+}(x,y)=\dfrac{y}{\pi(x^2+y^2)}, \qquad (x,y) \in
   {{\mathbb  R}}^2\setminus{{\{(0,0)\}}}.

Földunarreglan fyrir Fourier-myndir gefur okkur nú lausnarformúluna

.. math::

  u(x,y)=P_{\Bbb H_+}(\cdot,y)\ast \varphi(x)=\dfrac y\pi\int_{-\infty}^{+\infty}
   \dfrac{\varphi(t)}{(x-t)^2+y^2}\, dt.

Þessi formúla nefnist *Poisson-formúla á efra hálfplaninu*. Í útleiðslu
okkar á lausnarformúlunni gengum við út frá því að fallið :math:`\varphi`
væri heildanlegt, en Poisson-formúlan gildir ef við gerum ráð fyrir að
:math:`\varphi` sé samfellt og takmarkað á :math:`{{\mathbb  R}}`.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Dirichlet-verkefnið á fjórðungi

Nú þegar við þekkjum lausnarformúluna fyrir Dirichlet-verkefnið á
hálfplani, þá er auðvelt að beita aðferðinni sem lýst er í lok greinarinnar um þýð föll og fágaðar varpanir hér að framan
til þess að leysa hliðstætt verkefni á fjórðungi af planinu,

.. math::

  \begin{cases}
   \Delta u=0, &x>0, \ y>0,\\
   u(x,0)=\varphi_1(x), &x\geq 0,\\
   u(0,y)=\varphi_2(y), &y\geq 0,
   \end{cases}

þar sem föllin :math:`\varphi_1` og :math:`\varphi_2` eru samfelld á
:math:`{{\mathbb  R}}_+` og :math:`\varphi_1(0)=\varphi_2(0)`. Við látum
:math:`X=\{z=x+iy; x>0, y>0\}` tákna fjórðunginn og
:math:`Y=\{\zeta=\xi+i\eta; \eta>0\}` tákna efra hálfplanið. Fallið
:math:`F`, sem gefið er með

.. math:: \zeta=\xi+i\eta=F(z)=z^2=x^2-y^2+2ixy,

skilgreinir gagntæka vörpun frá :math:`\overline X` á
:math:`\overline Y`. Við skilgreinum nú samfellda fallið :math:`\psi` á
:math:`{{\mathbb  R}}` með

.. math::

  \psi({\xi})=\begin{cases}
   \varphi_1(\sqrt {\xi}), &{\xi}\geq 0,\\ 
   \varphi_2(\sqrt{-{\xi}}), &{\xi}<0.\end{cases}

Nú látum við :math:`v` tákna lausnina á :math:`\Delta v=0` á :math:`Y`
með jaðargildin :math:`v(\xi,0)={\psi}(\xi)` ef
:math:`\xi\in {{\mathbb  R}}`. Samkvæmt Poisson-formúlunni
fyrir efra hálfplan er

.. math::

  v(\zeta)=\dfrac \eta\pi\int_{-\infty}^{+\infty}
   \dfrac{{\psi}(t)\, dt}{(\xi-t)^2+\eta^2}, \qquad \zeta=\xi+i\eta\in Y.

Nú setjum við inn :math:`\xi=x^2-y^2` og :math:`\eta=2xy` samkvæmt
formúlunni hér að framan og fáum þá lausnarformúlu fyrir Dirichlet-verkefni á fjórðungi,

.. math::

  u(z)=\dfrac {2xy}\pi
   \int_0^{+\infty} \bigg(
   \dfrac{\varphi_1(\sqrt t)}
   {(x^2-y^2-t)^2+4x^2y^2}
   +\dfrac{\varphi_2(\sqrt t)}
   {(x^2-y^2+t)^2+4x^2y^2}
   \bigg)\, dt.

.. end-toggle::

Green-formúlurnar
-----------------

Green-formúlurnar
~~~~~~~~~~~~~~~~~

Látum nú :math:`X` vera opið hlutmengi í :math:`{{\mathbb  R}}^2` og
látum :math:`D` vera takmarkað hlutsvæði í :math:`X` með jaðar
:math:`{\partial}D`, sem er samfellt deildanlegur á köflum og
innihaldinn í :math:`X`. Ef :math:`\vec F:X\to {{\mathbb  R}}^2` er
samfellt deildanlegt vigursvið á :math:`X`, þá gefur Gauss-setningin

.. math::

  \iint_D \nabla\cdot\vec F \, dA = \int_{{\partial}D} \vec F\cdot \vec n \,
   ds,

þar sem :math:`\nabla\cdot={{\operatorname{div}}}` er
sundurleitnivirkinn, :math:`dA` er flatarmálsfrymið á
:math:`{{\mathbb  R}}^2`, :math:`\vec n` táknar ytri þvervigurinn á
jaðrinum og :math:`ds` er bogalengdarfrymið á jaðrinum. Með því að beita
Gauss-setningunni á sértilfellið :math:`\vec F=v \nabla  u` þar sem
:math:`u,v\in C^2(X)` og :math:`\nabla={{\operatorname{grad}}}` er
stigullinn, þá fáum við *fyrstu formúlu Greens*,

.. math::

  \int_{{\partial} D} v\dfrac{\partial u}{\partial n} \, ds
   =\iint_D \nabla v\cdot \nabla u\, dA 
   +\iint_D v \Delta  u\, dA.

Hér er :math:`{\partial}u/{\partial}n=\nabla u\cdot \vec n`
stefnuafleiða :math:`u` í stefnu ytri þvervigursins á jaðrinum. Ef við
skiptum á hlutverkum :math:`u` og :math:`v`, þá fáum við

.. math::

  \int_{{\partial} D} u\dfrac{\partial v}{\partial n} \, ds
   =\iint_D \nabla u\cdot \nabla v\, dA
   +\iint_D u \Delta  v\, dA.

Tökum nú mismuninn af þessum tveimur jöfnum. Þá fáum við *aðra formúlu
Greens*,

.. math::

  \int_{{\partial} D} \bigg(u\dfrac{\partial v}{\partial n}
   -v\dfrac{\partial u}{\partial n}\bigg) \, ds
   =\iint_D \big(u \Delta  v-v\Delta u\big) \, dA.

Þessar formúlur eiga sér hliðstæður í þremur víddum. Þá látum við
:math:`X` vera opið hlutmengi í :math:`{{\mathbb  R}}^3` og látum
:math:`D` vera takmarkað hlutsvæði í :math:`X` með jaðar
:math:`{\partial}D` innihaldinn í :math:`X`. Við gefum okkur að jaðarinn
sé samfellt deildanlegur flötur. Ef :math:`\vec F:X\to {{\mathbb  R}}^3`
er samfellt deildanlegt vigursvið á :math:`X`, þá gefur Gauss-setningin

.. math::

  \iiint_D \nabla\cdot \vec F \, dV 
   = \iint_{{\partial}D} \vec F\cdot \vec n \, dS,

þar sem :math:`dV` er rúmmálsfrymið í :math:`{{\mathbb  R}}^3`,
:math:`\vec n` táknar ytri þvervigurinn á jaðrinum og :math:`dS` er
flatarmálsfrymið á jaðrinum. Með því að beita Gauss-setningunni á
sértilfellið :math:`\vec F=v \nabla u` eins og áður þar sem
:math:`u,v\in C^2(X)`, þá fáum við *fyrstu formúlu Greens*,

.. math::

  \iint_{{\partial} D} v\dfrac{\partial u}{\partial n} \, dS
   =\iiint_D \nabla v\cdot \nabla u\, dV 
   +\iiint_D v \Delta  u\, dV.

Með sama hætti og áður fáum við *aðra formúlu Greens*,

.. math::

  \iint_{{\partial} D} \bigg(u\dfrac{\partial v}{\partial n}
   -v\dfrac{\partial u}{\partial n}\bigg) \, dS
   =\iiint_D \big(u \Delta  v-v\Delta u\big) \, dV.

Nú er nauðsynlegt að samhæfa ritháttinn fyrir heildi í öllum víddum, til
þess að þurfa ekki að endurtaka röksemdafærslur, sem eru óháðar víddinni
á rúminu. Við hættum því að skrifa margföld heildi og táknum óháðu
breyturnar með :math:`x=(x_1,\dots,x_n)`,
:math:`{\xi}=({\xi}_1,\dots,{\xi}_n)` o.s.frv. Ef fall :math:`u` er
gefið á einhverju opnu mengi :math:`D` í :math:`{{\mathbb  R}}^n` sem
hefur samfellt deildanlegan jaðar :math:`{\partial}D`, þá táknum við
rúmheildið af :math:`u` yfir :math:`D` og flatarheildið af :math:`u`
yfir :math:`{\partial}D` með

.. math:: \int_D u\, dx \qquad \text { og } \qquad  \int_{{\partial}D} u\, dS.

Ef víddin er :math:`2`, þá er :math:`dS` bogalengdarfrymi, en ef víddin
er :math:`3`, þá er :math:`dS` flatarmálsfrymi. Gauss-formúlurnar gilda
raunar þó svo að jaðarinn sé ekki samfellt deildanlegur í öllum punktum.
Í tveimur víddum dugir að hann sé samfellt deildanlegur á köflum og í
þremur víddum mega vera horn og brot í jaðrinum. Sem dæmi getum við
tekið tening eða einhvern annan margflötung. Við munum segja að jaðar á
svæði :math:`X` í :math:`{{\mathbb  R}}^n` sé *sléttur*, ef hægt er að
beita Gauss-setningunni á samfelld vigursvið
:math:`\vec F:\overline X\to {{\mathbb  R}}^n` sem eru samfellt
deildanleg á :math:`X`.

Við eigum eftir að sjá Green-formúlurnar notaðar á margvíslegan hátt.
Ein skemmtileg beiting á þeim er sönnun á *meðalgildissetningunni*.
Gerum nú ráð fyrir að :math:`X` sé opið hlutmengi í
:math:`{{\mathbb  R}}^3` og að :math:`X` innihaldi :math:`\overline D`
þar sem :math:`D` er eitthvert takmarkað svæði með sléttan jaðar. Ef
:math:`u\in C^2(X)\cap C(\overline X)`, þá gefur önnur formúla Greens að

.. math::

  \int_{{\partial} D} \dfrac{\partial u}{\partial n}\, dS
   =\int_D \Delta  u\, dx.

Ef :math:`u` er þýtt fall, þá fáum við

.. math::

  \int_{{\partial} D} \dfrac{\partial u}{\partial n}\, dS
   =0.

Nú skulum við láta :math:`D=\overline B(0,r)` vera lokuðu kúluna með
miðju í :math:`0` og geislann :math:`r`. Athugum að ytri þvervigurinn á
:math:`{\partial}B(0,r)` í punktinum :math:`x=(x_1,x_2,x_3)` er
:math:`\vec n=\vec e_r=(x_1/r,x_2/r,x_3/r)`. Þar með er

.. math::

  \dfrac{{\partial} u}{{\partial} n}
   =\dfrac {x_1}r\dfrac{{\partial}u}{{\partial} x_1}+
   \dfrac {x_2}r\dfrac{{\partial}u}{{\partial} x_2}+
   \dfrac {x_3}r\dfrac{{\partial}u}{{\partial} x_3}
   =\dfrac{{\partial} v}{\partial r},

þar sem fallið :math:`v` er framsetning á :math:`u` í kúluhnitum,

.. math::

  v(r,{\theta},\phi)=u(r\sin{\theta}\cos\phi, 
   r\sin{\theta}\sin\phi,r\cos{\theta}).

Nú stikum við yfirborð kúlunnar og fáum

.. math::

  \int_{{\partial} B(0,r)} \dfrac{\partial u}{\partial n}\, dS
   =\int_0^{\pi}\int_0^{2\pi}\dfrac{{\partial} v}{\partial r}(r,{\theta},\phi)
   \, r^2\sin{\theta}\, d{\theta} d\phi.

Flatarmál kúluyfirborðsins er :math:`a({\partial}B(0,r))=4{\pi} r^2` svo
meðalgildi fallsins :math:`u` yfir :math:`{\partial}B(0,r)` er

.. math::

  \begin{aligned}
   \dfrac 1{a({\partial}B(0,r))} \int_{{\partial}B(0,r)} u\, dS
   &=\dfrac 1{4{\pi}r^2}\int_0^{\pi}\int_0^{2\pi} v(r,{\theta},\phi)
   \, r^2\sin{\theta}\, d{\theta} d\phi\\
   &=\dfrac 1{4{\pi}}\int_0^{\pi}\int_0^{2\pi} v(r,{\theta},\phi)
   \, \sin{\theta}\, d{\theta} d\phi.\end{aligned}

Ef við gefum okkur að :math:`u` sé þýtt fall, þá gefa formúlurnar fyrir heildi :math:`\frac{\partial u}{\partial n}` yfir :math:`\partial D` og :math:`\partial B(0,r)` hér að framan að

.. math::

  \dfrac{\partial} {\partial r}\bigg(
   \dfrac 1{a({\partial}B(0,r))} \int_{{\partial}B(0,r)} u\, dS\bigg)
   =\dfrac 1{4{\pi}}\int_0^{\pi}\int_0^{2\pi} 
   \dfrac{\partial v}{\partial r}(r,{\theta},\phi)
   \, \sin{\theta}\, d{\theta} d\phi=0.

Þetta meðalgildi er því óháð geislanum :math:`r` á kúlunni. Greinilegt
er að

.. math::

  \lim\limits_{r\to 0}\bigg(
   \dfrac 1{a({\partial}B(0,r))} \int_{{\partial}B(0,r)} u\, dS\bigg)
   =\dfrac 1{4{\pi}}\int_0^{\pi}\int_0^{2\pi} 
   v(0,{\theta},\phi)
   \, \sin{\theta}\, d{\theta} d\phi=u(0).

Þar með höfum við:

Setning
^^^^^^^

(*Meðalgildissetning*).   Látum :math:`u` vera þýtt fall á opnu mengi
:math:`X` í :math:`{{\mathbb  R}}^3` og gerum ráð fyrir að lokaða kúlan
:math:`\overline B({\alpha},r)` með miðju í :math:`{\alpha}` og geislann
:math:`r` sé innihaldin í :math:`X`. Þá er

.. math::

  u({\alpha})=
   \dfrac 1{4{\pi}r^2} \int_{{\partial}B({\alpha},r)} u\, dS.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við höfum sannað þessa reglu í sértilfellinu :math:`{\alpha}=0` hér að
framan og fáum almenna tilfellið með því að hliðra upphafspunktinum í
:math:`{\alpha}`.

.. end-toggle::

Með nákvæmlega sömu aðferð er hægt að sanna meðalgildissetninguna í
öllum rúmvíddum :math:`n`.

Há- og lággildislögmál fyrir þýð föll
-------------------------------------

Há- og lággildislögmál fyrir þýð föll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mikilvægasta afleiðing meðalgildissetningarinnar er:

Setning
^^^^^^^

(*Há- og lággildislögmál*).   Látum :math:`X` vera takmarkað svæði í
:math:`{{\mathbb  R}}^n`, :math:`n=2,3` og látum
:math:`u:\overline X\to {{\mathbb  R}}` vera fall sem er þýtt á
:math:`X` og samfellt á lokuninni :math:`\overline X`. Þá tekur
:math:`u` hæsta og lægsta gildi sitt á jaðrinum :math:`{\partial} X`. Ef
hæsta eða lægsta gildi er tekið í innri punkti, þá er :math:`u`
fastafall.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Fyrri staðhæfingin leiðir beint af þeirri síðari. Fyrst :math:`u` er
samfellt á :math:`\overline X`, þá tekur :math:`u` hæsta gildi sem við
táknum með :math:`M`. Við setjum :math:`A=\{z; u(z)=M\}`. Ef
:math:`A\neq \overline X`, þá hefur :math:`A` jaðarpunkt :math:`{\alpha}\in X`. Sérhver lokuð
kúla :math:`\overline B({\alpha},r)\subset X` sker bæði :math:`A` og
:math:`X\setminus A` og þar með er hægt að velja :math:`r` þannig að
einhver opinn flötur í jaðrinum :math:`{\partial} B({\alpha},r)` skeri
:math:`X\setminus A`. Á þessum opna fleti er :math:`u<M` og þar með er meðalgildi
:math:`u` yfir allan jaðarinn :math:`<M`. Gildið í miðpunktinum
:math:`{\alpha}` er :math:`M`, svo þetta er mótsögn við
meðalgildisregluna. Við höfum þar með sannað að hágildi er ekki tekið í
innri punkti nema :math:`u` sé fastafall. Við fáum lággildislögmálið með
því að beita hágildislögmálinu á :math:`-u`.

.. end-toggle::

Af hágildislögmálinu leiðir síðan ótvíræðni í lausn
Dirichlet-verkefnisins fyrir Poisson-jöfnuna:

Setning
^^^^^^^

Látum :math:`X` vera takmarkað svæði í :math:`{{\mathbb  R}}^n`,
:math:`n=2,3`, og gerum ráð fyrir að til sé
:math:`u\in C^2(X)\cap C(\overline X)` sem uppfyllir

.. math::

  \Delta  u=f \quad \text { á }  \quad X \qquad \text{ og } \qquad
   u=\varphi   \quad \text { á }  \quad {\partial}X,

þar sem :math:`f\in C(X)` og :math:`\varphi\in C({\partial} X)` eru
gefin föll. Þá er :math:`u` ótvírætt ákvarðað.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Ef :math:`u_1` og :math:`u_2` eru tvær lausnir á verkefninu, þá
uppfyllir mismunurinn :math:`v=u_1-u_2` Laplace-jöfnuna
:math:`\Delta  v=0` á :math:`X` og :math:`v=0` á :math:`{\partial} X`. Með því að beita há- og lággildislögmálinu á föllin
:math:`{{\operatorname{Re\, }}}v` og :math:`{{\operatorname{Im\, }}}v`,
þá fáum við að :math:`v` er núllfallið og þar með að :math:`u_1=u_2`.

.. end-toggle::

Green-föll
----------

Green-föll
~~~~~~~~~~

Í þessari grein ætlum við að fást við úrlausn á Poisson-jöfnunni með
Dirichlet-jaðarskilyrðum á svæðum :math:`X\subset  {{\mathbb  R}}^n`,
þar sem :math:`n` getur verið :math:`2` eða :math:`3`,

.. math::

  \Delta u=f \quad  \text{ á } \quad X \qquad \text { og } \qquad 
   u={\varphi} \quad \text{ á }  \quad {\partial} X,

og við sýnum fram á að oft sé hægt að setja lausnina fram með heildum af
gerðinni

.. math::

  u(x)=\int_{{\partial}X} P_X(x,\xi){\varphi}(\xi)\, dS(\xi)
   +\int_X G_X(x,\xi)f(\xi)\, d\xi
   \qquad x \in  X,

þar sem :math:`P_X` og :math:`G_X` nefnast *Poisson-kjarni* og
*Green-fall fyrir Laplace-virkjann á svæðinu* :math:`X`. Byrjum á því að
gera ráð fyrir að :math:`X` sé opið takmarkað hlutmengi í
:math:`{{\mathbb  R}}^n` með sléttan jaðar. Við skilgreinum fallið
:math:`E` með

.. math::

  E(x)=\begin{cases} \dfrac 1{2{\pi}} \ln |x|,  & x\in {{\mathbb  R}}^n\setminus{{\{0\}}}, \ n=2,\\
   \dfrac {-1}{4{\pi}|x|},  & x\in {{\mathbb  R}}^n\setminus {{\{0\}}}, \ n=3.
   \end{cases}

Munið að :math:`|x|` táknar lengd vigurs í :math:`{{\mathbb  R}}^n`.
Athugið að fallið :math:`E` er þýtt á
:math:`{{\mathbb  R}}^n\setminus {{\{0\}}}`. Við festum nú einn punkt
:math:`x\in X` og lítum á fallið

.. math:: \xi\mapsto E(x-\xi)=E(\xi-x).

Þetta fall er þýtt á :math:`{{\mathbb  C}}\setminus{{\{x\}}}` og tekur
gildið :math:`-{\infty}` í :math:`x`, svo við skerum litla kúlu
:math:`\overline B(x,{\varepsilon})` umhverfis :math:`x` úr :math:`X` og
lítum á :math:`X_\varepsilon=X\setminus \overline B(x,\varepsilon)` eins og sýnt er á myndinni.

.. figure:: ./myndir/fig172.svg
    :align: center
    :alt: Svæðið :math:`X_{\varepsilon}`

    Mynd: Svæðið :math:`X_{\varepsilon}`

Önnur formúla Greens gefur okkur þá

.. math::

  \int_{\partial X_\varepsilon}\bigg(u(\xi)
   \dfrac{\partial E}{\partial n}(x-\xi)-E(x-\xi)
   \dfrac{\partial u}{\partial n}(\xi)\bigg)\, dS(\xi)
   =-\int_{X_\varepsilon} E(x-\xi)\Delta u(\xi)\, d\xi.

Jaðarinn :math:`\partial X_\varepsilon` samanstendur af tveimur hlutum,
:math:`\partial X` og :math:`\partial B(x,\varepsilon)`. Í punkti
:math:`\xi` á hringnum :math:`\partial B(x,\varepsilon)` er stefna ytri
þvervigursins inn í kúluna og því er

.. math::

  \dfrac{\partial E}{\partial n}(x-\xi)
   =\begin{cases} 
   -\dfrac {\partial}{\partial r}\bigg(\dfrac 1{2\pi} \ln r\bigg)
   \bigg|_{r=\varepsilon}=-\dfrac 1{2\pi\varepsilon}, &n=2,\\
   -\dfrac {\partial}{\partial r}\bigg(\dfrac {-1}{4\pi r}\bigg)
   \bigg|_{r=\varepsilon}=\dfrac {-1}{4\pi\varepsilon^2}, &n=3.
   \end{cases}

Þar með er

.. math::

  \lim\limits_{\varepsilon\to 0}
   \int_{\partial B(x,\varepsilon)}u(\xi)
   \dfrac{\partial E}{\partial n}(x-\xi) \, dS(\xi)
   =-\lim\limits_{\varepsilon\to 0}
   \dfrac 1{a({\partial}B(x,{\varepsilon}))}
   \int_{{\partial}B(x,{\varepsilon})}
   u\, dS = -u(x).

Athugið að síðasta markgildið er tekið af meðalgildi :math:`u` á
:math:`{\partial}B(x,{\varepsilon})` og vegna samfelldni :math:`u`
stefnir það á :math:`u(x)`. Ef :math:`n=2`, þá er seinni liðurinn í
vinstri hlið þriðju síðustu formúlu jafn

.. math::

  \lim\limits_{\varepsilon\to 0}
   \int_{\partial B(x,\varepsilon)}
   E(x-\xi) \dfrac{\partial u}{\partial n}(\xi) \, dS(\xi)
   =\lim\limits_{\varepsilon\to 0}
   {\varepsilon}{\ln \varepsilon}
   \dfrac 1{a({\partial}B(x,{\varepsilon}))}
   \int_{{\partial}B(x,{\varepsilon})}
   \dfrac{\partial u}{\partial n} \, dS =0.

Ef :math:`n=3`, fæst sams konar markgildi með :math:`{\varepsilon}` í
stað :math:`{\varepsilon}\ln{\varepsilon}`. Fyrst fallið
:math:`\xi\mapsto E(x-\xi)` er heildanlegt í grennd um :math:`x`, þá
fáum við að

.. math::

  \lim\limits_{\varepsilon\to 0}
   \int_{X_\varepsilon}E(x-\xi) \Delta u(\xi)\, d\xi
   = \int_{X}E(x-\xi) \Delta u(\xi)\, d\xi.

Nú getum við látið :math:`\varepsilon\to 0` og notfært okkur síðustu þrjár formúlur. Við fáum þá

.. math::

  \begin{aligned}
   u(x)&=
   \int_{\partial X}\bigg(u(\xi)
   \dfrac{\partial E}{\partial n}(x-\xi)-E(x-\xi)
   \dfrac{\partial u}{\partial n}(\xi)\bigg)\, dS(\xi)\\
   &+\int_{X} E(x-\xi)\Delta u(\xi)\, d\xi  .\nonumber\end{aligned}

Látum nú :math:`v` vera þýtt fall á :math:`X` sem er samfellt á
lokuninni og beitum annarri formúlu Greens,

.. math::

  0=\int_{\partial X}\bigg(  
   u(\xi)\dfrac{\partial v}{\partial n}(\xi)
   -v(\xi)\dfrac{\partial u}{\partial n}(\xi)\bigg)\, dS(\xi)
   +\int_X v(\xi)\Delta u(\xi)\, d\xi  .

Nú leggjum við saman tvær síðustu formúlur og fáum þá

.. math::

  \begin{aligned}
   u(x)&=
   \int_{\partial X}u(\xi)\bigg(
   \dfrac{\partial E}{\partial n}(x-\xi)
   +\dfrac{\partial v}{\partial n}(\xi)\bigg)\, dS(\xi)
   \\
   &-\int_{\partial X}\bigg(E(x-\xi)+v(\xi)\bigg)
   \dfrac{\partial u}{\partial n}(\xi) \, dS(\xi)\nonumber\\
   &+\int_{X} \bigg(E(x-\xi)+v(\xi)\bigg) \Delta u(\xi)\, d\xi
   .\nonumber\end{aligned}

Hugsum okkur nú að við gætum ákvarðað fall :math:`v` sem er háð
:math:`x` og :math:`\xi` þannig að :math:`\xi\mapsto v(x,\xi)` er þýtt
og :math:`E(x-\xi)+v(x,\xi)=0`, ef :math:`x\in \partial X` og
:math:`\xi\in X`. Þá verður miðliðurinn í síðustu formúlu að núlli.

Skilgreining
^^^^^^^^^^^^

*Green-fall* á svæðinu :math:`X` er fall
:math:`G_X:\overline X\times \overline X\to {{\mathbb  C}}`, þannig að
fyrir sérhvert :math:`\xi\in X` er :math:`x\mapsto G_X(x,\xi)` tvisvar
samfellt deildanlegt í :math:`X\setminus{{\{\xi\}}}` og

\(i) :math:`\Delta_xG_X(x,\xi)=0` á :math:`X\setminus {{\{\xi\}}}`.

\(ii) :math:`G_X(x,\xi)=0` ef :math:`x\in \partial X` og
:math:`\xi\in X`. Ef :math:`X` er ótakmarkað, þá er

.. math::

  \lim\limits_{\substack{b z\to \infty \\ z\in X }}
   G_X(x,\xi) =0.

\(iii) Unnt er að skrifa :math:`G_X(x,\xi)=E(x-\xi)+w(x,\xi)`, þar sem
fallið :math:`x\mapsto w(x,\xi)` er þýtt á öllu :math:`X`.

--------------

Það eru einkum tveir eiginleikar Green-fallsins sem við þurfum að nota,
ótvíræðni og samhverfa:

Setning
^^^^^^^

Látum :math:`X` vera takmarkað svæði með sléttan jaðar og gerum ráð
fyrir að til sé Green-fall :math:`G_X` á :math:`X`. Þá er :math:`G_X`
ótvírætt ákvarðað og :math:`G_X(x,{\xi})=G_X({\xi},x)` fyrir öll
:math:`x,{\xi}\in \overline X`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Hugsum okkur að við höfum tvö Green-föll
:math:`G_j(x,\xi)=E(x-\xi)+w_j(x,\xi)`, :math:`j=1,2` á :math:`X`.
Skilyrðið (iii) segir okkur að fyrir sérhvert :math:`\xi\in X` er fallið
:math:`x\mapsto G_1(x,\xi)-G_2(x,\xi)=w_1(x,\xi)-w_2(x,\xi)` þýtt og það
tekur gildið :math:`0` á jaðrinum. Þar með er þetta núllfallið og við
höfum :math:`G_1=G_2`.

Til þess að sanna samhverfuna, þá veljum við tvo punkta :math:`x_0` og
:math:`\xi_0`. Við ætlum síðan að beita annarri formúlu Greens á föllin
:math:`u(x)=G_X(x,x_0)` og :math:`v(x)=G_X(x,\xi_0)` til þess að sanna
að :math:`G_X(\xi_0,x_0)=u(\xi_0)=v(x_0)=G_X(x_0,\xi_0)`. Ef
:math:`x_0=\xi_0`, þá er ekkert að sanna, svo við megum gera ráð fyrir
að :math:`x_0\neq \xi_0`. Við látum :math:`\varepsilon` vera svo lítið
að skífurnar :math:`\overline B(x_0,\varepsilon)` og :math:`\overline   B(\xi_0,\varepsilon)` séu sundurlægar og innihaldnar í :math:`X`. Við
lítum síðan á mengið
:math:`X_\varepsilon=X\setminus\big(\overline B(x_0,\varepsilon)\cup \overline B(\xi_0,\varepsilon)\big)`.

.. figure:: ./myndir/fig175.svg
    :align: center
    :alt: Svæðið :math:`X_{\varepsilon}`.

    Mynd: Svæðið :math:`X_{\varepsilon}`.

Nú er :math:`\Delta u=\Delta v=0` á :math:`X_\varepsilon` og
:math:`u=v=0` á :math:`\partial X`. Jaðarinn á :math:`X_\varepsilon` er
:math:`\partial X_\varepsilon=\partial X\cup \partial B(x_0,\varepsilon)  \cup \partial B(\xi_0,\varepsilon)`. Ef við beitum annarri formúlu
Greens, þá fáum við

.. math::

  0=\int_{\partial B(x_0,\varepsilon)}
   \bigg( u\dfrac{\partial v}{\partial n}-
    v\dfrac{\partial u}{\partial n}\bigg) \, dS
   +\int_{\partial B({\xi}_0,\varepsilon)}
   \bigg( u\dfrac{\partial v}{\partial n}-
    v\dfrac{\partial u}{\partial n}\bigg) \, dS.

Hér er ytri þverafleiðan tekin út úr svæðinu :math:`X_\varepsilon`.
Athugum síðan að í tilfellinu :math:`n=2` er

.. math::

  u(x)=\dfrac 1{2\pi}\ln |x-x_0|+w(x,x_0)
   \quad \text { og } \quad 
   v(x)=\dfrac 1{2\pi}\ln |x-\xi_0|+w(x,\xi_0).

Í punkti
:math:`x=x_0+i\varepsilon e^{it}\in \partial B(x_0,\varepsilon)` er

.. math::

  u(x)=\dfrac 1{2\pi}\ln\varepsilon +w(x_0+\varepsilon e^{it},x_0)
   \quad \text { og } \quad  
   \dfrac{\partial u}{\partial n}(x)
   =\dfrac{-1}{2\pi\varepsilon}
   -\dfrac{\partial}{\partial r}w(x_0+\varepsilon e^{it},x_0),

og í punkti :math:`x=\xi_0+i\varepsilon e^{it}\in \partial B(\xi_0,\varepsilon)` er

.. math::

  v(x)=\dfrac 1{2\pi}\ln\varepsilon +w(\xi_0+\varepsilon e^{it},\xi_0)
   \quad \text { og } \quad  
   \dfrac{\partial v}{\partial n}(x)
   =\dfrac{-1}{2\pi\varepsilon}
   -\dfrac{\partial}{\partial r}w(\xi_0+\varepsilon e^{it},\xi_0).

Með nákvæmlega sömu röksemdafærslu og leiddi til jafnanna

.. math::

  \lim\limits_{\varepsilon\to 0}
   \int_{\partial B(x,\varepsilon)}u(\xi)
   \dfrac{\partial E}{\partial n}(x-\xi) \, dS(\xi)
   =-\lim\limits_{\varepsilon\to 0}
   \dfrac 1{a({\partial}B(x,{\varepsilon}))}
   \int_{{\partial}B(x,{\varepsilon})}
   u\, dS = -u(x)

og

.. math::

  \lim\limits_{\varepsilon\to 0}
   \int_{\partial B(x,\varepsilon)}
   E(x-\xi) \dfrac{\partial u}{\partial n}(\xi) \, dS(\xi)
   =\lim\limits_{\varepsilon\to 0}
   {\varepsilon}{\ln \varepsilon}
   \dfrac 1{a({\partial}B(x,{\varepsilon}))}
   \int_{{\partial}B(x,{\varepsilon})}
   \dfrac{\partial u}{\partial n} \, dS =0

fyrr í þessari grein fáum við að hægt er að taka markgildi í 

.. math::

  0=\int_{\partial B(x_0,\varepsilon)}
   \bigg( u\dfrac{\partial v}{\partial n}-
    v\dfrac{\partial u}{\partial n}\bigg) \, dS
   +\int_{\partial B({\xi}_0,\varepsilon)}
   \bigg( u\dfrac{\partial v}{\partial n}-
    v\dfrac{\partial u}{\partial n}\bigg) \, dS

og að það er :math:`0=v(x_0)-u(\xi_0)`, sem jafngildir því að
:math:`G_X(x_0,\xi_0)=G_X(\xi_0,x_0)`. Tilfellið :math:`n=3` er
meðhöndlað á nákvæmlega sama hátt.

.. end-toggle::

Niðurstaðan úr þessum erfiðu útreikningum er, að ef :math:`G_X` er
Green-fall takmarkaðs svæðis :math:`X` og við gerum ráð fyrir að ytri
þverafleiðan :math:`\partial G_X(x,\xi)/\partial n` af :math:`G_X` með
tilliti til :math:`\xi` sé til ef :math:`x\in X` og
:math:`\xi\in {\partial}X`, þar sem ekki er brot á jaðrinum
:math:`\partial X`, þá gefur formúlan

.. math::

  \begin{aligned}
   u(x)&=
   \int_{\partial X}u(\xi)\bigg(
   \dfrac{\partial E}{\partial n}(x-\xi)
   +\dfrac{\partial v}{\partial n}(\xi)\bigg)\, dS(\xi)
   \\
   &-\int_{\partial X}\bigg(E(x-\xi)+v(\xi)\bigg)
   \dfrac{\partial u}{\partial n}(\xi) \, dS(\xi)\nonumber\\
   &+\int_{X} \bigg(E(x-\xi)+v(\xi)\bigg) \Delta u(\xi)\, d\xi
   \nonumber\end{aligned}

okkur

.. math::

  u(x)=\int_{\partial X} \dfrac{\partial G_X}{\partial n}(x,\xi) 
   u(\xi)\, dS(\xi)
   +\int_X G_X(x,\xi) \Delta u(\xi)\, d\xi.

Einnig fáum við lausnarformúlu fyrir verkefnið :math:`\Delta u=f` á
:math:`X` með :math:`u=\varphi` á :math:`\partial X`, þar sem :math:`f`
er gefið samfellt fall á :math:`X` og :math:`\varphi` er gefið samfellt
fall á :math:`\partial X`, því

.. math::

  u(x)=\int_{\partial X} \dfrac{\partial G_X}{\partial n}(x,\xi) 
   \varphi(\xi)\, dS(\xi)
   +\int_X G_X(x,\xi) f(\xi)\, d\xi.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Green-fall skífu og kúlu

Látum nú :math:`D_a=\{x\in {{\mathbb  R}}^n; |x|<a\}` vera skífu/kúlu í
:math:`{{\mathbb  R}}^n` með miðpunkt :math:`0` og geisla :math:`a`. Til
þess að ákvarða Green-fall :math:`D_a`, þá þurfum við að finna fall
:math:`w_a` þannig að :math:`G_{D_a}(x,{\xi})=E(x-{\xi})+w_a(x,{\xi})`
uppfylli skilyrðin í skilgreiningunni á Green-falli. Þetta er hægt að
gera með svokallaðri *speglunaraðferð*. Hún er hugsuð þannig að fyrst
tökum við :math:`{\xi}\in D_a`, :math:`{\xi}\neq  0`. Við lítum síðan á
spegilpunkt :math:`{\xi}` um hringinn/kúluflötinn :math:`{\partial}D_a`,
sem táknaður er með :math:`{\xi}^\ast`. Hann liggur á geislanum frá
:math:`0` gegnum :math:`{\xi}` utanvert við :math:`{\partial}D_a` og
uppfyllir :math:`|{\xi}||{\xi}^\ast|=a^2`. Þar með er
:math:`{\xi}^\ast={\xi}a^2/|{\xi}|^2`.

.. figure:: ./myndir/fig173.svg
    :align: center
    :alt: Speglun um hring og kúluflöt.

    Mynd: Speglun um hring og kúluflöt.

Í ljós kemur að hægt er að velja
:math:`w_a(x,{\xi})=-E((x-{\xi}^\ast)|{\xi}|/a)`. Fyrst
:math:`{\xi}^\ast` er utanvert við hringinn og :math:`E` er þýtt á
:math:`{{\mathbb  R}}^n\setminus{{\{0\}}}`, þá er ljóst að fallið
:math:`x\mapsto w_a(x,{\xi})` er þýtt á :math:`D_a`, svo skilyrði (i) og
\(iii) í skilgreiningunni á Green-falli eru uppfyllt. Til þess að sanna að
\(ii) sé uppfyllt þá athugum við, að ef :math:`x\in {\partial}D_a`, þá
eru þríhyrningarnir með hornpunktana :math:`0,x,{\xi}` og
:math:`0,a{\xi}/|{\xi}|,|{\xi}|x/a` einslaga og þar með er

.. math::

  |x-{\xi}|=\big ||{\xi}|x/a-a{\xi}/|{\xi}| \big |=
   |x-a^2{\xi}/|{\xi}|^2||{\xi}|/a=|x-{\xi}^\ast||{\xi}|/a.

Þetta segir okkur að
:math:`G_{D_a}(x,{\xi}) = E(x-{\xi}) - E( (x-{\xi}^\ast)|{\xi}|/a ) = 0`
ef :math:`x\in {\partial}D_a`. Niðurstaðan er nú að

.. math::

  \begin{aligned}
   G_{D_a}(x,{\xi})&=E(x-{\xi})-E((x-a^2{\xi}/|{\xi}|^2)|{\xi}|/a) \\
   &=
   \begin{cases}
   \dfrac 1{2{\pi}}\ln|x-{\xi}|
   -\dfrac 1{2{\pi}}\ln\big(|x-a^2{\xi}/|{\xi}|^2||{\xi}|/a\big),
   &n=2,\\ 
   \dfrac {-1}{4{\pi}|x-{\xi}|}
   +\dfrac 1 {4{\pi}|x-a^2{\xi}/|{\xi}|^2||{\xi}|/a},
   &n=3.
   \end{cases}\nonumber\end{aligned}

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Green-fall hálfplans og hálfrúms.

Skoðum nú :math:`\Bbb H_+=\{x\in {{\mathbb  R}}^n; x_n>0\}`, sem er efra
hálfplanið/hálfrúmið. Jaðar þess :math:`{\partial}\Bbb H_+` er
rauntalnalínan :math:`{{\mathbb  R}}` í
:math:`{{\mathbb  C}}={{\mathbb  R}}^2`, ef :math:`n=2`, en
:math:`x_1x_2`-planið, ef :math:`n=3`. Eftir að hafa séð
speglunaraðferðina í sýnidæminu hér á undan, þá sjáum við í hendi
okkar að skilyrðin í skilgreiningunni á Green-falli eru uppfyllt fyrir

.. math:: G _{\Bbb H_+}(x,{\xi})=E(x-{\xi})-E(x-{\xi}^\ast),

þar sem :math:`{\xi}^\ast` táknar núna spegilpunkt :math:`{\xi}` um
línuna/planið :math:`{\partial}\Bbb H_+`,
:math:`{\xi}^\ast=({\xi}_1,-{\xi}_2)` ef :math:`n=2` og
:math:`{\xi}^\ast=({\xi}_1,{\xi}_2,-{\xi}_3)` ef n = 3.

.. figure:: ./myndir/fig174.svg
    :align: center
    :alt: Speglun um línu og plan.

    Mynd: Speglun um línu og plan.

Niðurstaðan er því

.. math::

  G_{\Bbb H_+}(x,{\xi})
   =
   \begin{cases}
   \dfrac 1{2{\pi}}\ln|x-{\xi}|
   -\dfrac 1{2{\pi}}\ln|x-{\xi}^\ast|,
   &n=2,  \ {\xi}^\ast=({\xi}_1,-{\xi}_2),\\ 
   \dfrac {-1}{4{\pi}|x-{\xi}|}+
   \dfrac 1 {4{\pi}|x-{\xi}^\ast|},
   &n=3, \ {\xi}^\ast=({\xi}_1,{\xi}_2,-{\xi}_3).
   \end{cases}

.. end-toggle::

Nú skulum við innleiða ritháttinn :math:`z` og :math:`{\zeta}` fyrir
punkta í :math:`{{\mathbb  R}}^2={{\mathbb  C}}` eins og venja er í
tvinnfallagreiningu og láta
:math:`\Bbb E=\{z\in {{\mathbb  C}}; |z|<1\}` tákna einingarskífuna í
:math:`{{\mathbb  C}}`. Auðvelt er að sannfæra sig um að

.. math::

  G_{\Bbb E}(z,\zeta)
   = \dfrac 1{2\pi}\bigg(\ln|x-\xi|
   -\ln|1-\overline  \zeta z|\bigg)
   =\dfrac 1{2\pi}\ln\bigg|\dfrac{x-\xi}{1-\overline  \zeta z}\bigg|.

Gerum nú ráð fyrir að :math:`X` og :math:`Y` séu opin mengi í
:math:`{{\mathbb  C}}`, að :math:`F:\overline  X\to \overline Y` sé
samfelld og gangtæk vörpun, sem er fáguð á :math:`X`. Gerum einnig ráð
fyrir að við þekkjum Green-fall mengisins :math:`Y` og að við viljum
ákvarða Green-fall :math:`X`. Þetta reynist vera auðvelt, því

.. math:: G_X(z,\zeta)=G_Y(F(z),F(\zeta)), \qquad z,\zeta\in \overline X.

Til þess að sjá að þessi formúla gildir, þá athugum við að hægt er að
skrifa

.. math::

  G_Y(z_1,\zeta_1)=
   \dfrac 1{2\pi}\ln |z_1-\zeta_1|+w_Y(z_1,\zeta_1),

og því uppfyllir

.. math::

  G_X(z,\zeta)=
   \dfrac 1{2\pi}\ln |z-\zeta|+
   \dfrac 1{2\pi}\ln|(F(z)-F(\zeta))/(z-\zeta)|+w_Y(F(z),F(\zeta)),

skilyrðin (i)-(iii) í skilgreiningunni á Green-falli, því fallið

.. math::

  z\mapsto w_X(z,\zeta)=
   \dfrac 1{2\pi}\ln|(F(z)-F(\zeta))/(z-\zeta)|+w_Y(F(z),F(\zeta))

er þýtt, því samskeyting af þýðu og fáguðu falli er þýtt.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Fyrr í kaflanum skoðuðum við svæðið sem takmarkast af hjartaferlinum
:math:`r=2(1+\cos {\theta})`, þ.e.

.. math:: X=\{z=re^{i{\theta}}; r<2(1+\cos {\theta})\}.

Við sáum þá að vörpunin :math:`z\mapsto z^{\frac 12}-1` varpar
:math:`\overline X` á :math:`\overline{\Bbb E}` og því er

.. math::

  G_X(z,{\zeta})=\dfrac 1{2{\pi}}\bigg(
   \ln|z^{\frac 12}-{\zeta}^{\frac 12}|
   -\ln|1-(z^{\frac 12}-1)(\overline \zeta^{\frac 12}-1)|\bigg), 
   \qquad z,{\zeta}\in
   \overline X.

.. end-toggle::

Poisson-kjarnar
---------------

Poisson-kjarnar
~~~~~~~~~~~~~~~

Í þessum kafla höfum við leyst Dirichlet-verkefnið fyrir hringskífu og 
hálfplan. Í báðum tilfellunum
leiddum við út lausnarformúlu, sem er heildi yfir jaðarinn á svæðinu og
hægt er að líta á það sem földun á jaðargildunum og kjarna, sem við
nefndum Poisson-kjarna. Nú ætlum við að alhæfa þessar formúlur, en við
sáum í síðustu grein að lausnarformúla fyrir verkefnið

.. math::

  \Delta  u=0 \quad \text{ á } \quad X \qquad \text{ og } 
   \qquad u=\varphi \quad \text{ á } \quad {\partial} X,

er gefin með heildinu

.. math::

  u(z)=\int_{{\partial} X} \dfrac{{\partial} G_X}{{\partial} n}(z,{\zeta})
   \varphi({\zeta}) \, dS({\zeta}).

Skilgreining
^^^^^^^^^^^^

Látum :math:`X`\ vera svæði í :math:`{{\mathbb  C}}` og látum
:math:`G_X` vera Green-fall á :math:`X`. Gerum ráð fyrir að jaðarinn
:math:`{\partial} X` sé samfellt deildanlegur á köflum og skilgreinum

.. math:: P_X(z,{\zeta})=\dfrac{{\partial} G_X}{{\partial} n}(z,{\zeta}),

ef :math:`z\in X` og :math:`{\zeta}\in {\partial} X` er punktur, þar
sem ytri þvervigurinn :math:`\vec n({\zeta})` er vel skilgreindur og

.. math::

  \dfrac{{\partial} G_X}{{\partial} n}(z,{\zeta})
   =\lim\limits_{{\varepsilon}\to 0+}
   \dfrac{G_X(z,{\zeta}-{\varepsilon}\vec n({\zeta}))-G_X(z,{\zeta})}
   {-{\varepsilon}}.

--------------

Auðvelt er að sannfæra sig um að

.. math::

  P_{\Bbb E}(z,e^{it})
   =\dfrac{{\partial} G_{\Bbb E}}{{\partial} r}(z,re^{it})
   \bigg|_{r=1}=\dfrac{1-|z|^2}{2{\pi}|z-e^{it}|^2},

og

.. math::

  P_{\Bbb H_+}(z,{\zeta})=
   -\dfrac{{\partial}G_{\Bbb H_+}(z,{\zeta}+i{\eta})}{{\partial}{\eta}}
   \bigg|_{{\eta}=0}=
   \dfrac {\zeta}{{\pi}(z^2+{\zeta}^2)},

í samræmi við umfjöllun okkar um Poisson-formúluna í greinum hér að framan.

Gerum nú ráð fyrir að við höfum gagntæka vörpun :math:`F:\overline X\to \overline Y` sem varpar jaðrinum :math:`{\partial} X` gagntækt á
:math:`{\partial} Y` og er fáguð á :math:`X`. Til einföldunar skulum við gera ráð fyrir að
:math:`{\zeta}\mapsto G_X(z,{\zeta})` sé samfellt deildanlegt í grennd
um :math:`\overline X` fyrir öll :math:`z\in X` og að
:math:`{\zeta}\mapsto G_Y(z,{\zeta})` sé samfellt deildanlegt í grennd
um :math:`\overline Y` fyrir öll :math:`z\in Y`. Ef
:math:`{\zeta}\in {\partial} X` og :math:`{\gamma}(s)` er stikun á
:math:`{\partial} X` í grennd um :math:`{\zeta}` með tilliti til
bogalengdarinnar :math:`s`, :math:`{\gamma}(0)={\zeta}` og
umferðarstefnan er jákvæð miðað við svæðið :math:`X`, þá er
einingarsnertill í :math:`{\zeta}` gefinn sem
:math:`\vec T({\zeta})={\gamma}{{^{\prime}}}(0)` og
einingarþvervigurinn er því
:math:`\vec n({\zeta})=-i\vec T({\zeta})=-i{\gamma}{{^{\prime}}}(0)`.

Ef :math:`u` er samfellt deildanlegt fall í grennd um :math:`{\zeta}`,
þá er

.. math::

  \begin{aligned}
   \dfrac{{\partial} u}{{\partial} n}({\zeta})
   &={{\operatorname{grad}}}u({\zeta}) \cdot \vec n({\zeta})\\
   &={{\operatorname{Re\, }}}\bigg(\bigg(
   \dfrac{{\partial} u}{{\partial} {\xi}}({\zeta})-i
   \dfrac{{\partial} u}{{\partial} {\eta}}({\zeta})\bigg)
   (-i){\gamma}{{^{\prime}}}(0)\bigg)\\
   &=2{{\operatorname{Im\, }}}\bigg(\dfrac{{\partial} u}{{\partial} {\zeta}}({\zeta})
   {\gamma}{{^{\prime}}}(0) \bigg).\end{aligned}

Nú er :math:`F({\gamma}(s))` stikun á jaðrinum :math:`{\partial} Y`
umhverfis punktinn :math:`F({\zeta})` og snertill er
:math:`\big(F({\gamma})\big){{^{\prime}}}(0)=F{{^{\prime}}}({\zeta}){\gamma}{{^{\prime}}}(0)`.
Einingarsnertill er síðan
:math:`F{{^{\prime}}}({\zeta}){\gamma}{{^{\prime}}}(0)/|F{{^{\prime}}}({\zeta})|`.
Nú skrifum við :math:`u=v(F)`, þar sem :math:`v` er samfellt deildanlegt
í grennd um :math:`F({\zeta})`. Þá sjáum við að

.. math::

  \begin{aligned}
   \dfrac{{\partial} u}{{\partial} n}({\zeta})
   &=2{{\operatorname{Im\, }}}\bigg( \dfrac{{\partial} v}{{\partial} {\zeta}}
   (F({\zeta}))F{{^{\prime}}}({\zeta}){\gamma}{{^{\prime}}}(0)\bigg)\\
   &= \dfrac{{\partial} v}{{\partial} n}(F({\zeta})){|F{{^{\prime}}}({\zeta})|} .\end{aligned}

Nú beitum við þessari formúlu á fallið
:math:`z\mapsto G_X(z,{\zeta})=G_Y(F(z),F({\zeta}))` og fáum samband
milli Poisson-kjarnanna á :math:`X` og :math:`Y`,

.. math::

  P_X(z,{\zeta})=P_Y(F(z),F({\zeta}))|F{{^{\prime}}}({\zeta})|,
   \qquad z\in  X, \ {\zeta}\in {\partial}X.

Hnikareikningur og jaðargildisverkefni
--------------------------------------

Hnikareikningur og jaðargildisverkefni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Oft eru jaðargildisverkefni jafngild ákveðnum útgildisverkefnum, sem
snúast um að hámarka eða lágmarka ákveðin orkuheildi. Gott dæmi er
Dirichlet-verkefnið fyir Poisson-jöfnuna,

.. math::

  -\Delta u =f \quad \text{ á } \quad X \qquad \text{ og } \qquad
   u=g \quad \text { á } \quad {\partial} X.

Það tengist orkuheildinu

.. math::

  {\cal E}[w]=\tfrac 12 \int_X|\nabla w|^2 \, dx -
   \int_X f w \, dx,

þar sem við gerum ráð fyrir að :math:`X` sé takmarkað svæði í
:math:`{{\mathbb  R}}^n` með sléttan jaðar og :math:`f` og :math:`g` eru
gefin samfelld föll á :math:`X` og :math:`{\partial}X`. Við hugsum okkur
að vörpunin :math:`w\mapsto {\cal E}[w]` sé skilgreind á :math:`V_g`,
mengi allra falla :math:`w\in C^2(X)\cap C(\overline X)` sem uppfylla
jaðarskilyrðið :math:`u=g` á :math:`{\partial}X`. Fall
:math:`v\in C^2(X)\cap C(\overline X)`, sem uppfyllir óhliðruðu
jaðarskilyrðin, nefnist *leyfileg hnikun á föllum* í :math:`V_g`.
Athugið að fyrir slík föll er :math:`w+sv\in V_g` fyrir öll
:math:`w\in V_g` og öll :math:`s\in {{\mathbb  R}}` og við fáum að
orkuheildið er

.. math::

  {\cal E}[w+sv] ={\cal E}[w]+ 
   s\int_X\big(\nabla w\cdot\nabla v  - f v\big) \, dx
   +\tfrac 12 s^2 \int_X|\nabla v|^2 \, dx.

Ef við beitum fyrstu formúlu Greens og notfærum okkur að :math:`v=0`, á
:math:`{\partial}X`, þá fáum við

.. math::

  {\cal E}[w+sv] ={\cal E}[w] 
   -s\int_X\big(\Delta w  + f\big)v \, dx
   +\tfrac 12 s^2 \int_X|\nabla v|^2 \, dx.

Af þessu sjáum við að

.. math::

  \dfrac d{ds} {\cal E}[w+sv]\bigg|_{s=0} =
   -\int_X \big(\Delta w  +  f\big) v \, dx

og

.. math::

  \dfrac {d^2}{ds^2} {\cal E}[w+sv]\bigg|_{s=0} 
   =\int_X |\nabla  v|^2 \, dx.

Setning
^^^^^^^

(*Lögmál Dirichlets*).   Fallið :math:`u\in C^2(X)\cap C(\overline X)`
er lausn á Dirichlet-verkefninu 

.. math::

  -\Delta u =f \quad \text{ á } \quad X \qquad \text{ og } \qquad
   u=g \quad \text { á } \quad {\partial} X

þá og því aðeins að
:math:`E[w]\geq E[u]` fyrir öll :math:`w\in C^2(X)\cap C(\overline X)`
sem uppfylla :math:`w=g` á :math:`{\partial} X`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Ef :math:`u` er lausn á Dirichlet-verkefninu og
:math:`w\in C^2(X)\cap C(\overline X)` uppfyllir :math:`w=g` á
:math:`{\partial} X`, þá er :math:`v=w-u` leyfileg hnikun á föllum í
:math:`V_g`. Þar með gefur 

.. math::

  {\cal E}[w+sv] ={\cal E}[w] 
   -s\int_X\big(\Delta w  + f\big)v \, dx
   +\tfrac 12 s^2 \int_X|\nabla v|^2 \, dx

að

.. math::

  {\cal E}[w]={\cal E}[u+v]=
   {\cal E}[u]+\tfrac 12 \int_X|\nabla v|^2 \, dx
   \geq {\cal E}[u].

Öfugt, ef :math:`u` er fall í :math:`V_g` sem lágmarkar orkuheildið og
:math:`v` er leyfileg hnikun á föllum í :math:`V_g`, þá er afleiðan af
fallinu :math:`s\mapsto {\cal E}[u+sv]` í punktinum :math:`s=0` jöfn
:math:`0`. Þar með gefur 

.. math::

  \dfrac d{ds} {\cal E}[w+sv]\bigg|_{s=0} =
   -\int_X \big(\Delta w  +  f\big) v \, dx

okkur að

.. math:: \int_X\big(\Delta w  + f\big)v \, dx=0.

Fyrst :math:`v` er ótiltekin leyfileg hnikun á föllum í :math:`V_g`, þá
gefur þetta að :math:`-\Delta u=f` á :math:`X`. Við höfum því sýnt að
:math:`u` er lausn á Dirichlet-verkefninu.

.. end-toggle::

Dirichlet-lögmálið og aðrar hliðstæðar lágmörkunarsetningar fyrir önnur
jaðargildisverkefni, eru ákaflega mikilvægar í tölulegri greiningu,
þegar verið er að finna nálgunarlausnir á jaðargildisverkefnum. Aðferðin
er kennd við Rayleigh og Ritz. Hún snýst um að velja fyrst fall
:math:`v_0` á :math:`\overline X`, sem uppfyllir hliðraða jaðarskilyrðið
:math:`v_0=g` á :math:`{\partial}X` eða er nálgun á þessu skilyrði.
Síðan eru valin föll :math:`v_1,\dots,v_N` á :math:`\overline X` sem
uppfylla óhliðruð jaðarskilyrði. Þvínæst er vörpunin

.. math::

  {{\mathbb  R}}^N \ni c=(c_1,\dots,c_N)
   \mapsto {\cal E}[v_0+c_1v_1+\cdots+c_Nv_N]

lágmörkuð. Út frá skilyrðinu

.. math::

  \dfrac {\partial}{\partial c_j}{\cal E}[v_0+c_1v_1+\cdots+c_Nv_N]=0,
   \qquad j=1,\dots,N,

sést með beinum reikningi að lágmarkið er tekið í falli
:math:`v=v_0+c_1v_1+\cdots+c_Nv_N`, þar sem :math:`c` uppfyllir línulegt
jöfnuhneppi :math:`Ac=b`. Stuðlafylkið :math:`A=\big(a_{jk}\big)` og
hægri hliðin :math:`b=(b_1,\dots,b_N)` eru gefin með

.. math::

  a_{jk}=\int_X\nabla v_j\cdot \nabla v_k\, dx, \qquad
   b_j=\int_X fv_j\, dx -\int_X \nabla v_0\cdot \nabla v_j\, dx.

Grunnföllin :math:`v_0,v_1,\dots,v_N` er hægt að velja á marga
mismunandi vegu og með skynsamlegu vali á þeim er hægt að sýna fram á að
skekkjan :math:`|u-v|` verði lítil á öllu svæðinu :math:`X`.

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Sýnið að í pólhnitum séu virkjarnir :math:`{\partial}_z` og
:math:`\partial_{\overline z}` gefnir með formúlunum

.. math::

  \dfrac{\partial}{\partial z} =
   \dfrac {e^{-i\theta}}2\bigg(\dfrac{\partial}{\partial r} -\dfrac ir
   \dfrac{\partial}{\partial \theta}\bigg) 
   \qquad \text { og } \qquad
   \dfrac{\partial}{\partial \overline  z} =
   \dfrac {e^{i\theta}}2\bigg(\dfrac{\partial}{\partial r} +\dfrac ir
   \dfrac{\partial}{\partial \theta}\bigg).

Hér er átt við að ef
:math:`v(r,\theta)=u(re^{i\theta})=u(r\cos\theta,r\sin \theta)`, þá er

.. math::

  \dfrac{\partial u}{\partial z}(z) =
   \dfrac {e^{-i\theta}}2\bigg(\dfrac{\partial v}{\partial r}(r,\theta)
   -\dfrac ir
   \dfrac{\partial v}{\partial \theta}(r,\theta)\bigg),
   \qquad
   \dfrac{\partial u}{\partial \overline z}(z) =
   \dfrac {e^{i\theta}}2\bigg(\dfrac{\partial v}{\partial r}(r,\theta) +\dfrac ir
   \dfrac{\partial v}{\partial \theta}(r,\theta)\bigg).

Dæmi
^^^^

Notið formúlurnar í síðasta dæmi til þess að leiða út formúluna fyrir
Laplace-virkjann í pólhnitum.

Dæmi
^^^^

Sýnið að :math:`\Delta =4{{\partial}^2}/{{\partial}z{\partial}\bar z} =4{{\partial}^2}/{{\partial}\bar z{\partial}z}`.

Dæmi
^^^^

Sýnið að :math:`{\partial_z \overline  f}= \overline{\partial_{ \overline z}f}` og
:math:`\partial_{ \overline z} \overline  f= \overline{{\partial_z  f}}`.

Dæmi
^^^^

Sannið keðjuregluna á forminu 

.. math::

  \begin{aligned}
   \dfrac{\partial u}{\partial z}(z)
   &=\dfrac{\partial v}{\partial \zeta}({\zeta})
   \dfrac{\partial F}{\partial z}(z)
   +\dfrac{\partial v}{\partial\overline\zeta}({\zeta})
   \dfrac{\partial \overline F}{\partial z}(z),
   \\
   \text{og}\\
   \dfrac{\partial u}{\partial \overline z}(z)
   &=\dfrac{\partial v}{\partial \zeta}({\zeta})
   \dfrac{\partial F}{\partial \overline z}(z)
   +\dfrac{\partial v}{\partial\overline \zeta}({\zeta})
   \dfrac{\partial  \overline F}{\partial \overline z}(z).\end{aligned}


Dæmi
^^^^

Sýnið að Poisson-kjarninn sé þýtt fall á efra hálfplaninu og staðfestið
að taka megi afleiður af fallinu 

.. math::

  u(x,y)=P_{\Bbb H_+}(\cdot,y)\ast \varphi(x)=\dfrac y\pi\int_{-\infty}^{+\infty}
   \dfrac{\varphi(t)}{(x-t)^2+y^2}\, dt

með því að
deilda undir heildið í hægri hliðinni.

Dæmi
^^^^

Sýnið að :math:`P_{\Bbb H_+}(\cdot,y)\to \delta_0` í veikum skilningi og
síðan að :math:`P_{\Bbb H_+}(\cdot,y)\ast \varphi(x)\to \varphi(x)`, ef
:math:`y\to 0`, fyrir sérhvert :math:`x\in {{\mathbb  R}}` og sérhvert
samfellt takmarkað fall :math:`\varphi`.

Dæmi
^^^^

Notið niðurstöðurnar úr dæmi 1 og 2 til þess að sanna að 

.. math::

  u(x,y)=P_{\Bbb H_+}(\cdot,y)\ast \varphi(x)=\dfrac y\pi\int_{-\infty}^{+\infty}
   \dfrac{\varphi(t)}{(x-t)^2+y^2}\, dt

sé lausnarformúla fyrir verkefnið 

.. math::

  \Delta u= 0  \quad \text { á  } \quad \Bbb H_+
   \qquad \text{ og } \qquad
   u={\varphi}   \quad \text{ á }  \quad  {{\mathbb  R}}.

Dæmi
^^^^

Notið speglunaraðferð og Green-fallið fyrir efra hálfplanið til þess að
finna Green-fallið fyrir fjórðunginn :math:`D=\{(x,y); x>0, y>0\}`.

Dæmi
^^^^

Sýnið að vörpunin :math:`z\mapsto z+1/z` varpi
:math:`X=\{z\in {{\mathbb  C}}; {{\operatorname{Im\, }}}z>0, |z|>1\}`
gagntækt á efra hálfplanið og ákvarðið síðan :math:`G_X`.

Dæmi
^^^^

Notið niðurstöðuna úr dæmi 2 til þess að finna :math:`G_X`, þar sem
:math:`X=\{z=x+iy\in{{\mathbb  C}}; |z|>1, 0<y<x\}`.

Dæmi
^^^^

Notið speglun og formúluna fyrir Green-fallið á hring til þess að finna
Green-fall á hálfhring
:math:`X=\{z; |z|<1, {{\operatorname{Im\, }}}z>0\}` og fjórðung úr hring
:math:`Y=\{z; |z|<1, {{\operatorname{Re\, }}}z>0, {{\operatorname{Im\, }}}z>0\}`.

Dæmi
^^^^

Notið formúluna 

.. math::

  P_X(z,{\zeta})=P_Y(F(z),F({\zeta}))|F{{^{\prime}}}({\zeta})|,
   \qquad z\in  X, \ {\zeta}\in {\partial}X.

til þess að reikna út Poisson-kjarnann
fyrir svæðið sem afmarkast af hjartaferlinum.

Dæmi
^^^^

Sýnið að Poisson-kjarninn fyrir kúluna :math:`D_a` í
:math:`{{\mathbb  R}}^3` er

.. math:: P_{D_a}(x,{\xi})=\dfrac{a^2-|x|^2}{4{\pi}|x-{\xi}|^3}.

Dæmi
^^^^

Sýnið að Poisson-kjarninn fyrir hálfrúmið :math:`\Bbb H_+` í
:math:`{{\mathbb  R}}^3` sé

.. math::

  P_{\Bbb H_+}(x,{\xi})=\dfrac{x_3}
   {2{\pi}\big((x_1-{\xi}_1)^2+(x_2-{\xi}_2)^2+x_3^2\big)^{3/2}}.

Dæmi
^^^^

Látum :math:`X` vera takmarkað svæði í :math:`{{\mathbb  R}}^n`,
:math:`F\in C( \overline X)` og gerum ráð fyrir að

.. math::

  \int_X F v\, dx=0, \qquad  v\in C(\overline X), \quad v=0
   \ \text { á } \ {\partial} X.

Sýnið að :math:`F` sé núllfallið. Gerum ráð fyrir að jaðarinn
:math:`{\partial} X` á :math:`X` sé sléttur og að

.. math:: \int_{\partial X} Fv  \, dS=0, \qquad   v\in C(\overline X).

Sýnið að :math:`F=0` á :math:`{\partial} X`.

Dæmi
^^^^

Látum :math:`X` vera takmarkað svæði í :math:`{{\mathbb  R}}^n` með
sléttan jaðar og gerum ráð fyrir að Neumann-verkefnið:
:math:`\Delta u=f` á :math:`X` og :math:`{\partial}u/ {\partial}n=g` á
:math:`{\partial}X`, hafi lausn. Sýnið að

.. math:: \int\limits_X f\, dx=\int\limits_{{\partial}X}g \, dS.

Skilgreinum orkuheildið fyrir Neumann-verkefnið með

.. math::

  E[w]=\tfrac 12 \int_X |\nabla w|^2\, dx -\int_{\partial X}g
   w\, dS,

þar sem :math:`w\in C^2(X)\cap C(\overline X)`. Sýnið að orkuheildið
taki lággildi í lausninni á Neumann-verkefninu.

Dæmi
^^^^

Látum :math:`X` vera takmarkað svæði í :math:`{{\mathbb  R}}^n` og gefum
okkur að til sé lausn á Robin-verkefninu

.. math::

  \Delta u=f   \quad \text{ á } \quad X  \qquad \text { og } \qquad
   \dfrac{{\partial}u}{{\partial} n}+{\alpha}u=h  \quad \text{ á } \quad 
   {\partial} X,

þar sem :math:`f` er samfellt fall á :math:`X`, :math:`{\alpha}` og
:math:`h` eru samfelld föll á jaðrinum :math:`{\partial} X` og
:math:`{\alpha}\geq 0` er ekki núllfallið. Sýnið að lausnin er ótvírætt
ákvörðuð. Setjið fram orkuheildi sem hefur lausnina sem lággildi.
