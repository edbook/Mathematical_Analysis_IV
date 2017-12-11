TVINNTÖLUR
==========

Talnakerfin
-----------

Þetta er breyting

:math:`{{\mathbb  N}}`, :math:`{{\mathbb  Z}}`, :math:`{{\mathbb  Q}}`,
:math:`{{\mathbb  R}}` og :math:`{{\mathbb  C}}`.

Rauntölur
~~~~~~~~~

Til sérhvers punkts á línu svarar nákvæmlega ein tala :math:`a`.
:math:`{{\mathbb  R}}` táknar mengi allra slíkra talna. Aðgerðirnar
samlagning og margföldun eru skilgreindar með færslum á punktum á
línunni.

.. figure:: ./myndir/siiibk01m01.svg
    :align: center
    :alt:

     

Sérhver rauntala sem ekki er ræð tala nefnist *óræð tala*. Ekki er neitt
sérstakt tákn notað fyrir mengi óræðra talna í stærðfræðinni, svo það er
oftast táknað :math:`{{\mathbb  R}}\setminus {{\mathbb  Q}}`.

Rauntölurnar uppfylla allar sömu reiknireglur of ræðar tölur, þannig að
fyrir rauntölur :math:`a`, :math:`b` og :math:`c` höfum við

+---------------------------+----------------------------------------+
| :math:`(a+b)+c=a+(b+c)`   | *tengiregla fyrir samlagningu*         |
+---------------------------+----------------------------------------+
| :math:`(ab)c=a(bc)`       | *tengiregla fyrir margföldun*          |
+---------------------------+----------------------------------------+
| :math:`a+b=b+a`           | *víxlegra fyrir samlagningu*           |
+---------------------------+----------------------------------------+
| :math:`ab=ba`             | *víxlegra fyrir margföldun*            |
+---------------------------+----------------------------------------+
| :math:`a(b+c)=ab+ac`      | *dreifiregla*                          |
+---------------------------+----------------------------------------+
| :math:`a+0=a`             | :math:`0` *er samlagningarhlutleysa*   |
+---------------------------+----------------------------------------+
| :math:`1a=a`              | :math:`1` *er margföldunarhlutleysa*   |
+---------------------------+----------------------------------------+

Sérhver rauntala :math:`a` á sér samlagningarandhverfu sem er ótvírætt
ákvörðuð og við táknum hana með :math:`-a` og sérhver rauntala
:math:`a\neq 0` á sér margföldunarandhverfu :math:`a^{-1}` sem er
ótvírætt ákvörðuð. Við athugum að :math:`a^{-1}=1/a`.

Við höfum röðun :math:`<` á :math:`{{\mathbb  R}}` sem er þannig að um
sérhverjar tvær tölur :math:`a` og :math:`b` gildir eitt af þrennu
:math:`a<b`, :math:`a=b` eða :math:`b<a`. Við skrifum einnig :math:`a>b`
ef :math:`b<a`. Við höfum eftirtaldar reglur um röðun rauntalna

+------------------------------------------------------+--------------------------------------+
| ef :math:`a<b` og :math:`b<c`, þá er :math:`a<c`     | *röðun er gegnvirk*                  |
+------------------------------------------------------+--------------------------------------+
| ef :math:`a<b` þá er :math:`a+c<b+c`                 | *röðun er óbreytt við samlagningu*   |
+------------------------------------------------------+--------------------------------------+
| ef :math:`a<b` og :math:`c>0`, þá er :math:`ac<bc`   | *röðun er óbreytt við margföldun*    |
+------------------------------------------------------+--------------------------------------+
|                                                      | *með jákvæðri tölu*                  |
+------------------------------------------------------+--------------------------------------+
| ef :math:`a<b` og :math:`c<0`, þá er :math:`bc<ac`   | *röðun er viðsnúin við margföldun*   |
+------------------------------------------------------+--------------------------------------+
|                                                      | *með neikvæðri tölu*                 |
+------------------------------------------------------+--------------------------------------+

Við höfum líka *hlutröðun* :math:`\leq` á :math:`{{\mathbb  R}}`. Við
skrifum :math:`a\leq b` og segjum að :math:`a` *sé minni eða jafnt*
:math:`b`, ef :math:`a<b` eða :math:`a=b`. Eins skrifum við
:math:`a\geq b` og segjum að :math:`a` *sé stærri eða jafnt* :math:`b`
ef :math:`a>b` eða :math:`a=b`.

Ef :math:`a,b\in {{\mathbb  R}}` og :math:`a<b`, þá skilgreinum við
mismunandi bil.

+------------------------------------------------------------+----------------------------+
| :math:`]a,b[=\{x\in {{\mathbb  R}}\,;\, a<x<b\}`           | *opið bil*                 |
+------------------------------------------------------------+----------------------------+
| :math:`[a,b]=\{x\in {{\mathbb  R}}\,;\, a\leq x\leq b\}`   | *lokað bil*                |
+------------------------------------------------------------+----------------------------+
| :math:`[a,b[=\{x\in {{\mathbb  R}}\,;\, a\leq x<b\}`       | *hálf-opið bil*            |
+------------------------------------------------------------+----------------------------+
| :math:`]a,b]=\{x\in {{\mathbb  R}}\,;\, a<x\leq b\}`       | *hálf-opið bil*            |
+------------------------------------------------------------+----------------------------+
| :math:`]-\infty,a[=\{x\in {{\mathbb  R}}\,;\, x<a\}`       | *opin vinstri hálflína*    |
+------------------------------------------------------------+----------------------------+
| :math:`]-\infty,a]=\{x\in {{\mathbb  R}}\,;\, x\leq a\}`   | *lokuð vinstri hálflína*   |
+------------------------------------------------------------+----------------------------+
| :math:`]a,\infty[=\{x\in {{\mathbb  R}}\,;\, x>a\}`        | *opin hægri hálflína*      |
+------------------------------------------------------------+----------------------------+
| :math:`[a,\infty[=\{x\in {{\mathbb  R}}\,;\, x\geq a\}`    | *lokuð hægri hálflína*     |
+------------------------------------------------------------+----------------------------+
| :math:`]-\infty,\infty[={{\mathbb  R}}`                    | *öll rauntalnalínan*       |
+------------------------------------------------------------+----------------------------+
| :math:`[a,a]`                                              | *eins punkts bil*          |
+------------------------------------------------------------+----------------------------+

Stundum er skrifað :math:`(a,b)` í stað :math:`]a,b[`, :math:`(a,b]` í
stað :math:`]a,b]` o.s.frv.

Á sérhverju opnu bili eru óendanlega margar ræðar tölur og óendanlega
margar óræðar tölur.

Fyrir sérhvert :math:`x\in {{\mathbb  R}}` skilgreinum við :hover:`tölugildið, tölugildi`
af :math:`x` með

.. math::

  |x|=\begin{cases}
   x &x\geq 0, \\
   -x &x <0. 
   \end{cases}

Talan :math:`|x|` mælir fjarlægð milli :math:`0` og :math:`x` á
talnalínunni. Ef gefnar eru tvær rauntölur :math:`x` og :math:`y`, þá
mælir :math:`|x-y|` fjarlægðina á milli þeirra. Ef :math:`a` og
:math:`\varepsilon` eru rauntölur og :math:`\varepsilon>0`, þá er

.. math:: \{x\in {{\mathbb  R}}\,;\,  |x-a|<\varepsilon\}=(a-\varepsilon,a+\varepsilon)

opið bil með miðju í :math:`a` og þvermálið :math:`2\varepsilon`.

Takmarkanir rauntalnakerfisins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum séð að öll talnakerfin :math:`{{\mathbb  N}}`,
:math:`{{\mathbb  Z}}` og :math:`{{\mathbb  Q}}` hafa sínar takmarkanir
og það sama á við um rauntölurnar :math:`{{\mathbb  R}}`.

Í :math:`{{\mathbb  N}}` náttúrlegra talna er frádráttur ófullkomin
aðgerð.

Í :math:`{{\mathbb  Z}}` er deiling ófullkomin aðgerð.

Ræðu tölurnar :math:`{{\mathbb  Q}}` duga ekki til þess að lýsa lengdum
á strikum og ferlum sem koma fyrir í rúmfræðinni.

Við vitum að rauntala í öðru veldi er alltaf stærri eða jöfn núlli svo
jafnan :math:`x^2+1=0` getur ekki haft lausn.

Sama er að segja um annars stigs jöfnuna :math:`ax^2+bx+c=0`,
:math:`a\neq 0`. Hún hefur enga lausn ef :math:`D=b^2-4ac<0`. Það er
auðvelt að skrifa niður dæmi um margliður sem hafa engar núllstöðvar í
:math:`{{\mathbb  R}}`, en stig þeirra þarf að vera slétt tala, því
margliður af oddatölustigi hafa alltaf núllstöð.

Nú er eðlilegt að spyrja, hvort hægt sé að stækka rauntalnakerfið yfir í
stærra mengi þannig að innan þess mengis sé hægt að finna lausn á annars
stigs jöfnunni :math:`x^2+1=0` og hvort slíkt talnakerfi gefi af sér
lausnir á fleiri jöfnum sem ekki eru leysanlegar í
:math:`{{\mathbb  R}}`.

Tvinntalnaplanið
----------------

:math:`{{\mathbb  C}}` er útvíkkun á :math:`{{\mathbb  R}}` þar sem til
er tala :math:`i` sem uppfyllir :math:`i^2=-1`.

Skilgreining á tvinntölum
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./myndir/siiibmynd0101.svg
    :align: center
    :alt: Hnit punkts í plani

    Mynd: Hnit punkts í plani

Lítum nú á mengi allra vigra í plani. Sérhver vigur hefur hnit
:math:`(a,b)\in {{\mathbb  R}}^2` sem segja okkur hvar lokapunktur
vigurs er staðsettur ef upphafspunktur hans er settur í upphafspunkt
hnitakerfisins. Á mengi allra vigra höfum við tvær aðgerðir, samlagningu
og margföldun með tölu. Samlagningunni er lýst með hnitum,

.. math:: (a,b)+(c,d)=(a+c,b+d).

og margfeldi tölunnar :math:`a` og vigursins :math:`(c,d)` er

.. math:: a(c,d)=(ac,ad).

Við skilgreinum nú margföldun á :math:`{{\mathbb  R}}^2` með hliðsjón
af formúlunni sem við uppgötvuðum hér að framan,

.. math:: (a,b)(c,d)=(ac-bd,ad+bc).

Talnaplanið :math:`{{\mathbb  R}}^2` með venjulegri samlagningu og
þessari margföldun nefnist *tvinntölur* og er táknað með
:math:`{{\mathbb  C}}`. Nú er auðvelt að sannfæra sig um að víxl-,
tengi- og dreifireglur gildi um þessa margföldun

+-------------------------------------------------------------------+--------------------------------------------+
| :math:`\big((a,b)+(c,d)\big)+(e,f)=(a,b)+\big((c,d)+(e,f)\big)`   | *tengiregla fyrir samlagningu*             |
+-------------------------------------------------------------------+--------------------------------------------+
| :math:`\big((a,b)(c,d)\big)(e,f)=(a,b)\big((c,d)(e,f)\big)`       | *tengiregla fyrir margföldun*              |
+-------------------------------------------------------------------+--------------------------------------------+
| :math:`(a,b)+(c,d)=(c,d)+(a,b)`                                   | *víxlregla fyrir samlagningu*              |
+-------------------------------------------------------------------+--------------------------------------------+
| :math:`(a,b)(c,d)=(c,d)(a,b)`                                     | *víxlregla fyrir margföldun*               |
+-------------------------------------------------------------------+--------------------------------------------+
| :math:`(a,b)\big((c,d)+(e,f)\big) =(a,b)(c,d)+(a,b)(e,f)`         | *dreifiregla*                              |
+-------------------------------------------------------------------+--------------------------------------------+
| :math:`(a,b)+(0,0)=(a,b)`                                         | :math:`(0,0)` *er samlagningarhlutleysa*   |
+-------------------------------------------------------------------+--------------------------------------------+
| :math:`(1,0)(a,b)=(a,b)`                                          | :math:`(1,0)` *er margföldunarhlutleysa*   |
+-------------------------------------------------------------------+--------------------------------------------+

Talan :math:`(-a,-b)` er samlagningarandhverfa :math:`(a,b)`.

Jafnan :math:`(a,b)(a,-b)=(a^2+b^2,0)` segir okkur að talan
:math:`(a,b)\neq (0,0)` eigi sér margföldunarandhverfuna

.. math:: (\dfrac a{a^2+b^2},\dfrac{-b}{a^2+b^2}).

Við tökum eftir að

.. math:: (a,0)(c,d)=(ac,ad)=a(c,d).

sem segir okkur að margföldun með vigrinum :math:`(a,0)` sé það sama og
margföldun með tölunni :math:`a`.

Vigrar af gerðinni :math:`(a,0)` haga sér eins og rauntölur því

.. math::

  (a,0)+(b,0)=(a+b,0) \qquad \text{ og } \qquad 
   (a,0)(b,0)=(ab,0).

Í :math:`{{\mathbb  C}}` gerum við því ekki greinarmun á rauntölunni
:math:`a` og vigrinum :math:`(a,0)` og lítum á lárétta hnitaásinn
:math:`\{(x,0)\in{{\mathbb  R}}^2\,;\, x\in {{\mathbb  R}}\}` sem
rauntalnalínuna :math:`{{\mathbb  R}}`. Við skrifum þá sérstaklega
:math:`1` í stað :math:`(1,0)` og :math:`0` í stað :math:`(0,0)`

Lítum nú á vigurinn :math:`(0,1)` sem við táknum með :math:`i`. Um hann
gildir

.. math:: i^2=(0,1)^2=(0,1)(0,1)=(-1,0)=-1.

Sérhvern vigur :math:`(a,b)` má skrifa sem samantekt
:math:`(a,b)=a(1,0)+b(0,1)` Við skrifum :math:`a` og :math:`b` í stað
:math:`(a,0)` og :math:`(b,0)` og erum þar með komin með framsetninguna

.. math:: (a,b)=(a,0)(1,0)+(b,0)(0,1)=a+ib.

Veldareglur
~~~~~~~~~~~

Ef :math:`z` er tvinntala þá getum við skilgreint heiltöluveldi þannig
að :math:`z^0=1`, :math:`z^1=z`, og :math:`z^n=z\cdots z` þar sem allir
þættirnir eru eins og fjöldi þeirra er :math:`n\geq 2`. 

Fyrir :math:`z\neq 0` eru neikvæðu veldin skilgreind þannig að :math:`z^{-1}` er margföldunarandhverfan af :math:`z` og fyrir neikvæð :math:`n` er :math:`z^n=(z^{-1})^{|n|}`. 

Með þessu fást sömu veldareglur og gilda um rauntölur

.. math::

  \begin{aligned}
   z^n\cdot z^m&=z^{n+m}\\
   \dfrac {z^n}{z^m}&=z^{n-m}\\
   z^n\cdot w^n&=(zw)^n\\
   (z^n)^m&=z^{nm}\end{aligned}

Tvíliðureglan
~~~~~~~~~~~~~

Tvíliðureglan er eins fyrir tvinntölur og rauntölur,

.. math:: (a+b)^n=\sum_{k=0}^n\binom nk a^kb^{n-k}

þar sem :hover:`tvíliðustuðlarnir,tvíliðustuðull` eru gefnir með

.. math:: \binom nk=\dfrac{n(n-1)\cdots(n-k+1)}{k!}=\dfrac{n!}{(n-k)!k!},

fyrir :math:`n=0,1,2,3,\dots` og :math:`k=0,\dots,n`.

Við köllum þennan stuðul :math:`n` *yfir* :math:`k`.

Tvíliðustuðlarnir eru samhverfir í þeim skilningi að

.. math:: \binom nk=\binom n{n-k}.

Tvíliðustuðlarnir uppfylla

.. math:: \binom n0=\binom nn=1

fyrir :math:`n=0,1,2,\dots` og rakningarformúluna

.. math:: \binom nk=\binom{n-1}{k-1}+\binom{n-1}k,

fyrir :math:`n=2,3,4,\dots` og :math:`k=1,2,\dots,n-1`. Þessari
rakningu er best lýst í þríhyrningi Pascals, en línurnar í honum geyma
alla tvíliðurstuðlana. Fyrstu :math:`7` línurnar, :math:`n=0,\dots,6`, í
honum eru

.. math::

  \begin{array}{ccccccccccccc}
    & & & & & & 1 & & & & & &\\
    & & & & & 1 & &1& & & & &\\
    & & & & 1 & &2 & &1 & & & &\\
    & & & 1 & &3 & &3& &1 & & &\\
    & & 1 & &4 & &6& &4& &1 & &\\
    & 1 & &5& &10& &10& &5  & &1 &\\
   1 & &6& &15& &20& &15 & & 6 & & 1
   \end{array}

Raunhluti, þverhluti og samok
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sérhverja tvinntölu :math:`z` má rita sem :math:`z=x+iy` þar sem
:math:`x` og :math:`y` eru rauntölur. Talan :math:`x` nefnist þá
:hover:`raunhluti` tölunnar :math:`z` og talan :math:`y` nefnist :hover:`þverhluti`
hennar. Við táknum raunhlutann með :math:`{{\operatorname{Re\, }}}z` og
þverhlutann með :math:`{{\operatorname{Im\, }}}z`.

Tvinntala :math:`z` er sögð vera *rauntala* ef
:math:`{{\operatorname{Im\, }}}z=0` og hún er sögð vera *hrein þvertala*
ef :math:`{{\operatorname{Re\, }}}z=0`.

Ef :math:`z\in {{\mathbb  C}}`, :math:`x={{\operatorname{Re\, }}}z` og
:math:`y={{\operatorname{Im\, }}}z`, þá nefnist talan
:math:`\bar z=x-iy` :hover:`samok` tölunnar :math:`z`. Athugið að
:math:`\bar z` er spegilmynd :math:`z` í raunásnum og því er
:math:`\bar{\bar z}=z`. Við höfum nokkrar reiknireglur um samok

.. math::

  \begin{aligned}
   z\bar z&=(x+iy)(x-iy)=x^2+y^2  \\
   z+\bar z&=2x=2\, {{\operatorname{Re\, }}}\, z, \\
   z-\bar z&=2iy=2i{{\operatorname{Im\, }}}\, z.\\  
   \overline{z+w} &= \bar z+ \bar w \\
   \overline{z-w} &= \bar z- \bar w \\
   \overline{zw} &= \bar z\cdot \bar w \\
   \overline{z/w} &= \bar z/ \bar w \\
    |\bar z|&=|z| \end{aligned}

Við höfum að :math:`z` er rauntala þá og því aðeins að :math:`z=\bar z`
og að :math:`z` er hrein þvertala þá og því aðeins að :math:`z=-\bar z`.

Lengd og stefnuhorn
~~~~~~~~~~~~~~~~~~~

.. figure:: ./myndir/siiibmynd0102.svg
    :align: center
    :alt:

     

Ef :math:`z\in {{\mathbb  C}}`, :math:`x={{\operatorname{Re\, }}}z` og
:math:`y={{\operatorname{Im\, }}}z`, þá nefnist talan

.. math:: |z|=\sqrt{x^ 2+y^2},

:hover:`lengd`, :hover:`tölugildi` eða :hover:`algildi` tvinntölunnar :math:`z`. Ef
:math:`\theta\in {{\mathbb  R}}` og hægt er að skrifa tvinntöluna
:math:`z` á forminu

.. math:: z=|z|(\cos \theta +i\sin \theta),

þá nefnist talan :math:`\theta` :hover:`stefnuhorn` eða *horngildi*
tvinntölunnar :math:`z` og stærðtáknið í hægri hliðinni nefnist *pólform
tvinntölunnar* :math:`z`. 

Hornaföllin :math:`\cos` og :math:`\sin` eru
lotubundin með lotuna :math:`2\pi` og því eru allar tölur af gerðinni
:math:`\theta+2\pi k` með :math:`k\in {{\mathbb  Z}}` einnig stefnuhorn
fyrir :math:`z`. 

Raðtvenndin :math:`(|z|,\theta)` er nefnd :hover:`pólhnit` eða
:hover:`skauthnit` tölunnar :math:`z`.

Við höfum að

.. math::

  \tan \theta=\dfrac{\sin\theta}{\cos\theta}
   =\dfrac{r\sin\theta}{r\cos\theta}=\dfrac yx

og af því leiðir að hornið er gefið með formúlunni

.. math:: \theta(z)=\arctan\bigg(\dfrac yx\bigg).

Athugið að það eru miklar takmarkanir á þessri formúlu, því hún gildir
aðeins fyrir :math:`x>0`, því fallið :math:`\arctan` gefur okkur gildi á
bilinu :math:`]-\tfrac 12 \pi,\tfrac 12 \pi[`.

Nú skulum við leiða út formúlu fyrir stefnuhorni tvinntölunnar :math:`z`
sem gefur okkur samfellt fall af :math:`z` á
:math:`{{\mathbb  C}}\setminus {{\mathbb  R}}_-` sem tekur gildi á
bilinu :math:`]-\pi,\pi[`. Þetta er gert úr frá formúlunni fyrir tangens
af hálfu horni,

.. math::

  \begin{aligned}
   \tan(\tfrac 12\theta)&=\dfrac{\sin(\tfrac 12\theta)}{\cos(\tfrac
   12\theta)} = \dfrac{2\sin(\tfrac 12\theta)\cos(\tfrac 12\theta)}
   {2\cos^2(\tfrac 12\theta)}=\dfrac{\sin \theta}{1+\cos\theta}  \\
   &=\dfrac{|z|\sin \theta}{|z|+|z|\cos\theta}=\dfrac y{|z|+x}.\end{aligned}

Formúlan sem við endum með er

.. math:: \theta(z)=2\arctan\bigg(\dfrac y{|z|+x}\bigg).

Þetta fall sem gefur okkur horngildið af tvinntölunni
:math:`z\in {{\mathbb  C}}\setminus {{\mathbb  R}}_-` á bilinu
:math:`]-\pi,\pi[` nefnist :hover:`höfuðgrein hornsins,meginhorn` og er það táknað með
:math:`{{\operatorname{Arg}}}\, z`

Við höfum nokkrar reiknireglur um lengd tvinntalna,

.. math::

  \begin{aligned}
     z\bar z&=(x+iy)(x-iy)=x^2+y^2=|z|^2,\\
   |\bar z|&=|z|,\\
   |zw|&=|z||w|.\end{aligned}

Fyrsta jafnan gefur okkur formúlu fyrir margföldunarandhverfunni

.. math:: z^{-1}=\dfrac 1z=\dfrac{x-iy}{x^2+y^2}=\dfrac{\bar z}{|z|^2}, \qquad z\neq 0.

Fjarlægð milli punkta
~~~~~~~~~~~~~~~~~~~~~

Fjarlægð milli tveggja punkta :math:`z=x+iy` og :math:`w=u+iv` er gefin
með

.. math:: |z-w|=\sqrt{(x-u)^2+(y-v)^2}.

Ef :math:`\alpha` og :math:`\beta` eru tvinntölur og :math:`\alpha\neq
\beta`, þá er

.. math:: \{z\in {{\mathbb  C}}\,;\, |z-\alpha|=|z-\beta|\}

mengi allra punkta :math:`z` í :math:`{{\mathbb  C}}` sem eru í sömu
fjarlægð frá báðum punktum :math:`\alpha` og :math:`\beta`. Það er
augljóst að miðpunktur striksins :math:`\frac
12(\alpha+\beta)` milli :math:`\alpha` og :math:`\beta` er í
fjarlægðinni :math:`\frac 12|\alpha-\beta|` frá báðum punktum. Ef við
drögum línuna gegnum miðpunktinn sem liggur hornrétt á strikið, þá fáum
við mengi allra punkta sem eru í sömu fjarlægð frá :math:`\alpha` og
:math:`\beta`.

Innfeldi og krossfeldi
~~~~~~~~~~~~~~~~~~~~~~

:hover:`Innfeldi` tveggja vigra
:math:`z=(x,y)` og :math:`w=(u,v)` er skilgreint sem rauntalan
:math:`z{{\mathbb \cdot}}w=xu+yv`. Ef við lítum á :math:`z` og :math:`w`
sem tvinntölur og skrifum :math:`z=x+iy=r(\cos\alpha+i\sin \alpha)` og
:math:`w=u+iv=s(\cos\beta+i\sin\beta)`, þá fáum við formúluna

.. math::

  {{\operatorname{Re\, }}}\big(z\bar w\big)={{\operatorname{Re\, }}}\big(\bar z w\big)
   =\tfrac 12\big(z\bar w+\bar z w\big)=xu+yv=(x,y)\cdot(u,v)=rs\cos(\alpha-\beta).

Þverhluti þessarar stærðar er :hover:`krossfeldi` :math:`z`
og :math:`w`,

.. math::

  {{\operatorname{Im\, }}}(\bar z w\big)=-{{\operatorname{Im\, }}}\big(z\bar w)=xv-yu=\left|\begin{matrix}
    x&u  \\
    y&v 
   \end{matrix}\right|=-rs\sin(\alpha-\beta)

en :hover:`tölugildi`  þess
:math:`|{{\operatorname{Im\, }}}\big(z\bar w)|` er flatarmál
samsíðungsins, sem tölurnar :math:`z` og :math:`w` spanna.

Jafna línu og jafna hrings
~~~~~~~~~~~~~~~~~~~~~~~~~~

:hover:`Bein lína` í :math:`{{\mathbb  C}}` er gefin sem mengi allra punkta :math:`(x,y)`
sem uppfylla jöfnu af gerðinni

.. math:: ax+by+c=0.

Við getum greinilega snúið þessu yfir í jöfnuna

.. math:: 2{{\operatorname{Re\, }}}\big( \bar {\beta} z\big)+c=\bar {\beta} z+{\beta}\bar z+c=0,

þar sem :math:`{\beta}=\frac 12(a+ib)`. Tvinntalan :math:`{\beta}` er
hornrétt á línuna og :math:`i{\beta}` er í stefnu hennar.

:hover:`Hringur` í :math:`{{\mathbb  C}}` með miðju :math:`m` og geisla :math:`r` er
mengi allra punkta :math:`z` sem eru í fjarlægðinni :math:`r` frá
:math:`m`, :math:`|z-m|=r`. Við getum greinilega tjáð þessa jöfnu með
jafngildum hætti,

.. math::

  |z-m|^2-r^2=(z-m)(\bar z-\bar m)-r^2=|z|^2-\bar
   mz-m\bar z +|m|^2-r^2=0.

Við getum auðveldlega flokkað öll mengi sem gefin eru með jöfnu af
gerðinni

.. math:: \alpha|z|^2+\overline \beta z+\beta\overline z +\gamma=0,

þar sem :math:`\alpha` og :math:`\gamma` eru rauntölur og :math:`\beta`
er tvinntala.

Tilfellin eru:

\(i) *Lína*: :math:`\alpha=0`, :math:`\beta\neq 0`.

\(ii) *Hringur*: :math:`\alpha\neq 0`,
:math:`|\beta|^2-{\alpha}\gamma>0`. Ef miðjan er :math:`m` og geislinn
:math:`r`, þá er

.. math::

  m=-\beta/\alpha\qquad \text{ og } \qquad
   r=\sqrt{|\beta|^2-\alpha\gamma}\, /|\alpha|.

\(iii) *Einn punktur*: :math:`\alpha\neq 0` og
:math:`|\beta|^2-\alpha\gamma=0`. Punkturinn er :math:`m=-\beta/\alpha`.

\(iv) *Tóma mengið*: :math:`\alpha\neq 0`,
:math:`|\beta|^2-\alpha\gamma<0` eða :math:`\alpha=0`, :math:`\beta=0`,
:math:`\gamma\neq 0`.

\(v) *Allt planið* :math:`{{\mathbb  C}}`: :math:`\alpha=\beta=\gamma=0`.

Einingarhringurinn
~~~~~~~~~~~~~~~~~~

Einingarhringurinn :math:`{{\mathbb  T}}` er hringurinn með miðju í
:math:`0` og geislann :math:`1`. Hann samanstendur af öllum tvinntölum
með tölugildi :math:`1`. Sérhvert :math:`z` í :math:`{{\mathbb  T}}` má
því skrifa á forminu :math:`z=\cos \alpha+i\sin \alpha`. Tökum nú aðra
slíka tölu :math:`w=\cos \beta+i\sin \beta` og margföldum saman

.. math::

  \begin{aligned}
   zw&=(\cos \alpha +i\sin \alpha)(\cos \beta+i\sin \beta) \\
   &=(\cos\alpha\cos\beta-\sin\alpha\sin\beta)+i(\sin\alpha\cos\beta+\cos
   \alpha\sin\beta)\\
   &=\cos(\alpha+\beta)+i\sin(\alpha+\beta). \end{aligned}

Í síðustu jöfnunni notuðum við samlagningarformúlur fyrir :math:`\cos`
og :math:`\sin`

.. math::

  \begin{aligned}
   \cos(\alpha-\beta) &=\cos \alpha \cos \beta +\sin \alpha \sin \beta \\
   \cos(\alpha+\beta) &=\cos \alpha \cos \beta -\sin \alpha \sin \beta \\
   \sin(\alpha+\beta) &=\sin \alpha \cos \beta + \cos \alpha \sin \beta \\
   \sin(\alpha-\beta) &=\sin \alpha \cos \beta - \cos \alpha \sin \beta \\\end{aligned}

*Formúla de Movire*

.. math::

  \big(\cos\theta+i\sin\theta\big)^n
   =\cos(n\theta)+i\sin(n\theta).

Rúmfræðileg túlkun á margföldun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`z` og :math:`w` vera tvær tvinntölur með lengdir
:math:`|z|` og :math:`|w|` og stefnuhornin :math:`\alpha` og
:math:`\beta`. Þá fáum við

.. math:: zw=|z||w|\big(\cos(\alpha+\beta)+i\sin(\alpha+\beta)\big).

sem segir okkur að lengd margfeldisins sé margfeldi lengda :math:`z` og
:math:`w` og að stefnuhorn margfeldisins sé summa stefnuhorna :math:`z`
og :math:`w`.

Ef nú :math:`u\in {{\mathbb  T}}` er tala á einingarhringnum með
stefnuhornið :math:`\beta`, þá er :math:`uz` snúningur á :math:`z` um
hornið :math:`\beta`.

Þríhyrningsójafnan
~~~~~~~~~~~~~~~~~~

Tökum tvær tvinntölur :math:`z` og :math:`w` og reiknum smávegis 

.. math::

  \begin{aligned}
   |z+w|^2&=(z+w)(\overline{z+w})=(z+w)(\bar z+\bar w)  \\
    &=z\bar z+z\bar w+w\bar z+w\bar w\\
   &=|z|^2+z\bar w+\overline{z\bar w}+|w|^2\\
   &=|z|^2+2{{\operatorname{Re\, }}}(z\bar w)+|w|^2\end{aligned}

Athugum nú að

.. math::

  |{{\operatorname{Re\, }}}z|\leq |z| \qquad \text{ og } \qquad 
   |{{\operatorname{Im\, }}}z|\leq |z|

Af fyrri ójöfnunni leiðir að

.. math:: |z+w|^2\leq |z|^2+2|z||w|+|w|^2=(|z|+|w|)^2.

Ef við tökum kvaðratrót beggja vegna ójöfnumerkisins, þá fáum við
*þríhyrningsójöfnuna*

.. math:: |z+w|\leq |z|+|w|

Ef henni er beitt á liðina :math:`z-w` og :math:`w` í stað :math:`z` og
:math:`w`, þá fáum við :math:`|z|=|(z-w)+w|\leq |z-w|+|w|`, svo
:math:`|z|-|w|\leq |z-w|`. Ef við skiptum á hlutverkum :math:`z` og
:math:`w`, þá fæst :math:`|w|-|z|\leq |w-z|=|z-w|`. Þessar tvær ójöfnu
gefa okkur annað afbrigði af þríhyrningsójöfnunni

.. math:: ||z|-|w||\leq |z-w|.

Rætur
-----

Látum nú :math:`w` vera gefna tvinntölu og :math:`n\geq 2` vera
náttúrlega tölu.

Tvinntala :math:`z` kallast :math:`n` *-ta rót* tvinntölunnar :math:`w`
ef hún uppfyllir jöfnuna :math:`z^n=w`

Einingarrætur
~~~~~~~~~~~~~

Lítum á jöfnuna :math:`z^n=1`, þar sem :math:`n\geq 2` er náttúrleg
tala.

Lausnir hennar nefnast :math:`n` *-tu einingarrætur* eða :math:`n` *-tu
rætur af einum*. Ef :math:`z` er lausn, þá er :math:`1=|z^n|=|z|^n` sem
segir okkur að :math:`|z|=1` og að við getum skrifað
:math:`z=\cos \theta+i\sin \theta`. Regla de Moivres segir nú að

.. math:: \cos (n\theta)+i\sin(n\theta)=(\cos \theta+i\sin \theta)^n=z^n=1

Talan :math:`1` hefur horngildi :math:`2\pi k` þar sem
:math:`k\in {{\mathbb  Z}}` getur verið hvaða tala sem er og þessi jafna
segir okkur því að :math:`n\theta` sé heiltölumargfeldi af :math:`2\pi`
og þar með eru möguleg horngildi

.. math:: \theta=2\pi k/n, \qquad k\in {{\mathbb  Z}}.

Ef tvær heiltölur :math:`k_1` og :math:`k_2` hafa sama afgang við
heiltöludeilingu með :math:`n`, þá er
:math:`\cos(2\pi k_1/n)=\cos(2\pi k_2/n)` og
:math:`\sin(2\pi k_1/n)=\sin(2\pi k_2/n)`. Þetta gefur okkur að jafnan
:math:`z^n=1` hefur :math:`n` ólíkar lausnir :math:`u_0,\dots,u_{n-1}`,
sem nefnast :math:`n` *-tu rætur af* :math:`1` og eru gefnar með
formúlunni

.. math:: u_k=\cos(2\pi k/n)+i\sin(2\pi k/n), \qquad k=0,1,2,\dots,n-1.

Þessar tölur eru allar á einingarhringnum.

Athugið að :math:`u_0=1`, :math:`u_k=u_1^k` fyrir :math:`k=0,\dots,n-1`,
og að þær raða sér í hornin á reglulegum :math:`n`-hyrningi, þar sem
tvíhyrningur er strikið :math:`[-1,1]`.

.. figure:: ./myndir/siiibmynd0103.svg
    :align: center
    :alt: Mynd: Einingarrætur

    Mynd: Einingarrætur

Útreikningur á :math:`n`-tu rótum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`w=s(\cos\alpha+i\sin \alpha)` vera gefna tvinntölu af
lengd :math:`s\geq 0` og með stefnuhornið :math:`\alpha` og leitum að
lausnum á jöfnunni :math:`z^n=w`.

Ef :math:`z` er slík lausn og :math:`u` er :math:`n`-ta einingarrót, þá
er :math:`(zu)^n=z^nu^n=z^n=w` og því er :math:`zu` einnig lausn. Nú eru
einingarræturnar :math:`n` talsins og þetta segir okkur að um leið og
við finnum eina lausn :math:`z_0` þá fáum við :math:`n` ólíkar lausnir
:math:`z_0u` með því að stinga inn öllum mögulegum :math:`n`-tu rótum
fyrir :math:`u`.

Látum nú :math:`z_0` vera tvinntöluna, sem gefin er með formúlunni

.. math:: z_0=s^{\frac 1n}\big(\cos(\alpha/n)+i\sin(\alpha/n)\big)

og færum hana síðan í :math:`n`-ta veldi,

.. math::

  \begin{aligned}
   z_0^n &=\big(s^{\frac 1n}\big)^n\big(\cos(\alpha/n)+i\sin(\alpha/n)\big)^n \\
    & =s\big(\cos(n\alpha/n)+i\sin(n\alpha/n)\big)=w\end{aligned}

Þar með erum við komin með formúlu fyrir einni lausn.

Með því að nota formúluna fyrir :math:`n`-tu einingarrótunum, þá fáum
við upptalningu á öllum lausnum jöfnunnar
:math:`z^n=w=\varrho(\cos\alpha+i\sin \alpha)`,

.. math::

  z_k=\varrho^{\frac 1n}\big(\cos((\alpha+2\pi k)/n)+i\sin((\alpha+2\pi
   k)/n)\big), \qquad k=0,\dots,n-1.

Þessari formúlu má lýsa þannig að :math:`n`-tu ræturnar eru fundnar
þannig að fyrst er fundin ein rót :math:`z_0`. Henni er snúið um hornið
:math:`2\pi/n` með því að margfalda með :math:`u_1` yfir í
:math:`z_1=u_1z_0`. Næst er :math:`z_1` snúið um hornið :math:`2\pi/n` í
:math:`z_2=u_1z_1` og þannig er haldið áfram þar til :math:`n` ólíkar
rætur eru fundnar.

Ferningsrætur
~~~~~~~~~~~~~

Ef :math:`w` er tvinntala og :math:`z` uppfyllir :math:`z^2=w`, þá er
:math:`z` sögð vera :hover:`ferningsrót` eða *kvaðratrót* tölunnar :math:`w`.

Munið að ef :math:`w` er jákvæð rauntala, þá táknar :math:`\sqrt w`
alltaf jákvæðu rauntöluna töluna sem uppfyllir
:math:`(\sqrt w)^2=\alpha`. Að sjálfsögðu er :math:`\sqrt 0=0`.

Ef :math:`w\neq 0` er tvinntala og :math:`w` er ekki jákvæð rauntala, þá
er hefur :math:`\sqrt w` enga staðlaða merkingu. Við vitum bara að
:math:`w` hefur tvær ferningsrætur :math:`z_0` og :math:`z_1`. Ef við
skrifum :math:`w=s(\cos \alpha+i\sin\alpha)`, þá gefa reikningar okkar
hér að framan að við getum við tekið

.. math:: z_0=\sqrt{s}(\cos(\alpha/2)+i\sin (\alpha/2))

og

.. math:: z_1=\sqrt{s}(\cos(\alpha/2+\pi)+i\sin (\alpha/2+\pi))=-z_0.

Ef :math:`z^2=x^2-y^2+2ixy=u+iv=w`, þá fæst með því að bera saman raun-
og þverhluta í þessari jöfnu að formúlur :math:`x^2-y^2=u` og
:math:`2xy=v`.

Formúlan :math:`|w|=|z^2|=|z|^2=x^2+y^2` gefur okkur eina jöfnu til
viðbótar og við getum leyst út :math:`x^2` og :math:`y^2`,

.. math::

  \begin{cases}
   x^2+y^2=|w|,\\
   x^2-y^2=u,
   \end{cases}\qquad
   \begin{cases}
   x^2=\tfrac 12(|w|+u),\\
   y^2=\tfrac 12(|w|-u).
   \end{cases}\qquad

Við gáfum okkur að :math:`x>0` og því er formerkið á :math:`y` það sama
og formerkið á :math:`v=2xy`.

:math:`{{\operatorname{sign}}}` er skilgreint með

.. math::

  {{\operatorname{sign}}}(t)=
   \begin{cases}
   1, &t>0,\\
   0, &t=0,\\
   -1,&t<0.
   \end{cases}

Ef :math:`v\neq 0`, þá gefur þessi formúla okkur kost á að við skrifa
lausina á einföldu formi

.. math::

  \begin{aligned}
   z&=\sqrt{\tfrac 12(|w|+u)}+i\, {{\operatorname{sign}}}(v)\, \sqrt{\tfrac 12(|w|-u)}\\
   &=\sqrt{\tfrac 12(|w|+{{\operatorname{Re\, }}}w)}+i\, {{\operatorname{sign}}}({{\operatorname{Im\, }}}w)\, \sqrt{\tfrac
   12(|w|-{{\operatorname{Re\, }}}w)}.\end{aligned}

Ef :math:`v=0` og :math:`u>0`, þá er :math:`w=u` og við fáum jákvæðu
rótina :math:`z=\sqrt w` út úr þessari formúlu.

Margliður
---------

*Margliða með tvinntölustuðlum* er stærðtákn af gerðinni

.. math:: P(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots+a_1z+a_0.

þar sem :math:`a_0,\dots,a_n` eru tvinntölur og :math:`z` er breyta sem
tekur gildi í tvinntölunum.

Við getum litið á :math:`P` sem fall sem skilgreint er á
:math:`{{\mathbb  C}}` og tekur gildi í :math:`{{\mathbb  C}}`.

*Núllmargliðan* er margliðan sem hefur alla stuðla :math:`a_j=0`. Við
táknum hana með :math:`0`. Stig margliðunnar :math:`P\neq 0` er
skilgreint eins og áður sem stærsta heiltala :math:`j` þannig að
:math:`a_j\neq 0`.

Margliðudeiling er alveg eins fyrir margliður með tvinntölustuðla og
margliður með rauntölustuðla.

Ef :math:`P` er margliða og :math:`Q` er margliða af stigi :math:`m`, þá
eru til margliða :math:`R` af stigi minna en :math:`m` og margliða
:math:`S`, þannig að

.. math:: P(z)=Q(z)S(z)+R(z)

Margliðan :math:`R` nefnist þá *leif* eða *afgangur við deilingu á*
:math:`P`  *með* :math:`Q` og :math:`S` nefnist *kvóti* :math:`P`  *og*
:math:`Q`. Við segjum að :math:`Q` *deili* :math:`P` eða að :math:`Q` 
*gangi upp í* :math:`P` ef :math:`R` er núllmargliðan.

Þáttaregla
~~~~~~~~~~

Ef :math:`\alpha\in {{\mathbb  C}}`, þá er :math:`z-\alpha` fyrsta stigs
margliða og við fáum að leifin við deilingu á :math:`P(z)` með
:math:`(z-\alpha)` verður fastamargliðan :math:`P(\alpha)`,

.. math:: P(z)=(z-\alpha)S(z)+P(\alpha).

Tvinntalan :math:`\alpha` er sögð vera :hover:`núllstöð` eða rót
margliðunnar :math:`P` ef :math:`P(\alpha)=0`.

Setning
^^^^^^^

(Þáttaregla) Margliða :math:`P` af stigi :math:`\geq 1` hefur núllstöð
:math:`\alpha` þá og því aðeins að :math:`z-\alpha` gangi upp í
:math:`P`.

Núllstöðvar annars stigs margliðu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú viljum við leysa jöfnuna :math:`az^2+bz+c=0` og ganga út frá því að
stuðlarnir :math:`a`, :math:`b` og :math:`c` séu tvinntölur og að
:math:`a\neq 0`.

Fyrsta skref er að deila báðum hliðum með :math:`a` og fá þannig
jafngilda jöfnu :math:`z^2+Bz+C=0`, þar sem :math:`B=b/a` og
:math:`C=c/a`.

Næsta skref er að líta á tvo fyrstu liðina :math:`z^2+Bz` og skrifa þá
sem ferning að viðbættum fasta. Með orðinu ferningur er átt við fyrsta
stigs stærðtákni í öðru veldi, :math:`(z+\alpha)^2`. Ferningsreglan
fyrir fyrir summu segir að :math:`(z+\alpha)^2=z^2+2\alpha z+\alpha^2`.
Því er

.. math:: 0=z^2+Bz+C=(z+\dfrac B2)^2-\dfrac {B^2}4+C.

Þetta segir okkur að upphaflega jafnan jafngildi

.. math:: 0=(az^2+bz+c)/a=\bigg(z+\dfrac {b}{2a}\bigg)^2-\dfrac{b^2}{4a^2}+\dfrac ca.

Með því að draga töluna :math:`-b^2/(4a^2)+c/a` frá báðum hliðum, þá
fáum við jafngilda jöfnu

.. math:: \bigg(z+\dfrac {b}{2a}\bigg)^2=\dfrac{b^2}{4a^2}-\dfrac ca=\dfrac{b^2-4ac}{4a^2}.

Tvinntalan :math:`D=b^2-4ac` nefnist :hover:`aðgreinir` eða *aðskilja*
jöfnunnar. Ef :math:`D\neq 0`, þá hefur :math:`D` tvær kvaðratrætur.
Látum :math:`\sqrt D` tákna aðra þeirra. Þá er hin jöfn :math:`-\sqrt D`
og við fáum tvær ólíkar lausnir

.. math::

  z_1=\dfrac{-b+\sqrt D}{2a} \qquad\text {og} \qquad
   z_2=\dfrac{-b-\sqrt D}{2a}.

Ef :math:`D=0`, fæst ein lausn

.. math:: z=\dfrac{-b}{2a}.

Ef :math:`D` er rauntala og :math:`D<0` þá getum við valið
:math:`\sqrt D=i\sqrt{|D|}` og lausnarformúlan verður

.. math::

  z_1=\dfrac{-b+i\sqrt{ |D|}}{2a} \qquad\text {og} \qquad
   z_2=\dfrac{-b-i\sqrt{|D|}}{2a}.

Undirstöðusetning algebrunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setning
^^^^^^^

  Sérhver margliða af stigi :math:`\geq 1` með stuðlum í
:math:`{{\mathbb  C}}` hefur núllstöð í :math:`{{\mathbb  C}}`.

--------------

Segjum nú að :math:`P` sé margliða af stigi :math:`m\geq 1` og að
:math:`\alpha_1` sé núllstöð hennar. Við getum þá skrifað

.. math:: P(z)=(z-\alpha_1)Q_1(z)

samkvæmt þáttareglunni. Þá er :math:`Q_1` af stigi :math:`m-1` og
samkvæmt undirstöðusetningunni hefur :math:`Q_1` núllstöð
:math:`\alpha_2` ef :math:`m\geq 2`. Við þáttum :math:`Q_1` með
:math:`z-\alpha_2` og fáum þannig

.. math:: P(z)=(z-\alpha_1)(z-\alpha_2)Q_2(z)

þar sem :math:`Q_2` er margliða af stigi :math:`m-2`.

Þessu er unnt að halda áfram þar til við endum með fullkomna þáttun á
:math:`P` í fyrsta stigs liði

.. math:: P(z)=A(z-\alpha_1)(z-\alpha_2)\cdots(z-\alpha_m)

þar sem :math:`\alpha_1,\dots,\alpha_m` er upptalning á öllum
núllstöðvum :math:`P` með hugsanlegum endurtekningum og :math:`A\neq 0`
er stuðullinn í veldið :math:`z^m` í margliðunni :math:`P`.

Ef :math:`\alpha` er núllstöð margliðu :math:`P` og hægt er að þátta
:math:`P` í :math:`P(z)=(z-\alpha)^jQ(z)` þar sem :math:`Q` er margliða
og :math:`Q(\alpha)\neq 0` þá segjum við að :math:`\alpha` sé
:math:`j` *-föld núllstöð* :math:`P` og köllum töluna :math:`j`
*margfeldni núllstöðvarinnar* :math:`\alpha`  *í* :math:`P`.

Ef :math:`P` er af stigi :math:`m` og :math:`\beta_1,\dots,\beta_k` er
upptalning á ólíkum núllstöðvum margliðunnar :math:`P` og þær hafa
margfeldni :math:`m_1,\dots,m_k`, þá getum við skrifað

.. math:: P(z)=A(z-\beta_1)^{m_1}\cdots(z-\beta_k)^{m_k}

og

.. math:: m=m_1+\cdots+m_k.

Margliður með rauntölustuðla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við lítum allaf á rauntölurnar sem hluta af tvinntölunum og því er
sérhver margliða með rauntölustuðla jafnframt margliða með
tvinntölustuðla.

Undirstöðusetning algebrunnar á því við um þessar margliður einnig.

Hugsum okkur nú að :math:`P(z)` sé margliða af stigi :math:`m\geq 1` með
rauntölustuðla :math:`a_0,\dots,a_m` og að
:math:`\alpha\in {{\mathbb  C}}` sé núllstöð hennar og gerum ráð fyrir
að :math:`\alpha` sé ekki rauntala. Með því að beita reiknireglunum
fyrir samok og þá sérstaklega að :math:`\bar a_j=a_j`, þá fáum við

.. math::

  0=P(\alpha)=\overline{P(\alpha)}
   =\overline{\sum_{k=0}^ma_k\alpha^k} =\sum_{k=0}^m \overline{a_k}\overline{\alpha^k}
   =\sum_{k=0}^m a_k (\overline{\alpha})^k=P(\bar\alpha)

Við höfum því sýnt að :math:`\bar \alpha` er einnig núllstöð :math:`P`.
Við getum því þáttað út :math:`(z-\alpha)(z-\bar \alpha)` Athugum að

.. math::

  (z-\alpha)(z-\bar\alpha)=
   z^2-(\alpha+\bar\alpha)z+\alpha\bar\alpha
   =z^2-2({{\operatorname{Re\, }}}\, \alpha)z+|\alpha|^2

Nú beitum við þáttareglunni og sjáum að í þessu tilfelli fæst þáttun á
:math:`P(z)` í tvær rauntalnamargliður

.. math:: P(z)=\big(z^2-2({{\operatorname{Re\, }}}\, \alpha)z+|\alpha|^2\big)Q(z).

Afleiður af margliðum
~~~~~~~~~~~~~~~~~~~~~

Tvíliðustuðlarnir eru dálítið fyrirferðarmiklir í útskrift svo við
skulum tákna :math:`n` yfir :math:`k` með :math:`c_{n,k}`. Við fáum þá

.. math:: (z+h)^n=z^n+nz^{n-1}h+c_{n,2}z^{n-2}h^2+\cdots+c_{n,n-2}z^{n-2}h^2+nzh^{n-1}+h^n.

Við fáum því formúluna

.. math:: \dfrac{(z+h)^n-z^n}h=nz^{n-1}+c_{n,2}z^{n-2}h+\cdots+nzh^{n-2}+h^{n-1}.

Nú látum við :math:`h` stefana á :math:`0` og fáum

.. math::

  \lim_{h\to 0}\bigg(
   \dfrac{(z+h)^n-z^n}h\bigg)=nz^{n-1}.

Við skilgreinum afleiðuna af einliðunni :math:`z\mapsto z^n` sem fallið
:math:`z\mapsto nz^{n-1}` fyrir :math:`n=0,1,2,\dots` og almennt
skilgreinum við afleiðu af margliðu :math:`P(z)=\sum_{n=0}^ma_nz^n` með

.. math:: P'(z)=\lim_{h\to 0}\dfrac{P(z+h)-P(z)}h=\sum_{n=0}^mna_nz^{n-1}.

Það er enginn vandi að sýna fram á að venjulegu reiknireglurnar fyrir
afleiður gildi,

.. math:: (P+Q)'(z)=P'(z)+Q'(z)

og

.. math:: (PQ)'(z)=P'(z)Q(z)+P(z)Q'(z).

.. _1.5:

Ræð föll
--------

:hover:`Rætt fall` er kvóti tveggja margliða :math:`R=P/Q`. Það er skilgreint í
öllum punktum :math:`z\in {{\mathbb  C}}` þar sem :math:`Q(z)\neq 0`.
Við skilgreinum afleiðuna af :math:`R` með hliðstæðum hætti og fyrir
margliður og fáum venjulega reiknireglu

.. math::

  R'(z)=\lim_{h\to
   0}\dfrac{R(z+h)-R(z)}h=\dfrac{P'(z)Q(z)-P(z)Q'(z)}{Q(z)^2}.

Stofnbrotaliðun
~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`P` og :math:`Q` eru margliður, :math:`Q\neq 0` og
:math:`{{\operatorname{stig}}}P\geq {{\operatorname{stig}}}Q`, þá getum
við alltaf framkvæmt deilingu með afgangi og fengið að

.. math:: R(z)=\dfrac {P(z)}{Q(z)}=P_1(z)+\dfrac {P_2(z)}{Q(z)}

þar sem :math:`P_1` og :math:`P_2` eru margliður,
:math:`{{\operatorname{stig}}}P_1={{\operatorname{stig}}}P-{{\operatorname{stig}}}Q`
og :math:`{{\operatorname{stig}}}P_2<{{\operatorname{stig}}}Q`.

Nú ætlum við að líta á rætt fall :math:`R=P/Q` þar sem :math:`P` og
:math:`Q` eru margliður og
:math:`{{\operatorname{stig}}}P < {{\operatorname{stig}}}Q`. Þá er
alltaf hægt að liða ræða fallið í :hover:`stofnbrot`.

Einfaldar núllstöðvar
^^^^^^^^^^^^^^^^^^^^^

Við gerum fyrst ráð fyrir því að að allar núllstöðvar :math:`Q` séu
einfaldar. Þá getum við skrifað

.. math:: Q(z)= a(z-\alpha_1)\cdots(z-\alpha_m), \qquad z\in {{\mathbb  C}},

þar sem :math:`\alpha_1,\dots,\alpha_m` eru hinar ólíku núllstöðvar
:math:`Q`. :hover:`Stofnbrotaliðun` :math:`R` er

.. math:: R(z) = \dfrac {A_1}{z-\alpha_1}+\cdots+\dfrac {A_m}{z-\alpha_m}.

Nú þarf að reikna stuðlana
:math:`A_1,\dots,A_m` út. Við athugum að

.. math::

  \lim\limits_{z\to\alpha_1} (z-\alpha_1)R(z) = A_1
   +\lim\limits_{z\to\alpha_1}
   (z-{\alpha}_1)\bigg(
   \dfrac {A_2}{z-\alpha_2}+\cdots+\dfrac {A_m}{z-\alpha_m}
   \bigg)=A_1.

Á hinn bóginn er :math:`Q(\alpha_1)=0`, svo

.. math::

  \lim\limits_{z\to\alpha_1}(z-\alpha_1)R(z) =
   \lim\limits_{z\to
   \alpha_1}\dfrac{(z-\alpha_1)P(z)}{Q(z)-Q(\alpha_1)}=
   \dfrac{P(\alpha_1)}{Q{{^{\prime}}}(\alpha_1)}.

Ef við meðhöndlum hinar núllstöðvarnar með sama hætti, þá fáum við
formúluna

.. math:: A_j=\dfrac{P(\alpha_j)}{Q{{^{\prime}}}(\alpha_j)}.

Við notum nú þáttunina á :math:`Q` í fyrsta stigs liði til þess að
reikna út afleiðuna af :math:`Q` í :math:`{\alpha}_j`,

.. math::

  Q{{^{\prime}}}(\alpha_j)=a\prod_{\substack{k=1\\ k\neq
    j}}^m
   (\alpha_j-\alpha_k).

Þessi formúla segir okkur að :math:`Q'(\alpha_j)` sé fundið með því að
taka þáttunina á :math:`Q` í fyrsta stigs liði, deila út þættinum
:math:`z-\alpha_j` og stinga síðan inn :math:`\alpha_j` fyrir :math:`z`.
Í sumum tilfellum getur verið einfaldast að nota þessa formúlu til þess
að reikna út gildin á afleiðum margliðunnar :math:`Q` í núllstöðvunum.

Margfaldar núllstöðvar
^^^^^^^^^^^^^^^^^^^^^^

Gerum nú ráð fyrir að :math:`Q` hafi ólíkar núllstöðvar
:math:`\alpha_1,\dots,\alpha_k` af stigi :math:`m_1,\dots,m_k`, og
:math:`{{\operatorname{stig}}}Q=m=m_1+\cdots+m_k`. Við getum þáttað út
núllstöðina :math:`\alpha_j` með því að skrifa
:math:`Q(z)=(z-\alpha_j)^{m_j}q_j(z)`, þar sem :math:`q_j` er margliða
af stigi :math:`m-m_j` og :math:`q_j(\alpha_j)\neq 0`. Stofnbrotaliðunin
verður nú af gerðinni

.. math::

  \begin{aligned}
   \dfrac{P(z)}{Q(z)}&=
   \dfrac{A_{1,0}}{(z-\alpha_1)^{m_1}}+\cdots+\dfrac{A_{1,m_1-1}}{(z-\alpha_1)}\\
   &+\dfrac{A_{2,0}}{(z-\alpha_2)^{m_2}}+\cdots+\dfrac{A_{2,m_2-1}}{(z-\alpha_2)}
   \nonumber\\
   &\qquad \vdots\qquad\qquad\vdots\qquad \qquad \vdots\nonumber\\
   &+\dfrac{A_{k,0}}{(z-\alpha_k)^{m_k}}+\cdots+\dfrac{A_{k,m_k-1}}{(z-\alpha_k)}\nonumber\end{aligned}

þar sem stuðlarnir eru gefnir með formúlunni

.. math::

  A_{j,\ell}=\left.\dfrac 1{\ell!}
   \bigg(\dfrac {d}{dz}\bigg)^{\ell}\bigg(
   \dfrac{P(z)}{q_j(z)}\bigg)\right|_{z=\alpha_j},

fyrir :math:`j=1,\dots,k` og :math:`\ell=0,\dots,m_k-1`.

Veldisvísisfallið og skyld föll
-------------------------------

Við höfum séð hvernig skilgreiningarmengi margliða er útvíkkað frá því
að vera rauntalnaásinn :math:`{{\mathbb  R}}` yfir í það að vera allt
tvinntalnaplanið :math:`{{\mathbb  C}}`. Þetta er hægt að gera á
eðlilegan máta fyrir mörg föll sem skilgreind eru á hlutmengjum á
rauntalnalínunni þannig að þau fái náttúrlegt skilgeiningarsvæði í
:math:`{{\mathbb  C}}`.

Framlenging á veldisvísisfallinu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Veldisvísisfallið :math:`\exp:{{\mathbb  R}}\to {{\mathbb  R}}` er
andhverfa náttúrlega lograns sem skilgreindur er með heildinu

.. math:: \ln x=\int_1^x\dfrac {dt}t, \qquad x>0.

Talan :math:`e` er skilgreind með :math:`e=\exp(1)`. Nú útvíkkum við
skilgreiningarsvæði :math:`\exp` þannig að það verði allt
:math:`{{\mathbb  C}}` með formúlunni

.. math:: \exp(z)=e^x(\cos y+i\sin y), \qquad z=x+iy\in {{\mathbb  C}}, \quad x,y\in {{\mathbb  R}}

Við skrifum :math:`e^z=\exp z` fyrir :math:`z\in {{\mathbb  C}}`.

Fyrst hornaföllin :math:`\cos` og :math:`\sin` eru lotubundin með
lotuna :math:`2\pi`, þá fáum við beint út frá skilgreiningunni á
veldisvísisfallinu að það er lotubundið með lotuna :math:`2\pi i`,

.. math:: e^{z+2\pi k i}=e^z, \qquad k\in {{\mathbb  Z}}.

Jöfnur Eulers
~~~~~~~~~~~~~

Stingum nú hreinni þvertölu :math:`i\theta`,
:math:`\theta\in {{\mathbb  R}}` inn í veldisvísisfallið
:math:`e^{i\theta}=(\cos\theta+i\sin\theta)\in {{\mathbb  T}}`. Þetta
segir okkur að vörpunin :math:`\theta\mapsto e^{i\theta}` varpi
rauntalnalínunni á einingarhringinn. Stillum nú upp tveimur jöfnum

.. math::

  \begin{aligned}
   e^{i\theta}&=\cos\theta+i\sin\theta\\
   e^{-i\theta}&=\cos\theta-i\sin\theta\end{aligned}

Tökum nú summu af hægri hliðum og vinstri hliðum. Þá fæst
:math:`e^{i\theta}+e^{-i\theta}=2\cos \theta`. Tökum síðan mismun af því
sama. Þá fæst :math:`e^{i\theta}-e^{-i\theta}=2i\sin \theta`. Út úr
þessu fæst samband milli veldisvísisfallsins og hornafallanna sem nefnt
er *jöfnur Eulers*,

.. math::

  \cos\theta=\dfrac{e^{i\theta}+e^{-i\theta}}2,\qquad \text{ og } \qquad
   \sin\theta=\dfrac{e^{i\theta}-e^{-i\theta}}{2i}.

Samlagningarformúla veldisvísisfallsins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Munum að veldisvísisfallið
:math:`\exp: {{\mathbb  R}}\to {{\mathbb  R}}`, :math:`x\mapsto e^x`,
uppfyllir regluna :math:`e^{a+b}=e^ae^b` fyrir allar rauntölur :math:`a`
og :math:`b`. Hún er nefnd *samlagningarformúla* eða *samlagningarregla*
veldisvísisfallsins.

tökum tvær tvinntölur :math:`z=x+iy` og :math:`w=u+iv`

.. math::

  \begin{aligned}
   e^ze^w &=e^x(\cos y+i\sin y)e^u(\cos v+i\sin v) \\
    & =(e^xe^u)(\cos y+i\sin y)(\cos v+i\sin v) \\
    & =e^{x+u}(\cos(y+v)+i\sin (y+v))\\
    & =e^{(x+u)+i(y+v)}=e^{z+w}.\end{aligned}

Þetta segir að samlagningarformúlan alhæfist

.. math:: e^{z+w}=e^ze^w, \qquad z,w\in {{\mathbb  C}}.

Reglurnar um reikning með samoka tvinntölum gefa okkur

.. math:: \overline{e^z}=e^{\overline z},\qquad z\in {{\mathbb  C}},

og síðan

.. math:: |e^z|^2=e^z\overline{e^{z}}=e^ze^{\overline z}=e^{x+iy}e^{x-iy}=e^{2x}

Þar með er

.. math:: |e^z|=e^{{{\operatorname{Re\, }}}z}, \qquad z\in {{\mathbb  C}},

og sérstaklega gildir

.. math:: |e^{iy}|=1, \qquad y\in {{\mathbb  R}}.

Af þessu leiðir að veldisvísisfallið hefur enga
núllstöð :math:`e^z=e^xe^{iy}` og
hvorugur þátturinn í hægri hliðinni getur verið núll. 

Við sjáum einnig að veldisvísisfallið varpar lóðréttu línunni sem gefin er með jöfnunni :math:`x={{\operatorname{Re\, }}}z=a` í :math:`z`-plani á hringinn sem gefinn er með jöfnununni :math:`|w|=e^a` í :math:`w`-plani og það varpar láréttu línunni sem gefin er með jöfnunni
:math:`y={{\operatorname{Im\, }}}z=b` á hálflínuna út frá :math:`0` með
stefnuvigur :math:`e^{ib}`.

.. figure:: ./myndir/fig0318.svg
    :align: center
    :alt: Mynd: Veldisvísisfallið

    Mynd: Veldisvísisfallið

Framlenging á hornaföllum og breiðbogaföllum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um leið og við höfum framlengt veldisvísisfallið yfir á allt
tvinntalnaplanið, þá framlengjast hornaföllin sjálfkrafa yfir á allt
planið með Euler formúlunum,

.. math::

  \cos z =\dfrac{e^{iz}+e^{-iz}}2, \qquad \text{ og } \qquad 
   \sin z =\dfrac{e^{iz}-e^{-iz}}{2i}

og sama er að segja um breiðbogaföllin

.. math::

  \cosh z =\dfrac{e^{z}+e^{-z}}2 \qquad \text{ og } \qquad  
   \sinh z =\dfrac{e^{z}-e^{-z}}{2}.

Tilsvarandi tangens- og kótangens-föll eru skilgreind þar sem
nefnararnir eru frábrugðnir :math:`0`

.. math::

  \tan z=\dfrac {\sin z}{\cos z}, \quad
   \cot z=\dfrac {\cos z}{\sin z}, \quad
   \tanh z=\dfrac {\sinh z}{\cosh z} \quad \text{ og } \quad
   \coth z=\dfrac {\cosh z}{\sinh z}. \quad

Gömlu góðu reglurnar gilda áfram, eins og til dæmis

.. math:: \cos^2z+\sin^2z=1  \qquad \text{ og } \qquad \cosh^2z-\sinh^2z=1,

sem gilda um öll :math:`z\in {{\mathbb  C}}`. Sama er að segja um allar
samlagningarformúlurnar fyrir hornaföll og breiðbogaföll til dæmis

.. math:: \cos(z-w)=\cos z\cos w+\sin z\sin w, \qquad z,w\in {{\mathbb  C}}.

Nú kemur líka í ljós samband milli hornafallanna og breiðboga fallanna,
því

.. math:: \cosh z=\cos(iz) \qquad \text{  og } \qquad \sinh z=-i \sin(iz)

gildir um öll :math:`z\in {{\mathbb  Z}}`.

Varpanir á tvinntöluplaninu
---------------------------

Í þessum kafla ætlum við að fjalla um föll
:math:`f:X\to {{\mathbb  C}}`, sem skilgreind eru á hlutmengi :math:`X`
í :math:`{{\mathbb  C}}` og taka gildi í :math:`{{\mathbb  C}}`. Til
þess að einfalda útreikninga okkar, þá skiptum við frjálslega milli
tvinntalnaritháttar og vigurritháttar á punktum :math:`z\in X`. Þannig
skrifum við

.. math:: z=x+iy=re^{i{\theta}}=(x,y)=\left[\begin{matrix} x\\ y\end{matrix}\right]

og segjum að :math:`z` hafi
:hover:`raunhlutann,raunhluti` :math:`x`,
:hover:`þverhlutann,þverhluti` :math:`y`,
:hover:`lengdina,lengd` :math:`r` og
:hover:`horngildið,stefnuhorn` :math:`{\theta}`.

Hér er :math:`x+iy` tvinntöluframsetning á
:math:`z` í :hover:`rétthyrndum hnitum,kartesk hnit` ,
:math:`re^{i{\theta}}` framsetning í :hover:`pólhnitum,pólhnit`,
:math:`(x,y)` er línuvigurframsetning á :math:`z` og
:math:`\left[\begin{matrix} x\\
y\end{matrix}\right]` er dálkvigurframsetning á :math:`z`. Með þessu
erum við að líta framhjá þeim greinarmun sem gerður er á vigrunum
:math:`(1,0)` og :math:`(0,1)` annars vegar og
:hover:`tvinntölunum,tvinntala` :math:`1` og :math:`i` hins vegar.

Fallgildið :math:`f(z)` skrifum við ýmist sem :math:`f(x+iy)` eða
:math:`f(x,y)`.

Við getum skrifað :math:`f=u+iv`, þar sem
:math:`u={{\operatorname{Re\, }}}f` er raunhluti :math:`f` og
:math:`v={{\operatorname{Im\, }}}f` er þverhluti :math:`f`. Við horfum
oft framhjá þeim greinarmun sem gerður er á :math:`{{\mathbb  R}}^2` og
:math:`{{\mathbb  C}}` og skrifum þá vigra ýmist sem línu- eða
dálkvigra. Þannig getum við skrifað

.. math::

  f(z)=u(z)+iv(z)=(u(x,y), v(x,y))=
   \left[\begin{matrix} u(x,y) \\ v(x,y)\end{matrix}\right], \quad
   z=x+iy=(x,y).

Línulegar varpanir
~~~~~~~~~~~~~~~~~~

Við skulum byrja á því að skoða :hover:`línulegar varpanir,línulegt fall` , en það eru föll af
gerðinni :math:`L:{{\mathbb  C}}\to {{\mathbb  C}}` sem uppfylla

.. math:: L(z+w)=L(z)+L(w) \qquad z,w\in {{\mathbb  C}}

og

.. math:: L(cz)=cL(z), \qquad z\in {{\mathbb  C}}, \quad c\in {{\mathbb  R}}.

Ef við lítum á :math:`L` sem vörpun
:math:`{{\mathbb  R}}^2\to {{\mathbb  R}}^2`, þá vitum við að hægt er að
skrifa hana sem

.. math:: (x,y)\mapsto (ax+by, cx+dy),

þar sem :math:`a`, :math:`b`, :math:`c` og :math:`d` eru rauntölur. Við
getum líka lýst vörpuninni :math:`L` með fylkjamargföldun sem

.. math::

  \left[\begin{matrix} x\\ y\end{matrix} \right]\mapsto
   \left[\begin{matrix} a & b\\ c & d\end{matrix} \right]
   \left[\begin{matrix} x\\ y\end{matrix} \right].

Þá nefnist :math:`2\times 2` fylkið sem hér stendur *fylki
vörpunarinnar* :math:`L`  *miðað við staðalgrunninn á*
:math:`{{\mathbb  R}}^2`

Nú skulum við snúa þessum framsetningum yfir í tvinntalnaframsetningu.
Eins og við höfum áður rifjað upp þá svarar tvinntalan :math:`1` til
vigursins :math:`(1,0)` og tvinntalan :math:`i` svarar til vigursins
:math:`(0,1)`. Við skrifum því :math:`L(1)` í stað :math:`L(1,0)` og
:math:`L(i)` í stað :math:`L(0,1)`. Við fáum þá :math:`L(1)=(a,c)=a+ic`
og :math:`L(i)=(b,d)=b+id` og þar með

.. math:: L(z)=L(x+iy)=xL(1)+yL(i).

Nú notfærum við okkur að :math:`x=(z+\bar z)/2` og :math:`y=-i(z-\bar
z)/2` og fáum formúluna

.. math:: L(z)=Az+B\bar z,

þar sem

.. math::

  \begin{aligned}
   A=\tfrac 12\big(L(1)-iL(i)\big)
   =\tfrac 12\big((a+ic)-i(b+id)\big),\\
   B=\tfrac 12\big(L(1)+iL(i)\big)
   =\tfrac 12\big((a+ic)+i(b+id)\big).\end{aligned}

Niðurstaða útreikninga okkar er:

Setning
^^^^^^^

Sérhverja línulega vörpun :math:`L:{{\mathbb  C}}\to{{\mathbb  C}}` má
setja fram sem :math:`L(z)=Az+B\bar z`, þar sem stuðlarnir :math:`A` og
:math:`B` eru tvinntölur. Ef

.. math:: \left[\begin{matrix} a & b\\ c & d\end{matrix} \right]

er fylki :math:`L` miðað við staðalgrunninn á :math:`{{\mathbb  R}}^2`,
þá er

.. math::

  A=\tfrac 12((a+d)+i(c-b)) \qquad \text{ og } \qquad
   B= \tfrac 12((a-d)+i(c+b)).

--------------

Hugsum okkur næst að við þekkjum stuðlana :math:`A` og :math:`B` og að
við viljum ákvarða stuðlana :math:`a`, :math:`b`, :math:`c` og :math:`d`
í fylki vörpunarinnar út frá þeim. Sambandið þarna á milli er

.. math::

  \begin{aligned}
   a&={{\operatorname{Re\, }}}\big(L(1)\big)={{\operatorname{Re\, }}}\big(A+B\big), \\
   b&={{\operatorname{Re\, }}}\big(L(i)\big)={{\operatorname{Re\, }}}\big(i(A-B)\big)=-{{\operatorname{Im\, }}}\big(A-B\big),\\
   c&={{\operatorname{Im\, }}}\big(L(1)\big)={{\operatorname{Im\, }}}\big(A+B\big),\\
   d&={{\operatorname{Im\, }}}\big(L(i)\big)={{\operatorname{Im\, }}}\big(i(A-B)\big)={{\operatorname{Re\, }}}\big(A-B\big).\end{aligned}

Í tvinnfallagreiningu þarf oft að gera greinarmun á
:math:`{{\mathbb  R}}` *-línulegum* vörpunum, en það eru nákvæmlega þær línulegu varpanir sem við
höfum verið að fjalla um, og
:math:`{{\mathbb  C}}` *-línulegum* vörpunum, en þær uppfylla

.. math::

  L(z+w)=L(z)+L(w) \quad \text{ og } \quad 
   L(cz)=cL(z), \quad z,w\in {{\mathbb  C}}, \quad c\in {{\mathbb  C}}.

Það er greinilegt að sérhver :math:`{{\mathbb  C}}`-línuleg vörpun er
:math:`{{\mathbb  R}}`-línuleg, því ef seinna skilyrðið gildir um
sérhverja tvinntölu, þá gildir það sérstaklega um sérhverja rauntölu.
Það er einnig augljóst að sérhver vörpun af gerðinni :math:`L(z)=Az` þar
sem :math:`A` er gefin tvinntala er :math:`{{\mathbb  C}}`-línuleg.

Hugsum okkur nú að :math:`L` sé :math:`{{\mathbb  C}}`-línuleg og
skrifum :math:`L(z)=Az+B\bar z` eins og lýst er hér að framan. Þá er
:math:`L(i)=iL(1)` og því er

.. math:: B=\tfrac 12\big(L(1)+iL(i)\big)= \tfrac 12\big(L(1)+i^2L(1)\big)=0,

svo :math:`L(z)=Az`. Niðustaðan er því

Setning
^^^^^^^

Sérhver :math:`{{\mathbb  C}}`-línuleg vörpun
:math:`L:{{\mathbb  C}}\to {{\mathbb  C}}` er af gerðinni

.. math:: L(z)=Az, \qquad z\in {{\mathbb  C}},

þar sem :math:`A` er tvinntala.

Myndræn framsetning á vörpunum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Til þess að lýsa hegðun raungildra falla á myndrænan hátt, þá teiknum
við upp gröf þeirra. Graf tvinngilda fallsins
:math:`f:X\to {{\mathbb  C}}`, :math:`X\subseteq {{\mathbb  C}}`, er
hlutmengið í :math:`{{\mathbb  C}}^2` sem skilgreint er með

.. math:: {{\operatorname{graf}}}f=\{(z,f(z))\in {{\mathbb  C}}^2; z\in X\}.

Nú er :math:`{{\mathbb  C}}^2` fjórvítt rúm yfir
:math:`{{\mathbb  R}}`, en rúmskynjun flestra manna takmarkast við þrjár
víddir, svo við getum ekki teiknað upp myndir af gröfum tvinnfalla. Við
getum vissulega teiknað upp gröf raungildu fallanna
:math:`{{\operatorname{Re\, }}}f` og :math:`{{\operatorname{Im\, }}}f` í
þrívíðu rúmi og gert okkur hugmynd um :math:`{{\operatorname{graf}}}f`
út frá þeim, en það hefur takmarkaða þýðingu. 

Til þess að lýsa tvinnföllum á myndrænan hátt er því oft brugðið á það ráð að skoða hvernig þau færa til punktana í :math:`{{\mathbb  C}}` og lýsa á mynd afstöðunni millli :math:`z` og :math:`f(z)`. Vert er að geta þess að í þessu samhengi eru orðin :hover:`vörpun`, *færsla*, *ummyndun* o.fl. oft notuð sem samheiti fyrir orðið :hover:`fall`. Við skulum nú taka nokkur dæmi um þetta.

Vörpun :math:`{{\mathbb  C}}\to {{\mathbb  C}}` af gerðinni
:math:`z\mapsto z+a`, þar sem :math:`a\in {{\mathbb  C}}` nefnist
:hover:`hliðrun`.

Vörpun af gerðinni :math:`z\mapsto az`, nefnist
:hover:`snúningur`, ef :math:`a\in
{{\mathbb  C}}` og :math:`|a|=1`,

hún nefnist :hover:`stríkkun`, ef
:math:`a\in
{{\mathbb  R}}` og :math:`|a|>1` og

:hover:`herping,samdráttur`, ef
:math:`a\in {{\mathbb  R}}` og :math:`|a|<1`,

en almennt nefnist hún
:hover:`snústríkkun` ef
:math:`a\in {{\mathbb  C}}\setminus\{0\}`.

Vörpunin
:math:`{{\mathbb  C}}\setminus{{\{0\}}} \to {{\mathbb  C}}\setminus{{\{0\}}}`,
:math:`z\mapsto 1/z` nefnist
:hover:`umhverfing`.

.. figure:: ./myndir/fig0312.svg
    :align: center
    :alt:

     

Brotnar línulegar varpanir
~~~~~~~~~~~~~~~~~~~~~~~~~~

Hliðranir, snústríkkanir og umhverfing eru hluti af almennum flokki
varpana, en fall af gerðinni

.. math:: f(z)=\dfrac{az+b}{cz+d}, \qquad ad-bc\neq 0, \quad a,b,c,d\in {{\mathbb  C}},

kallast :hover:`brotin línuleg vörpun, brotin línuleg færsla`, *brotin
línuleg færsla* eða
*Möbíusarvörpun*.

Við sjáum að :math:`f(z)` er skilgreint fyrir öll
:math:`z\in {{\mathbb  C}}`, ef :math:`c=0`, en fyrir öll
:math:`z\neq -d/c`, ef :math:`c\neq 0`.

Eðlilegt er að útvíkka skilgreningarsvæði með því að bæta einum punkti,
:hover:`óendanleikapunkti,óendanleikapunktur` :math:`\infty`, við
planið :math:`{{\mathbb  C}}` og skilgreina þannig *útvíkkaða
talnaplanið*

.. math:: \widehat {{\mathbb  C}}={{\mathbb  C}}\cup \{\infty\}.

Þá getum við litið á :math:`f` sem vörpun

.. math:: f:\widehat {{\mathbb  C}}\to \widehat {{\mathbb  C}}

með því að setja

.. math::

  \begin{gathered}
   f(\infty)=\infty, \qquad \text{ ef } \quad c=0, \qquad \text{ en }\\
   f(-d/c)=\infty \quad \text{ og } \quad f(\infty)=\lim_{|z|\to+\infty}f(z)=a/c, \qquad
   \text{ ef } \quad c\neq 0.\end{gathered}

Með þessari viðbót verður :math:`f` gagntæk vörpun. Andhverfuna
:math:`f^{[-1]}` er létt að reikna út, því

.. math::

  w=\dfrac{az+b}{cz+d} \qquad \Leftrightarrow \qquad
   z=\dfrac{dw-b}{-cw+a}

og það segir okkur að varpanirnar

.. math:: f^{[-1]}(w)=\dfrac{dw-b}{-cw+a}.

Ef við stillum stuðlum vörpunarinnar :math:`f` upp í fylkið

.. math:: \left[\begin{matrix} a&b\\c&d\end{matrix}\right]

þá eru stuðlar andhverfunnar :math:`f^{[-1]}` lesnir út úr andhverfa
fylkinu

.. math::

  \left[\begin{matrix} a&b\\c&d\end{matrix}\right]^{-1}=
   \dfrac 1{ad-bc}\left[\begin{matrix} d&-b\\-c&a\end{matrix}\right].

Athugið að ákveðan :math:`ad-bc` styttist þegar brotið er myndað.

Ef :math:`f_1` og :math:`f_2` eru tvær brotnar línulegar varpanir, þá er
samskeyting þeirra :math:`f_3`, :math:`f_1\circ f_2=f_3`, einnig brotin
línuleg vörpun. Ef

.. math::

  f_1(z)=\dfrac{a_1z+b_1}{c_1z+d_1} \quad \text{ og } \quad
   f_2(z)=\dfrac{a_2z+b_2}{c_2z+d_2},
   \quad \text{ þá er  } \quad 
   f_3(z)=\dfrac{a_3z+b_3}{c_3z+d_3},

þar sem stuðlarnir :math:`a_3,b_3,c_3` og :math:`d_3` fást með
fylkjamargföldun,

.. math::

  \left[\begin{matrix} a_1&b_1\\c_1&d_1\end{matrix}\right]
   \left[\begin{matrix} a_2&b_2\\c_2&d_2\end{matrix}\right]
   =
   \left[\begin{matrix} a_3&b_3\\c_3&d_3\end{matrix}\right].

Það er ljóst að hliðranir, snústríkkanir og umhvernig eru brotnar
línulegar varpanir og þar af leiðandi eru allar samskeytingar af
vörpunum af þessum þremur mismunandi gerðum einnig brotnar línulegar
varpanir.

Í ljós kemur að sérhver brotin línuleg vörpun er samskeyting af
hliðrunum, snústríkkunum og
umhverfingu. Til þess að sjá þetta athugum við fyrst tilfellið
:math:`c=0`, en þá er

.. math:: f(z)=\frac adz+\frac bd,

samsett úr snústríkkun og hliðrun. Ef :math:`c\neq 0`, þá getum við
skrifað

.. math::

  f(z)= \dfrac{az+b}{cz+d}=\dfrac 1c\cdot \dfrac{az+b}{z+d/c}=
   \dfrac 1c\cdot \dfrac{a(z+d/c)-ad/c+b}{z+d/c}=
   \dfrac ac+\dfrac{-ad/c+b}{cz+d},

og sjáum að :math:`f` er samsett úr snústríkkun,

.. math:: z\mapsto cz=z_1,

hliðrun

.. math:: z_1\mapsto z_1+d=cz+d=z_2,

umhverfingu

.. math:: z_2\mapsto 1/z_2 = \dfrac 1{cz+d}=z_3,

snústríkkun

.. math:: z_3\mapsto (-ad/c+b)z_3=\dfrac{-ad/c+b}{cz+d}=z_4

og hliðrun

.. math:: z_4\mapsto z_4+a/c=a/c+\dfrac{-ad/c+b}{cz+d}.

Fastapunktar
~~~~~~~~~~~~

Ef :math:`F:M\to M` er vörpun á einhverju mengi :math:`M`, þá nefnist
:math:`p\in M` :hover:`fastapunktur` vörpunarinnar :math:`F` ef :math:`F(p)=p`.
Allir punktar í :math:`M` eru fastapunktar :hover:`samsemdarvörpunarinnar,samsemdarvörpun`
:math:`x\mapsto x`.

Nú látum við :math:`M` vera útvíkkaða talnaplanið
:math:`\widehat {{\mathbb  C}}` og :math:`f` vera brotna línulega vörpun
á :math:`\widehat {{\mathbb  C}}`, sem gefin er með

.. math:: f(z)=\dfrac{az+b}{cz+d}, \qquad ad-bc\neq 0, \qquad z\in {{\mathbb  C}}.

Ef :math:`c=0`, þá er :math:`f(\infty)=\infty` svo punkturinn
:math:`\infty` er fastapunktur í þessu tilfelli. Gerum nú ráð fyrir að
:math:`p\in {{\mathbb  C}}` sé fastapunktur. Þá fullnægir :math:`p`
jöfnunni

.. math:: \dfrac ad p+\dfrac bd=p

sem jafngildir

.. math:: (a-d)p=-b.

Ef :math:`a=d`, þá er :math:`f` vörpunin :math:`z\mapsto z+b/d`, en
þessi vörpun hefur fastapunkt aðeins ef :math:`b=0` og þá er hún
samsemdarvörpunin. Ef :math:`a\neq d`, þá fæst nákvæmlega einn
fastapunktur til viðbótar við :math:`\infty` og hann er gefinn með

.. math:: p=\dfrac {-b}{a-d}.

Þá höfum við afgreitt tilfellið :math:`c=0`. Gerum því ráð fyrir að
:math:`c\neq
0`. Þá eru :math:`\infty` og :math:`-d/c` ekki fastapunktar, svo
fastapunktarnir :math:`p` uppfylla

.. math:: \dfrac{ap+b}{cp+d}=p,

sem jafngildir því að :math:`p` uppfylli annars stigs jöfnu,

.. math:: cp^2+(d-a)p-b=0.

Hún hefur í mesta lagi tvær lausnir. Niðurstaða okkar er því:

.. _se:fastapunktar:

Setning
^^^^^^^

Brotin línuleg vörpun, sem er ekki samsemdarvörpunin :math:`z\mapsto z`,
hefur í mesta lagi tvo fastapunkta.

Þriggja punkta reglan
~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`z_1`, :math:`z_2` og :math:`z_3` vera þrjá ólíka punkta
í :math:`{{\mathbb  C}}` og lítum á brotnu línulegu vörpunina

.. math:: f(z)=\dfrac{(z-z_1)}{(z-z_3)}\cdot \dfrac{(z_2-z_3)}{(z_2-z_1)}.

Við fáum þá að :math:`f(z_1)=0`, :math:`f(z_2)=1` og
:math:`f(z_3)=\infty`. Það er hægt að alhæfa skilgreininguna þannig að
einn punktanna :math:`z_1`, :math:`z_2` eða :math:`z_3` megi vera
:math:`\infty`. Þá tökum við bara markgildi :math:`|z_j|\to
+\infty` í hægri hliðinni.

Ef :math:`z_1=\infty`, þá skilgreinum við

.. math::

  f(z)=\lim_{|\tilde z_1|\to+\infty}
   \dfrac{(z-\tilde z_1)}{(z-z_3)}\cdot \dfrac{(z_2-z_3)}{(z_2-\tilde
   z_1)}
   =\dfrac {(z_2-z_3)}{(z-z_3)}.

Það er ljóst að hægri hliðin skilgreinir vörpun með
:math:`f(\infty)=0`, :math:`f(z_2)=1` og :math:`f(z_3)=\infty`. Ef
:math:`z_2=\infty`, þá setjum við

.. math::

  f(z)=\lim_{|\tilde z_2|\to+\infty}
   \dfrac{(z-z_1)}{(z-z_3)}\cdot \dfrac{(\tilde z_2-z_3)}{(\tilde z_2-
   z_1)}
   =\dfrac {(z-z_1)}{(z-z_3)}.

og út kemur vörpun sem uppfyllir :math:`f(z_1)=0`, :math:`f(\infty)=1`
og :math:`f(z_3)=\infty`. Ef við viljum að :math:`z_3=\infty`, þá setjum
við

.. math::

  f(z)=\lim_{|\tilde z_3|\to+\infty}
   \dfrac{(z-z_1)}{(z-\tilde z_3)}\cdot \dfrac{( z_2-\tilde z_3)}{(z_2-
   z_1)}
   =\dfrac {(z-z_1)}{(z_2-z_1)}.

og við höfum :math:`f(z_1)=0`, :math:`f(z_2)=1` og
:math:`f(\infty)=\infty`.

Látum nú :math:`z_1`, :math:`z_2` og :math:`z_3` vera ólíka punkta í
:math:`\widehat {{\mathbb  C}}` og setjum

.. math:: f(z)=\dfrac{(z-z_1)}{(z-z_3)}\cdot \dfrac{(z_2-z_3)}{(z_2-z_1)}.

Niðurstaðan af því að taka markgildin þrjú hér að framan er sú að við
eigum að skipta út svigum sem innihalda :math:`z_j` og tölunni
:math:`1`, ef :math:`z_j=\infty`. Í öllum tilfellum varpast :math:`z_1`
á :math:`0`, :math:`z_2` á :math:`1` og :math:`z_3` á :math:`\infty`.

Nú skulum við breyta til og taka einhverja þrjá ólíka punkta
:math:`w_1`, :math:`w_2` og :math:`w_3` í
:math:`\widehat {{\mathbb  C}}` í staðinn fyrir punktana :math:`0`,
:math:`1` og :math:`\infty` og spyrja okkur hvernig við finnum brotna
línulega vörpun sem uppfyllir :math:`f(z_1)=w_1`, :math:`f(z_2)=w_2` og
:math:`f(z_3)=w_3`.

Þetta er leyst þannig að við finnum fyrst tvær brotnar línulegar
varpanir :math:`F` og :math:`G` með forskriftinni hér að framan sem
uppfylla :math:`F(w_1)=0`, :math:`F(w_2)=1`, :math:`F(w_3)=\infty`,
:math:`G(z_1)=0`, :math:`G(z_2)=1` og :math:`G(z_3)=\infty`. Þá
uppfyllir samskeytingin

.. math:: f(z)=F^{-1}\circ G(z)

skilyrðin :math:`f(z_1)=w_1`, :math:`f(z_2)=w_2` og :math:`f(z_3)=w_3`.

Hugsum okkur nú að :math:`g` sé önnur brotin línuleg vörpun sem
uppfyllir :math:`g(z_1)=w_1`, :math:`g(z_2)=w_2` og :math:`g(z_3)=w_3`.
Þá hefur vörpunin :math:`f^{-1}\circ g(z)` þrjá fastapunkta :math:`z_1`,
:math:`z_2` og :math:`z_3`. Setningin hér að framan um fastapunkta segir nú að
:math:`f^{-1}\circ g(z)=z` fyrir öll
:math:`z\in \widehat {{\mathbb  C}}` og þar með er :math:`f(z)=g(z)`
fyrir öll :math:`z\in \widehat {{\mathbb  C}}`. Niðurstaðan er því:

.. _se:thrir\_punktar:

Setning
^^^^^^^

(*Þriggja punkta reglan*)   Ef gefnir eru þrír ólíkir punktar
:math:`z_1`, :math:`z_2` og :math:`z_3` í :math:`\widehat
{{\mathbb  C}}` og þrír ólíkir punktar :math:`w_1`, :math:`w_2` og
:math:`w_3` í :math:`\widehat {{\mathbb  C}}`, þá er til nákvæmlega ein
brotin línuleg vörpun :math:`f` sem varpar :math:`z_1` á :math:`w_1`,
:math:`z_2` á :math:`w_2` og :math:`z_3` á :math:`w_3`. Hún er gefin með
formúlunni :math:`f=F^{-1}\circ G` þar sem

.. math::

  F(w)=\dfrac{(w-w_1)}{(w-w_3)}\cdot \dfrac{(w_2-w_3)}{(w_2-w_1)}
   \quad \text{ og } \quad 
   G(z)=\dfrac{(z-z_1)}{(z-z_3)}\cdot \dfrac{(z_2-z_3)}{(z_2-z_1)}.

Þetta má einnig orða þannig að fallgildin :math:`w=f(z)` eru leyst úr
úr jöfnunni

.. math::

  \dfrac{(w-w_1)}{(w-w_3)}\cdot \dfrac{(w_2-w_3)}{(w_2-w_1)}
   =
   \dfrac{(z-z_1)}{(z-z_3)}\cdot \dfrac{(z_2-z_3)}{(z_2-z_1)}.

Þessi stærðtákn á að túlka þannig að ef :math:`z_j=\infty` eða
:math:`w_k=\infty` kemur fyrir innan einhverra sviga, þá á að skipta
þættinum sem inniheldur :math:`z_j` eða :math:`w_k` út fyrir töluna
:math:`1`.

Myndir af línum og hringum
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ein leið til þess að setja tvinngild föll :math:`f:X\to {{\mathbb  C}}`
fram á myndrænan hátt er að líta á þau sem varpanir sem taka punkta í
einu afriti af tvinntöluplaninu :math:`{{\mathbb  C}}` yfir í annað
afrit. 

Þá er :math:`X` teiknað upp í :math:`z`-plani og myndmengið
:math:`Y=\{w=f(z); z\in X\}` teiknað upp í :math:`w`-plani og síðan er
sýnt hvernig :math:`f` varpar punktum :math:`z\in X` á punkta
:math:`w=f(z)\in Y`. Oft er litið á einhverja fjölskyldu af ferlum í
:math:`X` og sýnt hvernig hún varpast yfir í :math:`Y`.

.. figure:: ./myndir/fig0313.svg
    :align: center
    :alt: Mynd: Varpanir

    Mynd: Varpanir

:hover:`Hliðrun` :math:`z\mapsto z+a` varpar línu gegnum
punktinn :math:`m` með þvervigur :math:`{\beta}` á línuna gegnum
:math:`m+a` með þvervigur :math:`{\beta}` og hún varpar hring með miðju
:math:`m` og geislann :math:`r` á hring með miðju :math:`m+a` og
geislann :math:`r`.

.. figure:: ./myndir/fig0314.svg
    :align: center
    :alt: Mynd: Hliðrun

    Mynd: Hliðrun

:hover:`Snústríkkun` :math:`z\mapsto az`, :math:`a\in {{\mathbb  C}}\setminus {{\{0\}}}`,
varpar línu gegnum punktinn :math:`m` með þvervigur :math:`{\beta}` á
línuna gegnum :math:`am` með þvervigur :math:`a{\beta}`.

Til þess að sjá þetta athugum við að jafna línunnar er af gerðinni
:math:`\bar {\beta} z+{\beta}\bar z+c=0` og ef við stingum
:math:`z=w/a`, þar sem :math:`w=az` er myndpunktur :math:`z`, inn í
þessa jöfnu, þá sjáum við að :math:`w` verður að uppfylla
:math:`(\bar {\beta}/a) w+({\beta}/\bar a)\bar w+c=0` og þar með
:math:`\bar a\bar {\beta} w+a{\beta}\bar w+c|a|^2=0`.

Snústríkkun varpar hring með miðju í :math:`m` og geislann :math:`r` á
hring með miðju í :math:`am` og geislann :math:`|a|r`.

.. figure:: ./myndir/fig0315.svg
    :align: center
    :alt: Mynd: Snústríkkun

    Mynd: Snústríkkun

:hover:`Umhverfing` er gefin með
:math:`z\mapsto 1/z`, :math:`0\to {\infty}`, :math:`{\infty}\to 0`. Til
þess að sjá hvernig hún varpar hringum og línum, þá lítum við á mengi
allra punkta :math:`z` sem gefnir eru með formúlunni

.. math:: {\alpha}|z|^2+\bar {\beta} z+{\beta}\bar z +{\gamma}=0,

en við höfum lýst öllum þeim mengjum sem svona jafna skilgreinir.

Við stingum myndpunktinum :math:`w`, en hann uppfyllir :math:`z=1/w`,
inn í þessa jöfnu og fáum að hann verður að uppfylla

.. math:: {\gamma}|w|^2+{\beta}w+\bar {\beta}\bar w +{\alpha}=0.

Ef þetta er jafna línu gegnum :math:`0` með þvervigur :math:`{\beta}`,
þá er :math:`{\alpha}={\gamma}=0` og við fáum að :math:`w` liggur á línu
gegnum :math:`0` með þvervigur :math:`\bar {\beta}`.

Ef þetta er jafna línu sem fer ekki gegnum :math:`0` og hefur þvervigur
:math:`{\beta}`, þá er :math:`{\alpha}=0` og :math:`{\gamma}\neq
0`. Við fáum því að myndmengið er hringur með miðju :math:`m=-\bar
{\beta}/{\gamma}` og geislann :math:`r=|{\beta}|/|{\gamma}|`.

.. figure:: ./myndir/fig0316.svg
    :align: center
    :alt: Mynd: Umhverfing af línu.

    Mynd: Umhverfing af línu.

.. figure:: ./myndir/fig0316a.svg
    :align: center
    :alt: Mynd: Umhverfing af línu.

    Mynd: Umhverfing af línu.

Ef við erum með jöfnu hrings gegnum :math:`0`, þá er
:math:`{\alpha}\neq 0`, :math:`{\gamma}=0`, miðjan er
:math:`m=-{\beta}/{\alpha}` og geislinn er
:math:`r=|{\beta}|/|{\alpha}|`. Athugum að punkturinn
:math:`-2{\beta}/{\alpha}` er á hringnum og því er myndmengi hans línan
með þvervigur :math:`\bar {\beta}` gegnum punktinn
:math:`-{\alpha}/2{\beta}=-{\alpha}\bar{\beta}/2|{\beta}|^2`.

Ef við erum hins vegar með hring, sem inniheldur ekki :math:`0`, þá er
:math:`{\alpha}\neq 0`, :math:`{\gamma}\neq 0`, miðjan er
:math:`m=-{\beta}/{\alpha}` og geislinn er
:math:`r=\sqrt{|{\beta}|^2-{\alpha}{\gamma}}\, /|{\alpha}|`. Myndmengið
er hringur með miðju :math:`-\bar {\beta}/{\gamma}` og geislann
:math:`\sqrt{|{\beta}|^2-{\alpha}{\gamma}}\, /|{\gamma}|`.



.. figure:: ./myndir/fig0317.svg
    :align: center
    :alt: Mynd: Umhverfing af hring.

    Mynd: Umhverfing af hring.

.. figure:: ./myndir/fig0317a.svg
    :align: center
    :alt: Mynd: Umhverfing af hring.

    Mynd: Umhverfing af hring.

Eins og við höfum séð, þá er sérhver brotin línuleg vörpun samsett úr
hliðrunum, snústríkkunum og umhverfingu, svo niðurstaða útreikninga
okkar er:

Setning
^^^^^^^

Sérhver brotin línuleg vörpun
:hover:`brotin línuleg færsla` varpar hring í :math:`{{\mathbb  C}}` á
hring eða línu og hún varpar línu á hring eða línu.
