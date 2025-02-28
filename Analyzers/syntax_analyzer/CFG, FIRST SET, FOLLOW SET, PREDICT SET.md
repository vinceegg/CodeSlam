# **CONTEXT FREE GRAMMAR** 

# **SD**

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

# H