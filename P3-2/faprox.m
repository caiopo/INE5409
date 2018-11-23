function [ygreg ymaclaurin ytcheb ypade] = faprox(a, b, x)
    ngreg = 15;
    xgreg = a : (b-a)/ngreg : b;

    ygreg = fPnGregoryNewton(ngreg, x);

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

