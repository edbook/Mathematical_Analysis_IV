
Nokkur undirstöðuatriði um hlutafleiðujöfnur
============================================

Nokkur atriði um hlutafleiður og hlutafleiðujöfnur
--------------------------------------------------

*Hlutafleiðujafna* er jafna sem tjáir samband fallgilda og gilda á
hlutafleiðum einhvers falls sem háð er fleiri en einni breytistærð.
*Stig jöfnunnar* er hæsta stig á hlutafleiðu, sem kemur fyrir í
jöfnunni. Það er til margs konar ritháttur til þess að tákna
hlutafleiður og sem dæmi getum við tekið hlutafleiðu af fallinu
:math:`u` með tilliti til breytistærðarinnar :math:`x_j`. Hún getur
verið skrifuð sem

.. math::

  \partial_ju, \quad  \dfrac{\partial u}{\partial x_j}, \quad
      \partial _{x_j}u, \quad   u'_{x_j} \quad \text{ eða } u_{x_j}.

Í þessum fyrirlestrum notum við þrjár fyrstu aðferðirnar til þess að
tákna hlutafleiður, en ekki fjórðu og fimmtu aðferðina, því þær koma
illa heim og saman við annan rithátt hjá okkur. Ef við veljum fyrsta
ritháttinn þá getum við alltaf skrifað fyrsta stigs jöfnu af tveimur
breytistærðum með jöfnu af gerðinni

.. math::

  F(x_1,x_2,u(x_1,x_2), \partial _1 u(x_1, x_2),
      \partial _2 u (x_1, x_2)) = 0.

Til þess að stytta jöfnuna er sleppt að skrifa inn punktinn
:math:`(x_1, x_2)` þar sem fallgildin eru tekin og þannig fæst jafnan

.. math:: F(x_1,x_2,u,\partial _1 u, \partial _2 u) = 0.

Annars stigs jafna af tveimur breytistærðum er af gerðinni

.. math::

  F(x_1,x_2,u, \partial _1 u,  \partial _2 u,
      \partial _1^2u, \partial _1 \partial _2 u,
       \partial_2^2 u) = 0.

Fjölvísar – einföldun á rithætti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Á þessu einfalda dæmi sjáum við að hlutafleiðunum fjölgar hratt um leið
og breytistærðunum fjölgar. Til þess að geta ritað flóknar
hlutafleiðujöfnur með auðveldum hætti er nauðsynlegt að velja góðan
rithátt. Það er best gert með því að skilgreina fyrst virkjann

.. math::

  \partial = (\partial _1, \dots , \partial _n) =
      \text{grad} = \nabla,

sem úthlutar falli :math:`u` af :math:`n` breytistærðum
:math:`x=(x_1,\dots,x_n)` stigli sínum,

.. math::

  \partial u = (\partial _1u, \partial _2u,
      \dots , \partial _nu) = \text{grad }u =
      \nabla u.

Vigur af gerðinni :math:`\alpha  = (\alpha _1,  \dots , \alpha _n)` þar sem :math:`\alpha _j` eru heiltölur :math:`\geq 0`
kallast *fjölvísir* eða *fjölnúmer*. Fyrir sérhvern fjölvísi
:math:`\alpha` skilgreinum við hlutafleiðuvirkjann

.. math::

  \partial ^{\alpha} = \partial _1^{\alpha _1}
      \dots \partial _n^{\alpha _n},

en hann úthlutar fallinu :math:`u` hlutafleiðunni

.. math::

  \partial ^{\alpha} u = \partial _1^{\alpha _1}
      \partial _2^{\alpha _2} \dots \partial _n^{\alpha _n} u.

Til þess að átta okkur á þessum rithætti skulum við líta á fall
:math:`u` af þremur breytistærðum :math:`x = (x_1, x_2, x_3)`. Við höfum
þá

.. math::

  \begin{aligned}
   \partial ^{\alpha} u  &=  u \, , &\qquad
     & \text{ef} \quad \alpha = (0,0,0) \, , \\
   \partial ^{\alpha} u  &=  \frac{{\partial}^2 u}
   {{\partial}x_1^2} \, , &\qquad
     & \text{ef} \quad \alpha = (2,0,0) \, , \\
   \partial ^{\alpha} u  &=  \frac{{\partial}^6 u}    
   {{\partial}x_1 {\partial}x_2^2 {\partial}x_3^3} \, , &\qquad
     & \text{ef} \quad \alpha = (1,2,3) \, , \\
   \partial ^{\alpha} u  &=  \frac{{\partial}^8 u}
   {{\partial}x_1^3 {\partial}x_2^2 {\partial}x_3^3} \, , &\qquad
     & \text{ef} \quad \alpha = (3,2,3) \, .
  \end{aligned}

*Stig* hlutafleiðunnar :math:`\partial^\alpha u` er
:math:`|\alpha |= \alpha_1 + \dots + \alpha_n`.

Línulegar hlutafleiðujöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hlutafleiðujafna af stigi :math:`m` er sögð vera línuleg ef hægt er að
umrita hana yfir í jafngilda jöfnu af gerðinni

.. math:: L u = f,

þar sem :math:`f` er gefið fall á einhverju opnu mengi :math:`X` í
:math:`{{\mathbb  R}}^n` og :math:`L` er línuleg vörpun sem úthlutar
fallinu :math:`u` línulegri samantekt af :math:`u` og hlutafleiðum
:math:`u` upp að stigi :math:`m` með stuðlum sem eru háðir
:math:`x\in X`. Línuleg vörpun af þessu tagi nefnist *línulegur
hlutafleiðuvirki* og við getum skrifað hana á forminu

.. math::

  L u(x) = \sum _{|\alpha |\leq m} \, a_{\alpha} (x) 
    \partial ^{\alpha} u(x), \qquad x\in X,

þar sem stuðullinn :math:`a_{\alpha}` er háður fjölvísinum
:math:`{\alpha} = (\alpha _1 , \dots , \alpha _n )` og punktinum
:math:`x = (x_1, \dots , x_n)`. Jafnan :math:`L u = f` er sögð vera
*óhliðruð* ef :math:`f` er núllfallið, en *hliðruð* annars.

Allar hlutafleiðujöfnur sem við fjöllum um eru línulegar. Ef stuðlarnir
:math:`a_{\alpha}` eru samfelld föll, sem skilgreind eru á opnu mengi
:math:`X` í :math:`{{\mathbb  R}}^n`, þá getum við litið á :math:`L` sem
vörpun :math:`L:C^m(X)\to C(X)`. Vörpunin :math:`L` er greinilega
línuleg, því

.. math::

  L(u+v)=Lu+Lv \qquad \text { og } \qquad L(cu)=cLu, \qquad
   u,v\in C^m(X), \quad c\in {{\mathbb  C}}.

Við gerum alltaf ráð fyrir að föllin :math:`u` geti verið tvinngild.
*Kjarni* eða *núllrúm* línulegs hlutafleiðuvirkja :math:`L` samanstendur
af öllum lausnum :math:`u\in C^m(X)`, á óhliðruðu jöfnunni :math:`Lu=0`.
Núllrúmið er línulegt rúm. Ef :math:`u_p` er lausn á :math:`Lu=f`, þá er
sérhver önnur lausn :math:`u` á :math:`Lu=f` af gerðinni
:math:`u=v+u_p`, þar sem :math:`v` er í núllrúminu.

Í mörgum útleiðslum á lausnarformúlum fyrir hlutafleiðujöfnur munum við
notfæra okkur það sem kallað er *samlagningarlögmál* línulegra
hlutafleiðuvirkja (e. *superposition principle*), en það segir að ef
:math:`Lu_j=f_j`, þar sem :math:`u_j\in C^m(X)` og :math:`f_j\in C(X)`,
:math:`j=1,2,3,\dots` og við setjum :math:`u=\sum_ju_j` og
:math:`f=\sum_jf_j`, þá er :math:`Lu=f`. Hér er gert ráð fyrir að það
megi láta hlutafleiðuvirkjann :math:`L` verka lið fyrir lið í summunni
fyrir :math:`u`. Það er að sjálfsögðu hægt ef summan hefur endanlega
marga liði. Samlagningarlögmálið er bein afleiðing af því að virkinn
:math:`L` er línulegur,

.. math:: Lu=\sum_jLu_j=\sum_jf_j=f.

Kennimargliða og kennijafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alveg eins og fyrir venjulega afleiðuvirkja þá skilgreinum við
*kennimargliðu* virkjans :math:`L` sem

.. math:: P (x, \xi ) = \sum _{|\alpha |\leq m}  a_{\alpha} (x) \xi ^{\alpha},

þar sem :math:`\xi = (\xi_1 , \dots , \xi_n)` og
:math:`\xi ^{\alpha} = \xi_1^{\alpha_1}  \xi_2^{\alpha_2}  \dots  \xi_n^{\alpha_n}`. Þetta er margliða af :math:`n` breytistærðum
af stigi :math:`\leq m` með stuðlum sem breytast með :math:`x`.
Hliðstætt við ritháttinn fyrir venjulega afleiðuvirkja er
hlutafleiðuvirkinn einnig táknaður með

.. math::

  P(x, \partial ) = \sum _{|\alpha |\leq m}
    a_{\alpha} (x) \partial ^{\alpha}.

Lítum nú á veldisvísisfallið :math:`u(x)=e^{{{\langle x,\zeta\rangle}}}`,
þar sem :math:`{{\langle x,\zeta\rangle}}=x_1\zeta_1+\cdots+x_n\zeta_n`
er innfeldi :math:`x\in {{\mathbb  R}}^n` og
:math:`\zeta\in {{\mathbb  C}}^n`. Þá er
:math:`\partial_{x_j}e^{{{\langle x,\zeta\rangle}}} =\zeta_je^{{{\langle x,\zeta\rangle}}}` og um hærri afleiður gildir
:math:`\partial^\alpha e^{{{\langle x,\zeta\rangle}}}=\zeta^\alpha e^{{{\langle x,\zeta\rangle}}}`.
Eftir að hafa tekið línulegar samantektir af hlutafleiðunum, þá fáum við
að

.. math::

  P(x,\partial)e^{{{\langle x,\zeta\rangle}}}=\sum\limits_{|\alpha|\leq m}a_\alpha(x)\zeta^\alpha
   e^{{{\langle x,\zeta\rangle}}}=P(x,\zeta)e^{{{\langle x,\zeta\rangle}}}, \qquad x\in {{\mathbb  R}}^n.

Ef virkinn hefur fastastuðla, :math:`P(x,\partial)=P(\partial)`, þá
sést að :math:`u(x)=e^{{{\langle x,\zeta\rangle}}}` er í núllrúminu ef
:math:`\zeta` er núllstöð kennimargliðunnar, :math:`P(\zeta)=0`.
Núllstöðvamengi margliðu af mörgum breytistærðum er alltaf óendanlegt og
föllin :math:`e^{{{\langle x,\zeta\rangle}}}`,
:math:`\zeta\in {{\mathbb  C}}^n` eru línulega óháð. Þar með sjáum við
að núllrúmið er óendanlega vítt.

Hlutafleiðujöfnur með hliðarskilyrðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lausn á venjulegri línulegri afleiðujöfnu af stigi
:math:`m` ákvarðast ótvírætt af :math:`m` skilyrðum á lausnina í einum
punkti, svokölluðum upphafsskilyrðum. Einnig gátum við fengið ótvírætt
ákvarðaða lausn með því að setja :math:`m` skilyrði á lausnina í tveimur
punktum, svokölluð jaðarskilyrði. Lausnir :math:`u` á línulegum
hlutafleiðujöfnum ákvarðast ekki ótvírætt af gildum :math:`u` og
:math:`\partial^\alpha u`, :math:`|\alpha|\leq m` í endanlega mörgum
punktum og því eru *hliðarskilyrði* sett á lausnina á óendanlegum
mengjum, sem oftast eru jaðrar á opnum hlutmengjum í
:math:`{{\mathbb  R}}^n`. Þessi skilyrði nefnast ýmist *upphafsskilyrði*
eða *jaðarskilyrði* og eru krafa um að lausnin og ákveðnar afleiður
hennar taki fyrirfram gefin gildi á ákveðnum mengjum.

Þegar fjallað er um almenna eiginleika lausna á hlutafleiðujöfnum, er
einfaldast að nota þann rithátt sem við höfum verið að lýsa. Flestar af
þeim jöfnum, sem við munum fjalla um eru upprunnar í eðlisfræði og
lausnirnar lýsa þá ástandi eðlisfræðilegra kerfa. Í eðlisfræði ráða
fastar venjur um tákn á breytistærðum. Það er hyggilegt að fylgja þeim
venjum og tákna breyturnar með :math:`x,y,z,t,\dots`, í stað
:math:`x_1,x_2,x_3,\dots`. Þannig er :math:`t` notað til þess að tákna
*tíma* og :math:`(x,y,z)` notað til að tákna staðarvigur í *rétthyrndum
hnitum*. *Pólhnit* í plani eru táknuð með :math:`(r,\theta)`. *Kúluhnit*
í þrívíðu rúmi eru táknuð með :math:`(r,\theta,\phi)`.

Hlutafleiðujöfnur í eðlisfræði
------------------------------

Hlutafleiðujöfnur koma fyrir í ótal tilbrigðum í eðlisfræði. Lausnir
þeirra lýsa ástandi eðlisfræðilegra kerfa eða eru nálganir á
ástandsstærðum. Við munum nú taka nokkur dæmi um slíkar
hlutafleiðujöfnur. Við nefnum helstu eðlisfræðilögmál, sem til
grundvallar liggja, en förum ekki út í ítarlegar útskýringar á þeim. Til
þess að kafa dýpra í lögmálin, þarf lesandinn að taka fram bækur um
efnið, sem lesnar eru í eðlis- og verkfræðinámskeiðum. Hér einbeitum við
okkur að stærðfræðilega hluta útleiðslanna í þeim tilgangi að sýna
hversu fjölbreytileg þessi fræði eru.

Hitastig í föstu efni – varmaleiðnijafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Hitastig;varmaleiðnijafna

*Varmaleiðnijafna* kemur fyrir þegar fjallað er um líkön fyrir hitastig
:math:`T=T(x,y,z,t)` í föstu efni en það er fall af þremur
rúmbreytistærðum :math:`(x,y,z)` og tíma :math:`t`. Við látum
:math:`{\varrho}={\varrho}(x,y,z)` tákna eðlismassa efnisins og
:math:`c=c(x,y,z)` varmarýmd þess. Til grundvallar leggjum við lögmál
Fouriers, sem segir að
varmaflæðið :math:`\vec v=\vec v(x,y,z,t)` sé gefið með formúlunni

.. math::

  \vec v= -{\lambda}\,\nabla \,T=-{\lambda}
   \bigg(\dfrac{\partial T}{\partial x},\dfrac{\partial T}{\partial y},
   \dfrac{\partial T}{\partial z}  \bigg)

þar sem fallið :math:`{\lambda}={\lambda}(x,y,z)>0` kallast
*varmaleiðnistuðull* efnisins. Þetta þýðir
að ef við lítum á lítinn flatarskika :math:`dA` umhverfis punktinn
:math:`(x,y,z)` með þvervigur :math:`\vec n`, þá er varmaorkan sem
flæðir á tímaeiningu í gegnum skikann í stefnu :math:`\vec n` jöfn

.. math:: {{\langle \vec v,\vec n\rangle}} dA=-{\lambda}{{\langle \nabla \, T,\vec n\rangle}}dA.

Við látum :math:`F(x,y,z,t)` tákna þá varmaorku sem myndast í punktinum
:math:`(x,y,z)` á rúm- og tímaeiningu. Ef :math:`F(x,y,z,t)>0` þá hitnar
efnið umhverfis punktinn :math:`(x,y,z)` á tímanum :math:`t`, en ef
:math:`F(x,y,z,t)<0` þá kólnar það.

Nú lítum við á lítinn rúmskika :math:`D` með jaðri :math:`{\partial} D`
og athugum orkuvarðveisluna í honum. Við táknum *ytri* þvervigurinn á
jaðarinn með :math:`\vec n`. Varmaorkan í :math:`D` sem fall af tíma er
þá

.. math:: E(t)= \iiint\limits_D c{\varrho}T\, dV.

Lögmálið um varðveislu orkunnar segir okkur að breyting varmaorkunnar í
:math:`D` sé jöfn summu þeirrar orku sem flæðir inn gegnum jaðarinn og
þeirrar orku sem myndast inni í :math:`D`. Þetta tjáum við með jöfnunni

.. math::

  \dfrac {\partial}{\partial t}
   \iiint\limits_D c{\varrho}T\, dV = 
   \iint\limits_{\partial D} 
   {\lambda}{{\langle \nabla \, T,\vec n\rangle}}\, dA +
   \iiint\limits_D F\, dV.

.. figure:: ./myndir/fig0115.svg
    :align: center
    :alt: Varmaflæði

    Mynd: Varmaflæði

Í þessari jöfnu táknar :math:`dV=dxdydz` 
:hover:`rúmmálsfrymið, rúmmálsfrymi` í :math:`D`, en :math:`dA` táknar flatarmálsfrymið
á yfirborðinu :math:`{\partial}D`. Athugið að flæði inn gegnum jaðarinn
er í stefnu :math:`-\vec n`. Nú beitum við Gauss–setningunni á flæðið
:math:`\vec v=-{\lambda}\,\nabla\, T`

.. math::

  \iint\limits_{\partial D} 
   {{\langle \vec v,\vec n\rangle}}dA =
   \iiint\limits_D \nabla\cdot \vec v \, dV.

Við getum því skrifað jöfnuna um orkuvarðveisluna í :math:`D` sem

.. math::

  \iiint\limits_D \bigg(
   c{\varrho}\dfrac {\partial T}{\partial t}-\nabla\cdot 
   \big({\lambda}\,\nabla \, T\big)
   - F\bigg) \, dV=0.

Fyrst þessi jafna gildir hvernig sem rúmskikinn :math:`D` er valinn, þá
verður heildisstofninn að vera :math:`0` og við fáum jöfnuna

.. math::

  c{\varrho}\dfrac {\partial T}{\partial t}-\nabla\cdot\big({\lambda}\,\nabla \, T\big)
   = F(x,y,z,t).

Ef við gerum ráð fyrir að :math:`{\varrho}`, :math:`c` og
:math:`{\lambda}` séu fastar og setjum
:math:`{\kappa}={\lambda}/(c{\varrho})` og :math:`f=F/(c{\varrho})`, þá
fáum við að hitastigið :math:`T` uppfyllir 
:hover:`varmaleiðnijöfnuna, varmaleiðnijafna`

.. math::

  \dfrac {\partial T}{\partial t}-{\kappa}\nabla\cdot\big(\nabla\, T\big) =
   \dfrac {\partial T}{\partial t}-{\kappa}{\Delta}T =
   f(x,y,z,t),

þar sem :math:`\Delta` táknar Laplace–virkjann,

.. math::

  \Delta T =\nabla\cdot \big(\nabla\, T\big) = 
   \dfrac {\partial^2 T}{\partial x^2}+
   \dfrac {\partial^2 T}{\partial y^2}+
   \dfrac {\partial^2 T}{\partial z^2}.

Varmaleiðnijafnan nefnist einnig *sveimjafna*. Sú nafngift á við þegar
verið er að lýsa styrk :math:`u(x,y,z,t)` á uppleystu efni í vökva.
Útleiðslan á sveimjöfnunni er hliðstæð útleiðslu okkar hér að framan. Í
stað lögmáls Fouriers kemur lögmál Flicks, en það segir að flæði
efnisins sé :math:`-\kappa\nabla u` og í þessu samhengi er
:math:`\kappa` þá nefnt *sveimstuðull*.

.. end-toggle::

Samhverfa – varmaleiðnijafna í einni og tveimur rúmvíddum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Einfaldanir á varmaleiðnijöfnu

Varmaleiðnijafnan lýsir eiginleikum falls :math:`T` af fjórum
breytistærðum. Í ýmsum verkefnum er hægt að gera ráð fyrir samhverfu af
einhverju tagi og með því fækkar óháðu rúmbreytistærðunum. Ef við gerum
ráð fyrir því að varmaflæðið sé alltaf samsíða ákveðnu plani, sem við
veljum sem :math:`(x,y)`-plan, þá fáum við tvívíðu varmaleiðnijöfnuna

.. math::

  \dfrac{\partial T}{\partial t}-\kappa\bigg(
   \dfrac{\partial^2 T}{\partial x^2}
   +\dfrac{\partial^2 T}{\partial y^2}\bigg)=f(x,y,t).

Ef hægt er að gera ráð fyrir því að varmaflæðið sé alltaf samsíða
ákveðinni línu, sem við veljum sem :math:`x`-ás, þá fæst

.. math::

  \dfrac{\partial T}{\partial t}-\kappa
   \dfrac{\partial^2 T}{\partial x^2} =f(x,t).

Þetta á við um hitastig í vegg, jarðlögum eða stöng, þar sem gert er ráð
fyrir að varmaflæðið sé alls staðar í sömu stefnu. Ef við tökum stöng af
lengd :math:`L` sem dæmi og veljum hnitin þannig að :math:`x`-ásinn sé
eftir stönginni, þá uppfyllir hitastigið

.. math::

  \dfrac{\partial T}{\partial t}-\kappa
   \dfrac{\partial^2 T}{\partial x^2} =f(x,t), \qquad
   0<x<L, \quad t>0,

og fallið :math:`c{\varrho}f(t,x)` gefur varmaframleiðsluna í stönginni
á lengdar- og tímaeiningu. Jaðarskilyrðin sem sett eru í endapunktinum
:math:`x=0` gætu til dæmis verið eitt af þrennu,

.. math::

  T(0,t)=T_0, \qquad
   -\lambda\partial_xT(0,t) = v_0,  \qquad
   -\lambda\partial_xT(0,t) = kT(0,t).

Fyrsta skilyrðið er að hitastigið sé fast í enda stangarinnnar, annað
skilyrðið segir að varmaflæðið gegnum enda stangarinnar sé fast og það
þriðja segir að varmaflæðið gegnum enda stangarinnar sé í hlutfalli við
hitastigið þar. Hliðstæð skilyrði má hugsa sér í punktinum :math:`x=L`.
Dæmigert upphafs- og jaðargildisverkefni gæti síðan verið að leysa

.. math::

  \begin{cases}
   \dfrac{\partial T}{\partial t}-\kappa
   \dfrac{\partial^2 T}{\partial^2 x}=f(x,t), 
   \qquad 0<x<L, \quad t>0,& \\
   T(0,t)=T_0, \qquad -\lambda \partial_xT(L,t)=k T(L,t).
   \end{cases}

Hugsum okkur nú að fallið :math:`f` sem lýsir varmamynduninni í
stönginni sé einungis háð :math:`x` en ekki háð tíma :math:`t`,
:math:`f=f(x)` og að við vitum að markgildin
:math:`\lim_{t\to+\infty} \partial_tT(x,t)=0`,
:math:`\lim_{t\to+\infty} T(x,t)=u(x)`,
:math:`\lim_{t\to+\infty} \partial_xT(x,t)=u{{^{\prime}}}(x)`,
:math:`\lim_{t\to+\infty} \partial_x^2T(x,t)=u{{^{\prime\prime}}}(x)`
séu öll til. Þá segjum við að :math:`u` lýsi *æstæðu hitaástandi*
í stönginni. Til þess að finna :math:`u`
þurfum við þá að leysa jaðargildisverkefnið

.. math::

  -\kappa u{{^{\prime\prime}}}=f(x), \quad
   0<x<L, \qquad u(0)=T_0, \qquad -\lambda u{{^{\prime}}}(L)=ku(L).

.. end-toggle::

Varmajafnvægi – Laplace-jafna og Poisson-jafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Varmajafnvægi

Oft er áhugavert að líta á *tímaóháð ástand* eða *æstætt ástand*. Þá er
einfaldlega gert ráð fyrir því að tímaafleiðan sé :math:`0` og að ytri
áhrif á kerfið séu tímaóháð. Hliðraða varmaleiðnijafnan einfaldast þá í
*Poisson-jöfnuna*

.. math:: -{\kappa}\Delta u=f(x,y,z),

Ef engin varmamyndun er í svæðinu, þá einfaldast varmaleiðnijafnan í
*Laplace-jöfnu*, :math:`\Delta u=0`.

.. end-toggle::

Sveiflandi strengur – bylgjujafna í einni rúmvídd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Strengur;bylgjujafna

Við höfum áður leitt út hreyfijöfnur fyrir festi. Nú
skulum við líta á skylt dæmi. Það er strengur af lengd :math:`L` og
massa :math:`m`. Við gerum ráð fyrir að hann sé strekktur, festur niður
í báðum endapunktum og að hann sveiflist í plani. Við veljum hnit þannig
að stengurinn sé á :math:`x`-ás þegar hann er í kyrrstöðu og látum
:math:`u(x,t)` tákna færslu strengsins frá punktinum :math:`x`. 

.. figure:: ./myndir/fig0113.svg
    :align: center
    :alt: Strengur

    Mynd: Strengur

Til þess að leiða út jöfnu fyrir hreyfingu strengsins, þá skoðum við
lítinn bút af honum á einhverju augnabliki :math:`t` yfir bilinu
:math:`[x,x+h]`. 

.. figure:: ./myndir/fig0114.svg
    :align: center
    :alt: Kraftar í streng

    Mynd: Kraftar í streng

Ef :math:`T` táknar spennuna í strengnum, þá er lóðrétti þáttur
togkraftsins, sem verkar á bútinn,

.. math:: -T\sin {\alpha}+T\sin {\beta}.

Við athugum að :hover:`bogalengdarfrymið, bogalengdarfrymi` á strengnum er

.. math:: ds=\sqrt{1+\big({\partial}_xu(x,t)\big)^2}\,  dx

og

.. math::

  \sin {\alpha} = \dfrac{{\partial}_xu(x,t)}
   {\sqrt{1+\big({\partial}_xu(x,t)\big)^2}}, \qquad 
   \sin {\beta} = \dfrac{{\partial}_xu(x+h,t)}
   {\sqrt{1+\big({\partial}_xu(x+h,t)\big)^2}}.

Annað lögmál Newtons gefur okkur því

.. math::

  \begin{gathered}
   \int_x^{x+h} {\varrho}{\partial}_t^2u({\xi},t)
   {\sqrt{1+\big({\partial}_xu({\xi},t)\big)^2}}\, d{\xi}\\
   = T\bigg(
   \dfrac{{\partial}_xu(x+h,t)}
   {\sqrt{1+\big({\partial}_xu(x+h,t)\big)^2}} - 
   \dfrac{{\partial}_xu(x,t)}
   {\sqrt{1+\big({\partial}_xu(x,t)\big)^2}}
   \bigg),\end{gathered}

þar sem :math:`{\varrho}=m/L` táknar massa á lengdareiningu í
strengnum. Nú gerum við til einföldunar ráð fyrir því að útslagið sé það
lítið að

.. math:: \sqrt{1+\big({\partial}_xu(x,t)\big)^2}\approx 1

og þar með að það megi fella niður kvaðratræturnar í þessum jöfnum. Þá
fáum við

.. math::

  \int\limits_x^{x+h} {\varrho}\dfrac{\partial^2 u}{\partial t^2}
   ({\xi},t) \, d{\xi} = T\bigg(\dfrac{\partial u}{\partial x}(x+h,t)-
   \dfrac{\partial u}{\partial x}(x,t)\bigg).

Nú deilum við í gegnum jöfnuna með :math:`h` og látum síðan :math:`h`
stefna á núll. Þá fáum við :hover:`bylgjujöfnuna, bylgjujafna`

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-
   c^2\dfrac{\partial^2 u}{\partial x^2}=0, \qquad c=\sqrt{T/\varrho}.

Strengurinn er festur niður í báðum endapunktum, svo við fáum náttúrleg
jaðarskilyrði

.. math:: u(0,t)=u(L,t)=0.

Þetta líkan má bæta á ýmsa vegu. Ef gert er ráð fyrir að ytri kraftur
verki á strenginn og að :math:`F(x,t)` sé kraftur á lengdareiningu, sem
verkar á strenginn í punkti :math:`x` við tímann :math:`t`, þá uppfyllir
færslan :math:`u(x,t)` hliðruðu bylgjujöfnuna

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-c^2
   \dfrac{\partial^2 u}{\partial x^2}=f(x,t),

þar sem :math:`f(x,t)=F(x,t)/{\varrho}`. Ef tekið er tillit til
loftmótstöðu eða núnings í strengnum og gert er ráð fyrir að þau séu í
hlutfalli við hraðann, þá kemur til sögunnar kraftliður af gerðinni
:math:`-a\partial_tu(x,t)`, þar sem :math:`a` er fasti. Ef tekið er
tillit til fjöðrunar í strengnum og gengið er út frá lögmáli Hookes, þá
bætist við kraftliður af gerðinni :math:`-bu(x,t)`, þar sem :math:`b` er
fasti. Ef gengið er út frá öllum þessum kraftáhrifum, þá gefur annað
lögmál Newtons eins og í útleiðslunni hér að framan að færslan uppfyllir

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-c^2
   \dfrac{\partial^2 u}{\partial x^2}
   +r\dfrac{\partial u}{\partial t}+k u=f(x,t),

þar sem :math:`r=a/{\varrho}` og :math:`k=b/{\varrho}`.

.. end-toggle::

Tromma – bylgjujafna í tveimur rúmvíddum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _sytrommabylgjujafnaitveimurrumviddum:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Tromma; tvívíða bylgjujafnan

Hugsum okkur að teygjanleg þunn himna sé strengd yfir ramma og gerum ráð
fyrir að spenna í henni :math:`T` sé alls staðar sú sama. Hugsum okkur
einnig að himnan hreyfist í lóðrétta stefnu og látum :math:`u(x,y,t)`
tákna færslu hennar frá jafnvægisstöðu. Látum :math:`X` tákna svæðið í
:math:`xy`-plani, sem himnan afmarkar þegar hún er kyrr og lítum á
flatarskika :math:`D\subset X` með sléttan jaðar :math:`{\partial}D`.
Við látum :math:`\nabla u=({\partial}_xu,{\partial}_yu)` tákna stigulinn af :math:`u` með
tilliti til :math:`(x,y)` og
:math:`{\partial}_nu={\partial}u/{\partial}n={{\langle \nabla u,\vec n\rangle}}`
vera stefnuafleiðu af :math:`u` í stefnu ytri þvervigursins í punkti
:math:`(x,y)` á jaðrinum :math:`{\partial}D`.

.. figure:: ./myndir/fig1211.svg
    :align: center
    :alt: Sveiflur himnu

    Mynd: Sveiflur himnu

Nú lítum við á þann bút af himnunni sem er yfir svæðinu :math:`D`, en
það er graf fallsins :math:`u` með tilliti til :math:`(x,y)`. Ef við
tökum síðan örsmæðarbút :math:`ds` á jaðrinum á himnunni yfir :math:`D`,
þá er lóðrétti þáttur togkraftsins sem verkar á hann jafn

.. math::

  T\dfrac{{\partial}_nu}{\sqrt{1+\big({\partial}_nu\big)^2}}ds
   \approx T\dfrac{{\partial}u}{{\partial} n}ds,

ef við gefum okkur að :math:`{\partial}_nu` sé það lítið að nálga megi
kvaðratrótina með tölunni :math:`1`. Ef :math:`{\varrho}` táknar massa á
flatareiningu í himnunni, þá gefur annað lögmál Newtons

.. math::

  \iint_D{\varrho}\dfrac{{\partial}^2u}{{\partial t}^2}\, dxdy
   =\int_{{\partial}D}T\dfrac{{\partial}u}{{\partial} n}\, ds.

Með því að beita Gauss-setningunni á seinna heildið, þá fáum við

.. math::

  \iint_D{\varrho}\dfrac{{\partial}^2u}{{\partial}t^2}\, dxdy
   =\iint_{D}T\Delta  u \, dxdy,

þar sem :math:`\Delta` táknar Laplace-virkjann í breytistærðunum
:math:`(x,y)`. Fyrst þessi jafna gildir um hvaða skika sem er, þá fáum
við að :math:`u` uppfyllir bylgjujöfnuna í tvívíðu rúmi,

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-c^2\Delta u=
   \dfrac{\partial^2 u}{\partial t^2}-c^2\bigg(
   \dfrac{\partial^2 u}{\partial x^2}
   +\dfrac{\partial^2 u}{\partial y^2}\bigg)=0,

þar sem :math:`c=\sqrt{T/{\varrho}}`.

.. end-toggle::

Sveiflur í bitum – bitajafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _sysveifluribitumbitajafna:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Sveiflur í bitum

Í burðarþolsfræðinni koma fyrir margar mikilvægar hlutafleiðujöfnur.
Meðal þeirra er bylgjujafnan, sem kemur fram þegar verið er að lýsa
sveiflum í bitum. Við skulum nú líta á bita af lengd :math:`L` sem
liggur láréttur og leggja hnitakerfið þannig að :math:`x`-ásinn liggi
eftir honum endilöngum með endapunktana í :math:`x=0` og :math:`x=L`.
Við skulum láta :math:`{\varrho}(x)` vera massa á lengdareiningu í
bitanum og :math:`A(x)` vera þversniðsflatarmál hans í punktinum
:math:`x`. Gerum einnig ráð fyrir að í punktinum :math:`x` verki kraftur
í stefnu :math:`x`-ássins og að :math:`F(x,t)` sé kraftur á
lengdareiningu í punkti :math:`x` við tímann :math:`t`. Við verkun
kraftsins verður teygja í stönginni og við látum :math:`u(x,t)` tákna
færslu efnispunkts í :math:`x` frá jafnvægisstöðu. Við gefum okkur að
færslurnar sé smáar og að lögmál Hookes gildi. Það segir að spennan
:math:`{\sigma}` í efninu sé í hlutfalli við þensluna
:math:`{\epsilon}`, :math:`{\sigma}=E{\epsilon}`, þar sem :math:`E=E(x)`
er efnisfasti óháður tíma og í punktinum :math:`x` er
:math:`{\epsilon}={\partial}_xu(x,t)`. Fallið :math:`E` nefnist
Young-stuðull. Þar með er spennukrafturinn sem verkar í þversniðinu við
:math:`x` við tímann :math:`t` jafn

.. math:: S(x,t)=A(x){\sigma}(x,t)=A(x)E(x){\partial}_xu(x,t).

.. figure:: ./myndir/fig1212.svg
    :align: center
    :alt: Langsveiflur í bita

    Mynd: Langsveiflur í bita

Nú lítum við á bút af bitanum sem afmarkast af bilinu :math:`[x,x+h]`.
Spennukrafturinn sem verkar á bútinn er þá :math:`S(x+h,t)-S(x,t)` og
því fáum við að annað lögmál Newtons gefur

.. math::

  \int_x^{x+h} 
   {\varrho}({\xi}){\partial}_t^2u({\xi},t)A({\xi})\, d{\xi} 
   =
   \big(S(x+h)-S(x)\big)
   +\int_x^{x+h} F({\xi},t)\, d{\xi}.

Með því að deila í gegnum þessa jöfnu með :math:`h` og láta síðan
:math:`h\to 0`, þá fáum við

.. math::

  {\varrho}A\dfrac{{\partial}^2u}{{\partial}t^2}
   -\dfrac{\partial}{\partial x}\bigg(
   AE\dfrac{{\partial}u}{{\partial}x}\bigg)=F(x,t).

Í þessari útleiðslu var hægt að gefa sér að :math:`{\varrho}`, :math:`A`
og :math:`E` væru föll af :math:`x`. Í sértilfellinu þegar þetta eru
fastar, þá er hreyfingunni lýst með hliðruðu bylgjujöfnunni

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-c^2
   \dfrac{\partial^2 u}{\partial x^2}=f(x,t),

þar sem :math:`c=\sqrt{E/{\varrho}}` og :math:`f=F/({\varrho}A)` er
kraftur á massaeiningu í bitanum.

.. figure:: ./myndir/fig1213.svg
    :align: center
    :alt: Þversveiflur í bita.

    Mynd: Þversveiflur í bita.

Nú skulum við gera ráð fyrir því að krafturinn :math:`F(x,t)` verki
þvert á ás bitans í stefnu :math:`y`-ássins. Nú er nauðsynlegt að taka
tillit til spennunnar sem myndast í bitanum við það að hann svignar. Við
látum :math:`v(x,t)` tákna færslu punktanna á :math:`x`-ásnum frá
jafnvægisstöðu, :math:`M(x,t)` tákna beygjuvægið og :math:`S(x,t)` tákna
*skerkraftinn* í stefnu færslunnar. Skerkraftur er einnig nefndur
*skúfkraftur*. Ef við lítum á kraftjafnvægið í litlum bút á bitanum
:math:`[x,x+h]`. Þá gefur annað lögmál Newtons

.. math::

  \int_x^{x+h} 
   {\varrho}({\xi}){\partial}_t^2v({\xi},t)A({\xi})\, d{\xi} 
   =-(S(x+h)-S(x)) +\int_x^{x+h} F({\xi},t)\, d{\xi}.

Við deilum í gegnum jöfnuna með :math:`h` og látum síðan
:math:`h\to 0`, þá fáum við jöfnuna

.. math::

  {\varrho}A\dfrac{{\partial}^2v}{{\partial}t^2}=
   -\dfrac{{\partial}S}{{\partial}x}+F.

Til þess að skilja sambandið milli skerkraftsins :math:`S` og færslunnar
:math:`v` er nauðsynlegt að hafa góða innsýn í fjaðurmagnsfræði. Til
þess að gera langa sögu stutta, þá nefnum við fyrst að beygjuvægið
uppfyllir :math:`M(x,t)=E(x)I(x){\kappa}(x,t)`, þar sem :math:`E` er
Young-stuðullinn, :math:`I` er tregðuvægi og :math:`{\kappa}(x,t)` er
krappinn sem ferillinn :math:`x\mapsto v(x,t)` myndar við tímann
:math:`t`. Ef gert er ráð fyrir því að færslurnar séu smáar, þá má gefa
sér nálgunina :math:`{\kappa}(x,t)\approx {\partial}^2_xv(x,t)`. Næst er
að nefna að sambandið milli skerkraftsins og beygjuvægisins er
:math:`S(x,t)={\partial}_xM(x,t)`. Ef við notum þessar upplýsingar í
jöfnunni hér að framan, þá fáum við að færslan verður að uppfylla
hlutafleiðujöfnuna,

.. math::

  {\varrho}A\dfrac{{\partial}^2v}{{\partial}t^2}
   +\dfrac{\partial^2}{\partial x^2}\bigg(
   EI\dfrac{{\partial}^2v}{{\partial}x^2}\bigg)=F(x,t).

Í burðarþolsfræðinni er þessi jafna nefnd *bitajafna*. Í henni má gera
ráð fyrir að stærðirnar :math:`{\varrho}`, :math:`A`, :math:`E` og
:math:`I` séu föll af :math:`x`. Ef þetta eru fastar þá fáum við
sértilfellið

.. math::

  \dfrac{{\partial}^2v}{{\partial}t^2}
   +a^4\dfrac{{\partial}^4v}{{\partial}x^4}=f(x,t),

þar sem :math:`a=\root 4 \of {EI/{\varrho}A}` og
:math:`f(x,t)=F(x,t)/{\varrho}A` er ytri kraftur á massaeiningu í
bitanum.

.. end-toggle::

Sveiflur í plötum
~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Sveiflur í plötum

Annað mikilvægt viðfangsefni í burðarþolsfræði er athugun á sveiflum í
plötum. Hugsum okkur að plata afmarki svæði :math:`X` í
:math:`xy`-plani, að hún sé af þykkt :math:`h` og hafi eðlismassann
:math:`{\varrho}`. Við gerum ráð fyrir að ytri kraftur verki hornrétt á
plötuna, að :math:`F(x,y,t)` tákni kraft á flatareiningu í punkti
:math:`(x,y)` við tímann :math:`t` og að :math:`w(x,y,t)` sér færsla
efnispunkts í :math:`(x,y)` frá jafnvægisstöðu við tímann :math:`t`.

.. figure:: ./myndir/fig1214.svg
    :align: center
    :alt: Þversveiflur í plötu.

    Mynd: Þversveiflur í plötu.

Útleiðslan á hreyfijöfnu :math:`w` er svipuð og fyrir hreyfijöfnu bita, en töluvert snúnari. Niðurstaðan er að

.. math:: {\varrho}h\dfrac{{\partial}^2w}{{\partial}t^2}+D\Delta^2w=F,

þar sem :math:`D=Eh^3/12(1-{\nu}^2)`, :math:`E` er Young-stuðull,
:math:`{\nu}` er Poisson-stuðull og :math:`\Delta^2` er Laplace-virkinn
í öðru veldi

.. math::

  \Delta^2=\bigg(\dfrac{{\partial}^2}{{\partial}x^2}+
   \dfrac{{\partial}^2}{{\partial}y^2}\bigg)^2
   =\dfrac{{\partial}^4}{{\partial}x^4}
   +2\dfrac{{\partial}^4}{{\partial}x^2{\partial}y^2}
   +\dfrac{{\partial}^4}{{\partial}y^4}.

Í burðarþolsfræðinni er þessi virki nefndur *tvíþýður virki* (e.
biharmonic operator). Ef við deilum nú í gegnum jöfnuna með
:math:`{\varrho}h`, þá fáum við

.. math:: \dfrac{{\partial}^2w}{{\partial}t^2}+a^4\Delta^2w=f,

þar sem :math:`a=\root 4 \of{D/{\varrho}h}` og :math:`f=F/{\varrho}h`
er kraftur á massaeiningu.

.. end-toggle::

Rafsegulfræði – Maxwell-jöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Maxwell-jöfnurnar

Öllum raf- og segulfyrirbærum í náttúrunni, þar sem ekki þarf að taka
tillit til skammtaáfhrifa, má lýsa sem lausnum á fjórum
hlutafleiðujöfnum. Þær eru kenndar við Maxwell,

.. math::

  \nabla \cdot {\mathbf D}={\varrho}, \quad
   \nabla \times {\mathbf H}-\dfrac{{\partial}{\mathbf D}}{{\partial} t}=
   {\mathbf  J},\quad  \nabla\cdot {\mathbf B}=0, \quad
   \nabla \times {\mathbf E}+\dfrac{{\partial}{\mathbf B}}{{\partial} t}=0.

Hér er :math:`\nabla=({\partial}_x,{\partial}_y,{\partial}_z)`
stigullinn með tilliti til rúmbreytistærðanna,
:math:`\nabla\cdot={{\operatorname{div}}}` er sundurleitnivirkinn og
:math:`\nabla \times={{\operatorname{rot}}}` er rótvirkinn. Stærðirnar
:math:`\mathbf B`, :math:`\mathbf D`, :math:`\mathbf E`,
:math:`\mathbf  H` og :math:`\mathbf  J` eru þrívíð vigursvið, en
:math:`{\varrho}` er skalarsvið og þau eru öll háð staðsetningu
:math:`(x,y,z)` í rúminu og tíma :math:`t`. Stærðin :math:`\mathbf E` er
*rafsvið*, :math:`\mathbf D` er *raffærslusvið*, :math:`\mathbf B` er
*segulsvið*, :math:`\mathbf H` er *segulflæði*, :math:`\mathbf J` er
*straumþéttleiki* og :math:`{\varrho}` er *hleðsluþéttleiki*.
Stærðirnar, sem hér eru upp taldar ákvarðast ekki af Maxwell-jöfnunum
einum saman. Til viðbótar koma einnig hliðarskilyrði og svokallaðar
gerðarjöfnur sem tengja stærðirnar saman. Athugið að framsetningin á
Maxwell-jöfnunum er háð einingarkerfinu sem unnið er í. Hér eru þær
settar fram í SI-kerfinu.

.. end-toggle::

Rafstöðufræði – Laplace-jafna og Poisson-jafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Rafstöðufræði; Laplace-jafna og
Poisson-jafna

Mikilvægi Laplace-virkjans kemur skýrt fram í *rafstöðufræðinni*, þegar
gert er ráð fyrir því að sviðin í jöfnum Maxwells séu tímaóháð. Þá fáum
við

.. math::

  \nabla\cdot {\mathbf D}  = {\varrho},
   \qquad  \nabla\times {\mathbf  E}=0.

Ef svæðið, þar sem sviðin eru skilgreind, er einfaldlega samanhangandi,
þá gefur síðari jafnan okkur tilvist á *rafmætti* :math:`V` og það
uppfyllir

.. math:: {\mathbf E} =  -\nabla V.

Sambandið milli :math:`\mathbf D` og :math:`\mathbf  E` getur verið mjög
flókið og er það háð efninu sem verið er að skoða, en einfaldasta
sértilfellið er *einsátta línulegt efni*, en í því er gerðarjafnan

.. math:: {\mathbf D}= \epsilon {\mathbf  E}.

Talan :math:`\epsilon` er *rafsvörunarstuðull* efnisins. Rafmættið
:math:`V` verður því að uppfylla Poisson-jöfnuna,

.. math:: \Delta  V=\nabla^2 V=-\nabla\cdot {\mathbf  D}/\epsilon=-{\varrho}/\epsilon.

Í sértilfellinu þegar :math:`{\varrho}=0` þá nefnist jafnan
Laplace-jafna. Tvívíðu Laplace- og Poisson-jöfnurnar eru einnig
mikilvægar í rafstöðufræði, því lausnir þeirra geta lýst rafstöðumætti
þar sem sívalningssamhverfa er til staðar eða rafstöðumætti í þunnri
plötu, þar sem rafsviðið er alls staðar samsíða plötunni. Þá hugsum við
okkur að hnitakerfið sé valið þannig að skilgreining á svæðinu sé í
:math:`(x,y)`-plani og að hún sé óháð þriðja hnitinu :math:`z`.
Hleðsludreifingin er þá einungis háð :math:`(x,y)`,
:math:`{\varrho}={\varrho}(x,y)`.

.. end-toggle::

Rafsegulbylgjur – bylgjujafna í þremur rúmvíddum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Rafsegulbylgjur; þrívíða
bylgjujafnan

Nú skulum við líta aftur á Maxwell-jöfnurnar í einsátta línulegu efni,
þar sem við höfum gerðarjöfnurnar

.. math::

  {\mathbf  D}={\epsilon} {\mathbf  E}, \qquad {\mathbf  H}
   =\dfrac 1{\mu} {\mathbf  B},

:math:`{\epsilon}` táknar rafsvörunarstuðul efnisins og :math:`{\mu}`
táknar segulsvörunarstuðul þess. Þær eru

.. math::

  {\epsilon}\nabla \cdot {\mathbf E}={\varrho}, \quad
   \nabla \times {\mathbf  B}
   -{\epsilon}{\mu}\dfrac{{\partial}{\mathbf  E}}{{\partial} t}={\mu}
   {\mathbf J},\quad  \nabla\cdot {\mathbf  B}=0, \quad
   \nabla \times {\mathbf  E}+\dfrac{{\partial}{\mathbf  B}}{{\partial} t}=0.

Ef :math:`\mathbf  A` er þrívítt vigursvið, þá gildir jafnan

.. math::

  \nabla\times(\nabla\times {\mathbf  A})=\nabla(\nabla\cdot {\mathbf A})-
   \nabla^2{\mathbf  A}.

Ef við látum virkjann :math:`\nabla \times` verka á fjórðu Maxwell-jöfnuna, þá fáum við

.. math::

  \nabla\times(\nabla\times {\mathbf E})=\nabla(\nabla\cdot {\mathbf  E})-
   \nabla^2{\mathbf  E}=-\nabla \times \dfrac{{\partial}{\mathbf  B}}
   {{\partial} t},

og ef við látum :math:`{\partial}/{\partial}t` verka á aðra Maxwell-jöfnuna, þá fáum við

.. math::

  {\epsilon}{\mu}\dfrac{{\partial^2}{\mathbf  E}}{{\partial} t^2}
   +{\mu}\dfrac{{\partial} {\mathbf  J}}{{\partial} t}=
   \nabla \times \dfrac{{\partial}{\mathbf  B}}{{\partial} t}.

Nú notfærum við okkur að :math:`\nabla(\nabla\cdot {\mathbf  E})=\nabla {\varrho}/{\epsilon}` og fáum síðan með því að leggja saman tvær síðustu
jöfnurnar að

.. math::

  \dfrac{{\partial}^2{\mathbf  E}}{{\partial}t^2}-c^2\nabla^2 {\mathbf  E}=
   -\dfrac 1{{\mu}{\epsilon}^2}\nabla {\varrho}-\dfrac
   1{\epsilon}\dfrac{{\partial} {\mathbf  J}}{{\partial} t},

þar sem :math:`c=1/\sqrt{{\epsilon}{\mu}}`. Athugið að í vinstri
hliðinni stendur bylgjuvirkinn í þrívíðu rúmi
:math:`{\partial}^2/{\partial}t^2-c^2\Delta`, því
:math:`\nabla^2=\Delta`. Hann verkar á hvert hnit fyrir sig í
rafsviðinu :math:`\mathbf E`. Til þess að fá hliðstæða jöfnu fyrir
segulsviðið, þá látum við :math:`\nabla\times` verka á aðra Maxwell-jöfnuna

.. math::

  \nabla\times(\nabla\times {\mathbf  B})
   = \nabla(\nabla\cdot {\mathbf  B})- \nabla^2{\mathbf  B}
   = {\epsilon}{\mu}\nabla \times\dfrac{{\partial}{\mathbf  E}}{{\partial}t}
   +{\mu}\nabla \times {\mathbf J}.

Ef við látum :math:`{\partial}/{\partial}t` verka á fjórðu Maxwell-jöfnuna, þá fáum við

.. math::

  \dfrac{{\partial}^2{\mathbf  B}}{{\partial}t^2}=-\nabla \times
   \dfrac{{\partial}{\mathbf  E}}{{\partial}t}.

Nú notfærum við okkur að :math:`\nabla(\nabla\cdot {\mathbf B})=0`,
leggjum saman tvær síðustu jöfnur og fáum þá

.. math::

  \dfrac{{\partial}^2{\mathbf B}}{{\partial}t^2}-c^2\nabla^2 {\mathbf B}=
   \dfrac 1{\epsilon} \nabla \times{\mathbf J}.

Niðurstaða þessara útreikninga okkar er að ef :math:`u` táknar eitt af
hnitaföllum rafsegulsviðsins :math:`({\mathbf E},{\mathbf  B})` í
einsátta línulegu efni, þá uppfyllir :math:`u` þrívíðu bylgjujöfnuna

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-c^2\Delta u=
   \dfrac{\partial^2 u}{\partial t^2}-c^2\bigg(
   \dfrac{\partial^2 u}{\partial x^2}
   +\dfrac{\partial^2 u}{\partial y^2}
   +\dfrac{\partial^2 u}{\partial z^2}\bigg)=f(x,y,z,t),

þar sem fallið :math:`f` er háð hleðslu- og straumþéttleikanum í efninu
og er lesið út úr hægri hliðum jafnanna hér að framan.

.. end-toggle::

Skammtafræði –Schrödinger-jafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Schrödinger-jafna

Undirstöðujafna skammtafræðinnar er kennd við Schrödinger,

.. math::

  i\hbar \dfrac{{\partial}u}{{\partial} t}
   =-\dfrac{\hbar^2}{2m}\Delta u +V(x)u,  \qquad x=(x_1,x_2,x_3)\in {{\mathbb  R}}^3.

Lausn :math:`u` á jöfnunni, sem er stöðluð þannig að

.. math:: \iiint_{{{\mathbb  R}}^3}|u(x,t)|^2\, dV(x)=1,

er bylgjufall fyrir ögn með massa :math:`m` sem hreyfist í mætti
:math:`V`. Fastinn :math:`\hbar` er kenndur við Planck. Fallið
:math:`x\mapsto |u(x,t)|^2` er þá líkindaþéttleikafall á
:math:`{{\mathbb  R}}^3`, sem er túlkað þannig að heildi yfir rúmskika
:math:`X`,

.. math:: \iiint_X|u(x,t)|^2\, dV

eru líkindi þess að ögnin sé í skikanum :math:`X` við tímann :math:`t`.
Í tengslum við Schrödinger- jöfnuna fæst eigingildisverkefnið

.. math:: -\dfrac{\hbar^2}{2m}\Delta u +V(x)u=Eu,

en möguleg eigingildi :math:`E` eru túlkuð sem hugsanleg orkustig
agnarinnar.

.. end-toggle::

Hliðarskilyrði og vel framsett verkefni
---------------------------------------

Í síðustu grein sáum við nokkur dæmi um línulegar hlutafleiðujöfnur, sem
lýsa ástandi eðlisfræðilegra kerfa. Þær eru flestar háðar einni, tveimur
eða þremur rúmbreytistærðum og tíma. Lausnin ákvarðast ekki ótvírætt af
jöfnunni einni saman, en ef sett eru eðlileg hliðarskilyrði á lausnina,
þá fæst ótvírætt ákvörðuð lausn.

Upphafsskilyrði
~~~~~~~~~~~~~~~

Hugsum okkur að :math:`u` sé fall á menginu

.. math::

  \overline X\times \overline I=\{(x,t); x=(x_1,\dots,x_n)\in
   \overline X, t\in\overline I \},

þar sem :math:`X` er opið mengi í :math:`{{\mathbb  R}}^n`, :math:`I`
er opið bil í :math:`{{\mathbb  R}}` og :math:`\overline X` og
:math:`\overline I` tákna lokanir þeirra og að :math:`u` uppfylli
einhverja hlutafleiðujöfnu á :math:`X\times I`. Ef lausnin er tímaháð,
þá er eðlilegt að setja *upphafsskilyrði* á hana með því að tilgreina
gildi hennar og einhverra tímaafleiða hennar
:math:`{\partial}_tu, {\partial}_t^2u,\dots`, fyrir eitthvert ákveðið
gildi :math:`t_0` á tímanum :math:`t`,

.. math::

  u(x,t_0)={\varphi}_0(x), \qquad
   {\partial}_tu(x,t_0)={\varphi}_1(x), \qquad\dots, \qquad x\in X.

Ef :math:`m` er hæsta stig á afleiðu, sem fyrir kemur í jöfnunni, þá
dugir oft að tilgreina gildi á :math:`u` og tímaafleiðum
:math:`{\partial}_t^ku` af stigi :math:`k\leq m-1`.

Jaðarskilyrði
~~~~~~~~~~~~~

*Jaðarskilyrði* eru sett á lausnina með því að tilgreina gildi :math:`u`
og einhverra hlutafleiða af :math:`u` í punktum :math:`(x,t)`, þar sem
:math:`x` er á jaðrinum :math:`{\partial}X` og :math:`t` er í :math:`I`.
Skilyrði af gerðinni

.. math::

  u(x,t)=h(x,t), \qquad 
   x\in \partial X, \quad t\in  I,

þar sem :math:`h` er gefið fall á :math:`{\partial} X\times I`, nefnist
*fallsjaðarskilyrði*. Skilyrði af gerðinni

.. math::

  \dfrac{\partial u}{\partial n}(x,t)=h(x,t), \qquad 
   x\in \partial X, \quad t\in I,

nefnist *flæðisskilyrði* og skilyrði af gerðinni

.. math::

  a(x,t)\dfrac{\partial u}{\partial n}(x,t)
   +b(x,t)u(x,t)=h(x,t), \qquad 
   x\in \partial X, \quad t\in I,

nefnist *blandað jaðarskilyrði*. Nokkrar tegundir af skilyrðum, sem
sett eru á lausnir hlutafleiðujafna, bera nöfn sem vert er að leggja á
minnið:

\(i) *Cauchy-skilyrði*: Lausnin :math:`u` og einhverjar tímaafleiður
hennar :math:`\partial_tu`, :math:`\partial_t^2u`, …, eru tilgreindar
á einhverjum tíma :math:`t=t_0`. Samheiti er *upphafsskilyrði*.

\(ii) *Dirichlet-skilyrði*: Lausnin :math:`u` er tilgreind á jaðri
svæðis. Samheiti er *fallsjaðarskilyrði*.

\(iii) *Neumann-skilyrði*: Þverafleiðan :math:`\partial    u/\partial n` er tilgreind á jaðri svæðis. Samheiti er
*flæðisskilyrði*.

\(iv) *Robin-skilyrði*: Línuleg samantekt af þverafleiðu og falli,
:math:`\partial u/\partial n+au`, er tilgreind á jaðri svæðis.
Samheiti er *blandað jaðarskilyrði*.

Oft er jaðri svæðis skipt í parta og ólík skilyrði sett á lausnina á
hinum ýmsu pörtum. Til dæmis getur verið eðlilegt að hugsa sér að á
hluta jaðarsins sé sett fallsjaðarskilyrði en annars staðar
flæðisskilyrði. Jaðarskilyrðið verður þá

.. math::

  \begin{cases} \dfrac{\partial u}{\partial n}(x,t)=g(x,t), 
   &x\in A, \ t\in I,\\
   u(x,t)=h(x,t),  &x\in B, \ t\in I,\end{cases}

þar sem :math:`\partial X=A\cup B` er skipting á jaðrinum í tvö
sundurlæg mengi.

Upphafs- og jaðarskilyrði fyrir streng og himnu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Strengur og himna

Við fjölluðum um streng sem ytri kraftur
verkar á og sáum að með vissum nálgunum væri fráviki strengsins frá
jafnvægisstöðu :math:`u(x,t)` lýst með einvíðu bylgjujöfnunni

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-c^2
   \dfrac{\partial^2 u}{\partial x^2}=f(x,t), \qquad 0<x<L, \quad t>0.

Eðlilegt er að staða og hraði strengsins séu gefin á einhverju
augnabliki, segjum :math:`t=0`. Með því er sett upphafsskilyrði

.. math::

  u(x,0)={\varphi}(x), \qquad {\partial}_tu(x,0)={\psi}(x), \qquad
   0<x<L,

þar sem litið er á :math:`{\varphi}` og :math:`{\psi}` sem þekkt föll.
Ef strengurinn er festur niður í báðum endapunktum, þá fáum við
fallsjaðarskilyrðin

.. math:: u(0,t)=u(L,t)=0, \qquad t>0.

Ef við hugsum okkur að hægt sé að stjórna stöðu endapunkta strengsins,
þá fáum við hliðruð jaðarskilyrði,

.. math:: u(0,t)=g(t), \qquad u(L,t)=h(t), \qquad t>0,

þar sem :math:`g` og :math:`h` eru gefin föll af tíma. Við getum alhæft
þessi skilyrði með því að setja almenn aðskilin jaðarskilyrði,

.. math::

  {\alpha}_1u(0,t)-{\alpha}_2{\partial}_xu(0,t)=g(t), 
   \qquad
   {\beta}_1u(L,t)+{\beta}_2{\partial}_xu(L,t)=h(t).

Við fjölluðum um hreyfingu himnu, sem ytri
kraftur verkar á og sáum þar að með ákveðnum nálgunum uppfyllir færsla
:math:`u(x,y,t)` efnispunkts :math:`(x,y)` frá jafnvægisstöðu tvívíðu
bylgjujöfnuna

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-c^2\Delta u=
   \dfrac{\partial^2 u}{\partial t^2}-c^2\bigg(
   \dfrac{\partial^2 u}{\partial x^2}
   +\dfrac{\partial^2 u}{\partial y^2}\bigg)=0,  \qquad (x,y)\in X,

þar sem :math:`X` táknar svæðið í :math:`xy`-plani sem himnan afmarkar í
kyrrstöðu. Eðlileg upphafsskilyrði á lausnina eru þá

.. math::

  u(x,y,0)={\varphi}(x,y), \qquad {\partial}_tu(x,y,0)={\psi}(x,y), \qquad
   (x,y)\in X,

þar sem :math:`{\varphi}` og :math:`{\psi}` eru nú gefin föll á menginu
:math:`X`, sem lýsa stöðu og hraða himnunnar við tímann :math:`t=0`. Þar
sem himnan er fest niður á jaðrinum, þá fáum við jaðarskilyrðið

.. math:: u(x,y,t)=0, \qquad (x,y)\in {\partial} X, \qquad t>0.

.. end-toggle::

Upphafs- og jaðargildisverkefni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Varmaleiðni

Við skulum nú kynna okkur hvernig hliðarskilyrði eru sett á lausnir
varmaleiðnijöfnunnar

.. math:: \dfrac{\partial u}{\partial t}-\kappa\Delta u=f(x,y,z,t),

þar sem :math:`\Delta` stendur fyrir Laplace-virkjann í þrívíðu rúmi.
Hún lýsir hitastigi :math:`u` á einhverju svæði :math:`X` í þrívíðu
rúmi, eins og við höfum þegar séð. Þar sem aðeins fyrsta stigs
tímaafleiður koma fyrir í jöfnunni, þá er upphafsskilyrði aðeins sett á
lausnina sjálfa með því að tilgreina hitastigið :math:`u` á ákveðnum
tíma :math:`t=t_0`,

.. math:: u(x,y,z,t_0)=\varphi(x,y,z), \qquad (x,y,z)\in X,

þar sem :math:`\varphi` er eitthvert fall á :math:`X`. *Jaðarskilyrði*
er sett á lausnina í jaðarpunktum :math:`X`. Sem dæmi getum við tekið
*fallsjaðarskilyrði*, þar sem hitastigið er tilgreint á jaðrinum
:math:`\partial X` á svæðinu :math:`X`,

.. math::

  u(x,y,z,t)=h(x,y,z,t), \qquad 
   (x,y,z)\in \partial X.

*Flæðisskilyrði* tilgreinir varmaflæðið í gegnum jaðarinn,

.. math::

  -\lambda\dfrac{\partial u}{\partial n}(x,y,z,t)=h(x,y,z,t), \qquad 
   (x,y,z)\in \partial X,

þar sem :math:`\partial u/\partial n={{\langle \nabla u,\vec n\rangle}}`
táknar ytri þverafleiðuna af :math:`u` á jaðrinum. Hér táknar
:math:`\vec n(x,y,z)` ytri þvervigurinn á jaðarinn í punktinum
:math:`(x,y,z)` og :math:`{\lambda}` er varmaleiðnistuðullinn. Stundum
er gert ráð fyrir því að *kælingarlögmál Newtons* gildi, en það segir að
varmaflæðið í jaðarpunktunum sé í hlutfalli við mismuninn á hitastiginu
þar og umhverfishitastiginu,

.. math::

  -\lambda\dfrac{\partial u}{\partial n}(x,y,z,t)=k(u(x,y,z,t)-u_0), \qquad 
   (x,y,z)\in \partial X.

Hér er þá gert ráð fyrir því að :math:`X` sé heitur hlutur í köldu
umhverfi og að hitastig umhverfisins :math:`u_0` hækki nánast ekkert
þegar hluturinn kólnar.

.. end-toggle::

Vel framsett verkefni
~~~~~~~~~~~~~~~~~~~~~

Úrlausn á hlutafleiðujöfnu með hliðarskilyrðum nefnist *vel framsett
verkefni*, ef eftirfarandi þrjú skilyrði eru uppfyllt:

\(i) *Tilvist*: Til er lausn sem uppfyllir jöfnuna og öll
hliðarskilyrðin.

\(ii) *Ótvíræðni*: Aðeins ein lausn er til.

\(iii) *Stöðugleiki*: Lausnin er stöðug í þeim skilningi að
lítilsháttar frávik frá hliðarskilyrðum kemur fram í lítilsháttar
fráviki frá lausninni. Í hverju verkefni um sig þarf að skigreina
hvaða mælikvarði er lagður á frávik í hliðarskilyrðum og í lausn.

Þegar verið er að sýna fram á að ákveðið verkefni sé vel framsett, þá er
venjulega byrjað á að ganga út frá því að til sé lausn og síðan er
formúla fyrir lausnina leidd út. Þá þarf að staðfesta að sérhvert fall
sem skilgreint er með lausnarformúlunni uppfylli bæði hlutafleiðujöfnuna
og öll hliðarskilyrðin. Þá er tilvistin sönnuð.

Í næsta skrefi er gengið út frá því að verkefnið hafi tvær lausnir
:math:`u_1` og :math:`u_2` og síðan er sýnt fram á að í raun sé
:math:`u_1=u_2`. Sannanir af þessu tagi eru mjög fjölbreytilegar. Til
grundvallar eru stundum lögð varðveislulögmál, en þau geta til dæmis
sagt að ákveðin orkuheildi séu minnkandi sem föll af tíma eða breytist
ekki með tíma. Einnig getur verið að lausnir uppfylli há- og
lággildislögmál. Með þessu er ótvíræðnin sönnuð.

Í síðasta skrefinu þarf fyrst að ákveða einhvern mælikvarða á frávik. Þá
eru oft skilgreindir staðlar (norm) á línulegu fallarúmin þar sem
hliðarskilyrðin og lausnirnar eru skilgreindar. Sem dæmi um slíka staðla
getum við tekið

.. math::

  \|u\|_{\infty,X}=\max\limits_{x\in X} |u(x)|, \qquad
   \|u\|_{1,X}=\int_X|u(x)|\, dx, \qquad
   \|u\|_{2,X}=\bigg(\int_X|u(x)|^2\, dx\bigg)^\frac 12.

Frávik :math:`u_1` frá :math:`u_2`, eða öllu heldur fjarlægðin milli
:math:`u_1` og :math:`u_2`, er þá :math:`\|u_1-u_2\|`. Til þess að
útskýra þetta nánar skulum við líta á:

Stöðugleiki Dirichlet-verkefnisins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Dirichlet-verkefnið fyrir Laplace-jöfnuna

Látum :math:`X` vera takmarkað svæði í þrívíðu rúmi með sléttan jaðar
:math:`{\partial}X` og lítum á verkefnið

.. math::

  \Delta u=0 \quad \text{ á } \quad X, \qquad
   u={\varphi} \quad \text{ á } \quad {\partial} X.

Við höfum þegar séð tvenns konar eðlisfræðilega túlkun á þessu
verkefni. Lausnin :math:`u` getur verið rafstöðumætti í :math:`X` sem
gefið er á jaðrinum :math:`{\partial} X` með fallinu :math:`{\varphi}`
eða æstætt hitastig í :math:`X` sem gefið er á jaðrinum með
:math:`{\varphi}`.

Lausn á Laplace-jöfnunni þýtt fall. Einn af undirstöðueiginleikum þýðra
falla er að þau taka há- og lággildi á jaðri takmarkaðra svæða. Ef
:math:`u_1` og :math:`u_2` eru lausnir á Laplace-jöfnu með jaðargildin
:math:`{\varphi}_1` og :math:`{\varphi}_2` þá er :math:`u=u_1-u_2` lausn
á Laplace-jöfnu með jaðargildin
:math:`{\varphi}={\varphi}_1-{\varphi}_2`. Hágildislögmálið segir okkur
þá að

.. math::

  \|u_1-u_2\|_{\infty,X}=\max\limits_{x\in X} |u_1(x)-u_2(x)|\leq 
   \max\limits_{x\in {\partial} X} |{\varphi}_1(x)-{\varphi}_2(x)|
   =\|\varphi_1-\varphi_2\|_{\infty,\partial X}.

Þessi ójafna segir okkur að frávik í lausninni geti ekki verið meira en
frávikið í jaðargildunum. Þar með er lausn verkefnisins Laplace-jöfnu
stöðug.

.. end-toggle::

Flokkun á annars stigs jöfnum
-----------------------------

Flokkun á annars stigs jöfnum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eins og við höfum séð, þá eru annars stigs hlutafleiðujöfnur með
fastastuðla mjög mikilvægar í eðlisfræði. Í tveimur breytistærðum er
línuleg óhliðruð annars stigs jafna með fastastuðla af gerðinni

.. math::

  a_{11}\partial^2_{x_1}u
   +2a_{12}\partial^2_{x_1x_2}u
   +a_{22}\partial^2_{x_2}u+a_1\partial_{x_1}u+a_2\partial_{x_2}u+a_0u=0.

Skilgreining
^^^^^^^^^^^^

Hlutafleiðuvirkinn og hlutafleiðujafnan eru sögð vera
*sporger* eða *elliptísk* ef :math:`a_{12}^2<a_{11}a_{22}`, þau eru sögð
vera *breiðger* eða *hýperbólsk* ef :math:`a_{12}^2>a_{11}a_{22}`, og
þau eru sögð vera *fleygger* eða *parabólsk* ef
:math:`a_{12}^2=a_{11}a_{22}`.

--------------

Þessar nafngiftir tengjast keilusniðunum í tveimur breytistærðum. Við
lítum þannig á ferningsjöfnuna

.. math:: a_{11}{\xi}_1^2+2a_{12}{\xi}_1{\xi}_2+a_{22}{\xi}_2^2=1.

Hún skilgreinir sporbaug ef :math:`a_{12}^2<a_{11}a_{22}`, breiðboga ef
:math:`a_{12}^2>a_{11}a_{22}` og fleygboga ef
:math:`a_{12}^2=a_{11}a_{22}`. Athugið að með þessum rithætti er
Laplace-jafnan :math:`\partial^2_{x_1}u+\partial^2_{x_2}u=0` sporger,
bylgjujafnan :math:`\partial^2_{x_1}u-\partial^2_{x_2}u=0`,
(:math:`c=1`), breiðger og varmaleiðnijafnan
:math:`\partial^2_{x_1}u-\partial_{x_2}u=0`, (:math:`\kappa=1`), er
fleygger. Þegar fram í sækir munum við sjá að eiginleikar lausna þessara
þriggja jafna eru mjög ólíkir. Hins vegar eru eiginleikar hverrar um sig
einkennandi fyrir flokkinn sem hún tilheyrir. Það liggur í þeirri
staðreynd að hægt er að framkvæma línuleg hnitaskipti :math:`y=Bx`,
:math:`v(y)=u(B^{-1}y)=u(x)`, þannig að sporger jafna jafngildi

.. math::

  \partial^2_{y_1}v+\partial^2_{y_2}v
   +\alpha_1\partial_{y_1}v+\alpha_2\partial_{y_2}v+\alpha_0v=0,

breiðger jafna jafngildi

.. math::

  \partial^2_{y_1}v-\partial^2_{y_2}v
   +\alpha_1\partial_{y_1}v+\alpha_2\partial_{y_2}v+\alpha_0v=0,

og fleygger jafna jafngildi

.. math::

  \partial^2_{y_1}v
   +\alpha_1\partial_{y_1}v+\alpha_2\partial_{y_2}v+\alpha_0v=0.

Þetta má alhæfa yfir á annars stigs línulegar jöfnur með fastastuðla í
:math:`n` breytistærðum :math:`x=(x_1,\dots,x_n)`,

.. math::

  \sum_{j,k=1}^n a_{jk} \partial_{x_j}{\partial}_{x_k}u
   +\sum_{j=1}^n a_j\partial_{x_j}u+a_0u=0.

Hér táknum við stuðlafylkið við annars stigs liðina með
:math:`A=\big(a_{jk}\big)_{j,k=1}^n`. Ef við innleiðum nú línuleg
hnitaskipti :math:`y=Bx`, :math:`y_l=\sum_{j=1}^nb_{lj}x_j`, þar sem
:math:`B=\big(b_{jk}\big)_{j,k=1}^n` er :math:`n\times n` fylki og
setjum :math:`v(y)=u(B^{-1}y)=u(x)`, þá gefur keðjureglan okkur

.. math::

  \dfrac{\partial u}{\partial x_j}
   =\sum_{l=1}^n\dfrac{\partial v}{\partial y_l}
   \dfrac{\partial y_l}{\partial x_j}
   =\sum_{l=1}^nb_{lj}\dfrac{\partial v}{\partial y_l}.

Af þessari formúlu leiðir síðan að

.. math::

  \sum\limits_{j,k=1}^n a_{jk}\partial_{x_j}{\partial}_{x_k}u
   =\sum\limits_{l,m=1}^n
   \bigg(\sum\limits_{j,k=1}^n b_{lj}a_{jk}b_{mk}\bigg)
   \partial_{y_l}{\partial}_{y_m}v,

þar sem vinstri hliðin er fall af :math:`x` en hægri hliðin er fall af
:math:`y`. Nú segir rófsetningin úr línulegri algebru okkur að koma megi
sérhverju samhverfu fylki yfir á hornalínuform, :math:`A=T\Lambda T^t`,
þar sem :math:`T` er hornrétt fylki, en það þýðir að :math:`TT^t=I`, og
:math:`\Lambda={{\operatorname{diag}}}\big(\lambda_1,\dots,\lambda_n\big)`
er hornalínufylki, þar sem eigingildin talin með margfeldni standa á
hornalínunni. Ef öll eigingildin eru jákvæð og við skilgreinum :math:`B`
sem

.. math::

  B=\Lambda^{-\frac 12}T^t
   ={{\operatorname{diag}}}\big(1/\sqrt{\lambda_1},\dots,1/\sqrt{\lambda_n}\big)T^t,

þá er greinilegt að :math:`B AB^t=I`, þar sem :math:`I` táknar
:math:`n\times n` einingarfylkið. Athugið að
:math:`\sum_{j,k=1}^n b_{lj}a_{jk}b_{mk}` er stak í sæti :math:`(l,m)` í
fylkinu :math:`B AB^t` og þar með fæst með þessu vali á :math:`B` að

.. math::

  \sum\limits_{j,k=1}^n a_{jk}\partial_{x_j}{\partial}_{x_k}u
   =\sum_{l=1}^n \partial^2_{y_l}v=\Delta v.

Ef öll eigingildin eru neikvæð, þá getum við margfaldað í gegnum jöfnuna
með :math:`-1` og litið á :math:`-A` í stað :math:`A`.

Lítum nú á sértilfellið :math:`n=2` aftur. Kennijafna fylkisins
:math:`A` er

.. math::

  \left |\begin{matrix} \lambda-a_{11} & -a_{12}\\ -a_{12} & \lambda -a_{22}
   \end{matrix}\right| = \lambda^2-(a_{11}+a_{22})\lambda+a_{11}a_{22}-a_{12}^2=0,

og :math:`\lambda_1\lambda_2=a_{11}a_{22}-a_{12}^2`. Virkinn er því
sporger þá og því aðeins að bæði eigingildin hafi sama formerki, hann er
breiðger þá og því aðeins að eigingildin hafi ólík formerki og hann er
fleygger þá og því aðeins að annað eigingildið sé :math:`0`. Við getum
nú alhæft hugtökin sporger, breiðger og fleygger yfir á :math:`n`
breytistærðir.

Skilgreining
^^^^^^^^^^^^

Hlutafleiðuvirkinn og hlutafleiðujafnan

.. math::

  \sum_{j,k=1}^n a_{jk} \partial_{x_j}{\partial}_{x_k}u
   +\sum_{j=1}^n a_j\partial_{x_j}u+a_0u=0.

eru sögð vera
*sporger* ef öll eigingildi stuðlafylkisins :math:`A` eru jákvæð eða ef
þau eru öll neikvæð. Þau eru sögð vera *breiðger* ef öll eigingildin eru
frábrugðin :math:`0` og eitt þeirra hefur öfugt formerki við hin
:math:`n-1`. Þau eru sögð vera *fleygger* ef nákvæmlega eitt eigingildi er
:math:`0` og öll hin hafa sama formerki.

--------------

Við höfum séð að sporger jafna ummyndast með
hnitaskiptunum :math:`y=Bx` og :math:`v({y})=u(x)` í

.. math:: \Delta v+\sum\limits_{j=1}^n \alpha_j\partial_{y_j}v+\alpha_0v=0.

Ef við lítum á breiðgera jöfnu og númerum eigingildin þannig að
:math:`\lambda_1,\dots,\lambda_{n-1}>0` og :math:`\lambda_n<0`, þá fæst
með sama hætti og hér að framan að hún varpast í

.. math::

  \partial^2_{y_1}v+\cdots+\partial^2_{y_{n-1}}v-\partial^2_{y_n}v
   +\sum\limits_{j=1}^n \alpha_j\partial_{y_j}v+\alpha_0v=0.

Að lokum, ef við lítum á fleyggera jöfnu með
:math:`\lambda_1,\dots,\lambda_{n-1}>0` og :math:`\lambda_n=0`, þá sést
með sama hætti og hér að framan að hún varpast yfir í

.. math::

  \partial^2_{y_1}v+\cdots+\partial^2_{y_{n-1}}v
   +\sum\limits_{j=1}^n \alpha_j\partial_{y_j}v+\alpha_0v=0.

Af þessu sést að hægt er að alhæfa ýmsa eiginleika lausna á
Laplace-jöfnunni yfir á lausnir á sporgerum jöfnum, eiginleika lausna á
bylgjujöfnunni yfir á lausnir á breiðgerum jöfnum og eiginleika lausna
varmaleiðnijöfnunnar yfir á lausnir á fleyggerum jöfnum. Það er því
eðlilegt að leggja höfuðáherslu á þessar þrjár tilteknu jöfnur og
tilsvarandi virkja.

Við munum fjalla um fjölbreytileg verkefni um hlutafleiðujöfnur. Þau eru
nánast öll vel framsett og við munum einbeita okkur að því að sýna fram
á tilvist á lausnum með því að leiða út lausnarformúlur fyrir verkefnin.
Við leggjum hins vegar litla áherslu á að sýna fram á að verkefnin hafi
ótvírætt ákvarðaða lausn og að lausnin sé stöðug. Fourier-greiningin er
helsta hjálpartæki okkar við úrlausn á verkefnunum. Við byrjum á því að
líta á verkefni þar sem lausnin er skilgreind á takmörkuðu bili í einni
rúmvídd og rétthyrningum í tveimur rúmvíddum. Þá er hægt að beita
Fourier-röðum og eiginfallaröðum til þess að setja lausnirnar fram. Ef
lausnin er skilgreind á hálfás með tilliti til tíma, þá er oft hægt að
nota Laplace-ummyndun til þess að leiða út lausnarformúlur. Ef lausnin
er skilgreind á öllu rúminu, þá er oft hægt að finna lausn með því að
beita Fourier-ummyndun. Við útskýrum lausnaraðferðirnar að verulegu
leyti í reiknuðum sýnidæmum og þau eru flest upprunin úr eðlisfræði.

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

*Símajafnan*: Hugsum okkur að :math:`i(x,t)` og :math:`u(x,t)` tákni
straum og spennu í rafstreng, til dæmis símalínu, þar sem :math:`x`
táknar fjarlægð frá einhverjum viðmiðunarpunkti á strengnum og :math:`t`
táknar tíma. Út frá Maxwell-jöfnunum er leitt sambandið

.. math::

  L{\partial}_ti+Ri+{\partial}_xu=0, \qquad
   {\partial}_xi+C{\partial}_tu+Gu=0,

þar sem :math:`C` táknar rýmd strengsins á lengdareiningu, :math:`G`
táknar lekaleiðni á lengdareiningu, :math:`R` táknar viðnám á
lengdareiningu og :math:`L` táknar sjálfspan á lengdareiningu. Sýnið að
bæði :math:`u` og :math:`i` uppfylli símajöfnuna

.. math:: LC{\partial}_t^2v-{\partial}_x^2v+(RC+LG){\partial}_tv+RGv=0.

Dæmi
^^^^

Skrifið upp Laplace-virkjann í pólhnitum :math:`(x,y)=(r\cos {\theta},r\sin {\theta})` og ákvarðið síðan allar lausnir Laplace
jöfnunnar :math:`\Delta u=0` af gerðinni :math:`u(x,y)=f(r)` og allar
lausnir af gerðinni :math:`u(x,y)=g({\theta})`. (Sjá viðauka D.)

Dæmi
^^^^

Skrifið upp Laplace-virkjann í kúluhnitum :math:`(r,{\theta},\phi)`, þar
sem :math:`r` táknar lengd, :math:`{\theta}` pólhorn og :math:`\phi`
áttarhorn. Ákvarðið síðan allar lausnir Laplace-jöfnunnar
:math:`\Delta u=0` af gerðinni :math:`u(x,y,z)=f(r)` og allar lausnir af
gerðinni :math:`u(x,y,z)=g(\phi)`. (Sjá viðauka D.)

Dæmi
^^^^

Notið pólhnitaframsetningu á Laplace-virkjanum í tveimur víddum til þess
að ákvarða allar lausnir *tvíþýðu jöfnunnar* :math:`\Delta^2u=0` af
gerðinni :math:`u(x,y)=f(r)`. Leysið sams konar verkefni í þremur
víddum.

Dæmi
^^^^

*Æstæða bitajafnan*: Ef við gerum ráð fyrir því að ytri krafturinn í bitajöfnunni sé tímaóháður og að bitinn sé í
kyrrstöðu við þetta álag, þá fáum við æstæðu bitajöfnuna
:math:`EIv^{(4)}(x)=F(x)`.

\(i) Ef gert er ráð fyrir því að bæði færslan og beygjuvægið í
endapunktunum sé núll, þá fást jaðarskilyrðin

.. math:: v(0)=v(L)=v{{^{\prime\prime}}}(0)=v{{^{\prime\prime}}}(L)=0,

en þetta tilfelli er nefnt *einfaldlega undirstuddur biti*. Ákvarðið
Green-fallið fyrir jaðargildisverkefnið sem hér fæst og skrifið færsluna
:math:`v` sem

.. math:: v(x)=\int_0^L G_B(x,{\xi})F({\xi})\, d{\xi}, \qquad 0\leq x\leq L.

\(ii) Ef gert er ráð fyrir því að færslan sé núll í öðrum endapunktinum
og að bitinn sé láréttur þar, þá er sagt að bitinn sé *innspenntur* í
þeim punkti. Ef punkturinn er :math:`x=0`, þá fæst þar jaðarskilyrðið
:math:`v(0)=v{{^{\prime}}}(0)`. Ef ekki eru settar neinar skorður á
færslu og halla bitans í endapunkti, þá er hann sagður vera *frjáls* í
þeim punkti. Þá gildir sjálfkrafa að beygjuvægið og skerkrafturinn þar
eru núll. Ef punkturinn er :math:`x=L`, þá fáum við jaðarskilyrðið
:math:`v{{^{\prime\prime}}}(L)=v{{^{\prime\prime\prime}}}(L)=0`.
Ákvarðið lausnina fyrir jaðargildisverkefnið sem hér fæst með sama hætti
og í (i).

Dæmi
^^^^

*Varmajafnvægi*: Látum :math:`T` tákna hitastig í rúmskika :math:`X` og
gerum ráð fyrir að :math:`T` sé lausn á æstæðu varmaleiðnijöfnunni
:math:`-{\lambda}\Delta T=F` á :math:`X` með flæðisskilyrðinu
:math:`-{\lambda}{\partial}T/{\partial}n=g` á jaðrinum
:math:`{\partial}X`. Sýnið að þá gildi

.. math:: \iiint\limits_X F\, dV=\iint\limits_{{\partial} X}  g\, dA,

þar sem :math:`dV` er rúmmálsfrymi í :math:`{{\mathbb  R}}^3` og
:math:`dA` er flatarmálsfrymið á jaðrinum :math:`{\partial}X`. Hver er
eðlisfræðileg merking þessarar jöfnu.

Dæmi
^^^^

Kannið hvort eftirfarandi virkjar eru sporgerir, breiðgerir eða
fleyggerir og innleiðið hnitaskipti þannig að þeir verði að
Laplace-virkja, bylgjuvirkja eða varmaleiðnivirkja að viðbættum fyrsta
stigs liðum,

.. math::

  {\partial}_{x_1}{\partial}_{x_2}, \qquad
   {\partial}_{x_1}^2-2{\partial}_{x_1}{\partial}_{x_2}+{\partial}_{x_1}^2,
   \qquad
   {\partial}_{x_1}^2+{\partial}_{x_1}{\partial}_{x_2}+{\partial}_{x_1}^2.


