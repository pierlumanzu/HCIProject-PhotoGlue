\ENCODING=ISO-8859-1
\Problem name: miqpex

Maximize
 obj: s_0 + s_1
Subject To
 c1:  s_0 - s_1 <= 0
 c2:  - s_0 + s_1 <= 0
 c3:  - s_0 + s_1 <= 0
 c4:  s_0 - s_1 <= 0
 c5:  x_0 + 960 s_0 <= 10
 c6:  y_0 + 720 s_0 <= 10
 c7:  x_1 + 1280 s_1 <= 10
 c8:  y_1 + 720 s_1 <= 10
 c9:  x_0 + 960 s_0 - x_1 - 10 S_0 <= 0
 c10: - x_0 + x_1 + 1280 s_1 - 10 S_1 <= 0
 c11: y_0 + 720 s_0 - y_1 - 10 S_2 <= 0
 c12: - y_0 + y_1 + 720 s_1 - 10 S_3 <= 0
 c13: S_0 + S_1 + S_2 + S_3 <= 3
Bounds
 0 <= S_0 <= 1
 0 <= S_1 <= 1
 0 <= S_2 <= 1
 0 <= S_3 <= 1
Binaries
 S_0  S_1  S_2  S_3 
End
