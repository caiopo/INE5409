function [ygreg ymaclaurin ytcheb ypade] = faprox(a, b, x)
    ngreg = 50;
    xgreg = a : (b-a)/ngreg : b;
    yexato = f(x);

    difdiv1 = fdifdiv(ngreg, xgreg, yexato);
    ygreg = fgregoryn(ngreg, xgreg, yexato, difdiv1, x);

    nmac = 15;
    cmac = fcoefMaclaurin(nmac,a,b);
    ymaclaurin = fPnH(nmac, cmac, x);

    ntcheb = 12;
    ytc = fTchebychev(ntcheb, 1, 10);
    ytcheb = fcalculaTchebychev(ntcheb, ytc, x);

    npade = 8;
    mpade = 8;
    ypade = fPnPade(npade, mpade, x);
end

