# **CONTEXT FREE GRAMMAR**

| 1 | \<program\> | → | \<global\_decl\> \<function\_dec\> \<functions\> Team() { \<local\_decl\> \<team\_statements\> }  |
| :---- | :---- | :---- | :---- |
| 2 | \<global\_decl\> | → | \<global\_declared\> \<global\_decl\> |
| 3 | \<global\_decl\> | → | λ |
| 4 | \<global\_declared\> | → | \<variable\_dec\> |
| 5 | \<global\_declared\> | → | \<array\_dec\>  |
| 6 | \<global\_declared\> | → | \<constant\_dec\> |
| 7 | \<function\_dec\> | → | Wilt \<function\_decls\>\< \<function\_dec\> |
| 8 | \<function\_dec\> | → | λ |
| 9 | \<functions\> | → | \<function\_definition\> \<functions\> |
| 10 | \<functions\> | → | λ |
| 11 | \<variable\_dec\> | → | \<variable\_decls\> |
| 12 | \<variable\_decls\> | → | \<data\_type\> identifier \<initialize\_end\> \<decls\_end\>; |
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
| 38 | \<function\_decls\> | → | Wilt \<data\_type\> identifier(\<parameters\>) \<function\_definition\>; |
| 39 | \<parameters\> | → | \<parameter\>\<parameters\_end\> |
| 40 | \<parameters\> | → | λ |
| 41 | \<parameter\> | → | \<data\_type\> identifier |
| 42 | \<parameters\_end\> | → | , \<parameters\> |
| 43 | \<parameters\_end\> | → | λ |
| 44 | \<function\_definition\> | → |  λ |
| 45 | \<function\_definition\> | → | {\<team\_statements\> \<rebound\_statements\>} |
| 46 | \<function\_definition\> | → | Dunk identifier(\<parameters\>){\<team\_statements\>} |
| 47 | \<local\_decl\> | → | \<local\_declared\> \<local\_decl\> |
| 48 | \<local\_decl\> | → | λ |
| 49 | \<local\_declared\> | → | \<variable\_dec\> |
| 50 | \<local\_declared\> | → | \<array\_dec\> |
| 51 | \<rebound\_statements\> | → | Rebound \<local\_value\>; |
| 52 | \<rebound\_statements\> | → | λ |
| 53 | \<team\_statements\> | → | \<statement\> \<next\_statements\> |
| 54 | \<team\_statements\> | → | \<dribble\_statements\> \<next\_statements\> |
| 55 | \<team\_statements\> | → |   \<array\_dec\>\<next\_statements\> |
| 56 | \<next\_statements\> | → | \<team\_statements\> \<next\_statements\> |
| 57 | \<next\_statements\> | → | λ |
| 58 | \<statement\> | → | \<announce\_statement\> |
| 59 | \<statement\> | → | \<inbound\_statement\> |
| 60 | \<statement\> | → | \<forward\_statement\> |
| 61 | \<statement\> | → | \<play\_statement\> |
| 62 | \<statement\> | → | \<run\_play\_statement\> |
| 63 | \<statement\> | → | \<variable\_dec\> |
| 64 | \<statement\> | → | \<assignment\_statement\> |
| 65 | \<statement\> | → | \<switch\_statement\> |
| 66 | \<statement\> | → | \<array\_manipulation\> |
| 67 |  \<array\_manipulation\>  | → | identifier\[\<element\_index\>\] \<2d\_manipulation\> \<array\_man\>; |
| 68 | \<2d\_manipulation\> | → | \[\<element\_index\>\] |
| 69 | \<2d\_manipulation\> | → | λ |
| 70 | \<array\_man\> | → | \= \<array\_elem\> |
| 71 | \<array\_man\> | → | λ |
| 72 | \<switch\_statement\> | → | Switch (\<switch\_exp\>) {\<case\_list\> \<default\_case\>} |
| 73 | \<switch\_exp\> | → | identifier |
| 74 | \<switch\_exp\> | → | Feint literal |
| 75 | \<switch\_exp\> | → | Chant literal |
| 76 | \<case\_list\> | → | \<case\> \<case\_list\> |
| 77 | \<case\> | → | Get \<switch\_value\>: |
| 78 | \<switch\_value\> | → | ‘arith\_op’ |
| 79 | \<switch\_value\> | → | ‘alphabet’ |
| 80 | \<switch\_value\> | → | Feint literal |
| 81 | \<switch\_value\> | → | Floater literal |
| 82 | \<default\_case\> | → | Default: \<Announce\> |
| 83 | \<assignment\_statement\> | → | \<data\_type\> identifier \<assign\_op\> \<local\_value\>; |
| 84 | \<inbound\_statement\> | → | Inbound(\<input\> \<inputs\>); |
| 85 | \<input\> | → | Chant literal  |
| 86 | \<inputs\> | → | , identifier |
| 87 | \<announce\_statement\> | → | Announce(\<outputs\>); |
| 88 | \<outputs\> | → | \<output\>\<output\_end\> |
| 89 | \<output\_end\> | → | & \<outputs\> |
| 90 | \<output\_end\> | → | λ |
| 91 | \<output\> | → |  \<global\_value\> |
| 92 | \<output\> | → |  \<local\_value\> |
| 93 | \<output\> | → | \<chant\_concat\> |
| 94 | \<global\_value\> | → | identifier |
| 95 | \<global\_value\> | → | \<literal\> |
| 96 | \<global\_value\> | → | \<expression\> |
| 97 | \<local\_value\> | → | Identifier \<arr\_identifier\> |
| 98 | \<arr\_identifier\> | → | \[\<element\_index\>\] |
| 99 | \<local\_value\> | → | \<expression\> |
| 100 | \<local\_value\> | → | \<func\_call\> |
| 101 | \<local\_value\> | → | \<type\_casted\> |
| 102 | \<local\_value\> | → | \<escape\_sequence\> |
| 103 | \<escape\_sequence\> | → | \\\<esc\_charac\> |
| 104 | \<esc\_charac\> | → | n |
| 105 | \<esc\_charac\> | → | t |
| 106 | \<esc\_charac\> | → | \\ |
| 107 | \<esc\_charac\> | → | " |
| 108 | \<esc\_charac\> | → | @ |
| 109 | \<esc\_charac\> | → | & |
| 110 | \<literal\> | → | Feint literal |
| 111 | \<literal\> | → | Floater literal |
| 112 | \<literal\> | → | Chant literal |
| 113 | \<literal\> | → | Stat literal |
| 114 | \<type\_casted\> | → | \<data\_type\> (\<type\_cast1\>) |
| 115 | \<type\_cast1\> | → | \<literal\> |
| 116 | \<type\_cast1\> | → | identifier |
| 117 | \<assign\_op\> | → | \= |
| 118 | \<assign\_op\> | → | \+= |
| 119 | \<assign\_op\> | → | \-= |
| 120 | \<assign\_op\> | → | \*= |
| 121 | \<assign\_op\> | → | %= |
| 122 | \<assign\_op\> | → | /= |
| 123 | \<arith\_op\> | → | \+ |
| 124 | \<arith\_op\> | → | \- |
| 125 | \<arith\_op\> | → | \* |
| 126 | \<arith\_op\> | → | / |
| 127 | \<arith\_op\> | → | % |
| 128 | \<rel\_op\> | → | \< |
| 129 | \<rel\_op\> | → | \> |
| 130 | \<rel\_op\> | → | \<= |
| 131 | \<rel\_op\> | → | \>= |
| 132 | \<rel\_op\> | → | \<relation\_equality\> |
| 133 | \<relation\_equality\> | → | \== |
| 134 | \<relation\_equality\> | → | \!= |
| 135 | \<log\_op\> | → | AND |
| 136 | \<log\_op\> | → | OR |
| 137 | \<log\_op\> | → | NOT |
| 138 | \<expression\> | → | \<arithmetic\_expr\> |
| 139 | \<expression\> | → | \<relational\_expr\> |
| 140 | \<expression\> | → | \<logical\_expr\> |
| 141 | \<arithmetic\_expr\> | → | \<term\> \<arithexpr\_end\> |
| 142 | \<arithexpr\_end\> | → | \<arith\_op\> \<term\> \<arithexpr\_end\> |
| 143 | \<arithexpr\_end\> | → | λ |
| 144 | \<term\> | → | identifier |
| 145 | \<term\> | → | \<num\_literal\> |
| 146 | \<term\> | → | \<num\_type\_casted\> |
| 147 | \<term\> | → | ( \<arithmetic\_expr\> )  |
| 148 | \<num\_literal\> | → | Feint literal |
| 149 | \<num\_literal\> | → | Floater literal |
| 150 | \<relational\_expr\> | → | \<rel\_operand\> \<rel\_op\> \<rel\_operand\> \<rel\_end\> |
| 151 | \<rel\_end\> | → | \<rel\_op\> \<rel\_operand\> \<rel\_end\> |
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
| 212 | \<forward\_incdec\_operand\> | → | \++ |
| 213 | \<forward\_incdec\_operand\> | → | \-- |
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
| 231 | \<argument\> | → | \<literal\> |
| 232 | \<argument\> |  | Identifier \<array\_id\> |
| 233 |   \<array\_id\> |  | λ |
| 234 |   \<array\_id\> |  | \[\<element\_index\>\] |
| 235 | \<argument\> | → | \<type\_casted\> |

# 