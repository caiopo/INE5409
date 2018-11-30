function Gm = fIntegralGauss(m, a, b, f)
    t = fCalctm2(m);
    C = fCalcCm2(m,t);

    x = 0.5.*((b-a).*t(m, 1:m) .+ (b+a));
    y = f(x);

    Gm = 0.5*(b-a) * sum(C(m, 1:m).*y(1:m));
end
