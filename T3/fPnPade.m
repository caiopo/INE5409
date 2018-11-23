function y = fPnPade(n, m, tp)
    a_mac = fCoefMaclaurin(n + m);
    [ap, bp] = fCoefPade(n, m, a_mac);
    for r = 1 : length(tp)
        y(r) = fPnH(n, ap, tp(r)) / fPnH(m, bp, tp(r));
    end
end
