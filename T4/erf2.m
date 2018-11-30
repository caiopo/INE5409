function y = erf2(x)
    if x == 0
        y = [0 0 0];
        return
    end

    f = @(t) exp(-(t .* t));

    a = 0;
    b = x;

    T =  fIntegralTrapezios(2**18, a, b, f);

    m = 10;
    G = fIntegralGauss(m, a, b, f);

    S = fIntegralSimpson(2**11, a, b, f);

    y(1) = (2/sqrt(pi)) * T;
    y(2) = (2/sqrt(pi)) * G;
    y(3) = (2/sqrt(pi)) * S;
end
