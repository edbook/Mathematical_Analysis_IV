=-0.4truecm =-1truecm =16truecm =23truecm =0truecm

#1#2 #1#2 0 1 0 = -1 0 by-1 1 = 1 2 = -0 2 by100 = 1 100 by2 100 by1 1 1
=-100 0 [section] [setning+] Skilgreining [setning+] Setning og
skilgreining [setning+] Hjálparsetning [setning+] Fylgisetning
[setning+] Sýnidæmi [setning+] Forrit

[1]*#1:*\ :math:`\blacksquare`

#1\ **#1.**   #1\ **#1.**   #1\ **#1.**

ÞÝÐ FÖLL OG FÁGAÐAR VARPANIR
============================

Þýð föll
--------

Laplace-virki, Laplace-jafna og þýð föll 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`X` tákna opið mengi í
:math:`{{\mathbb  C}}={{\mathbb  R}}^2` og látum
:math:`\varphi:X\to {{\mathbb  R}}` vera deildanlegt fall á :math:`X`.
Munum að *stigull* fallsins :math:`\varphi` er vigursviðið

.. math::

   \nabla \varphi=\big(\dfrac{\partial \varphi}{\partial x},
   \dfrac{\partial \varphi}{\partial y}\big).

 Munum einnig að fyrir deildanlegt vigursvið
:math:`\vec V=(p,q):X\to {{\mathbb  R}}^ 2` er *sundurleitni* þess
skilgreind sem fallið

.. math::

   \nabla\cdot \vec V=\dfrac{\partial p}{\partial x}+\dfrac{\partial
   q}{\partial y}.

 Ef við tengjum saman stigul og sundurleitni, þá fáum við

.. math::

   \nabla^2\varphi=\nabla\cdot (\nabla \varphi)= \dfrac {\partial^2 \varphi}{\partial x^2}+  
   \dfrac {\partial^2 \varphi}{\partial y^2}.

Skilgreining
^^^^^^^^^^^^

Látum :math:`\varphi:X\to {{\mathbb  R}}` vera tvisvar deildanlegt fall
á opnu hlutmengi :math:`X` í :math:`{{\mathbb  C}}`. Hlutafleiðuvirkinn

.. math::

   {\Delta}=\nabla^2=\dfrac {\partial^2 }{\partial x^2}+  
   \dfrac {\partial^2 }{\partial y^2}

 nefnist *Laplace-virki :hover:‘Laplace!virki‘ :hover:‘virki!Laplace‘*,
óhliðraða hlutafleiðujafnan :math:`{\Delta}\varphi=0` nefnist
*Laplace-jafna :hover:‘Laplace!jafna‘ :hover:‘jafna!Laplace‘* og lausn
:math:`\varphi:X\to {{\mathbb  R}}` á henni er sögð vera *þýtt fall
:hover:‘þýtt fall‘* á :math:`X`.

————–

Wirtinger-afleiðuvirkjarnir
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rifjum nú upp skilgreininguna á Wirtinger-afleiðuvirkjunum:

.. math::

   \dfrac{\partial}{\partial z}=\dfrac 12\bigg(\dfrac{\partial }{\partial x}-i
   \dfrac{\partial}{\partial y}\bigg)
   \qquad \text{ og } \qquad 
   \dfrac{\partial}{\partial \bar z}=\dfrac 12\bigg(\dfrac{\partial
   }{\partial x}+i \dfrac{\partial}{\partial y}\bigg)

 Með smá útreikningi sjáum við að

.. math::

   \Delta u=4\dfrac{\partial^2 u}{\partial z\partial \bar z}
   =4\dfrac{\partial^2 u}{\partial \bar z\partial z}

 og þar með er fallið :math:`u` er þýtt þá og því aðeins að
:math:`\partial^2 u/\partial z\partial\bar z =0`. Munum einnig að fall
:math:`f` er fágað þá og því aðeins að
:math:`\partial f/\partial \bar z=0`.

Tengsl við fáguð föll
~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f: X\to {{\mathbb  C}}`, :math:`f=u+iv` vera fágað fall þar
sem :math:`u={{\operatorname{Re\, }}}f` og
:math:`v={{\operatorname{Im\, }}}f` tákna raun- og þverhluta. Þá eru
bæði :math:`u` og :math:`v` óendanlega oft deildanleg föll og þau
uppfylla Cauchy-Riemann jöfnurnar

.. math::

   \dfrac{\partial u}{\partial x}
   =\dfrac{\partial v}{\partial y} \qquad \text{ og } \qquad
   \dfrac{\partial u}{\partial y}
   =-\dfrac{\partial v}{\partial x}.

 Við getum nú skrifað Cauchy-Riemann jöfnurnar sem

.. math::

   \nabla u=\big(\dfrac{\partial v}{\partial y},-\dfrac{\partial
   v}{\partial x}\big) \qquad \text{ og } \qquad
   \nabla v=\big(-\dfrac{\partial u}{\partial y},\dfrac{\partial
   u}{\partial x}\big).

 Af þessu leiðir að

.. math:: \nabla u\cdot \nabla v=0,

 sem segir okkur að stiglar :math:`u` og :math:`v` eru hornréttir.

Munum að raungilt á fall á svæði :math:`X` er fastafall þá og því aðeins
að stigull þess sé núll í sérhverjum punkti. Cauchy-Riemann jöfnurnar
segja okkur að :math:`u` sé fastafall þá og því aðeins að :math:`v` sé
fastafall.

Af Cauchy-Riemann jöfnunum leiðir einnig

.. math::

   \dfrac {\partial^2 u}{\partial x^2}+  
   \dfrac {\partial^2 u}{\partial y^2}
   =\dfrac{\partial^2 v}{\partial x\partial y}  
   -\dfrac{\partial^2 v}{\partial y\partial x}=0,

 af því að :math:`v` er óendanlega oft deildanlegt og
:math:`\partial^2 v/\partial x\partial y=\partial^2 v/\partial y\partial x`,
og einnig fæst að

.. math::

   \dfrac {\partial^2 v}{\partial x^2}+  
   \dfrac {\partial^2 v}{\partial y^2}
   =-\dfrac{\partial^2 u}{\partial x\partial y}  
   +\dfrac{\partial^2 u}{\partial y\partial x}=0.

 Við höfum því sannað:

Setning
^^^^^^^

Ef :math:`f` er fágað fall á opnu mengi :math:`X` í
:math:`{{\mathbb  C}}`, þá eru :math:`u={{\operatorname{Re\, }}}f` og
:math:`v={{\operatorname{Im\, }}}f` þýð föll og stiglar þeirra eru
hornréttir í sérhverjum punkti í :math:`X`. Ef :math:`X` er svæði og
annað hvort :math:`u` eða :math:`v` er fastafall, þá er hitt fallið það
líka.

————–

Gerum nú aftur ráð fyrir að :math:`u` sé þýtt fall á svæði :math:`X` í
:math:`{{\mathbb  C}}` og athugum hvernig hægt er að finna :math:`v`
þannig að :math:`u+iv` verði fágað fall. Gerum ráð fyrir að slíkt
:math:`v` sé til og setjum :math:`f=u+iv`. Þá er

.. math:: f'(z)=\dfrac{\partial u}{\partial x}+i\dfrac{\partial v}{\partial x}

 og fyrri Cauchy-Riemann-jafnan gefur að

.. math::

   f'(z)=\dfrac{\partial u}{\partial x}-i\dfrac{\partial u}{\partial y}
   =2\dfrac{\partial u}{\partial z}.

 Það er því nauðsynlegt skilyrði að afleiðan af :math:`f` sé gefin með
þessari formúlu. Athugum að fallið sem stendur í hægri hliðinni
uppfyllir Cauchy-Riemann-jöfnurnar og er þar með fágað, því ef við látum
virkjann :math:`\partial/\partial \bar z` verka á hægri hliðina þá fáum
við :math:`\partial^2u/\partial\bar z \partial z=0`.

Nú sjáum við að sérhvert þýtt fall á :math:`X` er raunhluti af fáguðu
falli þá og því aðeins að sérhvert fágað fall á :math:`X` hafi
stofnfall. Í 3. kafla sáum við að þetta einkennir einfaldlega
samanhangandi svæði:

Setning
^^^^^^^

Látum :math:`X` vera svæði í :math:`{{\mathbb  C}}`. Þá er sérhvert þýtt
fall á :math:`X` raunhluti af fáguðu falli þá og því aðeins að :math:`X`
sé einfaldlega samanhangandi. Ef :math:`a\in X` er fastur punktur þá er
fallið :math:`f` gefið með formúlunni

.. math::

   f(z)=u(a)+ic+2\int_{\gamma_z} \dfrac{\partial u}{\partial
   \zeta}(\zeta) \, d\zeta,

 þar sem :math:`\gamma_z` er einhver vegur í :math:`X` með upphafspunkt
:math:`a` og lokapunkt :math:`z` og :math:`c\in {{\mathbb  R}}` er
fasti.

————–

Athugið að veginn í setningunni má velja sem línustrik, ef :math:`X` er
stjörnusvæði með tilliti til :math:`a`.

Gerum nú ráð fyrir að :math:`u` sé þýtt fall á svæði :math:`Y` og að
:math:`g:X\to {{\mathbb  C}}` sé fágað fall á svæði
:math:`X\subset {{\mathbb  C}}` þannig að :math:`g(X)\subset Y`. Ef
:math:`a\in  X` þá er til opin skífa með miðju í :math:`g(a)` í
:math:`Y` þannig að :math:`u` er raunhluti fágaðs falls á :math:`f` á
skífunni. Þá verður samskeytingin :math:`u\circ g` raunhluti
:math:`f\circ g` sem er fágað fall í grennd um :math:`a`. Þetta segir
okkur að samskeyting af þýðu falli við fágað fall er þýtt fall.

Hagnýtingar í straumfræði
-------------------------

Hagnýtingar í straumfræði
~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`\vec V` vera vigursvið á opnu mengi :math:`X` í
:math:`{{\mathbb  R}}^2`. Við ætlum að líta á :math:`\vec V` sem
hraðasvið :hover:‘hraðasvið‘, sem er háð tveimur breytistærðum

.. math:: \vec V(x,y)= (p(x,y), q(x,y)), \qquad (x,y)\in X.

 *Straumlína :hover:‘straumlína‘* vigursviðsins :math:`\vec V` er ferill
:hover:‘ferill‘ :hover:‘ferill!einfaldur‘ :hover:‘ferill!lokaður‘ í
:math:`X` sem stikaður er með lausn :math:`\vec z:I\to {{\mathbb  R}}^2`
á

.. math::

   \vec z\, {{\sp{\prime}}}(t)=\vec V(\vec z(t)), \qquad t\in I,


   .. _4.7.1:

 á einhverju bili :math:`I` á :math:`{{\mathbb  R}}`. Þessi jafna
jafngildir afleiðujöfnuhneppinu

.. math::

   x{{\sp{\prime}}}=p(x,y), \qquad y{{\sp{\prime}}}=q(x,y).


   .. _4.7.2:

 Vigursviðið getur átt sér eðlisfræðilega túlkun. Við getum til dæmis
litið á :math:`\vec V` sem hraðasvið fyrir streymi vökva eða lofts.
Gengið er út frá því að streymið sé óháð tíma og einni rúmbreytistærð og
að það sé samsíða einhverju plani, sem við höfum valið sem
:math:`(x,y)`-plan. Straumlínurnar eru þá brautir agnanna í vökvanum eða
loftinu. :math:`\vec V` getur einnig verið hraðasvið rafstraums í þunnri
plötu og þá er :math:`\vec V` samsíða straumsviðinu í sérhverjum punkti.

Hugsum okkur nú að :math:`{\Omega}` sé hlutsvæði í :math:`X` með jaðar
:math:`{\partial} {\Omega}` í :math:`X` og gerum ráð fyrir að hægt sé að
stika :math:`{\partial}{\Omega}` með einföldum lokuðum ferli
:math:`{\gamma}`, sem er samfellt deildanlegur á köflum og
:math:`{\gamma}` stikar :math:`{\partial}{\Omega}` í jákvæða stefnu, en
það þýðir að svæðið :math:`{\Omega}` er vinstra megin við snertilínuna í
:math:`{\gamma}(t)`, ef horft er í stefnu snertilsins
:math:`{\gamma}{{\sp{\prime}}}(t)`. Ef
:math:`(x,y)={\gamma}(t)\in {\partial}{\Omega}` er punktur, þar sem
:math:`{\gamma}` er deildanlegt fall, þá skilgreinum við
*einingarsnertil :hover:‘einingarsnertill‘* :math:`\vec T(x,y)` í
:math:`(x,y)`, sem einingarvigurinn í stefnu
:math:`{\gamma}{{\sp{\prime}}}(t)`,
:math:`\vec T(x,y)={\gamma}{{\sp{\prime}}}(t)/|{\gamma}'(t)|`, og *ytri
einingarþvervigur :hover:‘einingarþverhringur‘ :hover:‘ytri
einingarþverhringur‘ á* :math:`{\partial}{\Omega}` sem einingarvigurinn
:math:`\vec n(x,y)` sem er hornréttur á
:math:`{\gamma}{{\sp{\prime}}}(t)` og vísar út úr :math:`{\Omega}`. Við
látum :math:`ds` tákna *bogalengdarfrymið :hover:‘bogalengdarfrymi‘*.
Með :math:`{\gamma}` sem stikun á :math:`{\partial}{\Omega}` er það
gefið sem :math:`ds=|{\gamma}{{\sp{\prime}}}(t)|\, dt`.

.. figure:: ./myndir/fig0328.svg

:align: center

:alt: Jaðar á svæði, snertill og þvervigur

2BeRemovedMynd: Jaðar á svæði, snertill og þvervigur

Gauss-setningin :hover:‘Gauss-setningin‘ :hover:‘setning!Gauss‘ gefur nú

.. math::

   \begin{aligned}
   \int_{\partial\Omega}(\vec V\cdot\vec n)\, ds
   &=\int_{{\gamma}}(\vec V\cdot\vec n)\, ds
   =\iint\limits_{{\Omega}} {{\operatorname{div}}}\vec V\, dxdy\\
   &=\iint\limits_{{\Omega}}
   \big({\partial}_xp(x,y)+{\partial}_yq(x,y)\big)\, dxdy.\nonumber\end{aligned}

 Heildið í vinstri hliðinne nefnist *flæði :hover:‘flæði‘ vigursviðsins*
:math:`\vec
V` yfir jaðarinn :math:`{\partial}{\Omega}`. Green-setningin
:hover:‘Green-setningin‘ :hover:‘setning!Green‘ gefur

.. math::

   \begin{aligned}
   \int_{\partial\Omega}(\vec V\cdot\vec T)\, ds
   &=\int_{{\gamma}}(\vec V\cdot\vec T)\, ds
   =\iint\limits_{{\Omega}} {{\operatorname{rot}}}\vec V\, dxdy\\
   &=\iint\limits_{{\Omega}}
   \big({\partial}_xq(x,y)-{\partial}_yp(x,y)\big)\, dxdy.\nonumber\end{aligned}

 Heildið í vinstri hliðinni nefnist *hringstreymi :hover:‘hringstreymi‘*
vigursviðsins :math:`\vec V` eftir jaðrinum :math:`{\partial}{\Omega}`.
Við gefum okkur nú tvær forsendur um hraðasviðið :math:`\vec V`:

(i) *Streymið er geymið*: Fyrir sérhvert :math:`{\Omega}\subset X` er
flæðið yfir :math:`{\partial}{\Omega}` jafnt :math:`0`. Þetta hefur í
för með sér að

.. math::

   \dfrac{\partial p}{\partial x}(x,y)+
   \dfrac{\partial q}{\partial y}(x,y)=0, \qquad (x,y)\in X.


   .. _4.7.5:

 Þessi jafna er oft nefnd *samfelldnijafna :hover:‘samfelldnijafna‘*.
Þetta er lögmálið um varðveislu massans, ef :math:`\vec V` er hraðasvið
fyrir vökvastreymi, en lögmálið um varðveislu hleðslunnar, ef
:math:`\vec V` er hraðasvið rafstraums.

(ii) *Streymið er án hvirfla*: Fyrir sérhvert :math:`{\Omega}` er
hringstreymi :math:`\vec V` eftir jaðrinum :math:`{\partial}{\Omega}`
jafnt :math:`0`. Þetta hefur í för með sér að

.. math::

   \dfrac{\partial q}{\partial x}(x,y)-
   \dfrac{\partial p}{\partial y}(x,y)=0, \qquad (x,y)\in X.


   .. _4.7.6:

 Ein mikilvæg afleiðing þessa skilyrðis er að í streyminu geta ekki
verið *hvirflar :hover:‘hvirfill‘*, en það eru lokaðar straumlínur, sem
mynda jaðar á svæði :math:`{\Omega}\subset X`. Hugsum okkur að
:math:`\vec z:[a,b]\to {{\mathbb  R}}^2` væri slík straumlína. Þá er
:math:`\vec T(\vec z(t))=\pm z{{\sp{\prime}}}(t)/|z{{\sp{\prime}}}(t)|`,
:math:`\vec V(\vec z(t))= z{{\sp{\prime}}}(t)`,
:math:`ds=|z{{\sp{\prime}}}(t)|\, dt` og þar með

.. math::

   \int_{{\partial}{\Omega}} \vec V\cdot \vec T\, ds =
   \pm\int_a^b |z{{\sp{\prime}}}(t)|^2\, dt \neq 0.

Nú skulum við skrifa :math:`\vec V` sem tvinnfall,
:math:`V(z)=p(z)+iq(z)`. Hlutafleiðujöfnurnar hér að framan segja að
:math:`\overline  V=p-iq` uppfylli Cauchy-Riemann-jöfnurnar og þar með
er fallið :math:`\overline V` fágað. Hugsum okkur að :math:`\overline V`
hafi stofnfall :hover:‘stofnfall‘, sem við táknum með :math:`f`. Ef
:math:`{\varphi}={{\operatorname{Re\, }}}f` og
:math:`{\psi}={{\operatorname{Im\, }}}f`, þá leiðir af
Cauchy-Riemann-jöfnunum að

.. math::

   f{{\sp{\prime}}}(z)=\partial_x\varphi(z)+i\partial_x\psi(z)
   =\partial_x\varphi(z)-i\partial_y\varphi(z)
   =p(z)-iq(z).

 Við höfum því :math:`{{\operatorname{grad}}}\varphi=\vec V=(p,q)`, svo
straumlínurnar eru hornréttar á jafnhæðarlínurnar :hover:‘jafnhæðarlína‘
:math:`\{z; \varphi(z)=c\}`, þar sem :math:`c` er fasti. Nú gefa
Cauchy-Riemann-jöfnurnar hins vegar að
:math:`{{\operatorname{grad}}}\psi=(\partial_x\psi,
\partial_y\psi)` er hornréttur á
:math:`{{\operatorname{grad}}}\varphi=(\partial_x\varphi,
\partial_y\varphi)` og þar með eru staumlínurnar fyrir vigursviðið
:math:`\vec V` gefnar sem jafnhæðarlínurnar :math:`\{z; \psi(z)=c\}`,
þar sem :math:`c` fasti.

Fallið :math:`f` kallast *tvinnmætti :hover:‘tvinnmætti‘* fyrir
straumfallið :math:`V`, fallið :math:`\varphi` kallast *raunmætti
:hover:‘raunmætti‘* fyrir :math:`V` og fallið :math:`\psi` kallast
*streymisfall :hover:‘streymisfall‘*. Niðurstaða athugana okkar er því
að straumlínur vigursviðsins :math:`\vec V` eru jafnhæðarlínur
streymisfallsins :math:`\psi`, þar sem
:math:`\psi= {{\operatorname{Im\, }}}f` og
:math:`f{{\sp{\prime}}}= \overline
V`. Ef við þekkjum streymisfallið :math:`{\psi}` og getum ákvarðað
jafnhæðarlínur þess, þá höfum við ákvarðað brautir lausna
afleiðujöfnuhneppisins

.. math:: x{{\sp{\prime}}}=p(x,y), \qquad y{{\sp{\prime}}}=q(x,y).

 án þess að leysa jöfnurnar.

Sýnidæmi
^^^^^^^^

Lítum fyrst á hraðasviðið :math:`V` sem gefið er með

.. math::

   V(z)=\dfrac a{\overline z}= a\dfrac {e\sp{i\theta}}r, \qquad
   z=re\sp{i\theta}, \quad z\in {{\mathbb  C}}\setminus{{\{0\}}},


   .. _4.7.7:

 þar sem :math:`a\in {{\mathbb  R}}`. Fallið :math:`\overline V` hefur
ekkert stofnfall á öllu :math:`{{\mathbb  C}}\setminus {{\{0\}}}`, en á
menginu :math:`X={{\mathbb  C}}\setminus {{\mathbb  R}}_-` getum við
tekið

.. math:: f(z)=a{{\operatorname{Log}}}z=a(\ln |z|+i\theta(z)),  \qquad -\pi<\theta(z)<\pi,

 fyrir stofnfall, þar sem :math:`{{\operatorname{Log}}}` táknar
höfuðgrein lografallsins. Straumlínurnar verða þá jafnhæðarlínur fyrir
hornið :math:`\{z;
\theta(z)=c\}`, en þær eru geislar út frá :math:`0`. Heildarflæði
straumfallsins gegnum hring með geislann :math:`r` er

.. math::

   \int_{|z|=r}{{\langle\vec V,\vec n\rangle}} \, ds=
   \int_0\sp{2\pi}\dfrac ar \, rd\theta=2\pi a.

 Ef :math:`a>0` þá stefna straumlínurnar út frá :math:`0` og þetta
straumfall er til komið af *uppsprettu :hover:‘uppspretta‘* í punktinum
:math:`0` með styrkinn :math:`2\pi a`. Ef :math:`a<0` þá er straumfallið
til komið af *svelg :hover:‘svelgur‘* í punktinum :math:`0` með styrkinn
:math:`2\pi a`.

————–

.. figure:: ./myndir/fig0319.svg

:align: center

:alt: Punktuppspretta

2BeRemovedMynd: Punktuppspretta

Sýnidæmi
^^^^^^^^

Lítum nú á fallið :math:`V` sem gefið er með

.. math::

   V(z)=\dfrac {ib}{\overline z}= ib\dfrac {e\sp{i\theta}}r, \qquad
   z=re\sp{i\theta}, \quad z\in X={{\mathbb  C}}\setminus{{\{0\}}},


   .. _4.7.8:

 þar sem :math:`b\in {{\mathbb  R}}`. Hér er hraðavigurinn í stefnu
:math:`ie\sp{i\theta}` og þar með hornréttur á stöðuvigurinn. Á menginu
:math:`X={{\mathbb  C}}\setminus {{\mathbb  R}}_-` höfum við tvinnmættið

.. math:: f(z)=-ib{{\operatorname{Log}}}z=b(\theta(z)-i\ln |z|).

 Hér verða straumlínurnar :math:`\{z; \ln|z|=c\}` hringir með miðju í
:math:`0`. Hringstreymi vigursviðsins :math:`\vec V` eftir hring með
geisla :math:`r` er

.. math::

   \int_{|z|=r}{{\langle\vec V,\vec T\rangle}} \, ds=
   \int_0\sp{2\pi}\dfrac br \, rd\theta=2\pi b.

 Þetta mætti er sagt lýsa *hringstreymi :hover:‘hringstreymi‘* umhverfis
*hvirfilpunkt* með styrk :math:`2\pi b` í :math:`0`.

————–

.. figure:: ./myndir/fig0320.svg

:align: center

:alt: Hringstreymi

2BeRemovedMynd: Hringstreymi

Sýnidæmi
^^^^^^^^

Lítum á enn eitt afbrigðið,

.. math::

   V(z)=\dfrac {(a+ib)}{\overline z}= (a+ib)\dfrac {e\sp{i\theta}}r, \qquad
   z=re\sp{i\theta}, \quad z\in {{\mathbb  C}}\setminus{{\{0\}}},


   .. _4.7.9:

 þar sem :math:`a,b\in {{\mathbb  R}}`. Hér tvinnmætti á menginu
:math:`{{\mathbb  C}}\setminus {{\mathbb  R}}_-` gefið með

.. math:: f(z)=(a-ib){{\operatorname{Log}}}z=(a\ln |z| + b\theta(z))+i(a\theta(z)-b\ln |z|).

 Straumlínurnar eru :math:`\{z;a\theta(z)-b\ln |z|=c\}`. Í pólhnitum eru
þær gefnar með jöfnunni :math:`r=e\sp{(a\theta-c)/b}`, en þetta eru
*skrúflínur :hover:‘skrúflína‘* eða *iðustreymi :hover:‘iðustrymi‘* út
frá :math:`0`. Þetta mætti er myndað af straumuppsprettu með styrkinn
:math:`2\pi a` og hvirfilpunkti með styrkinn :math:`2\pi b` í :math:`0`.

————–

.. figure:: ./myndir/fig0321.svg

:align: center

:alt: Iðustreymi

2BeRemovedMynd: Iðustreymi

Sýnidæmi
^^^^^^^^

Lítum nú á dæmið þar sem tvær uppsprettur með styrk :math:`2\pi a` eru í
punktunum :math:`\alpha` og :math:`-\alpha` á raunásnum. Straumfallið
verður þá

.. math:: V(z)= \dfrac a{\overline z+\alpha}+\dfrac a{\overline z-\alpha},

 og sem tvinnmætti á
:math:`{{\mathbb  C}}\setminus\{x\in {{\mathbb  R}}; x\leq \alpha\}`
getum við tekið

.. math::

   \begin{aligned}
   f(z)&= a{{\operatorname{Log}}}(z+\alpha)+a{{\operatorname{Log}}}(z-\alpha) \\
   &=
   a(\ln|z+\alpha|+\ln|z-\alpha|)+ia(\theta(z+\alpha)+\theta(z-\alpha)).\end{aligned}

Við sjáum vð þverásinn er straumlína, því þar er
:math:`\theta(iy+\alpha)+\theta(iy-\alpha)={\pi}`, ef :math:`y>0` og
:math:`\theta(iy+\alpha)+\theta(iy-\alpha)=-{\pi}`, ef :math:`y<0`.
Straumvigurinn er í stefnu þverássins, upp ef :math:`y>0` og niður ef
:math:`y<0`, því

.. math::

   V(z)=\dfrac{2a\overline z}{\overline z\sp 2-\alpha\sp 2},\qquad
   V(iy)=\dfrac{2ayi}{y\sp 2+\alpha\sp 2}.

 Við getum einnig notað þetta fall til þess að lýsa streymi út frá
uppsprettu í punktinum :math:`\alpha` af styrk :math:`2\pi a` í
hálfplaninu
:math:`\{z\in {{\mathbb  C}}; {{\operatorname{Re\, }}}z>0\}`, þar sem
litið er á þverásinn sem vegg.

————–

.. figure:: ./myndir/fig0322.svg

:align: center

:alt: Straumuppspretta við vegg

2BeRemovedMynd: Straumuppspretta við vegg

Sýnidæmi
^^^^^^^^

Lítum nú á mættið sem til er komið vegna uppsprettu af styrk
:math:`2\pi a` í punktinum :math:`\alpha` og svelgs af styrk
:math:`2\pi a` í punktinum :math:`-\alpha`. Straumfallið verður

.. math:: V(z)=\dfrac {a}{\overline z-\alpha}-\dfrac a{\overline z+\alpha}.

 Tvinnmættið á
:math:`{{\mathbb  C}}\setminus\{x\in {{\mathbb  R}}; x\leq \alpha\}`
getum við valið sem

.. math::

   f(z)=a{{\operatorname{Log}}}(z-\alpha)-a{{\operatorname{Log}}}(z+\alpha)=
   a\ln\bigg|\dfrac{z-\alpha}{z+\alpha}
   \bigg | +ia\theta\bigg(\dfrac{z-\alpha}{z+\alpha}\bigg).

 Talan :math:`\theta((z-\alpha)/(z+\alpha))` er hornið sem bilið
:math:`[-\alpha,\alpha]` sést undir miðað við punktinn :math:`z`. Við
getum lýst straumlínu :math:`\{z\in {{\mathbb  C}}; 
\theta((z-\alpha)/(z+\alpha))=c\}` fyrir þetta streymi, sem mengi allra
punkta sem eru þannig að bilið :math:`[-\alpha,\alpha]` sést undir
horninu :math:`c` frá :math:`z`. Við sjáum að

.. math::

   w=\dfrac{z-\alpha}{z+\alpha} \qquad \Leftrightarrow \qquad 
   z=\dfrac {\alpha w+\alpha}{-w+1}=-\alpha\dfrac{w+1}{w-1}.

 Straumlínurnar eru gefnar sem :math:`\theta(w)=c`, sem eru hálflínur út
frá :math:`0` í :math:`w`-planinu með stefnuvigur :math:`e^{ic}`. Við
sjáum að :math:`w=0 \Leftrightarrow z=\alpha` og
:math:`w=\infty \Leftrightarrow z=-\alpha`. Straumlínurnar eru því
hringbogar frá :math:`\alpha` til :math:`-\alpha`. Jafnmættislínurnar
eru síðan gefnar með jöfnum af gerðinni

.. math:: \bigg| \dfrac{z-{\alpha}}{z+{\alpha}} \bigg|^2=c,

 þar sem :math:`c>0`. Ef :math:`c=1`, þá er þetta þverásinn, en fyrir
:math:`c\neq 1` er þetta hringur.

————–

.. figure:: ./myndir/fig0323.svg

:align: center

:alt: Straumuppspretta í :math:`-\alpha` og svelgur í :math:`+\alpha`

2BeRemovedMynd: Straumuppspretta í :math:`-\alpha` og svelgur í
:math:`+\alpha`

Sýnidæmi
^^^^^^^^

Lítum nú á fallið :math:`f:X\to {{\mathbb  C}}`,

.. math::

   f(z)=\arcsin z, \qquad
   z\in X={{\mathbb  C}}\setminus\{x\in {{\mathbb  R}}; |x|\geq 1\}.

 sem tvinnmætti. Við skrifum :math:`w=\arcsin z`, :math:`z=x+iy` og
:math:`w=u+iv`. Þá er :math:`-{\pi}/2<u<{\pi}/2` og

.. math::

   \begin{aligned}
   z&=x+iy=\sin w=\sin(u+iv)\\
   &=\sin u\cos(iv)+\cos u\sin(iv)\\
   &=\sin u\cosh v+i\cos u\sinh v.\end{aligned}

 Straumlínurnar eru því gefnar sem
:math:`{\psi}(z)={{\operatorname{Im\, }}}\arcsin z=v=\text{fasti}` og
við sjáum að jöfnur þeirra í :math:`z`-planinu eru

.. math::

   \dfrac{x^2}{\cosh^2 v}+\dfrac{y^2}{\sinh^2 v}=
   \sin^2u+\cos^2u=1.

 Þetta eru sporbaugar með hálfásana :math:`a=\cosh v` og
:math:`b=\sinh v`. Jafnmættislínurnar eru hins vegar gefnar sem
:math:`{\varphi}(z)={{\operatorname{Re\, }}}\arcsin z=u=\text{fasti}` og
jöfnur þeirra í :math:`z`-planinu eru

.. math::

   \dfrac{x^2}{\sin^2 u}-\dfrac{y^2}{\cos^2 u}=
   \cosh^2v-\sinh^2v=1.

 Þetta eru jöfnur fyrir breiðboga.

.. figure:: ./myndir/fig0326.svg

:align: center

:alt: Tvinnmættið :math:`f(z)=\arcsin z`

2BeRemovedMynd: Tvinnmættið :math:`f(z)=\arcsin z`

Ef við lítum á fallið :math:`g(z)=-i\arcsin z`, þá skipta straumlínur og
jafnmættislínur um hlutverk og breiðbogarnir verða straumlínur. Við
tökum eftir því að þverásinn er straumlína. Við getum því túlkað þetta
sem mætti fyrir streymi gegnum hlið :hover:‘streymi!gegnum hlið‘.

.. figure:: ./myndir/fig0327.svg

:align: center

:alt: Streymi gegnum hlið

2BeRemovedMynd: Streymi gegnum hlið

————–
