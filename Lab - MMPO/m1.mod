
var x1 >= 0; /* żołnierzyki */
var x2 >= 0; /* pociągi */

/* Funkcja celu: */
maximize zysk: 4*x1 + 3*x2;

/* Ograniczenia: */
s.t. Materials : 2*x1 + 4*x2 <= 220;
s.t. Labor     : 3*x1 + 2*x2 <= 150;

end;
