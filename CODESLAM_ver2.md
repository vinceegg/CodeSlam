          **PAMANTASAN NG LUNGSOD NG MAYNILA**  
(University of the City of Manila)  
**College of Information System and**   
**Technology Management**  
**Computer Science Department**

** **

Bachelor of Science in Computer Science (BSCS)

S.Y. 2024-2025

**CSC 0322 \- COMPILER DESIGN**

![][image1]

**\[CODE SLAM\]** 

**Group Leader:**  
Liwag, Justin E.

**Group Members:**  
Balaoro, Clarisse Anne D.  
Buscas, Louweesiana M.  
Carlos, Michael D.  
Carlos, Vince Anthony S.  
Tendilla, Shieryl E.  
Verdillo, Korinne L.  
Villanueva, Maisie Allena F.

**Submitted by:**  
CodeSlam

**Submitted to:**  
Prof. Leisyl M. Mahusay  
Prof. Jonathan C. Morano

# **TABLE OF CONTENTS**

[**TABLE OF CONTENTS	2**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.eq0ihiibq4hd)

[**STRUCTURE OVERVIEW	4**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.d8df4y10csjv)

[Code Structure	5](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.976rdpw6ejwy)

[**GENERAL RULES	8**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.um4wgau201j1)

[**DETAILED RULES	10**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.ipgwh5hnirtj)

[II. Data Type and Literals	10](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.fr53izqeign6)

[A. Feint Data Type	11](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.5rr87e9v9i89)

[A. Floater Data Type	11](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.dtn6wzlb9p0b)

[B. Chant Data Type	13](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.o5igcmqxos7z)

[C. Stat Data Type	14](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.g38hrvih21kl)

[III. Type Conversion	14](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.m9bv3vtz4c0)

[IV.  Type Casting	15](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.8nocs51mapre)

[A. Feint Type Casting	15](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.o2c12cz6b74g)

[B. Floater Type Casting	16](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.8zdaavvwcf07)

[C. Chant Type Casting	17](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.jt8iexx23g2q)

[D. Stat Type Casting	17](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.naylsl9ncqt4)

[V. Chant Concatenation	18](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.mvzgse68efnt)

[VI. Data Structures	18](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.k07j2ksdkr43)

[Rules for Array Declaration	21](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.idowhi9on5xz)

[VII. Variables	24](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.b0vty2osln05)

[VIII. Constants	25](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.d8ijfoxjgv18)

[IX. Operators	26](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.t7s09v7uwhkt)

[X. Operator Precedence	29](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.zcfknsh8ld34)

[XI. Expressions	30](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.mrw50qxk1y0l)

[A. Arithmetic Expressions	30](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.f1i2tjty3xm)

[B. Relational Expressions	32](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.gzcxtdmc91h)

[C. Logical Expressions	33](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.pbg46udnubvv)

[XII. Functions	35](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.hxqdxn5tqfww)

[A. Dunk Function Calls	37](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.9j9bwlf22c5k)

[B. Non-Dunk Function Calls	38](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.m11cuxbetnel)

[XIII. Statements	38](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.jmz2bytjijkh)

[A. Rebound Statements	38](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.tsqcssm0592j)

[B. Inbound and Announce Statements	39](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.vt6wp02qx2x2)

[C. Conditional Statements	41](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.uqjyytqfub4w)

[Switch-Get Statements	43](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.k8b5jz427bhq)

[Rules for Switch-Get Statements	43](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.piz0r0kcvttu)

[D. Looping Statements	44](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.nov3izqyzlza)

[1\. Forward Loop Statement	44](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.g3t9qbnjk39o)

[2\. Play Loop Statement	46](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.d9f6fuxub1qk)

[3\. Run-Play Statement	47](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.cbeo7f8a8yj9)

[4\. Timeout Statement	48](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.zhby2drs4yc)

[5\. Resume Statement	49](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.q2ycb35uixo2)

[D. Assignment Statement	50](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.r320b59y41hm)

[XIV. Comments	51](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.bm2i1nygj1p4)

[**PRE-DEFINED WORDS (RESERVED WORDS)	52**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.j7cgodke2gcx)

[Data Types	52](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.ynpfpykmsj89)

[Input and Output Statements	52](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.9dzr0hmazer0)

[Conditional Statements	52](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.rywauwflgunb)

[Looping Statements	53](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.maf2d9rg74li)

[Others	54](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.tdpqbi4a37cs)

[**RESERVED SYMBOLS	54**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.76e7zon8phsj)

[Arithmetic Operators	54](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.57yl9knnpesf)

[Assignment Operators	55](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.tiho293ibhk1)

[Relational Operators	56](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.qk9h9httj91m)

[Logical Operators	56](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.6zs6zmc0ies6)

[**REGULAR DEFINITION	57**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.7wdbkmz29dqk)

[**REGULAR EXPRESSION	60**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.ta7o6g87ftak)

[DATA TYPES	60](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.ebqot3fsw597)

[Input and Output Statements	60](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.4hj82yi0axol)

[Conditional Statements	60](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.u7z78p10318n)

[Looping Statements	60](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.9cylp2exurg3)

[Others	61](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.opgyrg9vd5jt)

[**B. Reserved Symbols	61**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.sqdlq2ncv4xg)

[Arithmetic Operators	61](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.hveiinqhx7lz)

[Assignment Operators	61](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.zh0cgplbgccp)

[Logical Operators	62](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.da7275irr6kw)

[Relational Operators	62](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.rwyf9lpw8pet)

[Others	62](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.v3sy17f60tpi)

[**C. Literals	63**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.ql3t9s98beby)

[**TRANSITION DIAGRAM	64**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.krfqy2nhtzlk)

[Reserved Words	64](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.1ixnj6fbur43)

[Reserved Symbols	66](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.hlk7vh8ee0o1)

[Identifiers	68](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.dnzgnmmm4r0c)

[**CONTEXT FREE GRAMMAR	73**](https://docs.google.com/document/d/1N0rDomy012ENgeMPfjXp_PhmtMRqqGLeqJkcSk_XOBg/edit?fbclid=IwY2xjawH9U7dleHRuA2FlbQIxMAABHTdivExXc30V_83d9Elgs6EQfIy5Nd7OsTHUFBU18qQZ8in3le3ablR-xA_aem_wOf4p9A6SHVSAF2kRx7z4g&tab=t.5nz3m8uso3sw#heading=h.tws2j09yamlj)

# **STRUCTURE OVERVIEW**

| \# Global declarations (variables, constants, etc.) \<global\_declarations\>; \<data\_type\> \<variables\> \= \<initial\_value\>; / \# Feint @intNum \= 5; \<datatype\> \<identifier\>\[\<array\_size\>\] \= \<array\_initialization\>; / \<constants\> \<data\_type\> \<variable\> \= \<initial\_value\>; \#Const Floater @pi= 3.14; \#Function Declaration \<data\_type\> \<identifier\>(\<parameters\>);  \#Function definitions \<function return\_type\> \<function\_name\>(\<parameters\>) {     \# Local declarations     \<local\_declarations\>;     \# Statements (logic, calculations, etc.)     \<statements\>;     \# Return value (if not void/Feint)     Rebound \<return\_value\>; } \# Team Function  Team() {      \# Local declarations \- arrays, variables, and constants (Orders does not matter in declarations)     \<local\_declarations\>;     \<variables\> \= \<initial\_value\>; \#Optional initialization      \# Statements (Orders does not matter in statements)     \<Assignment statements\>; / \<Inbound statements\>; / \<Announce statements\>; /     \<Conditional statements\>; / \<Loop statements\>;     \# Function Call (to other functions)       \<function\_name\>(\<arguments\>); }  |
| :---- |

##  **Code Structure**

The program begins in a set of global declarations such as variables, constants, arrays, and functions. Global declarations are followed by the function declaration and function definition. The program runs from top to bottom, starting from global declarations and ends at the Team() function. The function contains local declarations and assignments to demonstrate its logic. The global declaration can be accessed inside the function definition and team function. The system utilizes curly braces to define code blocks, and each statement must end with a semicolon (;). 

1. **Declarations**

   Declaration specifies the meaning of an identifier such as its type and properties. It is used for variables, constants, functions, and arrays.

   1. **Global Declarations**

      Global declarations are always defined at the beginning of the program and outside the functions. It can be accessed and utilized anywhere within the program. Global declarations can be a:

      1) **Variable** stores a piece of information;  
         2) **Constant** an immutable variable;  
         3) **Array** stores multiple data**;**  
      2. **Local Declarations**

      Local Declarations are always defined inside and at the beginning of a function. These declarations can only be accessed in the specific function where it is defined. If a variable is declared both globally and locally, the local declaration takes precedence.

   2. **Functions**

   Functions are a set of instructions that performs a specific task. Functions are used to group a series of commands into one unit, making it easier to reuse code and organize programs better. Functions can only be created at the global level, functions inside other functions (nested functions) are not allowed.

      1. **Team Function**

      The Team function is a predefined function that serves as the point of the program where all functions called inside are executed. The reserved word Team followed by parenthesis () is used to define the Team function and it cannot be reused inside any other function. User-defined functions can be utilized inside the Team() function.

      2. **User-defined Functions**

      User-defined functions are functions created by the programmer**.** These functions are defined using the syntax: \<data\_type\> identifier(\<parameters\>) { \<statements \>}. User-defined functions can be accessed and used within the Team function or other functions.

   3. **Assignments**  
      1. **Assignment statements** are statements that assign the data value of an identifier.  
      2. **Announce statements** (print) are statements that display any processed outputs of the program.   
      3. **Inbound statements** (input) are statements that read user inputs.  
      4. **Conditional statements** execute a block of code if the condition is met.  
      5. **Loop statements** allow repeated execution of a block of code.  
      6. **Timeout statements** (break) initiates the exit in the loop statement.  
      7. **Resume statements** (continue) initiate moving onto the next iteration of the program.  
      8. **Function calls** are statements used to call a specific function for it to be executed by the program.  
      9. **Rebound statements** (return) are statements that indicate what value the program must return.  
      10. **Variable declaration statements** are used to define the data type and name of a variable.  
      11. **Variable initialization statements** are used to initialize a variable and its value.  
   4. **Comments**

   Comments are a set of characters used in the program to enhance its readability, however, it does not have any effect in the program and it is ignored by the system. Comments can either be a single-line comment which occupies only one line or multi-line comment that occupies multiple lines.

   5. **Program Termination**

   The program runs from top to bottom, where each line is processed sequentially. The global declarations are the first one to be processed followed by the function declarations and then the function definitions up to the Team() function. The program is terminated after the last statements in the Team function. 

# 

# **GENERAL RULES**

1. Identifiers begin with an @ symbol followed by a lowercase letter and can contain any combination of lowercase and uppercase letters, digits, and the special character underscore “\_”*,* which is used for spacing.  
2. Identifiers must be between 1 to 20 characters long to ensure clarity and ease of understanding for both developers and the compiler.  
3. Identifiers are **case-sensitive**, meaning any difference in capitalization creates distinct identifiers.  
4. Global declarations for variables, constants, and arrays, regardless of order, must be made before the **Team** function and any subfunctions.  
5. Local declarations are variables defined within a function. These can only be accessed inside the function where they are declared.  
6. Always specify the data type in declarations (e.g., Feint @myNumber \= 5;).  
7. All variables must be declared before use. A declared variable that is not used will be ignored during execution.  
8. Declare only one type of variable per line (e.g., Feint @a, @b \= 10; is accepted, but not Feint @a; Chant @str \= “hello”; on the same line).  
9. Constants are immutable once defined. They are declared using the reserved word Const followed by a variable.  
10. Each data type has specific formatting rules for values:  
    1. **Floater (float)** values are floating-point numbers storing up to 13 digits and 6 decimal places, rounding any extra decimal places.  
    2. **Feint** (int) values must be whole numbers. It can store up to 13 digits.  
    3. **Chant** (string) values must be enclosed in double quotation marks (" "), representing sequences of characters. Single quotes (‘ ‘) are not accepted.  
    4. **Stat** (bool) values must be either **Win** (true) or **Loss** (false), representing boolean data.  
11. A **tilde (“\~”)** is used as a negative symbol and to negate Feint and Floater Literals.  
12. In type casting, there should be no space between the data type and parenthesis.  
13. All reserved words must start with an uppercase letter followed by lowercase letters. Ensure the correct capitalization for valid data types except for logical operators (**AND, OR, NOT**) and that must be in all uppercase letters.  
14. Reserved word **Inbound** is used for input statements, while **Announce** is used for output/print statements.  
15. Function prototype and function definition must be declared before the **Team.**  
16. The array size is static, meaning their size is fixed and cannot be changed after declaration. For clarity, the size and dimensions must match its elements  
17. Arrays follow zero-based indexing, which implies that the number 0 is used to access the array's first element, the number 1 to access its second member, and so on.  
18. The type of elements in an array is determined by its declared data type, meaning all elements must be of the same type.  
19. 2-dimensional arrays are supported in the programming language.  
20. All statements must end in a semicolon ( ; ) signaling termination and separation from other statements.  
21. Operations in expressions are performed following the PEMDAS rule: Parentheses, Exponents, Multiplication/Division (left-to-right), and Addition/Subtraction (left-to-right).  
22. Values with different data types can be directly concatenated with each other except for a value with a Stat (boolean) data type, unless it was type casted.   
23. Single-line comments start with “\#”, and multi-line comments are enclosed within matching “|\*\*|”. Therefore, any code or program written following “\#” or enclosed within matching “|\*\*|” will be considered as a comment.  
24. Escape sequences like (\\n, \\t, \\", \\&, and \\\\) are permitted within Chant literals to represent non-printable characters.  
25.  Reserved words cannot be used as identifiers. However, if a reserved word uses different letter casing and is prefixed with the “@” symbol, it can be used as an identifier.  
  


# 

# **DETAILED RULES**

1. **Identifiers**  
     
   An **identifier** is a name used to identify a variable, function or other user-defined item. Identifiers are essential because they give meaning to different elements of code, allowing programmers to reference them throughout the program.

   Rules for Creating Identifiers

1. Identifiers begin with a @ symbol followed by a lowercase letter and could include a combination of lowercase and uppercase letters, digits, and the underscore (\_) as the only special character.  
2. Identifiers must be at least 1 character long and no more than 20 characters long.  
3. Identifiers are case-sensitive, meaning small differences in capitalization create unique identifiers with different meanings within the program.  
   

| Valid Identifier | Invalid Identifier | Reason |
| :---- | :---- | :---- |
| @player | \_player, $name, \#name | Must not start with a special character except “@”. |
| @d8te | @8ate | Must not start with a number.  |
| @sHoot | @Shoot | Must not start with a capital letter. |
| @buzzer\_Beater | @Buzzer Beater | Must have no spaces between separate words. |

## **II. Data Type and Literals**

1. **Data Types** refer to the classification of data that tells the compiler or interpreter how the programmer intends to use the data. Each data type specifies the type of operations that can be performed on the data and the way the data is stored in memory  
2. A **literal** is a fixed value that appears directly in the source code of a program. These values represent data that is interpreted as-is during execution. Literals are written directly as part of the code and have a specific data type.

1. ### **Feint Data Type**

* **Feint** is used for storing integer values.

  Rules for Feint

1. **Feint** can store integer values from \-9999999999999 up to 9999999999999\.  
2. When a **Feint** starts with zero (0) followed by another number other than zero, the zero will be ignored and the preceding number is read.   
3. A tilde (\~) in front of a **Feint** is considered as the negative symbol.  
4. Negative zero is prohibited (e.g. \-0 or \-0000 is prohibited but \-0001 is allowed).  
   

| Valid Feint Literal | Invalid Feint Literal | Reason |
| :---- | :---- | :---- |
| 23 | "23" | Quotation marks ( " " ) are not an accepted **Feint** character. |
| \~30 | 30\~ | Misplaced tilde symbol ( \~ ). |
| 40474 | 40,474 | Comma ( , ) is not an accepted **Feint** character. |
| 35 | 35.5 | Period ( . ) is not an accepted **Feint** character. |
| 0 | LeBron | Letters are not an accepted **Feint** character. |

1. ### **Floater Data Type**

* **Floater (float)** is used for storing real numbers with decimal points.

  Rules for Floater

1. **Floater** can store values ranging from \-9999999999999.999999 up to 9999999999999.999999.  
2. **Floater** must include a decimal point (.) between the whole number from the fractional part (e.g., 2.3)  
3. **Floater** must be represented with a fractional part, even if it corresponds to a whole number (e.g. 3 should be 3.0).  
4. **Floater** must include a whole number before the decimal point because a number before a decimal point is expected for it to be considered as floater. (e.g., .3 is not allowed, but 0.3 is valid).  
5. If a **Floater** value exceeds 6 decimal places, it is rounded off to the nearest value. (e.g.: 6.6666666 \= 6.666667)  
6. A tilde (\~) in front of a **Floater** is considered as the negative symbol.  
   

| Valid Floater Literal | Invalid Floater Literal | Reason |
| :---- | :---- | :---- |
| 23.00 | "23.00" | Quotation Marks ( " " ) are not a valid symbol for **Floater** literals. |
| \~0.30 | 30.0\!, \#30.0, ?30.0 | Invalid use of symbols. |
| 40.474 | 40,474 | A comma is not an accepted symbol for **Floater** literals. |
| 24.0 | 240 | The Given invalid example  is classified as a **Feint** literal. |
| 2.3 | jordan | Non-numeric characters excluding tilde ( \~ ) and period ( . ) are not accepted as **Floater** literals. |

2. ### **Chant Data Type**

* **Chant** is used for storing a sequence of one or more characters that may consist of letters, numbers, or symbols.

  Rules for Chant

1. **Chant** can contain any of the ASCII characters.  
2. **Chant** accepts empty strings (for example, "").  
3. Use the (&) operator to concatenate **Chants**.  
4. Escape sequences are character sequences that represent non-printable or restricted characters. These sequences start with a backslash (\\), followed by one or more characters. The following escape sequences can be used inside a **Chant** literal:  
* \\n \- new line  
* \\t \- tab  
* \\\\ \- \\ symbol  
* \\" \- “” symbol  
* \\& \- & symbol


| Valid Chant Literal | Invalid Chant Literal | Reason |
| :---- | :---- | :---- |
| "JORDAN" | 'JORDAN' | Single quotation marks ( ' ' ) are not accepted when defining **Chant** literals. |
| "Anthony Davis" | "Nice | Unterminated **Chant**. |
| "10.5" | 10.5 | Floater literal is invalid as a **Chant**. |
| "passed" | "passed' | Unterminated **Chant**. A single quotation mark was used to terminate the **Chant**. |
| "Michael\\n Jordan" | "Michael\\z Jordan" | Invalid escape sequence. |
| "Lebron" & "James\!"  | "Lebron", "James\!"  "Lebron"&"James\!"  | Invalid use of a comma ( , ) as **Chant** operator.  |
|  "Hi, you'll be safe"  | "Hi "you'll be safe\!"  | This results in a syntax error because the codeslam compiler sees two separate **Chant** ("Hi " and "you'll be safe\!") with an incomplete statement in between. |

3. ### **Stat Data Type**

* **Stat (boolean)** is used for storing **Win (True)**  and **Loss (False)** values.

  Rules for Stat Data Type

1. **Stat** must only be **Win** or **Loss**, other word/s are prohibited.

2. When **Stat** is printed, its value will output as either "1" for Win or "0" for Loss.

	

| Valid Stat Literal | Invalid Stat Literal | Reason |
| :---- | :---- | :---- |
| Win | win | Invalid reserved word. |
| Loss | loss | Invalid reserved word. |

## **III. Type Conversion**

**Type conversion** is the process of converting a value from one data type to another. Essential for performing operations between different data types and for ensuring data compatibility.

Rules for Type Conversion

1. When an arithmetic operation involves both a **Feint** and a **Floater** number, the compiler will automatically convert the **Feint** number to a **Floater**.  
2. When **Feint** or **Floater** literals, variables, or array elements are concatenated with a **Chant**, the compiler will automatically convert them, resulting in a **Chant.**   
3. **Chant** is not accepted as an arithmetic operator.

   

| Valid Type Conversion | Invalid Type Conversion | Reason |
| :---- | :---- | :---- |
| 5  \* 10.9 | 5  \* “Ten” | **Chant** is not accepted as an arithmetic operator |
| "My age is " & 21   | "My age is " \+ Win | **Stat** literal cannot be converted to **Chant** |
| @my\_array\[2\] & “hello” | @my\_array\[\] & “hi” | Array doesn’t have an element |

## **IV.  Type Casting**

**Type casting** is the process of converting one data type into another. It is commonly used in programming to ensure that operations involving different types of data are handled correctly or to avoid errors.

| Syntax \<data\_type\>(\<value\>); where: \<data\_type\> \= Feint , Floater, Chant, Stat \<value\> \= identifier,  Feint literal, Floater literal, Chant literal, Stat literal |
| :---- |

1. ### **Feint Type Casting**

	Rules for Feint Type Casting

1. **Feint** may only be used for type casting if the **value** has a valid literal conversion to **Feint.**  
2. When a **Floater** is converted to a **Feint** using type-casting, the decimal portion of the **Floater** is discarded, and only the whole number part is retained.  No rounding is performed during this conversion.  
3. When casting **Stat** literals into **Feint**, **Win** will be converted as 1, while **Loss** will be converted as 0\.

   

| Valid Feint Type Casting | Invalid FeintType Casting | Reason |
| :---- | :---- | :---- |
| **Feint**(“23”) | **Feint**(“twentythree”) | Words have no valid literal conversion to **Feint** |
| **Feint**(2.4) | **Feint** 2.4 | Missing parentheses |
| **Feint**(Win) | **Feint**(win) | Invalid **Stat** literal |

2. ### **Floater Type Casting**

Rules for Floater Type Casting

1. **Chant** may only be used for type casting if the contained **Chant** has a valid literal conversion to **Floater**  
2. When casting **Feint** to a **Floater**, a decimal point and zero will be appended to the **Feint**, ensuring a valid **Floater** representation.  
3. When casting **Stat** literals into **Floater**, **Win** will be converted as 1.0, while **Loss** will be converted as 0.0.

   

| Valid Floater Type Casting | Invalid Floater Type Casting | Reason |
| :---- | :---- | :---- |
| **Floater**(“2.3”) | Floater(“two.three”) | Words have no valid literal conversion to Floater. |
| **Floater**(24) | Floater 24 | Missing parentheses. |
| **Floater**(Loss) | Floater(loss) | Invalid **Stat** literal. |

3. ### **Chant Type Casting**

Rules for Chant Type Casting

1. Any value can be type cast to **Chant**.

| Valid Chant Type Casting | InvalidChant Type Casting | Reason |
| :---- | :---- | :---- |
| Chant(2.3) | Chant (2.3 | Unterminated parenthesis. |
| Chant(24) | Chant 2 | Missing parentheses. |
| Chant(Win)  | chant(Win) | Invalid reserved word for **Chant**. |

4. ### **Stat Type Casting**

Rules for Stat Type Casting

1. Values containing **Feint** or **Floater** can be typecasted to **Stat.**  
2. Zero, regardless if it is a **Feint** or **Floater**, is always cast to **Loss**.  
3. Any non-zero value (whether it's a positive or negative number) when subjected to **Stat** typecasting, will be cast to **Win**.   
4. When casting **Chant** literals to **Stat**, empty **Chant** will be cast as **Loss**, while non-empty **Chant** will be **Win** regardless of the content as there is no type conversion from **Stat** to **Chant.**

| Valid Stat Type Casting | Invalid Stat Type Casting | Reason |
| :---- | :---- | :---- |
| Stat(23) | Stat(23 | Unterminated parenthesis. |
| Stat(\~23) | Stat 23 | Missing parentheses. |
| Stat(“”) | Stat (Five) | Invalid value. The given value is not a valid **Feint**, **Floater**, or **Chant** literal. |

## **V. Chant Concatenation** 

* Chant concatenation involves adding or merging two or more Chants into one.

	Rules for Chant Concatenation

1. If at least one operand is of type Chant, the “&” symbol serves as a string concatenation operator.   
2. Only **Feint** and **Floater** data types can be concatenated to **Chant**.  
3. To concatenate a **Stat** data type, type casting it either into **Feint** or **Float** is necessary to convert its value into **Chant**.  
4. The following data types can be concatenated using “&”. Two or more **Chants** can be concatenated directly.

| Syntax  \<chant\_operand\> & \<operand\> \<operand\> & \<chant\_operand\> where:  \<chant\_operand\> \= values that contain a Chant literal \<operand\> \= Chant literal, Feint literal, Floater literal, type casts |
| :---- |

## 

## **VI. Data Structures**

**Data structures** are specialized formats used to organize, manage, and store data efficiently. They provide a way to process and manipulate data depending on the task or algorithm at hand. 

1. **Array**  
   An **array** is a data structure that stores a fixed-size, ordered collection of elements, all of the same data type. Arrays allow you to store multiple values in a single variable and access each value using an index.

Rules for Array Declaration

1. An array can be declared with or without initialization.  
2. Array declarations start with a data type followed by an identifier, and the array size enclosed in square brackets \[\].  
3. The array size must always be provided, and it can only be a positive Feint literal.  
4. The minimum array size is 2 elements, and the maximum size is 999,999,999 elements.  
5. Array size is static, meaning their size is fixed and cannot be changed after declaration.   
6. Arrays should be declared with a data type, and the data type of the array should match the data typeof its elements.  
7. Stat data type is not allowed for declaring arrays.  
8. The size and dimensions of an array must match its elements.

   

| Syntax \<data\_type\> identifier\[\<array\_size\>\]; where: \<array\_size\> \= Feint literal, identifier |
| :---- |

| Valid Array Declaration | Invalid Array Declaration | Reason |
| :---- | :---- | :---- |
| Feint @my\_array\[2\]; | $my\_array\[2\]; | Array is initialized without a proper identifier. |
| Floater @my\_list\[3\]; | @my\_list\[\]; | Array is initialized without an array size. |
| Feint @size \= 3; Feint @num\[@size\]; | Feint @size \=; Feint @num{@size}; | Invalid symbol for array size |

Rules for Array Initialization

1. Array initialization starts with declaring the array and its size, followed by an equal sign (=), and then the elements enclosed in curly brackets {}, separated by commas.  
2. The minimum array size must be two.  
   

| Syntax \<data\_type\> identifier\[\<array\_size\>\] \= {\<array\_elem\>, \<array\_elem\>}; where: \<array\_size\> \= Feint literal \<array\_elem\> \= Feint literal, Floater literal, Chant literal |
| :---- |

| Valid Array Initialization | Invalid Array Initialization | Reason |
| :---- | :---- | :---- |
| Floater @my\_array\[3\] \= {2.3, 2.4, 3.0}; | Floater @my\_array\[3\] \= {2.3, 2.4}; | Mismatched dimensions: the array expects 3 elements but 2 are provided. |
| Chant @my\_list\[3\] \= {"Michael", "Jordan", "\!"}; | Floater @my\_list\[3\] \= (); | Invalid use of parentheses.   |

Rules for Array Manipulation

1. Indexing can be used to retrieve individual elements from an array by simply stating the array name and the element index contained in square brackets  "\[\]" (e.g., \<array name\>\[\<element index\>\]).  
2. Arrays employ zero-based indexing, which implies that the number 0 is used to access the array's first element, the number 1 to access its second member, and so on.   
3. Accessing an index outside the array's bounds will result in an error.  
4. To update a specific element, use its index, followed by \= and the new value.

   

   

| Syntax identifier\[\<element\_index\>\]; identifier\[\<element\_index\>\] \= \<array\_elem\>; where: \<element\_index\> \= Feint literal \<array\_elem\> \= Feint literal, Floater literal, Chant literal |
| :---- |

| Valid Array Manipulation | Invalid Array Manipulation | Reason |
| :---- | :---- | :---- |
| @my\_array\[2\] \= 0; | @my\_array\[-2\]; | Accessing array elements that do not exist. Index for array elements must only be positive numbers greater than or equal to 2\. |
| @my\_array\[2\] \= 3.0; | my\_array\[2\] \= "Three"; | Missing @ symbol: The array must start with @ to follow the naming convention. |

2. **Two-dimensional Array** 

   A 2D array is structured as a matrix, represented by rows and columns.

## Rules for Array Declaration

1.  Two-dimensional arrays are declared using a data type followed by an identifier followed by two sets of square brackets \[\]\[\], indicating the rows and columns.   
2. The array size of a two-dimensional array must always be provided.  
3. Both the number of rows and columns must be provided as positive Feint literals or identifiers that store Feint values.  
4. The minimum size for a two-dimensional array is 2x2, while the maximum size can be up to 999,999,999 x 999,999,999.  
5. Like one-dimensional arrays, two-dimensional arrays have a fixed size that cannot be changed after declaration.  
6. Stat data type is not allowed for declaring arrays.  
7. The size and dimensions of an array must match its elements. 

| Syntax \<data\_type\> identifier\[\<array\_size\>\]\[\<array\_size\>\]; where: \<array\_size\> \= Feint literal, identifier |
| :---- |

| Valid 2D Array Declaration | Invalid 2D Array Declaration | Reason |
| :---- | :---- | :---- |
| Feint @my\_array\[2\]\[3\]; | Feint $my\_array\[2\]\[3\]; | Array is declared without a proper identifier. |
| Feint @my\_list\[3\]\[2\]; | Feint @my\_list\[3\]\[\]; | Array is declared without an array size. |

Rules for Two-Dimensional Array Initialization

1. Two-dimensional arrays are initialized by specifying their size, followed by an equals sign (=) and enclosing the entire array in a set of curly braces ({}). Each row within the array is then enclosed in its own set of curly braces.  
2. The minimum array size for initialization is 1x1.  
3. The number of elements in each row must match the declared column size.  
   

| Syntax \<data\_type\> identifier\[\<array\_size\>\]\[\<array\_size\>\]= {\<array\_elem\>}; where: \<array\_size\> \= Feint literal \<array\_elem\> \= Feint literal, Floater literal, Chant literal |
| :---- |

| Valid 2D Array Initialization | Invalid 2D Array Initialization | Reason |
| :---- | :---- | :---- |
| Feint @my\_array\[2\]\[2\] \= {{1,2}, {3,4}}; | Feint @my\_array\[2\]\[2\] \= {{1,2}} | Mismatched in rows: Array expects 2 rows.  |
| Floater @my\_grid\[3\]\[2\]= {{1.5, 2.3}, {3.0, 4.1}, {5.2, 6.3}}; | Feint @my\_grid\[3\]\[2\] \= ({1, 2}, {3, 4, 5}); | Invalid use of parentheses.   |

Rules for Two-Dimensional Array Manipulation

1. Access elements using row and column indices in the format identifier\[row\]\[column\]. Both indices must be valid positive Feint literal.  
2. Arrays use zero-based indexing, meaning the first row and first column are accessed using \[0\]\[0\].  
3. Attempting to access indices outside the declared row or column size results in an error.  
4. To update a specific element, specify its indices followed by \= and the new value.

   

| Syntax identifier\[\<element\_index\>\]\[\<element\_index\>\]; identifier\[\<element\_index\>\]\[\<element\_index\>\]= \<array\_elem\>; where: \<element\_index\> \= Feint literal \<array\_elem\> \= Feint literal, Floater literal, Chant literal |
| :---- |

| Valid 2D Array Manipulation | Invalid 2D Array Manipulation | Reason |
| :---- | :---- | :---- |
| @my\_array\[1\]\[1\] \= 5; | @my\_array\[1\]\[-1\] \= 5; | Column index must be a positive integer. |
| @my\_array\[0\]\[0\] \= 3.5; | my\_array\[0\]\[0\] \= 3.5; | Missing @ symbol: The array must start with @ to follow the naming convention. |

## **VII. Variables**

A **variable** in programming is a container that holds a value or data. Variables allow you to store data in memory and manipulate it throughout the execution of a program.

Rules in Declaration and Initialization of Variables

1. Variables declared within a block or function have local scope and are only accessible within that block or function.  
2. Global variables, declared outside of any block or function, are accessible throughout the entire program.  
3. Variable names must follow the identifier naming rules.  
4. The equal sign (=) is used to assign values to variables (e.g., \<var\_Name\> \= value).  
5. Multiple variables can be declared on a single line, without assigned values. They must have the same data types and must be separated by commas.

| Syntax \<data type\> \<identifier\> \= \<value\>; Where: \<data type\> \= Feint, Floater, Chant, Stat \<value\> \= Feint literal, Floater literal, Chant literal, Stat literal |
| :---- |

	

| Valid Variable Declaration and Initialization | Invalid Variable Declaration and Initialization | Reason |
| :---- | :---- | :---- |
| Feint @my\_number \= 23;    | $my\_number \=  "Jordan"; | Incompatible variable initialization. The variable starts with “$”. |
| Floater @decimal\_num \= 2.3; | Floater @Decimal\_num; | Invalid identifier. Identifiers must start “@” and follow with a lowercase. |
| Floater @decimal\_num \= 3.0;  | Floater @decimal num \= 3.0; | Incompatible variable initialization. The variable has a whitespace which is not allowed |

## **VIII. Constants**

**Constants** are immutable once defined, their value remains constant throughout the program execution. They are declared using the reserved word Const followed by a data type and a variable. 

Rules for Constants

1. Constants are declared using the reserve Const followed by a data type  and variable. Its value must always be initialized.  
2. Constants can only be declared at a global declaration.  
3. Constants are immutable and cannot be overridden even by a local variable.  
4. The value stored by constants be of any type of literal including Feint literal, Floater literal, Chant literal, or Stat literal.

| Syntax Const \<data\_type\> identifier \= \<literal\>; Where: \<literal\> \= Feint literal, Floater literal, Chant literal, Stat literal |
| :---- |

| Valid Constant Declaration and Initialization | Invalid Constant Declaration and Initialization | Reason |
| :---- | :---- | :---- |
| Const Floater @pi \= 3.14;    | const Floater @pi \= 3.14;    | Invalid reserved word for constants. |
| Const Chant @my\_name \= “Juan”;   | Const Chant @my\_name;   | Value is not initialized. |
| Const Feint @totalStudents \=35;    | Const Feint totalStudents \=35;   | Invalid identifier. |

## 

## **IX. Operators**

**Operators** are symbols or keywords used to perform operations on operands (data or variables). They are used in expressions to manipulate values and variables to produce a result. Operators are categorized based on the types of operations they perform.

* Below are the following types of operators:  
  * Arithmetic Operators  
  * Assignment Operators  
  * Relational Operators  
  * Logical Operators  
  * Other Operators

| Symbol | Name | Description  |
| :---- | :---- | :---- |
| **Arithmetic Operators** |  |  |
| \+ | Addition  | Adds the operands from left to right |
| \- | Subtraction  | Subtract the operands from left to right |
| \* | Multiplication  | Multiplies the operands on both sides of the operator |
| / | Division  | Divides the left operand by the right operand |
| % | Modulus | Returns the remainder of the division of the left operand by the right operand |
| **Assignment Operators** |  |  |
| \= | Assignment Operator | Assigns the left operand with the value of the right operand |
| \+= | Addition Assignment Operator | Adds the right operand to the left operand and assigns the result to the left operand |
| \-= | Subtraction Assignment Operator | Subtracts the right operand from the left operand and assigns the result to the left operand |
| \*= | Multiplication Assignment Operator | Multiplies the left operand by the right operand and assigns the result to the left operand |
| /= | Division Assignment Operator | Divides the left operand by the right operand and assigns the result to the left operand |
| %= | Modulus Assignment Operator | Calculates the remainder of the division of the left operand with the right operand and assigns the result to the left operand |
| **Relational Operators** |  |  |
| \== | Is equal to  | Checks if two operands, the left and right operands, are equal |
| \!= | Not equal to | Checks if the left and right operands are not equal |
| \< | Less than | Checks if the value of the left operand is less than the value of the right operand |
| \> | Greater than | Checks if the value of the left operand is greater than the value of the right operand |
| \<= | Less than or equal to | Checks if the value of the left operand is less than or equal to the value of the right operand |
| \>= | Greater than or equal to | Checks if the value of the left operand is greater than or equal to the value of the right operand |
| **Logical Operators** |  |  |
| AND | Logical AND | Returns **Win** if the value of both operands is **TRUE** |
| OR | Logical OR | Returns **Win** if at least one operand is **TRUE** |
| NOT | Logical NOT | Returns the opposite Stat value of the operand |
| **Other Operators** |  |  |
| & | Chant Concatenation Operator | Concatenates Chant together when working with Chant data types |
| \~ | Negative Operator | Negates the numerical values, making a positive number negative and negative number positive |
| () | Grouping Operator | Used to group values or expressions  |

## **X. Operator Precedence**

| Precedence | Symbol | Description | Associativity |
| :---- | :---- | :---- | :---- |
| 1 | () | Parentheses | Left to Right |
| 2 | \* | Multiplication | Left to Right |
|  | / | Division  |  |
|  | % | Modulus |  |
| 3 | \+ | Addition  | Left to Right |
|  | \- | Subtraction |  |
|  | \~ | Negative symbol | Left to Right |
| 4 | \< | Less than | Left to Right |
|  | \<= | Less than or equal |  |
|  | \> | Greater than |  |
|  | \>= | Greater than or equal |  |
|  | \== | Is equal to |  |
|  | \!= | Not equal |  |
| 5  | NOT | Logical NOT | Left to Right |
|  | AND | Logical AND |  |
|  | OR | Logical OR |  |
| 6 | \= | Assignment | Right to Left |
|  | \*= | Multiplication Assignment |  |
|  | /= | Division Assignment |  |
|  | %= | Modulus Assignment |  |
|  | \+= | Addition Assignment |  |
|  | \-= | Subtraction Assignment |  |

## 

## **XI. Expressions**

* Combinations of operands and operators that result in a value when evaluated are called expressions.   
* Expressions are grouped together and the evaluation order is managed using parentheses ().    
* Expressions cannot make a statement by itself.  
* Variables, literals, non-**Dunk** function calls, and typecasts as well as arithmetic, logical, and relational operations that evaluate to a value can all be used as expression operands. 

1. ### **Arithmetic Expressions**

   An **arithmetic expression** is a combination of numbers, operators, and sometimes parentheses, which evaluates to a single numeric value. Arithmetic expressions are used to perform mathematical operations such as addition, subtraction, multiplication, and division.

   Rules For Arithmetic Expression

1. It must always include operands and arithmetic operators.  
2. Arithmetic operands must be numerical values.  
3. The correct operator precedence must be followed in arithmetic expressions.  
4. An arithmetic operand can be any literal, variable, function return value, or other arithmetic expression, with the explicit restriction that only the Feint and Floater data types are permitted.  
5. An arithmetic operand must be present at both the start and the end of an arithmetic expression.  
6. Type casted **Feint** and **Floater** are accepted as arithmetic operands.  
7. Every arithmetic expression within a statement must terminate with a semicolon (;).  
8. Using arrays as operands is not permitted.  
   

| Syntax \<arithmetic\_operand\> \<arithmetic\_operator\> \<arithmetic\_operand\> where: \<arithmetic\_operand\>  \= variable; \<num\_value\>;\<arithmetic\_expr\>; \<num\_typecast\> \<arithmetic\_operator\> \= \+;  \-;  \*;  /;  % |
| :---- |

| Valid Expression | Invalid Expression | Reason |
| :---- | :---- | :---- |
| 2 \+ 3.0; | 2 \++ 3;  | Invalid operator |
| @x \* 3; | @x \*/ 3; | Invalid operator |
| (3.0) \+ 4; | Chant(5) \+ 4; | Invalid operand |
| @w \- @x; | @w  @x; | No operator |
| (@w \* @x) % @y; | ((@w \* @x) \+ @y; | Unterminated parenthesis |
| (\~7 \+ 8\) \* 9;  | (7 \+ 8 \* 9; | Unterminated parenthesis |

2. ### **Relational Expressions**

* A relational expression is made up of two or more operands compared using relational operators, that gives a **Stat** result.

  Rules for Relational Expressions

1. The outcome of a relational expression must be of the Stat data type, either **Win** (*true*) or **Loss** (*false*). The result is Loss if the operands do not satisfy the relational operator's condition; otherwise, it is Win.  
2. It must consist solely of relational operators and operands of the same data type.  
3. A relational operand can be a numeric literal, variable, or arithmetic expression, but a **Stat** or **Chant** operand is only valid when using ***\==*** or **\!=** with another operand of the same type.  
4. Type casts can be used as relational operands, provided they are cast to match the data type of the other operand.  
5. Arrays cannot be used as operands.  
6. A relational expression must start with a relational operand, followed by a relational operator, and end with another relational operand.  
7. Every relational expression in a statement must terminate with a semicolon (;).

| Syntax \<relational\_operand\> \<rel\_op\> \<relational\_operand\> where: \<relational\_operand\> \= variable; \<num\_val\>; \<arithmetic\_expr\>; (\<relational\_operand\>); \<type\_casted\>; Chant literal; Stat literal; \<rel\_op\> \=  \==; \!=; \>; \<; \>=; \<= |
| :---- |

| Valid Expression | Invalid Expression | Reason |
| :---- | :---- | :---- |
| @w \< @x; | @w \<; | Not a valid relational expression. The given example ends with an operator. |
| @age1 \< @age2; | "LBJ" \< 23; | Incompatible data types |
| @num1 \<= @num2; | list1 \<\< list2; | Invalid relational operator (\<\< ) |
| "hi" \!= "Hi"; | **Win** \!= "True"; | Incompatible data types |
| **Feint**(5.0) \>= 3; | **Chant**(5) \>= 3; | Incompatible data types |
| 3 \* @x \+ 2  \>= @y; |  3 \* @x \+ 2 \= @y; | Not an expression |
| (@y \<@z) \>= @result; | (@y \<@z \>= @result; | Unterminated parenthesis |
| **Win** \== **Loss;** | **Win** \== 0; | Incompatible data type |
| **Win** \!= **Win;** | **Win** \< **Win;**  | Invalid relational operator |

### 

3. ### **Logical Expressions**

* A logical expression comprises logical operators and logical, numerical, or relational operands. It is utilized to assess conditions and generate a Stat result.

  Rules for Logical Expressions

1. The result of **Stat** data type, which can either be **Loss**(false) or **Win**(true). The expression says **Loss** if the operand's value does not meet the operator's criteria, and **Win** otherwise.  
2. It must consist exclusively of logical operators and logical operands.  
3. Logical expressions are evaluated based on operator precedence.  
4. Parentheses ( ) must be used to group expressions and manage the evaluation order when needed.  
5. A logical operand can be a **Stat** literal, a variable holding a **Stat** value, a relational expression, or another logical expression.  
   

| Syntax \<logic\_operand\> \<logic\_operator\> \<logic\_operand\> where: \<logic\_operand\> \= \<Stat\_lit\>; variable; \<relational\_expr\>; \<logical\_expr\> \<logic\_operator\> \= AND; OR; NOT |
| :---- |

| Valid Expression | Invalid Expression | Reason |
| :---- | :---- | :---- |
| **Win** AND (@y \< 10\) | @x \> 5 AND AND (@y \< 10\) | Invalid logical operator (AND AND) |
| (@a \== @b) OR **Loss** | not (@a \== @b) OR (@c \!= @d) | Invalid logical operator (NOT) |
| NOT (@x \< 0\) | NOT OR(y \== 0\) | Invalid logical operator (NOT OR) |
| ((@x \> 0\) AND (@y \< 5)) OR (@z \== 3\) | NOT (@x \> 0, @y \< 5\) | Invalid (,) symbol |
| NOT ((@a OR @b) AND (@c OR @d) OR **Win**); | (@a OR OR @b) AND (@b OR @d); |  Invalid logical operator (OR OR) |

## **XII. Functions**

* A function is a reusable block of code that performs a specific task. It takes inputs (arguments), processes them, and often returns an output. Functions help organize code, reduce redundancy, and improve readability by encapsulating logic in a defined structure.

	Rules for Team Functions

1. The reserved word Team followed by parenthesis () is used to declare the Team function.   
2. User-defined functions can be utilized inside the Team function.  
3. There can only be one **Team** function in a program. It is not permitted to define **Team** more than once in a program; doing so will cause an error.

   Rules for Creating User-Defined Functions

1. Function prototypes must be initialized before the **Team** function; initializing them afterward will cause an error.  
2. To create a function prototype, start by indicating the return value's data type, followed by the function name, a parameter list, and end with a semicolon. Always include parentheses after the function name.  
3. Function Definitions can be defined before the **Team** function. But can only be defined once.  
4. Functions that are expected to return a value must provide a return value that matches the specified data type.  
5. Enclose executable statements in curly braces ({}) for the function definition  
6. Function names must adhere to identifier naming conventions.  
7. Define parameters within the parentheses to accept input data, separating multiple parameters with commas (,).  
8. Use the **Rebound** keyword to indicate the value that the function should return.  
9. For functions that do not return a value, use the **Dunk** (void) keyword as the return type.  
10. Functions inside other functions (nested functions) are not allowed.

    **Syntax**

| Function Declaration:  |
| :---- |
| \<data\_type\> identifier(\<parameters\>); |
| Function Definition: |
| \<data\_type\> identifier(\<parameters\>) { 		\<statements\>; 		Rebound \<value\>; } |

| Valid Function  | Invalid Function  | Reason |
| :---- | :---- | :---- |
| Floater @addition(Feint @x, Floater @y) {     @result \= @x \+ @y;     Rebound @result;} | Feint @addition(@x, @y) {     @result \= @x \+ @y;} | There is no Rebound statement |
| Dunk @hello() {    Announce("Let\\’s Play\!");} | Dunk @hello() {    Announce("Let\\’s Play\!");    Rebound 1;} | There is a Rebound statement. |
| Chant @hello(){ Rebound “And One\!”; } | Chant @hello(){ @message \= 4; Rebound message; } | Function is expected to return a value of data type Chant, but received a value of Feint. |
|  Dunk @shout(Chant @taunt, Feint @number); Dunk @shout(Chant @name, Feint @jersey) {Inbound(“Today\! Meet ” & name & “ with jersey number is " & @jersey);}  Team() {        @shout(“King James\!”, 23);}  |  Dunk shout(Chant taunt, Feint number) {Inbound(“Today\! Meet ” \+ name \+ “ with jersey number is " \+ jersey;} Team() {    @shout(“Nieut Nieut\! ”, 30);}  | The function is used before it’s declared.  |

1. ### **Dunk Function Calls**

   When invoking a **Dunk** (Void) function, the return value doesn't need to be assigned or used in any expression; you can simply call it by writing its name followed by parentheses.

| Dunk @greet() {    Announce("Hello, World\!\\n"); } Team() {     @greet(); \# Void function call } |
| :---- |

2. ### **Non-Dunk Function Calls**

   In contrast, when calling a **non-Dunk** function, the return value must be utilized in an assignment or expression; failing to do so will lead to an error.

| Feint @add(Feint @a, Feint @b) {     Rebound @a \+ @b; } Team() {     Feint @sum \= @add(5, 3); \# Non-void function call, using return value    Announce("The sum is: " \+ @sum); } |
| :---- |

## 

## **XIII. Statements**

1. ### **Rebound Statements**

* **Rebound** (Return) statements are used within a function to indicate the value that should be returned when the function is called. A Rebound statement enables data to be sent back to the caller, terminating the function's execution and returning control to the calling function. Additionally, a Rebound statement cannot be left empty.

  Rules for Rebound Statements

1. Return statements have to begin with the reserved word **Rebound** and then an expression.

| Syntax	Rebound \<expression\>; / Rebound \<local\_value\>; 	Where:  	                  \<expression\> is of the same data type as the declared function’s data type                                 \<local\_value\> is a locally declared variable. |
| :---- |

| Valid Rebound Statement | Invalid Rebound Statement | Reason |
| :---- | :---- | :---- |
| Rebound @var1; | Rebound @a+@b | Unterminated statement |
| Rebound @x \+ @y; | Rebound Announce@x; | Invalid expression |

2. ### **Inbound and Announce Statements**

* A portion of the program that reads data from external sources, and displays information. It instructs the computer how to read and gather the information from an input device, and process and send the information to an output device.

* **Inbound** statements take input (e.i digits, characters, special characters, etc.) from the user.

* **Announce** statements display a specific message or any outputs processed by the program into the console or any output device.

  Rules for Inbound Statements

1. The reserved term **"Inbound"** (input) must come first in input statements. This is followed by an open parenthesis, which contains a **Chant** where the user will type an input. The input prompt cannot be closed without the user pressing enter. 

2. If a user provides an inbound with a wrong data type that does not match the expected type of the declared variable, the system will trigger an error, displaying a descriptive message to guide the user and, optionally, allow re-entry of the correct value to prevent runtime inconsistencies.

	

| Syntax | Example |
| :---- | :---- |
| Inbound(\<input\_value\>, \<identifier\>); | Inbound(”Enter ID: ”, @studentID); |

Rules for Announce Statements

1. The reserved word **Announce** (print) must come first in output statements. This is followed by an open parenthesis. Next, **Chant** parameter, variable, array element, literal, function return value, or arithmetic, relational, or logical expressions, and finally, a closing parenthesis must come last.  
2. Double quote marks ("") must separate **Announce** with Chant parameters. The **Announce** function has the capability to perform chant concatenation using the symbol “**&”**.   
3. **Announce** Chant formatting adheres to compilers own escape sequences as specified in the Chant rules.  
   

| Syntax | Example |
| :---- | :---- |
| Announce(\<value\>); | Announce(@department); |
| Announce("\<value\>"); | Announce("Hello, World\!"); |
| Announce(\<expression\>); | Announce(@x \* 2); |
| Announce(“\<value\>” & variable); | Announce(“My name is “ & @name); |
| Syntax Announce(\<value\>); |  |
| where: \<value\> \= identifier, Feint literal, Floater literal, Chant literal, Stat literal, Array element, \<expression\> \<expression\> \= \<arithmetic\_expr\>; \<relational\_expr\>; \<logical\_expr\> |  |

3. ### **Conditional Statements**

   **Conditional statements** (or control flow statements) are used to make decisions in programming. They allow the program to execute different code blocks based on whether a condition is true or false. Conditional statements help in controlling the flow of execution based on certain conditions.

   Rules for Dribble-Pass-Shoot Statements

1. **Dribble (if)** statements must start with the reserved word **Dribble**, followed by a condition in parentheses and curly braces ({}) for the executable statements.   
2. The  **Pass (else if)** must start with the reserved word **Pass**, followed by a condition in parentheses and curly braces ({}) for the executable statements.  However,  **Pass (else if)** can only be used in between **Dribble (if)** and **Shoot (else)** and can never be used as a standalone conditional statement.  
3. **Dribble (if)** statements can either be a standalone statement or be paired with an **Shoot (else)** statement. If the condition in the **Dribble (if)** statement is not met, the **Shoot (else)** statement will be executed.  
4. **Shoot (else)** statements must start with the reserved word **Shoot**, followed by a condition and curly braces ({}) for the executable statements.  
5. Both **Dribble** and **Pass** statements must include a condition.

	

| Syntax | Example |
| :---- | :---- |
| Dribble (\<condition\>) {     \<statements\> } | Dribble (@score \== 100\) {    Announce(“Perfect Score\!”); } |
| Dribble (\<condition\>) {     \<statements\> } Shoot (\<condition\>) {    \<statements\> }  | Dribble (@score \>= 70\) {    Announce("Passed\!"); } Shoot {    Announce("Failed\!"); }  Dribble (@score \>= 90\) {     Announce("A"); } Pass (@score \>= 80\) {     Announce("B"); } Pass (@score \>= 70\) {     Announce("C"); } Shoot {     Announce("F"); } |
| Dribble (\<condition\>) {    \<statements\> } Pass (\<condition\>) {    \<statements\> } Shoot {    \<statements\> }  | Dribble (@score \>= 70\) {    Announce("Passed\!"); } Shoot {    Announce("Failed\!"); }  Dribble (@score \>= 90\) {     Announce("A"); } Pass (@score \>= 80\) {     Announce("B"); } Pass (@score \>= 70\) {     Announce("C"); } Shoot {     Announce("F"); } |
| where: \<condition\> \= \<relational\_expr\>; \<logical\_expr\>; Result\_literal \<statements\> \= \<expr\_stmt\>; \<func\_call\>, \<Announce\_stmt\>; \<Inbound\_stmt\>; \<condi\_stmt\> |  |

### **Switch-Get Statements** 

* Switch-Get statements provide an alternative way to handle multiple conditional checks.

  ### Rules for Switch-Get Statements

1. The **Switch()** statement evaluates an expression.   
2. The Get keyword checks if the expression matches a specific value.  
3. The default keyword provides a code block to execute if no Get matches the expression. 

| Syntax | Example |
| :---- | :---- |
| Switch (\<identifier\>, \<feint\>, \<chant\>) {     Get  \<value\>:              \<statements\>              Timeout;      Get  \<value\>:              \<statements\>             Timeout;      Get \<value\>:            \<statements\>            Timeout;      Default:           \<statements\> } | Chant @grade; Inbound("Enter your grade", @grade); Announce("Your grade is" & @grade); Switch(@grade){       Get 'A':               Announce("Excellent");                Timeout;       Get 'B':                Announce("Very Good");                Timeout;       Get 'C':                Announce("Good");                Timeout;       Get 'D':                Announce("Fair");                Timeout;       Get 'F’:               Announce("failed");              Timeout;       Default:               Announce("Invalid Grade"); } |
| Where:\<value\> \= \<feint, chant, const\> \<statements\> \= \<expr\_stmt\>; \<func\_call\>, \<Announce\_stmt\>; \<Inbound\_stmt\>; \<condi\_stmt\> |  |

###  **D. Looping Statements**

* Looping statements allows repetitions of blocks of statements multiple times.

1. ### **Forward Loop Statement**

* Statements in a **Forward (for)** loop iterate over a list, executing a block of statements for every item in the list. 

  Rules for Forward Loop Statements

1. The reserved word **"Forward"** must always start with a loop statement. Followed by a whitespace. Then, an opening parenthesis, counter initialization, loop condition, (+=) symbol or (-=) symbol, and a closing parenthesis must come next.   
2. Counters in **Forward** loops must always be of type Feint.  
3. Two curly braces need to encapsulate loop statements.

| Syntax | Examples |
| :---- | :---- |
| Forward (counter initialization; condition; \+=/-=) {    \<stmts\>; }  | Forward ( @i \= 0; @i \<=3; @i+=1) {    Announce(“\*”);  } |
|  | Forward (@counter \= 3;  @counter \< @num3 \+ @num4; @counter \+= 1\) {     Announce((@num+3 \< @num+4) \> (@num+3 \<= @num+3));     Dribble ( @num+3 \< Chant(3.1)) {           Announce(“Hello”);           Dribble ( @num1 \< 5\) {                  Announce(“Hello world ulit”);                  Timeout;          } Pass (@num1 \+ @num2 AND @number)     } } |
|  | Feint @sum \= 0; Forward (@num \= 0; @num \< 5; @num \+= 1){      @sum \+= @num; } Announce(“The sum of numbers 1 to 5 is “ & @sum);  |
| Where: \<condition\> \= \<relational\_expr\>; \<logical\_expr\>, Stat lit \<stmts\> \= \<expre\_stmt\>; Timeout; Resume; \<func\_call\>; \<Inbound\_stmt\>; \<Announce\_stmt\>; \<condi\_stmt\> |  |

2. ### **Play Loop Statement**

* **Play (while)** loop statements execute a block of code repeatedly as long as the specified condition is true, making them especially useful when the number of iterations is not predetermined.

  Rules for Play Loop Statements

1. While loop statements must start with the reserved word **Play**, followed by a whitespace and an open parenthesis. A condition inside the parentheses and the loop statements enclosed in curly braces.   
2. To create a while loop, the following syntax must be followed:  
   	Play (\<condition\>){

   	\<stmts\>;

   }

   1. **Play** : Introduces the loop  
   2. **\<condition\>** : The condition may be a **Stat** literal, a relational expression, a logical expression, or a combination of both relational and logical expressions.  
   3. **“{“**  Marks as the start of the loop body,  
   4. **\<stmts\>** are the content of the code block executed. Valid content of \<stmts\> in Play loop are definitions and statements (output, conditional, iterative, insert, update, delete). Inbound (input) statement is not allowed inside the Play loop. However, the \<stmts\> inside the Play loop can be null.  
   5. **“}”** Marks as the end of the loop body.

| Syntax | Example |
| :---- | :---- |
| Play (\<condition\>) {     \<stmts\>; }  | Feint @count \= 1;  Play (@count \< 5\) {      Announce(@count);      @count \+= 1;} |
|  | Feint @x \= 0; Play (@x \< 5\) {     Announce("Iteration " & @x);     @x \+= 1;  \# Increment @x to eventually end the loop }  |
|  | Feint @num \= 0; Play (@num \!= 10){    Dribble(@num % 2 \== 0){     Announce(@num & “is even.”);    }         @num \+=1;} |
| where: \<condition\> \= \<relational\_expr\>; \<logical\_expr\>, Stat lit \<stmts\> \= \<expr\_stmt\>; Timeout; Resume; \<Inbound\_stmt\>; \<Announce\_stmt\>; \<condi\_stmt\> |  |

### 

3. ### **Run-Play Statement**

* The **Run-Play** is  a loop statement used to repeat some part of the code till the given condition is fulfilled.

  Rules for Run-Play Statements 

1. A **Run-Play**  loop starts with the keyword **Run** followed by a block of code enclosed in {}.  
2. The block of code must be followed by the keyword **Play** and a condition enclosed in parentheses ().  
3. The statement ends with a semicolon ;

| Syntax | Example |
| :---- | :---- |
| Run {     \<stmts\>; } Play (\<condition\>);  | Run { Announce (@count); @count \+= 1; } Play (@count \< 5);  |

4. ### **Timeout Statement**

* The **Timeout (break)** statement is used to exit a loop when a certain condition is satisfied.

  Rules for Timeout Statements

  1. The **Timeout** statement must not be used outside of loop constructs.  
  2. The **Timeout** statement immediately exits the loop, regardless of the loop’s iteration conditions.

| Syntax | Example |
| :---- | :---- |
| \<Forward statement\> {     \<Dribble statements\> {         Timeout;     }      \<Announce Statement\>;  } | Forward (@i \= 0; @i \<10; @i+=1){       Dribble (@i \== 5\) {              Timeout; \#exit the loop when i equals 5      }     Announce( @i ); } |

5. ### **Resume Statement**

* When a condition is met, the **Resume (continue)** statement is used to move on to the next iteration and skip the remaining code inside the loop for the current iteration.

  Rules for Resume Statements

1. **Resume** statements must only be utilized inside of loops. It is not allowed to utilize the **Resume** statement outside of loop constructs.  
2. The **Resume** statement skips the current iteration of the loop and proceeds to the next iteration.   
3. There should be no whitespace between the reserved word **Resume** and the semicolon.

| Syntax | Example |
| :---- | :---- |
| \<Forward statement\>{     \<Dribble statements\> {         Resume;     }     \<Announce Statement\>;  }  | Forward ( @i \= 0; @i \<=3; @i+=1) {        Dribble (@i \== 3\) {             Resume;         }         Announce(“\*”); \#skip the following code (Announce) when i equals 3 and moves to the next iteration of the loop } |
|  |  Forward (@num \= 1; @num \< 10; @num \+= 1){      Dribble(@num % 2 \!= 0){      Announce(@num & “is an odd number”);     } Shoot {           Resume;  \#skips the even numbers.     } } |

4. ### **Assignment Statement**

* The **Assignment** statements are used to assign new values to existing variables and perform operations simultaneously.

Rules for Assignment Statement

1. Identifier: The name of the variable to which the value is assigned.  
   2. Assignment Operators: \=, \+=, \-=, \*=, /=, %=  
   3. The assignment statement applies the value on the right side of the expression to the variable on the left side.  
   4. Value/Expression: The value or result of an operation on the right-hand side of the assignment.

| Syntax              \<data\_type\> \<identifier\> \<assign\_op\> \<value\>; |
| :---- |
| where:             \<data\_type\> \= Feint, Floater, Chant, Stat            \<assign\_op\> \= \=, \+=, \-=, \*=, /=, %=            \<value\> \= Variable, Feint literal, Floater literal, Chant literal, Stat literal, \<expression\> |

| Valid Assignment Statement | Invalid Assignment Statement | Reason |
| :---- | :---- | :---- |
| Feint @num \= 23; | Feint @Num \= 23; | The variable starts with “@” and is followed by a capital letter. |
| Floater @average \= (@grades \* @units) /@ total\_units; | Floater @average \= (@grades \* @units) /@ total\_units | Unterminated statement  |
| Feint @num \+= 23; | Feint @num \=+ 23; | Invalid assignment operator |
| Chant @myPlayer \= “Jordan”; | Floater @total \==- 27.5; | Invalid assignment operator |
| Chant @letter \= “M”; | Floater @length \= 6.5s; | Floating-point value cannot be assigned to a variable with a “s” in the end. |

## **XIV. Comments**

* Comments provide explanations, descriptions, or notes within the source code. They are ignored by the compiler or interpreter and are not executed, serving as documentation to enhance code readability.

  Rules in Writing Single-line Comments


1. Single-line comments, created using the Pound Symbol (\#) followed by the comment text.  
2. Once the \# symbol is encountered on a line, the subsequent characters will be ignored by the program. Single-line comment will end after a newline.   
3. Single-line comments can be positioned either at the end of a line of code or on a dedicated line by themselves.  
4. Comments should not be placed inside function parameters or within any uncompleted statements.

   Rules in Writing Multi-line Comments

1. Multi-line comments in CodeSlam are created using a vertical bar |\* at the start, followed by the comment, and another vertical bar to close it \*|  
2. If the |\*\*| appears within the multi-line comment, the program will treat it as the conclusion of multi-line comments.

| Syntax | Example |
| :---- | :---- |
| |\*  comment \*| | |\* This is a multi \-line comment. \*| |
| \# comment | \# This is a single-line comment. |

# **PRE-DEFINED WORDS (RESERVED WORDS)**

| RESERVED WORDS | PYTHON OR C COUNTERPART | DESCRIPTION |
| :---- | :---- | :---- |
| **Data Types** |  |  |
| Feint | int | Data type for whole numbers |
| Chant | str | Data type for a sequence of one or more characters that may consist of letters, numbers, or symbols. |
| Floater | float | Data type representing whole numbers and a decimal. |
| Stat | bool | Data type that holds the values for either Win or Loss. |
| **Input and Output Statements** |  |  |
| Inbound | input | Reads and stores data. |
| Announce | print | Displays data as formatted. |
| **Conditional Statements** |  |  |
| Dribble | if | Discerns whether a condition is True or False. If the evaluation holds true, it executes the statements within its body. Otherwise, it does not execute the statements within its body. |
| Shoot | else | Extension of an “if” statement. Provides the default statements to execute if all conditions are evaluated as False. |
| Pass | elif | Extension of an “if” statement. Offers an alternate condition, which can be determined to be True or False. If the evaluation holds true, it executes the statements within its body. Otherwise, it does not execute the statements within its body. |
| Switch | switch | Instead of writing many Dribble..Shoot statements, you can use the Switch statement. |
| Get | case | Each value is called a case, and the variable being switched on is checked for each switch case. |
| Default | default | The default reserved word specifies the default block of code in a switch statement, which is the code to run if there is no case match in the switch. |
| **Looping Statements** |  |  |
| Forward | for | Iterates the statements within its body for a specified amount of times. |
| Play | while | Executes the statements within its body repeatedly while the condition is True. |
| Run | do | Indicates the start of a loop body that will execute at least once, regardless of the condition. |
| Run-Play | do/while | This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true. |
| Timeout | break | Terminates the loop once a specified condition is met. |
| Resume | continue | A loop control statement that triggers the program to skip to the next iteration of a loop when executed. |
| **Others** |  |  |
| Rebound | return | Used for exiting a function and returns a value to the caller if prompted. |
| Win | true | Stat value returned when an expression is evaluated as correct. |
| Loss | false | Stat value returned when an expression is evaluated as incorrect. |
| Team | Main | Refers to the function that serves as the entry point for program execution. |
| Dunk | void | Refers to functions that don't return any value. |

# 

# **RESERVED SYMBOLS**

| RESERVED SYMBOLS | DESCRIPTION |
| :---- | :---- |
| **Arithmetic Operators** |  |
| **\+** | Addition: Adds values together. |
| **\-** | Subtraction: Finds the difference between values. |
| **\*** | Multiplication: Multiplies values by another. |
| **/** | Division: Divides values by another. |
| **%** | Modulus: Finds the remainder after division. |
| **Assignment Operators** |  |
| **\=** | Assignment: Assigns a value to a variable. |
| **\+=** | Add and Assign: Adds and assigns the result to a variable. |
| **\-=** | Subtract and Assign: Subtracts and assigns the result to a variable. |
| **\*=** | Multiply and Assign: Multiplies and assigns the result to a variable. |
| **/=** | Divide and Assign: Divides and assigns the result to a variable. |
| **%=** | Modulus and Assign: Finds modulus and assigns the result to a variable. |
| **Relational Operators** |  |
| **\==** | Equal to: Checks if two values are equal. |
| **\!=** | Not equal to: Checks if two values are not equal. |
| **\< ** | Less than: Checks if one value is smaller than another. |
| **\> ** | Greater than: Checks if one value is larger than another. |
| **\<=** | Less than or equal to: Checks if one value is smaller or equal to another. |
| **\>=** | Greater than or equal to: Checks if one value is larger or equal to another. |
| **Logical Operators** |  |
| **AND** | Logical AND: Returns True if the value of both operands are True. |
| **OR** | Logical OR: Returns true if at least one operand is True. |
| **NOT** | Logical NOT: Returns the opposite Boolean value of the operand. |
| **Other Operators** |  |
| **&** | Chant Concatenation: Used for concatenation when working with Chant data types |
| **\[\]** | Array Size/Index: Used to specify the size or index of an array. |
| **{}** | Code Blocks: Used to define the start and end points of a programming structure (i.e. functions, loops, conditional statements or array initialization). |
| **()** | Grouping: Used to group values or expressions  |
| **\~** | Negative: Negates the numerical values, making a positive number negative and negative number positive |
| **@** | “@” sign is used to write or make a variable initialization. Every identifier must strictly start with an “@” sign. |

# **REGULAR DEFINITION**

| NAME | DEFINITION |
| :---- | :---- |
| **zero** | 0 |
| **digit** | 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| **num** | \<zero\>, \<digit\> |
| **lowercase** | a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z |
| **uppercase** | A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z |
| **alpha** | \<lowercase\>, \<uppercase\> |
| **alphanum** | \<alpha\>, \<num\> |
| **Stat** | Win, Loss |
| **arithmetic\_op** | \+, \-, \*, /, % |
| **assign\_op** | \+, \+=, \-=, \*=, /=, %= |
| **relational\_op** | \==, \!=, \<, \>, \<=, \>= |
| **logical\_op** | AND, OR, NOT |
| **other\_op** | &, \[\], {}, (), \~, @ |
| **ascii** | space, \!, ", \#, $, %, &, ', (, ), \*, \+, ,, \-, ., /, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, :, ;, \<, \=, \>, ?, @, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, \[, \\, \], ^, \_, \`, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, {, |, }, \~ |
| **new\_line** | \\n |
| **tab** | \\t |
| **space** | ˽ |
| **whitespace** | \<new\_line\>, \<tab\>, \<space\> |
| **delim1** | \<whitespace\>, (  |
| **delim2** | \<whitespace\>, { |
| **delim3** | ; |
| **delim4** | \<whitespace\>, \<num\>, (, @  |
| **delim5** | \<whitespace\>, \<alphanum\>, “ |
| **delim6** | \<whitespace\> |
| **delim8** | : |
| **asval\_delim** | \<whitespace\>, (, @, \<num\> |
| **chant\_delim** | \<whitespace\>, comma, ;, ), } |
| **equal\_delim** | \<whitespace\>, \<num\>, @, “,( |
| **stat\_delim** | \<whitespace\>, ;, ) |
| **idt\_delim** | \<white space\>, comma, \[, (, \], ;, ) |
| **num\_delim** | \<whitespace\>, \+, \-, \*, /, %, \<, ;, space comma, ), \], \=, \!, (, }, : |
| **other1\_delim**  | \<whitespace\>, num, @ |
| **other2\_delim** | \<whitespace\>, \=, ; |
| **other3\_delim** | \<whitespace\>, ;, alphanum, }, comma |
| **other4\_delim** | \<whitespace\>, @, ”, num |
| **other5\_delim** | ;, ), {, } |

Legend  
\* \- null or many  
λ \- null/none  
\+ \- one or many

# **REGULAR EXPRESSION**

1. **Reserved Words**

| Reserved Words | Regular Expression | Token |
| :---- | :---- | :---- |
| **DATA TYPES** |  |  |
| Feint | (F)(e)(i)(n)(t) | Feint |
| Chant | (C)(h)(a)(n)(t) | Chant |
| Floater | (F)(l)(o)(a)(t)(e)(r) | Floater |
| Stat | (S)(t)(a)(t) | Stat |
| **Input and Output Statements** |  |  |
| Inbound | (I)(n)(b)(o)(u)(n)(d) | Inbound |
| Announce | (A)(n)(n)(o)(u)(n)(c)(e) | Announce |
| **Conditional Statements** |  |  |
| Dribble | (D)(r)(i)(b)(b)(l)(e) | Dribble |
| Get | (G)(e)(t) | Get |
| Shoot | (S)(h)(o)(o)(t) | Shoot |
| Switch | (S)(w)(i)(t)(c)(h) | Switch |
| Pass | (P)(a)(s)(s) | Pass |
| **Looping Statements** |  |  |
| Forward | (F)(o)(r)(w)(a)(r)(d) | Forward |
| Play | (P)(l)(a)(y) | Play |
| Timeout | (T)(i)(m)(e)(o)(u)(t) | Timeout |
| Resume | (R)(e)(s)(u)(m)(e) | Resume |
| Run  | (R)(u)(n) | Run |
| **Others** |  |  |
| Default | (D)(e)(f)(a)(u)(l)(t) | Default |
| Rebound | (R)(e)(b)(o)(u)(n)(d) | Rebound |
| Win | (W)(i)(n) | Win |
| Loss | (L)(o)(s)(s) | Loss |
| Team | (T)(e)(a)(m) | Team |
| Dunk | (D)(u)(n)(k) | Dunk |

2. # **Reserved Symbols**

   

| Reserved Symbols | Regular Expression | Token |
| :---- | :---- | :---- |
| **Arithmetic Operators** |  |  |
| \+ | (+) | \+ |
| \- | (-) | \- |
| \* | (\*) | \* |
| / | (/) | / |
| % | (%) | % |
| **Assignment Operators** |  |  |
| \= | (=) | \= |
| \+= | (+)(=) | \+= |
| \-= | (-)(=) | \-= |
| \*= | (\*)(=) | \*= |
| /= | (/)(=) | /= |
| %= | (%)(=) | %= |
| **Logical Operators** |  |  |
| AND | (A)(N)(D) | AND |
| OR | (O)(R) | OR |
| NOT | (N)(O)(T) | NOT |
| **Relational Operators** |  |  |
| \== | (=)(=) | \== |
| \!= | (\!)(=) | \!= |
| \< | (\<) | \< |
| \> | (\>) | \> |
| \<= | (\<)(=) | \<= |
| \>= | (\>)(=) | \>= |
| **Others** |  |  |
| & | (&) | & |
| \[\] | (\[)(\]) | \[\] |
| {} | ({)(}) | {} |
| () | (()()) | () |
| \~ | (\~) | \~ |
| @ | (@) | @ |

3. # **Literals**

   

| Literals | Regular Expression | Token |
| :---- | :---- | :---- |
| identifier | (@)(lowercaps)(alphanum/\_/λ)18 | identifier |
| Feint Literal | (\~/λ)(num)(num/λ)12 | FeintLiteral |
| Floater Literal | (\~/λ)(num)(num/λ)12(.)(num)(num/λ)5 | FloaterLiteral |

4. **Others**  
   

| Literals | Regular Expression | Token |
| :---- | :---- | :---- |
| Single line comment | (\#)(ascii)\+(new\_line) | SingleCom |
| Multi-line comment | (|)(\*)(ascii)\+(new\_line)\*(\*)(|) | MultiCom |

Legend  
\* \- null or many  
λ \- null/none  
\+ \- one or many

# **TRANSITION DIAGRAM**

## **Reserved Words**

![][image2]

![][image3]

## **Reserved Symbols**

![][image4]

## **![][image5]**

## 

## 

## **Identifiers**

![][image6]

![][image7]

**Numeric Literals (Positive/Negative Feint)**

**![][image8]**

**Floater Literals (Positive/Negative)**

**![][image9]**  
**Comments and Chant**

# 

![][image10]

# 

# **CONTEXT FREE GRAMMAR** 

# 

| 1 | \<program\> | → | \<global\_decl\> \<function\_dec\> \<functions\> Team() { \<local\_decl\> \<team\_statements\> }  |
| :---- | :---- | :---- | :---- |
| 2 | \<global\_decl\> | → | \<global\_declared\> \<global\_decl\> |
| 3 | \<global\_decl\> | → | λ |
| 4 | \<global\_declared\> | → | \<variable\_dec\> |
| 5 | \<global\_declared\> | → | \<array\_dec\>  |
| 6 | \<global\_declared\> | → | \<constant\_dec\> |
| 7 | \<function\_dec\> | → | \<function\_decls\> \<function\_dec\> |
| 8 | \<function\_dec\> | → | λ |
| 9 | \<functions\> | → | \<function\_definition\> \<functions\> |
| 10 | \<functions\> | → | λ |
| 11 | \<variable\_dec\> | → | \<variable\_decls\> |
| 12 | \<variable\_decls\> | → | \<data\_type\> identifier \<initialize\_end\> \<decls\_end\>; |
|  |  |  |  |
| 13 | \<decls\_end\> | → | , identifier \<initialize\_end\> \<decls\_end\> |
| 14 | \<decls\_end\> | → | λ |
| 15 | \<data\_type\> | → | Feint |
| 16 | \<data\_type\> | → | Floater |
| 17 | \<data\_type\> | → | Chant |
| 18 | \<data\_type\> | → | Stat |
| 19 | \<initialize\_end\> | → | \= \<global\_value\> \<decls\_end\> |
| 20 | \<initialize\_end\> | → | λ |
| 21 | \<array\_dec\> | → | \<data\_type\> \<array\_decls\> |
| 22 | \<array\_decls\> | → | identifier\[\<array\_size\>\] \<2d\> \<array\_initialization\>; |
| 23 | \<2d\> | → | λ |
| 24 | \<2d\> | → | \[\<array\_size\>\] |
| 25 |  \<array\_initialization\> | → | \= { \<row\> \<rows\> } |
| 26 |  \<array\_initialization\> | → | λ |
| 27 | \<row\> | → | {\<array\_elem\> \<elements\> } |
| 28 | \<rows\>  | → | , {\<array\_elem\> \<elements\> } |
| 29 | \<rows\>  | → | λ |
| 30 |   \<element\_index\> | → |  Feint literal |
| 31 | \<array\_size\> | → |  Feint literal |
| 32 | \<array\_elem\> | → | Feint literal |
| 33 | \<array\_elem\> | → | Floater literal |
| 34 | \<array\_elem\> | → | Chant literal |
| 35 | \<elements\> | → | , \<array\_elem\>\<elements\> |
| 36 | \<elements\> | → | λ |
| 37 | \<constant\_dec\> | → | Const \<data\_type\> identifier \= \<literal\>; |
| 38 | \<function\_decls\> | → | \<data\_type\> identifier(\<parameters\>) \<function\_definition\>; |
| 39 | \<parameters\> | → | \<parameter\>\<parameters\_end\> |
| 40 | \<parameters\> | → | λ |
| 41 | \<parameter\> | → | \<data\_type\> identifier |
| 42 | \<parameters\_end\> | → | , \<parameters\> |
| 43 | \<parameters\_end\> | → | λ |
| 44 | \<function\_definition\> | → |  λ |
|  | \<function\_definition\> | → | {\<team\_statements\> \<rebound\_statements\>} |
| 45 | \<function\_definition\> | → | Dunk identifier(\<parameters\>){\<team\_statements\>} |
| 46 | \<local\_decl\> | → | \<local\_declared\> \<local\_decl\> |
| 47 | \<local\_decl\> | → | λ |
| 48 | \<local\_declared\> | → | \<variable\_dec\> |
| 49 | \<local\_declared\> | → | \<array\_dec\> |
| 50 | \<rebound\_statements\> | → | Rebound \<local\_value\>; |
| 51 | \<rebound\_statements\> | → | λ |
| 52 | \<team\_statements\> | → | \<statement\> \<next\_statements\> |
| 53 | \<team\_statements\> | → | \<dribble\_statements\> \<next\_statements\> |
|  | \<team\_statements\> | → |   \<array\_dec\>\<next\_statements\> |
| 54 | \<next\_statements\> | → | \<team\_statements\> \<next\_statements\> |
| 55 | \<next\_statements\> | → | λ |
| 56 | \<statement\> | → | \<announce\_statement\> |
| 57 | \<statement\> | → | \<inbound\_statement\> |
| 58 | \<statement\> | → | \<forward\_statement\> |
| 59 | \<statement\> | → | \<play\_statement\> |
| 60 | \<statement\> | → | \<run\_play\_statement\> |
| 61 | \<statement\> | → | \<variable\_dec\> |
| 62 | \<statement\> | → | \<array\_dec\> |
|  |  |  |  |
| 63 | \<statement\> | → | \<assignment\_statement\> |
| 64 | \<statement\> | → | \<switch\_statement\> |
| 65 | \<statement\> | → | \<array\_manipulation\> |
| 66 |  \<array\_manipulation\>  | → | identifier\[\<element\_index\>\] \<2d\_manipulation\> \<array\_man\>; |
| 67 | \<2d\_manipulation\> | → | \[\<element\_index\>\] |
| 68 | \<2d\_manipulation\> | → | λ |
| 69 | \<array\_man\> | → | \= \<array\_elem\> |
| 70 | \<array\_man\> | → | λ |
| 71 | \<switch\_statement\> | → | Switch (\<switch\_exp\>) {\<case\_list\> \<default\_case\>} |
| 72 | \<switch\_exp\> | → | identifier |
| 73 | \<switch\_exp\> | → | Feint literal |
| 74 | \<switch\_exp\> | → | Chant literal |
| 75 | \<case\_list\> | → | \<case\> \<case\_list\> |
| 76 | \<case\> | → | Get \<switch\_value\>: |
| 77 | \<switch\_value\> | → | ‘arith\_op’ |
| 78 | \<switch\_value\> | → | ‘alphabet’ |
| 79 | \<switch\_value\> | → | Feint literal |
| 80 | \<switch\_value\> | → | Floater literal |
| 81 | \<default\_case\> | → | Default: \<Announce\> |
| 82 | \<assignment\_statement\> | → | \<data\_type\> identifier \<assign\_op\> \<local\_value\>; |
| 83 | \<inbound\_statement\> | → | Inbound(\<input\> \<inputs\>); |
| 84 | \<input\> | → | Chant literal  |
| 85 | \<inputs\> | → | , identifier |
| 86 | \<announce\_statement\> | → | Announce(\<outputs\>); |
| 87 | \<outputs\> | → | \<output\>\<output\_end\> |
| 88 | \<output\_end\> | → | & \<outputs\> |
| 89 | \<output\_end\> | → | λ |
| 90 | \<output\> | → |  \<global\_value\> |
| 91 | \<output\> | → |  \<local\_value\> |
| 92 | \<output\> | → | \<chant\_concat\> |
| 93 | \<global\_value\> | → | identifier |
| 94 | \<global\_value\> | → | \<literal\> |
| 95 | \<global\_value\> | → | \<expression\> |
| 96 | \<local\_value\> | → | Identifier \<arr\_identifier\> |
| 97 |  |  |  |
| 98 |  |  |  |
| 99 | \<arr\_identifier\> | → | \[\<element\_index\>\] |
|  | \<arr\_identifier\> |  | λ |
| 100 | \<local\_value\> | → | \<expression\> |
| 101 | \<local\_value\> | → | \<func\_call\> |
| 102 | \<local\_value\> | → | \<type\_casted\> |
| 103 | \<local\_value\> | → | \<escape\_sequence\> |
| 104 | \<escape\_sequence\> | → | \\\<esc\_charac\> |
| 105 | \<esc\_charac\> | → | n |
| 106 | \<esc\_charac\> | → | t |
| 107 | \<esc\_charac\> | → | \\ |
| 108 | \<esc\_charac\> | → | " |
| 109 | \<esc\_charac\> | → | @ |
| 110 | \<esc\_charac\> | → | & |
| 111 | \<literal\> | → | Feint literal |
| 112 | \<literal\> | → | Floater literal |
| 113 | \<literal\> | → | Chant literal |
| 114 | \<literal\> | → | Stat literal |
| 115 | \<type\_casted\> | → | \<data\_type\> (\<type\_cast1\>) |
| 116 | \<type\_cast1\> | → | \<literal\> |
| 117 | \<type\_cast1\> | → | identifier |
| 118 | \<assign\_op\> | → | \= |
| 119 | \<assign\_op\> | → | \+= |
| 120 | \<assign\_op\> | → | \-= |
| 121 | \<assign\_op\> | → | \*= |
| 122 | \<assign\_op\> | → | %= |
| 123 | \<assign\_op\> | → | /= |
| 124 | \<arith\_op\> | → | \+ |
| 125 | \<arith\_op\> | → | \- |
| 126 | \<arith\_op\> | → | \* |
| 127 | \<arith\_op\> | → | / |
| 128 | \<arith\_op\> | → | % |
| 129 | \<rel\_op\> | → | \< |
| 130 | \<rel\_op\> | → | \> |
| 131 | \<rel\_op\> | → | \<= |
| 132 | \<rel\_op\> | → | \>= |
| 133 | \<rel\_op\> | → | \<relation\_equality\> |
| 134 | \<relation\_equality\> | → | \== |
| 135 | \<relation\_equality\> | → | \!= |
| 136 | \<log\_op\> | → | AND |
| 137 | \<log\_op\> | → | OR |
| 138 | \<log\_op\> | → | NOT |
| 139 | \<expression\> | → | \<arithmetic\_expr\> |
| 140 | \<expression\> | → | \<relational\_expr\> |
| 141 | \<expression\> | → | \<logical\_expr\> |
| 142 | \<arithmetic\_expr\> | → | \<term\> \<arithexpr\_end\> |
| 143 | \<arithexpr\_end\> | → | \<arith\_op\> \<term\> \<arithexpr\_end\> |
| 144 | \<arithexpr\_end\> | → | λ |
| 145 | \<term\> | → | identifier |
| 146 | \<term\> | → | \<num\_literal\> |
| 147 | \<term\> | → | \<num\_type\_casted\> |
| 148 | \<term\> | → | ( \<arithmetic\_expr\> )  |
| 149 | \<num\_literal\> | → | Feint literal |
| 150 | \<num\_literal\> | → | Floater literal |
| 151 | \<relational\_expr\> | → | \<rel\_operand\> \<rel\_op\> \<rel\_operand\> \<rel\_end\> |
|  | \<rel\_end\> | → | \<rel\_op\> \<rel\_operand\> \<rel\_end\> |
| 152 | \<rel\_end\> | → | λ |
| 153 | \<rel\_operand\> | → | \<arithmetic\_expr\> |
| 154 | \<rel\_operand\> | → | identifier |
| 155 | \<rel\_operand\> | → | \<type\_casted\> |
| 156 | \<rel\_operand\> | → | \<num\_literal\> |
| 157 | \<rel\_operand\> | → | (\<rel\_expr\>) |
| 158 | \<rel\_expr\> | → | \<rel\_operand\_eq\> \<relation\_equality\> \<rel\_operand\_eq\> \<rel\_end\_eq\> |
| 159 | \<rel\_end\_eq\> | → | \<relation\_equality\> \<rel\_operand\_eq\> \<rel\_end\_eq\> |
| 160 | \<rel\_end\_eq\> | → | λ |
| 161 | \<rel\_operand\_eq\> | → | Stat literal |
| 162 | \<rel\_operand\_eq\> | → | Chant literal |
| 163 | \<rel\_operand\_eq\> | → | identifier |
| 164 | \<rel\_operand\_eq\> | → | (\<relational\_expr\>) |
| 165 | \<logical\_expr\> | → | \<log\_operand\>\<log\_op\>\<log\_operand\> \<log\_end\> |
| 166 | \<log\_end\> | → | \<log\_op\>\<log\_operand\>\<log\_end\> |
| 167 | \<log\_end\> | → | λ |
| 168 | \<log\_operand\> | → | \<logical\_expr\> |
| 169 | \<log\_operand\> | → | \<relational\_expr\> |
| 170 | \<log\_operand\> | → | identifier |
| 171 | \<log\_operand\> | → | Stat literal |
| 172 | \<log\_operand\> | → | (\<logical\_expr\>) |
| 173 | \<chant\_concat\> | → | \<chant\_operand\> \<chant\_concat\_end\> |
| 174 | \<chant\_concat\> | → | \<concat\_op\> \<concat\_end\> |
| 175 | \<chant\_operand\> | → | Chant literal |
| 176 | \<chant\_operand\> | → | identifier |
| 177 | \<chant\_operand\> | → | \<chant\_type\_casted\> |
| 178 | \<chant\_type\_casted\> | → | Chant (\<chant\_typcst\>) |
| 179 | \<chant\_typcst\> | → | \<literal\> |
| 180 | \<chant\_typcst\> | → | identifier |
| 181 | \<chant\_concat\_end\> | → | & \<concat\_op\> |
| 182 | \<chant\_concat\_end\> | → | λ |
| 183 | \<concat\_end\> | → | & \<chant\_operand\> |
| 184 | \<concat\_end\> | → | λ |
| 185 | \<concat\_op\> | → | \<chant\_operand\> |
| 186 | \<concat\_op\> | → | \<num\_literal\> |
| 187 | \<concat\_op\> | → | identifier |
| 188 | \<concat\_op\> | → | \<num\_type\_casted\> |
| 189 | \<num\_type\_casted\> | → | \<num\_data\_type\>(num\_literal) |
| 190 | \<num\_data\_type\> | → | Feint  |
| 191 | \<num\_data\_type\> | → | Floater |
| 192 | \<dribble\_statements\> | → | Dribble ( \<condition\> ) { \<team\_statements\> } \<pass\_statements\> \<shoot\_scp\> |
| 193 | \<pass\_statements\> | → | \<pass\_scp\> \<pass\_statements\> |
| 194 | \<pass\_statements\> | → | λ |
| 195 | \<pass\_scp\> | → | Pass ( \<condition\> ) { \<team\_statements\> } |
| 196 | \<shoot\_scp\> | → | Shoot { \<team\_statements\> } |
| 197 | \<shoot\_scp\> | → | λ |
| 198 | \<condition\> | → | \<relational\_expr\> |
| 199 | \<condition\> | → | \<logical\_expr\> |
| 200 | \<condition\> | → | Stat literal |
| 201 | \<forward\_statement\> | → | Forward (\<forward\_initialization\>; \<forward\_condition\>; \<forward\_incdec\>) {\<loop\_stmts\> \<next\_loopstmts\>} |
| 202 | \<forward\_initialization\> | → | \<numdata\_type\> identifier \= \<initial\_operand\> |
| 203 | \<numdata\_type\> | → | Feint |
| 204 | \<initial\_operand\> | → | \<num\_literal\> |
| 205 | \<initial\_operand\> | → | \<arithmetic\_expr\> |
| 206 | \<forward\_condition\> | → | \<forward\_operand\>\<forward\_op\>\<forward\_operand\> |
| 207 | \<forward\_operand\> | → | identifier |
| 208 | \<forward\_operand\> | → | \<arithmetic\_expr\> |
| 209 | \<forward\_operand\> | → | \<num\_literal\> |
| 210 | \<forward\_op\> | → | \<rel\_op\> |
| 211 | \<forward\_incdec\> | → | Identifier \<forward\_incdec\_operand\> \<num\_literal\>  |
| 212 | \<forward\_incdec\_operand\> | → | \-= |
| 213 | \<forward\_incdec\_operand\> | → | \+= |
| 214 | \<loop\_stmts\> | → | \<statement\> |
| 215 | \<loop\_stmts\> | → | \<loop\_dribble\> |
| 216 | \<loop\_dribble\> | → | Dribble ( \<condition\> ) { \<loop\_stmts\> \<next\_loopstmts\> } \<loop\_pass\> \<loop\_shoot\> |
| 217 | \<loop\_pass\> | → | \<next\_loop\_pass\> \<loop\_pass\> |
| 218 | \<loop\_pass\> | → | λ |
| 219 | \<next\_loop\_pass\> | → | Pass ( \<condition\> ) { \<loop\_stmts\> \<next\_loopstmts\> } |
| 220 | \<loop\_shoot\> | → | Shoot { \<loop\_stmts\> \<next\_loopstmts\> } |
| 221 | \<loop\_shoot\> | → | λ |
| 222 | \<next\_loopstmts\> | → | \<loop\_stmts\> \<next\_loopstmts\> |
| 223 | \<next\_loopstmts\> | → | λ |
| 224 | \<next\_loopstmts\> | → | Timeout; |
| 225 | \<next\_loopstmts\> | → | Resume; |
| 226 | \<play\_statement\> | → | Play (\<condition\>) { \<loop\_stmts\> \<next\_loopstmts\>\<forward\_incdec\>} |
| 227 | \<run\_play\_statement\> | → | Run { \<loop\_stmts\> \<next\_loopstmts\>\<forward\_incdec\> } Play ( \<condition\> ); |
| 228 | \<func\_call\> | → | identifier(\<arguments\>); |
| 229 | \<arguments\> | → | \<argument\> \<arguments\_end\> |
| 230 | \<arguments\_end\> | → | ,\<arguments\> |
| 233 | \<argument\> | → | \<literal\> |
| 234 | \<argument\> |  | Identifier \<array\_id\> |
| 235 |   \<array\_id\> |  | λ |
| 236 |   \<array\_id\> |  | \[\<element\_index\>\] |
| 237 | \<argument\> | → | \<type\_casted\> |

# **FIRST SET**

| First Set |  |  |  |
| :---: | :---: | ----- | :---: |
| \# | Production |  | Production Set |
| 1 | \<program\> | → | { Feint, Floater, Chant, Stat, λ} |
| 2 | \<global\_decl\> | → | { Feint, Floater, Chant, Stat, Const, λ } |
| 3 | \<global\_declared\> | → | { Feint, Floater, Chant, Stat, Const } |
| 4 | \<function\_dec\> | → | { Feint, Floater, Chant, Stat, λ } |
| 5 | \<functions\> | → | { Feint, Floater, Chant, Stat, Dunk, λ } |
| 6 | \<variable\_dec\> | → | { Feint, Floater, Chant, Stat} |
| 7 | \<data\_type\> | → | { Feint, Floater, Chant, Stat,} |
| 8 | \<initialize\_end\> | → | {=, λ} |
| 9 | \<array\_dec\> | → | { Feint, Floater, Chant, identifier} |
| 10 | \<2d\> | → | {λ, \[} |
| 11 | \<array\_initialization\> | → | {=, λ} |
| 12 | \<array\_manipulation\> | → | {identifier} |
| 13 | \<2d\_manipulation\> | → | {λ, \[} |
| 14 | \<array\_man\> | → | {=, λ} |
| 15 | \<element\_index\> | → | {Feint literal} |
| 16 | \<array\_size\> | → | {Feint literal} |
| 17 | \<array\_elem\> | → | {Feint literal, Floater literal, Chant literal} |
| 18 | \<elements\> | → | {, ,λ} |
| 19 | \<constant\_dec\> | → | { Const } |
| 20 | \<function\_decls\> | → | { Feint, Floater, Chant, Stat } |
| 21 | \<parameters\> | → | { Feint, Floater, Chant, Stat, λ } |
| 22 | \<parameters\_end\> | → | {, λ} |
| 23 | \<function\_definition\> | → | { λ, {,  Dunk } |
| 24 | \<local\_decl\> | → | { Feint, Floater, Chant, Stat, λ } |
| 25 | \<rebound\_statements\> | → | { Rebound, λ } |
| 26 | \<team\_statements\> | → | { Announce, Inbound, Dribble, Play, Forward, Run, Switch, Feint, Floater, Chant, Stat, identifier } |
| 27 | \<next\_statements\> | → | { Announce, Inbound, Dribble, Play, Forward, Run, switch, Feint, Floater, Chant, Stat, identifier, λ } |
| 28 | \<statement\> | → | { Announce, Inbound, identifier, Feint, Floater, Chant, Play, Run, Switch } |
| 29 | \<switch\_statement\> | → | { Switch } |
| 30 | \<case\_list\> | → | { Get } |
| 31 | \<case\> | → | { Get } |
| 32 | \<switch\_value\> | → | { Feint literal, Floater literal, ‘} |
| 33 | \<default\_case\> | → | { Default } |
| 34 | \<assignment\_statement\> | → | { Feint, Floater, Chant, Stat} |
| 35 | \<inbound\_statement\> | → | { Inbound } |
| 36 | \<input\> | → | { Chant literal} |
| 37 | \<inputs\> | → | { , } |
| 38 | \<announce\_statement\> | → | { Announce } |
| 39 | \<outputs\> | → | {identifier, Feint literal, Floater literal, Chant literal, Stat literal, “\\n, \\t, \\\\, \\”, \\@, \\&”, λ, } |
| 40 | \<output\_end\> | → | { &, λ } |
| 41 | \<global\_value\> | → | {identifier, Feint literal, Floater literal, (, \+, \-, \*, /, % , \< , \>, \<=, \>=, \==, \!=, \\n, \\t, \\\\, \\”, \\@, \\&, Chant literal, Stat literal} |
| 42 | \<local\_value\> | → | {identifier, Feint literal, Floater literal,  λ, (, \+, \-, \*, /, %, Chant literal, Stat literal, \\n, \\t, \\\\, \\”, \\@, \\&} |
| 43 | \<escape\_sequence\> | → | { \\n, \\t, \\\\, \\”, \\@, \\& } |
| 44 | \<literal\> | → | { Feint literal, Floater literal, Chant literal Stat literal } |
| 45 | \<type\_casted\> | → | { Feint, Floater, Chant, Stat} |
| 46 | \<type\_cast1\> | → | { identifier, Feint literal, Floater literal, Chant literal Stat literal} |
| 47 | \<assign\_op\> | → | {=, \+=, \-=, \*=, %=, /=, } |
| 48 | \<arith\_op\> | → | {+, \*, %, /, \- } |
| 49 | \<rel\_op\> | → | {\<, \>, \<=, \>=} |
| 50 | \<relation\_equality\> | → | {==, \!=} |
| 51 | \<log\_op\> | → | {AND, OR, NOT} |
| 52 | \<expression\> | → | {identifier, Feint literal, Floater literal, Stat Literal, Feint, Floater,Chant, Stat  (} |
| 53 | \<num\_literal\> | → | {Feint literal, Floater literal} |
| 54 | \<relational\_expr\> | → | {identifier, Feint, Floater, Chant, Stat, Feint literal, Floater literal, (, λ} |
| 55 | \<rel\_operand\> | → | {identifier, Chant, Stat, Feint literal, Floater literal, Feint, Floater, (} |
| 56 | \<rel\_expr\> | → | {identifier, Stat literal, Chant Literal, (} |
| 57 | \<rel\_operand\_eq\> | → | {Stat literal, Chant Literal, identifier, (} |
| 58 | \<logical\_expr\> | → | {identifier, Stat literal, (, Chant, Feint literal, Floater literal, λ} |
| 59 | \<log\_operand\> | → | {identifier, Stat literal, (, Chant, Feint literal, Floater literal, λ, \<, \>, \<=, \>=,} |
| 60 | \<chant\_concat\> | → | {Chant literal, identifier, Chant, Feint literal, Floater literal, Stat Literal, Feint, Floater, &, λ, } |
| 61 | \<dribble\_statements\> | → | { Dribble } |
| 62 | \<pass\_statements\> | → | {λ, Pass} |
| 63 | \<shoot\_scp\> | → | {λ, Shoot} |
| 64 | \<condition\> | → | {identifier, Chant, Stat, Feint literal, Floater literal,  (, λ, Stat literal} |
| 65 | \<forward\_statement\> | → | {Forward} |
| 66 | \<forward\_initialization\> | → | {Feint} |
| 67 | \<initial\_operand\> | → | {Feint literal, Floater literal, identifier, Chant, Stat, (,  } |
| 68 | \<forward\_condition\> | → | {+=, \-=, Feint literal, Floater literal, identifier, Chant, Stat, (,\<, \>, \<=, \>= } |
| 69 | \<forward\_operand\> | → | {Feint literal, Floater literal, identifier, Chant, Stat,} |
| 70 | \<forward\_op\> | → | {\<, \>, \<=, \>=} |
| 71 | \<forward\_incdec\> | → | Identifier |
| 72 | \<forward\_incdec\_operand\> | → | {+=, \-=} |
| 73 | \<loop\_stmts\> | → | {Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble, λ,  } |
| 74 | \<loop\_dribble\> | → | {Dribble} |
| 75 | \<loop\_pass\> | → | {λ, Pass} |
| 76 | \<loop\_shoot\> | → | {λ, Shoot} |
| 77 | \<next\_loopstmts\> | → | { λ,Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble,  Timeout; , Resume; } |
| 78 | \<play\_statement\> | → | {Play} |
| 79 | \<run\_play\_statement\> | → | {Run} |
| 80 | \<func\_call\> | → | { identifier } |
| 81 | \<arguments\> | → | {Feint, Floater, Chant, Stat, Feint literal Floater literal, Chant literal, Stat literal, identifier} |
| 82 | \<arguments\_end\> | → | { “,”} |
| 83 | \<argument\> | → | {Feint, Floater, Chant, Stat, Feint literal Floater literal, Chant literal, Stat literal, identifier} |
| 84 | \<array\_decls\> | → | {identifier} |
| 85 | \<decls\_end\> | → | {, , λ} |
| 86 | \<local\_declared\> | → | { Feint, Floater, Chant, Stat} |
| 87 | \<output\> | → | {identifier, Feint literal, Floater literal,  λ, (, \+, \-, \*, /, %, Chant, Stat literal, \\n, \\t, \\\\, \\”, \\@, \\&, Chant literal, &} |
| 88 | \<term\> | → | {identifier, Feint literal, Floater literal, Feint, Floater, (} |
| 89 | \<log\_end\> | → | {AND, OR, NOT, λ} |
| 90 | \<rel\_end\_eq\> | → | {==, \!=, λ} |
| 91 | \<arithexpr\_end\> | → | {+, \-, \*, /, &,λ} |
| 92 | \<concat\_op\> | → | {Chant literal, identifier, Chant, Feint literal, Floater literal, identifier, Feint, Floater} |
| 93 | \<chant\_operand\> | → | {Chant literal, identifier, Chant} |
| 94 | \<chant\_type\_casted\> | → | {Chant} |
| 95 | \<num\_type\_casted\> | → | {Feint, Floater} |
| 96 | \<concat\_end\> | → | {&, λ} |
| 97 | \<chant\_concat\_end\> | → | {&, λ} |
| 98 | \<variable\_decls\> | → | { Feint, Floater, Chant, Stat,} |
| 99 | \<parameter\> | → | {Feint, Floater, Chant, Stat,} |
| 100 | \<arithmetic\_expr\> | → | {identifier, Feint literal, Floater literal, Feint, Floater, (} |
| 101 | \<num\_data\_type\> | → | {Feint, Floater} |
| 102 | \<rel\_end\> | → | {λ} |
| 103 | \<pass\_scp\> | → | {Pass} |
| 104 | \<next\_loop\_pass\> |  | {Pass} |
| 105 | \<rows\> |  | {, , λ} |
| 106 | \<esc\_charac\> |  | {n, t, \\, ", @, &} |

# 

# 

# 

# 

# 

# 

# **FOLLOW SET**

| Follow Set |  |  |  |
| :---: | :---: | ----- | ----- |
| \# | Production |  |  |
| 1 | \<program\> | → |  |
| 2 | \<global\_decl\> | → | { Feint, Floater, Chant, Stat, Dunk } |
| 3 | \<global\_declared\> | → | { Feint, Floater, Chant, Stat, Const } |
| 4 | \<function\_dec\> | → | { Feint, Floater, Chant, Stat, Dunk } |
| 5 | \<functions\> | → | {Team(), Feint, Floater, Chant, Stat, Dunk } |
| 6 | \<variable\_dec\> | → | { Feint, Floater, Chant, Stat, Const } |
| 7 | \<data\_type\> | → | { identifier, ( } |
| 8 | \<initialize\_end\> | → | {, , ; } |
| 9 | \<array\_dec\> | → | { Feint, Floater, Chant, Stat, Const } |
| 10 | \<2d\> | → | { \=, ;} |
| 11 | \<array\_initialization\> | → | {;} |
| 12 | \<array\_manipulation\> | → | { Inbound, Announce, Dribble, Play, Forward,  identifier } |
| 13 | \<2d\_manipulation\> | → | {=, ;,  Feint literal, Floater literal, Chant literal, Inbound, Announce, Dribble, Play, Forward,  identifier } |
| 14 | \<array\_man\> | → | {;} |
| 15 | \<element\_index\> | → | { \] } |
| 16 | \<array\_size\> | → | { \] } |
| 17 | \<array\_elem\> | → | {, , } } |
| 18 | \<elements\> | → | { } } |
| 19 | \<constant\_dec\> | → | { Feint, Floater, Chant, Stat, Const } |
| 20 | \<function\_decls\> | → | { Feint, Floater, Chant, Stat } |
| 21 | \<parameters\> | → | { ) } |
| 22 | \<parameters\_end\> | → | { ) } |
| 23 | \<function\_definition\> | → | { Feint, Floater, Chant, Stat, Dunk, ; } |
| 24 | \<local\_decl\> | → | { },  Inbound, Announce, Dribble, Play, Forward, identifier} |
| 25 | \<rebound\_statements\> | → | { } } |
| 26 | \<team\_statements\> | → | { },  Inbound, Announce, Dribble, Play, Forward, identifier } |
| 27 | \<next\_statements\> | → | { },  Inbound, Announce, Dribble, Play, Forward, identifier, Switch, Feint, Floater, Run } |
| 28 | \<statement\> | → | { Announce, Inbound, Dribble, Play, Forward, Run, switch, Feint, Floater, Chant, Stat, identifier, } } |
| 29 | \<switch\_statement\> | → | { Inbound, Announce, Dribble, Play, Forward, identifier } |
| 30 | \<case\_list\> | → | { Get } |
| 31 | \<case\> | → | { Get } |
| 32 | \<switch\_value\> | → | { : } |
| 33 | \<default\_case\> | → | { } } |
| 34 | \<assignment\_statement\> | → | {  Announce, Inbound, Dribble, Play, Forward, Run, switch, Feint, Floater, Chant, Stat, identifier, } } |
| 35 | \<inbound\_statement\> | → | { Announce, Inbound, Dribble, Play, Forward, Run, switch, Feint, Floater, Chant, Stat, identifier, } } |
| 36 | \<input\> | → |  { , } |
| 37 | \<inputs\> | → | { ) } |
| 38 | \<announce\_statement\> | → | {  Announce, Inbound, Dribble, Play, Forward, Run, switch, Feint, Floater, Chant, Stat, identifier, } } |
| 39 | \<outputs\> | → | {&, )} |
| 40 | \<output\> | → | {&, )} |
| 41 | \<output\_end\> | → | {&, )} |
| 42 | \<global\_value\> | → | {&, )} |
| 43 | \<local\_value\> | → | {&, )} |
| 44 | \<escape\_sequence\> | → | {&, )} |
| 45 | \<literal\> | → | {; , &, )} |
| 46 | \<type\_casted\> | → | {&, ), Feint, Floater, Chant, Stat, Feint literal Floater literal, Chant literal, Stat literal, identifier, “,”} |
| 47 | \<type\_cast1\> | → | { ) } |
| 48 | \<assign\_op\> | → | {identifier, Feint literal, Floater literal, Chant literal,  ;, (, \+, \-, \*, /, %, Chant, Stat literal, \\n, \\t, \\\\, \\”, \\@, \\& } |
| 49 | \<arith\_op\> | → | { identifier, Feint literal, Floater literal, Feint, Floater, ‘} |
| 50 | \<rel\_op\> | → | { Feint literal, Floater literal, identifier, Chant, Stat, ( }  |
| 51 | \<relation\_equality\> | → | { Feint literal, Floater literal, identifier, Chant literal, Stat literal, (} |
| 52 | \<log\_op\> | → | { identifier, Stat literal, (, Chant, Feint literal, Floater literal, \<, \>, \<=, \>=, AND, OR, NOT } |
| 53 | \<expression\> | → | { &, ) } |
| 54 | \<num\_literal\> | → | {=, \+=, \-=, \*=, %=, /=, \+, \=, \*, /, %, identifier, Feint literal, Floater literal, (,λ, ), } , Chant literal, identifier, Chant, Stat, identifier, Feint, Floater \<, \>, \<=, \>=, ; \==, \!=, } |
| 55 | \<relational\_expr\> | → | {&, ), \==, \!= } |
| 56 | \<rel\_operand\> | → | {\<, \>, \<=, \>=, identifier, Chant, Stat, Feint literal, Floater literal, (, λ, \<, \>, \<=, \>=, } |
| 57 | \<rel\_expr\> | → | {identifier, Chant, Stat, Feint literal, Floater literal, (,  } |
| 58 | \<rel\_operand\_eq\> | → | {==, \!= } |
| 59 | \<logical\_expr\> | → | {AND, OR, NOT, identifier, Chant, Stat, Feint literal, Floater literal, (, λ, \<, \>, \<=, \>=, Stat literal, &, )}  |
| 60 | \<log\_operand\> | → | {AND, OR, NOT} |
| 61 | \<chant\_concat\> | → | {&, )} |
| 62 | \<dribble\_statements\> | → | { Inbound, Announce, Dribble, Play, Forward, identifier, }, } |
| 63 | \<pass\_statements\> | → | { Inbound, Announce, Dribble, Play, Forward, identifier, } , Shoot}  |
| 64 | \<shoot\_scp\> | → | {Inbound, Announce, Dribble, Play, Forward, identifier, }, } |
| 65 | \<condition\> | → | { ) } |
| 66 | \<forward\_statement\> | → | { Inbound, Announce, Dribble, Play, Forward, identifier } |
| 67 | \<forward\_initialization\> | → | {;} |
| 68 | \<initial\_operand\> | → | {;}  |
| 69 | \<forward\_condition\> | → | {;} |
| 70 | \<forward\_operand\> | → | {\<, \>, \<=, \>=, ; } |
| 71 | \<forward\_op\> | → | {Feint literal, Floater literal, identifier, Chant, Stat, } |
| 72 | \<forward\_incdec\> | → | { ), }  } |
| 73 | \<forward\_incdec\_operand\> | → | {Feint literal, Floater literal } |
| 74 | \<loop\_stmts\> | → | {Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble, λ,  Timeout; , Resume;, }, } |
| 75 | \<loop\_dribble\> | → | {Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble, ,  Timeout; , Resume; } |
| 76 | \<loop\_pass\> | → | {Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble, λ,  Timeout; , Resume; Shoot} |
| 77 | \<loop\_shoot\> | → | {Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble, ,  Timeout; , Resume;}  |
| 78 | \<next\_loopstmts\> | → | {}, Identifier, }  |
| 79 | \<play\_statement\> | → | { Inbound, Announce, identifier, Feint, Floater, Chant, Play, Run, Switch } |
| 80 | \<run\_play\_statement\> | → | { Inbound, Announce, identifier, Feint, Floater, Chant, Play, Run, Switch } |
| 81 | \<func\_call\> | → | {identifier, Feint literal, Floater literal,  λ, (, \+, \-, \*, /, %, Chant, Stat literal, “\\n, \\t, \\\\, \\”, \\@, \\&”} |
| 82 | \<arguments\> | → | { ), } \#AddFollowSetOfArguments\_end |
| 83 | \<arguments\_end\> | → | {} |
| 84 | \<term\> | → | {=, \+=, \-=, \*=, %=, /=, \+, \=, \*, /, %, identifier, Feint literal, Floater literal, (,  &, \<, \>, \<=, \>=, Chant, Stat } |
| 85 | \<arithmetic\_expr\> | → | { &, ), \=, \+=, \-=, \*=, %=, /=, \+, \=, \*, /, %, identifier, Feint literal, Floater literal, (, \<, \>, \<=, \>=, Chant, Stat, } |
| 86 | \<concat\_op\> | → | {&, )} |
| 87 | \<array\_decls\> | → | { Feint, Floater, Chant, Stat, Const } |
| 88 | \<decls\_end\> | → | {, , ;} |
| 89 | \<local\_declared\> | → | { Feint, Floater, Chant, Stat, identifier} |
| 90 | \<log\_end\> | → | {&, )} |
| 91 | \<rel\_end\_eq\> | → | {identifier, Chant, Stat, Feint literal, Floater literal, (,  } |
| 92 | \<argument\> | → | {Feint, Floater, Chant, Stat, Feint literal Floater literal, Chant literal, Stat literal, identifier, “,”} |
| 93 | \<num\_type\_casted\> | → | {=, \+=, \-=, \*=, %=, /=, \+, \=, \*, /, %, identifier, Feint literal, Floater literal, (,  &, \<, \>, \<=, \>=, Chant, Stat } |
| 94 | \<chant\_operand\> | → | {&, )} |
| 95 | \<chant\_type\_casted\> | → | {&, )} |
| 96 | \<concat\_end\> | → | {&, )} |
| 97 | \<chant\_concat\_end\> | → | {&, )} |
| 98 | \<variable\_decls\> | → | { Feint, Floater, Chant, Stat, Const } |
| 99 | \<parameter\> | → | {, λ} |
| 100 | \<rel\_end\> | → | {&, ), \==, \!= , } |
| 101 | \<num\_data\_type\> | → | { ( } |
| 102 | \<pass\_scp\> | → | (Pass, Shoot} |
| 103 | \<next\_loop\_pass\> | → | {Pass} |
| 104 | \<arithexpr\_end\> | → | {  &, ), \=, \+=, \-=, \*=, %=, /=, \+, \=, \*, /, %, identifier, Feint literal, Floater literal, (, \<, \>, \<=, \>=, Chant, Stat} |
| 105 | \<rows\> |  | { } } |
| 106 | \<esc\_charac\> |  | {&, )} |

# 

# **PREDICT SET**

| 1 | First\<global\_decl\> \<function\_dec\> \<functions\> Team() { \<local\_decl\> \<team\_statements\> } | First(\<global\_decl\>) | { Feint, Floater, Chant, Stat, Const, λ } |
| :---- | :---- | :---- | ----- |
| 2 | First\<global\_declared\> \<global\_decl\> | First(\<global\_declared\>) | { Feint, Floater, Chant, Stat, Const } |
| 3 | First (λ) ∪ Follow \<global\_decl\> | Follow(\<global\_decl\>) | { Feint, Floater, Chant, Stat, Dunk } |
| 4 | First\<variable\_dec\> | First(\<variable\_dec\>) | { Feint, Floater, Chant, Stat} |
| 5 | First\<array\_dec\> | First(\<array\_dec\>) | { Feint, Floater, Chant, identifier} |
| 6 | First\<constant\_dec\> | First(\<constant\_dec\>) | { Const } |
| 7 | First\<function\_decls\>\<function\_dec\> | First(\<function\_decls\>) | { Feint, Floater, Chant, Stat } |
| 8 | First (λ) ∪ Follow \<function\_dec\> | Follow(\<function\_dec\>) | { Feint, Floater, Chant, Stat, λ } |
| 9 | First \<function\_definition\> \<functions\> | First(\<function\_definition\>) | { Feint, Floater, Chant, Stat, Dunk } |
| 10 | First (λ) ∪ Follow \<functions\> | Follow(\<functions\>) | {Team(), Feint, Floater, Chant, Stat, Dunk } |
| 11 | First \<variable\_decls\> | First(\<variable\_decls\>) |  |
| 12 | First \<data\_type\> identifier \<initialize\_end\> \<decls\_end\>; | First(\<data\_type\>) | { Feint, Floater, Chant, Stat,} |
| 13 | First , identifier \<initialize\_end\> \<decls\_end\> | First(,) | { , } |
| 14 | First (λ) ∪ Follow \<decls\_end\> | Follow(\<decls\_end\>) | {, , ;} |
| 15 | First Feint | First(Feint) | \[ Feint } |
| 16 | First Floater | First(Floater) | { Floater } |
| 17 | First Chant | First(Chant) | { Chant } |
| 18 | First Stat | First(Stat) | { Stat } |
| 19 | First \= \<global\_value\> \<decls\_end\> | First(=) | { \= } |
| 20 | First (λ) ∪ Follow \<initialize\_end\> | Follow(\<initialize\_end\>) | {, , ;,  } |
| 21 | First \<data\_type\> \<array\_decls\>   | First(\<data\_type\>) | { Feint, Floater, Chant, Stat,} |
| 22 | First (identifier\[\<array\_size\>\] \<2d\> \<array\_initialization\>;) | First(identifier) | { Identifier } |
| 23 | First(λ) ∪ Follow\<2d\> | Follow(\<2d\>) | {=,  Feint literal, Floater literal, Chant literal} |
| 24 | First(\[\<array\_size\>\]) | First(\[\<array\_size\>\]) | {Feint literal} |
| 25 | First \= { \<row\> \<rows\> } | First(=) | { \= } |
| 26 | First (λ) ∪ Follow \<array\_initialization\> | Follow(\<array\_initialization\>) | {;} |
| 27 | First {\<array\_elem\> \<elements\> } | First(\<array\_elem\>) | {Feint literal, Floater literal, Chant literal} |
| 28 | First , {\<array\_elem\> \<elements\> } | First(,) | { , } |
| 29 | First (λ) ∪ Follow \<rows\>  | Follow(\<rows\>) | { rows } |
| 30 | First Feint literal | First(Feint literal) | { Feint literal } |
| 31 | First Feint literal | First(Feint literal) | { Feint literal } |
| 32 | First Feint literal | First(Feint literal) | { Feint literal } |
| 33 | First Floater literal | First(Floater literal) | { Floater literal } |
| 34 | First Chant literal | First(Chant literal) | { Chant literal } |
| 35 | First , \<array\_elem\>\<elements\> | First(,) | { , } |
| 36 | First (λ) ∪ Follow \<elements\> | Follow(\<elements\>) | { , } |
| 37 | First Const \<data\_type\> identifier \= \<literal\>; | First(Const) | { Const } |
| 38 | First \<data\_type\> identifier(\<parameters\>);  | First(\<data\_type\>) | { Feint, Floater, Chant, Stat,} |
| 39 | First \<parameter\>\<parameters\_end\> | First(\<parameter\>) | {Feint, Floater, Chant, Stat,} |
| 40 | First (λ) ∪ Follow \<parameters\> | Follow(\<parameters\>) | { ) } |
| 41 | First \<data\_type\> identifier | First(\<data\_type\>) | { Feint, Floater, Chant, Stat,} |
| 42 | First , \<parameters\> | First(,) | { , } |
| 43 | First (λ) ∪ Follow\<parameters\_end\> | Follow(\<parameters\_end\>) | { ) } |
| 44 | First \<data\_type\> identifier(\<parameters\>) {\<team\_statements\> \<rebound\_statements\>} | First(\<data\_type\>) | { Feint, Floater, Chant, Stat,} |
| 45 | First Dunk identifier(\<parameters\>){\<team\_statements\>} | First(Dunk) | { Dunk } |
| 46 | First \<local\_declared\> \<local\_decl\> | First(\<local\_declared\>) | { Feint, Floater, Chant, Stat, identifier} |
| 47 | First  (λ) ∪ Follow \<local\_decl\> | Follow \<local\_decl\> | { Feint, Floater, Chant, Stat, identifier} |
| 48 | First \<variable\_dec\> | First(\<variable\_dec\>) | { Feint, Floater, Chant, Stat} |
| 49 | First \<array\_dec\> | First(\<array\_dec\>) | { Feint, Floater, Chant, Stat, Const } |
| 50 | First Rebound \<local\_value\>; | First(Rebound) | { Rebound } |
| 51 | First (λ) ∪ Follow\<rebound\_statements\> | Follow(\<rebound\_statements\>) | { } } |
| 52 | First \<statement\> \<next\_statements\> | First(\<statement\>) | {Announce, Inbound, identifier, Feint, Floater, Chant, Play, Run, Switch } |
| 53 | First \<dribble\_statements\> \<next\_statements\> | First(\<dribble\_statements\>)  | { Inbound, Announce, Dribble, Play, Forward, identifier, }, } |
| 54 | First \<team\_statements\> \<next\_statements\> | First(\<team\_statements\>) | {Announce, Inbound, Dribble, Play, Forward, Run, switch, Feint, Floater, Chant, Stat, identifier } |
| 55 | First (λ) ∪ Follow \<next\_statements\> | Follow(\<next\_statements\>) | { Inbound, Announce, Dribble, Play, Forward, identifier } |
| 56 | First \<announce\_statement\> | First(\<announce\_statement\>) | {Announce} |
| 57 | First \<inbound\_statement\> | First(\<inbound\_statement\>) | {Inbound} |
| 58 | First \<forward\_statement\> | First(\<forward\_statement\>) | { Inbound, Announce, Dribble, Play, Forward, identifier } |
| 59 | First \<play\_statement\> | First(\<play\_statement\>) | {Play} |
| 60 | First \<run\_play\_statement\> | First(\<run\_play\_statement\>) | {Run} |
| 61 | First \<variable\_dec\> | First(\<variable\_dec\>) | { Feint, Floater, Chant, Stat} |
| 62 | First \<array\_dec\> | First(\<array\_dec\>) | { Feint, Floater, Chant, Stat, Const } |
| 63 | First \<assignment\_statement\> | First(\<assignment\_statement\>) | { Feint, Floater, Chant, Stat,} |
| 64 | First \<switch\_statement\> | First(\<switch\_statement\>) | {Switch} |
| 65 | First \<array\_manipulation\> | First(\<array\_manipulation\>) | {identifier} |
| 66 | First identifier\[\<element\_index\>\] \<2d\_manipulation\> \<array\_man\>; | First(identifier) | {identifier} |
| 67 | First \[\<element\_index\>\] | First(\<element\_index\>) | {Feint literal} |
| 68 | First (λ) ∪ Follow \<2d\_manipulation\> | Follow(\<2d\_manipulation\>) | {=, Feint literal, Floater literal, Chant literal, Inbound, Announce, Dribble, Play, Forward,  identifier } |
| 69 | First \= \<array\_elem\> | First(=) | { \= } |
| 70 | First (λ) ∪ Follow \<array\_man\> | Follow(\<array\_man\>)8 | {;} |
| 71 | First Switch (\<switch\_exp\>) {\<case\_list\> \<default\_case\>} | First\<Switch\> | { Switch } |
| 72 | First identifier | First identifier | { Identifier } |
| 73 | First Feint literal | First Feint literal | { Feint literal } |
| 74 | First Chant literal | First Chant literal | { Chant literal } |
| 75 | First \<case\> \<case\_list\> | First \<case\> | {Get} |
| 76 | First Get \<switch\_value\>: | First Get | {Get} |
| 77 | First ‘arith\_op’ | First\<arith\_op\> | {=, \+=, \-=, \*=, %=, /=, \+, \=, \*, /, %, } |
| 78 | First ‘alphabet’ | First\<alphabet\> | { alphabet } |
| 79 | First Feint literal | First(Feint literal) | { Feint literal } |
| 80 | First Floater literal | First(Floater literal) | { Floater literal } |
| 81 | First Default: \<Announce\> | First(Default) | { Default } |
| 82 | First \<data\_type\> identifier \<assign\_op\> \<local\_value\>; | First(data\_type\>) | { Feint, Floater, Chant, Stat,} |
| 83 | First Inbound(\<input\> \<inputs\>); | First(Inbound\>) | { Inbound } |
| 84 | First Chant literal  | First(First Chant literal) | { Chant literal} |
| 85 | First , identifier | First(,) | { , } |
| 86 | First Announce(\<outputs\>); | First(Announce) | { Announce} |
| 87 | First \<output\>\<output\_end\> | First(output) | { Output} |
| 88 | First & \<outputs\> | First(&) | { & } |
| 89 | First (λ) ∪ Follow \<output\_end\> | Follow(output\_end) | {&, )} |
| 90 | First \<global\_value\> | First(global\_value) | {identifier, Feint literal, Floater literal, λ, (, \+, \-, \*, /, % , \< , \>, \<=, \>=, \==, \!=, \\n, \\t, \\\\, \\”, \\@, \\&, Chant, Stat literal} |
| 91 | First \<local\_value\> | First(local\_value) | {identifier, Feint literal, Floater literal,  λ, (, \+, \-, \*, /, %, Chant, Stat literal, \\n, \\t, \\\\, \\”, \\@, \\&} |
| 92 | First \<chant\_concat\> | First(chant\_concat) | {Chant literal, identifier, Chant, Feint literal, Floater literal, &, λ, } |
| 93 | First identifier | First(identifier) | { identifier } |
| 94 | First \<literal\> | First(\<literal\>) | { Literal } |
| 95 | First \<expression\> | First(\<expression\>) | {identifier, Feint literal, Floater literal, (} |
| 96 | First loc\_identifier | First(loc\_identifier) | { loc\_identifier } |
| 97 | First arr\_identifier | First(arr\_identifier) | { arr\_identifier } |
| 98 | First identifier | First(identifier) | { identifier } |
| 99 | First identifier \[\<element\_index\>\] | First(identifier) | { identifier } |
| 100 | First \<expression\> | First(\<expression\>) | {identifier, Feint literal, Floater literal, (} |
| 101 | First \<func\_call\> | First(\<func\_call\>) | { identifier } |
| 102 | First \<type\_casted\> | First(\<type\_casted\>) | {Feint, Floater, Chant, Stat} |
| 103 | First \<escape\_sequence\> | First (\<escape\_sequence\>) | {\\n, \\t, \\\\, \\”, \\@, \\&} |
| 104 | First “\\\<esc\_charac\>” | First(“\\\<esc\_charac\>”) | { \\esc\_charac } |
| 105 | First n | First(n) | { n } |
| 106 | First t | First(t) | { t } |
| 107 | First \\ | First(\\) | { \\ } |
| 108 | First “ | First(“) | { “ } |
| 109 | First @ | First(@) | { @ } |
| 110 | First & | First(&) | { & } |
| 111 | First Feint literal | First(Feint literal) | { Feint literal } |
| 112 | First Floater literal | First(Floater literal) | { Floater literal } |
| 113 | First Chant literal | First(Chant literal) | { Chant literal } |
| 114 | First Stat literal | First(Stat literal) | { Stat literal } |
| 115 | First \<data\_type\> (\<type\_cast1\>) | First(\<data\_type\>) | { Feint, Floater, Chant, Stat,} |
| 116 | First \<literal\> | First(\<literal\>) | { literal } |
| 117 | First identifier | First(identifier) | { Identifier } |
| 118 | First \= | First(=) | { \= } |
| 119 | First \+= | First(+=) | { \+= } |
| 120 | First \-= | First(-=) | { \-= } |
| 121 | First \*= | First(\*=) | { \*= } |
| 122 | First %= | First(%=) | { %= } |
| 123 | First /= | First(/=) | { /= } |
| 124 | First \+ | First(+) | { \+ } |
| 125 | First \- | First(-) | { \- } |
| 126 | First \* | First(\*) | { \* } |
| 127 | First / | First(/) | { / } |
| 128 | First % | First(%) | { % } |
| 129 | First \< | First(\<) | { \< } |
| 130 | First \> | First(\>) | { \> } |
| 131 | First \<= | First(\<=) | { \<= } |
| 132 | First \>= | First(\>=) | { \>= } |
| 133 | First \<relation\_equality\> | First(\<relation\_equality\>) | {==, \!=} |
| 134 | First \== | First(==) | { \== } |
| 135 | First \!= | First(\!=) | { \!= } |
| 136 | First AND | First(AND) | { AND } |
| 137 | First OR | First(OR) | { OR } |
| 138 | First NOT | First(NOT) | { NOT } |
| 139 | First \<arithmetic\_expr\> | First(\<arithmetic\_expr\>) | { Feint, Floater } |
| 140 | First \<relational\_expr\> | First(\<relational\_expr\>) | {identifier, Chant, Stat, Feint literal, Floater literal, (, λ, \<, \>, \<=, \>=, } |
| 141 | First \<logical\_expr\> | First(\<logical\_expr\>) | {identifier, Stat literal, (, Chant, Feint literal, Floater literal, λ, \<, \>, \<=, \>=,} |
| 142 | First \<term\> \<arithexpr\_end\> | First(\<term\>) | {identifier, Feint literal, Floater literal, Feint, Floater, (} |
| 143 | First \<arith\_op\> \<term\> \<arithexpr\_end\> | First(\<arith\_op\>) | {=, \+=, \-=, \*=, %=, /=, \+, \=, \*, /, %, } |
| 144 | First (λ) ∪ Follow \<arithexpr\_end\> | Follow(\<arithexpr\_end\>) | {=, \+=, \-=, \*=, %=, /=, \+, \=, \*, /, %, identifier, Feint literal, Floater literal, (} |
| 145 | First identifier | First(identifier) | { Identifier } |
| 146 | First \<num\_literal\> | First(\<num\_literal\>) | {Feint literal, Floater literal} |
| 147 | First \<num\_type\_casted\> | First(\<num\_type\_casted\>) | {Feint, Floater} |
| 148 | First  \<arithmetic\_expr\>  | First(\<arithmetic\_expr\> ) | { Feint, Floater } |
| 149 | First Feint literal | First(Feint literal) | {Feint literal} |
| 150 | First Floater literal | First(Floater literal) | {Float literal} |
| 151 | First \<rel\_operand\> \<rel\_op\> \<rel\_operand\> \<rel\_end\> | First(\<rel\_operand) | {identifier, Chant, Stat, Feint literal, Floater literal, (,  } |
| 152 | First (λ) ∪ Follow\<rel\_end\> | Follow(\<rel\_end\>) | { rel\_end } |
| 153 | First \<arithmetic\_expr\> | First(\<arithmetic\_expr\>) | {identifier, Feint literal, Floater literal, Feint, Floater, (} |
| 154 | First identifier | First(identifier) | { Identifier } |
| 155 | First \<type\_casted\> | First(\<type\_casted\>) | {Feint, Floater, Chant, Stat, λ} |
| 156 | First \<num\_literal\> | First(\<num\_literal\>) | {Feint literal, Floater literal} |
| 157 | First (\<rel\_expr\>) | First(\<rel\_expr\>) | {identifier, Stat literal, Chant, \==, \!=, (, λ } |
| 158 | First (\<rel\_operand\_eq\> \<relation\_equality\> \<rel\_operand\_eq\> \<rel\_end\_eq\>) | First(\<rel\_operand\_eq\>) | {Stat literal, Chant, identifier, (} |
| 159 | First (\<relation\_equality\> \<rel\_operand\_eq\> \<rel\_end\_eq\>) | First (\<relation\_equality\>) | {==, \!=} |
| 160 | First (λ) ∪ Follow \<rel\_end\_eq\> | Follow(\<rel\_end\_eq\>) | {identifier, Chant, Stat, Feint literal, Floater literal, (,  } |
| 161 | First Stat literal | First(Stat literal) | { Stat } |
| 162 | First Chant literal | First(Chant literal) | { Chant } |
| 163 | First identifier | First(identifier) | { identifier } |
| 164 | First \<relational\_expr\> | First(\<relational\_expr\>) | {identifier, Chant, Stat, Feint literal, Floater literal, (, λ, \<, \>, \<=, \>=, } |
| 165 | First \<log\_operand\>\<log\_op\>\<log\_operand\> \<log\_end\> | First(\<log\_operand\>) | {identifier, Stat literal, (, Chant, Feint literal, Floater literal, λ, \<, \>, \<=, \>=,} |
| 166 | First \<log\_op\>\<log\_operand\>\<log\_end\> | First(\<log\_op\>) | {AND, OR, NOT} |
| 167 | First (λ) ∪ Follow \<log\_end\> | Follow(\<log\_end\>) | {AND, OR, NOT, λ} |
| 168 | First \<logical\_expr\> | First(\<logical\_expr\>) | {identifier, Stat literal, (, Chant, Feint literal, Floater literal, λ, \<, \>, \<=, \>=,} |
| 169 | First \<relational\_expr\> | First(\<relational\_expr\>) | {identifier, Chant, Stat, Feint literal, Floater literal, (, λ, \<, \>, \<=, \>=, } |
| 170 | First identifier | First(identifier) | { identifier } |
| 171 | First Stat literal | First(Stat literal) | { Stat literal } |
| 172 | First (\<logical\_expr\>) | First(\<logical\_expr\>) | {identifier, Stat literal, (, Chant, Feint literal, Floater literal, λ, \<, \>, \<=, \>=,} |
| 173 | First (\<chant\_operand\> \<chant\_concat\_end\>) | First(\<chant\_operand\> ) | {Chant literal, identifier, Chant} |
| 174 | First \<concat\_op\> \<concat\_end\> | First(\<concat\_op\>) | {Chant literal, identifier, Chant, Feint literal, Floater literal, identifier, Feint, Floater} |
| 175 | First Chant literal | First(Chant literal) | { Chant literal } |
| 176 | First identifier | First(identifier) | { Identifier } |
| 177 | First \<chant\_type\_casted\> | First(\<chant\_type\_casted\>) | { Chant } |
| 178 | First Chant (\<chant\_typcst\>) | First(Chant) | { Chant } |
| 179 | First \<literal\> | First(\<literal\>) | { literal } |
| 180 | First identifier | First(identifier) | { identifier } |
| 181 | First & \<concat\_op\> | First(&) | {&} |
| 182 | First (λ) ∪ Follow \<chant\_concat\_end\> | Follow(\<chant\_concat\_end\>) | {&, )} |
| 183 | First & \<chant\_operand\> | First(&) | {&} |
| 184 | First (λ) ∪ Follow \<concat\_end\> | Follow(\<concat\_end\>) | {&, )} |
| 185 | First \<chant\_operand\> | First(\<chant\_operand\>) | {Chant literal, identifier, Chant} |
| 186 | First \<num\_literal\> | First(\<num\_literal\>) | {Feint literal, Floater literal} |
| 187 | First identifier | First(identifier) | { Identifier } |
| 188 | First \<num\_type\_casted\> | First(\<num\_type\_casted\>) | {Feint, Floater} |
| 189 | First \<num\_data\_type\>(num\_literal) | First(\<num\_data\_type\>) | {Feint, Floater} |
| 190 | First Feint  | First(Feint)  | { Feint } |
| 191 | First Floater | First(Floater) | { Floater } |
| 192 | First Dribble ( \<condition\> ) { \<team\_statements\> } \<pass\_statements\> \<shoot\_scp\> | First(Dribble) | { Dribble } |
| 193 | First \<pass\_scp\> \<pass\_statements\> | First(\<pass\_scp\>)  | {Pass} |
| 194 | First (λ) ∪ Follow \<pass\_statements\> | Follow(\<pass\_statements\>) | { Inbound, Announce, Dribble, Play, Forward, identifier, } , Shoot}  |
| 195 | First Pass ( \<condition\> ) { \<team\_statements\> } | First(Pass) | {λ, Pass} |
| 196 | First Shoot { \<team\_statements\> } | First(Shoot) | { Shoot } |
| 197 |  First (λ) ∪ Follow \<shoot\_scp\> | Follow(\<shoot\_scp\>) | {Inbound, Announce, Dribble, Play, Forward, identifier, }, } |
| 198 | First \<relational\_expr\> | First(\<relational\_expr\>) | {identifier, Chant, Stat, Feint literal, Floater literal, (, λ, \<, \>, \<=, \>=, } |
| 199 | First \<logical\_expr\> | First (\<logical\_expr\>) | {identifier, Stat literal, (, Chant, Feint literal, Floater literal, λ, \<, \>, \<=, \>=,} |
| 200 | First Stat literal | First(Stat literal) | { Stat literal } |
| 201 | First (Forward \<forward\_initialization\>; \<forward\_condition\>; \<forward\_incdec\>) {\<loop\_stmts\> \<next\_loopstmts\>} | First(Forward) | { Forward } |
| 202 | First \<num\_data\_type\> identifier \= \<initial\_operand\> | First(\<num\_data\_type\>) | {Feint, Floater} |
| 203 | First Feint | First(Feint) | { Feint literal } |
| 204 | First \<num\_literal\> | First(\<num\_literal\>) | {Feint literal, Floater literal} |
| 205 | First \<arithmetic\_expr\> | First(\<arithmetic\_expr\>) | {identifier, Feint literal, Floater literal, Feint, Floater, (} |
| 206 | First \<forward\_operand\>\<forward\_op\>\<forward\_operand\> | First(\<forward\_operand\>) | Feint literal, Floater literal, identifier, Chant, Stat,} |
| 207 | First identifier | First(identifier) | { Identifier } |
| 208 | First \<arithmetic\_expr\> | First(\<arithmetic\_expr\>) | {identifier, Feint literal, Floater literal, Feint, Floater, (} |
| 209 | First \<num\_literal\> | First(\<num\_literal\>) | {Feint literal, Floater literal} |
| 210 | First \<rel\_op\> | First(\<rel\_op\>) | {\<, \>, \<=, \>=} |
| 211 | First Identifier \<forward\_incdec\_operand\> \<num\_literal\>  | First(Identifier)  | { Identifier } |
| 212 | First \+= | First(+=) | { \+= } |
| 213 | First \-= | First(-=) | { \-= } |
| 214 | First \<statement\> | First(\<statement\>) | {Announce, Inbound, identifier, Feint, Floater, Chant, Play, Run, Switch } |
| 215 | First \<loop\_dribble\> | First(\<loop\_dribble\>) | {Dribble} |
| 216 | First Dribble ( \<condition\> ) { \<loop\_stmts\> \<next\_loopstmts\> } \<loop\_pass\> \<loop\_shoot\> | First(Dribble) | { Dribble } |
| 217 | First \<next\_loop\_pass\> \<loop\_pass\> | First(\<next\_loop\_pass\>)  | { Pass } |
| 218 |  First (λ) ∪ Follow \<loop\_pass\> | Follow(\<loop\_pass\>) | {Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble, λ,  Timeout; , Resume; Shoot} |
| 219 | First Pass ( \<condition\> ) { \<loop\_stmts\> \<next\_loopstmts\> } | First(Pass) | { Pass } |
| 220 | First Shoot { \<loop\_stmts\> \<next\_loopstmts\> } | First(Shoot) | {Shoot} |
| 221 | First (λ) ∪ Follow \<loop\_shoot\> | Follow(\<loop\_shoot\>) | {Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble, ,  Timeout; , Resume;} |
| 222 | First \<loop\_stmts\> \<next\_loopstmts\> | First(\<loop\_stmts\>)  | {Inbound, Announce, identifier, Feint, Floater, Chant, Forward, Play, Run, Switch, Dribble, λ,  } |
| 223 | First (λ) ∪ Follow \<next\_loopstmts\> | Follow(\<next\_loopstmts\>) | {  Identifier } |
| 224 | First Timeout; | First(Timeout;) | {Timeout} |
| 225 | First Resume; | First(Resume;) | {Resume} |
| 226 | First Play (\<condition\>) { \<loop\_stmts\> \<next\_loopstmts\>\<forward\_incdec\>} | First(Play) | {Play} |
| 227 | First Run { \<loop\_stmts\> \<next\_loopstmts\>\<forward\_incdec\> } Play ( \<condition\> ); | First(Run) | {Run} |
| 228 | First identifier(\<arguments\>); | First(identifier) | {Identifier} |
| 229 | First \<argument\> \<arguments\_end\> | First(\<argument\>) | {Feint, Floater, Chant, Stat, Feint literal Floater literal, Chant literal, Stat literal, identifier} |
| 230 | First ,\<arguments\> | First(\<”,”\>) | { , } |
| 231 | First arg\_identifier | First(arg\_identifier) | {arg\_identifer} |
| 232 | First array\_identifier | First(array\_identifier) | {array\_identifer} |
| 233 | First \<literal\> | First(\<literal\>) | {Feint literal, Floater literal, Chant literal Stat literal} |
| 234 | First \<type\_casted\> | First(\<type\_casted\>) | {Feint, Floater, Chant, Stat, λ} |
| 235 | First identifier | First(identifier) | {Identifier} |
| 236 | First identifier \[\<element\_index\>\] | First(identifier) | {Identifier} |

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,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>

[image7]: <data:image/png;base64,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>

[image8]: <data:image/png;base64,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>

[image9]: <data:image/png;base64,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>

[image10]: <data:image/png;base64,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>